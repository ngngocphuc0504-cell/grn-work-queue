# GAMIFICATION ENGINE SPECIFICATION
## Career Twin Workspace — Autonomy Ramp v1.0
### Document Type: Formal Architecture Specification
**Status:** APPROVED FOR IMPLEMENTATION
**Version:** 1.0 | April 2026
**Owner:** MAS Architecture Practice — Nathan Pham
**Applies to:** ws-career-twin-v1, all governed workspaces in ecosystem

---

## DOCUMENT MAP

```
SECTION 1  — Architecture Philosophy & Constraints
SECTION 2  — Data Schemas (Event A / B / C)
SECTION 3  — Scoring Engine Rules (XP Logic)
SECTION 4  — Level Thresholds & Agentic Privileges
SECTION 5  — Decay & Penalty Logic
SECTION 6  — UI Feedback Templates (End-Session + Weekly Advisory)
SECTION 7  — Agent Computation Instructions
SECTION 8  — Schema Registry & Versioning
```

---

# SECTION 1 — ARCHITECTURE PHILOSOPHY & CONSTRAINTS

## 1.1 Design Principles

```
PRINCIPLE-01: Quality Over Quantity
  XP is earned by QUALITY of engagement, never by volume of tasks alone.
  A user who completes 1 task with deep reflection earns more than
  one who completes 10 tasks with Blind Trust approvals.

PRINCIPLE-02: Decay Is Real
  Inactivity, Blind Trust, and automation dependency generate NEGATIVE
  signals. The system models real capability — not just activity.

PRINCIPLE-03: Privilege Must Be Earned
  Agentic privileges unlock ONLY when quantitative thresholds are met.
  No manual override by user. Gates are enforced by QUALITY-GATE agent.

PRINCIPLE-04: Feedback Is Non-Intrusive
  Dashboard appears ONLY at End-Session and Weekly Advisory.
  Never mid-task. Never as pop-ups. Never blocking workflow.

PRINCIPLE-05: Falsification-Resistant
  Users cannot game the system by repeating trivial actions.
  Novelty bonus applies to first-occurrence events only.
  Diminishing returns apply to repeated same-type actions.

PRINCIPLE-06: Legible to Agents
  All rules use strict Boolean/Numeric logic.
  No natural language ambiguity in scoring triggers.
  Every rule maps to a log field in the Event schema.
```

## 1.2 System Components

```
COMPONENT                AGENT OWNER         READ/WRITE
─────────────────────────────────────────────────────────
XP Ledger               SC-SKILL            READ (all) | WRITE (SC-SKILL only)
Level Registry          CTO                 READ (all) | WRITE (CTO on unlock)
Event A Log             REFLECTION-HARVESTER WRITE on session close
Event B Log             EVAL-ENGINE         WRITE on weekly advisory trigger
Event C Log             EVAL-ENGINE         WRITE on monthly snapshot trigger
Privilege Registry      QUALITY-GATE        READ (gate checks) | WRITE (CTO on unlock)
Dashboard Template      CTO                 WRITE (appended to reports)
Decay Engine            SC-SKILL            RUN daily (background)
```

## 1.3 Data Storage Convention

```
All gamification data stored under:
  02_twin_memory/twin-current/{user_id}/gamification/

File structure:
  gamification/
  ├── XP-LEDGER.json           ← Running XP totals + history
  ├── LEVEL-REGISTRY.json      ← Current level + unlock timestamps
  ├── PRIVILEGE-REGISTRY.json  ← Active privileges + conditions
  ├── events/
  │   ├── event-a/
  │   │   └── {YYYY-MM-DD}.json      ← One per session day
  │   ├── event-b/
  │   │   └── {YYYY-WNN}.json        ← One per week
  │   └── event-c/
  │       └── {YYYY-MM}.json         ← One per month
  └── decay/
      └── DECAY-LOG.json             ← Penalty history
```

---

# SECTION 2 — DATA SCHEMAS

## 2.1 Event A Schema — End Session Log

**Trigger:** WF-INF-02 (End Session) execution
**Writer:** REFLECTION-HARVESTER + CTO
**Frequency:** Once per working session (not per calendar day if no session)

```json
{
  "schema_version": "event-a-v1.0",
  "event_type": "END_SESSION",

  "meta": {
    "user_id": "string",
    "session_id": "string",
    "workspace_id": "ws-career-twin-v1",
    "session_date": "YYYY-MM-DD",
    "session_start": "ISO-8601",
    "session_end": "ISO-8601",
    "session_duration_minutes": 0,
    "co_work_mode_active": "OBSERVE | COWORK | DELEGATED | SWARM"
  },

  "task_telemetry": {
    "tasks_submitted": 0,
    "tasks_completed": 0,
    "tasks_wf01_framed": 0,
    "tasks_wf03_reviewed": 0,
    "tasks_wf04_comm_reviewed": 0,
    "tasks_wf05_passed_quality_gate": 0,
    "tasks_wf05_failed_quality_gate": 0,
    "bounded_delegations_made": 0,
    "bounded_delegations_with_valid_brief": 0
  },

  "input_quality_signals": {
    "quick_captures_submitted": 0,
    "knowledge_captures_submitted": 0,
    "networking_captures_submitted": 0,
    "learning_captures_submitted": 0,
    "sop_digitizations_completed": 0,
    "new_process_mapped": false,
    "daily_morning_checkin_done": false
  },

  "oversight_quality_signals": {
    "reflections_submitted": 0,
    "reflection_quality_scores": [],
    "reflection_avg_quality": 0.0,
    "self_assessments_before_twin_score": 0,
    "ai_corrections_made": 0,
    "ai_assumptions_refuted": 0,
    "ai_outputs_partially_edited": 0,
    "ai_outputs_fully_accepted_unedited": 0,
    "blind_trust_events": 0,
    "blind_trust_threshold_output_length": 500
  },

  "blind_trust_details": [
    {
      "task_id": "string",
      "output_length_tokens": 0,
      "edit_count": 0,
      "flagged": false,
      "flag_reason": "null | ZERO_EDITS_LONG_OUTPUT | AUTO_APPROVE_NO_REVIEW"
    }
  ],

  "skill_signals_generated": {
    "skh_01_work_framing": {"count": 0, "avg_delta": 0.0},
    "skh_02_evidence_reasoning": {"count": 0, "avg_delta": 0.0},
    "skh_03_execution_control": {"count": 0, "avg_delta": 0.0},
    "skh_04_communication": {"count": 0, "avg_delta": 0.0},
    "skh_05_ai_cowork": {"count": 0, "avg_delta": 0.0}
  },

  "ki_distillation": {
    "ki_candidates_queued": 0,
    "ki_passed_all_gates": 0,
    "ki_rejected_gate1_incomplete": 0,
    "ki_rejected_gate2_low_quality": 0,
    "ki_rejected_gate3_duplicate": 0
  },

  "xp_earned_this_session": 0,
  "xp_penalties_this_session": 0,
  "xp_net_this_session": 0,
  "session_xp_breakdown": []
}
```

