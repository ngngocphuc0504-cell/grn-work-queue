# Target Resolution

## Purpose

Resolve the exact Outline target and classify the task before reading deeply or drafting any restructure bundle.

## Allowed Targets

- an existing project collection
- an existing root project page
- an existing child subtree inside a project
- a new project collection or page that needs a full scaffold

## Resolution Workflow

1. If the user pastes an Outline doc URL, resolve that exact page first.
2. If the user names a collection or page vaguely, search the gateway-exposed Outline tool family and match by exact title and surrounding context.
3. If multiple plausible matches exist, show the candidates and stop.
4. Once matched, read the target page and its descendants only.
5. Identify whether the target acts as:
   - project root
   - hub page
   - owner page
   - archive subtree
   - child subtree needing local repair only

## Mode Selection

Choose `bootstrap new collection/page` when:

- the target does not exist yet, or
- the user explicitly asks for a new project knowledge-base skeleton

Choose `reorganize existing project KB` when:

- the target already exists and has enough content to preserve
- multiple pages need role cleanup, reparenting, or archive work

Choose `repair stale structure` when:

- the tree mostly exists already
- the main problem is stale naming, duplicate pages, broken reading paths, or outdated owner boundaries

Choose `inventory only` when:

- the user only wants analysis, mapping, or a change preview
- the user has not approved mutation yet

## Scope Boundaries

- Root page input: read root + descendants only.
- Child page input: read child subtree only unless a parent hub is required to understand ownership.
- Collection input: read only that collection tree.
- Never expand to sibling projects by default.

## New vs Existing Decision Test

Treat the target as `new scaffold` only when at least one of these is true:

- the collection or page does not exist yet
- the target exists only as a placeholder without meaningful project content
- the user explicitly wants a brand-new project KB

Otherwise treat it as `existing restructure`.

