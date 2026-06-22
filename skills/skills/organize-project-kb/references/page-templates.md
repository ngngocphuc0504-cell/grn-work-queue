# Page Templates

## Root Page

Use the root page as an entry page and navigator only.

It should:

- define what the project is
- state the current active scope
- provide default reading paths
- link to top-level hubs

It should not:

- hold detailed module rules
- hold technical implementation truth
- act as an archive

## `01 Working With This Knowledge Base`

Use this page to define:

- page roles
- update rules
- conflict rules
- reading path boundaries
- what future agent-prep docs do and do not override

## Canonical Pages

### `10 Canonical — Project Overview`

Use for:

- durable product framing
- current active delivery scope
- scope boundaries

### `11 Canonical — Module Catalog`

Use for:

- directory of module owner pages
- module routing

### `12 Canonical — Technical Hub`

Use for:

- route into repo or technical references
- technical owner page links

Do not use for:

- long implementation logs

### `13 Canonical — Data & Schema`

Use for:

- data contracts
- schema references
- UI/data reference sheets

## Operational Pages

### `20 Operational — Current State`

Use for:

- current scope
- recent verification state
- current gaps
- short route to daily board if present

### `21 Operational — Roadmap & Priorities`

Use for:

- current sequencing
- next milestone priorities

### `22 Operational — Decisions & Changelog`

Use for:

- durable documentation or process decisions
- notable structure milestones

### `23 Operational — Intake (Feature Requests / Bug Tracker)`

Use for:

- untriaged requests, bugs, and ideas

Do not treat intake as truth until promoted.

### `24 Operational — User Guide`

Use for:

- operator-facing usage guides
- daily workflows for non-tech readers
- common issues, self-serve checks, and escalation paths
- AI routing into the correct module guide

Do not use for:

- canonical module truth
- technical contracts
- roadmap or execution logs

Recommended child-page naming when this branch exists:

- foundation pages:
  - `00 User Guide — How To Use This Guide`
  - `01 User Guide — Quick Start For Daily Operators`
  - `02 User Guide — Common Rules Across The Website`
  - `03 User Guide — Common Problems & Escalation Guide`
- module pages:
  - `10 Module Guide — Dashboard`
  - `11 Module Guide — Creator`
  - `12 Module Guide — Mission`
  - continue by module

Writing rules for this branch:

- write in Vietnamese with diacritics
- use non-tech wording
- start with the metadata block, not a duplicate `H1`
- let the first body heading be a semantic section like `Purpose`

## Team Page

### `30 Team — Ownership & Ways of Working`

Use for:

- ownership
- onboarding links
- collaboration rules
- links to agent-prep docs

## Archive Page

### `90 Archive — Historical / Replaced Docs`

Use for:

- historical provenance
- replaced docs
- stale carryover pages that should not stay live

## Agent-Prep Pages

### `Agent Operating Model`

Use for:

- read route for future agent work
- source priority
- sync bundle
- escalation triggers

### `Daily Command Board`

Use for:

- current milestone
- why now
- main blocker
- single next step
- completion snapshot
- exit condition

### `Autonomy Matrix Draft`

Use for:

- current autonomy level
- what is allowed
- what must escalate
