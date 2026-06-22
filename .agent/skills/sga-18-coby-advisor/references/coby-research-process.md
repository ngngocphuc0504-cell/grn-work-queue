# Coby Nguyen's Research & Hypothesis Validation Playbook
> **Version:** 1.0  
> **Status:** ACTIVE — Integrated into sga-18-coby-advisor  
> **Source:** Extracted from Onboarding Process Digitization Interview | 2026-04-17

---

## 1. Overview

This playbook defines Mr. Coby Nguyen's structured approach to research, market analysis, brainstorming, and hypothesis validation. It is designed to move systematically from vague business questions to high-fidelity, evidence-backed strategic recommendations.

---

## 2. The 3-Step Research Operating Procedure (SOP)

### Step 1: Requirements Decomposition (AI-Assisted)
**Input:** Raw requirements, vague business questions, or untested hypotheses.
**Action:**
- Breakdown the high-level request into MECE (Mutually Exclusive, Collectively Exhaustive) sub-components.
- Map out specific, searchable topics or questions for each component.
- Validate the decomposition with the user before gathering data.

*System Check:* Trigger `TASK-FRAMER` validation to ensure the decomposition is structurally sound before moving to Step 2.

---

### Step 2: Evidence Gathering & Hypothesis Validation (Human-Led / Ground Truth)
**Input:** The decomposed sub-components from Step 1.
**Action (Iterative):**
- Gather empirical, verifiable data for each component.
- Apply the **3-Source Minimum Rule** to ensure grounding and prevent bias:
  1.  **Primary Source (1):** Direct client data, operational baselines, or raw industry reports.
  2.  **Secondary Source (1):** Expert analyses, reputable B2B articles, or market literature.
  3.  **Counter-Evidence (1):** Actively search for data or arguments that *disprove* the initial hypothesis to challenge confirmation bias.
- Classify missing or weak data explicitly as `⏳ Pending` or `⚠️ TBD` (per P-02).

---

### Step 3: Synthesis & Iteration Loop (AI + Human Review)
**Input:** Gathered evidence and verified data from Step 2.
**Action:**
- Synthesize findings into structured, actionable business recommendations.
- Present explicit **MVP vs. Full Option** trade-offs when presenting strategic paths (per P-06).
- Conclude with a singular, pushing strategic question to drive the next operational step.

---

## 3. Heuristics for "Done"

A research or validation task is considered completed when it satisfies the following criteria:
1.  **Bidirectional Grounding (P-05):** The strategic conclusions are mathematically anchored to a numeric run-rate or baseline metric.
2.  **Evidence Checklist Passed:** All major assertions are supported by the 3-Source Minimum, or gaps are transparently flagged as uncertain.
3.  **MECE Structure (P-08):** The final report structure has no overlapping topics and covers the entire scope of inquiry.
