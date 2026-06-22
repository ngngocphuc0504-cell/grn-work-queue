# Command Templates

## `get-context` Output

```md
Resolved scope: `social-listening`

[global]
- stable personal defaults from HUB
- durable personal memory from Personal Memory - Canonical

[project]
- bootstrap facts from Social listening Context

[canonical-next]
- Canonical - Product Overview
- Canonical - Codebase Context
```

If no project is resolved:

```md
Resolved scope: `global-default`

[global]
- stable personal defaults from HUB
- durable personal memory from Personal Memory - Canonical
```

## `save-context` Write Plan

```md
Write plan
- item: "Prefer concise implementation summaries in Vietnamese"
  - scope: `personal`
  - durability: `durable`
  - confidence: `high`
  - target_page: `Personal Memory - Canonical`
  - promoted_by: `auto`
- item: "Social Listening topic metrics page now treats engage as canonical aggregate"
  - scope: `project:social-listening`
  - durability: `durable`
  - confidence: `high`
  - target_page: `Personal Memory - Inbox Journal`
  - promoted_by: `auto`
- item: "Unsure whether this note belongs to UGC or ODP"
  - scope: `unknown`
  - durability: `session`
  - confidence: `low`
  - target_page: `Personal Memory - Inbox Journal`
  - promoted_by: `auto`
```

## `organize-context` Summary

```md
Organize result
- promoted to Personal Memory - Canonical: 2
- promoted to project bootstrap: 1
- kept in Inbox Journal: 3

Kept in inbox because
- unresolved project scope
- duplicate but lower-confidence copy
- session-only note with no durable value
- candidate target was outside collection `Hai Son`
```

## Metadata Template

```md
- note: "<short fact>"
  - scope: `personal | project:<slug> | unknown`
  - durability: `session | working | durable`
  - source: `<thread/session/date>`
  - confidence: `low | med | high`
  - target_page: `<doc name>`
  - promoted_by: `manual | auto | organize`
```
