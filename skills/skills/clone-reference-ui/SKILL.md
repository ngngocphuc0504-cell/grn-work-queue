---
name: clone-reference-ui
description: Use to rebuild a logged-in reference web UI locally: capture screenshots/DOM, brief the target, implement, browser-QA, compare source vs target, and fix visible gaps safely.
---

# Clone Reference UI

## Purpose

Turn a reference web UI into a controlled local rebuild workflow:

1. Capture reference artifacts from a browser the user logged into.
2. Convert those artifacts into a source brief.
3. Build the equivalent target UI in the local repo.
4. QA the target in browser.
5. Run an independent difference scan from top-to-bottom and left-to-right.
6. Compare source vs target and write a gap report.
7. Fix the next visible gap batch and repeat.

Do not ask for passwords, cookies, or session tokens. The user logs in manually in a browser profile; use Chrome DevTools Protocol only after login.

## When Triggered

Use this skill when the user asks to:

- clone a page from a logged-in SaaS/app into a local project
- capture source screenshots or DOM from a reference app
- create a UI/feature brief from a reference page
- compare a target implementation against a reference UI
- run a source-to-target gap analysis for a UI rebuild
- build a local agent/workflow for capture -> brief -> code -> QA -> gap -> fix

For pure code implementation, combine with `build-frontend`. For source/target comparison, combine with `analyze-gap`. For browser QA, combine with `test-website`.

## Operating Rules

- Source artifacts are evidence. Do not rely on memory when a screenshot/DOM capture can be made.
- Capture states before coding. At minimum capture the default page, key filters/menus, detail panels/modals, alternate view modes, and every toolbar/editor icon that opens a menu, popover, upload chooser, or secondary action list.
- Rebuild functional equivalence, not brand theft. Bring over all source-visible feature behavior, content structure, labels, states, validation, menu choices, empty states, and workflow affordances unless the user explicitly narrows scope.
- Adapt implementation to the target project's existing design system and component library. If the target already uses Ant Design, implement cloned UI with Ant Design components first (`Button`, `Input`, `Select`, `Dropdown`, `Menu`, `Tabs`, `Modal`, `Drawer`, `Card`, `List`, `Table`, `Form`, `Switch`, `Checkbox`, `Badge`, `Avatar`, `Tooltip`, `Popover`, `Typography`, `Empty`, `Tag`) and use CSS only for layout, spacing, and source-specific visual treatment that AntD does not provide.
- Do not replace Ant Design primitives with raw `button`, `input`, `select`, or hand-rolled modal/dropdown/list controls unless a source interaction cannot be expressed safely with AntD. When raw elements are unavoidable, document why in implementation notes.
- Store artifacts under `.agent-workflows/{slug}/`.
- Keep every loop small: fix the highest-impact visible gaps first.
- Always verify render path in target code. A complete component that is not rendered is still a gap.
- Interaction parity is part of layout parity. Small icon buttons, overflow buttons, split buttons, upload buttons, media/library buttons, and disabled menu items must be captured and rebuilt when visible in the source workflow.
- Use a dedicated Difference Scanner Agent for long or high-fidelity clones. This agent runs independently from the Code Agent, scans the source page in visual order, and feeds missing areas back to the main implementation loop.

## Workflow

### Step 1: Source Capture

If the reference app requires login:

1. Open a separate Chrome/Edge profile with remote debugging.
2. Ask the user to log in manually.
3. Verify the tab through `http://127.0.0.1:{port}/json/list`.
4. Capture source artifacts using `scripts/capture-cdp.mjs`.

Default artifact path:

```text
.agent-workflows/{slug}/source/
```

Capture at least:

- screenshot at baseline viewport
- `document.body.innerText`
- interactive element inventory
- accessibility tree when available
- manifest with URL, title, viewport, timestamp

For icon-driven toolbars and composers, also capture:

- each toolbar icon's opened state, including upload/media/source menus
- menu grouping, item order, enabled/disabled state, labels, icons, and separators
- hover/focus state when it reveals affordances such as overflow actions or remove buttons
- the close/dismiss behavior for each popover or menu

For detailed state coverage and prompt templates, read `references/workflow.md`.

### Step 2: Source Brief

Create:

```text
.agent-workflows/{slug}/brief/SOURCE-BRIEF.md
```

The brief must include:

- page purpose
- layout inventory
- component inventory
- interaction matrix
- inferred data model
- visual rules to adapt, not copy
- acceptance criteria
- source coverage gaps if screenshots/states are missing

Do not write code in this step.

### Step 3: Difference Scanner Agent

Run this role in parallel with the main implementation flow when the user asks for near-exact parity or when the page is long.

Responsibilities:

1. Scan the source page from top-to-bottom.
2. Inside each horizontal band, scan from left-to-right.
3. Continue through every scroll slice until the bottom of the page or scrollable panel is reached.
4. Repeat for nested scroll containers such as composer panels, right previews, drawers, menus, and popovers.
5. Click every safe visible element that behaves like a function, filter, button, tab, menu, dropdown, toolbar icon, upload source, overflow action, toggle, checkbox, radio group, profile/channel selector, creative-type selector, or view switch.
6. Capture the opened state after each click, including menus, popovers, drawers, validation changes, disabled options, hover-only affordances, and changed layout.
7. Restore the prior state when possible before continuing to the next element.
8. Record every visible section, control, label, icon, menu item, disabled item, badge, selected state, empty state, validation state, platform-specific state, creative-specific state, and media affordance.
9. Feed only findings to the main Code Agent or Fix Loop Controller. Do not implement code in this role.

