---
name: work-with-plane
description: >
  Use when Codex needs to work with Plane through MCP on the Garena self-hosted instance
  (`managetask.odp.garena.vn`): inspect or update projects, work items, cycles, modules,
  milestones, labels, states, epics, initiatives, intake, relations, comments, work logs,
  custom work item types/properties, workspace/project features, or Plane pages; evaluate
  Business-plan features such as dashboards, workflows/approvals, customers, teamspaces,
  recurring work, templates, and SLAs against live MCP coverage; plan or triage delivery work;
  or sync durable changes between Plane and Garena
  Outline (`wiki.odp.garena.vn`) such as roadmap, current state, decisions, and intake.
  Trigger on requests mentioning Plane, `managetask`, backlog, sprint/cycle, module, milestone,
  triage, work item, initiative, epic, Plane Business, feature flags, or `sync Plane va Outline`.
---

# Work With Plane

Use Plane MCP as the primary interface for operational project work. Use Outline MCP as the companion system for durable project knowledge, reading paths, and curated status pages.

## Connection Model

- Treat `Plane`, `managetask.odp.garena.vn`, and the connected Plane MCP tools as the same system.
- Treat `Outline`, `wiki.odp.garena.vn`, and the connected Outline MCP tools as the same system.
- Default to MCP instead of browsing either UI when MCP can answer the task.
- If the user is reconnecting a local Plane MCP server for the Garena instance, infer these defaults from the deployment URL unless live config proves otherwise:
  - workspace URL: `https://managetask.odp.garena.vn/garena-vietnam-odp`
  - likely workspace slug: `garena-vietnam-odp`
  - likely API base URL for stdio transport: `https://managetask.odp.garena.vn/api`
- Start any non-trivial Plane task by confirming live access with `get_me`, reading workspace feature flags with `get_workspace_features`, then resolving the project from `list_projects`.

## Working Modes

Choose one mode before reading or writing.

- `context bootstrap`: understand a Plane project, its active structure, and the matching Outline subtree
- `triage / intake`: capture raw requests, bugs, or ideas without prematurely turning them into canonical truth
- `planning / execution`: create or update work items, cycles, modules, milestones, relations, and ownership
- `status / reporting`: summarize delivery state from live Plane data and write the right durable update to Outline
- `cross-system sync`: keep Plane and Outline aligned without duplicating noisy operational chatter

## Deterministic Plane Workflow

1. Confirm identity and access with `get_me`.
2. Read workspace feature flags with `get_workspace_features`.
3. Resolve the target project with `list_projects`.
4. Read the project's live shape before changing anything:
   - `get_project_features`
   - `list_states`
   - `list_labels`
   - `list_work_item_types`
   - `list_cycles`
   - `list_modules`
   - `list_milestones`
5. For feature-specific tasks, gate behavior by workspace and project features first:
   - workspace: `wiki`, `pi`, `initiatives`, `teams`, `customers`, `project_grouping`
   - `cycle_view`
   - `module_view`
   - `issue_views_view`
   - `page_view`
   - `intake_view`
   - `is_issue_type_enabled`
   - `is_time_tracking_enabled`
6. If the user references an item like `ABC-123`, use `retrieve_work_item_by_identifier`.
7. If the user references a fuzzy request like "open bugs in publishing", use `list_work_items` with filters or `search_work_items`.
8. Prefer updating existing objects over creating new ones when the target already exists.
9. Re-read the exact live object immediately before any destructive or high-impact change.
10. After writing, re-read the updated object and summarize the result in user language.

## Operational Heuristics

- Treat work items as the atomic execution record.
- Treat cycles as time boxes and modules as scope buckets. Do not confuse them.
- Use milestones for ship checkpoints or date commitments.
- Use relations for blockers, dependencies, and duplicates instead of burying those links in prose.
- Use comments for execution context or short decisions that belong on the item.
- Use work logs only if the project actually uses time tracking. Read project features first.
- Use custom properties only after reading live work item types and property definitions.
- Treat workspace and project feature flags as configuration, not execution data. Do not enable or disable features unless the user explicitly asks for that structural change.
- Use Plane pages sparingly from AI. Current MCP coverage can create and retrieve pages, but long-lived knowledge maintenance is usually safer in Outline.

## Feature-Specific MCP Rules

### Workspace And Business Features

- Always read `get_workspace_features` before using Business-plan concepts.
- Treat Business availability and MCP support as separate questions:
  - a feature can exist in Plane UI but still have no dedicated MCP tool
  - a workspace feature flag can be off even after the plan upgrade
  - MCP may expose a feature flag update without exposing object-level CRUD for that feature
- Use `update_workspace_features` only when the user explicitly asks to enable or disable a workspace feature.
- When the user asks about a Business feature with no MCP object tools, state the gap and offer the closest supported workflow or a UI fallback.

