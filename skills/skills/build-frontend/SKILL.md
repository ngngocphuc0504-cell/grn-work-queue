---
name: build-frontend
description: >
  Skill for implementing frontend work on internal tools. This is the role-first
  replacement for `internal-tool-code-agent`. It owns code output, output mode,
  implementation rules, and self-review before handoff.
---

# Build Frontend

Use this skill when the task is to implement or modify frontend code for an internal tool.

## Scope

This skill owns:

- choosing the right output mode
- editing frontend code
- keeping implementation aligned with project contracts
- self-review before handoff

Read project context in this order when available:

1. `PROJECT-INSTRUCTIONS.md`, `CLAUDE.md`, `AGENTS.md`, or equivalent
2. `DESIGN.md`
3. `LAYOUT-BLUEPRINT.md`
4. `design-system-antd` when component or page-pattern decisions are needed

If discovery or feature planning is still missing, use `discover-product` first.

## Core rules

- Follow the existing design and layout contract of the project.
- Prefer Ant Design foundations, thin business wrappers, and selective Pro Components.
- Do not invent a new design language when the project already has one.
- Do not change unrelated files unless the task truly requires it.

## No redundant context rule

When app shell, sidebar, header, selected menu, or tabs already communicate page location:

- Do not add in-page breadcrumb text, hierarchy text, or path text again.
- Do not add helper copy like `Settings / X / Y` above the content.
- Do not restate the current tab, selected section, or parent page in body copy.
- For config and admin pages, start directly with tabs, filters, tables, or forms unless missing context would create real ambiguity.

Hierarchy source of truth:

- Use only one hierarchy surface for navigation context.
- Prefer app shell, header, and sidebar as the source of truth.
- Add page-local breadcrumb only if the shell does not already expose that hierarchy.

Less-is-more enforcement:

- If a line can be removed without hurting task completion, remove it.
- Duplicated context is a bug, not harmless extra copy.

## Pro Components adoption rule

- Keep `antd` plus the existing token and theme setup as the base.
- Use `@ant-design/pro-components` only when it clearly reduces implementation cost.
- Do not adopt full `ProLayout` or other shell patterns just because the package exists.
- Prefer `ProTable`, `ProForm`, `ModalForm`, `DrawerForm`, `StepsForm`, `ProDescriptions`, and `PageContainer` for data-heavy admin flows.
- For simple screens, stay with core Ant Design if Pro Components do not meaningfully simplify the work.

## UI language and locale rule

- Default system UI chrome is English unless the project contract says otherwise.
- Configure component-library locale explicitly.
- Configure date-library locale explicitly.
- Use shared formatters for dates, ranges, numbers, and currencies.
- Do not rely on browser or OS locale defaults for system UI.
- User-generated content may remain in the source language.

### Ant Design locale checklist

When a project uses Ant Design or Pro Components:

- Always set `ConfigProvider locale={enUS}` at the app root unless the project explicitly defines another system UI locale.
- Always set the date library locale explicitly, for example `dayjs.locale('en')`.
- Do not assume `ProTable`, `Pagination`, `DatePicker`, or other AntD-based controls will stay in English without an explicit root locale.
- If any system chrome text appears in Chinese or another unexpected language, treat it as a locale configuration bug and fix the root provider first.
- If the user says the UI must be 100% English, enforce that for pagination labels, table chrome, picker chrome, validation chrome, empty states, and all other library-provided UI strings.

## Default internal-web viewport rule

- Primary desktop baseline for internal tools is `1920 x 900` usable viewport.
- Treat this as the normal Full HD working area after subtracting browser chrome.
- Validate dense list, table, filter, and card-grid layouts against `1920 x 900` first.
- Do not optimize primarily for narrow laptop widths unless the project contract says so.
- Use 4K as a secondary regression check only; do not let wider screens silently add columns or drift the intended layout unless the user explicitly asks for that behavior.
- Choose page max width, grid rules, and card sizing so the intended desktop layout still holds at the `1920 x 900` baseline.

## Deploy and config safety rule

This skill may implement UI and app logic, but it must not casually change deploy or build config.

Treat these files as high-risk:

- `.gitlab-ci.yml`, `.github/workflows/**`
- `vite.config.*`, `webpack.config.*`, `next.config.*`, `nuxt.config.*`
- `package.json` build, dev, preview, or deploy scripts
- `.env.production`, `.env.staging`
- `src/config/**`, `config/**`, `public/config/**`
- any file controlling base path, asset prefix, outDir, API host, or deploy target

Only change them when:

- project instructions explicitly allow it
- the user explicitly requests it
- or a verified bug root cause is in that config

Before changing them, explain:

- which file will change
- the old value and new value
- the build or deploy impact

Default Vite safety rules:

- do not change `base` without clear evidence
- do not change `build.outDir` without clear evidence
- do not change API host settings without clear evidence

## Output modes

### Mode A: Claude Artifact

- React 19
- no Ant Design
- single `.jsx` file
- use for very fast prototypes

### Mode B: HTML Preview

- React 19 plus Ant Design CDN
- one `.jsx` file plus one `preview.html`
- use when complex Ant Design components are needed without a full project setup

### Mode C: Vite Multi-file

- React plus Vite plus Ant Design
- use for repo-based or production-oriented work
- follow the repo structure instead of inventing a new one

If the repo already exists as a Vite project, default to Mode C.

## Navigation implementation addendum

Apply these rules when editing app shell, sidebar, route manifest, or settings navigation:

- follow the approved menu hierarchy from discovery or `LAYOUT-BLUEPRINT.md`
- do not flatten grouped navigation for convenience
- keep top-level order aligned with workflow order, not alphabet order, unless the contract says otherwise
- keep admin or config pages under their approved parent such as `Settings`
- keep `Create` or `New` flows out of the sidebar if the contract defines them as CTA-only
- prefer small helper structures for menu contracts over hardcoding everything inside one layout component

## Windows encoding safety rule

When editing source files on Windows:

- never use `Get-Content` plus `Set-Content` to rewrite `.js`, `.jsx`, `.ts`, `.tsx`, `.json`, or `.md` files
- default to `apply_patch` for all manual source edits
- if a full-file rewrite is unavoidable, use explicit UTF-8 read and write APIs instead of shell text pipelines
- after editing any file that may contain non-ASCII text, scan for mojibake markers such as `Â`, `Ã`, `Ä`, `â†`, `ðŸ`, or `�`
- if the terminal displays corrupted text, do not copy that text back into the source file
- if you need to fix JSX structure near Vietnamese or other non-ASCII literals, do not patch against the mojibake shown by PowerShell; first verify the real file text with `python -X utf8` or restore the clean block from git, then patch from that UTF-8 source
- terminal-rendered mojibake is never a trustworthy patch source; treat it as a console problem until UTF-8-aware verification proves the file bytes are actually bad
- do not use shell regex replacement for JSX blocks containing template literals unless there is no safer option

Safe fallback on Windows:

```powershell
$content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
[System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))
```

Regression check after shell-assisted edits:

- reopen the file from disk
- verify the changed lines in source, not just terminal preview
- build or typecheck immediately
- if mojibake appears, stop and restore the affected strings before continuing

## List and admin page implementation addendum

Apply these rules when editing list pages, settings pages, admin tables, or management surfaces:

- reuse the shared toolbar wrapper when the project already has one; do not hardcode a one-off search/filter/action layout per page
- desktop toolbar order should follow `search -> standard filters -> utility controls -> actions`
- search and filter widths should come from shared project presets instead of per-page tuning
- keep the toolbar on one row on desktop whenever feasible; only wrap when the viewport is narrow or the control count truly exceeds the available width
- keep spacing compact across `tabs -> toolbar -> content`; do not create hero-like gaps on management pages
- create CTA wording must follow the contract: one create target uses `Add`, multiple create targets use `Add + noun`
- if a toolbar uses `SmartFilter` as the filter trigger, that trigger must remain the leftmost control of the filter cluster
- do not place a standalone search input in `PageToolbar.search` when the same toolbar already starts with `SmartFilter`; keep that search input inside the `filters` cluster after the `Filter` trigger so the visual order still starts from `Filter`
- when the user cites a reference page for toolbar order, compare the target page against that reference before handoff instead of relying only on the generic contract
- if a page needs a different pattern, that exception must come from the project contract instead of implementation convenience

## Reference clone parity addendum

Apply these rules when implementing a UI from a captured reference product:

- Treat the captured reference as a layout contract for feature placement, hierarchy, and interaction order. Do not move toolbar groups, filter rows, view switches, overflow menus, or primary actions unless the local app shell makes that exact placement impossible.
- "Same design system" means use the local component library and tokens for rendering, not permission to change the reference information architecture. Keep the reference layout and feature affordances intact while replacing raw primitives with local Ant Design components.
- Before marking a cloned view as complete, verify every source view mode separately. For each captured List, Week, Month, board, table, or detail state, check toolbar order, body structure, card density, media/thumbnail region, overflow actions, empty affordances, and scroll behavior.
- If a source card has media, thumbnails, video play affordances, or a post-level `...` menu, the target must render an equivalent safe mock region and an equivalent menu action using local components. A text-only placeholder is a gap unless the source card is text-only.
- If source screenshots show compact and expanded density, implement both visual densities or explicitly record the missing density as a gap. Do not use one generic card for all modes when the source changes card height, media visibility, or action placement.
- Browser QA for cloned UI must include screenshot comparison of the reference and target at the same viewport, plus at least one interaction check for overflow menus and media/detail actions.

## Self-review before handoff

Before finishing, check:

- the feature matches the user request
- layout consistency is preserved
- no unnecessary abstraction was added
- no deploy or config file was changed without explicit justification
- the implementation stays within the design system
- system UI chrome still follows the agreed language contract
- locale-sensitive UI still behaves correctly if the feature touches dates or formatted values, including at least one regression check when component chrome or date formatting is affected
- navigation changes still preserve grouping, ordering, active state, and hidden CTA-only routes, with regression coverage for top-level order and parent-child structure
- no in-page breadcrumb or context text duplicates shell, header, sidebar, or tabs
- no helper copy repeats information already visible in the selected navigation state
- list and admin pages still follow the shared compact toolbar pattern and standardized widths when the project defines that pattern
- representative browser verification covered not just presence of toolbar chrome but also the left-to-right order of critical controls when a toolbar layout changed
- create CTA wording still follows the `Add` / `Add + noun` contract
- shell, toolbar, header, sidebar, or shared spacing changes were verified in a browser on representative pages before handoff

## When to hand off to another skill

- use `design-system-antd` or `design-uiux` for component or UX decisions
- use `discover-product` for planning, discovery, or scope definition
- use `manage-git` for git, branch, commit, push, or MR/PR work
