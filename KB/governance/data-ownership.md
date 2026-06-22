# Data Ownership Policy — Career Twin Workspace v1

## Nguyên tắc nền tảng

> Mọi dữ liệu twin cá nhân thuộc về user, không thuộc về workspace operator.

## Data Layer Architecture

```
LAYER A — USER-OWNED (user controls, user deletes)
  02_twin_memory/twin-current/{user_id}/SKILL-MATRIX.md
  02_twin_memory/twin-current/{user_id}/KI-STORE/
  02_twin_memory/twin-current/{user_id}/PATTERN-LOG.md
  02_twin_memory/twin-future/{user_id}/ROLE-PACK.md
  02_twin_memory/twin-future/{user_id}/GAP-MAP.md
  projects/{user_id}/*/artifacts/
  training/reflection-log/{user_id}/

LAYER B — WORKSPACE ANALYTICS (aggregate, anonymized, operator access)
  analytics/skill-cohort-aggregate.json    ← no user_id
  analytics/adoption-metrics.json          ← session counts only
  analytics/workflow-effectiveness.json    ← pass rates, not content

LAYER C — SYSTEM (read-only, no user data)
  KB/
  rules/
  agents/
  02_twin_memory/twin-core/
```

## Hard Walls

- NEVER join Layer A data with Layer B output
- NEVER expose Layer A to company HR systems in v1
- Layer B data MUST be aggregated (N≥5 users) before any export
- User deletion of Layer A: MUST execute within 24 hours

## Write Permissions

| Data | Who can write | When |
|------|--------------|------|
| SKILL-MATRIX.md | SC-SKILL (automated) | After each task |
| KI-STORE/ | MEMORY-CONSOLIDATOR (background) | Post-session |
| PATTERN-LOG.md | REFLECTION-HARVESTER | After reflection |
| ROLE-PACK.md | TC-TWIN (with user confirmation) | Quarterly only |
| GAP-MAP.md | TC-TWIN (automated) | After CST update |
| CPT files | FORBIDDEN — architect only | Never in runtime |
