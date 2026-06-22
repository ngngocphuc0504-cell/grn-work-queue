# Plane

Use for Garena Plane at `managetask.odp.garena.vn`: projects, work items, states, labels, cycles, modules, milestones, epics, intakes, relations, comments, work logs, project features, and Plane pages.

## Known Surface

The 2026-06-15 MCP admin screenshot showed 109 Plane tools. This surface is large and changes more often than smaller families. Resolve exact `plane_*` callable names from the active session before acting.

Common logical groups:

- Workspace/project discovery and project features
- Work items: list, search, retrieve by identifier, create, update, delete/archive when exposed
- States, labels, priorities, assignees, work item types, custom properties
- Cycles, cycle membership, transfer/archive flows
- Modules, module membership, archive/delete flows
- Milestones and epics
- Intake work items
- Relations, links, comments, work logs
- Project/workspace pages where exposed

## Workflow

1. Start with the cheapest successful Plane read, such as current user, workspace features, or project list.
2. Resolve the target project before reading or mutating work.
3. Read project features before assuming cycles, modules, pages, intake, or work logs are enabled.
4. Resolve identifiers like `ABC-123` through retrieve-by-identifier; use search/list for fuzzy requests.
5. Prefer updating existing objects over creating duplicates.
6. For mutations, re-read the exact object first, perform the change, then verify by reading back.

## Plane And Outline Boundary

- Plane is source of truth for execution: backlog, assignees, state, cycles, modules, blockers, and item-level comments.
- Outline is source of truth for durable knowledge: specs, reading paths, current-state narrative, roadmap framing, and decisions.
- Do not mirror every Plane mutation to Outline.
- For cross-system sync, read `cross-tool-workflows.md`.

## Safety

- Never guess project IDs, state IDs, label IDs, cycle IDs, module IDs, or work item ids.
- Never bulk-edit from a vague request.
- Never archive, delete, transfer, or close items without explicit user intent.
- For complex Plane workflows, the older `work-with-plane` skill has deeper reference material and can be used as a companion.
