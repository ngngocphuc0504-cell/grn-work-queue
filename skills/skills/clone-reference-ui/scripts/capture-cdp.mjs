#!/usr/bin/env node

import fs from "node:fs";
import http from "node:http";
import path from "node:path";

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i += 1) {
    const item = argv[i];
    if (!item.startsWith("--")) continue;
    const key = item.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith("--")) {
      args[key] = true;
    } else {
      args[key] = next;
      i += 1;
    }
  }
  return args;
}

function getJson(url) {
  return new Promise((resolve, reject) => {
    http
      .get(url, (res) => {
        let data = "";
        res.on("data", (chunk) => {
          data += chunk;
        });
        res.on("end", () => {
          try {
            resolve(JSON.parse(data));
          } catch (error) {
            reject(error);
          }
        });
      })
      .on("error", reject);
  });
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function writeJson(file, data) {
  ensureDir(path.dirname(file));
  fs.writeFileSync(file, `${JSON.stringify(data, null, 2)}\n`, "utf8");
}

function writeText(file, data) {
  ensureDir(path.dirname(file));
  fs.writeFileSync(file, data, "utf8");
}

function normalizeName(value) {
  return String(value || "capture")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80) || "capture";
}

function parseViewport(value) {
  const fallback = { width: 1920, height: 900 };
  if (!value) return fallback;
  const match = String(value).match(/^(\d+)x(\d+)$/i);
  if (!match) return fallback;
  return {
    width: Number(match[1]),
    height: Number(match[2]),
  };
}

class CdpClient {
  constructor(wsUrl) {
    this.wsUrl = wsUrl;
    this.nextId = 1;
    this.pending = new Map();
    this.ws = null;
  }