---

## 2.2 Event B Schema — Weekly Reverse Advisory Log

**Trigger:** Weekly Advisory command (Monday 08:00 or manual trigger)
**Writer:** EVAL-ENGINE
**Frequency:** Once per calendar week

```json
{
  "schema_version": "event-b-v1.0",
  "event_type": "WEEKLY_REVERSE_ADVISORY",

  "meta": {
    "user_id": "string",
    "week_id": "YYYY-WNN",
    "week_start": "YYYY-MM-DD",
    "week_end": "YYYY-MM-DD",
    "sessions_this_week": 0,
    "active_days": 0,
    "inactive_streak_max_days": 0
  },

  "workflow_aggregates": {
    "tasks_total": 0,
    "tasks_fully_completed": 0,
    "processes_digitized": 0,
    "processes_fully_delegated_to_agent": 0,
    "delegation_briefs_written_by_user": 0,
    "delegation_briefs_skipped": 0,
    "handoff_protocol_violations": 0
  },

  "oversight_aggregates": {
    "total_ai_outputs_reviewed": 0,
    "total_ai_corrections": 0,
    "total_ai_refutations": 0,
    "total_ai_assumption_challenges": 0,
    "blind_trust_warnings_issued": 0,
    "blind_trust_repeat_offender": false,
    "blind_trust_repeat_threshold": 3,
    "action_whitelist_proposals_reviewed": 0,
    "action_whitelist_proposals_approved": 0,
    "action_whitelist_proposals_rejected": 0,
    "action_whitelist_proposals_modified": 0
  },

  "input_quality_aggregates": {
    "total_captures": 0,
    "capture_types_used": ["string"],
    "capture_diversity_score": 0.0,
    "days_without_any_capture": 0,
    "morning_checkin_streak": 0,
    "sops_digitized_this_week": 0
  },

  "pattern_analysis": {
    "recurring_errors_detected": [
      {
        "pattern_id": "string",
        "pattern_type": "FRAMING | REASONING | EXECUTION | COMMUNICATION | COWORK",
        "occurrence_count": 0,
        "first_seen": "YYYY-MM-DD",
        "flag_for_coaching": false
      }
    ],
    "strength_patterns_detected": [
      {
        "pattern_id": "string",
        "pattern_type": "string",
        "occurrence_count": 0
      }
    ],
    "new_patterns_vs_last_week": 0,
    "resolved_patterns_vs_last_week": 0
  },

  "xp_week_summary": {
    "xp_earned_week": 0,
    "xp_penalties_week": 0,
    "xp_net_week": 0,
    "xp_running_total": 0,
    "level_at_week_start": "string",
    "level_at_week_end": "string",
    "level_changed_this_week": false
  },

  "advisory_recommendations": [
    {
      "rank": 0,
      "category": "SKILL | HABIT | WORKFLOW | KNOWLEDGE",
      "recommendation": "string",
      "evidence": "string",
      "xp_opportunity": 0
    }
  ]
}
```

---

## 2.3 Event C Schema — Monthly Knowledge Graph Snapshot

**Trigger:** First session of new calendar month
**Writer:** EVAL-ENGINE + SC-SKILL
**Frequency:** Once per calendar month

```json
{
  "schema_version": "event-c-v1.0",
  "event_type": "MONTHLY_SNAPSHOT",

  "meta": {
    "user_id": "string",
    "month_id": "YYYY-MM",
    "snapshot_date": "YYYY-MM-DD",
    "workspace_age_days": 0,
    "total_sessions_lifetime": 0
  },

  "knowledge_graph_state": {
    "total_active_nodes": 0,
    "nodes_by_type": {
      "skills": 0,
      "projects": 0,
      "people": 0,
      "knowledge_items": 0,
      "goals": 0
    },
    "total_connections": 0,
    "avg_connections_per_node": 0.0,
    "orphan_nodes": 0,
    "orphan_node_ids": [],
    "highest_degree_nodes": [],
    "new_nodes_this_month": 0,
    "deprecated_nodes_this_month": 0,
    "graph_density_score": 0.0,
    "graph_health_score": 0.0
  },

  "ki_store_state": {
    "total_ki_count": 0,
    "ki_by_type": {
      "PATTERN": 0,
      "INSIGHT": 0,
      "PROCEDURE": 0,
      "CONSTRAINT": 0
    },
    "ki_by_scope": {
      "USER": 0,
      "AGENT": 0,
      "WORKSPACE": 0
    },
    "ki_stale_count": 0,
    "ki_stale_threshold_days": 60,
    "ki_applied_to_tasks_this_month": 0,
    "ki_application_rate": 0.0,
    "ki_created_this_month": 0
  },

  "skill_maturity_state": {
    "smi_snapshot": {
      "work_framing": 0.0,
      "evidence_reasoning": 0.0,
      "execution_control": 0.0,
      "communication": 0.0,
      "ai_cowork": 0.0
    },
    "smi_average": 0.0,
    "smi_delta_vs_last_month": {
      "work_framing": 0.0,
      "evidence_reasoning": 0.0,
      "execution_control": 0.0,
      "communication": 0.0,
      "ai_cowork": 0.0
    },
    "fastest_growing_skill": "string",
    "most_stagnant_skill": "string",
    "skills_at_target_level": 0,
    "skills_below_target": 0
  },

  "frt_gap_state": {
    "role_pack": "string",
    "frt_version": "string",
    "gap_map_summary": {
      "work_framing": {"frt_target": 0.0, "current": 0.0, "gap": 0.0},
      "evidence_reasoning": {"frt_target": 0.0, "current": 0.0, "gap": 0.0},
      "execution_control": {"frt_target": 0.0, "current": 0.0, "gap": 0.0},
      "communication": {"frt_target": 0.0, "current": 0.0, "gap": 0.0},
      "ai_cowork": {"frt_target": 0.0, "current": 0.0, "gap": 0.0}
    },
    "total_gap_score": 0.0,
    "gap_closing_rate_per_month": 0.0,
    "projected_frt_achievement_months": 0
  },

  "xp_monthly_summary": {
    "xp_earned_month": 0,
    "xp_penalties_month": 0,
    "xp_net_month": 0,
    "xp_running_total": 0,
    "level_at_month_start": "string",
    "level_at_month_end": "string"
  }
}
```

