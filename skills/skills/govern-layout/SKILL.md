---
name: govern-layout
description: >
  Skill sở hữu `LAYOUT-BLUEPRINT.md`, app shell, và page anatomy cho internal tools. Đây là tên mới
  theo vai trò của skill cũ `layout-consistency`. Skill này chỉ lo structure/layout language,
  không lo token, màu, hay typography system.
---

# Govern Layout

Skill tạo và enforce Layout Blueprint — bản mô tả chi tiết cấu trúc layout của 1 web project, dùng làm source of truth cho app shell và page structure.

Rule phân vai rõ:
- `DESIGN.md` lo **visual/system language**: token, component tone, hierarchy, interaction rules
- `LAYOUT-BLUEPRINT.md` lo **structural/layout language**: shell, page structure, tab structure, overlay structure

## Less is more cho layout
- Không thêm card wrapper, section title, hoặc breadcrumb phụ nếu shell hiện tại đã đủ ngữ cảnh.
- Ưu tiên một trục đọc rõ ràng thay vì chia màn hình thành quá nhiều khối ngang nhau.
- Chỉ giữ lại pattern layout lặp lại được; loại bỏ những layout one-off làm entropy tăng.
- Filter phụ, panel phụ, và metadata phụ phải được gom hoặc ẩn có chủ đích.

---

## Default desktop baseline for internal web

- Use `1920 x 900` usable viewport as the primary desktop baseline.
- Treat this as the standard Full HD browser working area after browser chrome.
- Define page width, content max width, grid columns, and card sizing so the intended layout holds at `1920 x 900` first.
- Wide screens such as 4K may add breathing room, but they must not silently change the core information architecture or card-column count unless the product explicitly calls for it.

## Header ownership va minimization

- Header duoc chia thanh 3 lop ro rang:
  - shell header = app identity only
  - page header = page identity only
  - body controls = tabs, filters, page actions
- Moi thong tin chi co 1 owner. Khong lap lai cung mot context o shell, page header, va body controls.
- Mac dinh uu tien brand-only shell. Khong dat page-level CTA, selected entity, topic selector, date-range context, hay operational state vao shell header tru khi project contract noi ro.
- Page header phai compact:
  - title la bat buoc
  - breadcrumb chi render khi day la drill-down that su, khong chi restate sidebar
  - subtitle, badge, meta, count chi duoc giu lai neu tao them action context hoac risk context ma body chua the hien
- Khi title, tab, filter, banner, hoac first content block da dien dat thong tin roi, khong lap lai thong tin do trong header.
- Khong coi mot top strip hien co la `project standard` neu no dang overloaded, wrap 2 dong, hoac tron nhieu loai context vao cung mot hang.

## Toolbar consistency for list pages

- In list pages, body controls own search, filters, clear utility actions, and page-level actions.
- If one list page in a product uses a toolbar-level `Clear all` for active filters, sibling list pages of the same pattern should do the same unless there is a documented exception.
- `Clear all` should live in the toolbar utility area, not inside page header copy, cards, or ad hoc inline text.
- A table-toolbar pattern is incomplete if it has resettable controls but no obvious toolbar-level reset behavior.

## KHÁI NIỆM CHÍNH

**Layout Blueprint** là 1 file Markdown mô tả toàn bộ layout system của project:
- **App Shell** — sidebar, header, breadcrumb, footer
- **Page Patterns** — cách bố trí nội dung trong từng loại page
- **Sub-page/Tab Patterns** — layout bên trong tabs, nested views
- **Overlay Patterns** — modal, drawer, popover layout
- **Spacing & Sizing Rules** — các con số cố định dùng xuyên suốt

Blueprint được lưu tại `LAYOUT-BLUEPRINT.md` trong root project (hoặc thư mục config).

---

## 2 CHẾ ĐỘ HOẠT ĐỘNG

### Mode A: SCAN — Tạo / cập nhật Blueprint

Khi project đã có code → scan codebase để extract layout patterns thực tế.

### Mode B: ENFORCE — Kiểm tra & apply Blueprint

Khi build page mới hoặc sửa page → đối chiếu với Blueprint hiện có.

---

## MODE A: SCAN & GENERATE BLUEPRINT

### Khi nào dùng Mode A
- Lần đầu dùng skill cho project này
- Sau khi refactor lớn, migration, hoặc thêm nhiều pages mới
- Khi muốn export layout standard sang project khác
- User nói "tạo blueprint", "scan layout", "extract layout"

### Quy trình scan

#### Bước 1 — Xác định project context

