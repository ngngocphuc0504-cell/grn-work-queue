# GIGI

Use when the user mentions GIGI, asks to "check gigi", or refers to a GIGI-backed internal assistant/search workflow.

## Current State

The 2026-06-15 MCP admin screenshot showed `gigi` enabled with 8 tools. In the inspected session, the exact `gigi_*` callable names were not exposed by discovery.

## Discovery Workflow

1. Search the active tool surface for `gigi`.
2. If no `gigi_*` callables appear, search broader terms from the user's request.
3. If still absent, report: "`gigi` is enabled in the MCP admin snapshot, but its callable tools are not exposed in this session."
4. Do not invent likely tool names.

## Working Rules

- If callables are discovered, prefer the least invasive read/search operation first.
- Treat GIGI outputs as assistant/search results that may need source verification.
- For action-like GIGI tools, preview what will be sent or changed before calling them.

## Safety

- Do not claim GIGI cannot do something solely because this reference lacks the callable list.
- Do not fall back to browser automation unless the user accepts that MCP discovery is unavailable or insufficient.