---

# SECTION 3 — SCORING ENGINE RULES

## 3.1 XP Architecture

```
XP is denominated in CAPABILITY POINTS (CP).

XP_RUNNING_TOTAL = Σ(POSITIVE_SIGNALS) - Σ(DECAY_PENALTIES) + Σ(BONUS_MULTIPLIERS)

Constraints:
  XP_RUNNING_TOTAL >= 0 (floor at zero, never negative total)
  Single session XP cap: 500 CP (prevents gaming via marathon sessions)
  Weekly XP cap: 2000 CP
  No monthly cap (encourages sustained engagement)
```

## 3.2 Positive Signal Table

| Signal ID | Event | Condition | Base CP | Diminishing Returns | Novelty Bonus |
|-----------|-------|-----------|---------|--------------------|----|
| **PS-01** | Brief framing completed | WF-01 output meets 5-element check | 10 | After 5/day: 50% | +5 if first ever |
| **PS-02** | Self-assessment before twin score | `self_assessments_before_twin_score > 0` in session | 15 | After 3/day: 0 | N/A |
| **PS-03** | AI correction made | `ai_corrections_made >= 1` in task | 20 | After 3/session: 50% | N/A |
| **PS-04** | AI assumption refuted | `ai_assumptions_refuted >= 1` in task | 25 | After 2/session: 25% | N/A |
| **PS-05** | Reflection quality 3/3 | `reflection_quality_score == 3` | 30 | After 2/day: 50% | N/A |
| **PS-06** | Reflection quality 2/3 | `reflection_quality_score == 2` | 15 | After 2/day: 50% | N/A |
| **PS-07** | SOP digitized | `sop_digitizations_completed >= 1` | 50 | After 2/week: 50% | +25 first ever |
| **PS-08** | New process mapped | `new_process_mapped == true` | 75 | After 1/week: 0 | +50 first ever |
| **PS-09** | Knowledge capture submitted | `knowledge_captures_submitted >= 1` | 10 | After 3/day: 25% | N/A |
| **PS-10** | Morning check-in done | `daily_morning_checkin_done == true` | 5 | N/A | +10 if 7-day streak |
| **PS-11** | KI passed all 4 gates | `ki_passed_all_gates >= 1` | 20 | After 3/session: 50% | N/A |
| **PS-12** | Delegation brief written | `delegation_briefs_written_by_user >= 1` | 15 | After 3/session: 25% | +20 first ever |
| **PS-13** | Partial edit (AI output edited) | `ai_outputs_partially_edited >= 1` | 8 | After 5/session: 0 | N/A |
| **PS-14** | Quality gate PASS | `tasks_wf05_passed_quality_gate >= 1` | 20 | After 3/session: 50% | N/A |
| **PS-15** | Weekly capture diversity score ≥0.7 | Event B: `capture_diversity_score >= 0.7` | 50 | Weekly, no DR | N/A |
| **PS-16** | Morning check-in 5-day streak | Event B: `morning_checkin_streak >= 5` | 25 | Weekly | N/A |
| **PS-17** | Zero blind trust events in week | Event B: `blind_trust_warnings_issued == 0` | 75 | Weekly | N/A |
| **PS-18** | KI application rate ≥50% | Event C: `ki_application_rate >= 0.50` | 100 | Monthly | N/A |
| **PS-19** | Knowledge graph density ≥0.3 | Event C: `graph_density_score >= 0.30` | 100 | Monthly | N/A |
| **PS-20** | SMI delta positive (any skill) | Event C: any `smi_delta > 0` | 50/skill | Per skill, monthly | N/A |
| **PS-21** | Action whitelist item reviewed+modified | `action_whitelist_proposals_modified >= 1` | 35 | After 2/week: 50% | N/A |
| **PS-22** | Recurring error resolved | Event B: `resolved_patterns_vs_last_week >= 1` | 60 | Per pattern | N/A |

**Diminishing Returns (DR) function:**
```
DR_multiplier(n, threshold, floor):
  IF n <= threshold: multiplier = 1.0
  IF n > threshold: multiplier = max(floor, 1.0 - (0.5 * (n - threshold)))
  Applied per Signal ID per session/day/week as specified
```

---

## 3.3 Bonus Multiplier Table

| Multiplier ID | Condition | Effect |
|--------------|-----------|--------|
| **BM-01: Correction Streak** | ≥3 AI corrections in single session | +50% on all PS-03 CP this session |
| **BM-02: Refutation Streak** | ≥2 AI refutations in single session | +30% on all PS-04 CP this session |
| **BM-03: Perfect Oversight Session** | PS-02 + PS-03 + PS-05 all triggered in same session | +100 flat bonus |
| **BM-04: Zero Blind Trust Week** | PS-17 triggered (0 BT events entire week) | +25% on all Event B positives |
| **BM-05: Learning Capture Chain** | ≥3 different capture types in same day | +40 flat bonus |
| **BM-06: Level-Up Bonus** | Level threshold crossed | +200 flat (one-time per level) |
| **BM-07: Weekly Consistency** | ≥4 active days with ≥1 reflection | +75 flat (Event B) |
| **BM-08: KI Excellence Month** | Monthly `ki_application_rate >= 0.70` | +150 flat (Event C) |

---

# SECTION 4 — DECAY & PENALTY LOGIC

## 4.1 Penalty Table

