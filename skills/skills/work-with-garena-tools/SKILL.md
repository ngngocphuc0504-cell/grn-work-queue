---
name: work-with-garena-tools
description: >
  Route Garena internal-tool requests through the gateway MCP `garena-vn-mcp-gw` / `mcp__garena_vn_mcp_gw`.
  Use when the user mentions MCP, gateway tools, `wiki.odp.garena.vn`, Outline, Plane, `managetask.odp.garena.vn`,
  Demo System/deploy app, Creative Lab, Datcom, Booking, Vendor, GIGI, Google Drive MCP, Infra Knowledge,
  or asks to check/read/update/create through an internal Garena tool instead of a normal website.
---

# Work With Garena Tools

Use this as the first routing layer for Garena internal tools. Keep this file lean; load only the reference file for the tool family needed by the user's request.

## Routing Workflow

1. Identify the internal system from the user's words, pasted URL, or requested action.
2. Read `references/routing.md` to map aliases, URLs, and feature words to a tool family.
3. Read exactly the relevant `references/<tool>.md` file, plus `cross-tool-workflows.md` only when the task spans systems.
4. Resolve the live callable tool names from the active MCP/tool surface before acting. Tool counts and names can drift.
5. Prefer MCP tools over browser automation when the requested data or mutation is available through MCP.
6. For any write, mutation, signing, order, deploy, delete, archive, or bulk action: re-read the live target, preview impact when non-trivial, execute only when the user's intent is explicit, then verify by reading back.

## Tool References

- `creative-lab` -> [creative-lab.md](./references/creative-lab.md)
- `datcom` -> [datcom.md](./references/datcom.md)
- `deploy-app` / Demo System -> [deploy-app.md](./references/deploy-app.md)
- `garena-booking` -> [garena-booking.md](./references/garena-booking.md)
- `garena-vendor` -> [garena-vendor.md](./references/garena-vendor.md)
- `gigi` -> [gigi.md](./references/gigi.md)
- `google-drive-mcp` -> [google-drive-mcp.md](./references/google-drive-mcp.md)
- `infra-knowledge` -> [infra-knowledge.md](./references/infra-knowledge.md)
- `outline` / `wiki.odp.garena.vn` -> [outline.md](./references/outline.md)
- `plane` / `managetask.odp.garena.vn` -> [plane.md](./references/plane.md)

Use [migration-map.md](./references/migration-map.md) when maintaining older tool-specific skills after this router exists.
