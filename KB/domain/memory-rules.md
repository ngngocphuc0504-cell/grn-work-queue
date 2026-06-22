# Memory Rules — Career Twin Workspace

## What Gets Written (per scope)

### User-Scoped (hot path — immediate)
✅ User preferences (communication style, preferred output format)
✅ Role Pack selection
✅ FRT updates (after user confirmation)

### User-Scoped (background consolidation — post-session)
✅ KI candidates from reflection (quality-gated)
✅ Pattern flags (recurring errors/strengths)
✅ Skill signals (after 5+ similar tasks)
✅ Skill Maturity Index updates

### System-Scoped (CPT only — architect updates)
✅ 5 human skill playbooks
✅ Co-work methodology
❌ NEVER updated during runtime

## What Stays Read-Only
❌ KB/governance/ — never writeable by agents
❌ 02_twin_memory/twin-core/ — never writeable in runtime
❌ rules/ — never writeable in runtime
❌ Any shared analytics namespace

## KI Distillation Gates (4 gates, all must pass)
1. **Completion gate:** Task status = SUCCESS or PARTIAL_ACCEPTED
2. **Quality gate:** Reflection quality score ≥ 2/3
3. **Novelty gate:** KI not >80% similar to existing KIs in store
4. **Timing gate:** Distillation runs POST-session, never mid-task

## Temporal Validity
All KIs in CST include:
```
created_at: ISO-8601
expires_at: ISO-8601 | NEVER
staleness_risk: HIGH | MEDIUM | LOW
last_validated: ISO-8601
```
KIs marked HIGH staleness_risk flagged for quarterly review.
