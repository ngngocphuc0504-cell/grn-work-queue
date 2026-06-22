---
description: Skill signal update — tổng hợp tín hiệu skill và cập nhật Skill Maturity Index.
---

# Workflow: WF-08 Skill Signal Update

- **👤 Owner:** `[@SC-SKILL]` (Skill Coordinator)
- **🛠 Skill Target:** `[sga-07]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-07`**: SMI Calculation Engine — tính toán và cập nhật Skill Maturity Index

## Goal & Governance Context

- **Purpose:** Aggregate skill signals từ các workflow (WF-01→WF-06) và cập nhật SMI. Kiểm tra mode unlock thresholds.
- **Scope:** Chỉ read signals + write SKILL-MATRIX. KHÔNG tự ý unlock mode.

## Execution Steps

### Step 1: Collect Signals

1. Read pending skill signals từ current session
2. Group by SKH dimension (SKH-01 through SKH-05)

### Step 2: Calculate SMI Update

1. Load current SKILL-MATRIX from `02_twin_memory/twin-current/`
2. Apply weighted signal aggregation per dimension
3. Calculate new SMI average

### Step 3: Mode Threshold Check

1. Compare new SMI against `mode_unlock_thresholds` in memory contract:
   - COWORK: smi_avg ≥ 2.0 AND min_tasks ≥ 5
   - DELEGATED: smi_avg ≥ 3.0 AND min_tasks ≥ 15
   - SWARM: smi_avg ≥ 4.0 AND min_tasks ≥ 30
2. IF threshold met → RECOMMEND unlock to CTO (NOT auto-unlock)
3. CTO presents to Human for approval

### Step 4: Persist

1. Update SKILL-MATRIX.md
2. Log SMI change in session log

## Audit & Metrics (Quality Gates)

- **Gate 1 (No Auto-Unlock):** Mode changes MUST go through CTO → Human approval. Auto-unlock = VIOLATION.
- **Metrics:** SMI per dimension, total tasks completed, mode unlock eligibility