Đọc nhanh cấu trúc project:
```
1. ls src/ (hoặc tương đương) — xem folder structure
2. Tìm `DESIGN.md` — baseline cho visual/system language
3. Tìm App shell file (App.jsx, Layout.jsx, MainLayout, AppLayout...)
4. Tìm routing file — xác định danh sách pages
5. Tìm theme/token file — baseline design tokens
```

#### Bước 2 — Scan App Shell

Đọc chi tiết file layout chính. Extract:

| Layer | Cần extract | Cách tìm |
|-------|------------|----------|
| **Sidebar** | width, collapsed width, menu structure depth, icon usage, active state style | Grep `Sider`, `Menu mode="inline"`, sidebar keywords |
| **Header** | height, nội dung (logo, search, user menu, language, notifications), position (fixed/static) | Grep `Header`, header keywords |

Khi scan header, extract them:
- shell header dang chua nhung gi
- page header dang chua nhung gi
- body controls dang chua nhung gi
- co thong tin nao bi lap lai giua 3 lop khong
- shell co dang chua page-level action hay context khong
- page header co dang bi day len boi breadcrumb, badge, subtitle, count, hay meta khong
| **Breadcrumb** | có/không, format, max depth | Grep `Breadcrumb` |
| **Content wrapper** | padding, background, min-height | Đọc content area trong layout |
| **Footer** | có/không, height, nội dung | Grep `Footer` |

#### Bước 3 — Scan Page Patterns (3-5 pages đại diện)

Chọn pages đại diện cho các loại khác nhau:
- 1 list page (table + filter)
- 1 detail page
- 1 form/config page
- 1 dashboard (nếu có)
- 1 page có tabs/sub-pages

Với mỗi page, extract:

| Aspect | Chi tiết |
|--------|---------|
| **Page header** | Title vị trí, action buttons vị trí, có subtitle không |
| **Filter bar** | Kiểu (inline, collapsible, sidebar), vị trí, số fields visible |
| **Content area** | Card wrapper hay không, padding, background |
| **Tab layout** | Tab position, tab style (line/card/pill), content padding |
| **Table** | Có toolbar phía trên không, pagination style, row actions |
| **Card grid** | Grid columns, gutter, card structure |
| **Card action row** | Button sizing pattern (block vs flex:1), gap, alignment — tất cả cards cùng type phải dùng cùng pattern |
| **Quick actions** | Floating buttons, batch actions bar |

#### Bước 4 — Scan Sub-page / Tab Patterns

Với mỗi page có tabs:
- Đọc 2-3 tabs để xem nội dung bên trong
- So sánh: các tabs có cùng pattern không? (cùng dùng table, cùng có filter, cùng spacing)

#### Bước 5 — Scan Overlay Patterns

Grep `Modal`, `Drawer` trong codebase:
- Modal: default width, title style, footer button layout
- Drawer: width, placement, header/footer pattern

#### Bước 6 — Generate Blueprint

Đọc **references/blueprint-schema.md** để biết format chuẩn của blueprint file.

Tạo `LAYOUT-BLUEPRINT.md` với format đó. Điền data thực tế từ scan.

#### Bước 7 — Review & Present

Tóm tắt cho user:
- Đã scan X pages, Y components
- Layout system gồm: [tóm tắt nhanh shell + patterns]
- Có Z inconsistencies phát hiện (nếu có)
- Blueprint lưu tại [path]

---

## MODE B: ENFORCE — Check & Apply

### Khi nào dùng Mode B
- Build page/sub-page/tab mới
- Sửa layout page hiện tại
- Review xem page có match chuẩn không
- User nói "check layout", "page này đúng chuẩn chưa", "build page X theo layout chuẩn"

### Quy trình enforce

#### Bước 1 — Load contract

Đọc theo thứ tự:
1. `DESIGN.md` trong project, nếu có
2. `LAYOUT-BLUEPRINT.md` trong project

Nếu chưa có `DESIGN.md` → dùng foundation mặc định từ `design-system-antd/templates/DESIGN.md`.

Nếu chưa có `LAYOUT-BLUEPRINT.md` → hỏi user:
> "Project này chưa có Layout Blueprint. Muốn tôi scan tạo blueprint trước (Mode A), hay dùng layout standard mặc định?"

Nếu user chọn standard mặc định → đọc **references/shell-patterns.md** + **references/page-layout-catalog.md** làm baseline.

#### Bước 2 — Xác định page type

Dựa vào context, xác định page sắp build/sửa thuộc loại nào:

| Page type | Đặc điểm | Blueprint section tham chiếu |
|-----------|----------|------------------------------|
| List page | Table + filter + CRUD | `page_patterns.list` |
| Detail page | Info display + related data | `page_patterns.detail` |
| Form page | Create/edit entity | `page_patterns.form` |
| Dashboard | KPIs + charts + recent | `page_patterns.dashboard` |
| Config page | Settings, tabs + forms | `page_patterns.config` |
| Approval page | Cards/list + approve/reject | `page_patterns.approval` |
| Workflow page | Flow diagram + config | `page_patterns.workflow` |

#### Bước 3 — Apply layout rules

Khi build page mới → dùng layout specs từ blueprint:

```
Visual:    DESIGN.md (token, hierarchy, component tone)
Shell:     Blueprint.shell (sidebar, header, breadcrumb)
Page:      Blueprint.page_patterns[type]
Sub-page:  Blueprint.subpage_patterns (nếu page có tabs)
Overlays:  Blueprint.overlay_patterns (modals, drawers)
Spacing:   Blueprint.spacing_rules
```

Khi review page hiện tại → so sánh từng layer:

```
✅ Match   — giữ nguyên
🟡 Gần     — suggest minor adjustment (ví dụ: padding 16 → 24)
🔴 Khác    — flag rõ, explain khác gì, suggest fix
```

Header review checklist bat buoc khi enforce:
- shell header co chi con app identity khong
- page header co chi con page identity khong
- body controls co dang la noi duy nhat chua tabs / filters / page actions khong
- breadcrumb co that su can thiet hay chi lap lai menu
- subtitle / badge / meta / count co lap lai tab, filter, banner, table summary, hay first content block khong
- co page-level CTA nao dang nam sai o shell header khong
- co selected entity, date range, active state nao dang bi lap lai giua header va content khong

#### Bước 4 — Cross-page consistency check

So sánh page đang build/review với 1-2 pages cùng type đã có trong project:

| Check | Ví dụ |
|-------|-------|
| Same page type, same structure? | 2 list pages đều có filter bar → page mới cũng phải có |
| Same spacing? | Cards gap 16px everywhere → page mới cũng 16px |
| Same tab style? | Tất cả tabs dùng line style → page mới không dùng card style |
| Same action placement? | Primary button luôn góc phải trên → page mới cũng vậy |
| Same header ownership? | Shell chua brand only, page header chua page title, body moi chua controls |
| Same card action buttons? | Nếu PostCard dùng `block` trên cả 2 button → MissionCard, RewardCard cũng phải dùng `block`. KHÔNG mix `flex:1` với button không có flex |

#### Bước 5 — Report

Output ngắn gọn:
```
Layout Check: [Page name]
Type: [list/detail/form/dashboard/config]
Blueprint match: X/Y rules passed

🔴 Issues:
- [issue 1 + fix suggestion]
- [issue 2 + fix suggestion]

🟡 Suggestions:
- [suggestion 1]

✅ Matches:
- Shell layout, page header, filter bar position, table pagination
```

---

## CROSS-PROJECT SYNC

Khi cần dùng layout từ project A cho project B → đọc **references/cross-project-sync.md**.

Quy trình tóm tắt:
1. Export blueprint từ project A (đã có từ Mode A)
2. Import blueprint vào project B
3. Adjust project-specific values (sidebar menu items, colors, branding)
4. Giữ nguyên structural rules (spacing, layout patterns, overlay patterns)

---

## MODE C: BUILD SHARED LAYOUT COMPONENT (ProLayout-inspired)

Khi cần enforce layout consistency ở mức CODE (không chỉ document) — tạo shared AdminLayout component package lấy cảm hứng từ Ant Design ProLayout nhưng dùng antd v6 core.

### Khi nào dùng Mode C
- Bắt đầu ecosystem mới với nhiều projects
- Muốn layout enforce bằng code thay vì chỉ bằng document
- User nói "tạo layout component", "shared layout", "AdminLayout"
- Khi blueprint đã ổn định và muốn "đóng gói" thành component tái sử dụng

### Quy trình

1. **Load blueprint** (từ Mode A) hoặc dùng standard defaults
2. Đọc **references/admin-layout-component.md** — chứa architecture + code patterns
3. Generate các components:
   - `AdminLayout` — wrap antd Layout + Sider + Header + Content
   - `PageContainer` — auto breadcrumb + page header + tabs
   - `LayoutContext` — share layout state (collapsed, isMobile, siderWidth)
   - `layout-tokens.js` — layout-specific design tokens
4. Output theo mode phù hợp (tham chiếu build-frontend cho output mode)

### ProLayout concepts được adopt

