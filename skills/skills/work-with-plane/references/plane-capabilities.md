# Plane Capabilities

Use this reference when you need the full capability map of Plane and the practical MCP coverage currently available to AI agents.

## Product Surface

Official Plane product and developer docs indicate these core capabilities:

- projects and work items
- cycles
- modules
- pages / docs
- multiple layout views
- intake and triage
- dashboards
- estimates
- REST API and webhooks

Official docs also show additional workspace or commercial capabilities that may be enabled depending on deployment and licensing:

- epics
- initiatives
- custom work item properties
- wiki
- program increment / PI support
- teamspaces / teams
- integrations
- governance and approval features
- dashboards and dashboard widgets
- workflows and approvals
- customer profiles and customer requests
- recurring work items
- project and page templates
- custom SLAs
- AI agents and AI-assisted summaries/search

Do not assume a capability is enabled for the current workspace just because Plane supports it in general. Read live workspace and project features first.

## Business Plan Reality Check

Plane Business currently advertises workflows and approvals, AI agents, SSO, advanced dashboards, intake forms/email, nested pages, project templates, customer profiles, recurring work items, custom SLAs, and additional AI credits. Treat these as product capabilities, not automatic MCP capabilities.

Observed live through the Garena Plane MCP environment on 2026-05-22:

- official MCP exposes workspace feature flags through:
  - `get_workspace_features`
  - `update_workspace_features`
- official MCP exposes project feature flags through:
  - `get_project_features`
  - `update_project_features`
- current MCP object coverage includes:
  - work items
  - epics
  - initiatives
  - cycles
  - modules
  - milestones
  - intake work items
  - labels and states
  - work item types and custom properties
  - relations, comments, links, activities, and work logs
  - partial pages
- current MCP does not expose dedicated object tools for:
  - dashboards
  - workflows or approval rules
  - customers/customer requests
  - teamspaces/teams
  - recurring work items
  - saved project/page templates
  - custom SLAs
  - AI agent assignment, AI search, or AI summaries
- current workspace feature flags on 2026-05-22 after Business feature enablement:
  - `wiki = true`
  - `pi = true`
  - `project_grouping = true`
  - `initiatives = true`
  - `teams = true`
  - `customers = true`

When a Business feature is requested, answer in three layers:

1. whether the live workspace/project feature flag is enabled
2. whether MCP exposes object-level tools for the operation
3. the closest supported fallback or the need for a logged-in UI workflow

## Observed Garena Context

Observed through MCP on 2026-05-22:

- connected user: `haison.tran@garena.vn`
- visible projects include `Ads Manager`, `Creative Lab`, `Data Platform`, `Garena Vietnam ODP`, `Hai-Son`, `OM`, `Publishing Platform`, `Social Data`, `Social Hub`, `Social Listening`, and `UGC Website`
- workspace features returned:
  - `wiki = true`
  - `pi = true`
  - `project_grouping = true`
  - `initiatives = true`
  - `teams = true`
  - `customers = true`

Project-level features vary. Example from live data:

- some projects have `intake_view = true`
- some projects have `intake_view = false`
- some projects have `is_time_tracking_enabled = false`
- some projects have `is_issue_type_enabled = false`
- some projects have `issue_views_view = true`
- some projects have `issue_views_view = false`

Always check the target project before designing the workflow.

## MCP Coverage By Category

The official Plane MCP server README on GitHub described 100+ tools across 20 categories as of the page crawled in April 2026. Use the live tool surface in the current environment as final authority.

## Requested Feature Matrix

Use this matrix first when the user asks specifically about `Cycles`, `Modules`, `Views`, `Pages`, or `Intakes`.

### Cycles

Project feature gate:

- `cycle_view`

Direct MCP support:

- yes

Available actions:

- `list_cycles`
- `create_cycle`
- `retrieve_cycle`
- `update_cycle`
- `delete_cycle`
- `archive_cycle`
- `unarchive_cycle`
- `list_archived_cycles`
- `list_cycle_work_items`
- `add_work_items_to_cycle`
- `remove_work_item_from_cycle`
- `transfer_cycle_work_items`

Effective usage:

- use for sprint planning and timeboxed delivery
- inspect the current cycle set before creating a new one
- transfer unfinished work forward instead of duplicating items

### Modules

Project feature gate:

- `module_view`

Direct MCP support:

- yes

Available actions:

- `list_modules`
- `create_module`
- `retrieve_module`
- `update_module`
- `delete_module`
- `archive_module`
- `unarchive_module`
- `list_archived_modules`
- `list_module_work_items`
- `add_work_items_to_module`
- `remove_work_item_from_module`

Effective usage:

- use for feature or scope grouping
- combine with cycles when you need both scope and time structure
- check existing modules before creating a near-duplicate

### Views

Project feature gate:

- `issue_views_view`

Direct MCP support:

