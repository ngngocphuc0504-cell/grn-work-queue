# USER SETTINGS & CUSTOMIZATION SPECIFICATION
## Career Twin Workspace — ws-settings-v1.0
### Formal Architecture Document
**Status:** DRAFT FOR REVIEW
**Version:** 1.0 | April 2026
**Owner:** Nathan Pham — MAS Architecture Practice

---

## DOCUMENT MAP

```
SECTION 1  — Settings Architecture & Philosophy
SECTION 2  — Settings Schema (JSON)
SECTION 3  — Category Specifications (6 categories, 40+ settings)
SECTION 4  — Agent Behavior Rules (how settings cascade)
SECTION 5  — Settings UI Specification
SECTION 6  — Default Profiles (3 preset configurations)
SECTION 7  — Migration & Versioning Rules
```

---

# SECTION 1 — ARCHITECTURE PHILOSOPHY

## 1.1 Design Principles

```
PRINCIPLE-01: Settings Are Preferences, Not Permissions
  Settings customize HOW the workspace operates, not WHAT it allows.
  Agentic privileges are governed by the Level/XP system exclusively.
  A user cannot disable safety gates or bypass Human-First Rule via settings.

PRINCIPLE-02: Sensible Defaults That Work Out of the Box
  All settings have defaults that represent the recommended configuration.
  A new user who never opens settings still gets a functional workspace.
  Settings exist to refine, not to fix a broken default.

PRINCIPLE-03: Settings Cascade Cleanly Into Agent Behavior
  Every setting maps to at least one specific agent behavior rule.
  No setting is decorative. If it has no behavioral effect, it doesn't exist.

PRINCIPLE-04: Character Identity Is Upstream of Settings
  Character Genesis choices (SOUL.md, Universe, Archetype) are NOT settings.
  They are identity-level configuration and live in SOUL.md, not settings.json.
  Settings customize the operational layer on top of character identity.

PRINCIPLE-05: Privacy Settings Have Architectural Priority
  Privacy settings override all other settings when in conflict.
  If a user disables a logging type, no other setting can re-enable it.
  Privacy = what gets captured. Settings = how it's used.

PRINCIPLE-06: Power Users Can Go Deep, Beginners Stay Simple
  Settings are organized in layers: Quick Settings → Standard → Advanced.
  Advanced settings are hidden behind a toggle. Beginners never see them.
  Every advanced setting has a plain-language explanation of tradeoffs.
```

## 1.2 Settings Storage

```
Storage location: 02_twin_memory/twin-current/{user_id}/settings.json
Backup: 02_twin_memory/twin-current/{user_id}/settings-history/settings-{timestamp}.json
Read by: CTO (all agents via CTO), EVAL-ENGINE, SC-SKILL
Written by: User (via settings interface) only
Change log: settings-history/ (last 10 versions retained)

Load order on session start:
  1. CTO loads settings.json
  2. CTO validates schema (falls back to defaults if corrupt)
  3. CTO injects relevant settings into each agent's context
  4. Settings-driven behavior active for duration of session
```

## 1.3 What Cannot Be Customized

```
IMMUTABLE ELEMENTS (cannot be changed via settings):
  - Human-First Rule (user must state approach before twin responds)
  - Reflection gate (session cannot close without reflection)
  - Level/XP unlock thresholds (governed by gamification engine)
  - Data ownership wall (personal data never crosses to org analytics)
  - SOUL.md content (governed by Character Genesis, not settings)
  - KI distillation 4-gate logic (quality standard is fixed)
  - Agentic privilege gates (governed by Level Registry)

WHY: These are the structural guarantees of the workspace.
     If they can be disabled, the workspace loses its integrity.
     Customization lives on top of these guarantees, not around them.
```

---

# SECTION 2 — SETTINGS SCHEMA

## 2.1 Full settings.json Schema

