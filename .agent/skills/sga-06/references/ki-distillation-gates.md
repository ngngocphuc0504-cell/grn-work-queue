# KI Distillation Gates — Domain Reference

> Reference document for skill `sga-06`.
> Defines the 4-gate qualification system for filtering Knowledge Items from reflections.

---

## Core Principle

Not every insight is worth preserving. CST quality degrades when flooded with trivial, duplicate, or unfalsifiable "knowledge." The 4-gate system ensures only HIGH-VALUE learning enters long-term twin memory.

---

## Gate A: NOVELTY — "Is this NEW?"

### Definition
The insight must NOT already exist in CST (Current Skill Twin) in any form.

### Evaluation Method
1. Load `02_twin_memory/twin-current/{user_id}/SKILL-MATRIX.md`
2. Search for semantic overlap with existing entries
3. Classify:

| Result | Definition | Action |
|--------|-----------|--------|
| ✅ NOVEL | No existing CST entry covers this insight | PASS |
| ⚠️ REINFORCEMENT | Similar entry exists but new evidence adds depth | PASS (merge into existing) |
| ❌ DUPLICATE | Functionally identical entry already exists | FAIL — save as reinforcement signal only |

### Anti-Patterns
- **AP-01:** "Chuẩn bị kỹ quan trọng" — likely already in CST after 3+ sessions
- **AP-02:** Rephrased version of existing KI — semantic match, different words

---

## Gate B: GENERALIZABILITY — "Does it apply beyond THIS task?"

### Definition
The insight must be applicable to at least 1 other task type or context. Task-specific details must be abstracted into transferable principles.

### Evaluation Method
1. Try to rephrase the insight WITHOUT mentioning the specific task
2. If the rephrased version is still meaningful → PASS

| Test | Example | Result |
|------|---------|--------|
| Original | "Khi làm báo cáo Q1, cần cross-validate ERP vs POS" | Task-specific |
| Generalized | "Khi phân tích từ multiple data sources, cần cross-validation trước khi kết luận" | ✅ Generalizable |
| Failed | "Hôm nay em hơi mệt nên làm chậm" | ❌ Not generalizable — situation-specific |

### Anti-Patterns
- **AP-03:** Insight is about a specific tool/system, not a transferable skill
- **AP-04:** Insight is about feelings, not methodology

---

## Gate C: ACTIONABILITY — "Can it change future behavior?"

### Definition
The insight must contain an explicit or implicit action that the user can take in future tasks. It must describe a BEHAVIORAL CHANGE, not just an observation.

### Evaluation Method
1. Check for action verbs: "sẽ", "nên", "phải", "cần", "bắt đầu", "dừng"
2. Verify action is specific (not "cố gắng hơn")

| Test | Example | Result |
|------|---------|--------|
| Has action + specificity | "Trước khi kết luận, tôi sẽ luôn list 3 counter-arguments" | ✅ PASS |
| Has action, no specificity | "Tôi sẽ cẩn thận hơn" | ❌ FAIL — not actionable enough |
| Observation only | "Data quality ảnh hưởng lớn đến kết quả" | ❌ FAIL — no behavior change |

---

## Gate D: EVIDENCE — "Is there proof, not just feeling?"

### Definition
The insight must be grounded in specific, observable events from the task — not intuitions, emotions, or guesses.

### Evaluation Method
1. Check for specific artifact references, feedback citations, or measurable outcomes
2. "Tôi cảm thấy" is evidence of emotion, not evidence of learning

| Test | Example | Result |
|------|---------|--------|
| Specific event cited | "CFO feedback chỉ ra slide 5 thiếu baseline comparison" | ✅ PASS |
| Measurable outcome | "Iteration count giảm từ 4 xuống 2 khi tôi áp dụng checklist" | ✅ PASS |
| Feeling-based | "Tôi cảm thấy mình đã học được nhiều" | ❌ FAIL |
| Unverifiable | "Tôi nghĩ approach mới tốt hơn" | ❌ FAIL — no evidence |

---

## Aggregate Decision

| Gates Passed | Decision | Action |
|-------------|----------|--------|
| 4/4 | 🏆 HIGH-VALUE KI | Queue for WF-07. Priority: HIGH |
| 3/4 | ✅ QUALIFIED KI | Queue for WF-07. Priority: NORMAL |
| 2/4 | ⚠️ MARGINAL | Save as session reflection. Note which gates failed. |
| 0-1/4 | ❌ REJECTED | Save as session note only. Not KI material. |
