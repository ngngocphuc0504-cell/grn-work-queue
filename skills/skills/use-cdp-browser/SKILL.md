---
name: use-cdp-browser
description: Use to open, inspect, verify, or operate Chrome/Edge through CDP, especially visible logged-in sessions for screenshots, DOM capture, and safe UI clicks.
---

# Use CDP Browser

## Purpose

Manage browser sessions that are both user-visible and machine-controllable through Chrome DevTools Protocol. Use this to let the user log in manually, then let Codex inspect pages, capture evidence, and click safe controls without handling passwords, cookies, or session tokens.

## Session Types

- **Headless CDP session**: Chrome has `--headless` and `--remote-debugging-port`. Codex can control it, but the user cannot see or log in through the window.
- **CDP-controlled visible browser session**: Chrome does not have `--headless`, has `--remote-debugging-port`, and opens a normal visible window. This is the preferred session for logged-in reference apps.
- **Normal browser session**: Chrome has no remote debugging port. The user can browse, but Codex cannot reliably inspect or click through CDP.

Use a separate `--user-data-dir` for each CDP session so it does not share cookies with the user's normal browser profile.

## Open A Visible Session

Prefer the bundled script on Windows:

```powershell
& "<skill-dir>\scripts\open-visible-chrome.ps1" `
  -Port 9226 `
  -Url "https://app.example.com/" `
  -Profile "C:\ChromeDebugExample9226"
```

If the script is not available, launch Chrome manually with:

```powershell
Start-Process -FilePath "$env:LocalAppData\Google\Chrome\Application\chrome.exe" -ArgumentList @(
  "--new-window",
  "--remote-debugging-port=9226",
  "--remote-debugging-address=127.0.0.1",
  "--remote-allow-origins=*",
  "--user-data-dir=C:\ChromeDebugExample9226",
  "--no-first-run",
  "--no-default-browser-check",
  "--window-size=1368,900",
  "https://app.example.com/"
)
```

If Chrome is already running with the default profile, opening a debug window can be redirected to that existing instance and lose the debug flags. Fix this by using a short, separate profile path such as `C:\ChromeDebug<name><port>`.

## Verify The Session

Check the DevTools endpoint before claiming the browser is ready:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:9226/json/version"
Invoke-RestMethod -Uri "http://127.0.0.1:9226/json/list"
```

To classify a live session, read the owner process command line:

```powershell
Get-CimInstance Win32_Process -Filter "name = 'chrome.exe'" |
  Where-Object { $_.CommandLine -match 'remote-debugging-port=9226' } |
  Select-Object ProcessId,CommandLine
```

Report the exact classification:

- `--headless` present: headless CDP session.
- `--remote-debugging-port` present and `--headless` absent: CDP-controlled visible browser session.
- no matching remote debugging process: normal browser session or failed launch.

## Login Rule

Never ask for passwords, cookies, tokens, or session storage. The user logs in manually in the visible browser. After login, verify through `/json/list` that the target tab title and URL are correct.

Separate CDP profiles normally do not affect the user's normal Chrome login. They can still be logged out if the app revokes sessions server-side or the user chooses a "log out all sessions" action.

## Safe Interaction

Before clicking, inspect visible controls and choose the lowest-risk target:

1. Read `document.title`, `location.href`, and visible buttons/links.
2. Prefer menus, filters, dropdowns, tabs, view switches, and non-submitting popovers.
3. Avoid publish/send/schedule/delete/logout/billing/account actions.
4. If a click opens a confirmation modal, capture it and dismiss it.
5. After the click, verify a harmless state change such as `aria-expanded`, focus text, menu role, dialog role, URL, or page title.

Minimal Node pattern:

```javascript
const tabs = await fetch("http://127.0.0.1:9226/json/list").then(r => r.json());
const page = tabs.find(t => t.type === "page");
const ws = new WebSocket(page.webSocketDebuggerUrl);
```

Use CDP `Runtime.evaluate` for DOM inspection and `Input.dispatchMouseEvent` for clicks. Record the exact clicked label, before/after state, and visible menu/dialog text.

## Capture Use

For clone workflows, use the visible CDP session as source evidence after the user logs in. Capture screenshots, DOM text, interactive inventories, and opened menu states. Store artifacts under the project workflow folder, for example `.agent-workflows/{slug}/source/`.

When working with `clone-reference-ui`, use that skill for the full source-to-target workflow and this skill for the browser session setup, verification, and safe CDP interaction rules.
