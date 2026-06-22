# AGENTS.md — Career Twin Workspace v1 MAS Constitution

> **Version:** 1.1
> **Read this file FIRST before any other file in the workspace.**
> **All agents must comply with the rules, matrices and contracts defined here.**

---

## Sứ mệnh

Career Twin Workspace xây dựng **Digital Twin chuyên nghiệp** của người dùng — phản chiếu năng lực hiện tại, theo dõi tiến trình phát triển, và vận hành dự án theo mô hình Co-work Human-AI. Hệ thống phục vụ 1 người dùng chính, giúp họ phát triển 5 kỹ năng cốt lõi thông qua việc cùng làm việc thực tế với AI.

**Phép tương tự:** Career Twin = Một người mentor cá nhân + PA thực thi + Nhật ký phản hồi tự động — tất cả trong một hệ thống liền mạch.

---

## MAS Hierarchy Diagram

```text
┌─────────────────────────────────────────────┐
│ TIER 1: 🧑 HUMAN — Primary User             │
│ Strategic direction, task ownership          │
├─────────────────────────────────────────────┤
│ TIER 1 AGENT: CAREER-TWIN-ORCHESTRATOR (CTO)│
│ Route, mode-gate, session lifecycle          │
├──────────────┬──────────────────────────────┤
│ TIER 2       │ TIER 2                        │
│ TC-TWIN      │ SC-SKILL                      │
│ Twin Coord   │ Skill Coord                   │
├──────────────┼──────────────────────────────┤
│ TIER 3 WORKERS                               │
│ TASK-FRAMER │ REVIEW-COACH │ REFL-HARVESTER │
│         QUALITY-GATE (Exec Coord)            │
├──────────────────────────────────────────────┤
│ TIER 4 SPECIALISTS                           │
│ CONTENT-WRITER │ SLIDE-MAKER │ T4-LECTURER   │
│ T4-AI-CONSULTANT │ T4-CURRICULUM-DESIGNER    │
│ T4-COBY-ADVISOR (Coby's Second Eye)          │
└──────────────────────────────────────────────┘
```

---

## Agent Roster Table

| ID | Agent | Tier | Role | Reports To | Definition File |
|----|-------|------|------|-----------|----------------|
| — | Primary User | 1 | Human Orchestrator | — | — |
| CTO | Career Twin Orchestrator | 1 | Coordinator & Router | Human | `.agent/agents/tier_1_orchestrator/CTO/INDEX.md` |
| TC-TWIN | Twin Coordinator | 2 | Twin Layer Manager | CTO | `.agent/agents/tier_2_coordinator/TC-TWIN/INDEX.md` |
| SC-SKILL | Skill Coordinator | 2 | Skill Signal Aggregator | CTO | `.agent/agents/tier_2_coordinator/SC-SKILL/INDEX.md` |
| TASK-FRAMER | Task Framer | 3 | Brief & Framing | CTO | `.agent/agents/tier_3_worker/TASK-FRAMER/INDEX.md` |
| REVIEW-COACH | Review Coach | 3 | Analytical & Communication Review | CTO | `.agent/agents/tier_3_worker/REVIEW-COACH/INDEX.md` |
| REFLECTION-HARVESTER | Reflection Harvester | 3 | Post-task Reflection | CTO | `.agent/agents/tier_3_worker/REFLECTION-HARVESTER/INDEX.md` |
| QUALITY-GATE | Quality Gate & Executor | 3 | DoD Validation & Execution Control | CTO | `.agent/agents/tier_3_worker/QUALITY-GATE/INDEX.md` |
| CONTENT-WRITER | Specialist Content Writer | 4 | Content Production | QUALITY-GATE | `.agent/agents/tier_4_specialist_agent/CONTENT-WRITER/INDEX.md` |
| SLIDE-MAKER | Specialist Slide Engineer | 4 | Slide Engineering | QUALITY-GATE | `.agent/agents/tier_4_specialist_agent/SLIDE-MAKER/INDEX.md` |
| T4-LECTURER | Academic Lecturer Persona | 4 | Academic Evaluation | QUALITY-GATE | `.agent/agents/tier_4_specialist_agent/T4-LECTURER/INDEX.md` |
| T4-AI-CONSULTANT | AI Consultant Persona | 4 | ROI & Optimization | QUALITY-GATE | `.agent/agents/tier_4_specialist_agent/T4-AI-CONSULTANT/INDEX.md` |
| T4-CURRICULUM-DESIGNER | Curriculum Architect | 4 | Education Framework | QUALITY-GATE | `.agent/agents/tier_4_specialist_agent/T4-CURRICULUM-DESIGNER/INDEX.md` |
| T4-COBY-ADVISOR | Coby's Second Eye | 4 | Strategic Review (Opt-in via `/coby-view`) | QUALITY-GATE | `.agent/agents/tier_4_specialist_agent/T4-COBY-ADVISOR/INDEX.md` |

