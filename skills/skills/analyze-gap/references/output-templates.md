# Output Templates And Severity Rules

Các template này giúp output ngắn, có structure, và không trượt sang essay dài.

## 1. Scope Confirmation

```md
## Scope
- Mode: `catalog-alignment` | `module-deep-compare` | `re-verify-after-fix`
- Spec truth: <Outline root / catalog / owner page / subtree>
- Code target: <route / folder / entry file>
- Boundary: <what is included>
- Out of scope: <what is intentionally not read yet>
```

## 2. Catalog Alignment Matrix

```md
## Catalog Alignment Matrix
| Canonical item | Type | Outline evidence | Code evidence | Status | Notes |
|---|---|---|---|---|---|
| 00 Global UI Patterns & Platform | shared global pattern | module catalog section | app shell / shared component anchor | match / partial / unknown | ... |
| 06 Settings | route group | catalog + settings order | sidebar + route map | ... | ... |
| 06.01 Shop Config | level-2 module | settings order row | `/reward` route + menu label | ... | ... |
```

## 3. Module Surface Inventory

```md
## Module Surface Inventory
| Surface | Class | Spec evidence | Code evidence | Status | Notes |
|---|---|---|---|---|---|
| Creator list | route | owner page overview | `src/pages/Creator/index.jsx` | match | ... |
| Creator drawer | right panel / detail side sheet | child page workflow | `CreatorDrawer.jsx` + click handler | partial | ... |
| Program modal | drawer/modal | spec section "Add new program" | `ProgramModal` lazy import + open state | match | ... |
| Row action menu | row action / bulk action | spec mentions action menu | not yet found | unknown | need deeper code read |
```

## 4. Detailed Diff Matrix

```md
## Detailed Diff Matrix
| Surface | Severity | Spec says | Code has | Status | Recommended fix |
|---|---|---|---|---|---|
| Registration config detail | critical | sidebar + grouped config sections + hidden detail behavior | only flat controls / partial view | stub | rebuild the grouped detail surface |
| Settings level-2 IA | medium | `06.01` to `06.04` explicit decomposition | local menu flattening or naming drift | partial | align catalog, menu label, and owner mapping |
```

## 5. Open Unknowns / Need More Read

```md
## Open Unknowns / Need More Read
| Item | Why unknown | Next read |
|---|---|---|
| Creator row action detail panel | owner page hints it, current subtree read chưa đủ | read companion page for action workflow |
| Shop Config secondary surfaces | code has triggers but render path chưa trace xong | inspect handler + overlay entry |
```

## 6. Fix Backlog

```md
## Fix Backlog
| Priority | Surface | Target | Action |
|---|---|---|---|
| P1 | Settings IA alignment | route map + sidebar labels | align `06` subtree with canonical order |
| P1 | Creator hidden surfaces | creator module entry + overlays | restore missing drawers/modals/right panel flows |
| P2 | Unknown render paths | target module | trace handlers and reclassify orphan vs live |
```

## Severity Rules

### `critical`

Dùng khi:

- thiếu route chính
- thiếu tab chính
- thiếu hidden surface bắt buộc để hoàn thành workflow
- chỉ có shell/stub cho flow chính

### `medium`

Dùng khi:

- có surface nhưng thiếu behavior đáng kể
- settings decomposition lệch
- action cluster / detail panel chưa khớp

### `minor`

Dùng khi:

- naming drift
- menu label drift
- ordering drift
- formatting / presentation mismatch nhỏ

## Status Rules

- `match`: có evidence ở cả spec và code, behavior đủ
- `partial`: đã có surface nhưng chưa đủ behavior/content
- `stub`: surface chỉ là shell hoặc simplified placeholder
- `missing`: spec có, code chưa có counterpart
- `unknown`: chưa đủ evidence, chưa đọc đủ subtree, hoặc chưa trace đủ render path

## Output Length Rule

Nếu scope lớn:

- output theo phase
- mỗi phase chỉ tóm tắt các phát hiện chính
- dồn chi tiết vào matrix
- không viết prose dài để “bù” phần chưa đọc