| ProLayout Feature | Adopt? | Cách implement với antd v6 |
|---|---|---|
| **Auto menu từ routes** | ✅ | Route config → Menu items transform |
| **Auto breadcrumb** | ✅ | Parse pathname → Breadcrumb items |
| **Layout tokens** (header.*, sider.*) | ✅ | ConfigProvider theme + custom token object |
| **LayoutContext** (isMobile, collapsed) | ✅ | React Context + useBreakpoint hook |
| **Layout modes** (side/top/mix) | ✅ | Props-driven: `layout="side"` |
| **PageContainer** | ✅ | Wrapper: breadcrumb + title + tabs + actions |
| **FooterToolbar** | ✅ | Fixed bottom bar, accounts for sider width |
| **WaterMark** | 🟡 Optional | antd v6 có sẵn `Watermark` component |
| **Responsive collapse** | ✅ | Sider breakpoint + Drawer on mobile |
| **navTheme** (dark/light) | ✅ | Token switching |
| **splitMenus** (mix mode) | ❌ Skip | Phức tạp, ít dùng cho internal tool |

### Token system (lấy từ ProLayout, simplified)

```javascript
const layoutTokens = {
  header: {
    colorBgHeader: '#fff',
    heightLayoutHeader: 48,
    colorTextMenu: 'rgba(0,0,0,0.88)',
  },
  sider: {
    colorMenuBackground: '#001529',
    colorTextMenu: 'rgba(255,255,255,0.65)',
    colorTextMenuSelected: '#fff',
    colorBgMenuItemSelected: 'rgba(255,255,255,0.08)',
    colorBgMenuItemHover: 'rgba(255,255,255,0.04)',
    menuWidth: 200,
    collapsedWidth: 64,
  },
  pageContainer: {
    colorBgPageContainer: '#f5f5f5',
    paddingContent: 24,
    marginContent: 16,
  },
};
```

Chi tiết implementation → đọc **references/admin-layout-component.md**

---

## TƯƠNG TÁC VỚI CÁC SKILL KHÁC

| Skill | Quan hệ |
|-------|---------|
| **design-system-antd** | Cung cấp AntD foundation và `DESIGN.md` mặc định. Govern-layout chỉ lo structural enforcement |
| **build-frontend** | Code agent đọc `DESIGN.md` trước, rồi `LAYOUT-BLUEPRINT.md` để output code đúng visual + structure |
| **design-uiux** | Design agent đọc `DESIGN.md` trước, rồi blueprint để quyết định layout và UI |
| **review-frontend** | Review skill chấm consistency. Govern-layout cung cấp blueprint làm scoring baseline |
| **analyze-gap** | Analyze-gap so sánh logic/content. Govern-layout so sánh layout structure |

---

## NGUYÊN TẮC

### Blueprint là descriptive, không prescriptive
Blueprint mô tả layout THỰC TẾ của project, không phải layout "lý tưởng". Nếu project đang dùng sidebar 240px thay vì 200px chuẩn antd — blueprint ghi 240px. Consistency quan trọng hơn "best practice".

### Tolerance cho intentional variations
Không phải mọi page đều phải giống nhau. Dashboard layout khác List page layout là bình thường. Blueprint ghi nhận các loại page patterns khác nhau, chỉ flag khi cùng loại mà khác nhau.

### Minimal disruption
Khi enforce, ưu tiên suggest thay đổi nhỏ nhất để đạt consistency. Không đề xuất refactor toàn bộ page chỉ vì 1 chỗ khác biệt.

### Blueprint evolves
Blueprint cần update khi project thay đổi đáng kể. Không phải tạo 1 lần rồi bỏ. Suggest user re-scan sau mỗi major release hoặc migration phase.

---

## NAVIGATION SHELL ADDENDUM

Khi scan hoac enforce `LAYOUT-BLUEPRINT.md`, coi navigation shell la mot phan cua structural contract:

- App shell phai the hien dung information architecture da chot o discovery, khong flatten menu vi ly do implementation.
- Top-level nav chi danh cho workspaces/chuc nang chinh. Settings, admin, permission, credential, integration, notification, system pages mac dinh phai group duoi node cha.
- Blueprint phai ghi ro:
  - top-level nav order
  - parent/child hierarchy
  - child order trong cac node nhu `Settings`
  - active/open-state behavior khi vao route con
  - page nao la `CTA-only flow`
- Khi scan codebase, sidebar extraction phai kiem tra them:
  - hierarchy dang co hay dang bi flatten
  - page nao dang la CTA-only flow nhung bi day len menu
  - route con co giu parent node mo dung khong
- Khi enforce layout:
  - top-level nav phai match workflow order da chot
  - grouped pages phai nam dung duoi parent node
  - khong bien `Create` flow thanh sidebar item neu blueprint ghi `CTA-only`