| Penalty ID | Trigger Event | Condition | CP Penalty | Notes |
|-----------|--------------|-----------|------------|-------|
| **PEN-01: Blind Trust — Short** | End Session | `output_length_tokens >= 200 AND edit_count == 0` | -10 per occurrence | Includes auto-approved outputs |
| **PEN-02: Blind Trust — Long** | End Session | `output_length_tokens >= 500 AND edit_count == 0` | -25 per occurrence | Replaces PEN-01 (not additive) |
| **PEN-03: Blind Trust — Block** | End Session | `output_length_tokens >= 1000 AND edit_count == 0` | -50 per occurrence | Critical violation |
| **PEN-04: No Reflection** | End Session | `reflections_submitted == 0 AND tasks_submitted > 0` | -30 | Per session |
| **PEN-05: Delegation Skip** | End Session | `bounded_delegations_made > 0 AND delegation_briefs_written_by_user == 0` | -20 per skip | Delegating without brief |
| **PEN-06: Capture Drought** | Event B (Weekly) | `days_without_any_capture >= 3` | -75 | Per week |
| **PEN-07: Blind Trust Repeat** | Event B (Weekly) | `blind_trust_warnings_issued >= 3` | -100 | Repeat offender flag |
| **PEN-08: Checkin Streak Break** | Event B (Weekly) | `morning_checkin_streak == 0 AND active_days >= 3` | -25 | |
| **PEN-09: Orphan KI Accumulation** | Event C (Monthly) | `orphan_nodes >= 10` | -50 | Unmaintained knowledge graph |
| **PEN-10: KI Stale Accumulation** | Event C (Monthly) | `ki_stale_count >= 15` | -75 | Too many stale knowledge items |
| **PEN-11: SMI Regression** | Event C (Monthly) | any `smi_delta < -0.2` | -40 per skill | Skill going backwards |
| **PEN-12: No Process Digitized (30 days)** | Event C (Monthly) | `processes_digitized == 0 AND workspace_age_days >= 30` | -100 | Failure to build procedural memory |
| **PEN-13: Reflection Quality 0/3 Twice** | End Session | `reflection_quality_score == 0 twice in same session` | -40 | Pattern of minimal effort |

## 4.2 Penalty Ceiling Rules

```
RULE: Max penalty per session = 200 CP
RULE: Max penalty per week = 500 CP (prevents runaway negative spiral)
RULE: PEN-02 and PEN-03 are mutually exclusive (highest applies)
RULE: PEN-07 supersedes PEN-01/02/03 for the week (not additive)
RULE: Floor on XP_RUNNING_TOTAL = 0 (cannot go negative)
```

## 4.3 Decay Engine — Daily Background Run

```
DECAY_ENGINE runs daily at 00:00 user timezone
Checks: days since last session

IF days_since_last_session == 0: no decay
IF days_since_last_session == 1: no decay (yesterday's session)
IF days_since_last_session == 2: no decay (grace day)
IF days_since_last_session == 3: SOFT_DECAY = -10 CP (silent, logged)
IF days_since_last_session == 5: MEDIUM_DECAY = -25 CP (logged + alert queued)
IF days_since_last_session == 7: HARD_DECAY = -50 CP + ALERT issued
IF days_since_last_session == 14: DORMANCY_FLAG = true + ALERT issued
IF days_since_last_session >= 30: DORMANCY = -100 CP one-time + status set to DORMANT

DORMANCY recovery: First session after dormancy = WAKE_UP_BONUS +50 CP
```

---

# SECTION 5 — LEVEL THRESHOLDS & AGENTIC PRIVILEGES

## 5.1 Level Architecture Overview

```
LEVEL 1: THE INTERN          XP: 0 → 499
LEVEL 2: THE ANALYST         XP: 500 → 1,999
LEVEL 3: THE CHIEF OF STAFF  XP: 2,000 → 4,999
LEVEL 4: THE TWIN            XP: 5,000 → 9,999
LEVEL 5: THE MASTER          XP: 10,000+
```

**Important:** XP is NECESSARY but NOT SUFFICIENT for level unlock.
All quantitative criteria below must ALSO be met.
Level registry is updated by CTO only when ALL conditions pass.

---

## 5.2 Level 1 — THE INTERN

**Philosophy:** The user is learning the co-work protocol. Twin observes, demonstrates, and challenges. Human watches and confirms.

### Unlock Criteria (Default starting state — no unlock required)

| Criterion | Value | Source Field |
|-----------|-------|-------------|
| XP minimum | 0 | xp_running_total |
| Onboarding complete | true | onboarding_complete |

### Quantitative Requirements to HOLD Level 1

```
No requirements — this is the entry state.
But falling below requirements for Level 2 after achieving it = demotion to Level 1.
```

### Agentic Privileges — Level 1

| Privilege ID | Privilege | Status |
|-------------|-----------|--------|
| PRIV-L1-01 | View own SKILL-MATRIX.md | ACTIVE |
| PRIV-L1-02 | Submit tasks for twin framing (WF-01) | ACTIVE |
| PRIV-L1-03 | Receive twin reviews (WF-03, WF-04) | ACTIVE |
| PRIV-L1-04 | Twin demonstrates tasks (OBSERVE mode) | ACTIVE |
| PRIV-L1-05 | Knowledge captures accepted | ACTIVE |
| PRIV-L1-06 | Access Labs 1-2 | ACTIVE |
| PRIV-L1-07 | Delegation briefs: LOCKED | LOCKED |
| PRIV-L1-08 | Executor-Swarm: LOCKED | LOCKED |
| PRIV-L1-09 | Action Whitelist: LOCKED | LOCKED |
| PRIV-L1-10 | FRT modification: LOCKED | LOCKED |

---

## 5.3 Level 2 — THE ANALYST

**Philosophy:** The user has proven they can frame work correctly and review AI critically. COWORK mode unlocks. Twin now challenges actively, not just demonstrates.

### Unlock Criteria

| Criterion | Required Value | Source Field | Logic |
|-----------|---------------|-------------|-------|
| XP total | >= 500 | xp_running_total | AND |
| Sessions completed | >= 10 | total_sessions_lifetime | AND |
| SOPs digitized | >= 1 | processes_digitized (lifetime) | AND |
| Reflections submitted | >= 8 | reflections_submitted (lifetime) | AND |
| Reflection quality avg | >= 2.0/3.0 | reflection_avg_quality (last 5) | AND |
| AI corrections made | >= 5 | ai_corrections_made (lifetime) | AND |
| Blind trust warnings | <= 2 | blind_trust_warnings_issued (last 2 weeks) | AND |
| SMI average | >= 1.5 | smi_average (current) | AND |
| Morning check-in streak | >= 3 | morning_checkin_streak (current) | AND |

### Unlock Boolean Logic

```python
level_2_unlock = (
    xp_running_total >= 500 AND
    total_sessions >= 10 AND
    lifetime_sops >= 1 AND
    lifetime_reflections >= 8 AND
    recent_reflection_avg >= 2.0 AND
    lifetime_ai_corrections >= 5 AND
    recent_blind_trust_warnings <= 2 AND
    smi_average >= 1.5 AND
    checkin_streak >= 3
)
```

### Agentic Privileges Unlocked — Level 2

