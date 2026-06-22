# Creative Lab

Use for Creative Lab requests, request lookup, current-user checks, and request-detail inspection.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `creative_lab_get_current_user`
- `creative_lab_search_requests`
- `creative_lab_get_request_detail`

The 2026-06-15 MCP admin screenshot showed 3 tools, matching this discovered list.

## Workflow

1. Confirm the user identity only when access or requester scope matters.
2. Search requests before fetching a detail page unless the user provides a stable request id.
3. Fetch the exact request detail before summarizing state, ownership, due dates, attachments, or blockers.
4. For ambiguous names or keywords, return candidate matches with enough identifying fields for the user to choose.

## Safety

- Treat search results as candidates, not final truth.
- Do not infer approval, delivery, or SLA status without reading the detail object.
- If the user asks for a mutation and no Creative Lab mutation tool is exposed, say the current MCP surface appears read-only.
