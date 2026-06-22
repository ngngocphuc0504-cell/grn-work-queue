# SMI Calculation Method — Domain Reference

> Reference document for skill `sga-07`.
> Defines the Exponential Moving Average methodology for Skill Maturity Index calculation.

---

## Core Principle

The Skill Maturity Index (SMI) is the quantitative backbone of the autonomy ramp. Raw skill signals from individual sessions are noisy — a single bad day shouldn't crash the score. EMA smooths the signal while giving recent performance more weight than historical.

---

## Formula: Exponential Moving Average (EMA)

```
New_Score = α × Latest_Signal + (1 - α) × Previous_Score
```

Where:
- `α` (smoothing factor) = **0.3** (tuned for weekly session cadence)
- `Latest_Signal` = most recent skill signal from a workflow (1-5 scale)
- `Previous_Score` = existing SMI score for that dimension

### Why α = 0.3?
- α = 0.1 → too slow: takes 10+ sessions to reflect improvement
- α = 0.5 → too reactive: single outlier session distorts score
- α = 0.3 → balanced: meaningful improvement shows in 3-4 sessions while dampening noise

---

## Dimension-by-Dimension Calculation

| Dimension | Signal Sources | Weight |
|-----------|---------------|--------|
| SKH-01 (Work Framing) | WF-01 via SGA-01 | Equal (1/5) |
| SKH-02 (Evidence Reasoning) | WF-03 via SGA-02 | Equal (1/5) |
| SKH-03 (Execution Control) | WF-05 via SGA-04 | Equal (1/5) |
| SKH-04 (Communication) | WF-04 via SGA-02 | Equal (1/5) |
| SKH-05 (AI Co-work) | WF-02 via SGA-03 | Equal (1/5) |

**SMI Average** = Arithmetic Mean of all 5 dimensions

---

## Reliability Threshold

| Signal Count per Dimension | Reliability | Note |
|---------------------------|-------------|------|
| < 3 signals | ⚠️ UNRELIABLE | Display with warning: "Insufficient data" |
| 3-9 signals | 📊 DEVELOPING | Score is indicative but volatile |
| 10+ signals | ✅ STABLE | Score is reliable for mode decisions |

**Rule:** NEVER use an UNRELIABLE score for mode unlock threshold checks.

---

## Mode Unlock Thresholds

| Mode | SMI Average Required | Min Tasks Completed | Additional Criteria |
|------|---------------------|---------------------|---------------------|
| OBSERVE → COWORK | ≥ 2.0 | ≥ 5 | Onboarding complete |
| COWORK → DELEGATED | ≥ 3.0 | ≥ 15 | No dimension below 2.0 |
| DELEGATED → SWARM | ≥ 4.0 | ≥ 30 | No dimension below 3.0, 0 circuit breaker in last 10 sessions |

### Unlock Decision Flow
```
1. Calculate current SMI average
2. Check task count threshold
3. Check dimension floor (no single dim below minimum)
4. IF all pass → RECOMMEND to CTO
5. CTO presents to Human
6. Human approves → Mode change executed
7. Human declines → Log reason, maintain current mode
```

---

## Trend Analysis

| Trend | Definition | Notation |
|-------|-----------|----------|
| Improving | Current > Previous by ≥ 0.2 | ↑ |
| Stable | Delta < 0.2 in either direction | → |
| Declining | Current < Previous by ≥ 0.2 | ↓ |

**Alert Trigger:** Any dimension declining for 3+ consecutive sessions → CTO notification.

---

## Anti-Patterns

- **AP-01 (Score Inflation):** Assigning high signals without evidence → breaks mode integrity
- **AP-02 (Stale Score):** Not recalculating after new signals → user sees outdated SMI
- **AP-03 (Auto-Unlock):** System unlocks mode without human approval → governance violation
- **AP-04 (Single-Dimension Focus):** Only updating 1 dimension repeatedly while others stagnate