| Privilege ID | Privilege | Condition |
|-------------|-----------|-----------|
| PRIV-L2-01 | COWORK mode activated | Automatic on unlock |
| PRIV-L2-02 | Delegation briefs accepted | Requires valid brief schema |
| PRIV-L2-03 | Access Labs 3-4 | Automatic on unlock |
| PRIV-L2-04 | Twin proposes workflow improvements | Weekly Advisory feature |
| PRIV-L2-05 | FRT gap map visible | View-only, no modification |
| PRIV-L2-06 | SMI Dashboard with trend lines | Full 5-dimension view |
| PRIV-L2-07 | Executor-Swarm (bounded): LOCKED | Still locked |
| PRIV-L2-08 | Action Whitelist: LOCKED | Still locked |

---

## 5.4 Level 3 — THE CHIEF OF STAFF

**Philosophy:** The user manages the twin like a capable chief of staff. They delegate reliably, spot errors systematically, and their knowledge graph is actively growing and connected.

### Unlock Criteria

| Criterion | Required Value | Source Field | Logic |
|-----------|---------------|-------------|-------|
| XP total | >= 2,000 | xp_running_total | AND |
| Sessions completed | >= 30 | total_sessions_lifetime | AND |
| SOPs digitized | >= 3 | processes_digitized (lifetime) | AND |
| Processes delegated to agent | >= 5 | processes_fully_delegated (lifetime) | AND |
| Valid delegation briefs | >= 10 | delegation_briefs_written (lifetime) | AND |
| Reflections quality 3/3 | >= 10 | lifetime count of score==3 reflections | AND |
| AI refutations made | >= 10 | ai_assumptions_refuted (lifetime) | AND |
| Blind trust warnings | <= 1 | blind_trust_warnings_issued (last 4 weeks) | AND |
| SMI average | >= 2.5 | smi_average (current) | AND |
| Any skill at Level 3+ | >= 1 | smi_snapshot any value >= 3.0 | AND |
| Active KI nodes | >= 20 | ki_store_state.total_ki_count | AND |
| KI application rate | >= 0.30 | ki_application_rate (last month) | AND |

### Unlock Boolean Logic

```python
level_3_unlock = (
    xp_running_total >= 2000 AND
    total_sessions >= 30 AND
    lifetime_sops >= 3 AND
    lifetime_delegated_processes >= 5 AND
    lifetime_valid_delegation_briefs >= 10 AND
    lifetime_quality_3_reflections >= 10 AND
    lifetime_ai_refutations >= 10 AND
    recent_blind_trust_warnings <= 1 AND
    smi_average >= 2.5 AND
    max(smi_snapshot.values()) >= 3.0 AND
    total_ki_count >= 20 AND
    ki_application_rate >= 0.30
)
```

### Agentic Privileges Unlocked — Level 3

| Privilege ID | Privilege | Condition |
|-------------|-----------|-----------|
| PRIV-L3-01 | DELEGATED mode activated | Automatic on unlock |
| PRIV-L3-02 | Executor-Swarm: bounded tasks | Valid brief required each time |
| PRIV-L3-03 | Lab 5 access (Read Your Progress) | Automatic |
| PRIV-L3-04 | Twin proposes new SOPs proactively | Based on task pattern detection |
| PRIV-L3-05 | Action Whitelist PROPOSAL mode | User reviews + approves proposed actions |
| PRIV-L3-06 | FRT modification (with confirmation) | Explicit confirmation string required |
| PRIV-L3-07 | Reverse Advisory — DEEP mode | Full pattern analysis available |
| PRIV-L3-08 | Knowledge Graph visualization | Full 5-node graph view |
| PRIV-L3-09 | SWARM mode: LOCKED | Still locked |
| PRIV-L3-10 | Full Action Whitelisting: LOCKED | Still locked |

---

## 5.5 Level 4 — THE TWIN

**Philosophy:** The user's twin is a genuine extension of them. It represents their thinking accurately, executes with high fidelity, and the human-twin pair operates as a coordinated unit.

### Unlock Criteria

| Criterion | Required Value | Source Field | Logic |
|-----------|---------------|-------------|-------|
| XP total | >= 5,000 | xp_running_total | AND |
| Sessions completed | >= 60 | total_sessions_lifetime | AND |
| SOPs digitized | >= 6 | processes_digitized (lifetime) | AND |
| Processes fully delegated | >= 15 | processes_fully_delegated (lifetime) | AND |
| SMI average | >= 3.5 | smi_average (current) | AND |
| ≥ 2 skills at Level 4+ | >= 2 | count(smi values >= 4.0) | AND |
| AI refutations lifetime | >= 30 | ai_assumptions_refuted (lifetime) | AND |
| Blind trust events (90d) | = 0 | blind_trust_warnings_issued (last 90 days) | AND |
| KI count active | >= 50 | total_ki_count | AND |
| KI application rate | >= 0.50 | ki_application_rate (last 3 months avg) | AND |
| Graph density score | >= 0.40 | graph_density_score (last month) | AND |
| No orphan nodes | <= 3 | orphan_nodes (last month) | AND |
| FRT gap closing rate positive | true | gap_closing_rate_per_month > 0 | AND |
| Action whitelist reviewed ≥5 | >= 5 | action_whitelist_proposals_reviewed (lifetime) | AND |

### Unlock Boolean Logic

```python
level_4_unlock = (
    xp_running_total >= 5000 AND
    total_sessions >= 60 AND
    lifetime_sops >= 6 AND
    lifetime_delegated_processes >= 15 AND
    smi_average >= 3.5 AND
    len([v for v in smi_snapshot.values() if v >= 4.0]) >= 2 AND
    lifetime_ai_refutations >= 30 AND
    blind_trust_warnings_90d == 0 AND
    total_ki_count >= 50 AND
    avg_ki_application_rate_3m >= 0.50 AND
    graph_density_score >= 0.40 AND
    orphan_nodes <= 3 AND
    gap_closing_rate_per_month > 0 AND
    action_whitelist_reviewed >= 5
)
```

### Agentic Privileges Unlocked — Level 4

| Privilege ID | Privilege | Condition |
|-------------|-----------|-----------|
| PRIV-L4-01 | SWARM mode activated | Full MAS swarm coordination |
| PRIV-L4-02 | Action Whitelist EXECUTION mode | Approved actions execute autonomously |
| PRIV-L4-03 | Twin self-updates CST between sessions | Background learning without prompt |
| PRIV-L4-04 | Proactive twin briefings | Twin prepares morning brief without check-in |
| PRIV-L4-05 | Multi-project parallel orchestration | Swarm coordinates across active projects |
| PRIV-L4-06 | Twin proposes FRT evolution | Quarterly update drafted proactively |
| PRIV-L4-07 | Networking agent activated | Relationship nurturing reminders + draft follow-ups |
| PRIV-L4-08 | Cross-project knowledge synthesis | Twin connects insights across projects automatically |
| PRIV-L4-09 | Full Twin Mode: LOCKED | Requires Level 5 |

