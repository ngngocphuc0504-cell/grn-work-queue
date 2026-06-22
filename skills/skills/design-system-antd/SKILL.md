---
name: design-system-antd
description: >
  Source of truth cho design language Ant Design 6 và template `DESIGN.md`. Đây là tên mới theo vai trò
  của skill cũ `antd-saas-patterns`. Skill này sở hữu token, component rules, state matrix,
  và guardrails cross-project cho internal tools.
---

# Design System AntD
## AntD foundation with selective Pro Components

---

## PHẠM VI

Skill này là **design contract + pattern library** cho internal tool dùng **Ant Design 6** làm foundation, với **selective Pro Components adoption** cho data-heavy enterprise flows.

Mục tiêu:
- Cho agent một **nguồn sự thật duy nhất** để đọc trước khi đề xuất UI/code
- Giữ **một ngôn ngữ thiết kế chung** giữa nhiều project nội bộ
- Cho phép project-specific override có kiểm soát mà **không drift khỏi AntD**

Skill này **không viết code trực tiếp**. Khi cần code:
- chuyển sang **build-frontend**
- khi cần decision UI/UX cụ thể: chuyển sang **design-uiux**

---

## NGUYÊN TẮC NỀN TẢNG

### 1. AntD foundation with selective Pro Components
- Ant Design 6 là **design language chuẩn**
- `@ant-design/pro-components` được phép dùng khi giúp giảm custom wrapper entropy ở table, form, detail, và admin-heavy flows
- Không duy trì `BaseUI` như một hệ UI song song
- Shared wrapper hợp lệ chỉ là **business composition mỏng** như `PageContainer`, `FilterBar`, `QuickFilterPills`, `EntityStatusTag`
- Wrapper **phải compose AntD**, không tự định nghĩa visual language trái token/state của AntD
- Không thay toàn bộ app shell sang Pro layout mặc định nếu project chưa chốt layout contract đó

### 2. Hai lớp rõ ràng

#### Foundation cố định giữa mọi project
- Typography scale
- Spacing rhythm
- Interaction hierarchy
- Status colors
- Table / filter / form / overlay patterns
- Icon style
- Empty / loading / error / confirmation / notification states

#### Project override có kiểm soát
- Brand accent
- Platform colors
- Chart palette
- Module-specific cards
- Sidebar IA, route labels, business wording

### 2.1 UI language and locale contract
- Default internal-tool contract: **system UI chrome is English-only**
- "System UI chrome" includes navigation, headers, buttons, empty states, validation text, helper text, tooltips, badges, system notifications, table chrome, form chrome, and date labels
- User-generated or imported business content may keep the source language
- Do not inherit browser, OS, or runtime locale for system UI formatting
- Dates, times, numbers, and currencies shown in system UI must use an explicit locale and centralized formatter
- If a project needs non-English system UI, that override must be written explicitly in `DESIGN.md`

### 2.2 Default desktop baseline for internal web
- Standard baseline is `1920 x 900` usable viewport.
- Treat this as the real Full HD working area after browser chrome, not the raw monitor size.
- Solve information density, card grids, tables, and filter bars for `1920 x 900` first.
- Do not let wide screens silently add more card columns or change hierarchy unless the product explicitly wants that behavior.
- 4K and larger screens should preserve the same core layout with controlled whitespace or max-width, not accidental layout drift.

### 3. Một pipeline chuẩn cho agent
1. Đọc `DESIGN.md` của project nếu có
2. Nếu chưa có `DESIGN.md` → dùng template tại `templates/DESIGN.md`
3. Đọc `LAYOUT-BLUEPRINT.md` nếu project có
4. Chọn pattern + component AntD
5. Mới đề xuất UI hoặc code

---

## ANT DESIGN LANGUAGE

Skill này encode 4 design values của Ant Design thành rule cho internal tool:

| Design value | Dịch sang internal tool |
|---|---|
| **Natural** | Giảm cognitive load, scan nhanh, dùng cấu trúc quen thuộc |
| **Certain** | Consistency cao giữa project, ít entropy, ít phải học lại |
| **Meaningful** | Action rõ mục tiêu, feedback tức thì, không thêm UI thừa |
| **Growing** | Mở rộng module được mà không vỡ pattern, token và layout |