  async connect() {
    this.ws = new WebSocket(this.wsUrl);
    this.ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      if (message.id && this.pending.has(message.id)) {
        const { resolve, reject } = this.pending.get(message.id);
        this.pending.delete(message.id);
        if (message.error) reject(new Error(JSON.stringify(message.error)));
        else resolve(message);
      }
    };
    await new Promise((resolve, reject) => {
      this.ws.onopen = resolve;
      this.ws.onerror = reject;
    });
  }

  send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = this.nextId;
      this.nextId += 1;
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }

  close() {
    if (this.ws) this.ws.close();
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const port = args.port || "9223";
  const outDir = path.resolve(process.cwd(), args.out || ".agent-workflows/reference-ui/source");
  const name = normalizeName(args.name || "capture");
  const match = args.match ? String(args.match) : "";
  const targetUrl = args.url ? String(args.url) : "";
  const waitMs = Number(args.wait || 1000);
  const viewport = parseViewport(args.viewport);

  const tabs = await getJson(`http://127.0.0.1:${port}/json/list`);
  const pages = tabs.filter((tab) => tab.type === "page" && tab.webSocketDebuggerUrl);
  let page = null;

  if (match) {
    page = pages.find((tab) => tab.url.includes(match) || tab.title.includes(match));
  }
  if (!page && targetUrl) {
    page = pages[0];
  }
  if (!page) {
    page = pages[0];
  }
  if (!page) {
    throw new Error(`No debuggable page found on port ${port}`);
  }

  const client = new CdpClient(page.webSocketDebuggerUrl);
  await client.connect();

  try {
    await client.send("Page.enable");
    await client.send("Runtime.enable");
    await client.send("Accessibility.enable").catch(() => null);
    await client.send("Emulation.setDeviceMetricsOverride", {
      width: viewport.width,
      height: viewport.height,
      deviceScaleFactor: 1,
      mobile: false,
    });

    if (targetUrl) {
      await client.send("Page.navigate", { url: targetUrl });
      await new Promise((resolve) => setTimeout(resolve, Math.max(waitMs, 2000)));
    } else {
      await client.send("Runtime.evaluate", { expression: "window.scrollTo(0, 0)" });
      await new Promise((resolve) => setTimeout(resolve, waitMs));
    }

    const titleResult = await client.send("Runtime.evaluate", {
      expression: "document.title",
      returnByValue: true,
    });
    const urlResult = await client.send("Runtime.evaluate", {
      expression: "location.href",
      returnByValue: true,
    });
    const textResult = await client.send("Runtime.evaluate", {
      expression: "document.body ? document.body.innerText : ''",
      returnByValue: true,
    });
    const interactiveResult = await client.send("Runtime.evaluate", {
      expression: `(() => {
        const selector = [
          'button',
          'a',
          'input',
          'textarea',
          'select',
          '[role="button"]',
          '[role="menuitem"]',
          '[role="tab"]',
          '[role="switch"]',
          '[aria-label]',
          '[tabindex]'
        ].join(',');
        return [...document.querySelectorAll(selector)].slice(0, 1000).map((el, index) => {
          const rect = el.getBoundingClientRect();
          return {
            index,
            tag: el.tagName,
            role: el.getAttribute('role') || '',
            type: el.getAttribute('type') || '',
            ariaLabel: el.getAttribute('aria-label') || '',
            title: el.getAttribute('title') || '',
            text: (el.innerText || el.value || '').trim().slice(0, 300),
            disabled: Boolean(el.disabled) || el.getAttribute('aria-disabled') === 'true',
            href: el.href || '',
            visible: rect.width > 0 && rect.height > 0,
            rect: {
              x: Math.round(rect.x),
              y: Math.round(rect.y),
              width: Math.round(rect.width),
              height: Math.round(rect.height)
            }
          };
        });
      })()`,
      returnByValue: true,
    });
    const overflowResult = await client.send("Runtime.evaluate", {
      expression: `(() => ({
        documentWidth: document.documentElement.scrollWidth,
        viewportWidth: document.documentElement.clientWidth,
        documentHeight: document.documentElement.scrollHeight,
        viewportHeight: document.documentElement.clientHeight,
        hasHorizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
      }))()`,
      returnByValue: true,
    });
    const screenshotResult = await client.send("Page.captureScreenshot", {
      format: "png",
      fromSurface: true,
      captureBeyondViewport: false,
    });
    const axResult = await client.send("Accessibility.getFullAXTree").catch(() => null);

    const screenshotDir = path.join(outDir, "screenshots");
    const domDir = path.join(outDir, "dom");
    const interactiveDir = path.join(outDir, "interactive");
    const accessibilityDir = path.join(outDir, "accessibility");
    ensureDir(screenshotDir);
    ensureDir(domDir);
    ensureDir(interactiveDir);
    ensureDir(accessibilityDir);

    const screenshotPath = path.join(screenshotDir, `${name}.png`);
    fs.writeFileSync(screenshotPath, Buffer.from(screenshotResult.result.data, "base64"));

    const title = titleResult.result.result.value || "";
    const finalUrl = urlResult.result.result.value || "";
    const bodyText = textResult.result.result.value || "";
    const interactive = interactiveResult.result.result.value || [];
    const overflow = overflowResult.result.result.value || {};
    const accessibility = axResult ? axResult.result.nodes || [] : [];

    writeText(path.join(domDir, `${name}.txt`), bodyText);
    writeJson(path.join(interactiveDir, `${name}.json`), interactive);
    writeJson(path.join(accessibilityDir, `${name}.json`), accessibility);

    const manifestPath = path.join(outDir, "capture-manifest.json");
    let manifest = { captures: [] };
    if (fs.existsSync(manifestPath)) {
      try {
        manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
      } catch {
        manifest = { captures: [] };
      }
    }
    manifest.captures.push({
      name,
      capturedAt: new Date().toISOString(),
      title,
      url: finalUrl,
      viewport,
      screenshot: path.relative(outDir, screenshotPath).replaceAll("\\", "/"),
      domText: `dom/${name}.txt`,
      interactive: `interactive/${name}.json`,
      accessibility: `accessibility/${name}.json`,
      overflow,
    });
    writeJson(manifestPath, manifest);

    console.log(JSON.stringify({
      ok: true,
      title,
      url: finalUrl,
      outDir,
      screenshot: screenshotPath,
      interactiveCount: interactive.length,
      hasHorizontalOverflow: Boolean(overflow.hasHorizontalOverflow),
    }, null, 2));
  } finally {
    client.close();
  }
}

main().catch((error) => {
  console.error(error.stack || error.message);
  process.exit(1);
});

