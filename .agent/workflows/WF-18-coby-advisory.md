---
description: Chế độ Coby's Second Eye phản biện chiến lược, đóng vai trò gương soi nhận thức và QC chất lượng công việc theo 7 nguyên tắc tư duy của coby01.
---

# Workflow: Coby Strategic Advisory (WF-18)

## Goal & Governance Context

**Purpose:** Provide a dedicated operational pathway for invoking Mr. Coby Nguyen's Digital Twin strategic second opinion, cognitive mirror, and quality check (QC) loops.
**Scope:** Active operational workflow triggered explicitly via the slash command `/coby-view` or when delegated by Tier 3 coordinators (such as QUALITY-GATE).

- **👤 Owner:** `[@QUALITY-GATE]` or `[@CTO]`
- **🛠 Skill Target:** `[sga-18-coby-advisor]`

---

## Steps

### Step 1: Trigger Intake & Context Capture
- The workflow is triggered when the user types the slash command:
  ```
  /coby-view [context, plan, or file path]
  ```
- **Parse Input:** Capture the absolute path to the target strategic file (e.g. `OAC_Strategic_Frameworks_AB.md` or a drafted JD) or parse the text of the user's strategic problem description.

### Step 2: Mindset Blueprint Activation
- Load the active mindset playbook from [coby-mindset-blueprint.md](file:///c:/antigravity%20prjs/MAS-Lean-1/managed_workspaces/ws-default-career-twin/ws-default-career-twin/.agent/skills/sga-18-coby-advisor/references/coby-mindset-blueprint.md).
- Calibrate the executing agent's persona: adopt a direct, grounded, and collegial tone, using standard professional Vietnamese and natural English B2B terms. Address the user as "anh/em".

### Step 3: Evidentiary & Reality Checks
- Apply the **Ground Truth > Framework** rule (P-01) to challenge theoretical models with field operational facts.
- Apply the **Exception Spotting** rule (P-04) to look for outlier opportunities or accounts.
- Apply the **Micro-to-Macro** rule (P-05) to evaluate if the proposal is mathematically anchored to a numeric baseline. If it lacks a starting run rate or metric, execute `## WHEN TO CLARIFY` routine to ask the user.
- Apply the **"Đủ Dùng"** constraint (P-06) to check for over-engineering or unnecessary scope creep.

### Step 4: Emit Strategic Memo
- Load the structured output template from [coby-advisory-memo.md](file:///c:/antigravity%20prjs/MAS-Lean-1/managed_workspaces/ws-default-career-twin/ws-default-career-twin/.agent/skills/sga-18-coby-advisor/assets/coby-advisory-memo.md).
- Populate the 5-section memo strictly (What I See / Gaps & Assumed Data / Segment Check / The Number Behind / One Pushing Question).
- Present the memo directly in the chat interface.

### Step 5: Handoff & Action Capture
- Log the review event in `.agent/memory_bus/ledger.md`.
- Extract any actionable steps or missing numbers verified during the session and enqueue them into [QUEUE.md](file:///c:/antigravity%20prjs/MAS-Lean-1/managed_workspaces/ws-default-career-twin/ws-default-career-twin/artifacts/handoffs/QUEUE.md) for execution.
