# Read Scope

Use this file when resolving an Outline link or deciding how far to read.

## URL Parsing

Supported default target:

- Outline document URLs in the form `https://wiki.odp.garena.vn/doc/<slug>-<urlId>`

Resolution fields:

- `urlId`: the suffix after the last hyphen in the doc path
- relative `url`: for example `/doc/social-listening-ngIWEVuwP0`

Prefer matching by `urlId`. Use relative `url` as fallback.

## Preferred Lookup Path

Use the live Outline tool family only.

Treat operation names below as logical names. In the current Garena setup the callable tool ids are usually namespaced as `outline_*` through `mcp__garena_vn_mcp_gw`.

1. Call `list_collections`.
2. For each visible collection, call `list_documents`.
3. Search each returned document for:
   - exact `urlId` match first
   - exact relative `url` match second
4. Once found, record:
   - document id
   - collection id
   - title
   - parent document id if present
5. Call `get_document` for the exact document.
6. Call `get_collection_documents` for the collection tree.

Also use `get_document` as the primary source for:

- `updatedAt` and revision recency
- `parentDocumentId`
- available page-level abilities or policy signals when deciding whether a follow-up mutation is realistic through the current MCP surface

Do not identify the page from title-only matching when a doc URL was provided.

## Subtree Resolution

Given the collection tree from `get_collection_documents`:

1. Traverse the tree until node `id == target document id`.
2. Treat that node as the subtree root.
3. Read:
   - the target page content from `get_document`
   - descendants discovered in that subtree
4. Do not read:
   - ancestors of the subtree root
   - siblings of the subtree root
   - nodes outside the subtree root

If the tree is large, summarize descendant structure first and only open child pages that are likely needed for the current user request.

## Root Project Link Behavior

When the pasted page is the root project entry page:

- read the root page
- inspect the descendants under that page in the collection tree
- build context from that subtree only
- do not read parent app/platform pages
- do not read sibling projects in the same collection

Example:

- If the root page is `Social Listening`, do not read parent `Application` or sibling apps like `Communication Tool` unless the user asks.

This boundary is for `context bootstrap`.

Do not reuse it blindly for subtree defect scans.

## Child Page Link Behavior

When the pasted page is a child page under a project:

- treat that child page as the subtree root
- read the child page plus its descendants only
- do not jump back to the project root unless:
  - the user asks to widen scope, or
  - the child page itself lacks enough context to identify its purpose and the parent is strictly necessary

If widening scope is necessary, say that you are expanding scope and why.

## Inline Links Inside Page Bodies

Default policy:

- do not follow inline links automatically

Allowed exceptions:

- the user explicitly asks to follow them
- the links point to descendants already inside the resolved subtree and they are directly needed for the task

Not allowed by default:

- following cross-links to parent hubs
- following cross-links to sibling branches
- following cross-links to archive/workstream areas just because they are mentioned

## Pages With No Descendants

If the target page is visible but has no descendants:

- read only that page
- say that the current page appears to have no child tree under the resolved node
- do not widen to neighbors to compensate

## Subtree-Limited Bulk Scan

When the user asks to fix repeated issues in a project subtree:

1. Resolve the subtree root.
2. Collect only descendant pages under that root.
3. Search for the broken pattern only within those pages.
4. If the subtree contains multiple branches, cover more than hubs:
   - sample leaf pages as well as index pages
   - include archive and workstream descendants when they are inside the subtree
   - do not stop at first-level hubs if the defect may live in leaves
4. Exclude:
   - ancestors
   - sibling branches
   - unrelated projects in the same collection

If the broken pattern is found outside the subtree as well, ignore those pages unless the user expands scope.

For defect scans, report scan confidence explicitly:

- `sampled scan`: only a subset of branches or leaves was checked
- `high-signal scan`: all major branches were checked, but not every leaf
- `exhaustive subtree scan`: all discovered descendants in the subtree were checked

Do not claim the subtree is clean without naming the confidence level.

## Page Not Found

If the page cannot be found from visible collections/documents:

- say the page could not be resolved from the current tool visibility
- if the Outline tool family itself is missing from the current session, say the gateway/tool surface is unavailable before doing anything else
- do not guess using title similarity alone
- do not switch to generic website browsing as the primary fallback
- if useful, report which collections are currently visible through the tool surface

## UI Delay And Render Mismatch

If the user says a page still looks wrong after a write:

1. Re-read the exact page with `get_document`.
2. Compare the tool-returned text with the reported UI symptom.
3. Report one of these states explicitly:
   - content is still wrong in the tool-returned document state
   - content is correct in the tool-returned document state and the website may be showing stale UI/render output
4. Use exact timestamps when useful.

Do not assume the website is the source of truth for save verification when the tool-returned document state already shows the update.

## Child Creation Scope Check

When the user asks to create a child page under an existing page:

1. Resolve the intended parent page.
2. Inspect `get_document` for parent-page abilities such as child creation.
3. Check the currently exposed tools before promising the action.
4. If the current tool surface only supports collection-level creation and does not expose `parentDocumentId`, say that the limitation is in the current tool surface, not necessarily in Outline permissions.

If a root-level fallback is considered:

- say it is a fallback
- say where the page will actually be created
- do not proceed unless the user accepts that scope

## Screenshot-Derived Scan Signature

If the user provides a screenshot of an Outline defect:

1. Extract visible tokens from the screenshot.
2. Identify the likely defect zone:
   - page header metadata
   - list
   - table
   - inline link block
   - body paragraph
3. Build search terms from the screenshot text itself before relying on page-role assumptions.
4. Use those terms to find similar pages in the subtree.

Examples of useful signature terms:

- `Document Role:`
- `Status:`
- `Owner:`
- `Last Verified:`
- `Ngày build:`
- `Người build:`
- `Trạng thái:`
- `Tóm tắt thay đổi:`