Interactive safety:

- Do not click destructive, irreversible, outbound, billing, publish/send/schedule, delete, disconnect, logout, or account-management actions unless the user explicitly authorizes it.
- Prefer opening menus, popovers, filters, and panels over confirming actions.
- If a click opens a confirmation modal, capture it and dismiss it.
- If a click changes a draft form state, record the change and continue only when the state can be reset or reproduced.
- For source apps, never submit a real post, schedule a real post, upload private files, or change account settings.

Default output:

```text
.agent-workflows/{slug}/reports/{SLUG}-DIFFERENCE-SCAN.md
```

The report must include:

- scan order and viewport slices covered
- source evidence screenshots or DOM files
- target evidence when available
- missing or mismatched areas
- interaction matrix for clicked elements and resulting states
- platform/channel matrix for selected profile combinations when applicable
- creative-type matrix for text/image/video/link variants when applicable
- uncertainty notes for any area that could not be inspected
- next feed items for the Code Agent, ordered by visual position

Treat any unscanned area as unknown, never as matched.

### Step 4: Build Target

Read the local project instructions first:

1. `PROJECT-INSTRUCTIONS.md`, `CLAUDE.md`, `AGENTS.md`, or equivalent
2. `DESIGN.md`
3. `LAYOUT-BLUEPRINT.md`
4. relevant existing source files

Then implement the page using local patterns. If backend/API is missing, create a clear mock data adapter and keep it isolated.

Before editing code, identify the target UI library from `package.json` and existing pages. If Ant Design is present, map the source feature inventory to AntD primitives and preserve the source functionality/content while keeping local AntD styling consistency.

Create:

```text
.agent-workflows/{slug}/target/IMPLEMENTATION-NOTES.md
```

### Step 5: Target QA

Run the target app locally, open the page in browser, and capture target artifacts using the same viewport as source.

Create:

```text
.agent-workflows/{slug}/target/screenshots/
.agent-workflows/{slug}/target/QA-REPORT.md
```

QA must cover:

- page loads and is not blank
- no obvious overlap or unreadable text
- main toolbar works
- filters/dropdowns open and close
- toolbar/editor icon menus open and expose the same option groups and disabled states as the reference
- view modes/tabs switch or clearly communicate disabled state
- detail drawers/modals/cards work
- no unintended horizontal page overflow at the baseline viewport

### Step 6: Gap Analysis

Create:

```text
.agent-workflows/{slug}/reports/{SLUG}-GAP-ANALYSIS.md
```

Compare:

- source screenshots vs target screenshots
- source DOM/interactive inventory vs target UI
- Difference Scanner Agent report vs target implementation
- source brief vs target implementation
- target render path in code
- each captured interaction state vs the equivalent target state, including popovers from icon buttons

Classify findings:

- Critical: missing core layout, state, or behavior
- Medium: simplified or partial feature
- Minor: visual polish, copy, spacing, naming, low-risk mismatch
- Match: verified equivalent behavior or layout

End the report with a "Next Fix Batch" of no more than 5 items.

### Step 7: Fix Loop

Pick one small batch from the gap report, implement, QA again, then update the gap report.

Stop when:

- no Critical gaps remain
- remaining Medium gaps are accepted or backlogged
- target satisfies the source brief acceptance criteria

## Script Usage

Capture a logged-in reference tab:

```powershell
node "C:\Users\Hai Son\.codex\skills\clone-reference-ui\scripts\capture-cdp.mjs" `
  --port 9223 `
  --match "/publishing/calendar" `
  --out ".agent-workflows/sprout-calendar/source" `
  --viewport 1920x900 `
  --name "month-expanded"
```

Capture a target tab from another debug browser:

```powershell
node "C:\Users\Hai Son\.codex\skills\clone-reference-ui\scripts\capture-cdp.mjs" `
  --port 9224 `
  --url "http://localhost:3000/publishing/calendar" `
  --out ".agent-workflows/sprout-calendar/target" `
  --viewport 1920x900 `
  --name "target-calendar"
```

If the script cannot find a matching tab, inspect:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:9223/json/list"
```

Interactively scan safe controls on a source or target tab:

```powershell
node "C:\Users\Hai Son\.codex\skills\clone-reference-ui\scripts\interactive-scan-cdp.mjs" `
  --port 9224 `
  --url "http://localhost:3000/publishing/new-post" `
  --out ".agent-workflows/sprout-new-post/target/interactive-scan" `
  --viewport 1368x900 `
  --name "target-new-post" `
  --max-clicks 80
```

Use interactive scan output as evidence, not as an automatic implementation decision. The Code Agent still decides the smallest safe fix batch.

## Output Contract

Every run should leave a readable trail:

```text
.agent-workflows/{slug}/
  source/
  brief/SOURCE-BRIEF.md
  target/IMPLEMENTATION-NOTES.md
  target/QA-REPORT.md
  reports/{SLUG}-GAP-ANALYSIS.md
```

Final response should summarize:

- artifacts created
- implementation files changed
- QA result
- remaining Critical/Medium/Minor gaps
- next recommended fix batch
