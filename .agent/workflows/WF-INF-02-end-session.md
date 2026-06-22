---
description: Terminate the active working session — encapsulate Memory Bus, distill DIKW intelligence, and export the Secretary Session Report. Use when user outputs "end session".
semantic_triggers: ['kết thúc phiên', 'đóng workspace', 'nghỉ ngơi', 'end session', 'xuất báo cáo phiên']
---

# Workflow: End Session (Secretary Report System)

// turbo-all

## Goal & Governance Context

**Purpose:** Terminate the active working session safely, distill acquired operational knowledge (DIKW) directly into the Knowledge Base (KB), firmly update the System Ledger, and dynamically generate the Secretary Report payload securely stored within the Memory Bus.
**Scope & SLA:** Mandatory execution before ending the terminal or stopping chat. Must guarantee zero data fragmentation.

## 🗃️ Required Input

- `end session` explicit termination request originating from the Human Orchestrator.

## 🛠️ Execution Sequence

### Step 1: Knowledge Distillation (OODA-DIKW Distillation Engine)

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** Raw conversation history transcript spanning active session
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Systematically classify operational signals and compute rigorous Relevance Scoring to govern persistence logic gates.
- **📦 Output Required:** Proposed explicit Intelligence Distillation Report awaiting Human confirmation.

Agent officially executes the intelligence distillation mapping procedure to relentlessly optimize Memory Bus load limits, actively preventing context bloat overload:

#### 1.1. Observe & Classify (Orient)

Systematically scan the raw conversation history transcript and rigidly classify ALL operational signals into 5 defined groups:
- **DECISION**: Structural design constraints, architectural choices (Record mapping into `.agent/memory_bus/ledger.md` + generate independent explicit KI).
- **PREFERENCE**: Human preferences, desired mechanical working style of the User (Record strictly into `.agent/memory_bus/coordinator/status/state.json` under `["user_preferences"]`).
- **MILESTONE**: Phase physical completion events, recorded audit results (Record specifically into `.agent/memory_bus/coordinator/status/state.json` mapped domain parameter).
- **ERROR**: Execution flaws and implemented logic fixes (Record explicitly into `artifacts/audits/lessons_learned_[date].md`).
- **NOISE**: Casual chit-chat, conversational misinterpretations, hallucinations, network failures (ABSOLUTELY DISCARD - Eradicate).

#### 1.2. Decide (Scoring & Filtering Mechanism)

Compute the strict **Relevance Score** = `(Recurrence*0.4) + (Impact*0.4) + (Novelty*0.2)`.
- **Score ≥ 0.6**: Elevate signal into the Persistence Queue.
- **Score 0.4 - 0.59**: Log temporarily strictly into `ledger.md` (Archival history tracking only).
- **Score < 0.4**: DISCARD (Irrelevant).

#### 1.3. Intelligence Distillation Output Matrix

The agent will visibly output the generated distillation roster array to the Chat interface for documentation purposes:

> **[PROPOSED INTELLIGENCE DISTILLATION REPORT]**
> - **Signal**: [Brief summarized description] | **Classification**: [Type] | **Relevance Score**: [Score]
> - **System Action**: [Where precisely to write / Which specific JSON key to aggressively overwrite]

*Because auto-run is enabled, the system automatically accepts this distillation matrix and immediately transitions to Step 2 without waiting for human confirmation.*

### Step 2: Update Handoff Queue Log

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** Confirmed explicitly approved distillation roster matrix (Step 1.3)
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Access and safely update queue status matrices, firmly codifying pending parameters enabling mechanical resumption.
- **📦 Output Required:** Actively verified updated constraints within `artifacts/handoffs/QUEUE.md`.

- Access and safely update `artifacts/handoffs/QUEUE.md`.
- Transform status classifications of successfully completed operational tasks securely to `COMPLETED`.
- Guarantee mechanically that any actively unfinished tasks remain strictly codified as `PENDING` or `IN_PROGRESS` enabling the subsequent session iteration to resume processing uninterrupted.

