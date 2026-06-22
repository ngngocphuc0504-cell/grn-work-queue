# Safe Operations

Use this file before reading for actionability or making any Outline mutation.

## Core Rules

- Always resolve the exact target page through MCP before acting.
- Always re-read the latest target page immediately before writing.
- Never write from stale session memory alone.
- Never assume the last page discussed is still the correct target.
- Always separate `permission visible in policy` from `mutation actually exposed by current MCP tools`.

## Preview Before Mutation

Default mode is `explicit + preview`.

Before writing, state:

- target page(s)
- why those pages are the right targets
- section(s) to update
- concise preview of the intended content

If the user request is broad or inferred, wait for confirmation after the preview.

If the user already gave an exact page and exact content, a compact preview is still preferred, then proceed only if the request is clearly actionable and low-risk.

For create or move operations, also state:

- whether the requested parent or location can be targeted directly through the current MCP tools
- whether the proposed action is exact or only a fallback
- for create operations, the exact duplicate-prevention evidence:
  - parent page checked
  - sibling titles checked
  - collection-wide candidate titles checked
  - normalized title comparisons checked
  - reason no existing page can be reused

Never create when duplicate-prevention evidence is incomplete. If MCP search is truncated, errors, or cannot prove absence, stop and ask for confirmation or broaden read-only audit instead of creating.

For batch repairs, also state:

- the defect pattern being fixed
- the normalization target format
- one short before/after example when practical

## Owner And Canonical Preference

When docs define local source-of-truth rules:

- prefer updating the owner or canonical page first
- treat hub pages as navigation unless the docs explicitly say they are the owner page
- do not put detailed behavior into a hub page if the docs route that information elsewhere

If the page defines an `Update Bundle Rule` or similar policy, follow it.

## Update Bundle Awareness

When a change appears to affect multiple pages:

- identify companion pages before writing
- preview the full update bundle
- keep each page aligned with its intended role

Common companion pages may include:

- canonical product or module pages
- data contracts or data model pages
- user guide or operational docs
- workstream pages
- build history or archive pages

Do not silently update only one page when the local documentation rules imply several.

## Minimal Change Principle

- Prefer section-level edits or append operations.
- Do not rewrite the whole document unless the user explicitly requests a rewrite.
- Preserve existing headings, order, style, and wording conventions where practical.
- Avoid removing existing content unless the user explicitly asks or the replacement clearly supersedes it.
- If testing is needed, prefer creating clearly-labeled temporary pages over touching live pages.

## Duplicate Prevention For Page Creation

Before creating any Outline page:

- Resolve the intended parent and inspect its current children.
- Search the collection for the exact intended title and the title without numeric prefix.
- Normalize compared titles by removing numeric prefixes, trimming whitespace, ignoring punctuation-only differences, and lowercasing.
- Treat same-surface labels as duplicates even if one is a companion spec, tab label, or Vietnamese/English variant until the page body proves otherwise.
- If an existing page has real content for the same surface, keep it canonical. Use rename, move, or hub-link updates rather than creating a placeholder.
- If the desired tree structure requires a page but existing content is combined inside another page, do not split or duplicate automatically. Preview the options and get explicit user confirmation.
- For bulk organization, create no pages until the full target subtree has been audited and candidate duplicates have been listed.

Creation is allowed only after the response or notes make clear which existing pages were checked and why none can be reused.

## Batch Repair Rule

For repeated defects across multiple pages:

- identify one repair pattern at a time
- inventory the affected pages before editing
- state the normalization rule before the first write
- state the batch scope in user language before the first write
- list the exact pages that will be edited before the first write
- state what will explicitly not be touched in that batch
- call out the practical impact if the batch is wrong, such as broad link damage or cross-page inconsistency
- require explicit user confirmation before the first batch write
- keep each page change as small as possible
- do not mix link repair, content refresh, and structural cleanup in one batch unless the user explicitly wants that
- after each page update, verify that the target pattern is removed and the intended links or formatting render correctly

For multi-page changes, "the user already asked to fix it" is not enough to skip confirmation.

## Scan Confidence

When reporting a scan result, label it as one of:

- `sampled scan`
- `high-signal scan`
- `exhaustive subtree scan`

Do not say "no more issues found in the subtree" unless scan coverage is explicit.

## Destructive Actions

Treat these as destructive:

- delete
- archive
- unarchive
- move
- restore

Never perform them unless the user explicitly requests:

- the exact action
- the exact target page or collection

If the request is vague, stop and ask for the precise target and action.

## Verification After Write

After any write:

1. Re-read the updated page through MCP.
2. Verify the intended content is present.
3. Check that surrounding structure still makes sense.
4. Check that the new format is renderer-stable and not relying on fragile plain newlines.
5. If the user reports that the website still looks stale, compare MCP state against the UI symptom and call out likely UI delay or cache when appropriate.
6. Report what changed and what companion pages, if any, still need follow-up.

## Unsafe Requests

Do not act directly on requests like:

- "dọn outline"
- "sắp xếp lại outline"
- "xóa bớt"
- "fix giúp docs này"

unless the request also specifies:

- exact page targets
- intended scope
- whether the action is additive, corrective, reorganizing, or destructive

When unsafe, narrow the task first instead of guessing.