- no dedicated View-object tools are exposed in the current environment

What MCP can still do:

- reproduce the data result of a view with `list_work_items`
- search across the workspace with `search_work_items`
- filter by state, assignee, priority, label, cycle, module, creator, and archive state

Current gap:

- no `list_views`
- no `create_view`
- no `update_view`
- no `delete_view`
- no Display/layout management

Effective usage:

- treat Views as a UI layer
- when the user asks for a view, provide the equivalent filtered query result or define the filter logic in plain language

### Epics

Project feature gate:

- `get_project_features.epics`

Direct MCP support:

- yes

Available actions:

- `list_epics`
- `create_epic`
- `retrieve_epic`
- `update_epic`
- `delete_epic`

Effective usage:

- use for large project-level delivery containers
- inspect states, labels, assignees, and work item types before creating
- do not treat epics as cross-project initiatives

### Initiatives

Workspace feature gate:

- `get_workspace_features.initiatives`

Direct MCP support:

- yes

Available actions:

- `list_initiatives`
- `create_initiative`
- `retrieve_initiative`
- `update_initiative`
- `delete_initiative`

Effective usage:

- use for strategic goals that can span projects, epics, and work items
- inspect live initiatives before creating a new one
- if the workspace feature flag is off, do not create or update initiatives unless the user first asks to enable the feature

### Pages

Project feature gate:

- `page_view`

Direct MCP support:

- partial

Available actions:

- `create_project_page`
- `create_workspace_page`
- `retrieve_project_page`
- `retrieve_workspace_page`

Current gap:

- no page list
- no page search
- no page update
- no page delete

Effective usage:

- safe for one-off creation when the destination is explicit
- safe for reading when the page ID is already known
- poor fit for ongoing documentation maintenance; use Outline instead

### Dashboards

Workspace/product availability:

- Business product capability

Direct MCP support:

- no dedicated dashboard or widget tools are exposed in the current environment

What MCP can still do:

- generate live dashboard-like summaries from work items, cycles, modules, milestones, and worklogs
- define dashboard metrics and filters for a human to save in the UI

### Workflows And Approvals

Workspace/product availability:

- Business product capability

Direct MCP support:

- no dedicated workflow-rule or approval-rule tools are exposed in the current environment

What MCP can still do:

- inspect and update states when asked
- model blockers through work item relations
- document approval expectations in comments or Outline

### Customers And Customer Requests

Workspace feature gate:

- `get_workspace_features.customers`

Direct MCP support:

- no dedicated customer profile/request object tools are exposed in the current environment

What MCP can still do:

- preserve customer context through labels, links, intake fields, or custom work item properties if the target project schema supports it
- use Outline for durable customer-request narratives when Plane native customer objects cannot be managed through MCP

### Teamspaces / Teams

Workspace feature gate:

- `get_workspace_features.teams`

Direct MCP support:

- no dedicated teamspace/team object tools are exposed in the current environment

What MCP can still do:

- use project membership and ownership data where exposed
- avoid moving projects between teamspaces unless a live tool exists

### Recurring Work Items

Workspace/product availability:

- Business product capability

Direct MCP support:

- no dedicated recurring-work-item tools are exposed in the current environment

What MCP can still do:

- create normal work items for known occurrences
- prepare UI instructions or a spec for recurrence rules
- never claim a recurrence has been configured through MCP

### Templates And SLAs

Workspace/product availability:

- Business product capability

Direct MCP support:

- no dedicated saved template or custom SLA tools are exposed in the current environment

What MCP can still do:

- create normal projects, pages, intakes, and work items from a repeated pattern
- represent SLA-like metadata through labels, target dates, priorities, and custom properties when the schema supports it
- document the intended template or SLA in Outline if it is durable operating guidance

### Intakes

Project feature gate:

- `intake_view`

Direct MCP support:

- yes

Available actions:

- `list_intake_work_items`
- `create_intake_work_item`
- `retrieve_intake_work_item`
- `update_intake_work_item`
- `delete_intake_work_item`

Effective usage:

- keep raw requests separate from committed delivery
- use intake for noisy inflow, then create or update a real work item when the team commits

Current gap:

- no dedicated "promote intake to work item" tool is exposed here

### Projects

Supported well:

- list projects
- create, retrieve, update, delete projects
- read and update project features
- read project members
- get project worklog summary

Use for:

- discovering the workspace structure
- checking whether modules, cycles, intake, pages, or time tracking are enabled
- finding project IDs and identifiers before deeper actions

### Work Items

Supported well:

- list, filter, search, create, retrieve, update, delete work items
- retrieve by human identifier like `PROJECT-123`

Use for:

- backlog management
- current execution tracking
- bug fixing workflows
- status reporting from live records

Best practice:

- read states, labels, and types first
- use relations instead of prose for blockers
- use comments for short execution context

### Cycles

Supported well:

- list, create, retrieve, update, delete
- archive and unarchive
- add, remove, list, and transfer work items

Use for:

- sprint planning
- active iteration management
- moving unfinished work between time boxes

Effective MCP pattern:

1. `list_cycles`
2. `list_cycle_work_items`
3. update membership with add/remove/transfer actions
4. archive when the cycle is done instead of deleting by default

### Modules

Supported well:

- list, create, retrieve, update, delete
- archive and unarchive
- add, remove, and list work items

Use for:

- feature grouping
- initiative slicing inside a project
- cross-cycle scope organization

Effective MCP pattern:

1. `list_modules`
2. `list_module_work_items`
3. adjust membership rather than cloning work items
4. archive when the module is retired

### Views

Supported indirectly only:

- use `list_work_items` and `search_work_items` to emulate the result set

Not supported as first-class MCP objects:

- no saved View CRUD
- no layout or Display controls

Use for:

- reproducing what a saved view would show
- handing the user the exact filter logic they can save manually in the UI if needed

### Milestones

Supported well:

- list, create, retrieve, update, delete
- add, remove, and list work items

Use for:

- ship checkpoints
- release milestones
- top-level delivery gates

### Labels and States

Supported well:

- full CRUD for labels
- full CRUD for states

Use for:

- standardizing triage
- building filtered views through consistent metadata

Safety:

- never create duplicate labels or states without checking the live set first

### Work Item Types and Properties

Supported:

- list and CRUD work item types
- list and CRUD custom properties for a type

Use for:

- tailoring project schemas
- creating richer intake or delivery metadata

Safety:

- these changes affect project structure, not just one ticket
- inspect existing types and property definitions before editing

### Intake

Supported:

- list, create, retrieve, update, delete intake work items

Use for:

- collecting requests before promotion into planned work
- keeping noisy inflow separate from committed execution

Effective MCP pattern:

1. `list_intake_work_items`
2. create or update the intake record
3. if the request becomes planned work, create or update the real work item explicitly

### Epics and Initiatives

Supported in the MCP surface:

- epics: list and CRUD inside a project
- initiatives: list and CRUD at workspace level

Reality check:

- availability depends on workspace features and deployment state
- do not assume they are actively used just because tools exist
- in the observed Garena workspace on 2026-05-22, `initiatives = true`; still inspect existing initiatives before creating new ones

### Relations, Comments, Links, Activities, Work Logs

Supported:

- relations
- comments
- external links
- activity reads
- work log CRUD

Use for:

- preserving execution trace on the item itself
- linking specs, PRs, dashboards, or incidents
- tracking blockers and duplicates
- producing better status summaries from activity history

### Pages

Currently supported in this tool surface:

- create workspace page
- create project page
- retrieve workspace page
- retrieve project page

Important limitation:

- no page list/search/update/delete tools are exposed here
- long-lived knowledge maintenance is usually better done in Outline, where document listing and updates are available

Effective MCP pattern:

1. only create a page when the destination is explicit
2. only retrieve a page when you already know the page ID
3. move durable, editable documentation workflows to Outline

## High-Value Query Patterns

Use these patterns to work efficiently:

- project discovery: `list_projects`
- one exact ticket: `retrieve_work_item_by_identifier`
- filtered backlog: `list_work_items` with project, states, priorities, labels, cycles, or modules
- workspace-wide fuzzy search: `search_work_items`
- project health snapshot:
  - `list_cycles`
  - `list_modules`
  - `list_work_items`
  - `get_project_worklog_summary`
- blocker analysis:
  - `list_work_items`
  - `list_work_item_relations`
  - `list_work_item_activities`

## Practical Gaps To Call Out

Do not overpromise these areas from the current MCP tool surface:

- dashboards are a Plane product capability, but no dedicated dashboard MCP tools are exposed here
- layout views exist in the product, but not as direct MCP-managed objects here
- attachments and file uploads are not represented in the available Plane MCP tools here
- notifications, inbox, and command palette behavior are not exposed as MCP actions here
- approval gates, SSO admin, and broader instance governance are not represented in the current tool surface
- workflows/approvals, customers, teamspaces, recurring work items, saved templates, custom SLAs, and AI agents/search/summaries are Business capabilities but do not currently have dedicated MCP object tools here
- Plane page maintenance is partial because create/retrieve exist, but list/update/delete are not available here

When a request lands in one of these gaps, say that clearly and either:

- fall back to the closest supported Plane operation, or
- move the durable narrative to Outline if that is the safer fit

## Source Notes

- Plane open-source product page: projects, docs, cycles, intake, layout views, dashboards, estimates, REST API, and webhooks
- Plane developer docs: project and work item API references
- Plane MCP server docs and official GitHub README: transport setup and tool category coverage
- Plane Business page checked on 2026-05-22 for current Business-only features and product-language capability list

Use live MCP behavior as final truth when docs and environment differ.
