---
description: Review phân tích — đánh giá chất lượng tư duy phân tích và evidence reasoning của user.
---

# Workflow: WF-03 Analytical Review

- **👤 Owner:** `[@REVIEW-COACH]`
- **🛠 Skill Target:** `[sga-02]`, `[skh-02]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-02`**: Review Rubric Protocol — rubric-based feedback methodology cho analytical artifacts
> - **`skh-02`**: Evidence Reasoning Signal — đo lường khả năng suy luận dựa trên bằng chứng

## Goal & Governance Context

- **Purpose:** Đánh giá chất lượng tư duy phân tích trong artifact user submit. REVIEW-COACH là mentor/challenger — KHÔNG phải examiner. Feedback phải evidence-based, trích dẫn artifact cụ thể.
- **Scope:** Chỉ review artifact đã submit qua WF-02 checkpoint. KHÔNG tự tạo output thay user. KHÔNG đánh giá vấn đề ngoài analytical dimension.
- **Mode Required:** Any

## Execution Steps

### Step 1: Request Self-Assessment (REVIEW-COACH)

1. Prompt user: "Bạn tự chấm artifact này bao nhiêu điểm (1-5) và tại sao?"
2. WAIT for user response — do NOT proceed without self-assessment
3. Record self-assessment score + rationale

### Step 2: Load Review Context (REVIEW-COACH)

1. Load role-pack rubric from TC-TWIN (CST layer)
2. Load the submitted artifact via path from WF-02 checkpoint
3. Cross-reference artifact against role-pack expectations

### Step 3: Rubric-Based Scoring (REVIEW-COACH)

1. Score artifact across relevant skill dimensions:
   - SKH-01 (work_framing): IF framing issues detected in artifact
   - SKH-02 (evidence_reasoning): PRIMARY — quality of analysis, evidence citation, logic chain
2. Each score MUST cite specific artifact evidence:
   - ✅ Correct: "Đoạn 3 thiếu data source cho claim 'revenue tăng 20%'"
   - ❌ Wrong: "Cần improve evidence" (quá chung chung)

### Step 4: Deliver Structured Feedback (REVIEW-COACH)

1. Present feedback in priority order (most impactful first)
2. Each feedback item gắn với skill dimension cụ thể
3. Include constructive direction: "nên làm gì" — không chỉ "sai"
4. Prioritize exactly 1 next action for user

### Step 5: Checkpoint — User Acknowledges

1. User acknowledges feedback (verbal or artifact update)
2. Route decision:
   - User iterates → loop back to WF-02
   - User declares done → handoff to QUALITY-GATE (WF-05)

### Step 6: Signal Extraction

1. Extract SKH-02 (evidence_reasoning) primary signal
2. Extract SKH-01 secondary signal if framing issues found
3. Signal → SC-SKILL via CTO

## Audit & Metrics (Quality Gates)

- **Gate 1 (Self-Assessment Required):** User MUST provide self-assessment before receiving feedback. Skip = FAIL.
- **Gate 2 (Evidence-Based Feedback):** Every feedback point MUST cite specific artifact evidence. Generic feedback = REWORK feedback.
- **Metrics:** Review quality score (rubric completeness), user self-assessment accuracy delta (self-score vs coach-score)

## Troubleshooting

| Vấn đề | Xử lý |
|---------|--------|
| User refuses self-assessment | Explain: "Self-assessment là bước quan trọng để phát triển metacognition." |
| Artifact too short to review | Return to WF-02 with guidance on minimum artifact requirements |
| User disagrees with score | Accept disagreement. Log as learning signal. Adjust if user provides valid evidence. |
