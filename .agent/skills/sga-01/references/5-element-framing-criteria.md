# 5-Element Framing Criteria — Domain Reference

> Reference document for skill `sga-01`.
> Defines exact criteria, scoring thresholds, and anti-patterns for each framing element.

---

## Element 1: Objective (OUTCOME, not Activity)

### Criteria
The objective MUST be framed as a desired OUTCOME state, not as an activity or process.

### Scoring (0-3)
| Score | Definition | Example |
|-------|-----------|---------|
| 0 | No objective stated | — |
| 1 | Activity-based | "Viết báo cáo tài chính" ❌ |
| 2 | Outcome-based but vague | "Có báo cáo tài chính cho Q1" ⚠️ |
| 3 | Clear outcome with impact | "Board hiểu được tình hình tài chính Q1 để quyết định phân bổ ngân sách Q2" ✅ |

### Anti-Patterns
- **AP-01:** Objective starts with a verb describing an action, not a state: "Viết...", "Tạo...", "Làm..."
- **AP-02:** Objective describes deliverable format instead of business value: "1 file PPTX 20 slides"
- **AP-03:** Objective is unmeasurable: "Tốt hơn", "Hiệu quả hơn" without baseline or target

---

## Element 2: Stakeholders & Their Definition of Done

### Criteria
MUST identify at least 1 primary stakeholder AND articulate THEIR acceptance criteria (not just the author's).

### Scoring (0-3)
| Score | Definition | Example |
|-------|-----------|---------|
| 0 | No stakeholders identified | — |
| 1 | Generic stakeholder | "Cho sếp" ❌ |
| 2 | Named stakeholder, no DoD | "Cho CFO review" ⚠️ |
| 3 | Named stakeholder + their specific DoD | "CFO duyệt: số liệu khớp ERP, có executive summary ≤1 trang" ✅ |

### Anti-Patterns
- **AP-04:** Stakeholder is "team" or "mọi người" — too vague
- **AP-05:** DoD is author-centric: "Tôi hài lòng" instead of stakeholder-centric

---

## Element 3: Assumptions (≥3 Required)

### Criteria
MUST surface at least 3 explicit assumptions. Each assumption must be falsifiable (can be proven wrong).

### Scoring (0-3)
| Score | Definition | Example |
|-------|-----------|---------|
| 0 | No assumptions stated | — |
| 1 | 1-2 assumptions, generic | "Data sẽ có sẵn" ❌ |
| 2 | ≥3 assumptions, specific | "ERP data Q1 đã close, AR team đã xác nhận bad debt" ⚠️ |
| 3 | ≥3 assumptions with risk rating | "ERP data Q1 đã close (HIGH risk: AR confirms bad debt mỗi Q trễ 1 tuần)" ✅ |

### Anti-Patterns
- **AP-06:** Assumptions are truisms: "Data phải chính xác" — not falsifiable
- **AP-07:** No risk assessment on any assumption

---

## Element 4: Scope Boundary (IN/OUT)

### Criteria
MUST clearly delineate what is IN scope and what is OUT of scope. Both lists must be non-empty.

### Scoring (0-3)
| Score | Definition |
|-------|-----------|
| 0 | No scope stated |
| 1 | Only IN scope, no OUT |
| 2 | Both IN and OUT stated, but vague |
| 3 | Specific items listed in both, with rationale for key exclusions |

### Anti-Patterns
- **AP-08:** "Everything related to finance" — unbounded scope
- **AP-09:** OUT scope is "nothing" — unrealistic, leads to scope creep

---

## Element 5: Measurable Definition of Done

### Criteria
DoD MUST contain at least 1 specific, testable metric or verifiable Boolean condition. "Done when I feel it's done" is ILLEGAL.

### Scoring (0-3)
| Score | Definition | Example |
|-------|-----------|---------|
| 0 | No DoD | — |
| 1 | Subjective DoD | "Khi nào thấy ổn" ❌ |
| 2 | Checklist but not measurable | "Có đủ 5 sections" ⚠️ |
| 3 | Measurable + stakeholder-verifiable | "CFO ký duyệt + số liệu khớp ERP ±1% + submit trước 15/4" ✅ |

### Anti-Patterns
- **AP-10:** DoD is identical to objective (circular reference)
- **AP-11:** DoD has no deadline or quantifiable threshold

---

## Aggregate Scoring

Total Framing Score = Sum of 5 elements (0-15 scale)

| Range | Grade | Action |
|-------|-------|--------|
| 12-15 | ✅ Ready | Proceed to execution |
| 8-11 | ⚠️ Needs Work | Return specific elements for improvement |
| 0-7 | ❌ Reject | Full reframing required |
