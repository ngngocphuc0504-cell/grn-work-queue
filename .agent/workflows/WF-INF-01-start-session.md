---
description: Start a new working session — Crash Recovery, Memory Bus activation, QUEUE scan, and Morning Briefing. Use when user types "start session" or "begin work".
semantic_triggers: ['bắt đầu phiên', 'start session', 'làm việc thôi', 'chào buổi sáng', 'mở khoá memory']
---

# Workflow: Start Session (Secretary Mode) v2.0.0

// turbo-all

## Goal & Governance Context

**Purpose:** Automatically activate and decrypt the Memory Bus when the user begins working, forcibly recover from any abnormally crashed sessions, scan for pending handover tasks from previous sessions, and dynamically generate a Morning Briefing executive dashboard.
**Scope & SLA:** Applies to all initial morning session start events. Required to execute fully within the first 2 dialogue turns.

## Input

- `start session` request from the Human Orchestrator.

## Execution Steps

### Step 0: Crash Recovery Check ⚠️

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** `.agent/memory_bus/coordinator/status/state.json`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Evaluate crash states and force reset session mapping if anomalous termination is detected.
- **📦 Output Required:** Secure uncorrupted initialization baseline.

**BEFORE proceeding with any operation, the system MUST verify:**

1. Read `.agent/memory_bus/coordinator/status/state.json`
2. Evaluate `session_status`:
   - If `"INACTIVE"` → Normal state, proceed securely to Step 1.
   - If `"ACTIVE"` → ⚠️ Previous session crashed abnormally!

**If a system crash is detected:**
1. Log event securely to `ledger.md`: `| [today date] | SYSTEM | Session-Recovery | Warning | Previous session [last_session_start] ended abnormally |`
2. Force reset state data inside `state.json`: `session_status → "INACTIVE"`, `active_task → null`
3. Check `artifacts/handoffs/QUEUE.md`: flag any task marked `IN_PROGRESS` → immediately alter to `INTERRUPTED`
4. Inject warning into the upcoming Morning Briefing: "⚠️ Previous session ended abnormally. [X] tasks may require emergency review."
5. Proceed to Step 1 normally.

### Step 0.5: Auto-Launch Work Environment 🚀

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** `user_preferences.startup_apps` (hardcoded)
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Launch Chrome with the designated work profile and navigate to the primary productivity dashboard.
- **📦 Output Required:** Browser window opened and navigated.

**ALWAYS execute on every session start (regardless of crash state):**

Run the following PowerShell command to open Chrome with Profile 5 (`ngngocphuc.0504@gmail.com`) pointed at the DB Time Chamber training dashboard:

```powershell
Start-Process "chrome.exe" -ArgumentList '--profile-directory="Profile 5"', 'https://db-time-chamber-training.vercel.app/'
```

> [!NOTE]
> **Profile:** Chrome Profile 5 (`ngngocphuc.0504@gmail.com`)
> **Target URL:** `https://db-time-chamber-training.vercel.app/`
> If Chrome fails to launch, log a warning to `ledger.md` and proceed to Step 1.

### Step 1: Scan Memory Bus & Garena Work Queue (Handoff Iteration)

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** `artifacts/handoffs/QUEUE.md` + `Garena/work queue/garena-tasks.md`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Enumerate and quantify outstanding tasks retaining pending or blocked operational status constraints.
- **📦 Output Required:** Accurate queued bandwidth calculation.

- Scan `artifacts/handoffs/QUEUE.md`
- Identify any pending tasks retaining status `PENDING`, `IN_PROGRESS`, or `BLOCKED`
- Scan `Garena/work queue/garena-tasks.md` and extract any unfinished checklist items (marked with `- [ ]`)
- Accurately count total pending tasks requiring operational bandwidth

### Step 2: Initialize Session State

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** System time data + `state.json`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Lock operational session registry securely into "ACTIVE" state and officially record start temporal bounds.
- **📦 Output Required:** Appended `.agent/memory_bus/ledger.md` log + dynamically updated `state.json`.

- Append log strictly to `ledger.md`: `| [today date] | SYSTEM | Session-Start | Done | Session officially started by [Human Orchestrator] |`
- Update `state.json` securely: override `session_status: "ACTIVE"`, `lock_status: "OPEN"`
- Record official `session_start_time`

### Step 2.1: Settings Engine Initialization
- Nạp cấu hình cá nhân hóa từ `02_twin_memory/twin-current/{user_id}/settings.json`.
- Truy xuất context: tải `CST`, `FRT` snapshot gần nhất và ma trận Skills.

### Step 2.5: Gamification Decay Evaluation (Lazy Engine)

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** `02_twin_memory/twin-current/{user_id}/gamification/XP-LEDGER.json`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Calculate elapsed time since the last recorded session to apply XP decay penalties automatically without a background cronjob.
- **📦 Output Required:** Updated XP total + decay warnings (if any).

**Decay Logic Application:**
1. Read the `session_history` array's last recorded date.
2. Determine `days_since_last_session`.
3. Apply penalty strictly following SECTION 4.3 of Gamification Engine Spec.
   - 3 Days = -10 CP
   - 5 Days = -25 CP
   - 7 Days = -50 CP + Alert
   - Dormancy recovery: +50 CP
4. Inject any decay penalty alerts directly into the upcoming Morning Briefing payload.

### Step 2.6: Conditional Trend Signal Scrape 🕷

