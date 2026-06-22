# Clone Reference UI Workflow Reference

## Recommended Artifact Tree

```text
.agent-workflows/
  {slug}/
    source/
      screenshots/
      dom/
      interactive/
      accessibility/
      capture-manifest.json
    brief/
      SOURCE-BRIEF.md
    target/
      screenshots/
      dom/
      interactive/
      accessibility/
      IMPLEMENTATION-NOTES.md
      QA-REPORT.md
    reports/
      {SLUG}-GAP-ANALYSIS.md
```

## State Coverage Checklist

Capture the states that users actually rely on:

- default page loaded
- primary navigation selected state
- top toolbar
- filter panel closed and opened
- each important filter popover opened
- each toolbar/editor icon opened when it exposes a menu, popover, upload chooser, or secondary action list
- upload/media menus with item labels, grouping, disabled states, separators, and source integrations
- main view modes or tabs
- dense data state
- empty state if available
- loading state if available
- error or permission state if visible
- row/card hover, selected, or focused state
- create/edit/detail modal or drawer
- destructive confirmation if part of the workflow

## Source Brief Template

```markdown
# {Page} Source Brief

## Page Purpose

## Source Coverage
| Artifact | Status | Notes |
|---|---|---|

## Layout Inventory
| Area | Source Evidence | Required | Notes |
|---|---|---|---|

## Component Inventory
| Component | Behavior | Data Needed | Priority |
|---|---|---|---|

## Interaction Matrix
| Action | Expected Result | Evidence |
|---|---|---|

## Inferred Data Model
| Entity | Fields | Notes |
|---|---|---|

## Visual Rules To Adapt

## Non-Goals

## Acceptance Criteria
```

## QA Report Template

```markdown
# {Page} QA Report

## Environment
| Item | Value |
|---|---|
| URL | |
| Viewport | |
| Browser | |

## Passed Checks

## Findings
### QA-001: {Visible issue}
Location:
What happens:
Expected:
Screenshot:
Severity:

## Untested Areas
```

## Gap Report Template

```markdown
# {Page} Gap Analysis

## Summary
| Category | Count |
|---|---:|
| Critical | 0 |
| Medium | 0 |
| Minor | 0 |
| Matched | 0 |

## Critical Gaps

## Medium Gaps

## Minor Gaps

## Matched Areas

## Render Path Checks
| Component | Rendered From | Status |
|---|---|---|

## Next Fix Batch
1. 
```

## Agent Prompts

### Source Capture Agent

```text
Use $clone-reference-ui as Source Capture Agent.
Capture the logged-in reference page through Chrome DevTools Protocol.
Write artifacts under .agent-workflows/{slug}/source.
Do not ask for credentials. If login is needed, ask the user to log in manually.
Capture screenshots, DOM text, interactive inventory, accessibility tree, and a manifest.
For composer/editor screens, click every toolbar icon and capture any opened menu or popover, including upload/media source menus with disabled items and separators.
```

### Source Brief Agent

```text
Use $clone-reference-ui as Source Brief Agent.
Read .agent-workflows/{slug}/source and create .agent-workflows/{slug}/brief/SOURCE-BRIEF.md.
Do not write code. Distinguish source evidence from inference.
Include layout inventory, component inventory, interaction matrix, inferred data model, visual rules, non-goals, and acceptance criteria.
```

### Difference Scanner Agent

```text
Use $clone-reference-ui as Difference Scanner Agent.
Run independently from the Code Agent. Do not edit code.
Scan the logged-in source page in strict visual order:
1. Start at the top-left of the visible viewport.
2. Move left-to-right across the current horizontal band.
3. Move down to the next band and repeat.
4. Scroll one viewport slice at a time and continue until the bottom of the page is reached.
5. For nested scroll areas, drawers, composers, previews, menus, and popovers, repeat the same top-to-bottom and left-to-right scan inside that container.
For each region, record visible labels, buttons, icons, active states, disabled states, counters, badges, media thumbnails, menu options, separators, and hover-only affordances when captured.
Then run Interactive Drilldown:
- Click every safe visible function/filter/button/tab/menu/dropdown/toolbar icon/upload source/overflow/toggle/checkbox/radio/profile selector/creative selector/view switch.
- Capture the opened or changed state after each click.
- Record menu groups, option order, enabled/disabled state, selected state, validation messages, layout changes, and preview changes.
- Dismiss popovers/modals and restore state before moving to the next control when possible.
- Do not click destructive, publish/send/schedule/delete/logout/disconnect/billing/account actions unless the user explicitly authorizes them. If a confirmation appears, capture and dismiss it.
For publishing composers, always run a state matrix:
- selected profile/channel combinations by platform
- active per-network platform tab
- creative type: text-only, image, video, link when available
- upload source menu and asset/library menu
- validation panel for each platform and creative type
Compare against target artifacts/code if available.
Write .agent-workflows/{slug}/reports/{SLUG}-DIFFERENCE-SCAN.md with scan coverage, source evidence, target evidence, clicked interaction matrix, platform/channel matrix, creative-type matrix, missing/mismatched areas, uncertainty notes, and feed items for the Code Agent.
Do not stop early. Treat unscanned areas as unknown, not matched.
```

### Code Agent

```text
Use $clone-reference-ui with $build-frontend as Code Agent.
Read SOURCE-BRIEF.md and local project instructions, then implement the target UI using existing project patterns.
If backend data is missing, create an isolated mock adapter.
Write .agent-workflows/{slug}/target/IMPLEMENTATION-NOTES.md and run available validation.
```

### QA Agent

```text
Use $clone-reference-ui with $test-website as QA Agent.
Open the target page in browser, capture target artifacts at the same viewport as source, click all primary controls, and write QA-REPORT.md.
For icon toolbars, click each icon that should open a menu/popover and compare item order, grouping, disabled states, labels, and dismissal behavior.
Do not fix code in this role.
```

### Gap Analysis Agent

```text
Use $clone-reference-ui with $analyze-gap as Gap Analysis Agent.
Compare source artifacts, SOURCE-BRIEF.md, the Difference Scanner report when present, target screenshots, and target code.
Check render paths for orphaned components.
Treat a missing menu/popover from a visible source button as a Critical or Medium gap depending on workflow impact.
Write the gap report with Critical, Medium, Minor, Matched, and Next Fix Batch sections.
```

### Fix Loop Controller

```text
Use $clone-reference-ui as Fix Loop Controller.
Read the latest gap report, choose a small batch of high-impact visible gaps, implement with the Code Agent, QA again, and update the gap report.
Stop when no Critical gaps remain.
```
