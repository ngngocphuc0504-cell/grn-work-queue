---
name: organize-project-kb
description: >
  Organize or reorganize project knowledge bases on Outline into a clear owner-based structure.
  Use when Codex needs to: (1) inventory an existing project collection or page subtree,
  (2) preview a restructure bundle before mutating docs, (3) scaffold a new project knowledge base
  with UGC-style root, canonical, operational, team, archive, and agent-prep pages,
  (4) normalize reading paths, metadata blocks, module catalogs, and owner boundaries,
  or (5) archive stale or superseded pages without deleting original information unless it is clearly wrong or outdated.
---

# Organize Project KB

Use the gateway-exposed Outline tool family as the only source of truth for discovery and mutation in this skill.

## Connection Rule

- Treat `Outline`, `wiki.odp.garena.vn`, and project knowledge bases as the same system.
- Use the live Outline tool family exposed in the current session for all reads and writes. In the current Garena setup this is usually the `outline_*` tool family exposed through `mcp__garena_vn_mcp_gw`.
- Resolve the exact callable tool ids from the active tool surface first. If the Outline tool family is missing, stop and report the unavailable gateway/tool surface instead of assuming a standalone server still exists.
- Do not browse Outline as a normal webpage when the Outline tool family can answer.
- Resolve the exact target page or collection before making structure claims.

## Working Modes

Choose one mode before reading deeply or writing anything.

- `bootstrap new collection/page`
- `reorganize existing project KB`
- `repair stale structure`
- `inventory only`

Read [target-resolution.md](./references/target-resolution.md) first to resolve the target and pick the mode.
Read [restructure-rules.md](./references/restructure-rules.md) before any structural decision.
Read [scaffold-template.md](./references/scaffold-template.md) when the target needs a new skeleton.
Read [page-templates.md](./references/page-templates.md) before drafting or rewriting pages.
Read [apply-checklist.md](./references/apply-checklist.md) before previewing or applying changes.

## Required Workflow

1. Resolve the target exactly through the Outline tool family.
2. Classify the task as `bootstrap new`, `existing restructure`, `stale repair`, or `inventory only`.
3. Inventory only the relevant subtree:
   - current page roles
   - likely owner pages
   - duplicate or conflicting pages
   - live, stale, archive, and superseded candidates
4. Build a preview bundle before any mutation:
   - pages to create
   - pages to rewrite or repurpose
   - pages to move or archive
   - pages to keep but demote from the default reading path
5. Stop and require explicit user confirmation before applying any restructure or scaffold write.
6. After applying, re-read owner pages and key hub pages to verify final structure, links, and role boundaries.

## Scope Rules

- Stay scoped to the requested collection, root page, or subtree.
- Do not widen to sibling projects or parent app/platform trees unless the user explicitly asks.
- If the user provides a root project page, read that page plus descendants only.
- If the user provides a child page, stay inside that subtree unless the task cannot be completed without the parent.

## Core Structure Rules

- Root project page name should stay human-readable and should not use a numeric prefix.
- Child hub pages should follow the UGC-style numbered bands from [scaffold-template.md](./references/scaffold-template.md).
- When a branch uses numeric prefixes, never rely on creation time or default append order. Inspect sibling titles first, then place each new page at the correct numeric index.
- After creating, moving, or archiving pages in a numbered branch, verify the final sibling order and normalize it so the displayed tree stays ascending by number.
- Every live owner page should start with a metadata block.
- Each type of truth should have one owner page only.
- Archive pages should preserve provenance but never drive the default reading path.
- If a project has a heavy operator-facing guide, prefer a dedicated subtree `24 Operational — User Guide` instead of burying long guides inside `20 Operational — Current State`.
- Inside `24 Operational — User Guide`, prefer semantic titles that still keep sort order:
  - foundation pages: `00 User Guide — ...`
  - module pages: `10 Module Guide — <Module>`
  - deeper child pages: `<Module> — <Workflow>` or `<Module> — <Area>`, not generic names like `Intake & Review` without the module name.
- For Outline pages, do not duplicate the document title as an identical `H1` in the page body. Start with the metadata block, then the first meaningful section such as `Purpose`, `Summary`, or `How To Read This Page`.
- User-facing guides should default to Vietnamese with diacritics and non-tech wording unless the local subtree has an explicit different convention.

## Safety Rules

- Never delete original information just because it is old.
- Archive instead of delete when provenance still matters.
- Delete only when the content is clearly wrong or outdated and archival value is negligible.
- Prefer `archive + pointer` over hard removal when a page was recently live or is likely still linked elsewhere.
- If a page is still reusable, repurpose it before creating a brand-new page with the same meaning.
- Do not leave two live pages owning the same truth.
- Do not turn archive pages into current truth by linking to them as default next reads.
- When reorganizing an active project, preserve existing information first and restructure around owner boundaries rather than “starting over”.

## Mutation Discipline

- Default mutation style is `preview then apply`.
- A restructure preview must be concrete enough that the user can see the intended tree and each affected page category.
- Do not apply changes after an `inventory only` request.
- Do not apply structural changes from session memory alone; always re-read the target subtree immediately before writing.
- If the apply step creates or moves pages inside a numbered branch, treat sibling reordering as part of the same apply bundle rather than as an optional cleanup afterward.

## Output Discipline

- For inventory: summarize the current tree, role map, conflicts, and restructure candidates.
- For preview: show the change bundle grouped by `create`, `rewrite`, `archive`, and `keep`.
- For apply: report what changed, what stayed live, what moved to archive, and what still needs human review.