---

## 5.6 Level 5 — THE MASTER / SYMBIOSIS

**Philosophy:** Human and twin are genuinely symbiotic. The human focuses entirely on judgment, relationships, and creativity. The twin handles execution orchestration autonomously. The user has built something larger than themselves.

### Unlock Criteria

| Criterion | Required Value | Source Field | Logic |
|-----------|---------------|-------------|-------|
| XP total | >= 10,000 | xp_running_total | AND |
| Sessions completed | >= 120 | total_sessions_lifetime | AND |
| SOPs digitized | >= 10 | processes_digitized (lifetime) | AND |
| SMI average | >= 4.0 | smi_average (current) | AND |
| ≥ 3 skills at Level 4+ | >= 3 | count(smi values >= 4.0) | AND |
| Any skill at Level 5 | >= 1 | count(smi values == 5.0) | AND |
| Blind trust events (180d) | = 0 | blind_trust_warnings_issued (last 180 days) | AND |
| KI count active | >= 100 | total_ki_count | AND |
| KI application rate | >= 0.70 | ki_application_rate (last 6 months avg) | AND |
| Graph density score | >= 0.60 | graph_density_score (last month) | AND |
| Orphan nodes | = 0 | orphan_nodes (last month) | AND |
| FRT achieved (any skill) | >= 1 | count(smi >= frt_target for any skill) | AND |
| Processes fully automated | >= 10 | processes_fully_delegated (lifetime) | AND |
| Recurring errors resolved | >= 5 | resolved_patterns_lifetime | AND |

### Unlock Boolean Logic

```python
level_5_unlock = (
    xp_running_total >= 10000 AND
    total_sessions >= 120 AND
    lifetime_sops >= 10 AND
    smi_average >= 4.0 AND
    len([v for v in smi_snapshot.values() if v >= 4.0]) >= 3 AND
    max(smi_snapshot.values()) == 5.0 AND
    blind_trust_warnings_180d == 0 AND
    total_ki_count >= 100 AND
    avg_ki_application_rate_6m >= 0.70 AND
    graph_density_score >= 0.60 AND
    orphan_nodes == 0 AND
    any(smi_snapshot[s] >= frt_target[s] for s in smi_snapshot) AND
    lifetime_delegated_processes >= 10 AND
    resolved_patterns_lifetime >= 5
)
```

### Agentic Privileges Unlocked — Level 5

| Privilege ID | Privilege | Condition |
|-------------|-----------|-----------|
| PRIV-L5-01 | Full Twin Autonomy Mode | All agents operate with full brief execution |
| PRIV-L5-02 | Dynamic Action Whitelisting | User defines categories, twin applies judgment |
| PRIV-L5-03 | Twin-initiated strategic recommendations | Unprompted FRT advisory |
| PRIV-L5-04 | Cross-workspace knowledge export | Package KIs for training others |
| PRIV-L5-05 | Twin trains new agents | User's procedural memory seeds new workspaces |
| PRIV-L5-06 | Ecosystem architect role | Can govern sub-workspaces as meta-orchestrator |
| PRIV-L5-07 | Legacy mode | Twin continues operating when user offline for 48h |
| PRIV-L5-08 | MASTER Certificate | Export verified skill credentials (OECD literacy level) |

---

## 5.7 Level Summary Table

| Level | Title | XP Range | Key Quantitative Gates | Mode | Key Privilege |
|-------|-------|----------|------------------------|------|---------------|
| 1 | The Intern | 0-499 | Onboarding complete | OBSERVE | Twin demonstrates |
| 2 | The Analyst | 500-1,999 | 10 sessions, 1 SOP, 5 corrections, BT ≤2 | COWORK | Delegation briefs |
| 3 | Chief of Staff | 2,000-4,999 | 30 sessions, 3 SOPs, 10 refutations, SMI≥2.5 | DELEGATED | Executor-Swarm + Whitelist proposals |
| 4 | The Twin | 5,000-9,999 | 60 sessions, 6 SOPs, 0 BT/90d, SMI≥3.5, KI≥50 | SWARM | Autonomous execution |
| 5 | The Master | 10,000+ | 120 sessions, 10 SOPs, 0 BT/180d, SMI≥4.0, KI≥100 | SYMBIOSIS | Full autonomy + legacy |

---

# SECTION 6 — UI FEEDBACK TEMPLATES

## 6.1 End-Session Dashboard (Event A Appendix)

Appended to session close report. Maximum 30 lines. Non-blocking. No action required from user.

```markdown
---
## ⚡ SESSION PULSE — [YYYY-MM-DD]

**Level:** [LEVEL_TITLE] | **XP:** [RUNNING_TOTAL] → [NEXT_LEVEL_XP] | **To next:** [GAP] CP

```
[████████████████░░░░░░░░░░░░░░] [PCT]% to [NEXT_LEVEL]
```

### Today's CP
| Signal | Count | CP Earned |
|--------|-------|-----------|
| [signal descriptions] | [n] | +[cp] |
| **Penalties** | | -[cp] |
| **Net this session** | | **[net]** |

### Co-Work Quality
🟢 AI Corrections: [n]  🟢 Refutations: [n]  🟢 Reflections: [score]/3
[🔴 Blind Trust events: [n] — [penalty note]] (only shown if BT > 0)

### Skill Pulse (last 5 sessions avg delta)
Work Framing  [▲/▼/─] [score]/5
Evidence      [▲/▼/─] [score]/5
Execution     [▲/▼/─] [score]/5
Communication [▲/▼/─] [score]/5
AI Co-Work    [▲/▼/─] [score]/5

[If level-up: 🎯 LEVEL UP: You are now [NEW_LEVEL]. [1-line unlock message]]
[If no reflection: ⚠️ Reflection pending — session not fully closed]

---
```

**Rendering rules:**
```
Progress bar: [████░░░░] format, 30 chars wide
▲ = smi_delta > 0 | ▼ = smi_delta < 0 | ─ = smi_delta == 0
BT block: ONLY rendered if blind_trust_events > 0
Level-up block: ONLY rendered if level changed this session
Reflection warning: ONLY rendered if reflection_pending = true
```

---

## 6.2 Weekly Advisory Dashboard (Event B Appendix)

