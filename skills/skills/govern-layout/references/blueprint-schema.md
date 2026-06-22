# Layout Blueprint Schema

File `LAYOUT-BLUEPRINT.md` có cấu trúc cố định để máy đọc được + người đọc được.

---

## Template chuẩn

```markdown
# Layout Blueprint — {Project Name}

> Generated: {date} | Last updated: {date}
> Source project: {repo URL hoặc folder name}
> Pages scanned: {số pages} | Components scanned: {số components}

---

## 1. App Shell

### Sidebar
- **Width**: {number}px (expanded) / {number}px (collapsed)
- **Collapsible**: yes/no
- **Position**: fixed / static
- **Background**: {color token hoặc hex}
- **Menu depth**: {number} levels
- **Menu icons**: level 1 only / all levels / none
- **Active indicator**: {mô tả — ví dụ: "left blue border + bg highlight"}
- **Hover style**: {mô tả}
- **Dividers**: {mô tả — ví dụ: "between menu groups"}
- **Bottom section**: {mô tả — ví dụ: "user info + settings"}

### Header
- **Height**: {number}px
- **Position**: fixed / static / sticky
- **Background**: {color token hoặc hex}
- **Content left**: {mô tả — ví dụ: "breadcrumb"}
- **Content center**: {mô tả — ví dụ: "global search"}
- **Content right**: {mô tả — ví dụ: "language toggle, notifications, user avatar"}
- **Border bottom**: yes/no, {color if yes}

### Breadcrumb
- **Enabled**: yes / no / only on detail pages
- **Position**: inside header / top of content area
- **Format**: {ví dụ: "Home / Module / Page"}
- **Max depth**: {number}

### Content Area
- **Padding**: {top} {right} {bottom} {left} px
- **Background**: {color token hoặc hex}
- **Max width**: {number}px / none (full width)
- **Min height**: calc(100vh - {header}px)

### Footer
- **Enabled**: yes / no
- **Height**: {number}px
- **Content**: {mô tả}

---

## 2. Page Patterns

### 2.1 List Page
- **Wrapper**: Card / none / custom
- **Card padding**: {number}px
- **Page header**: {title position} + {action buttons position}
  - Title: {font size}px, {font weight}
  - Actions: {ví dụ: "flex end, primary button + secondary buttons"}
- **Filter bar**:
  - Style: inline / collapsible / sidebar / tabs
  - Position: above content / inside card top
  - Fields visible: {number} (collapsed) / {number} (expanded)
  - Search + Reset buttons: {position}
- **Quick filter tabs**: {ví dụ: "Tất cả | Pending | Approved — using Segmented/Radio.Group"}
- **Table**:
  - Has toolbar above: yes / no
  - Toolbar content: {ví dụ: "count left, export + batch actions right"}
  - Row selection: checkbox / none
  - Row actions: inline links / dropdown / icon buttons
  - Pagination: full / simple / mini
  - Pagination position: bottom right / bottom center
- **Empty state**: {component hoặc pattern}

### 2.2 Detail Page
- **Header card**: {mô tả — title + actions}
- **Info section**: Descriptions / custom key-value / card grid
- **Tabs**: yes / no
  - Tab style: line / card / pill
  - Tab position: top / left
- **Related data**: Table / List / Cards
- **Back navigation**: breadcrumb / back button / both

### 2.3 Form Page
- **Modal form** (≤ {N} fields):
  - Modal width: {number}px
  - Form layout: vertical / horizontal
  - Label width: {number}px (if horizontal)
  - Footer: {ví dụ: "Cancel left, Submit right"}
- **Drawer form** ({N}–{M} fields):
  - Drawer width: {number}px
  - Placement: right / left
  - Extra (header actions): {ví dụ: "Cancel + Save buttons"}
- **Full page form** (> {M} fields):
  - Steps: yes / no
  - Steps position: top / left
  - Step count: {range}

### 2.4 Dashboard
- **KPI row**: {columns count} x Statistic cards
- **KPI card**: {mô tả — title, value, trend, comparison}
- **Grid**: Row gutter {number}px
- **Chart section**: {layout ví dụ: "2/3 + 1/3"}
- **Recent activity**: Table / Timeline / List

### 2.5 Config Page
- **Tabs**: yes / no
- **Tab style**: line / card
- **Form per tab**: yes / no
- **Save button**: per tab / global

### 2.6 Approval Page
- **View mode**: card grid / table / both (toggle)
- **Card structure**: {mô tả — status badge, title, meta, action buttons}
- **Quick filter**: status tabs (Pending, Approved, Rejected...)
- **Batch actions**: yes / no

### 2.7 Workflow Page
- **List panel**: left sidebar with workflow list
- **Detail panel**: right side with flow diagram
- **Flow display**: vertical steps / horizontal flow / visual diagram

---

## 3. Sub-page / Tab Patterns

### Tab container
- **Tab bar padding**: {number}px
- **Tab content padding**: {number}px
- **Tab + content gap**: {number}px

### Tab content patterns
Ghi nhận pattern phổ biến trong tabs:

| Pattern | Ví dụ | Structure |
|---------|-------|-----------|
| Tab → Table | Permissions tab in Admin | Filter + Table |
| Tab → Card grid | Mission types in Config | Card.Grid |
| Tab → Form | Settings tabs | Form + Save button |
| Tab → Mixed | Creator detail tabs | Varies per tab |

### Sibling consistency rules
- Tabs cùng level nên có cùng {padding / spacing / empty state}
- Nếu 1 tab có filter → xem xét tất cả tabs cùng level có cần filter không
- Tab content height: consistent min-height hoặc auto

---

## 4. Overlay Patterns

### Modal
- **Sizes**: small ({W}px) / default ({W}px) / large ({W}px)
- **Title style**: {font size, weight}
- **Body padding**: {number}px
- **Footer**: {ví dụ: "Cancel + OK, align right"}
- **Close behavior**: X button + click outside / X only
- **Scroll**: body scroll only (header + footer fixed)

### Drawer
- **Default width**: {number}px
- **Placement**: right / left
- **Header**: title + close button
- **Footer / Extra**: {mô tả}
- **Scroll**: body scroll only

### Popover / Dropdown
- **Max width**: {number}px
- **Max height**: {number}px (with scroll)
- **Shadow**: {token}

---

## 5. Spacing Rules

### Vertical rhythm
| Between | Spacing | Token |
|---------|---------|-------|
| Page header → Content | {N}px | {token} |
| Filter bar → Table | {N}px | {token} |
| Card → Card | {N}px | {token} |
| Section → Section | {N}px | {token} |
| Tab bar → Tab content | {N}px | {token} |
| Form items | {N}px | antd default |
| Button group gap | {N}px | {token} |

### Horizontal rhythm
| Context | Spacing | Token |
|---------|---------|-------|
| Card padding | {N}px | {token} |
| Content margin | {N}px | {token} |
| Grid gutter | {N}px | — |
| Inline form items gap | {N}px | — |

---

## 6. Consistency Score

Kết quả scan khi generate blueprint:

| Layer | Pages match | Total pages | Score |
|-------|-------------|-------------|-------|
| Shell | — | — | — (single instance) |
| Page headers | {X} | {Y} | {X/Y} |
| Filter bars | {X} | {Y} | {X/Y} |
| Table patterns | {X} | {Y} | {X/Y} |
| Tab patterns | {X} | {Y} | {X/Y} |
| Modal patterns | {X} | {Y} | {X/Y} |
| Spacing | {X} | {Y} | {X/Y} |
| **Overall** | | | **{avg}** |

### Inconsistencies found
| # | Layer | Issue | Pages affected | Suggested fix |
|---|-------|-------|---------------|---------------|
| 1 | ... | ... | ... | ... |
```

---

## Ghi chú cho người dùng

- Sections không áp dụng (ví dụ project không có footer) → ghi "N/A" hoặc bỏ section
- Values nên dùng design tokens khi có thể, fallback sang px values
- Blueprint nên được commit vào repo để team tham chiếu
- Re-generate sau mỗi major refactor hoặc mỗi quarter