### Epics

- Gate epics by `get_project_features.epics` and the live work item types before creating or updating.
- Use epics for large delivery containers inside one project.
- Available MCP actions:
  - `list_epics`
  - `create_epic`
  - `retrieve_epic`
  - `update_epic`
  - `delete_epic`
- Before creating an epic, inspect existing epics, states, labels, assignees, and work item types so it lands in the right schema.

### Initiatives

- Gate initiatives by `get_workspace_features.initiatives`.
- Treat initiatives as cross-project strategic goals above epics and work items.
- Available MCP actions:
  - `list_initiatives`
  - `create_initiative`
  - `retrieve_initiative`
  - `update_initiative`
  - `delete_initiative`
- Do not invent initiative hierarchy or project membership rules unless the live API exposes them. Link related work through explicit Plane fields only when the tool surface supports it; otherwise document the mapping in Outline.

### Work Item Types And Properties

- Gate custom schemas by `is_issue_type_enabled` / project features and `list_work_item_types`.
- Read property definitions with `list_work_item_properties` before creating or updating custom fields.
- Treat work item type/property changes as structural changes that affect future work across the project.
- Prefer adding labels or comments for one-off metadata; add custom properties only when the metadata will be reused.

### Time Tracking And Work Logs

- Gate work logs by `is_time_tracking_enabled`.
- Use:
  - `get_project_worklog_summary`
  - `list_work_logs`
  - `create_work_log`
  - `update_work_log`
  - `delete_work_log`
- Do not infer time tracking from comments or activity logs. If time tracking is disabled, say so and ask whether to enable it only if the user explicitly wants worklog operations.

### Cycles

- Treat cycles as sprint/timebox objects.
- Read with `list_cycles` before choosing a target cycle.
- Manage scope inside a cycle with:
  - `list_cycle_work_items`
  - `add_work_items_to_cycle`
  - `remove_work_item_from_cycle`
  - `transfer_cycle_work_items`
- Use `archive_cycle` and `unarchive_cycle` for lifecycle control instead of deleting by default.

### Modules

- Treat modules as scope or feature buckets, not time boxes.
- Read with `list_modules` before creating a new module.
- Manage scope membership with:
  - `list_module_work_items`
  - `add_work_items_to_module`
  - `remove_work_item_from_module`
- Use modules together with cycles when the user needs both scope and time dimensions.

#### Rebuilding Modules For Display Order

Use this pattern when the user needs Plane modules to display in a fixed order and `update_module` cannot change the visible order. Plane can sort module groups by internal `sort_order` instead of module name, and a newly created module may be inserted at the top of the list.

Safe workflow:

1. Read `list_modules` and confirm the current active modules, task counts, IDs, and `sort_order`.
2. If modules already exist with the desired names but wrong order, rename the old modules with an obvious temporary prefix such as `OLD - ...` before creating replacements. This prevents duplicate-name confusion.
3. Create the replacement modules in reverse display order when live behavior shows new modules are inserted at the top. Example: to display `01, 02, 03`, create `03`, then `02`, then `01`.
4. Add work items to the new modules with `add_work_items_to_module`, grouped by their intended target module.
5. Verify the new module memberships with `list_module_work_items`. Do not trust the mutation response alone.
6. Remove work items from the old modules with `remove_work_item_from_module`.
7. Verify old modules are empty with `list_module_work_items` and verify active module order/counts with `list_modules`.
8. Prefer `archive_module` for lifecycle cleanup. If `archive_module` fails and the user explicitly asked to remove/recreate modules, use `delete_module` only after the old modules are verified empty and the replacement modules have the expected work items.
9. Re-read `list_modules` after cleanup and report final module order and task counts.

MCP/tool reliability note: some Plane module membership and delete endpoints may return `Unexpected response type` even when the side effect succeeded. Treat these as "verify required" signals, not final failure. Always re-read the affected modules before continuing.

### Views

- Treat saved views as a UI capability, not a first-class MCP-managed object in the current tool surface.
- Do not promise create/update/delete support for Plane Views through MCP unless the tool surface changes.
- Emulate the practical outcome of a view by combining:
  - `list_work_items` filters
  - `search_work_items`
  - labels, states, priorities, cycles, modules, and assignees
- If the user asks to "make a view", explain that MCP can assemble the same filtered result set, but cannot currently manage the saved View object itself.

### Pages

- Treat Plane pages as partial MCP coverage only.
- Current safe operations are:
  - `create_project_page`
  - `create_workspace_page`
  - `retrieve_project_page`
  - `retrieve_workspace_page`
- Do not promise page list/search/update/delete support through MCP in the current environment.
- Prefer Outline for maintained docs, canonical knowledge, and repeated edits.

### Dashboards, Workflows, Approvals, Customers, Teamspaces, Templates, Recurring Work, And SLAs

