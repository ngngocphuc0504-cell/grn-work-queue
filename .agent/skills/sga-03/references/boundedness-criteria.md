# Boundedness Criteria — Domain Reference

> Reference document for skill `sga-03`.
> Defines the 3-filter test for determining whether a task is eligible for AI delegation.

---

## Core Principle

A task is **bounded** when the relationship between input and output is deterministic and does NOT require human judgment, creativity, or ethical decision-making. Bounded tasks are mechanical transformations.

---

## Filter 1: Input Specificity

### Definition
The task input must be explicitly defined — a specific file, dataset, text passage, or structured data. "Cái này" or "data đó" is NOT specific.

### Pass Criteria
| Status | Condition | Example |
|--------|-----------|---------|
| ✅ PASS | Named file/path provided | "Tổng hợp data từ `Q1-revenue.xlsx` sheet 'Summary'" |
| ✅ PASS | Exact text quoted | "Dịch đoạn sau sang tiếng Anh: '[exact text]'" |
| ❌ FAIL | Vague reference | "Lấy data tài chính" — từ đâu? |
| ❌ FAIL | Requires discovery | "Tìm số liệu phù hợp" — AI phải tự judge |

### Anti-Patterns
- **AP-01 (Implicit Input):** User assumes AI knows which file/data they mean
- **AP-02 (Discovery Task):** Task requires AI to search, evaluate, and select input — this is judgment, not delegation

---

## Filter 2: Output Determinism

### Definition
Given the same input, the expected output should be reproducible. Two different AI runs should produce substantially similar results.

### Pass Criteria
| Status | Condition | Example |
|--------|-----------|---------|
| ✅ PASS | Format specified + content constrained | "Tạo bảng pivot: rows=Product, cols=Quarter, values=Revenue" |
| ✅ PASS | Template filling | "Điền data vào template [template path]" |
| ❌ FAIL | Open-ended creation | "Viết 1 báo cáo hay" — "hay" is subjective |
| ❌ FAIL | Strategy/opinion needed | "Đề xuất phương án tốt nhất" — requires judgment |

### Anti-Patterns
- **AP-03 (Creative Task):** Writing that requires original ideas, not transformation
- **AP-04 (Evaluation Task):** "Đánh giá xem cái nào tốt hơn" — requires human values

---

## Filter 3: No Human Judgment Required

### Definition
The task must NOT require ethical decisions, value judgments, stakeholder-sensitive choices, or strategic direction.

### Pass Criteria
| Judgment Type | Delegable? | Reasoning |
|--------------|-----------|-----------|
| Formatting transformation | ✅ YES | Mechanical, deterministic |
| Data aggregation/pivot | ✅ YES | Mathematical, reproducible |
| Translation (with style guide) | ✅ YES | Constrained by guide |
| Content evaluation | ❌ NO | Requires quality standards = judgment |
| Prioritization | ❌ NO | Requires values/strategy |
| Stakeholder communication | ❌ NO | Requires relationship context |
| Ethical decision | ❌ NO | Requires moral reasoning |

### Anti-Patterns
- **AP-05 (Hidden Judgment):** "Tóm tắt cuộc họp" — seems mechanical but requires judging what's important
- **AP-06 (Automation Disguise):** User frames a judgment task as "just formatting" to bypass gate

---

## Aggregate Decision

| Filters Passed | Decision |
|---------------|----------|
| 3/3 | ✅ DELEGATE — Task is fully bounded |
| 2/3 | ⚠️ CONDITIONAL — Identify failing filter, ask user to constrain |
| 0-1/3 | ❌ REJECT — Task requires human execution |
