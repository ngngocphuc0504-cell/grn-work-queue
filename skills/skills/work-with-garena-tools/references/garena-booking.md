# Garena Booking

Use for booking request search, request detail, pending approvals, and updating approval status.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `garena_booking_advanceSearch`
- `garena_booking_getRequestDetail`
- `garena_booking_getPendingMyApproval`
- `garena_booking_updateRequestStatus`

The 2026-06-15 MCP admin screenshot showed 5 tools, so discover the live surface before assuming this list is complete.

## Workflow

1. Use pending-my-approval for approval inbox work.
2. Use advanced search for historical or fuzzy lookup.
3. Read request detail before interpreting requester, approver, schedule, cost, or status.
4. For status updates, state the target request and new status clearly, then verify by re-reading detail or approval inbox.

## Safety

- Approval/status update is a high-impact mutation. Require explicit user intent.
- Do not approve/reject based only on a search row.
- If an approval requires business judgment not provided by the user, surface the relevant facts and ask for the decision.
