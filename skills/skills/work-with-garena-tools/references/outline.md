# Outline

Use for Garena Outline at `wiki.odp.garena.vn`: reading pages, managing collections/documents, comments, attachments, and safe documentation updates.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `outline_fetch`
- `outline_list_collections`
- `outline_list_documents`
- `outline_list_collection_documents`
- `outline_create_collection`
- `outline_update_collection`
- `outline_delete_collection`
- `outline_create_document`
- `outline_update_document`
- `outline_move_document`
- `outline_delete_document`
- `outline_list_comments`
- `outline_create_comment`
- `outline_update_comment`
- `outline_delete_comment`
- `outline_create_attachment`

The 2026-06-15 MCP admin screenshot showed 17 tools, so discover the live surface before assuming this list is complete.

## URL Resolution Workflow

1. Parse `wiki.odp.garena.vn` doc URLs for the doc slug/urlId when present.
2. List collections and documents to resolve the exact page.
3. Prefer matching by stable id/urlId over title.
4. Read the exact document before summarizing or updating.
5. For subtree work, list the collection tree and stay scoped to the requested branch.

## Write Workflow

1. Re-read the latest target page immediately before writing.
2. Preserve existing structure, headings, tone, and local conventions.
3. For create-document actions, check siblings and collection-wide candidates to avoid duplicates.
4. Preview multi-page, canonical, destructive, or bulk edits before mutation.
5. After writing, re-read the page and report what changed.

## Safety

- Never guess a page target from memory.
- Never delete/move/archive without explicit intent.
- Keep canonical pages clean: stable truth only, not session logs or temporary execution notes.
- For complex Outline workflows, the older `work-with-outline` skill has deeper reference material and can be used as a companion.
