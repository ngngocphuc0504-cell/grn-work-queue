---
name: fco-delivery-agent
description: Use for FCO Web Events & VIP System delivery: read project specs, plan execution tasks, perform manual/automatic QA testing, and sync project data without drifting from the single source of truth.
---

# FCO Delivery Agent

## Purpose

Use this skill for full-lifecycle delivery work in `Garena FCO Web Events & VIP System`:

- bootstrap context from the live project specs and briefs
- turn specs or workstreams into an execution plan
- implement logic, HTML/CSS/JS code, or test scripts
- run verification, browser QA, and Excel checklist testing
- sync the project specs and work queues after meaningful changes

Default workspace:

- `c:\Users\VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin`

## Required Read Order

Read only what is needed, in this order:

1. Project Specs -> [member-web-system-comprehensive-spec.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/member-web-system-comprehensive-spec.md)
2. Project Brief -> [project-brief.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/project-brief.md)
3. QA Playbook -> [qa-testing-playbook.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/qa-testing-playbook.md)
4. Active work queue -> [garena-tasks.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/Garena/work%20queue/garena-tasks.md)
5. Recent meeting minutes -> [18_06_2026_Supervisor_SyncUp_Notes.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/Garena/meeting%20notes/18_06_2026_Supervisor_SyncUp_Notes.md)

## Hard Project Truths

- Live stack is `Vanilla HTML + Vanilla CSS + Javascript` for event landing pages, or `Ant Design + React` for internal portals.
- Default QA method is manual validation + `VIP_Revamp_QA_Checklist.xlsx` sheet tracking.
- Security boundary: Never expose absolute top-up/recharge values on the UI or in public API payloads (convert to points).
- Dual-Track balance: Treat PAY and PLAY tracks with equal weight on visual layouts.
- Decent Bronze rule: The visual of basic tier buildings must look polished and appealing.

## Default Delivery Pipeline

### 1. Resolve source of truth first

Before doing work, state:
- task intent
- owner spec or mockup
- code/asset area likely impacted
- fact vs assumption

Do not plan or code before the route is explicit.

### 2. Plan in small executable slices

Convert the task into a small phase/task plan with:
- exact goal
- files/modules affected
- test cases to run
- blockers or dependencies

### 3. Implement in the correct layer
- Put gameplay/monetization logic in the backend APIs.
- Put interactive building claim states in the UI frontend with proper glow/particle selectors.
- Do not duplicate event rules across engine and UI.

### 4. Verify before claiming success
Use browser tools and test scripts to verify:
- UI layout alignment (e.g. VVIP tower bottom-right)
- API fields mapping (topup, login days, playtime)
- Correct gacha discount multipliers (0.3 for 6-8, 0.4 for 7-8, 0.6 for +8)

### 5. Sync the right docs
After meaningful delivery:
- Update [member-web-system-comprehensive-spec.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/member-web-system-comprehensive-spec.md)
- Update [garena-tasks.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/Garena/work%20queue/garena-tasks.md)
- Log milestones in `.agent/memory_bus/ledger.md`

## Output Contract

- Use Vietnamese by default.
- Keep explanations operator-friendly and concrete.
- Separate `Fact` from `Assumption` whenever there is uncertainty.
- Surface blockers and tradeoffs early.

## Stop Conditions

Stop and ask before proceeding if:
- the task conflicts with the SSoT spec or design layout
- the task exposes real payment recharge money on UI
- API payloads are found to leak absolute billing currency values
