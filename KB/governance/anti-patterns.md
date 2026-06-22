# Anti-Patterns — Career Twin Workspace v1

## 7 Conflicts Resolved + Enforcement Rules

### AP-01: Twin Identity Collapse
**Pattern:** Attempting to merge CPT + CST + FRT into one persona  
**Risk:** Twin contradicts itself; user loses trust in session 1  
**Rule:** 3 twins ALWAYS operate as separate consultation layers. SOUL.md files NEVER merged.  
**Enforcement:** CTO routes queries to specific twin layer, never composite  

### AP-02: Autopilot Bypass
**Pattern:** User submits task without approach, asks twin to do it all  
**Risk:** User learns nothing; skill signals corrupted  
**Rule:** Human First — twin REJECTS any task submission without user's stated approach  
**Enforcement:** TASK-FRAMER checks for `user_approach` field; returns to user if missing  

### AP-03: Mode-Skip (jumping to SWARM before readiness)
**Pattern:** New user in Week 1 requesting full Executor-Swarm delegation  
**Risk:** Overwhelming complexity; user abandons; no skill signal generated  
**Rule:** Mode gates locked by skill maturity thresholds  
**Enforcement:** CTO checks `co_work_mode` against `skill_maturity_index` before routing  

### AP-04: Reflection Skip
**Pattern:** User closes session without submitting reflection  
**Risk:** No skill signal generated; KI store stagnates; twin cannot learn  
**Rule:** Session CANNOT close without reflection. REFLECTION-HARVESTER blocks WF-INF-02  
**Enforcement:** WF-INF-02 (End Session) has hard dependency on reflection_pending = false  

### AP-05: Performance Data Misuse
**Pattern:** Operator or manager attempts to use SKILL-MATRIX data for HR evaluation  
**Risk:** EU AI Act violation; user trust destroyed; legal liability  
**Rule:** Layer A data has ZERO read access for any entity except the user  
**Enforcement:** Data ownership policy enforced at architecture level (separate namespaces)  

### AP-06: Stale Twin
**Pattern:** CST not updated for >30 days; FRT never reviewed  
**Risk:** Gap Map becomes inaccurate; twin gives irrelevant challenges  
**Rule:** CST update triggered automatically after every task. FRT quarterly review mandatory.  
**Enforcement:** SKILL-TRACKER flags if last_updated > 30 days → prompts quarterly review  

### AP-07: Generic Twin (Personalization Failure)
**Pattern:** Onboarding intake skipped; twin uses only CPT defaults  
**Risk:** Twin challenges are irrelevant to user's actual context  
**Rule:** CST initialization is MANDATORY before first task. ONBOARDING cannot be skipped.  
**Enforcement:** CTO checks onboarding_complete flag; routes to ONBOARDING.md if false  
