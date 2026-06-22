---
description: Review giao tiếp — đánh giá chất lượng truyền đạt, cấu trúc, và clarity của output.
---

# Workflow: WF-04 Communication Review

- **👤 Owner:** `[@REVIEW-COACH]`
- **🛠 Skill Target:** `[sga-02]`, `[skh-04]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-02`**: Review Rubric Protocol — rubric-based feedback cho communication artifacts
> - **`skh-04`**: Communication Signal — đo lường khả năng truyền đạt rõ ràng, có cấu trúc

## Goal & Governance Context

- **Purpose:** Đánh giá artifact theo chiều giao tiếp: structure, clarity, audience fit, persuasiveness. Phân biệt rõ với WF-03 (analytical) — workflow này CHỈ focus communication dimension.
- **Scope:** Artifact types: reports, proposals, presentations, emails. KHÔNG review code hoặc technical artifacts.
- **Mode Required:** Any

## Execution Steps

### Step 1: Request Self-Assessment (REVIEW-COACH)

1. Prompt: "Bạn tự đánh giá communication quality (1-5) và giải thích?"
2. WAIT for user response

### Step 2: Load Communication Rubric (REVIEW-COACH)

1. Load role-pack rubric từ TC-TWIN (CST layer) — communication dimension
2. Load artifact via path from checkpoint
3. Evaluate against 4 communication criteria:
   - Structure (Pyramid Principle compliance)
   - Clarity (no ambiguity, no jargon without definition)
   - Audience Fit (tone matches stakeholder expectations)
   - Persuasiveness (call-to-action clear, evidence supports claims)

### Step 3: Deliver Evidence-Based Feedback (REVIEW-COACH)

1. Each feedback item cites specific passage in artifact
2. Prioritize 1 most impactful improvement
3. Provide rewrite example for worst passage

### Step 4: Checkpoint & Route

1. User acknowledges → iterate (WF-02) or proceed (WF-05)
2. Extract SKH-04 (communication) signal → SC-SKILL

## Audit & Metrics (Quality Gates)

- **Gate 1 (Self-Assessment Required):** User provides self-score before feedback. Skip = FAIL.
- **Gate 2 (Specific Evidence):** Every feedback point cites specific passage. Generic = REWORK.
- **Metrics:** Communication score (1-5 per criterion), self-assessment accuracy delta

## Troubleshooting

| Vấn đề | Xử lý |
|---------|--------|
| Artifact is pure data (no narrative) | Flag: "Artifact này thiếu communication layer. Cần thêm executive summary?" |
| User disagrees on audience fit | Request: "Audience cụ thể là ai? Chia sẻ thêm context." |
