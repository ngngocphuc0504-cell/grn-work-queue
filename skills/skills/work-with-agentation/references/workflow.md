# Agentation Workflow

## Standard Loop

Use this sequence whenever the user wants changes from Agentation feedback:

1. Check connectivity.
2. Find the relevant session.
3. Read pending annotations.
4. Inspect one annotation in detail before editing.
5. Change code.
6. Verify.
7. Reply in thread.
8. Resolve.

## Connectivity

Prefer the live Agentation tool family when the session exposes it.

Fallback checks:

```bash
python -X utf8 scripts/agentation_http.py health
python -X utf8 scripts/agentation_http.py sessions
```

If `health` fails, the likely causes are:

- the local Agentation bridge/server process is not running
- the toolbar is pointing at a different port
- the user is on another machine or browser profile than expected

## Session Heuristics

When many sessions exist:

- match by route first, such as `ugc-config`
- prefer the newest session
- treat `localhost` and `127.0.0.1` as the same app unless the user says otherwise
- ignore empty sessions if a newer non-empty matching session exists

Useful commands:

```bash
python -X utf8 scripts/agentation_http.py find-session --url-substring "ugc-config"
python -X utf8 scripts/agentation_http.py session --id <session-id>
```

## Pending Triage

Use these commands:

```bash
python -X utf8 scripts/agentation_http.py pending
python -X utf8 scripts/agentation_http.py pending --session <session-id>
python -X utf8 scripts/agentation_http.py annotation --id <annotation-id>
```

Inspect these fields before editing:

- `comment`
- `nearbyText`
- `elementPath`
- `url`
- `thread`

If the user says `fix all pending annotations`, read each pending item first and batch by page or module when it helps reduce repeated code verification.

## Thread Etiquette

Keep thread updates factual:

- `Looking at this now.`
- `Resolved: changed the section title from "Approver Rule" to "Approval process".`
- `Blocked: I found two similar labels and need the exact target.`

Useful commands:

```bash
python -X utf8 scripts/agentation_http.py reply --id <annotation-id> --message "Looking at this now."
python -X utf8 scripts/agentation_http.py resolve --id <annotation-id> --message "Resolved: updated the button label to Save."
python -X utf8 scripts/agentation_http.py dismiss --id <annotation-id> --reason "duplicate"
```

## Watch Mode

Prefer the live watch operation when it is exposed:

- call `agentation_watch_annotations`
- process the returned batch
- acknowledge or reply
- implement
- resolve
- call watch again

Fallback polling:

```bash
python -X utf8 scripts/agentation_http.py watch --url-substring "ugc-config" --timeout 300
```

## Prompt Recipes

These are good user prompts that should trigger this skill:

- `show pending annotations`
- `list my annotation sessions`
- `fix annotation 3`
- `fix all pending annotations`
- `watch mode for agentation`
- `reply to annotation 5 that I am checking it`
