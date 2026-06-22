# Twin Architecture — 3-Layer Model

## Separation of Concerns

Ba lớp twin KHÔNG BAO GIỜ được merge. Chúng hoạt động như "engine so sánh":

```
CPT ← stable foundation (who any knowledge worker should be)
CST ← real snapshot (who this user is TODAY)
FRT ← capability target (who this user is becoming)

Comparison engine:
  GAP = FRT - CST
  Today's learning priority = highest GAP items intersected with today's task type
```

## CPT — Core Professional Twin

**Nature:** Immutable knowledge base of 5 universal skills  
**Files:** `02_twin_memory/twin-core/SOUL-CPT.md`, `02_twin_memory/twin-core/skills/human/skh-0*.md`  
**Update rule:** Only via ws-governance harness patch (never in runtime)  
**Consultation:** Referenced by TASK-FRAMER, REVIEW-COACH for rubric standards  

## CST — Current Self Twin

**Nature:** Living snapshot, updated after every completed task  
**Files:** `02_twin_memory/twin-current/{user_id}/SKILL-MATRIX.md`, `KI-STORE/`, `PATTERN-LOG.md`  
**Update rule:**  
- Hot path: user preferences (immediate)  
- Background: KIs and skill signals (post-session, via MEMORY-CONSOLIDATOR)  
**Consultation:** TC-TWIN reads CST to personalize challenges and detect recurring errors  

## FRT — Future Role Twin

**Nature:** Semi-immutable capability model, reviewed quarterly  
**Files:** `02_twin_memory/twin-future/{user_id}/ROLE-PACK.md`, `GAP-MAP.md`, `LEARNING-QUEUE.md`  
**Update rule:** TC-TWIN proposes updates; user must explicitly confirm  
**Consultation:** Used by TC-TWIN to set learning priority, NOT as a judge of current performance  

## Co-Work Mode Ramp

| Mode | When Available | Twin Behavior | Executor-Swarm |
|------|---------------|---------------|----------------|
| OBSERVE | Week 1 default | Twin demonstrates, user watches | LOCKED |
| COWORK | Week 2+ / SMI avg ≥ 2.0 | Human drafts, twin reviews | LOCKED |
| DELEGATED | SMI avg ≥ 3.0 | Twin can execute bounded sub-tasks | UNLOCKED (bounded) |
| SWARM | SMI avg ≥ 4.0 | Full swarm on complex projects | UNLOCKED (full) |

**Mode gate enforcement:** CTO checks SMI before routing any execution request.
