---
name: ugc-delivery-agent
description: Use for UGC Website frontend delivery: read project docs, choose one small next step, implement safe UI changes, verify behavior, sync docs, and report roadmap status.
---

# UGC Delivery Agent

## Purpose

Use this skill for full-lifecycle frontend delivery work in `UGC Website`:

- bootstrap from the live UGC source of truth before doing work
- turn a high-level goal into one small executable next step
- keep design, layout, and shared shell behavior consistent
- implement only frontend-safe scope for BE handoff
- verify before claiming progress
- sync the right owner docs after verified truth changes
- report progress in roadmap context for a non-technical PM

Default repo:

- `C:\Users\Hai Son\Desktop\Claude\UGC website\ugc-website`

## Audience And Default Promise

- The primary user is a non-technical PM working with a team.
- Default ownership is frontend delivery and handoff quality, not backend implementation ownership.
- The user can state only the goal; the agent must figure out the next small step from project truth.
- The agent should keep moving until blocked by:
  - source-of-truth conflict
  - required product decision
  - unsafe repro or verification ambiguity

## Required Read Order

Read only what is needed, in this order:

1. [UGC Website](https://wiki.odp.garena.vn/doc/ugc-website-3mC4RHXzh1)
2. [10 Canonical — Project Overview](https://wiki.odp.garena.vn/doc/10-canonical-project-overview-4bugimqbPv)
3. [11 Canonical — Module Catalog](https://wiki.odp.garena.vn/doc/11-canonical-module-catalog-Nn0J4FW1Jo)
4. [20 Operational — Current State](https://wiki.odp.garena.vn/doc/20-operational-current-state-jtYSCjfvHb) when summarizing roadmap, big picture, or milestone
5. the task-specific owner page from the module catalog
6. [12 Canonical — Technical Hub](https://wiki.odp.garena.vn/doc/12-canonical-technical-hub-Y0Ns15SuoZ) or [13 Canonical — Data & Schema](https://wiki.odp.garena.vn/doc/13-canonical-data-schema-6ITHbnDL8V) when implementation or contract detail is needed
7. local repo routing docs:
   - `docs/README.md`
   - `AGENTS.md`
   - `docs/execution-plan.md`
   - `docs/agent-workflow/*` only for execution scaffolding
8. verified repo truth in:
   - `package.json`
   - `src/routes/appRoutes.jsx`
   - shared shell and tokens
   - the touched `src/pages/*` and nearby shared components

## Source Of Truth Rules

- Outline owner pages own product truth.
- Verified repo files own current implementation truth.
- Local docs under `docs/agent-workflow/` own execution scaffolding only.
- Do not let stale local notes override current Outline owner docs or verified repo behavior.
- If local notes and verified repo behavior conflict, update the owner doc instead of keeping parallel truth.

## Task Routing

- Roadmap, current focus, milestone, blocker, next step:
  - `20 Operational — Current State`
  - `AGENTS.md`
  - `docs/execution-plan.md`
  - `docs/agent-workflow/next-slice-source-of-truth-repair.md`
- Module boundary and business behavior:
  - the relevant module owner page from `11 Canonical — Module Catalog`
- Technical or contract detail:
  - `12 Canonical — Technical Hub`
  - `13 Canonical — Data & Schema`
- Local execution scaffolding:
  - `docs/agent-workflow/*`
- Layout and page anatomy:
  - `LAYOUT-BLUEPRINT.md`

## Required Skill Routing

Use these skills when relevant instead of improvising their role:

- `build-frontend` for implementation
- `design-uiux` for page-level or feature-level UX decisions
- `govern-layout` when shell, top slot, page anatomy, or layout consistency is touched
- `design-system-antd` when tokens, component states, or system-level UI consistency matters
- `test-website` for operator-visible browser verification when the environment supports it
- `document-delivery` for durable doc updates
- `work-with-outline` for Outline reads and writes
- `sync-task-status` for local status or build-history sync after meaningful progress
- `review-frontend` when the task is primarily audit or polish rather than direct feature delivery

Do not call every specialist skill on every task. Route only to the ones the slice truly needs.

## Default Delivery Pipeline

### 1. Resolve source of truth first

Before planning or coding, identify:

- the user goal
- the active roadmap or lane
- the touched module or route
- the likely repo area
- fact vs assumption when uncertainty exists

Do not start coding before the route is explicit.

### 2. Summarize the current picture

For every substantial session, summarize:

- `Roadmap`
- `Big Picture`
- `Milestone`

Use current UGC docs, not stale memory.

### 3. Choose one default next step

- Break broad goals into a single executable slice.
- Prefer the current local `next-slice` owner when the user asks to continue generally.
- If the user asked for a specific route or bug, choose the smallest slice that advances that exact goal safely.
- Do not fan out into multiple parallel implementation tracks unless the user explicitly changes scope.

### 4. Create or update the minimum local execution artifacts

When the work is substantial, keep the local execution loop aligned:

- session context packet
- task slice card
- role / data / language checklist when shared contract or visible behavior changes
- verification notes in the active slice file

Do not duplicate Outline roadmap truth inside local slice files.

### 5. Repro or add the smallest useful check first

- Reproduce the issue or confirm the target behavior first.
- Add or update the smallest useful check before larger edits when possible.
- Prefer behavior-level checks over speculative rewrites.

### 6. Implement only the scoped slice

- Stay within frontend delivery and BE handoff scope.
- Do not invent backend contracts beyond what the frontend handoff requires.
- Do not mix unrelated cleanup into the same slice.

### 7. Verify before claiming progress

Use `npm.cmd` on Windows.

Minimum baseline:

```bash
npm.cmd run build
```

UGC encoding regression check:

- When a slice edits UGC source files that contain Vietnamese, emoji, arrows, or typographic punctuation, verify the touched files with a UTF-8-aware scan before browser handoff.
- Never trust PowerShell-rendered text as source truth for non-ASCII strings; it can display correct bytes as mojibake and can also corrupt files if piped back through `Set-Content`.
- Never rewrite UGC `.js`, `.jsx`, `.ts`, `.tsx`, `.md`, or `.json` files with `Get-Content | Set-Content`.
- Use `apply_patch` for targeted edits. If encoding repair is unavoidable, use an explicit UTF-8 script and immediately scan for mojibake byte-like markers such as `Ã`, `Ä`, `Â`, `â€”`, `â†`, `âš`, `ðŸ`, and `ï¿½`.
- After any touched-file edit in this repo, run `npm.cmd run audit:encoding-regression -- <relative file paths>` and treat any hit as a hard failure before claiming progress.
- For high-risk slices, always include these files in the audit even if they are only imported indirectly:
  - `src/pages/Creator/CreatorDrawer.jsx`
  - `src/pages/System/index.jsx`
  - `src/pages/UGCConfig/workflowShared.js`
- If a visible page shows mojibake, inspect imported data modules as well as the page component. For UGC Config Workflow, check `src/pages/UGCConfig/workflowShared.js` first.

If the slice touches visible operator behavior, also require the matching smoke flow from:

- `docs/agent-workflow/operator-smoke-flows.md`

If the environment supports browser QA and the slice is operator-visible or visually sensitive, prefer using `test-website` in addition to local smoke notes.

### 8. Sync docs if truth changed

After verified truth changes:

- Outline owner pages first
- local workflow docs only if execution truth, next-slice selection, or verification truth changed

Do not mark docs as synced if they are still pending. State exact pending docs instead.

### 9. End with one concrete next step

- Always end substantial sessions with exactly one default `Next Step`.
- That step must be small, specific, and executable in the next turn.
- Do not end with a vague list of optional ideas.

## Frontend Quality Guardrails

- Do not ship UI changes without checking layout consistency against existing shell and page anatomy.
- Do not leave spacing, alignment, filter bar, tab, drawer, modal, or top-slot behavior inconsistent with neighboring routes.
- If a task touches shared UI surfaces such as shell, table, filter, tabs, modal, or drawer, verification must include the matching smoke flow.
- If the task is visually sensitive, run a design or layout audit step before finalizing.
- Prefer fixing root consistency issues in shared surfaces over patching one screen with one-off styling.
- Keep shell and system chrome in English unless current UGC source-of-truth says otherwise.
- Do not hardcode one program, role, or market as global truth unless current owner docs say so.

## Default Repo Boundaries

Current shared boundaries to respect:

- app shell and route map: `src/routes/appRoutes.jsx`
- shared layout: `src/components/AdminPageLayout.jsx`
- shared table and filter surfaces: `src/components/DataTable.jsx`, `src/components/SmartFilter.jsx`
- design tokens: `src/theme/tokens.js`
- heaviest page surfaces:
  - `src/pages/UGCConfig/index.jsx`
  - `src/pages/Mission/MissionFormModal.jsx`
  - `src/pages/Creator/CreatorDrawer.jsx`
  - `src/pages/Notification/index.jsx`
  - `src/pages/Website/index.jsx`

Use these as routing hints, not as permission to skip source-of-truth reading.

## Output Contract

For each substantial session, report in this exact structure:

### Roadmap

- active roadmap lane or track

### Big Picture

- where the current slice sits in the broader project

### Milestone

- the current milestone or execution checkpoint

### What Changed

- concise behavior-level summary of completed work

### Verification

- commands or checks run
- pass/fail result
- explicit note if a needed check could not run

### Docs Synced

- exact Outline pages or local docs updated
- if not synced, state exact pending docs

### Next Step

- exactly one default next action

Do not replace this format with a blog-style summary.

## Docs Sync Rules

When truth changes, sync the owner page instead of scattering prose:

- product or module behavior -> the relevant Outline owner page
- technical or contract truth -> `12 Canonical — Technical Hub` or `13 Canonical — Data & Schema`
- current execution truth -> local `docs/agent-workflow/*`
- durable milestone change -> the right changelog or status owner

If truth did not change, say no owner docs were updated.

## Stop Conditions

Stop and ask before proceeding if:

- source-of-truth pages and verified repo behavior conflict in a way that changes user-facing truth
- the task requires a product decision beyond frontend delivery
- the slice needs backend or database truth that is not available in repo or owner docs
- repro is uncertain enough that implementation would likely guess
- the slice cannot be verified at the current minimum gate level

## Default Recommendation For Broad Goals

When the user gives only a broad goal and does not specify a route, prefer this order:

1. read current roadmap and next-slice owner
2. pick one small slice that improves source-of-truth reliability, shared UI safety, or a visible operator flow
3. verify it
4. sync truth
5. propose one next slice only

## Final Reminder

- Act like a delivery agent, not a note-taker.
- Keep moving through small verified slices.
- Maintain layout and design consistency as a first-class requirement.
- Sync docs after verified truth changes.
- Report progress in roadmap context so the PM can understand status without reading code.