Appended to Weekly Reverse Advisory report. Maximum 60 lines.

```markdown
---
## 📊 WEEKLY GAMIFICATION REPORT — Week [WNN], [YYYY]

### Level & XP
**Current Level:** [LEVEL_TITLE]
**XP this week:** +[earned] gained | -[penalties] penalties | **Net: [net] CP**
**Running total:** [total] CP

```
Journey: [L1]──[L2]──[L3]──●──[L4]──[L5]
              [progress marker at current position]
```

### Week at a Glance

| Metric | This Week | Last Week | Trend |
|--------|-----------|-----------|-------|
| Tasks completed | [n] | [n] | [▲▼─] |
| AI corrections | [n] | [n] | [▲▼─] |
| AI refutations | [n] | [n] | [▲▼─] |
| Blind Trust events | [n] | [n] | [▲▼─] |
| Captures made | [n] | [n] | [▲▼─] |
| Reflections 3/3 | [n] | [n] | [▲▼─] |
| SOPs digitized | [n] | [n] | [▲▼─] |

### Oversight Quality Score: [0-100]
```
[██████████████░░░░░░] [score]/100
```
Calculated: (corrections×2 + refutations×3 + reflections_quality×1.5) / max_possible

### Patterns Detected This Week
🔴 New error patterns: [n] — [descriptions]
🟢 Strengths reinforced: [n] — [descriptions]
✅ Resolved from last week: [n] — [descriptions]

### Next Level Progress
**To unlock [NEXT_LEVEL], you still need:**
| Requirement | Current | Required | Gap |
|------------|---------|----------|-----|
| [criterion] | [value] | [value] | [gap] |
| [criterion] | [value] | [value] | [gap] |
| ... | | | |

### CP Opportunity This Week
> Top 3 highest-value actions you could have taken:
> 1. [action] — would have earned [n] CP
> 2. [action] — would have earned [n] CP
> 3. [action] — would have earned [n] CP

[If level-up this week: 🏆 LEVEL ACHIEVED THIS WEEK: [LEVEL_TITLE]]
[If demotion risk: ⚠️ WARNING: [n] more BT events will trigger review]

---
```

---

## 6.3 Monthly Snapshot Badge (Event C Appendix)

Appended to Monthly Deep Dive Advisory report. Maximum 40 lines.

```markdown
---
## 🗓️ MONTHLY CAPABILITY SNAPSHOT — [Month YYYY]

**Level:** [TITLE] | **XP:** [total] | **Workspace age:** [N] days

### Skill Maturity Index (Current vs Target)
```
Work Framing  ████████████░░░░░░░░ [score]/5 → FRT: [target]  [gap]
Evidence      ██████████░░░░░░░░░░ [score]/5 → FRT: [target]  [gap]
Execution     ████████████████░░░░ [score]/5 → FRT: [target]  [gap]
Communication ████████░░░░░░░░░░░░ [score]/5 → FRT: [target]  [gap]
AI Co-Work    ██████████████░░░░░░ [score]/5 → FRT: [target]  [gap]
```
**FRT Achievement:** [N]% | Projected completion: [N] months

### Knowledge Graph Health
Total nodes: [n]  |  Connections: [n]  |  Density: [score]/1.0
Orphan nodes: [n]  |  Stale KIs: [n]  |  KI applied rate: [pct]%

### This Month's Milestones
[List of unlocks, level changes, personal bests]

### 3-Month Trend
XP: [M-2] → [M-1] → [M] [trend arrow]
SMI avg: [M-2] → [M-1] → [M] [trend arrow]

---
```

---

# SECTION 7 — AGENT COMPUTATION INSTRUCTIONS

## 7.1 SC-SKILL (Skill Coordinator) — XP Computation Protocol

```
ON EVENT_A_CLOSE:
  1. Load current XP-LEDGER.json
  2. For each PS-* rule: evaluate condition against event_a payload
  3. Apply diminishing returns per PS table
  4. Apply bonus multipliers (check BM-* conditions)
  5. For each PEN-* rule: evaluate condition against event_a payload
  6. Apply penalty ceiling (max 200 CP penalty per session)
  7. Apply XP session cap (max 500 CP positive per session)
  8. net_xp = sum(positive_signals) - sum(penalties)
  9. Update XP-LEDGER.json:
       running_total += net_xp (floor at 0)
       session_history.append(session_record)
  10. Write event_a to events/event-a/{date}.json
  11. Signal CTO: xp_updated, current_level, running_total

ON EVENT_B_CLOSE:
  1. Aggregate all event_a logs for the week
  2. Compute Event B fields from aggregates
  3. Evaluate PS-15 through PS-22 (weekly signals)
  4. Evaluate PEN-06 through PEN-08 (weekly penalties)
  5. Apply BM-04, BM-07 multipliers
  6. Check decay engine output for the week
  7. Update XP-LEDGER.json with week total
  8. Write event_b to events/event-b/{week_id}.json

ON EVENT_C_CLOSE:
  1. Aggregate all event_b logs for the month
  2. Compute Knowledge Graph state from 02_twin_memory/twin-current/{user_id}/
  3. Compute SMI monthly delta (current vs last month)
  4. Evaluate PS-18 through PS-20 (monthly signals)
  5. Evaluate PEN-09 through PEN-12 (monthly penalties)
  6. Apply BM-08 multiplier
  7. Update XP-LEDGER.json with month total
  8. Write event_c to events/event-c/{month_id}.json
```

## 7.2 CTO (Orchestrator) — Level Check Protocol

```
TRIGGER: After every SC-SKILL XP update

LEVEL_CHECK_PROCEDURE:
  1. Load LEVEL-REGISTRY.json (current_level)
  2. Load XP-LEDGER.json (running_total)
  3. Load all required data fields for next level check
  4. Evaluate unlock_boolean_logic for (current_level + 1)
  5. IF all conditions TRUE:
       a. Write LEVEL-REGISTRY.json: level = new_level, unlocked_at = timestamp
       b. Write PRIVILEGE-REGISTRY.json: add new privileges
       c. Trigger BM-06 bonus (+200 CP)
       d. Append level-up block to next session dashboard
       e. Log: LEVEL_UP event
  6. IF conditions FALSE: no action, log which conditions failed
  7. Check demotion: IF current_level > 1 AND key criteria drop below threshold:
       a. Issue WARNING (not immediate demotion)
       b. 7-day grace period before demotion executes
       c. Log: DEMOTION_WARNING event
```