---

## Interaction Matrix

> ❌ = CẤM giao tiếp trực tiếp. Mọi cross-agent communication PHẢI qua CTO. 
> *(Tier 4 Specialists chỉ xuất hiện khi CTO/QUALITY-GATE gọi, không nhận lệnh trực tiếp từ Human. Ngoại lệ: T4-COBY-ADVISOR có thể được gọi thủ công bởi Human thông qua lệnh `/coby-view`)*

| From ↓ / To → | Human | CTO | TC-TWIN | SC-SKILL | TASK-FRAMER | REVIEW-COACH | REFL-HARV | QUALITY-GATE |
|----------------|-------|-----|---------|----------|-------------|--------------|-----------|--------------|
| **Human** | — | ✅ Request | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **CTO** | ✅ Deliver | — | ✅ Delegate | ✅ Delegate | ✅ Delegate | ✅ Delegate | ✅ Delegate | ✅ Delegate |
| **TC-TWIN** | ❌ | ✅ Report | — | ❌ | ✅ Consults | ✅ Consults | ❌ | ❌ |
| **SC-SKILL** | ❌ | ✅ Report | ❌ | — | ❌ | ❌ | ✅ Receives | ✅ Receives |
| **TASK-FRAMER** | ❌ | ✅ Handoff | ✅ Queries | ❌ | — | ❌ | ❌ | ❌ |
| **REVIEW-COACH** | ❌ | ✅ Handoff | ✅ Queries | ✅ Signals | ❌ | — | ❌ | ❌ |
| **REFL-HARV** | ❌ | ✅ Unblocks | ❌ | ✅ Signals | ❌ | ❌ | — | ❌ |
| **QUALITY-GATE** | ❌ | ✅ Handoff | ❌ | ✅ Signals | ❌ | ✅ Routes fail | ✅ Triggers | — |

---

## Decision Authority Matrix

| Loại quyết định | Tier 3 | Tier 2 | Tier 1 (CTO) | Human |
|-----------------|--------|--------|---------------|-------|
| Task framing approach | Propose | — | Validate | Approve |
| Mode upgrade | — | — | Recommend | Approve |
| Twin data update (CST) | — | Execute | Monitor | Notify |
| Twin data update (FRT) | — | Propose | Monitor | Approve |
| Skip reflection | — | — | Block | Override only |

---

## Escalation Matrix

| Tình huống | Xử lý bởi | Escalate lên | Thời hạn | Format |
|-----------|----------|-------------|---------|--------|
| Task framing ambiguity | TASK-FRAMER | CTO → Human | Immediate | Clarification prompt |
| Mode gate violation | QUALITY-GATE | CTO → Human | Immediate | Refusal + explanation |
| Reflection bypass 3x | REFL-HARVESTER | CTO → Human | End of session | Circuit breaker alert |
| KB data conflict | TC-TWIN | CTO → Human | Next session | Conflict report |

---

## Naming Convention

| Loại artifact | Format | Ví dụ |
|--------------|--------|-------|
| Project brief | `{project_id}/project-brief.md` | `proj-001/project-brief.md` |
| Session log | `{project_id}/session-log/{session_id}.md` | `proj-001/session-log/S003.md` |
| Reflection | `{project_id}/reflections/{date}.md` | `proj-001/reflections/2026-04-07.md` |
| Skill signal | `02_twin_memory/twin-current/{user_id}/SKILL-MATRIX.md` | Updated in-place |

---

*agents.md v1.1 — Last updated: 2026-04-07*