Chi tiết cách áp dụng → xem [references/design-principles.md](references/design-principles.md)

### Less is more là bộ lọc bắt buộc
- Một màn hình chỉ nên có một primary CTA thật sự nổi bật.
- Không lặp lại trạng thái bằng cả badge, helper text, subtitle, và summary nếu một dấu hiệu đã đủ.
- Ưu tiên table, form, tabs, modal AntD chuẩn trước khi nghĩ tới card stack hoặc wrapper mới.
- Filter nâng cao, metadata phụ, và settings hiếm dùng phải được ẩn có chủ đích.
- Mọi override theo project phải làm giao diện rõ hơn, không làm entropy cao hơn.

### Filter bar consistency is mandatory
- Any table-level filter bar with active search or active filters must expose a clear reset action such as `Clear all`.
- `Clear all` must appear only when there is something to reset, and it must clear every table-toolbar control in that bar.
- Multi-select filter bars in the same product should keep the same reset behavior, placement, and visibility rule across pages.
- Do not let one list page rely on chip-level clear only while sibling list pages expose a toolbar-level reset action.

### Default list page toolbar pattern
- Default admin, list, and settings pages should use a compact inline toolbar instead of a tall, airy hero-style filter bar.
- Desktop toolbar order should optimize left-to-right scanning: `search -> standard filters -> utility controls -> action buttons`.
- Search and standard filter widths should be standardized in a shared wrapper instead of chosen independently per page.
- On desktop, keep the toolbar on one row whenever feasible. Wrap only when the viewport is narrow or the control count truly exceeds the available width.
- Keep the action cluster right-aligned. If there is one create target, use `Add`; if there are multiple create targets, use `Add + noun`.
- Keep the vertical rhythm compact: tabs close to toolbar, toolbar close to table or list content, and no oversized gaps between chrome layers.
- Summary lines like `x total / y active / z paused` are not the default. Remove them when tabs, badges, table state, or body content already provide enough context.
- If a page needs a different pattern, the exception must be documented in `DESIGN.md` or `LAYOUT-BLUEPRINT.md` instead of being invented ad hoc.

---

## DESIGN CONTRACT MỚI

### Artifact bắt buộc
- Template chuẩn: [templates/DESIGN.md](templates/DESIGN.md)

### Nếu project có `DESIGN.md`
- Ưu tiên file đó làm source of truth cho visual/system language
- Chỉ dùng skill này để fill phần còn thiếu hoặc verify consistency

### Nếu project chưa có `DESIGN.md`
- Dùng template mặc định của skill này
- Sau đó project có thể override trong phạm vi cho phép

---

## REFERENCE MAP

### A. Foundation
- Colors → [references/colors.md](references/colors.md)
- Typography → [references/typography.md](references/typography.md)
- Layout & Spacing → [references/layout-spacing.md](references/layout-spacing.md)
- Icons → [references/icons.md](references/icons.md)
- Shadow → [references/shadow.md](references/shadow.md)
- Design Principles → [references/design-principles.md](references/design-principles.md)

### B. Patterns
- Page Patterns → [references/page-patterns.md](references/page-patterns.md)
- Navigation → [references/navigation.md](references/navigation.md)
- Button Usage → [references/buttons.md](references/buttons.md)
- UX Standards → [references/ux-standards.md](references/ux-standards.md)
- Motion → [references/motion.md](references/motion.md)
- Visualization → [references/visualization.md](references/visualization.md)

### C. Guardrails
- Token override matrix → [references/token-override-matrix.md](references/token-override-matrix.md)
- Component state matrix → [references/component-state-matrix.md](references/component-state-matrix.md)
- Do / Don't → [references/do-dont.md](references/do-dont.md)
- Copywriting → [references/copywriting.md](references/copywriting.md)
- Data format → [references/data-format.md](references/data-format.md)

### D. Legacy migration
- Component Mapping → [references/component-mapping.md](references/component-mapping.md)

---

## TECH STACK CHUẨN

```txt
antd@^6.0.0
@ant-design/icons@^6.0.0
@ant-design/pro-components (optional, stable or beta when migration requires it)
dayjs@^1.11.0
react@^19
vite@^6
recharts@^2.15
```

