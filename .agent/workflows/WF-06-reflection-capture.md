---
description: Reflection capture — thu hoạch phản hồi có cấu trúc và chưng cất Knowledge Items.
---

# Workflow: WF-06 Reflection Capture

- **👤 Owner:** `[@REFLECTION-HARVESTER]`
- **🛠 Skill Target:** `[sga-05]`, `[sga-06]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-05`**: Reflection Prompt Library — bộ prompt phản hồi 3 câu có cấu trúc
> - **`sga-06`**: KI Distillation Gates — 4 cổng lọc để chưng cất learning thành Knowledge Items

## Goal & Governance Context

- **Purpose:** Thu hoạch phản hồi có cấu trúc từ user sau mỗi task hoàn thành. Chưng cất learning có giá trị thành Knowledge Items cho long-term memory. Session KHÔNG ĐƯỢC đóng nếu reflection chưa hoàn thành.
- **Scope:** Chỉ thu thập reflection + distill KI. KHÔNG thực hiện coaching hoặc scoring bổ sung.
- **Mode Required:** Any (MANDATORY — không được skip ở bất kỳ mode nào)

## Execution Steps

### Step 1: Prompt 3-Sentence Reflection (REFLECTION-HARVESTER)

1. Deliver reflection prompt (structured 3-sentence format):
   - Câu 1: "Điều quan trọng nhất tôi học được từ task này là..." (WHAT)
   - Câu 2: "Tôi biết điều này vì..." (EVIDENCE)
   - Câu 3: "Lần tới tôi sẽ..." (ACTION INTENT)
2. WAIT for user response — do NOT provide examples or hints proactively

### Step 2: Score Reflection Quality (REFLECTION-HARVESTER)

1. Score reflection quality (0-3 scale):
   - 0: Empty/meaningless
   - 1: Generic (no specific evidence)
   - 2: Adequate (specific evidence + actionable intent)
   - 3: Excellent (deep insight + transferable principle)
2. IF score < 2: Return for revision with specific guidance on weakest sentence
3. IF score ≥ 2: Proceed

### Step 3: Skill Signal Extraction

1. Parse sentence 1-3 for implied skill development signals
2. Map to relevant SKH dimensions (SKH-01 through SKH-05)
3. Signal → SC-SKILL via CTO

### Step 4: KI Distillation Gate Check (REFLECTION-HARVESTER)

1. Run 4 KI qualification gates:
   - Gate A: Is this insight NOVEL (not already in CST)?
   - Gate B: Is this insight GENERALIZABLE (applies beyond this task)?
   - Gate C: Is this insight ACTIONABLE (can change future behavior)?
   - Gate D: Is there EVIDENCE (not just a feeling)?
2. IF ≥3 gates pass → Queue as KI candidate for MEMORY-CONSOLIDATOR (WF-07)
3. IF <3 gates pass → Save as session-level reflection only (not KI)

### Step 5: Save & Unblock Session Close

1. Save reflection to `outputs/{id}/reflections/{date}.md`
2. Set `reflection_pending = false`
3. Handoff → CTO (session may now close via WF-INF-02)

## Audit & Metrics (Quality Gates)

- **Gate 1 (Reflection Mandatory):** WF-INF-02 CANNOT execute while `reflection_pending = true`. This is a HARD BLOCK, not a suggestion.
- **Gate 2 (Quality Minimum):** Reflection score ≥ 2 required. Score < 2 = loop back to Step 1.
- **Metrics:** Reflection quality score (0-3), KI conversion rate (reflections → KIs), skip attempts logged

## Troubleshooting

| Vấn đề | Xử lý |
|---------|--------|
| User tries to close session without reflection | BLOCK. Route back to Step 1. Log bypass_count. |
| User writes vague "tôi học được nhiều" | Score 1. Return: "Cụ thể hơn — điều gì và bạn biết vì sao?" |
| KI candidate duplicates existing CST entry | Reject KI. Save as reinforcement signal instead. |
