# I/O Contract — Zero-Floating FIO Governance

## Zero-Floating FIO Law

Every task artifact MUST be written to a named, traceable location.
No output floats in conversation history without a file anchor.

## Genesis Header (MANDATORY on ALL artifacts)

```yaml
---
artifact_id: [auto: task_id + artifact_type + timestamp]
task_id: [from active project folder]
project_id: [from active project folder]
created_by: [agent_id]
session_id: [current session_id]
co_work_mode: [OBSERVE|COWORK|DELEGATED|SWARM]
skill_signals_tagged: [comma-separated skh IDs]
twin_layer_consulted: [CPT|CST|FRT|COMPOSITE]
user_checkpoint_passed: [true|false]
user_approach_stated: [true|false]
reflection_linked: [reflection_id or PENDING]
---
```

## Artifact Storage Convention

```
outputs/{project_id}/
├── project-brief.md          ← framed brief (WF-01 output)
├── task-board.md             ← milestone tracking
├── artifacts/
│   ├── {task_id}-draft.md
│   ├── {task_id}-revised.md
│   └── {task_id}-final.md
├── feedback/
│   └── {task_id}-review.md   ← REVIEW-COACH output
├── decisions/
│   └── {task_id}-decision.md
└── reflections/
    └── {session_id}-reflection.md
```

## Agent I/O Contracts

### TASK-FRAMER
- Input: raw task description + user_approach string
- Output: `outputs/{id}/project-brief.md` (framed-brief-schema)
- Handoff: → CTO → REVIEW-COACH or EXECUTOR

### REVIEW-COACH
- Input: draft artifact path + skill rubric reference
- Output: `outputs/{id}/feedback/{task_id}-review.md`
- Handoff: → user for iteration → QUALITY-GATE

### QUALITY-GATE
- Input: final artifact path + DoD definition
- Output: validation_result (PASS|FAIL) + skill signals
- Handoff: PASS → REFLECTION-HARVESTER; FAIL → user

### REFLECTION-HARVESTER
- Input: session artifacts + user's 3-sentence reflection
- Output: `outputs/{id}/reflections/{session_id}-reflection.md` + KI queue
- Handoff: → MEMORY-CONSOLIDATOR (background)

### MEMORY-CONSOLIDATOR
- Input: KI queue + reflection log
- Output: `02_twin_memory/twin-current/{user_id}/KI-STORE/{ki_id}.md`
- Handoff: → SC-SKILL for skill signal update

### SKILL-TRACKER
- Input: aggregated skill signals (session)
- Output: Updated `02_twin_memory/twin-current/{user_id}/SKILL-MATRIX.md`
- Handoff: → CTO (mode unlock check)