```json
{
  "schema_version": "settings-v1.0",
  "user_id": "string",
  "created_at": "ISO-8601",
  "last_modified": "ISO-8601",
  "last_modified_by": "USER | SYSTEM",

  "identity": {
    "preferred_name": "string",
    "pronouns": "string | null",
    "preferred_address": "Sir | Ma'am | [name] | [custom]",
    "primary_language": "en | vi | bilingual",
    "secondary_language": "string | null",
    "timezone": "string (IANA)"
  },

  "twin_behavior": {
    "challenge_intensity": "low | medium | high | maximum",
    "verbosity": "concise | standard | detailed",
    "proactivity": "reactive | balanced | proactive",
    "humor_enabled": true,
    "encouragement_enabled": true,
    "devil_advocate_mode": false,
    "assumption_challenge_frequency": "always | sometimes | only_when_critical",
    "self_assessment_prompt_style": "mandatory | gentle | skip_if_busy"
  },

  "co_work_protocol": {
    "human_first_strictness": "strict | moderate",
    "blind_trust_threshold_tokens": 500,
    "blind_trust_warning_style": "inline | end_of_session | weekly_debrief_only",
    "delegation_brief_requirement": "always | for_complex_tasks | optional",
    "reflection_prompt_timing": "immediate | end_of_session",
    "reflection_minimum_sentences": 3,
    "checkin_reminder_enabled": true,
    "checkin_reminder_time": "08:00"
  },

  "rhythm": {
    "session_target_minutes": 60,
    "daily_capture_target": 3,
    "weekly_advisory_day": "monday",
    "weekly_advisory_time": "08:00",
    "inactivity_alert_days": 3,
    "decay_grace_days": 2,
    "monthly_snapshot_day": 1,
    "quarterly_frt_review_reminder": true
  },

  "gamification": {
    "gamification_enabled": true,
    "xp_display": "always | end_of_session_only | hidden",
    "level_notifications": "immediate | end_of_session | weekly_only",
    "streak_display": true,
    "penalty_visibility": "always | summary_only | hidden",
    "dashboard_style": "full | compact | minimal",
    "pairing_name_in_greeting": true
  },

  "captures": {
    "knowledge_capture_enabled": true,
    "networking_capture_enabled": true,
    "learning_capture_enabled": true,
    "morning_checkin_enabled": true,
    "evening_capture_enabled": false,
    "auto_tag_captures": true,
    "capture_min_length_chars": 50
  },

  "notifications": {
    "inactivity_alert_enabled": true,
    "blind_trust_alert_enabled": true,
    "level_up_alert_enabled": true,
    "ki_staleness_alert_enabled": true,
    "pattern_detection_alert_enabled": true,
    "orphan_node_alert_enabled": true,
    "alert_channel": "inline | session_start | weekly_digest",
    "digest_day": "monday",
    "suppress_alerts_during_focus": false
  },

  "privacy": {
    "log_task_content": true,
    "log_reflection_content": true,
    "log_capture_content": true,
    "log_networking_content": false,
    "ki_store_encryption": false,
    "data_retention_days": 365,
    "allow_aggregate_analytics": false,
    "session_log_verbosity": "full | summary | metadata_only"
  },

  "display": {
    "dashboard_language_style": "agency | workshop | academy | lab | field | firm | default",
    "date_format": "DD/MM/YYYY | MM/DD/YYYY | YYYY-MM-DD",
    "time_format": "24h | 12h",
    "metric_format": "absolute | percentage | both",
    "progress_bar_style": "filled | dots | minimal | none",
    "emoji_in_output": false,
    "markdown_rendering": true
  },

  "advanced": {
    "smi_calculation_window_tasks": 10,
    "smi_recency_weight": 1.5,
    "ki_novelty_threshold_pct": 80,
    "ki_distillation_auto": true,
    "background_consolidation_delay_minutes": 30,
    "session_xp_cap": 500,
    "weekly_xp_cap": 2000,
    "drift_detection_enabled": true,
    "drift_variance_threshold_pct": 10,
    "pattern_detection_min_occurrences": 2,
    "auto_frt_gap_map_update": true,
    "debug_mode": false
  }
}
```

---

# SECTION 3 — CATEGORY SPECIFICATIONS

## 3.1 Category 1: Identity

**Purpose:** How the twin addresses and communicates with the user.