### Step 3: Execute Queue Extraction & Archiving

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** `artifacts/handoffs/QUEUE.md`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Trigger the background Python maintenance script to auto-archive completed tasks and enforce the 14-day retention policy.
- **📦 Output Required:** Physically archived items in `artifacts/handoffs/archive/` and a normalized QUEUE.md.

// turbo
```powershell
python .agent/scripts/archive_queue.py --days=14
```

### Step 4: Archive Context to Daily Notes (MAS 5.0 Memory Flush)

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** Executed Queue Update (Step 2) + Evaluated KIs List
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Thực thi "Memory Flush". Agent tự suy ngẫm (silent turn) và phân tách Context Session thành Daily Notes.
- **📦 Output Required:** Memory file physically rendered at `artifacts/daily_notes/[YYYY-MM-DD].md`.

Agent mechanically generates a strict summary report artifact physically rendered at `artifacts/daily_notes/[YYYY-MM-DD].md` utilizing this schema template:

```markdown
# Daily Notes (MAS 5.0): [YYYY-MM-DD]

**1. Work Production Executed (Results)**
- [Roster encapsulating tasks officially marked complete + physical output payload paths]

**2. Contextual Intelligence & Synthesized Learnings (Tacit Knowledge)**
- [Fresh Knowledge Items securely established or rules strategically updated - Để cron job Distillation thu thập sau]

**3. Strategic Hand-over Queue (Outstanding Architecture)**
- [Tasks persisting as PENDING/BLOCKED strictly requiring operational execution in the following lifecycle]
```

### Step 5: Optimize System Tokens (Log Truncation)

- **👤 Owner:** `[@GOV-COORD]`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Execute token truncation script to strictly limit memory bus payloads to 300 lines.

// turbo
```powershell
python .agent/scripts/optimize_memory_tokens.py
```

### Step 5.5: Gamification Computation (Event A — End Session)

- **👤 Owner:** `[SC-SKILL]` & `[@GOV-COORD]` 
- **📥 Input Source:** Active session transcript + Gamification Logs
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Calculate Capability Points (CP), evaluate Blind Trust penalties, update XP Ledger, and check for Level up.
- **📦 Output Required:** Updated JSON logs and ASCII Dashboard UI.

Agent mechanically executes the `SC-SKILL` XP Computation Protocol:
1. Parse session history to satisfy `Event A Schema` criteria (e.g. AI corrections, Blind trust metrics).
2. Compute `net_xp` (Positives rules minus Penalties). 
3. Update `02_twin_memory/twin-current/{user_id}/gamification/XP-LEDGER.json`.
4. Run CTO Level Check. If conditions are met, update `LEVEL-REGISTRY.json` and append privileges.
5. Generate the `Session Pulse` UI block (Progress bar, Skills delta) and PREPARE to append it to the chat interface in Step 6.

### Step 6: Encapsulate Memory Bus & Engage System Lock

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** Systemic Secretary output parameters (Step 4)
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Forcibly transition environmental status variables into an inert locked configuration mapping.
- **📦 Output Required:** Logged temporal finality timestamp and secured explicit operational prompt payload termination sequence.

- Burn the final sequential log securely into `.agent/memory_bus/ledger.md`: "Operational Session Forcefully Terminated at [Timestamp]. Daily Memory Flush Executed."
- Alter operational state file `.agent/memory_bus/coordinator/status/state.json`: forcefully set `"lock_status": "LOCKED"`.
- Transmit a concise operational prompt payload strictly bridging the Chat GUI interface: "Session termination constraints cleanly executed securely. Daily Notes physically stored at `artifacts/daily_notes/`. Recommend rest, Sir/Architect!"

## Audit & Metrics (Quality Gates)

- **Gate 1 (Distillation Generation):** The system MUST generate and output the distillation matrix (Step 1.3) before auto-transitioning to Step 2.
- **Gate 2 (Ledger finalization):** The `ledger.md` must record the precise termination timestamp alongside the `Secretary Report Generation Executed`.
- **Metrics Tracking:** Tally total operational signals saved versus total discarded (Noise Ratio).