## 7.3 EVAL-ENGINE — Weekly/Monthly Trigger Protocol

```
WEEKLY TRIGGER (Monday 08:00 or manual):
  1. Collect all event_a logs for ISO week
  2. Compute all event_b fields
  3. Run pattern detection (compare vs previous weeks)
  4. Generate advisory_recommendations (top 3)
  5. Compute CP opportunity (top 3 missed actions)
  6. Write event_b JSON
  7. Generate weekly dashboard template
  8. Append to Weekly Advisory report output

MONTHLY TRIGGER (first session of new month):
  1. Collect all event_b logs for calendar month
  2. Compute Knowledge Graph snapshot (read 02_twin_memory/twin-current/)
  3. Compute SMI monthly delta
  4. Run FRT gap analysis
  5. Compute projected_frt_achievement_months
  6. Write event_c JSON
  7. Generate monthly snapshot badge
  8. Append to Monthly Deep Dive report output
```

## 7.4 Blind Trust Detection — REVIEW-COACH Protocol

```
ON EVERY WF-03/WF-04 COMPLETION:
  1. Read output artifact: count tokens in twin output
  2. Count user edits: compare twin_draft vs user_final (diff)
  3. IF token_count >= 200 AND edit_count == 0:
       flag blind_trust = TRUE
       flag_reason = determine (ZERO_EDITS_LONG_OUTPUT)
       severity = SHORT if tokens < 500
                  LONG if 500 <= tokens < 1000
                  BLOCK if tokens >= 1000
  4. Write to event_a.blind_trust_details[]
  5. Increment event_a.oversight_quality_signals.blind_trust_events
  6. IF severity == BLOCK: emit WARNING to user (inline, not blocking)

EDIT COUNT CALCULATION:
  edit_count = number of distinct text changes between twin_draft and user_final
  Minimum edit to count: ≥ 5 characters changed
  Token count: output tokens from twin (not including user edits)
```

---

# SECTION 8 — SCHEMA REGISTRY & VERSIONING

## 8.1 Schema Version Table

| Schema | Current Version | File | Backward Compatible |
|--------|----------------|------|---------------------|
| Event A | event-a-v1.0 | events/event-a/*.json | N/A (v1) |
| Event B | event-b-v1.0 | events/event-b/*.json | N/A (v1) |
| Event C | event-c-v1.0 | events/event-c/*.json | N/A (v1) |
| XP Ledger | xp-ledger-v1.0 | XP-LEDGER.json | N/A (v1) |
| Level Registry | level-reg-v1.0 | LEVEL-REGISTRY.json | N/A (v1) |
| Privilege Registry | priv-reg-v1.0 | PRIVILEGE-REGISTRY.json | N/A (v1) |

## 8.2 XP-LEDGER.json Schema

```json
{
  "schema_version": "xp-ledger-v1.0",
  "user_id": "string",
  "created_at": "ISO-8601",
  "last_updated": "ISO-8601",

  "totals": {
    "xp_running_total": 0,
    "xp_lifetime_earned": 0,
    "xp_lifetime_penalties": 0,
    "sessions_total": 0
  },

  "current_state": {
    "level": "THE_INTERN | THE_ANALYST | CHIEF_OF_STAFF | THE_TWIN | THE_MASTER",
    "level_numeric": 1,
    "level_unlocked_at": "ISO-8601",
    "next_level_xp_required": 500,
    "xp_to_next_level": 500,
    "pct_to_next_level": 0.0
  },

  "session_history": [
    {
      "session_id": "string",
      "date": "YYYY-MM-DD",
      "xp_earned": 0,
      "xp_penalties": 0,
      "xp_net": 0,
      "running_total_after": 0,
      "breakdown": []
    }
  ],

  "weekly_history": [],
  "monthly_history": []
}
```

## 8.3 LEVEL-REGISTRY.json Schema

```json
{
  "schema_version": "level-reg-v1.0",
  "user_id": "string",
  "current_level": "string",
  "current_level_numeric": 1,

  "level_history": [
    {
      "level": "string",
      "unlocked_at": "ISO-8601",
      "xp_at_unlock": 0,
      "criteria_met": {},
      "demoted_at": null
    }
  ],

  "demotion_warnings": [],
  "next_level_criteria_status": {}
}
```

## 8.4 PRIVILEGE-REGISTRY.json Schema

```json
{
  "schema_version": "priv-reg-v1.0",
  "user_id": "string",
  "last_updated": "ISO-8601",

  "active_privileges": [
    {
      "privilege_id": "PRIV-L1-01",
      "label": "string",
      "unlocked_at": "ISO-8601",
      "level_requirement": 1,
      "status": "ACTIVE | LOCKED | SUSPENDED"
    }
  ],

  "locked_privileges": [],
  "suspended_privileges": []
}
```

---

# SECTION 9 — IMPLEMENTATION CHECKLIST

## Gate Enforcement Rules (Agent Executable)

```
RULE-IMPL-01:
  BEFORE any Executor-Swarm call:
    CHECK privilege_registry: PRIV-L2-02 status == ACTIVE
    IF NOT ACTIVE: return LOCKED message, do not execute

RULE-IMPL-02:
  BEFORE SWARM mode activation:
    CHECK privilege_registry: PRIV-L4-01 status == ACTIVE
    IF NOT ACTIVE: route to COWORK mode, log attempt

RULE-IMPL-03:
  ON every WF-INF-02 (End Session):
    REQUIRE: reflection_pending == false
    REQUIRE: event_a JSON written to storage
    REQUIRE: XP-LEDGER updated
    REQUIRE: Level check completed

RULE-IMPL-04:
  ON blind_trust_events > 0:
    APPEND warning to session dashboard
    DO NOT block session (non-blocking warning)
    LOG to event_a.blind_trust_details

RULE-IMPL-05:
  ON decay engine trigger (daily):
    RUN before any session opens
    IF DORMANT flag: show wake-up message on session open
    APPLY decay to XP-LEDGER (floor at 0)
    LOG to decay/DECAY-LOG.json

RULE-IMPL-06:
  ON level-up detection:
    WRITE level-registry BEFORE updating privileges
    UPDATE privilege-registry
    TRIGGER BM-06 bonus
    DO NOT immediately change co_work_mode (user decides when to activate)
```

---

*Document Classification: Implementation Specification — Internal*
*Review Cycle: Quarterly or on major version change*
*Owner: Nathan Pham — MAS Architecture Practice*
*Next Review: July 2026*
*Implements: Career Twin Workspace v1.0 Autonomy Ramp Architecture*
