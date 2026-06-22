# DoD Parsing Rules — Domain Reference

> Reference document for skill `sga-04`.
> Defines how to decompose a Definition of Done into individual Boolean criteria.

---

## Core Principle

A DoD is NOT a paragraph — it is a checklist of independently verifiable Boolean conditions. Each condition either MET (✅) or NOT MET (❌). No partial credit. No "almost."

---

## Parsing Algorithm

### Step 1: Sentence Decomposition
Split DoD text into individual sentences or clauses separated by:
- Period (.)
- Semicolon (;)
- Bullet point (-)
- "AND" conjunction
- Comma-separated list items

### Step 2: Boolean Conversion
Transform each decomposed element into a testable Boolean question:

| Original | Boolean Form |
|----------|-------------|
| "Số liệu khớp ERP" | "Does artifact contain numerical data matching ERP source? YES/NO" |
| "Có executive summary" | "Does artifact contain a section titled 'Executive Summary'? YES/NO" |
| "Trước ngày 15/4" | "Is submission date ≤ April 15? YES/NO" |
| "CFO approved" | "Has CFO provided written approval? YES/NO" |

### Step 3: Ambiguity Detection
Flag any criterion that cannot be converted to Boolean:

| Ambiguous DoD | Problem | Resolution |
|---------------|---------|------------|
| "Chất lượng tốt" | Cannot verify "tốt" | Ask: "Tốt = gì? Threshold?" |
| "Đủ chi tiết" | Cannot verify "đủ" | Ask: "Bao nhiêu sections/data points?" |
| "Phù hợp với audience" | Subjective | Ask: "Audience cụ thể? Criteria nào?" |

---

## Evidence Matching Rules

For each Boolean criterion, the assessor MUST:
1. **Locate** the specific artifact section that addresses the criterion
2. **Quote** the exact passage (≤ 50 words) as evidence
3. **Judge** MET or NOT MET based on the evidence

### Evidence Levels
| Level | Definition | Acceptable? |
|-------|-----------|-------------|
| Direct | Artifact explicitly contains required element | ✅ YES |
| Inferred | Element exists but requires interpretation | ⚠️ FLAG for human judgment |
| Missing | No trace of required element | ❌ NOT MET |

---

## Anti-Patterns

- **AP-01 (Batch Pass):** Passing all criteria as a batch without individual checking — each criterion MUST be individually evaluated
- **AP-02 (Generous Interpretation):** "Close enough" — this is NOT an acceptable assessment
- **AP-03 (Phantom Criteria):** Adding criteria not in the original DoD — assessor MUST only validate stated criteria
- **AP-04 (Orphan DoD):** DoD criteria that reference elements not in scope — flag as DoD defect, route to reframing
