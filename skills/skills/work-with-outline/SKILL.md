---
name: work-with-outline
description: Read, inspect, and safely update Garena Outline knowledge-base content at `wiki.odp.garena.vn` through the gateway-exposed Outline tool family, typically via `mcp__garena_vn_mcp_gw`. This is the role-first name replacing `outline-workflow`.
---

# Work With Outline

Use this skill whenever the user is working against Garena Outline pages or pastes a `wiki.odp.garena.vn` link.

## Connection Rule

- Treat `Outline`, `wiki.odp.garena.vn`, and pasted Outline doc links as the same system.
- Use the live Outline tool family exposed in the current session as the primary connection method. In the current Garena setup this is usually the `outline_*` tool family exposed through `mcp__garena_vn_mcp_gw`.
- Treat operation names in this skill such as `list_collections` or `get_document` as logical operations. Resolve the exact callable tool ids from the active tool surface first.
- If the needed Outline tool family is not exposed in the current session, stop and say the gateway/tool surface is unavailable instead of pretending the standalone `outline` server still exists.
- Do not browse the site as a normal webpage when the Outline tool family can answer the task.
- Resolve pages through the Outline tool family before making any statement about page identity, tree placement, or edit targets.
- Distinguish between `MCP-visible state` and `web UI render state`.
- If MCP shows the latest content but the website still looks stale, treat that as possible UI cache or render delay until proven otherwise.

## Quick Start

- If the user pastes an Outline doc URL, build context from the target page plus its descendants only.
- If the user asks to read a child page, stay scoped to that child subtree unless they ask to expand.
- If the user asks to update Outline, identify the exact target page through MCP, re-read it, preview the intended change, then write only when the request is explicit enough and safe.

## Working Modes

Choose the mode first before deciding how far to read or scan.

- `context bootstrap`: understand a project or page from the target node plus descendants
- `targeted read/write`: inspect or update one page or a small known set of pages
- `defect scan / bulk repair`: inspect a subtree for repeated formatting, link, or markup defects

Do not reuse the read-depth rule from one mode inside another mode by accident.

## Deterministic Read Workflow

For any Outline doc URL:

1. Parse the URL and extract:
   - `urlId` from `/doc/<slug>-<urlId>`
   - the relative doc path when available
2. Resolve the document through MCP only.
3. Preferred lookup path:
   - call `list_collections`
   - for each visible collection, call `list_documents`
   - match the target by `urlId` first, then by relative `url`
4. Once matched, call `get_document` on the exact document id.
5. Call `get_collection_documents` for the document's collection.
6. Find the node in the collection tree whose id matches the target document.
7. Read only that node and its descendants.

Default boundaries:

- Do read the target page content.
- Do read descendants in the target subtree.
- Do not read parent nodes by default.
- Do not read sibling branches by default.
- Do not read unrelated pages in the same collection by default.
- Do not auto-follow inline links in the page body unless:
  - the user explicitly asks, or
  - the linked page is already inside the resolved subtree and directly needed.

If the page cannot be resolved from visible collections, stop and say it could not be found from current MCP visibility instead of guessing.

See [read-scope.md](./references/read-scope.md) for the detailed lookup and subtree rules.

## Default Context Output After A Pasted Link

After reading the target page and subtree, summarize the context in this order:

1. Exact page identity:
   - title
   - collection
   - page id or `urlId` when useful
   - page role if the body exposes one, such as hub, canonical, operational, archive, or workstream
2. Root page purpose:
   - what the page is for
   - what it is not for, if stated
3. Child-tree structure:
   - useful subtree outline
   - notable descendants grouped by purpose
4. Reading guidance:
   - any explicit reading order, AI reading guide, or update bundle rule found on the root page
5. Scope boundary:
   - what was intentionally not read because it was outside the subtree

When useful, call out which descendants appear to be:

- canonical/source-of-truth pages
- hubs/navigation pages
- operational/user guide pages
- archive/history pages
- workstream/planning pages

## Safe Write Workflow

Before any write:

1. Resolve the exact page through MCP.
2. Re-read the latest page content immediately before writing.
3. Inspect the current page policy/capabilities from `get_document` before assuming the action is available.
4. Identify whether the target page itself defines owner/canonical/update-bundle guidance.
5. If companion pages are implied, enumerate them before changing anything.
6. Preview the intended update:
   - target page(s)
   - section(s) to update
   - concise draft of what will change
7. Write only when the user's request is explicit enough to safely apply.
8. After writing, re-read the updated page and verify the result.
9. If MCP verification passes but the user still sees stale content in the website, report that the saved state is correct on MCP and call out likely UI delay/cache.

Canonical page approval rule:

- If a target page has `Role: Canonical` or the user calls it a canonical page, always send the proposed canonical edit draft first and wait for explicit user approval before writing, even when the user asked to update the page.
- Canonical page edits must describe stable current truth only. Do not write work history, session summaries, commit logs, verification logs, temporary TODOs, or dated execution notes into canonical pages unless the page explicitly defines itself as a changelog or decision log.
- If the canonical page is polluted with work history, propose a clean replacement or section cleanup that preserves durable truth and moves no history into the canonical page.

Default safety rules:

- Never write from stale session memory alone.
- Never guess the target page if MCP resolution is unclear.
- Never assume a permission implied by policy is fully exposed by the current MCP tool surface.
- Never overwrite an entire document when a section update or append is sufficient.
- Preserve existing headings, structure, tone, and local conventions.
- Never delete, archive, move, or restore unless the user explicitly asks for that exact destructive action.
- If the user asks vaguely to "clean up" or "organize" Outline, require a concrete page target and exact intended action.

## No Duplicate Page Creation Gate

This gate is mandatory before every create-document action and before any plan that would create more than one page.

1. Resolve the intended parent page through MCP.
2. Inventory the current sibling set under that exact parent.
3. Search the visible collection for existing candidates using:
   - the exact intended title
   - the title without numeric prefix, for example `06.03.01 Workflow` -> `Workflow`
   - any known old title, menu label, or user-provided URL title
4. Compare candidates by normalized title:
   - trim whitespace
   - ignore numeric ordering prefixes like `00.`, `06.03.`, or `02.01.01`
   - ignore punctuation-only differences such as hyphen, dash, slash spacing, or casing
   - treat translated or near-equivalent module labels as possible duplicates until inspected
5. If any candidate page exists, re-use it by link, rename, or move instead of creating a new page.
6. If the matching page already contains useful content, never create a placeholder for the same surface. Keep the content page canonical and adjust hub links or tree position around it.
7. If a search result is truncated, errors, or cannot prove the target is absent, stop and report uncertainty instead of creating.
8. Preview the negative evidence before creation:
   - parent checked
   - sibling titles checked
   - collection-wide candidate titles checked
   - why none are the same page
9. Create only after the absence check is explicit and the request is still safe.

For menu/tree reorganization, prefer this order:

1. rename existing pages
2. move existing pages
3. update hub links
4. create a new page only when the audited tree has no existing page or near-duplicate

Never create placeholder pages merely to make a planned menu look complete. A missing detail can be represented as a TODO/link in the hub until the canonical target is confirmed.

## Page Body Hygiene

Apply these rules unless the local subtree clearly uses a different established convention:

- If Outline already renders the document title in the page chrome, do not repeat the same text as an identical `H1` in the body.
- Start the body with the metadata block or the first meaningful section such as `Purpose`, `Summary`, `How To Read This Page`, or `Workflow chính`.
- For user-facing guides, onboarding pages, operational help, and FAQ content, default to Vietnamese with diacritics.
- For those same user-facing pages, use non-tech wording and describe actions from the operator's point of view.

See [safe-operations.md](./references/safe-operations.md) for the full guardrails.

## Batch Repair Workflow

Use this workflow when the user asks to fix a repeated documentation problem across one Outline subtree, for example broken links, malformed markup, stale host links, or repeated formatting damage.

