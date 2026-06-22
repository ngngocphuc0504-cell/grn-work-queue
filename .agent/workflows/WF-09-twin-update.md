---
description: Twin update — cập nhật Digital Twin layers dựa trên dữ liệu session mới.
---

# Workflow: WF-09 Twin Update

- **👤 Owner:** `[@TC-TWIN]` (Twin Coordinator)
- **🛠 Skill Target:** `[sga-01]`, `[sga-02]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-01`**: Task Framing Methodology — context cho CST pattern updates
> - **`sga-02`**: Review Rubric Protocol — context cho performance pattern updates

## Goal & Governance Context

- **Purpose:** Cập nhật 3 twin layers (CPT/CST/FRT) với dữ liệu session mới. CPT read-only. FRT cần explicit user confirmation.
- **Scope:** Chỉ update twin data trong `02_twin_memory/twin-current/` và `02_twin_memory/twin-future/`. KHÔNG modify `02_twin_memory/twin-core/` (CPT).

## Execution Steps

### Step 1: CST Update (TC-TWIN)

1. Load session reflections, skill signals, work patterns
2. Update `02_twin_memory/twin-current/{user_id}/SKILL-MATRIX.md` with new evidence
3. Label all updates as "[CST]:" explicitly

### Step 2: FRT Proposal (TC-TWIN)

1. IF new gap detected between CST and user goals:
   - Update `02_twin_memory/twin-future/_template/GAP-MAP.md`
   - Update `02_twin_memory/twin-future/_template/LEARNING-QUEUE.md`
2. Present FRT changes to user for explicit confirmation
3. WAIT for user approval before persisting

### Step 3: CPT Verification

1. Verify `02_twin_memory/twin-core/SOUL-CPT.md` has NOT been modified
2. IF modification detected → HALT + alert CTO + rollback

## Audit & Metrics (Quality Gates)

- **Gate 1 (CPT Immutability):** Any write to `02_twin_memory/twin-core/` → HARD STOP + ESCALATE.
- **Gate 2 (FRT User Confirm):** FRT changes without explicit user confirmation string → REJECT.
- **Gate 3 (Layer Labeling):** All output MUST label source layer. Blended assertions → REWORK.
