---
name: work-with-agentation
description: Work with Agentation visual feedback from a local app. Use when Codex needs to inspect, triage, reply to, resolve, or continuously watch annotations created from the Agentation toolbar, especially on localhost React apps. Prefer Agentation tools exposed in the live session, whether directly or through a gateway, and otherwise use the bundled HTTP fallback script against the local Agentation server on port 4747. Trigger on requests such as "show pending annotations", "fix annotation 3", "fix all pending annotations", "list my annotation sessions", or "watch mode" for Agentation feedback.
---

# Work With Agentation

Use this skill to turn Agentation annotations into a tight edit loop: inspect feedback, map it to the right UI, change code, verify the result, and close the annotation cleanly.

## Tool Decision

Choose the access path in this order:

1. If active tools or `tool_search` expose an Agentation tool family in the current session, whether directly or through a gateway, use it first.
2. Treat names such as `agentation_list_sessions`, `agentation_get_all_pending`, `agentation_reply`, `agentation_resolve`, or `agentation_watch_annotations` as logical operations. Resolve the exact callable tool ids from the active tool surface first.
3. If the Agentation tool family is not available in the current session, use `scripts/agentation_http.py` against `http://localhost:4747`.
4. If neither path works, stop and tell the user the local Agentation server or toolbar is not reachable.

Do not ask the user to copy and paste annotations when the live Agentation tools or the local HTTP server are already available.

## Quick Start

Run this loop:

1. Confirm the local server is reachable.
2. List sessions and find the newest session for the relevant page URL.
3. Read pending annotations only, unless the user explicitly asks to inspect history.
4. For each annotation, inspect:
   - `comment`
   - `nearbyText`
   - `elementPath`
   - `url`
   - existing `thread`
5. Make the code change in the correct project.
6. Run the smallest verification that still proves the change is safe.
7. Reply in the annotation thread with a short factual summary.
8. Resolve the annotation only after the change and verification are complete.

## Session Selection

Choose the session carefully:

- Prefer the newest active session whose URL matches the page the user is discussing.
- Treat `localhost` and `127.0.0.1` as equivalent if the route matches.
- If multiple sessions match the same page, inspect the newest one first.
- If the user says `fix all pending annotations`, operate on current `pending` only. Do not reopen historical resolved items unless the user asks.

## Annotation Processing Rules

Apply these rules every time:

- Read the full annotation record before editing. `comment` alone is often ambiguous.
- Use `nearbyText`, `elementPath`, and thread history to avoid changing the wrong element.
- If the annotation asks for a risky or broad change, reply in thread with the assumption you are making before implementing it.
- If the user corrects the intended change in chat, trust the newer user instruction over the older annotation thread.
- Keep thread replies short and concrete, for example `Resolved: changed the field label from "Approve Type" to "Approve by".`
- If the code change is blocked, reply with the blocker instead of silently leaving the annotation pending.

## Watch Mode

If the live tool surface exposes an annotation-watch operation, use that for a blocking watch loop.

If the Agentation tool family is unavailable, use the HTTP fallback script `watch` command as a poll-based substitute. Polling is less efficient than live watch mode, so use it only when needed.

## HTTP Fallback Commands

Use the bundled script when no Agentation tool family is available:

```bash
python -X utf8 scripts/agentation_http.py health
python -X utf8 scripts/agentation_http.py sessions
python -X utf8 scripts/agentation_http.py find-session --url-substring "ugc-config"
python -X utf8 scripts/agentation_http.py pending
python -X utf8 scripts/agentation_http.py session --id <session-id>
python -X utf8 scripts/agentation_http.py annotation --id <annotation-id>
python -X utf8 scripts/agentation_http.py reply --id <annotation-id> --message "Looking at this now."
python -X utf8 scripts/agentation_http.py resolve --id <annotation-id> --message "Resolved: updated the label text."
python -X utf8 scripts/agentation_http.py watch --url-substring "ugc-config" --timeout 300
```

Read [references/workflow.md](./references/workflow.md) when you need the detailed fallback workflow, session heuristics, or prompt recipes.

## Verification

After changing code:

- Run the narrowest relevant verification first, such as `npm run build`, a feature-specific audit, or a targeted test.
- If verification is flaky due to a known local environment issue, state that precisely in the thread and in the final user report.
- Do not mark the annotation resolved until you have either verified the change or clearly stated why verification could not be completed.

## Final Reporting

When reporting back to the user:

- State how many pending annotations were handled.
- Name the affected page or module.
- Mention the verification result.
- Call out any remaining flaky checks or open risks.
