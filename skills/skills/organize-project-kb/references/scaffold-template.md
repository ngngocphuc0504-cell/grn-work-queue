# Scaffold Template

## Purpose

This is the default project knowledge-base skeleton for a new Outline project or a full restructure target.

## Naming Convention

- Root page: human-readable project name with no numeric prefix
- Child hub pages: numbered by role band
- If the project needs a dedicated operator guide branch, place it under `24 Operational — User Guide`
- Inside `24 Operational — User Guide`:
  - foundation pages use `00 User Guide — ...`
  - module pages use `10 Module Guide — <Module>`
  - deeper child pages should keep the module name in the title

## Default Tree

- `Project Root`
- `01 Working With This Knowledge Base`
- `10 Canonical — Project Overview`
- `11 Canonical — Module Catalog`
- `12 Canonical — Technical Hub`
- `13 Canonical — Data & Schema`
- `20 Operational — Current State`
- `21 Operational — Roadmap & Priorities`
- `22 Operational — Decisions & Changelog`
- `23 Operational — Intake (Feature Requests / Bug Tracker)`
- `30 Team — Ownership & Ways of Working`
- `90 Archive — Historical / Replaced Docs`

## Optional Operator-Guide Branch

Add this branch when the project has substantial daily-use guidance for non-tech operators or when AI needs a stable router for user-facing questions:

- `24 Operational — User Guide`
- `00 User Guide — How To Use This Guide`
- `01 User Guide — Quick Start For Daily Operators`
- `02 User Guide — Common Rules Across The Website`
- `03 User Guide — Common Problems & Escalation Guide`
- `10 Module Guide — Dashboard`
- `11 Module Guide — <Module>`
- `12 Module Guide — <Module>`

## Default Agent-Prep Pages

- `Agent Operating Model`
- `Daily Command Board`
- `Autonomy Matrix Draft`

Place them under:

- `Agent Operating Model` -> `30 Team — Ownership & Ways of Working`
- `Autonomy Matrix Draft` -> `30 Team — Ownership & Ways of Working`
- `Daily Command Board` -> `20 Operational — Current State`

## Metadata Block For Live Pages

Use this block at the top of every live page:

- `Role:`
- `Status:`
- `Owner:`
- `Primary Reader:`
- `Used For:`
- `Not Used For:`
- `Read This After:`
- `Read Next:`
- `Update Trigger:`
- `Last Verified:`

For Outline pages, the page body should start with the metadata block or the first semantic section. Do not repeat the document title as an identical `H1` inside the page body.

## Reading Paths

### Default picture for a new reader

`Project Root -> 10 Canonical — Project Overview -> 11 Canonical — Module Catalog -> 20 Operational — Current State -> 21 Operational — Roadmap & Priorities`

### Product or spec path

`Project Root -> 10 Canonical — Project Overview -> module owner page -> 13 Canonical — Data & Schema if needed`

### Code or debug path

`Project Root -> 12 Canonical — Technical Hub -> 13 Canonical — Data & Schema if needed -> module owner page`

### Operator guide path

`Project Root -> 24 Operational — User Guide -> foundation page or module guide -> deeper workflow page if needed`

## Owner Boundary

- `Canonical`: durable product, module, technical, and data truth
- `Operational`: current state, priorities, decisions, intake, and short-lived operator views
- `Operational — User Guide`: operator-facing workflows, common issues, self-serve checks, and escalation paths
- `Team`: ownership, onboarding, collaboration rules, and agent-prep policy
- `Archive`: historical or replaced material only

## Module Catalog Rule

When the project has module surfaces, `11 Canonical — Module Catalog` should act as the directory of module owner pages. Each module page should cover:

- module purpose
- target roles
- primary workflow
- key states and statuses
- important tables, filters, and actions
- dependencies
- relevant technical or data links
- explicit non-goals if scope is partial
