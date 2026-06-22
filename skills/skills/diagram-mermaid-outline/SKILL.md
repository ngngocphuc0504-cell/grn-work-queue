---
name: diagram-mermaid-outline
description: Design and improve Mermaid diagrams inside Garena Outline pages. Use when Codex needs to turn spreadsheet-like scope, ownership, workflow, RACI, handoff, or operating-process information into readable Mermaid flowcharts, sequence diagrams, swimlane-like maps, or diagram-first Outline documentation; also use when a user asks to improve, rewrite, validate, or compare Mermaid diagrams for Outline readability.
---

# Diagram Mermaid Outline

## Purpose

Create Mermaid diagrams for Outline pages that help non-technical readers understand ownership, workflow, handoffs, and operating scope faster than raw tables.

Pair this skill with `work-with-outline` whenever the target is `wiki.odp.garena.vn` or an Outline page.

## Workflow

1. Resolve and re-read the exact Outline page before editing.
2. Identify the reader question the diagram must answer:
   - `Who owns what?` -> use an owner map or RACI-style flowchart.
   - `What happens first, next, and last?` -> use a sequence diagram.
   - `Where are the handoffs?` -> use sequence diagram with short participant names.
   - `Which workstream contains which scope?` -> use grouped flowchart with subgraphs.
3. Keep the diagram focused on one scenario or one viewpoint. Split into multiple diagrams when one diagram needs to answer both ownership and process flow.
4. Put the diagram before the raw table, then keep the raw table as the audit/reference section.
5. Patch only the relevant diagram section in Outline when possible.
6. Re-read the page after writing and verify the Mermaid code block is saved.

## Writing Rules

- Use short labels, usually 3-7 words. Move explanation into prose below the diagram.
- Use role aliases such as `Lead`, `OM`, `Data`, `Reg` in Mermaid source, with readable participant names in labels.
- Use `autonumber` for sequence diagrams that describe an operating timeline.
- Use `box` to separate local team and regional support in sequence diagrams.
- Use `rect` to show phases such as Planning, Execution, Reporting, Support.
- Use `loop` for recurring work such as daily or weekly optimization.
- Use `par` when work happens in parallel, such as creative supply and campaign readiness.
- Use `opt` for support that happens only when needed, especially Regional support.
- Avoid long self-loops. If an actor performs several internal tasks, use a `loop`, a shorter self-message, or a note.
- Avoid stuffing every spreadsheet row into the diagram. Diagram the operating model, then keep the table as source detail.
- Prefer Vietnamese prose around the diagram when the Outline page is user-facing for Garena local teams; keep Mermaid labels concise and readable.

## Diagram Selection

Use this quick mapping:

| Source content | Best diagram | Why |
| --- | --- | --- |
| Owner by task / team | Flowchart owner map | Fast answer to who owns what |
| Time-ordered workflow | Sequence diagram | Shows handoffs and order |
| Repeated operating cadence | Sequence with `loop` | Shows recurring work without clutter |
| Conditional support / escalation | Sequence with `opt` or `alt` | Shows optional paths clearly |
| Parallel coordination | Sequence with `par` | Shows tasks that run at the same time |
| Workstreams and scope buckets | Flowchart with subgraphs | Keeps categories readable |

## Mermaid Guardrails

- Use fenced code blocks with `mermaid`.
- In flowcharts, avoid lowercase `end` inside node text because it can break Mermaid parsing.
- Quote node labels that contain punctuation, slashes, parentheses, Vietnamese text, or line breaks.
- Use `<br/>` for line breaks in flowchart node labels.
- Keep Mermaid syntax conservative because Outline may lag behind the newest Mermaid features.
- If a rendered diagram looks too wide in Outline, shorten participant names first, then split the diagram.

## References

For reusable templates and examples, read `references/diagram-patterns.md`.
