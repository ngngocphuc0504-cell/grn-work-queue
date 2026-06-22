---
description: Memory consolidation — chuyển KI candidates vào long-term twin memory.
---

# Workflow: WF-07 Memory Consolidation

- **👤 Owner:** `[@MEMORY-CONSOLIDATOR-NOTE]` (background, via CTO)
- **🛠 Skill Target:** `[sga-06]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-06`**: KI Distillation Gates — validate và consolidate KI candidates vào CST

## Goal & Governance Context

- **Purpose:** Background process chuyển KI candidates (từ WF-06) vào CST (Current Skill Twin) snapshot. Update SKILL-MATRIX.md với learning mới.
- **Scope:** Chỉ ghi vào `02_twin_memory/twin-current/`. KHÔNG modify CPT (read-only). FRT update cần user confirmation.

## Execution Steps

### Step 1: Load KI Queue

1. Read `ki_distillation_queue` từ memory contract state
2. Load each KI candidate

### Step 2: CST Integration

1. Load `02_twin_memory/twin-current/{user_id}/SKILL-MATRIX.md`
2. Map each KI to relevant skill dimension
3. Update skill level evidence with new KI

### Step 3: Signal Update to SC-SKILL

1. Notify SC-SKILL of SKILL-MATRIX changes
2. SC-SKILL recalculates SMI (Skill Maturity Index)
3. CTO checks mode unlock thresholds

### Step 4: Clear Queue

1. Clear processed KIs from queue
2. Log consolidation in session log

## Audit & Metrics (Quality Gates)

- **Gate 1 (CPT Immutability):** ANY write attempt to `02_twin_memory/twin-core/` → HALT + REJECT.
- **Metrics:** KI consolidation rate, SMI delta per session
