---
name: outline-memory-ops
description: Use for Outline memory commands `get-context`, `save-context`, and `organize-context`, keeping personal and project memory routed safely without leakage.
---

# Outline Memory Ops

## Overview

This skill turns Outline into a scoped memory system with explicit routing and write safety. It loads global personal context, resolves one project scope at a time, and enforces quarantine behavior when scope or write target is unclear.

Use the live Outline tool family exposed in the current session, typically through `mcp__garena_vn_mcp_gw`. Do not assume a separate standalone `outline` MCP server exists.

Read [references/page-map.md](references/page-map.md) for exact document IDs and URLs. Read [references/command-templates.md](references/command-templates.md) for output and write-plan formats.

## When To Use

- User says `get-context`, `save-context`, or `organize-context`.
- User wants to store or retrieve durable working context from Outline.
- User wants semi-auto context updates with strict separation between personal memory and project memory.
- User wants to promote session notes into canonical memory safely.

Do not use this skill for general project documentation edits that are not part of the memory workflow. Use the normal Outline workflow instead.

## Required Read Order

Always keep context small and read only the documents required by the resolved scope.

1. Read `HUB - Hai-Son Context`.
2. Read `Personal Memory - Canonical`.
3. Read `Memory Router Map`.
4. If a project scope is resolved, read only that project's bootstrap context.
5. Read project next-docs only if the command or task actually needs them.

## Collection Write Lock

This skill has a hard write lock.

- Write operations are allowed only inside the personal Outline collection `Hai Son`.
- External project collections may be read for context when needed, but they are read-only for this skill.
- If a resolved write target is outside `Hai Son`, reject that target and route the item to `Personal Memory - Inbox Journal` instead.
- Do not bypass this rule even if a project bootstrap page looks like the natural target.

## Scope Resolution

Resolve scope in this order:

1. Explicit project argument from the user.
2. Workspace or repo mapping from `Memory Router Map`.
3. Current thread hint if it is specific and recent.
4. Fallback to `global-default`.

If the scope is ambiguous:

- Do not guess the project.
- Do not write into any project page.
- Route unknown items to `Personal Memory - Inbox Journal`.

## Command Workflow

### `get-context`

1. Resolve scope first.
2. Read and assemble the context packet in this order:
   - `global`
   - `project`
   - `canonical-next`
3. Return only one project scope unless the user explicitly asks to compare multiple scopes.
4. Label each block with its source.
5. If no project is resolved, return only global personal context.

### `save-context`

1. Resolve scope first.
2. Classify session output into:
   - `personal durable`
   - `project durable`
   - `working/session`
   - `unknown`
3. Create a write plan before any mutation:
   - target page
   - target section
   - memory type
   - confidence
4. Apply routing rules:
   - No `project anchor` => do not write project.
   - No `allowed write target` => do not write canonical.
   - Mixed personal/project items must be split into separate blocks.
   - Any write target outside collection `Hai Son` is forbidden.
5. If scope or target is unclear, or the target is outside `Hai Son`, write to `Personal Memory - Inbox Journal` with full metadata.

### `organize-context`

1. Start from `Personal Memory - Inbox Journal`.
2. Dedupe repeated items.
3. Promote only durable items into the correct owner page.
4. Preserve traceability back to source session/date.
5. Keep session noise, uncertain notes, or un-routed items in inbox/quarantine instead of forcing promotion.

## Mandatory Metadata

Every memory item written by this workflow must carry:

- `scope`
- `durability`
- `source`
- `confidence`
- `target_page`
- `promoted_by`

## Safety Rules

- Never mix personal facts and project facts in the same write block.
- Never write project memory without a resolved project anchor.
- Never write canonical project docs without an allowed target in `Memory Router Map`.
- Never read multiple project bootstrap scopes in one `get-context` unless the user explicitly asks for a comparison.
- When global context conflicts with project-specific canonical docs, the project docs win.
- Never write to any Outline collection other than `Hai Son`.
- External project docs are read-only within this skill.
- Safety is more important than convenience. If unsure, quarantine to inbox.

## Output Discipline

- Keep replies concise.
- For `get-context`, return the packet, not a long essay.
- For `save-context`, show the write plan first, then perform the update.
- For `organize-context`, report what was promoted, what stayed quarantined, and why.
