# Plane To Outline Sync

Use this reference when the user wants work in Plane and project knowledge in Outline to stay aligned.

## Core Principle

- Plane stores operational execution truth.
- Outline stores durable navigation and project understanding truth.
- Sync intent, not noise.

Good sync keeps humans and AI oriented across both systems. Bad sync duplicates every small update and makes both systems noisy.

## Decide The Source Of Truth First

### Plane-first situations

Start from Plane when the change is about:

- backlog content
- assignee or ownership changes on active work
- item priority or state movement
- blockers and dependencies
- sprint / cycle movement
- module assignment
- milestone targeting
- active intake promotion

Typical flow:

1. read or update the Plane objects
2. decide whether the change is durable enough for Outline
3. update only the matching Outline page if needed

### Outline-first situations

Start from Outline when the change is about:

- project framing
- stable product truth
- reading path
- durable decisions
- long-lived roadmap themes
- cross-project operating conventions

Typical flow:

1. read the relevant Outline page and its role
2. identify whether Plane execution objects must be created or updated to match
3. apply the minimum Plane changes needed

## Sync Targets By Intent

Use role-based mapping instead of hard-coding one project structure forever.

### Intake and raw requests

Write to:

- Plane intake items or unplanned work items
- Outline operational intake page only if the request should remain visible outside a single ticket

Do not:

- write raw intake directly into canonical pages

### Active roadmap or priority movement

Write to:

- Plane milestones, cycles, modules, and selected work items
- Outline roadmap/priorities page when the shift changes how the project should be read at a high level

Do not:

- copy every ticket title into the roadmap page

### Durable decisions

Write to:

- Plane comments only if the decision belongs to a specific work item execution trail
- Outline decisions/changelog page when the decision changes process, scope, ownership, or information architecture

Do not:

- turn every implementation note into a durable decision

### Current state

Write to:

- Plane states, cycles, modules, relations, and milestones as the raw operational truth
- Outline current-state page as the curated human-readable snapshot

Do not:

- manually narrate a state in Outline that contradicts live Plane data

### Canonical product truth

Write to:

- Outline canonical pages only after the truth is stable enough to outlive one session or one sprint

Do not:

- dump temporary debug notes, work history, or unresolved debate into canonical pages

## SocialHub-Specific Reading Pattern

Observed from the `SocialHub` root page on 2026-05-06:

- root page role: project navigator
- default reading path points readers to:
  - `10 Canonical — Project Overview`
  - `11 Canonical — Module Catalog`
  - `20 Operational — Current State`
- additional operational pages include:
  - `21 Operational — Roadmap & Priorities`
  - `22 Operational — Decisions & Changelog`
  - `23 Operational — Intake (Feature Requests / Bug Tracker)`

Use this as a strong example, not a universal hard-coded rule for every project.

## Recommended Sync Bundles

### Bundle A: New request becomes managed intake

Use when:

- the user drops a new bug, feature request, or opportunity

Actions:

1. create or update a Plane intake item
2. add labels, state, and any necessary triage metadata
3. if the request affects project-level visibility, append a concise note to the Outline intake page

### Bundle B: Planned priority shift

Use when:

- the active roadmap changed
- a milestone moved
- a module became a priority

Actions:

1. update Plane milestone, cycle, module, or work-item targeting
2. update the Outline roadmap/priorities page with the durable summary
3. if this materially changes project posture, refresh the current-state page too

### Bundle C: Stable decision after discovery or delivery

Use when:

- the team made a durable choice about scope, IA, workflow, or ownership

Actions:

1. update any affected Plane execution objects if needed
2. write the durable rationale to the Outline decisions/changelog page
3. update canonical pages only if the decision changes long-lived truth

### Bundle D: Sprint or status checkpoint

Use when:

- a cycle is closing
- a project update is needed
- leadership wants current status

Actions:

1. read live Plane data for work-item states, blockers, modules, cycles, and milestones
2. summarize what changed and what is stuck
3. update the Outline current-state page with the curated result
4. update roadmap or decision pages only if the checkpoint changes durable direction

## Anti-Patterns

Avoid these mistakes:

- copying every Plane work item into Outline
- using Outline intake pages as the only backlog system
- using Plane comments as the only durable decision log
- updating canonical pages from half-baked discovery
- writing status prose that does not reconcile with current Plane data
- assuming every project uses the same Outline page titles or same Plane feature flags

## Minimum Safe Sync Checklist

Before any two-system sync:

1. resolve the target Plane project live
2. resolve the target Outline page live
3. decide which system owns the truth for this kind of change
4. preview the exact write set
5. apply the minimum changes needed
6. re-read both systems if both were updated