- Treat these as Business product capabilities that may exist in the UI.
- In the current MCP surface, do not promise dedicated object CRUD for:
  - dashboards and dashboard widgets
  - workflows and approvals
  - customer profiles/customer requests
  - teamspaces/teams
  - project or page templates
  - recurring work items
  - custom SLAs
- If the task can be represented through supported Plane primitives, use those primitives:
  - dashboards -> live filtered summaries from work items, cycles, modules, milestones, and worklogs
  - workflows/approvals -> states, labels, relations, comments, and documented process in Outline
  - customers -> labels, custom properties, links, or intake metadata only after reading schema
  - recurring work -> create individual work items or prepare UI instructions; do not claim recurrence was configured
  - templates -> create a normal project/page/work item from an agreed pattern; do not claim a saved template exists
- If the user needs the native Business object, say MCP coverage is missing and use a browser/UI workflow only when a logged-in controllable browser is available.

### Intakes

- Treat Intake as the right place for raw requests before commitment into planned execution.
- Use:
  - `list_intake_work_items`
  - `create_intake_work_item`
  - `retrieve_intake_work_item`
  - `update_intake_work_item`
  - `delete_intake_work_item`
- If the team wants to promote an intake into committed execution, create or update the matching work item explicitly. Do not assume a dedicated "promote intake" MCP action exists.

## Plane And Outline Sync Rules

- Treat Plane as the source of truth for operational execution:
  - backlog
  - assignees
  - states
  - cycles
  - modules
  - blockers
  - work-item-level comments
  - epics and initiatives when they are enabled and actively used
- Treat Outline as the source of truth for durable project knowledge:
  - reading path
  - canonical product framing
  - current-state narrative
  - roadmap framing
  - durable decisions
  - curated intake summaries
- Do not mirror every Plane mutation into Outline.
- Sync only durable changes or information that helps humans and future AI readers orient faster.
- If the user asks to sync both systems, preview the full update bundle first:
  - which Plane objects will change
  - which Outline pages will change
  - what truth will live in each place after the sync

## Outline Mapping Pattern

If the target Outline subtree exposes a navigator page like `SocialHub`, read that root page first and follow its declared reading path. Resolve the actual target page by role, not by title memory alone.

Default intent mapping:

- raw request, bug report, or untriaged idea -> operational intake page
- active priorities, themes, or sequencing -> roadmap/priorities page
- durable decision or IA/process change -> decisions/changelog page
- current delivery snapshot -> current-state page
- stable product truth or module catalog -> canonical pages, usually only after the change is clearly durable

For the shared SocialHub subtree, the observed mapping on 2026-05-06 is:

- `23 Operational — Intake (Feature Requests / Bug Tracker)` for incoming requests
- `21 Operational — Roadmap & Priorities` for active priorities
- `22 Operational — Decisions & Changelog` for durable decisions and short change trace
- `20 Operational — Current State` for where the project stands today
- `10/11/12/13 Canonical ...` for stable product, module, technical, and data truth

Do not assume every other project uses the exact same page titles. Resolve live.

## High-Value Workflows

### Bootstrap a project

1. Read Plane project list and identify the target project.
2. Read project features, states, labels, cycles, modules, and milestones.
3. Inspect the matching Outline root page and its routing guidance.
4. Summarize:
   - what is active now in Plane
   - what structure exists in Outline
   - what is missing or stale between the two systems

### Turn new input into managed work

1. Decide whether the input is intake, planned work, or already-active execution.
2. Create or update the right Plane work item or intake item.
3. If the input matters beyond one ticket, add the matching durable note in Outline:
   - intake summary
   - roadmap delta
   - current-state change
   - decision log entry

### Close the loop after delivery movement

1. Read the live Plane items that changed.
2. Decide whether the change is:
   - execution-only
   - roadmap-relevant
   - decision-worthy
   - current-state-worthy
3. Update only the necessary Outline page.
4. Keep canonical pages clean from session noise, temporary debugging notes, and item-level churn.

## Safety Rules

- Never guess project IDs, state IDs, label IDs, cycle IDs, or module IDs from stale memory.
- Never bulk-edit multiple work items from a vague request.
- Never archive, delete, or transfer work without explicit user intent.
- Never create duplicate work items, modules, or milestones when a live object already exists.
- Never promote intake or short-lived execution chatter into canonical Outline pages.
- Never claim a Plane feature exists for the target project without reading live features first.
- If MCP coverage is missing for a desired action, say so clearly and choose the closest safe fallback.

## References

- Read [plane-capabilities.md](./references/plane-capabilities.md) for the full Plane feature surface, current MCP coverage, and notable gaps.
- Read [plane-outline-sync.md](./references/plane-outline-sync.md) for detailed sync patterns, page-role mapping, and anti-patterns.
