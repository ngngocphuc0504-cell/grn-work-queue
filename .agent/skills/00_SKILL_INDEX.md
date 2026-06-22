# Skill Index — ws-career-twin-v1

> **Last updated:** 2026-04-07
> **Standard:** Canonical 4-Tier Skill Spec

## System-Grade Agent Skills (SGA)

| ID | Name | Wired Workflows | Status |
|----|------|-----------------|--------|
| `sga-01` | Task Framing Methodology | WF-01, WF-09 | ✅ Production |
| `sga-02` | Review Rubric Protocol | WF-03, WF-04 | ✅ Production |
| `sga-03` | Executor Delegation Rules | WF-02 | ✅ Production |
| `sga-04` | Quality Gate Validation | WF-05 | ✅ Production |
| `sga-05` | Reflection Prompt Library | WF-06 | ✅ Production |
| `sga-06` | KI Distillation Gates | WF-06, WF-07 | ✅ Production |
| `sga-07` | SMI Calculation Engine | WF-08 | ✅ Production |
| `sga-18` | Coby Strategic Advisor | WF-18 | ✅ Production |

## Skill-Human Signal Skills (SKH)

| ID | Name | Dimension | Status |
|----|------|-----------|--------|
| `skh-01` | Work Framing Signal | SKH-01 (1-5) | ✅ Production |
| `skh-02` | Evidence Reasoning Signal | SKH-02 (1-5) | ✅ Production |
| `skh-03` | Execution Control Signal | SKH-03 (1-5) | ✅ Production |
| `skh-04` | Communication Signal | SKH-04 (1-5) | ✅ Production |
| `skh-05` | AI Co-work Signal | SKH-05 (1-5) | ✅ Production |
| `skh-06` | Content Writing | Execution | ✅ Production |
| `skh-07` | Slide Engineering | Execution | ✅ Production |

## INFRASTRUCTURE SKILLS (INF)

| ID | Name | Dimension | Status |
|----|------|-----------|--------|
| `session-manager` | Workflow State & DIKW Bus | Meta-Harness | ✅ Production |

## 4-Tier Compliance Matrix

| Skill | SKILL.md | references/ | assets/ | evals/ | scripts/ |
|-------|----------|-------------|---------|--------|----------|
| sga-01 | ✅ | ✅ (5-element-framing-criteria) | ✅ (framed-brief-schema) | ✅ (2 cases) | ⬜ |
| sga-02 | ✅ | ✅ (analytical-rubric-dimensions) | ✅ (review-feedback-schema) | ✅ (2 cases) | ⬜ |
| sga-03 | ✅ | ✅ (boundedness-criteria) | ⬜ | ✅ (2 cases) | ⬜ |
| sga-04 | ✅ | ✅ (dod-parsing-rules) | ⬜ | ✅ (2 cases) | ⬜ |
| sga-05 | ✅ | ✅ (reflection-scoring-rubric) | ✅ (reflection-schema) | ✅ (2 cases) | ⬜ |
| sga-06 | ✅ | ✅ (ki-distillation-gates) | ⬜ | ✅ (2 cases) | ⬜ |
| sga-07 | ✅ | ✅ (smi-calculation-method) | ⬜ | ✅ (2 cases) | ⬜ |
| sga-18-coby-advisor | ✅ | ✅ (coby-mindset-blueprint) | ✅ (coby-advisory-memo) | ✅ (evals.json) | ✅ (execute_mass_evals) |
| skh-01 | ✅ | ⬜ | ✅ (framed-brief-schema) | ✅ (inherited) | ⬜ |
| skh-02 | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| skh-03 | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| skh-04 | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| skh-05 | ✅ | ⬜ | ⬜ | ⬜ | ⬜ |
| skh-06 | ✅ | ✅ (writing-rubric) | ⬜ | ✅ (2 cases) | ⬜ |
| skh-07 | ✅ | ✅ (c-level-slide-rubric) | ⬜ | ✅ (2 cases) | ⬜ |
| session-manager | ✅ | ✅ (dikw, schema) | ⬜ | ✅ (unit) | ✅ (snapshot.py) |
