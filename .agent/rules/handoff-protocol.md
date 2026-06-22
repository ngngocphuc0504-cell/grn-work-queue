# Handoff Protocol — Agent-to-Agent

## Handoff Standard

Mọi handoff giữa agents phải truyền:
```yaml
handoff_package:
  from_agent: string
  to_agent: string
  session_id: string
  task_id: string
  artifact_path: string       # file path of primary output
  checkpoint_passed: boolean  # MUST be true
  skill_signals: list         # extracted from this step
  next_action: string         # what receiving agent should do
  escalation_flag: boolean    # true if human needed
```

## Routing Table (CTO authority)

| Trigger | From | To | Condition |
|---------|------|----|-----------|
| task_submitted | User | TASK-FRAMER | user_approach_stated = true |
| brief_complete | TASK-FRAMER | User | checkpoint: user confirm brief |
| brief_approved | User | REVIEW-COACH or EXECUTOR | mode gate check |
| draft_submitted | User | REVIEW-COACH | draft artifact exists |
| feedback_delivered | REVIEW-COACH | User | user reads + acknowledges |
| task_complete | User | QUALITY-GATE | user declares done |
| quality_passed | QUALITY-GATE | REFLECTION-HARVESTER | validation = PASS |
| quality_failed | QUALITY-GATE | User | validation = FAIL + reason |
| reflection_done | REFLECTION-HARVESTER | MEMORY-CONSOLIDATOR | background queue |
| ki_distilled | MEMORY-CONSOLIDATOR | SC-SKILL | KI written to store |
| signals_updated | SC-SKILL | CTO | SMI recalculated |

## Escalation Triggers (→ Human)

| Condition | Escalation Type |
|-----------|----------------|
| bypass_count ≥ 3 | MODE_LOCK + human notification |
| reflection quality 0/3 twice consecutive | Coaching prompt from CTO |
| SMI drops (regression) | TC-TWIN review + alert |
| User requests FRT update | Explicit confirmation required |
| Task spans > 5 sessions incomplete | CTO review prompt |
