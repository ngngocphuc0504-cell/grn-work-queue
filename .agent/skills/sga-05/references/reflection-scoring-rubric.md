# Reflection Scoring Rubric — Domain Reference

> Reference document for skill `sga-05`.
> Defines exact scoring criteria for the 3-sentence reflection quality assessment.

---

## Sentence 1: WHAT (Learning Statement)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | Empty or trivial | "Tôi học được nhiều" |
| 1 | Generic insight | "Tôi học được rằng cần chuẩn bị kỹ hơn" |
| 2 | Specific insight with context | "Tôi học được rằng khi phân tích tài chính, cần cross-validate ERP vs POS data trước khi kết luận" |
| 3 | Transferable principle derived | "Bất kỳ phân tích nào dựa trên single data source đều unreliable — cần triangulation methodology" |

### Anti-Patterns
- **Truism:** "Communication quan trọng" — everyone knows this
- **Self-flattery:** "Tôi đã làm tốt" — no learning content
- **Deflection:** "Nếu có thêm thời gian thì tốt hơn" — avoids self-reflection

---

## Sentence 2: EVIDENCE (Proof Statement)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No evidence | — |
| 1 | Feeling-based | "Tôi cảm thấy điều đó đúng" |
| 2 | Specific event | "Vì comment từ CFO về slide 5 chỉ ra tôi thiếu quarterly comparison" |
| 3 | Event + causal chain | "CFO feedback on slide 5 + khi tôi check lại, ERP data thiếu Q3 baseline, gây lệch 8% so actual reconciliation" |

### Anti-Patterns
- **Circular:** Evidence restates the WHAT sentence
- **External blame:** "Vì data team gửi trễ" — not self-reflective

---

## Sentence 3: ACTION (Intent Statement)

| Score | Criteria | Example |
|-------|----------|---------|
| 0 | No intent | — |
| 1 | Vague intent | "Tôi sẽ cố gắng hơn" |
| 2 | Specific action | "Lần tới tôi sẽ add a validation step: cross-check ERP vs POS trước khi tạo summary slide" |
| 3 | Action + trigger condition | "Mỗi khi tôi làm financial report (trigger), bước đầu tiên sẽ là ERP-POS reconciliation check (action) trước khi viết bất kỳ conclusion nào (gate)" |

### Anti-Patterns
- **Too ambitious:** "Tôi sẽ thay đổi hoàn toàn cách làm việc"
- **No behavioral change:** "Tôi sẽ nhớ điều này" — not an action

---

## Aggregate Scoring

Total = Sum of 3 sentences (0-9 scale, mapped to 0-3 for simplicity)

| Sum | Mapped Score | Action |
|-----|-------------|--------|
| 7-9 | 3 (Excellent) | Proceed to KI gate check |
| 5-6 | 2 (Adequate) | Proceed to KI gate check |
| 3-4 | 1 (Generic) | Return: target weakest sentence |
| 0-2 | 0 (Empty) | Return: full rewrite needed |
