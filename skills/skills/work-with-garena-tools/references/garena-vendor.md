# Garena Vendor

Use for Garena Vendor workflows: partner/vendor lookup, request detail, order detail, pending signatures, and file signing.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `garena_vendor_getCurrentUser`
- `garena_vendor_advanceSearch`
- `garena_vendor_getRequestDetail`
- `garena_vendor_getOrderDetail`
- `garena_vendor_getPartnerDetail`
- `garena_vendor_getPendingMySignatures`
- `garena_vendor_signFile`

The 2026-06-15 MCP admin screenshot showed 9 tools, so discover the live surface before assuming this list is complete.

## Workflow

1. Resolve current user for signature inbox or permission-sensitive work.
2. Search by request/order/partner identifiers before reading detail.
3. Fetch detail object before summarizing contract, partner, order, or signature status.
4. For signing, read pending signature detail and identify the exact file, request, and consequence.
5. After signing, re-read pending signatures or the target request detail.

## Safety

- Signing is a high-impact mutation. Require explicit user instruction naming the target or accepting the identified candidate.
- Never sign based on a fuzzy search result alone.
- If business/legal approval is unclear, summarize facts and ask for a decision.
