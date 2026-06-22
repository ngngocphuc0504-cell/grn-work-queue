# Ant Design 6 Foundation for Internal Tools

## 1. Visual Theme & Atmosphere

This project uses **Ant Design 6 as the primary design language** for enterprise/internal workflows, with **selective Pro Components adoption** allowed where it reduces enterprise UI scaffolding.

The interface should feel:
- **Natural**: low cognitive load, quick to scan, familiar UI grammar
- **Certain**: consistent across modules and projects, low entropy, predictable behavior
- **Meaningful**: every action has a clear outcome and immediate feedback
- **Growing**: the system can expand across pages, modules, and products without breaking patterns

Design tone:
- clean, dense, operational
- action-first, not decorative-first
- restrained color usage
- strong visual consistency across tables, filters, forms, tabs, cards, modals, and drawers

For internal tools, prioritize:
- readability
- scanability
- consistency
- operational confidence

Do not create a parallel custom design system if Ant Design or Pro Components already solve the problem well.
Do not adopt Pro Components as a blanket replacement for all simple screens.

---

## 2. UI Language & Locale Contract

- System UI chrome language: English-only unless explicitly overridden by product requirements
- Allowed content languages: content may preserve the source language when it is user-generated, imported, or business-facing
- Date/time locale: explicit English locale for all system UI formatting
- Number/currency locale: explicit project-level formatter, never browser-default
- Locale safety: do not inherit browser or OS locale for component chrome, calendar labels, or date strings

---

## 3. Color Palette & Roles

### Core Brand / Action
- `colorPrimary`: `#1677ff`
- `colorPrimaryHover`: `#4096ff`
- `colorPrimaryActive`: `#0958d9`
- `colorPrimaryBg`: `#e6f4ff`

### Semantic
- `colorSuccess`: `#52c41a`
- `colorWarning`: `#faad14`
- `colorError`: `#ff4d4f`
- `colorInfo`: `#1677ff`

### Text
- `colorText`: `rgba(0,0,0,0.88)`
- `colorTextSecondary`: `rgba(0,0,0,0.65)`
- `colorTextTertiary`: `rgba(0,0,0,0.45)`
- `colorTextQuaternary`: `rgba(0,0,0,0.25)`

### Surface / Border
- `colorBgLayout`: `#f5f5f5`
- `colorBgContainer`: `#ffffff`
- `colorBgElevated`: `#ffffff`
- `colorBorder`: `#d9d9d9`
- `colorBorderSecondary`: `#f0f0f0`
- `colorSplit`: `rgba(5,5,5,0.06)`

### Override policy
- Project may override `colorPrimary`
- Project may add domain-specific palette such as platform colors or chart colors
- Project should not redefine semantic colors in a way that breaks user intuition

---

## 4. Typography Rules

### Font family
- Primary: system/Ant Design stack

### Scale
| Role | Size | Weight | Use |
|---|---|---|---|
| Page title | 20px | 500 | top-level page heading |
| Section / card title | 16px | 500 | cards, sections, panels |
| Body / table cell | 14px | 400 | default reading size |
| Caption / hint | 12px | 400 | metadata, helper text |

### Typography rules
- Prefer 12 / 14 / 16 / 20 as the main scale for internal tools
- Avoid oversized marketing-style headings
- Use heavier weight sparingly
- Use text hierarchy to reduce visual noise, not increase it
- Placeholder text must never replace labels

---

## 5. Component Stylings

### Buttons
- Use Ant Design button hierarchy
- Maximum one primary action per action group
- Use concrete labels such as `Lưu`, `Tạo mới`, `Xoá`, `Duyệt`
- Avoid vague labels such as `OK`, `Submit`, `Action`

### Inputs
- Use `Form.Item` + AntD inputs for validation and state
- Fixed list small: `Select`
- Large/async list: `Select` with search
- Multi-line input: `Input.TextArea`

### Table
- Standard enterprise table with:
  - loading
  - empty state
  - pagination
  - sort/filter where needed
  - ellipsis for long text
