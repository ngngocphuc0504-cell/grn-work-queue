# Routing

Use this file to choose the right `garena-vn-mcp-gw` tool family before loading a deeper reference.

## First Principles

- Treat `garena-vn-mcp-gw`, `mcp__garena_vn_mcp_gw`, and the Garena MCP gateway as the same connection.
- Treat child MCP names in the admin UI as tool families, not final callable names.
- Resolve callable names from the live tool surface for each session. If a family is missing or partial, report the gap instead of guessing.
- Prefer the purpose-built MCP family over browsing internal websites.
- Use browser/CDP only for visual verification, login-only UI state, or functionality not exposed through MCP.

## Alias Map

| User says | Load |
|---|---|
| `wiki.odp.garena.vn`, Outline, wiki, KB, doc page | `outline.md` |
| Plane, `managetask.odp.garena.vn`, task, issue, backlog, cycle, module, milestone | `plane.md` |
| Demo System, deploy app, deploy, logs, public URL, database, managed DB | `deploy-app.md` |
| Creative Lab, creative request, request detail | `creative-lab.md` |
| Datcom, lunch, meal, menu, order, preorder | `datcom.md` |
| Booking, approval, booking request | `garena-booking.md` |
| Vendor, partner, order detail, pending signature, sign file | `garena-vendor.md` |
| GIGI, chat/search assistant, "check gigi" | `gigi.md` |
| Google Drive, Drive file/folder/doc/sheet/slide | `google-drive-mcp.md` |
| server, database, Redis, alert, monitor, certificate, port, infra | `infra-knowledge.md` |

## Screenshot Snapshot From 2026-06-15

The MCP admin screenshot showed these enabled child MCPs and counts:

| Family | Count |
|---|---:|
| creative-lab | 3 |
| datcom | 14 |
| deploy-app | 16 |
| garena-booking | 5 |
| garena-vendor | 9 |
| gigi | 8 |
| google-drive-mcp | 13 |
| infra-knowledge | 20 |
| outline | 17 |
| plane | 109 |

Counts are inventory hints only. Trust the current callable surface at execution time.

## Cross-System Routing

Read `cross-tool-workflows.md` when the request spans more than one system, for example:

- Create tasks in Plane from an Outline spec.
- Update Outline after Plane delivery movement.
- Deploy an app, then record URL/status in Outline or Plane.
- Investigate infra alerts for a deployed service.
- Pull Drive files into an Outline/Plane workflow.

## Missing Or Partial Tool Surface

When a family is expected but callable names are not visible:

1. Use the available tool-discovery surface first.
2. Search by family aliases and likely prefixes, for example `outline`, `plane`, `gigi`, or `infra_knowledge`.
3. If discovery still fails, state the family is enabled in the MCP admin snapshot but not currently exposed to this session.
4. Do not fabricate tool names.
