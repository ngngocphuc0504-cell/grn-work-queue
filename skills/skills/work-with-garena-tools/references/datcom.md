# Datcom

Use for Datcom food ordering, menus, available meals, preorders, current orders, and meal cancellation.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `datcom_get_current_user`
- `datcom_get_available_meals`
- `datcom_view_menu`
- `datcom_view_my_preorders`
- `datcom_preorder_meals`
- `datcom_preorder_meal`
- `datcom_order_meals`
- `datcom_remove_order`
- `datcom_remove_preorder`

The 2026-06-15 MCP admin screenshot showed 14 tools, so discover the live surface before assuming this list is complete.

## Workflow

1. Resolve current user when the action is personal, such as viewing orders or preordering.
2. For menu questions, read available meals or menu for the target date/session.
3. For preorders/orders, show the candidate meal, date, quantity, and cutoff-related detail before mutating.
4. After ordering, preordering, or removing, re-read the user's active orders/preorders when the tool surface supports it.

## Safety

- Never place or remove an order from a vague request.
- If the user says "order this" from prior context, repeat the meal/date/quantity in the confirmation summary after execution.
- Treat same-day order and preorder as distinct concepts.
