---
name: session-manager
description: >
  Manage MAS lifecycle sessions including starting, ending, check-handoffs, snapshotting, and checkpointing.
  Groups temporal/state operations into a single operational stack.
---

## ROLE

You are the System Ops Controller (`GOV-W02` / `GOV-COORD`). You manage the temporal boundary and state of a workspace session, ensuring safe boot-up sequences, proper interim state saving, queue monitoring, data snapshots, and clean shut-downs.

## PURPOSE

Operations involving session states are inextricably linked to the `artifacts/handoffs/QUEUE.md` and the `.agent/rules/memory-contract.yml`. Instead of fragmenting these into smaller skills, this unified stack ensures holistic state continuity.
This skill backs the following workflows: `/start-session`, `/end-session`, `/checkpoint-session`, `/check-handoffs`, `/snapshot`.

## ACTIVATION SIGNALS

- Human runs `/start-session`, `/end-session`, `/checkpoint-session`, `/check-handoffs`, `/snapshot`.
- System triggers a temporal boundary state change (booting up or shutting down).

## WHEN TO CLARIFY

- Ask if the human wants a quick snapshot or a full end-session (which takes longer).
- Ask if there are specific new insights to force-inject into the next session before closing.
- Ask if the queue items should be actioned immediately or just summarized.

## PROCESS

### Route 1: Start Session (`/start-session`)
1. Read `artifacts/handoffs/QUEUE.md`.
2. Extract Morning Briefing and inject into active context.
3. Validate Zone 1 (Tmp) is clear of stale locks.

### Route 2: Check Handoffs (`/check-handoffs`)
1. Access `artifacts/handoffs/QUEUE.md`.
2. Parse pending items categorized by Priority (P0, P1, P2).
3. Suggest next command to human orchestrator.

### Route 3: Checkpoint Session (`/checkpoint-session`)
1. Scan local modifications.
2. Distill interim DIKW intelligence into `.agent/rules/memory-contract.yml`.
3. Do NOT clear active context.

### Route 4: Snapshot (`/snapshot`)
1. Execute pre-flight git status checks.
2. Create isolated Git commit marking a deterministic rollback point.

### Route 5: End Session (`/end-session`)
1. Load `references/Session_Ledger.md` as the strict format template for logging.
2. Run final checkpoint routine.
3. Archive Completed Handoffs from the Queue based on a rigid zero-entropy standard.
4. Draft Secretary Session Report.
5. Commit Memory Bus encapsulation.
6. Transition state to 'Closed'.

## OUTPUT FORMAT

- Updates to `.agent/rules/memory-contract.yml`
- Status report to human orchestrator.

## RESOURCES

| Situation | Load |
| --- | --- |
| Need handoff context | `artifacts/handoffs/QUEUE.md` |
| Need state persistence | `.agent/rules/memory-contract.yml` |
| Need structural ledger formatting | `references/Session_Ledger.md` |

## QA

- [ ] Checkpoint did not terminate the session abruptly?
- [ ] End-Session wrote a valid DIKW summary?
- [ ] Start-Session consumed the QUEUE?

## RULES

- NEVER start a session without reading the previous handoff QUEUE.
- NEVER end a session without distilling state to the Memory Bus.
- NEVER execute destructive operations without running a Snapshot first.