- **👤 Owner:** `[@CF-SCANNER]`
- **📥 Input Source:** `content_factory/scripts/scrape_rss.py`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** At session start, prompt the user: "Do you want to run a fresh trend scrape?" If they say nothing or say "no", do not execute. If they say "yes", execute the scraper script (`python content_factory/scripts/scrape_rss.py`) to fetch the latest 10 signals and write to the digest.
- **📦 Output Required:** Scraper script executed conditionally based on user confirmation.

### Step 2.7: External Signal Scrape (Morning Dispatcher) 🌐

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** `session_scanner.py`
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Run the platform scanner script (`python .agent/scripts/session_scanner.py`) to aggregate Google Calendar, Gmail, Drive, Viber, Zalo, and SeaTalk updates into `.agent/memory_bus/coordinator/status/session_context.json`.
- **📦 Output Required:** Compiled `session_context.json` containing active external state context.

### Step 3: Render Morning Briefing Report 🌅

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** Bandwidth calculations (Step 1) + State matrix (Step 2) + Platform cache (Step 2.7)
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Dynamically generate an executive "Morning Briefing" dashboard directly to the visual Chat interface. Parse `session_context.json` to populate meetings, emails, and urgent chats. Always include a reminder at the end: "⚠️ Reminder: Please update your posted article metrics in `content_factory/outputs/performance-log.md` so the twin can calibrate signal scoring and analyze insights!"
- **📦 Output Required:** Premium consolidated executive dashboard displayed visually.

Generate a comprehensive `Morning Briefing` output and broadcast directly to the Chat interface for the Human Orchestrator:

```markdown
## 🌅 Morning Briefing — Session [YYYY-MM-DD]

### 1. System Status & Workspace Bandwidth
- **System Protocol Status:** 🟢 ACTIVE
- **Active Mobilized Workers:** [List IDs if any, e.g., @GOV-COORD]
- **Crash Recovery Status:** [🟢 Clean boot / ⚠️ Recovered from severe underlying crash]
- **Pending Tasks:** [X] tasks
- **In Progress Tasks:** [Y] tasks
- **Blocked Tasks:** 🔴 [Z] tasks (Urgent attention required)

### 1.5. 📅 Probation Milestones Countdown (Onboarding: 2026-06-08)
- **Mid-probation catch-up (T+25):** 2026-07-13 | **[X]** working days remaining
- **Slide submission (T+40):** 2026-08-03 | **[Y]** working days remaining
- **End-probation presentation (T+50):** 2026-08-17 | **[Z]** working days remaining
- *(Note: Working days exclude Saturdays & Sundays)*

### 1.7. 📋 Garena Active Work Queue (garena-tasks.md)
- [List pending tasks/checklist items from Garena/work queue/garena-tasks.md]

### 2. 📅 Today's Agenda (Google Calendar)
*Status: [Google API Status (e.g., 🟢 Connected / ⚠️ Offline Placeholder Mode)]*
- **[Time Range]** - [Event Title] (Organizer: [Name]) [Join Link]
- *(Or "No scheduled meetings for today" if empty)*

### 3. 📬 Actionable Inbox (Gmail)
- **[Sender Name]** - *[Subject]* ([Received Time])
- *(Or "In box is clean" if empty)*

### 4. 💬 Urgent Communications (Zalo, Viber, SeaTalk)
*Status: [Local SQLite Scraper / Universal Notification Bridge]*
- **[[App Name]] [Sender]**: [Message Content] ([Timestamp])
- *(Or "No urgent chats detected in the last 24 hours" if empty)*

### 5. 📂 Recently Modified Files (Google Drive)
- **[Filename]** - (Modified by [User] [Time])

### 6. Recommended Operational Actions (Next Logical Steps)
- [Algorithmic suggestions computed based on Blocked or Pending operational tasks]
```

### Step 4: Standby for Dispatch

- **👤 Owner:** `[@GOV-COORD]`
- **📥 Input Source:** Visual Morning Briefing display (Step 3)
- **🛠 Skill Target:** `[session-manager]`
- **⚙️ Action:** Pause active computations and hold Standby for the Human Orchestrator to assign specific routing duties.
- **📦 Output Required:** Readiness state established for subsequent human objective dispatch.

Pause active computations and hold Standby for the Human Orchestrator to physically assign tasks or issue commands. All task routing processed after this specific step goes explicitly through the `Coordinator` for dispatch mapping to functional Workers.

> [!TIP]
> **Mid-session saves:** If a session runs long or completes a major milestone, invoke `/checkpoint-session` to auto-save state, update ledger, and distill interim DIKW without closing the active session.

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| `state.json` not physically found | First system session or file maliciously deleted | Terminate cycle, create fresh `state.json` populated with default genesis values |
| `QUEUE.md` entirely empty | Expected behavior: No pending work | Normal operation — securely proceed with accepting new task assignments |
| Multiple `ACTIVE` ghost sessions detected | Concurrent session race condition bug | Force reset all session states instantly to `INACTIVE`, deliberately log critical warning |
| `Ledger.md` write cascade fails | Host OS Permission or absolute path mapping issue | Verify rigid path, create logical file directory if missing |

## Audit & Metrics (Quality Gates)

- **Gate 1 (Crash Vector Validation):** `state.json` must be flawlessly decrypted and locked.
- **Gate 2 (Bandwidth Visibility):** The queue length reported in Briefing MUST explicitly match the physical line count of `QUEUE.md` tracking.
- **Verification Matrix:** Log `Session-Start` event successfully written cleanly inside `.agent/memory_bus/ledger.md`.
