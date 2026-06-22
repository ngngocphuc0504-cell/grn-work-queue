#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
const getArg = (name, fallback = undefined) => {
  const index = args.indexOf(`--${name}`);
  return index >= 0 ? args[index + 1] : fallback;
};

const port = Number(getArg('port', '9223'));
const url = getArg('url');
const match = getArg('match');
const outDir = path.resolve(getArg('out', '.agent-workflows/interactive-scan'));
const name = getArg('name', 'interactive-scan');
const viewport = getArg('viewport', '1440x900');
const maxClicks = Number(getArg('max-clicks', '80'));
const [width, height] = viewport.split('x').map((value) => Number(value));

const unsafePattern = /\b(delete|remove account|disconnect|logout|log out|publish|schedule|send|boost|billing|payment|confirm|permanently|archive|trash|close composer|minimize composer|open compose in new window|close)\b/i;

fs.mkdirSync(path.join(outDir, 'screenshots'), { recursive: true });
fs.mkdirSync(path.join(outDir, 'interactive'), { recursive: true });
fs.mkdirSync(path.join(outDir, 'dom'), { recursive: true });

const tabs = await fetch(`http://127.0.0.1:${port}/json/list`).then((response) => response.json());
let tab = match
  ? tabs.find((item) => item.url?.includes(match) || item.title?.includes(match))
  : tabs.find((item) => item.type === 'page');

if (!tab && url) {
  tab = tabs.find((item) => item.type === 'page');
}

if (!tab?.webSocketDebuggerUrl) {
  throw new Error(`No debuggable page found on port ${port}`);
}

const ws = new WebSocket(tab.webSocketDebuggerUrl);
let id = 0;
const pending = new Map();

function send(method, params = {}) {
  const messageId = ++id;
  ws.send(JSON.stringify({ id: messageId, method, params }));
  return new Promise((resolve, reject) => {
    pending.set(messageId, { resolve, reject });
  });
}

ws.onmessage = (event) => {
  const message = JSON.parse(event.data);
  if (!message.id || !pending.has(message.id)) return;
  const waiter = pending.get(message.id);
  pending.delete(message.id);
  if (message.error) waiter.reject(new Error(JSON.stringify(message.error)));
  else waiter.resolve(message.result);
};

await new Promise((resolve) => {
  ws.onopen = resolve;
});

await send('Page.enable');
await send('Runtime.enable');
await send('Emulation.setDeviceMetricsOverride', {
  width,
  height,
  deviceScaleFactor: 1,
  mobile: false,
});

if (url) {
  await send('Page.navigate', { url });
  await new Promise((resolve) => setTimeout(resolve, 1600));
}

const startUrl = await evaluate('location.href');

async function screenshot(fileName) {
  const result = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  fs.writeFileSync(path.join(outDir, 'screenshots', fileName), Buffer.from(result.data, 'base64'));
}

async function evaluate(expression) {
  const result = await send('Runtime.evaluate', {
    expression,
    awaitPromise: true,
    returnByValue: true,
  });
  return result.result?.value;
}

const baseline = await evaluate(`(() => {
  let nextId = 0;
  const visible = (el) => {
    const rect = el.getBoundingClientRect();
    const style = getComputedStyle(el);
    return rect.width > 1 && rect.height > 1 && style.visibility !== 'hidden' && style.display !== 'none';
  };
  return [...document.querySelectorAll('button,a,input,textarea,select,[role="button"],[role="tab"],[role="menuitem"],[aria-haspopup],[aria-label]')]
    .filter(visible)
    .map((el) => {
      const rect = el.getBoundingClientRect();
      const scanId = 'scan-' + (++nextId);
      el.setAttribute('data-scan-id', scanId);
      return {
        scanId,
        tag: el.tagName,
        role: el.getAttribute('role') || '',
        label: el.getAttribute('aria-label') || el.getAttribute('title') || el.innerText || el.value || '',
        disabled: Boolean(el.disabled) || el.getAttribute('aria-disabled') === 'true',
        selected: el.getAttribute('aria-selected') || el.checked || false,
        rect: { x: Math.round(rect.x), y: Math.round(rect.y), width: Math.round(rect.width), height: Math.round(rect.height) }
      };
    })
    .sort((a, b) => a.rect.y - b.rect.y || a.rect.x - b.rect.x);
})()`);

fs.writeFileSync(path.join(outDir, 'interactive', `${name}-candidates.json`), JSON.stringify(baseline, null, 2));
fs.writeFileSync(path.join(outDir, 'dom', `${name}-baseline.txt`), await evaluate('document.body.innerText'));
await screenshot(`${name}-baseline.png`);

const clicked = [];
for (const candidate of baseline.slice(0, maxClicks)) {
  const label = String(candidate.label || '').trim();
  if (!label || candidate.disabled || unsafePattern.test(label)) {
    clicked.push({ ...candidate, skipped: true, reason: candidate.disabled ? 'disabled' : 'unsafe-or-empty-label' });
    continue;
  }

  const result = await evaluate(`(async () => {
    const el = document.querySelector('[data-scan-id="${candidate.scanId}"]');
    if (!el) return { clicked: false, reason: 'element-not-found' };
    el.scrollIntoView({ block: 'center', inline: 'center' });
    await new Promise((resolve) => setTimeout(resolve, 100));
    el.click();
    await new Promise((resolve) => setTimeout(resolve, 350));
    const openText = [...document.querySelectorAll('[role="menu"],[role="listbox"],.ant-popover,.ant-dropdown,.ant-modal,.ant-drawer')]
      .map((node) => node.innerText || node.textContent || '')
      .filter(Boolean)
      .join('\\n---\\n');
    return {
      clicked: true,
      activeElement: document.activeElement?.tagName || '',
      bodyText: document.body.innerText.slice(0, 5000),
      openText: openText.slice(0, 5000)
    };
  })()`);

  const safeName = `${String(clicked.length + 1).padStart(3, '0')}-${candidate.scanId}.png`;
  await screenshot(safeName);
  clicked.push({ ...candidate, result, screenshot: `screenshots/${safeName}` });
  const currentUrl = await evaluate('location.href');
  if (url && currentUrl !== startUrl) {
    await send('Page.navigate', { url: startUrl });
    await new Promise((resolve) => setTimeout(resolve, 900));
  }
  await send('Input.dispatchKeyEvent', { type: 'keyDown', key: 'Escape', code: 'Escape', windowsVirtualKeyCode: 27 });
  await send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'Escape', code: 'Escape', windowsVirtualKeyCode: 27 });
  await new Promise((resolve) => setTimeout(resolve, 150));
}

fs.writeFileSync(path.join(outDir, 'interactive', `${name}-clicked.json`), JSON.stringify(clicked, null, 2));
ws.close();

console.log(JSON.stringify({
  status: 'ok',
  outDir,
  candidates: baseline.length,
  clicked: clicked.filter((item) => item.result?.clicked).length,
  skipped: clicked.filter((item) => item.skipped).length,
}, null, 2));
