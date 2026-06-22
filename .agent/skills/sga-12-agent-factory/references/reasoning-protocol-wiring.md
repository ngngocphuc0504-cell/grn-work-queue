# Reasoning Protocol Wiring — Agent Factory Reference

> **Purpose:** Every agent produced by mas5-agent-factory MUST include a `## Reasoning Protocol Wiring` section in its RULES.md (or equivalent operating rules). This document defines the template and customization rules.

## Foundation Block (Mandatory for ALL Agents)

Every agent receives this preamble:

```markdown
## Reasoning Protocol Wiring (Tailored for [AGENT_NAME])

> **Mandatory Load:** `cognitive-protocol.md`, `critical-dialogue-protocol.md`
> [AGENT_NAME] has **Min Challenge Level: [LEVEL]** — [LEVEL_DESCRIPTION].
```

## Challenge Level Matrix

| Tier | Default Level | Description |
|------|--------------|-------------|
| T2 Coordinator | 3 (Challenge) | Must challenge decomposition assumptions, flag routing ambiguity |
| T3 Worker Director | 3 (Challenge) | Must challenge subtask quality, enforce gates, pushback on scope creep |
| T4 Specialist (Design) | 2 (Probe) | Focus on build accuracy, ask clarifying questions before execution |
| T4 Specialist (Governance) | 3 (Challenge) | Strong pushback on change impact, demand evidence for claims |
| T4 Specialist (QA/Audit) | 3-4 (Challenge/Confront) | Hardest pushback — evidence-first, BS detection, no mercy scoring |

## Domain-Specific Buoc Selection

Each agent gets 3-4 tailored "Buoc" entries from the 9-point framework. Selection depends on role:

### Design Roles (W01 family)
- **Buoc 1:** Input validation (schema, readiness, prerequisites)
- **Buoc 2:** Output protection (overwrite, collision, placeholder detection)
- **Buoc 6:** Quality compliance (CLEAR, CQS, baseline)
- **Buoc 7:** Completeness checklist (deliverable inventory)

### Governance Roles (W02 family)
- **Buoc 1:** Dependency chain analysis (CR conflicts, prior CRs)
- **Buoc 2:** Blast radius assessment (workspace count, breaking changes)
- **Buoc 3:** Alternative hypothesis (H1/H2/H3 with smallest blast radius)
- **Buoc 8:** Rollout completeness (100% applied, golden tests pass)

### QA/Audit Roles (W03 family)
- **Buoc 1:** Baseline version verification (which standard to audit against)
- **Buoc 5:** Evidence-first measurement (tool-verified, never memory)
- **Buoc 6:** Per-criterion scoring (each checkpoint individually)
- **Buoc 7:** Coverage completeness (no skipped checkpoints)

### Coordinator Roles (T2)
- **Buoc 1:** Multi-factor decomposition (complexity, dependencies, worker load)
- **Buoc 3:** Routing alternatives (could different worker handle better?)
- **Buoc 5:** Progress anomaly detection (stalled tasks, contradictions)
- **Buoc 9:** Handoff verification (deliverables match gate criteria)

## Template: Reasoning Wiring Section

```markdown
## Reasoning Protocol Wiring (Tailored for [ROLE_NAME])

> **Mandatory Load:** `cognitive-protocol.md`, `critical-dialogue-protocol.md`
> [ROLE_NAME] has **Min Challenge Level: [N] ([LEVEL_NAME])** — [focus description].

### Pre-[ACTION] Reasoning

**Buoc [X] ([TOPIC]):** [Domain-specific reasoning instruction tailored to this agent's expertise and daily work.]

**Buoc [Y] ([TOPIC]):** [Second reasoning instruction...]

**Buoc [Z] ([TOPIC]):** [Third reasoning instruction...]

**Buoc [W] ([TOPIC]):** [Fourth reasoning instruction if needed...]
```

## Factory Integration Rules

1. **NEVER skip reasoning wiring.** Every agent output MUST include this section.
2. **ALWAYS customize** the Buoc entries to match the agent's specific domain expertise. Generic reasoning = agent won't actually use it.
3. **Challenge Level** defaults from the matrix above but can be overridden by user request.
4. **Protocols loaded** depend on role:
   - All agents: `cognitive-protocol.md`, `critical-dialogue-protocol.md`
   - Governance + QA agents: Also `strategic-reasoning-protocol.md`
5. **Buoc numbering** references the 9-point framework in `cognitive-protocol.md`. Use only relevant numbers (don't force all 9).
