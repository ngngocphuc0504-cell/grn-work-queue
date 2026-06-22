---
name: aov-delivery-agent
description: Use for AoV Card Game delivery: read project docs, plan one task, write tests, implement code, run browser QA, and sync verified project docs without drifting from source of truth.
---

# AoV Delivery Agent

## Purpose

Use this skill for full-lifecycle delivery work in `AoV Card Game`:

- bootstrap context from the live project docs
- turn specs or workstreams into an execution plan
- write failing tests before implementation
- implement code in the correct layer
- run verification and browser QA
- sync the right project docs after meaningful changes

Default repo:

- `C:\Users\Hai Son\Desktop\Claude\AOV Card Game\aov-card-game`

## Required Read Order

Read only what is needed, in this order:

1. [00 Agent Entry](https://wiki.odp.garena.vn/doc/00-agent-entry-oHEEyvTRej)
2. [10 Operational - Session Handoff / Current State](https://wiki.odp.garena.vn/doc/10-operational-session-handoff-current-state-IQCRww2cFl)
3. The active workstream that matches the task
4. The canonical owner page for the task:
   - gameplay rules or rulings -> [21 Canonical - Game Rules](https://wiki.odp.garena.vn/doc/game-rules-o5cKFD3rPP)
   - card data, naming, assets -> [22 Canonical - Card Database](https://wiki.odp.garena.vn/doc/card-database-11fSVvlMuV)
   - stack, architecture, repo boundaries -> [23 Canonical - Tech Stack & Architecture](https://wiki.odp.garena.vn/doc/23-canonical-tech-stack-architecture-GNSzgMiiEv)
5. Read [40 Changelog / Decisions Log](https://wiki.odp.garena.vn/doc/40-changelog-decisions-log-YX0QCga9TQ) only if historical rationale is needed.

## Hard Project Truths

- Live stack is `React 19 + TypeScript + Tailwind CSS + Vite`.
- Default QA stack is `Vitest` plus `Playwright CLI`.
- Current active track is `VS AI` hardening, not broad new-feature expansion.
- Do not inherit old global assumptions like `Next.js`, `Clerk`, or live `Supabase` usage into this project.
- The current baseline is desktop-only and click-only.
- Do not reopen mobile scope unless the user explicitly changes roadmap.
- Do not reintroduce drag-and-drop as the main interaction model.
- AI must use the same engine rule path as the player. Never create a separate rule engine for AI.
- Do not break `self-play` while improving `VS AI`.

## Task Routing

- Current truth, blocker, next step -> `10 Operational`
- Active plan / phased execution -> active workstream under `30 Workstreams`
- Gameplay logic -> `21 Canonical`
- Card canon / asset truth -> `22 Canonical`
- Architecture, file ownership, test boundaries -> `23 Canonical`

## Default Delivery Pipeline

### 1. Resolve source of truth first

Before doing work, state:

- task intent
- owner page
- repo area likely impacted
- fact vs assumption

Do not plan or code before the route is explicit.

### 2. Plan in small executable slices

Convert the task into a small phase/task plan with:

- exact goal
- files/modules likely affected
- tests to add or update
- verification commands
- blockers or dependencies

Prefer the existing active workstream if it already covers the task. Do not create a parallel plan unless the docs are missing the lane entirely.

### 3. Write tests before implementation

Default mapping:

- engine rules -> `src/engine/__tests__/*`
- AI behavior -> `src/engine/__tests__/ai.test.ts` or nearby AI tests
- selectors / view-models -> `src/ui/__tests__/*` and `src/components/action-panels/__tests__/*`
- browser regression -> `scripts/audit/*` or Playwright-based audit scripts

If a task changes behavior and no test layer exists yet, add the smallest useful test harness first.

For foundational rule bugs, add at least one negative engine regression, one AI/legal-action regression, and one selector/view-model or UI affordance regression before implementation. The engine must reject illegal actions even if the UI accidentally allows them.

### 4. Implement in the correct layer

- Put gameplay truth in the engine, not in React components.
- Put AI action selection in `src/engine/ai/*`.
- Put legality/derived UI state in selectors or view-models.
- Keep render components presentation-focused.
- Do not duplicate cost, legality, or attack rules across engine and UI.

### 5. Verify before claiming success

Use `npm.cmd` on Windows when running project commands.

Default verification set:

```bash
npm.cmd run build
npm.cmd run test:engine
npm.cmd run test:ai
npm.cmd run test:viewmodel
npm.cmd run audit:selfplay
npm.cmd run audit:gameplay-qa
```

If the task touches `VS AI`, also require:

```bash
npm.cmd run audit:vs-ai
```

If `audit:vs-ai` does not exist yet and the task is in the AI hardening lane, create it instead of skipping the gap silently.

### 6. Sync the right docs

After meaningful delivery:

- session truth, blockers, next work -> `10 Operational`
- durable technical change -> `23 Canonical`
- gameplay rule change -> `21 Canonical`
- durable milestone or major state transition -> `40 Changelog / Decisions Log`

Do not spread the same truth across multiple pages. Update the owner page first.

## Default Recommendation For The Current Roadmap

Until the roadmap changes, prefer this order:

1. expand `test:ai` into broader phase-contract coverage
2. add `VS AI` UI and view-model tests
3. add and stabilize `audit:vs-ai`
4. tune pacing only after coverage and audit are green

## Output Contract

- Use Vietnamese by default.
- Keep explanations operator-friendly and concrete.
- Separate `Fact` from `Assumption` whenever there is uncertainty.
- Surface blockers and tradeoffs early.
- End each substantial session with:
  - changed files
  - commands run and pass/fail result
  - docs that should be synced

## Stop Conditions

Stop and ask before proceeding if:

- the task reopens mobile scope
- the task reintroduces drag-and-drop
- the task adds a new gameplay system outside the active roadmap
- project docs and verified repo behavior conflict in a way that changes user-facing truth
