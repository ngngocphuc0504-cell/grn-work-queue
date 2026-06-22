# PROJECT.md — Career Twin Workspace
**Workspace ID:** ws-career-twin-v1
**Version:** 1.0
**Platform:** Google Antigravity
**Genesis Date:** 2026-04-07

## Mission
Biến mỗi task công việc thành một sự kiện học tập có cấu trúc, thông qua co-work bắt buộc với Digital Twin cá nhân hóa.

## Users
- **Primary:** Học viên / early-mid career knowledge worker
- **Secondary:** Team lead, knowledge worker trong doanh nghiệp (Phase 2)

## Scope
**IN:** Task framing, co-work execution, artifact review, reflection, skill signal tracking, twin update
**OUT:** Performance evaluation for HR, voice/avatar interface, external API (v1), multi-user shared twin

## Key Constraints
- Human phải đưa approach trước khi twin respond (Human First rule)
- Không deploy FRT data sang company analytics mà không có user consent
- Session chỉ đóng sau khi reflection được submit
- Executor-Swarm chỉ unlock ở DELEGATED mode trở lên

## Architecture Summary
3-Twin Model (CPT/CST/FRT) + 7-Agent MAS Swarm + Folder Project System + Skill Signal Engine

## Agent Hierarchy
```
CTO (Tier 1)
├── TC-TWIN (Tier 2)
├── SC-SKILL (Tier 2)
├── TASK-FRAMER (Tier 3)
├── REVIEW-COACH (Tier 3)
├── REFLECTION-HARVESTER (Tier 3)
└── QUALITY-GATE (Tier 3)
```