1. Resolve the subtree root through MCP.
2. Keep the scan scoped to that subtree only, but allow every descendant branch under that subtree, including archive or workstream leaves if they are descendants.
3. Convert the user symptom into a scan signature:
   - visible screenshot text
   - likely defect type
   - likely section position such as page header, metadata block, table, list, or inline body text
4. Inventory candidate pages that match the broken pattern.
5. When the tree has multiple branches, sample across branch types before claiming the subtree is clean.
4. State the repair rule once, for example:
   - replace malformed pseudo-markup with normal markdown links
   - replace stale host links with live Outline links
   - normalize one repeated heading or section format
6. Produce a preview batch:
   - affected pages
   - affected sections
   - exact normalization rule
7. State the important user-facing cautions before any write:
   - exact subtree scope
   - pages that will be edited
   - what kinds of content will not be touched
   - likely impact if the batch is wrong, such as many links or references changing at once
8. State scan confidence explicitly:
   - sampled scan
   - high-signal scan
   - exhaustive subtree scan
9. Stop and require explicit user confirmation before the first batch write.
10. Apply the repair page by page with minimal edits.
11. Re-read each updated page and confirm the broken pattern is gone.

Default bulk-fix limits:

- do not widen outside the requested subtree
- do not rewrite unaffected prose
- do not combine unrelated cleanup into the same batch
- if multiple broken patterns exist, handle one pattern at a time
- for any multi-page batch, confirmation is mandatory even if the user already asked to "fix all"
- do not say "the subtree is clean" unless scan coverage is explicit
- do not let page role assumptions such as hub, canonical, or archive determine whether a descendant branch is scanned for defect work

## Decision Rules For Common Requests

If the user asks to bootstrap context from a project link:

- read the root page plus descendants only
- do not expand to parent app/platform pages
- do not expand to sibling projects

If the user asks to read a page under an existing project:

- stay within that page's subtree
- do not jump back to the project root unless asked or required to resolve ambiguity

If the user asks to sync or update docs after a product/code change:

- prefer the owner or canonical page first if the docs indicate one
- identify any companion docs named by local update rules, such as data contracts, user guide, workstreams, or build history
- preview the full update bundle before mutation

If the user asks for a spec, user guide, changelog, or progress update in Outline:

- resolve the exact page through MCP
- use the existing structure on that page
- preview the proposed section changes before writing unless the user already specified exact target content and page

If the user asks to create a new page under an existing page:

- check the target page policy for child-creation capability
- run the mandatory `No Duplicate Page Creation Gate` before any create-document action
- then check whether the current MCP tools actually expose a way to set `parentDocumentId`
- if the policy allows child creation but MCP only exposes collection-level `create_document`, say that clearly instead of implying the action is impossible
- do not create a root-level page as a substitute unless the user accepts that fallback
- if the target branch uses numeric ordering in sibling titles, inspect the existing sibling set first and insert the new page at the correct numeric position instead of appending it blindly
- after creating or moving a page inside a numerically ordered branch, verify the sibling order again and normalize it if the new page landed out of sequence
- when the branch contains mixed bands such as `01`, `10`, `20`, `24`, `30`, `90`, preserve the established ascending order of those numeric bands

If the user asks whether a recent fix "still looks wrong":

- re-read the exact page through MCP first
- compare MCP content with the reported UI symptom
- distinguish content-not-saved from likely UI cache/render delay
- use exact timestamps from MCP when useful

If the user asks to fix Outline pages in bulk:

- scan only the requested subtree for the repeated pattern
- derive the scan signature from the screenshot or symptom, not just from page role labels
- inventory affected pages before mutation
- define one repair rule per batch
- state scan confidence and coverage before concluding that nothing else is affected
- preview the batch, state impact and scope cautions, and require explicit confirmation
- only then repair with minimal edits
- verify the pattern is removed after each update

## References

- [read-scope.md](./references/read-scope.md): URL parsing, lookup path, subtree resolution, and fallback behavior
- [safe-operations.md](./references/safe-operations.md): write safety, bundle-awareness, and destructive-action guardrails
- [format-defects.md](./references/format-defects.md): repeated formatting defect patterns, scan signatures, and stable normalization targets