- Filters sit above the table in an inline filter bar
- `ProTable` is allowed for data-heavy pages when it reduces custom filter/table scaffolding and still matches the project token contract

### Cards
- Use cards as section wrappers, not as decorative chrome
- Keep padding and spacing stable across same card types

### Tabs
- Use one consistent tab style per context
- Typical range: 3–7 tabs

### Modal / Drawer
- Header and footer stay visible
- Only body scrolls
- Use for contextual tasks that should stay on the same page
- `ModalForm`, `DrawerForm`, and `StepsForm` are allowed when they simplify enterprise form flows without changing the agreed layout language

### Status
- Use `Tag`, `Badge`, `Alert`, `Result`, `message`, `notification` according to semantic meaning

---

## 6. Layout Principles

### Shell
- Desktop-first
- Typical app shell: sidebar + header + content
- Sidebar is the main navigation pattern for internal tools

### Spacing rhythm
- 8px: micro spacing
- 16px: default spacing in a group
- 24px: spacing between sections

### Grid
- Ant Design 24-column grid
- Common gutters: 8 / 16 / 24

### Page patterns
- List page: filter bar + table
- Detail page: summary info + tabs + related content
- Form/config page: grouped forms with tabs/collapse if needed
- Dashboard: KPI + charts + recent data
- Moderation/review page: clear decision areas, low-risk actions

### Layout rule
- `DESIGN.md` defines visual/system language
- `LAYOUT-BLUEPRINT.md` defines project shell, page structure, and layout specifics

---

## 7. Depth & Elevation

- Use AntD-style restrained elevation
- Cards and overlays should feel enterprise, not cinematic
- Borders are often enough; shadows should stay light

### Suggested hierarchy
| Level | Use |
|---|---|
| Flat | base page background |
| Light border / low elevation | cards, sections, table wrappers |
| Elevated | dropdowns, popovers |
| High elevation | modals, drawers |

---

## 8. Do / Don't

### Do
- read project `DESIGN.md` first
- use AntD core components first
- use Pro Components selectively when they simplify enterprise-heavy flows
- keep repeated page types visually consistent
- use tokens instead of hardcoded values
- keep system UI chrome in English unless the design contract explicitly says otherwise
- keep action hierarchy clear
- include empty/loading/error/confirmation states
- allow thin business wrappers only when they compose AntD

### Don't
- do not maintain BaseUI as a parallel foundation
- do not invent a custom visual language for simple components
- do not replace simple pages with Pro Components without a clear complexity win
- do not hardcode colors or spacing outside controlled overrides
- do not let browser or OS locale decide system UI date strings or component locale
- do not hide primary actions behind menus
- do not add helper text unless it materially reduces ambiguity
- do not override semantic colors for aesthetics only

---

## 9. Responsive Behavior

- Desktop-first, but still responsive
- Filter bars must wrap instead of overflowing horizontally
- Cards and grids collapse using AntD breakpoints
- On smaller screens, hide low-priority columns before breaking readability
- Overlay widths should adapt, but keep internal structure stable

### Priority on narrow screens
1. preserve core actions
2. preserve key identifiers
3. collapse secondary metadata
4. avoid horizontal scroll unless the content is truly tabular and high-density

---

## 10. Agent Prompt Guide

### When this file exists
- Read this file before proposing UI or code
- Then read `LAYOUT-BLUEPRINT.md` if the project has one
- Choose AntD components and patterns that match this contract

### Quick rules for agents
- AntD-first
- business wrappers only if thin and compositional
- one primary action per group
- use filter bar + table for list pages
- use modal/drawer for short contextual editing
- use tags/badges/messages/notifications according to semantic meaning
- keep pages dense but calm

### Example prompts
- "Build a list page using Ant Design 6 with an inline filter bar above a paginated table. Keep spacing at 16/24, use one primary CTA in the top-right, and include empty/loading/error states."
- "Design a detail page with a summary header, `Descriptions`, and line-style tabs for related entities. Keep typography restrained and operational."
- "Create a config form using grouped AntD `Form.Item` sections, with tabs only if the form is too long. Validation must be declarative and feedback immediate."