### Quy tắc stack
- Dùng **Ant Design 6** làm foundation mặc định
- Cho phép `@ant-design/pro-components` theo hướng selective adoption, kể cả beta line khi migration cần
- Không coi Pro Components là mặc định cho mọi page hoặc mọi component type
- Ưu tiên Pro Components ở data-heavy/admin/detail/form flows khi giúp bỏ custom scaffolding không cần thiết
- Nếu cần business wrapper, wrapper phải giữ nguyên token/state behavior của AntD

---

## COMPONENT SELECTION GUIDE

### Data display

| Tình huống | Component |
|---|---|
| Bảng có search + filter + sort + pagination | `Table` + `Form` filter bar |
| Bảng đơn giản < 5 cột | `Table` |
| Danh sách card | `List` + `Card` |
| Chi tiết 1 record | `Descriptions` |
| KPI cards | `Statistic` + `Card` |

### Forms

| Tình huống | Component |
|---|---|
| Form tạo/sửa trong popup | `Modal` + `Form` |
| Form tạo/sửa bên cạnh | `Drawer` + `Form` |
| Form nhiều bước | `Steps` + `Form` |
| Filter bar trên đầu table | `Form` inline hoặc `Row`/`Col` |
| Form đơn giản | `Form` |
| Form phức tạp | `Form` + `Tabs` hoặc `Collapse` |

### Inputs

| Tình huống | Component |
|---|---|
| Free text | `Input` |
| Multi-line text | `Input.TextArea` |
| Numeric | `InputNumber` |
| Date | `DatePicker` |
| Date range | `DatePicker.RangePicker` |
| Fixed list nhỏ | `Select` |
| List lớn / async | `Select showSearch` |
| Multi-select | `Select mode="multiple"` |
| Free-form tags | `Select mode="tags"` |
| Boolean | `Switch` |
| Single choice | `Radio.Group` |
| Multiple choice | `Checkbox.Group` |

### Table status controls

- For binary on/off states inside table cells, default to `Switch`.
- Do not replace a binary status toggle with a `Button` or inline `Select` editor unless there is a documented product reason.
- Use inline `Select` only when the cell represents 3 or more valid states, or when the status change needs explicit state labels in the same interaction.
- For binary status columns, the switch itself is the primary control. Extra text beside the switch should be omitted unless the page has a proven scanability problem.

### Layout & feedback

| Tình huống | Component |
|---|---|
| Main shell | `Layout` + `Sider` + `Header` + `Content` |
| Tabs trong trang | `Tabs` |
| Confirm hành động nguy hiểm | `Popconfirm` |
| Toast ngắn | `message` |
| Notification cần action | `notification` |
| Empty | `Empty` |
| Loading | `Spin` hoặc `Skeleton` |
| Error page | `Result` hoặc `Alert` |

---

## OUTPUT CONTRACT CHO AGENT

Khi dùng skill này để trả lời thiết kế hoặc code direction:
- Luôn nói rõ **page type**
- Luôn nói rõ **AntD component** nào sẽ dùng
- Nếu dùng Pro Components, phải nói rõ **vì sao dùng Pro thay vì core AntD hoặc thin wrapper**
- Luôn nói rõ **token / pattern** nào chi phối
- Nếu project dùng shared wrapper, phải mô tả wrapper đó là **thin business wrapper on top of AntD**
- Không được đề xuất `InputField`, `SelectField`, `SearchableSelect`, `BaseUI` như default foundation

---

## QUICK CHECKLIST

Trước khi chốt một solution, verify:
- Có đọc `DESIGN.md` chưa?
- Có đọc `LAYOUT-BLUEPRINT.md` chưa, nếu project có?
- Có đang dùng token thay vì hardcode không?
- Có tối đa 1 primary action mỗi nhóm không?
- Có empty/loading/error/confirmation state chưa?
- Có đang phát minh component riêng dù AntD đã có không?
- Có override vượt quá phạm vi cho phép trong token matrix không?

---

## TÓM TẮT NHANH

- AntD 6 foundation + selective Pro Components
- `DESIGN.md` là visual/system contract
- `LAYOUT-BLUEPRINT.md` là structural/layout contract
- Business wrappers được phép, nhưng chỉ là thin composition layer
- Cho phép Pro Components có chọn lọc, không dùng làm mặc định
- Không duy trì BaseUI như hệ UI song song
