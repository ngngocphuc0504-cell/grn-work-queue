---
description: Vòng lặp thực thi co-work — user dẫn dắt, twin hỗ trợ theo mode.
---

# Workflow: WF-02 Co-Work Execution Loop

- **👤 Owner:** `[@QUALITY-GATE]` (Executor-Swarm coordination)
- **🛠 Skill Target:** `[sga-03]`, `[skh-03]`, `[skh-05]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-03`**: Executor Delegation Rules — kiểm soát điều kiện delegate task cho AI
> - **`skh-03`**: Execution Control Signal — đo lường khả năng tự quản lý execution của user
> - **`skh-05`**: AI Co-work Signal — đo lường mức độ tương tác hiệu quả với AI

## Goal & Governance Context

- **Purpose:** Vận hành vòng lặp thực thi task dựa trên brief đã approved. User luôn là người drafts chính. Twin chỉ hỗ trợ theo mode được cấp phép.
- **Scope:** Chỉ xử lý execution trong project sandbox (`outputs/{id}/`). KHÔNG được tự ý nâng mode. KHÔNG delegate nếu mode là OBSERVE/COWORK.
- **Mode Required:** COWORK (human drafts, twin consults), DELEGATED/SWARM (executor available for bounded sub-tasks)

## Execution Steps

### Step 1: Load Execution Context (QUALITY-GATE)

1. Load approved brief từ `outputs/{id}/project-brief.md`
2. Verify `co_work_mode` từ memory contract
3. Determine execution path based on mode

### Step 2: COWORK Mode — User Drafts (User + QUALITY-GATE)

1. User drafts independently based on approved brief
2. Twin available for Q&A only — NOT proactive intervention
3. Track drafting progress in session log

### Step 3: DELEGATED/SWARM Mode — Bounded Delegation (QUALITY-GATE)

1. User writes explicit delegation brief containing: WHAT / WHY / CONSTRAINTS / DoD
2. QUALITY-GATE validates delegation brief against bounded task constraints:
   - Task has specific input AND specific output
   - Zero ambiguity in DoD
   - Task does NOT require human judgment or decision
3. IF valid → Executor completes bounded task
4. IF invalid → REJECT with specific missing element

### Step 4: User Integration & Critical Review (User)

1. User reviews executor output critically — NEVER blind-accept
2. User integrates executor output into their own work
3. User applies own judgment to modify/improve

### Step 5: Checkpoint 2 — Draft Submission

1. User submits draft with message: "Draft sẵn sàng để review"
2. Log artifact path for next workflow
3. Extract skill signals: SKH-03 (execution_control), SKH-05 (ai_cowork)

## Audit & Metrics (Quality Gates)

- **Gate 1 (Mode Compliance):** Delegation attempt in OBSERVE/COWORK → REFUSE + explain mode gate. Metrics: mode_violation_count.
- **Gate 2 (Delegation Brief Quality):** All 4 elements (WHAT/WHY/CONSTRAINTS/DoD) present. Missing any = REJECT.
- **Gate 3 (Draft Submission):** User confirms "Draft sẵn sàng để review" → Handoff to REVIEW-COACH via CTO.

## Troubleshooting

| Vấn đề | Xử lý |
|---------|--------|
| User requests delegation in OBSERVE mode | REFUSE. Explain: "Mode OBSERVE chỉ cho phép twin hướng dẫn." |
| Delegation brief too vague | REJECT + return with specific missing elements |
| User accepts executor output without review | Log warning. Prompt: "Bạn đã review chưa?" |
