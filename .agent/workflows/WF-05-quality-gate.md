---
description: Quality gate — kiểm tra output cuối cùng so với Definition of Done trước khi đóng task.
---

# Workflow: WF-05 Quality Gate

- **👤 Owner:** `[@QUALITY-GATE]`
- **🛠 Skill Target:** `[sga-04]`, `[skh-03]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-04`**: Quality Gate Validation Protocol — so sánh output vs DoD
> - **`skh-03`**: Execution Control Signal — đo lường khả năng user tự quản lý chất lượng

## Goal & Governance Context

- **Purpose:** Kiểm tra output cuối cùng của user so với Definition of Done (DoD) đã define trong brief. Đây là Hard-Gate — PASS/FAIL, không có "gần đạt".
- **Scope:** Chỉ validate artifact hiện tại vs DoD của project brief. KHÔNG thực hiện review bổ sung (đó là WF-03/WF-04).
- **Mode Required:** Any

## Execution Steps

### Step 1: Load DoD from Brief (QUALITY-GATE)

1. Load `outputs/{id}/project-brief.md` — extract DoD section
2. Parse DoD into checklist of measurable criteria
3. Load submitted artifact

### Step 2: Systematic DoD Validation (QUALITY-GATE)

1. For each DoD criterion:
   - Check: criterion met? (PASS/FAIL per criterion)
   - Evidence: cite specific artifact section that satisfies/violates
2. Calculate overall pass rate

### Step 3: Hard-Gate Decision

1. 100% DoD criteria met → **PASS**
   - Signal: Task completion confirmed
   - Handoff → WF-06 (Reflection Capture)
2. Any DoD criterion failed → **FAIL**
   - List specific failed criteria with evidence
   - Route back to WF-02 (re-execution) or WF-03/WF-04 (re-review)
   - NO soft suggestions — binary PASS/FAIL only

### Step 4: Signal Extraction

1. Extract SKH-03 (execution_control): score based on DoD pass rate
2. Signal → SC-SKILL via CTO

## Audit & Metrics (Quality Gates)

- **Gate 1 (DoD Existence):** Brief MUST contain measurable DoD. If missing → HALT + route to WF-01 for reframing.
- **Gate 2 (Binary Decision):** Output is strictly PASS or FAIL. "Partial pass" is ILLEGAL.
- **Metrics:** DoD pass rate (%), iteration count before pass, time-to-quality

## Troubleshooting

| Vấn đề | Xử lý |
|---------|--------|
| DoD criteria too vague to validate | HALT → route to TASK-FRAMER for DoD refinement |
| User disputes FAIL decision | Accept dispute. User provides evidence. Re-evaluate specific criterion. |
| 3+ FAIL iterations on same criterion | Escalate to CTO: "Possible skill gap detected. Recommend focused training." |
