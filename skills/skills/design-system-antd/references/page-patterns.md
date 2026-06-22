# Page Patterns - Ant Design 6 + Selective Pro Components

Use Ant Design 6 as the default page foundation. Pro Components are allowed selectively when they remove obvious enterprise scaffolding around tables, forms, descriptions, or admin-heavy pages.

## Decision rule

- Prefer core AntD for simple pages, lightweight CRUD, and surfaces that already read clearly with `Table`, `Form`, `Descriptions`, `Modal`, or `Drawer`.
- Prefer Pro Components when the page is data-heavy and the team would otherwise rebuild boilerplate for search forms, table state, detail layouts, or multi-step forms.
- Do not adopt Pro Components as a blanket replacement for every page.

## Pattern 1: List page

Use:
- Core AntD: `Card` + inline `Form` + `Table`
- Pro option: `PageContainer` + `ProTable`

Choose `ProTable` when the page needs many of these together:
- search form
- reset/submit behavior
- column settings
- toolbar actions
- server-side table state

Stay with core AntD when the table is simple and custom state is already small and readable.

## Pattern 2: Detail page

Use:
- Core AntD: `Card` + `Descriptions` + `Tabs`
- Pro option: `PageContainer` + `ProDescriptions`

Choose `ProDescriptions` when the detail surface is operational, field-heavy, and repeated across admin pages.

## Pattern 3: Short form page

Use:
- Core AntD: `Modal` + `Form` or `Drawer` + `Form`
- Pro option: `ModalForm` or `DrawerForm`

Choose Pro form wrappers when they remove repetitive submit/cancel/loading wiring without changing the agreed layout language.

## Pattern 4: Multi-step form

Use:
- Core AntD: `Steps` + `Form`
- Pro option: `StepsForm`

Choose `StepsForm` when the wizard is clearly form-driven and the team would otherwise hand-roll step persistence and validation orchestration.

## Pattern 5: Dashboard or monitoring page

Use:
- Core AntD: `Row`, `Col`, `Card`, `Statistic`, charts, tables
- Optional `PageContainer` only if the page benefits from a standard enterprise header shell

Do not force Pro Components into KPI or chart sections that are already clean with core AntD.

## Pattern 6: Admin and settings surfaces

Default recommendation:
- `PageContainer`
- `ProTable` for list-heavy admin pages
- `ProDescriptions` for record details
- `ModalForm` or `DrawerForm` for create/edit flows

Guardrails:
- preserve project tokens and `ConfigProvider` theme
- do not auto-adopt `ProLayout` unless the project explicitly chooses that shell
- keep custom business wrappers thin