| Setting Key | Type | Default | Options | Behavioral Effect |
|-------------|------|---------|---------|-------------------|
| `preferred_name` | string | "" | Any | Used in all direct address |
| `pronouns` | string | null | he/him, she/her, they/them, custom | Embedded in SOUL.md context |
| `preferred_address` | enum | "Sir" | Sir, Ma'am, [name], [custom] | Twin opening address in every response |
| `primary_language` | enum | "en" | en, vi, bilingual | Response language |
| `secondary_language` | string | null | Any | Used when bilingual = true |
| `timezone` | string | auto-detect | IANA tz string | Scheduling, timestamps, decay engine |

## 3.2 Category 2: Twin Behavior

| Setting Key | Type | Default | Options | Behavioral Effect |
|-------------|------|---------|---------|-------------------|
| `challenge_intensity` | enum | "medium" | low, medium, high, maximum | How aggressively TASK-FRAMER and REVIEW-COACH challenge |
| `verbosity` | enum | "standard" | concise, standard, detailed | Response length and elaboration level |
| `proactivity` | enum | "balanced" | reactive, balanced, proactive | Whether twin surfaces things user didn't ask |
| `humor_enabled` | bool | true | true, false | Dry wit / occasional levity in responses |

## 3.3 Category 3: Co-Work Protocol

| Setting Key | Type | Default | Options | Behavioral Effect |
|-------------|------|---------|---------|-------------------|
| `human_first_strictness` | enum | "strict" | strict, moderate | Whether twin responds without user approach |
| `blind_trust_threshold_tokens` | int | 500 | 200–2000 | Token count that triggers BT flag |

## 3.4 Category 4: Rhythm & Cadence

| Setting Key | Type | Default | Options | Behavioral Effect |
|-------------|------|---------|---------|-------------------|
| `session_target_minutes` | int | 60 | 15–240 | Twin references target in session summary |
| `decay_grace_days` | int | 2 | 1–3 | Days before XP decay starts |

## 3.5 Category 5: Gamification

| Setting Key | Type | Default | Options | Behavioral Effect |
|-------------|------|---------|---------|-------------------|
| `gamification_enabled` | bool | true | true, false | Enables/disables full XP system |
| `xp_display` | enum | "end_of_session_only" | always, end_of_session_only, hidden | When XP totals are shown |

## 3.6 Category 6: Privacy

| Setting Key | Type | Default | Options | Behavioral Effect |
|-------------|------|---------|---------|-------------------|
| `log_task_content` | bool | true | true, false | Whether task artifacts are logged to traces |

## 3.7 Advanced Settings

| Setting Key | Type | Default | Range | Description |
|-------------|------|---------|-------|-------------|
| `smi_calculation_window_tasks` | int | 10 | 5–20 | Rolling window for SMI calculation |
| `ki_distillation_auto` | bool | true | true, false | Whether KI distillation runs automatically |

---

# SECTION 4 — AGENT BEHAVIOR RULES (How Settings Map to Prompts)

```
ON SESSION START (WF-INF-01):
  CTO loads settings.json
  CTO constructs SETTINGS_CONTEXT block:

  SETTINGS_CONTEXT = {
    preferred_address: settings.identity.preferred_address,
    primary_language: settings.identity.primary_language,
    challenge_intensity: settings.twin_behavior.challenge_intensity,
    verbosity: settings.twin_behavior.verbosity,
    proactivity: settings.twin_behavior.proactivity,
    gamification_visible: settings.gamification.gamification_enabled
  }
```

---

# SECTION 5 — SETTINGS UI SPECIFICATION

## 5.2 Settings Screen Layout
```
SETTINGS — Career Twin Workspace
─────────────────────────────────────────────
QUICK SETTINGS (visible immediately)
  [ ] Twin challenge level:    [Low] [Medium ✓] [High] [Max]
  [ ] Response style:          [Concise] [Standard ✓] [Detailed]
  [ ] Language:                [EN ✓] [VI] [Bilingual]
  [ ] Address me as:           [Sir ✓] [Ma'am] [Name] [Custom___]
  [ ] Show gamification:       [On ✓] [Off]
```

---

# SECTION 6 — DEFAULT PROFILES

## 6.1 Profile 1: Standard Co-Worker (default for new users)
```yaml
twin_behavior:
  challenge_intensity: medium
  verbosity: standard
co_work_protocol:
  human_first_strictness: strict
gamification:
  gamification_enabled: true
  xp_display: end_of_session_only
```
