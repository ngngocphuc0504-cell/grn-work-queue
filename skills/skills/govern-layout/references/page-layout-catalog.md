# Page Layout Catalog

Catalog chi tiết layout patterns cho từng loại page + sub-page. Mỗi pattern bao gồm: structure diagram, spacing specs, consistency rules, và common variations.

Đây là reference khi chưa có project-specific blueprint, hoặc dùng làm baseline đối chiếu.

---

## 1. LIST PAGE LAYOUT

Trang phổ biến nhất trong internal tool. Hiển thị danh sách entities với filter + actions.

### Structure

```
┌─────────────────────────────────────────────────┐
│ [Page Title]                    [+ Create] [...]│  ← Page Header
├─────────────────────────────────────────────────┤
│ [Search] [Filter1 ▼] [Filter2 ▼]  [Search][Reset]│  ← Filter Bar
├─────────────────────────────────────────────────┤
│ [All 80] [Pending 6] [Active 2] [Rejected 4]   │  ← Quick Filter (optional)
├─────────────────────────────────────────────────┤
│ [X selected] [Batch Action]    [12/80] [Export] │  ← Toolbar (optional)
├─────────────────────────────────────────────────┤
│ ☐ │ Name    │ Status │ Date    │ Actions        │  ← Table (scroll.y auto)
│ ☐ │ ...     │ ...    │ ...     │ Edit | Delete  │
│ ☐ │ ...     │ ...    │ ...     │ Edit | Delete  │
├─────────────────────────────────────────────────┤
│                          [< 1 2 3 ... 10 >]    │  ← Pagination (always visible)
└─────────────────────────────────────────────────┘
```

### Spacing specs

| Gap | Value | Lý do |
|-----|-------|-------|
| Card padding | 24px (paddingLG) hoặc 16px | Container breathing room |
| Page header → Filter bar | 16px | Nhóm liên quan |
| Filter bar → Quick filter | 12–16px | Nhóm liên quan |
| Quick filter → Table | 16px | Phân tách section |
| Toolbar → Table | 8–12px | Liên kết chặt với table |
| Table → Pagination | 16px (antd default) | — |

### Consistency rules

| Rule | Mô tả |
|------|-------|
| **Filter bar position** | Luôn nằm TRÊN table, không ở sidebar |
| **Primary action** | Nút "Tạo mới" / "+ Create" luôn ở góc phải trên |
| **Quick filter style** | Dùng cùng component across pages (Radio.Group, Segmented, hoặc custom tabs) |
| **Table pagination** | Cùng style: showTotal + showSizeChanger. **Pagination luôn visible** trong viewport — xem Section 9 |
| **Row actions** | Cùng format: inline text links hoặc icon buttons (chọn 1, dùng cho tất cả) |
| **Empty state** | Cùng component/pattern: icon + text + CTA button |

### Common variations (cho phép khác nhau)

| Variation | Ví dụ | Lý do cho phép |
|-----------|-------|---------------|
| Card grid thay table | Approval center, Creator list | Data visual hơn dạng bảng |
| View toggle (grid/table) | Mission list, Reward request | User preference |
| Filter collapsible | Filter-heavy pages | Tiết kiệm space |
| Frozen columns | Wide tables (Shop Config) | Usability |

---

## 2. DETAIL PAGE LAYOUT

Hiển thị chi tiết 1 entity + related data.

### Structure

```
┌─────────────────────────────────────────────────┐
│ [← Back] Creator: Nguyễn Văn An     [Edit][Ban] │  ← Header Card
├─────────────────────────────────────────────────┤
│ Email: ...        │ Platform: ...                │
│ Phone: ...        │ Followers: ...               │  ← Info Card (Descriptions)
│ Status: Active    │ Joined: ...                  │
├─────────────────────────────────────────────────┤
│ [Missions] [Rewards] [History] [Settings]        │  ← Tabs
├─────────────────────────────────────────────────┤
│                                                  │
│  Tab content (table, list, form...)              │  ← Tab Content
│                                                  │
└─────────────────────────────────────────────────┘
```

### Spacing specs

| Gap | Value |
|-----|-------|
| Header card → Info card | 16px |
| Info card → Tabs card | 16px |
| Tab bar → Tab content | 16px (inside card) |
| Cards ngoài → content | 24px padding |

### Consistency rules

| Rule | Mô tả |
|------|-------|
| **Back navigation** | Breadcrumb hoặc back button — chọn 1 pattern dùng cho tất cả detail pages |
| **Header actions** | Align right, cùng button style với list page |
| **Info layout** | Descriptions 2 hoặc 3 columns — consistent across detail pages |
| **Tab style** | Cùng tab type (line/card) across detail pages |
| **Tab content padding** | Bằng nhau giữa các tabs |

---

## 3. FORM LAYOUTS

### 3.1 Modal Form

```
┌─────────────────────────────────┐
│ [Title]                    [✕]  │  ← Fixed header
├─────────────────────────────────┤
│                                 │
│  Label:  [Input___________]     │
│  Label:  [Select__________▼]    │  ← Scrollable body
│  Label:  [DatePicker______]     │
│                                 │
├─────────────────────────────────┤
│              [Cancel] [Submit]  │  ← Fixed footer
└─────────────────────────────────┘
```

Rules:
- Header + Footer luôn visible (không scroll mất)
- Body scroll khi content dài
- Tất cả input fields cùng width
- Label position: vertical (trên input) hoặc horizontal (trái input) — chọn 1 cho toàn project

### 3.2 Drawer Form

```
┌────────────────────────────────────┐
│ [Title]              [Cancel][Save]│  ← Fixed header + actions
├────────────────────────────────────┤
│                                    │
│  Label                             │
│  [Input____________________]       │
│                                    │  ← Scrollable body
│  Label                             │
│  [TextArea_________________]       │
│  [________________________]        │
│                                    │
└────────────────────────────────────┘
```

Rules:
- Width: 480–720px (consistent across project)
- Actions ở header (extra prop) hoặc footer — chọn 1
- Form layout: vertical preferred (more space)

### 3.3 Inline Form (filter bar)

```
[Search___] [Select▼] [DateRange] [🔍 Search] [↻ Reset]
```

Rules:
- Inline layout hoặc grid layout (Row/Col)
- Buttons luôn ở cuối hàng (hoặc hàng cuối)
- Style nhất quán: tất cả filter bars dùng cùng grid breakpoints

---

## 4. DASHBOARD LAYOUT

### Structure

```
┌────────┬────────┬────────┬────────┐
│ KPI 1  │ KPI 2  │ KPI 3  │ KPI 4  │  ← Row 1: Statistic Cards
├────────┴────────┴────────┴────────┤
│                                    │
│ ┌──────────────────┐ ┌──────────┐ │
│ │ Chart (2/3)      │ │Chart(1/3)│ │  ← Row 2: Charts
│ └──────────────────┘ └──────────┘ │
│                                    │
│ ┌──────────────────────────────┐  │
│ │ Recent Activity Table        │  │  ← Row 3: Data
│ └──────────────────────────────┘  │
└────────────────────────────────────┘
```

### Spacing

| Gap | Value |
|-----|-------|
| Row gutter | 16px |
| Col gutter | 16px |
| KPI card → Charts | 16–24px |
| Charts → Table | 16–24px |

### Consistency rules

| Rule | Mô tả |
|------|-------|
| **KPI cards** | Cùng height, cùng structure (title + value + trend) |
| **Card border** | Tất cả cards cùng border-radius + shadow |
| **Grid** | Row gutter = Col gutter (square grid feel) |
| **Responsive** | KPI: 4 cols → 2 cols → 1 col. Charts: 2 cols → 1 col |

---

## 5. CONFIG PAGE LAYOUT

```
┌─────────────────────────────────────────────────┐
│ [Tab1] [Tab2] [Tab3] [Tab4] [Tab5]              │
├─────────────────────────────────────────────────┤
│                                                  │
│  Form / Table / Config UI per tab                │
│                                                  │
│                            [Save Changes]        │
└─────────────────────────────────────────────────┘
```

Rules:
- Tabs ở top, line style
- Mỗi tab là 1 independent section
- Save button: per tab (preferred) hoặc global bottom
- Tab content padding: consistent across tabs

---

## 6. APPROVAL PAGE LAYOUT

```
┌─────────────────────────────────────────────────┐
│ [Page Title]              [🔲 Grid] [≡ Table]   │
├─────────────────────────────────────────────────┤
│ [All 34] [Pending 9] [Approved 2] [Rejected 8] │
│ 34 requests · 9 pending                         │
├─────────────────────────────────────────────────┤
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │ Card 1   │ │ Card 2   │ │ Card 3   │         │
│ │ [Type]   │ │ [Type]   │ │ [Type]   │         │
│ │ Title    │ │ Title    │ │ Title    │         │
│ │ Meta...  │ │ Meta...  │ │ Meta...  │         │
│ │[✓ OK][✗] │ │[✓ OK][✗] │ │[✓ OK][✗] │         │
│ └──────────┘ └──────────┘ └──────────┘         │
└─────────────────────────────────────────────────┘
```

Rules:
- View toggle (grid/table) nếu hỗ trợ cả 2
- Status color: consistent với project-wide status colors
- Card structure: cùng nhau giữa các loại request
- Action buttons: cùng vị trí, cùng style

---

## 7. WORKFLOW PAGE LAYOUT

```
┌─────────────────────────────────────────────────┐
│ [Tab1: Workflow] [Tab2: Config] [Tab3: ...]     │
├──────────────┬──────────────────────────────────┤
│ Workflows    │ Workflow Detail                   │
│              │                                   │
│ ● Active ✓  │ [Name]  [Tags]  [Status]          │
│   Sub1       │─────────────────────────────────  │
│   Sub2       │ [Flow (11 steps)] [History (4)]   │
│ ○ Inactive   │─────────────────────────────────  │
│              │ ┌─────────┐                       │
│              │ │ Step 1  │                       │
│              │ └────┬────┘                       │
│              │      │                            │
│              │ ┌────┴────┐                       │
│              │ │ Step 2  │                       │
│              │ └─────────┘                       │
└──────────────┴──────────────────────────────────┘
```

Rules:
- Master-detail layout: list trái, detail phải
- List panel: fixed width (200–300px), scrollable
- Detail panel: flex grow, scrollable independently
- Active workflow: visual indicator (color dot, border)

---

## 8. SETTINGS PAGE LAYOUT (My Setting + Role Presets)

Trang cài đặt notification hoặc preference với sidebar chọn role/profile + content panel bên phải.

### Structure

```
┌─────────────────────────────────────────────────────────────┐
│ [Tab1: Admin Notification] [Tab2: User Notification]        │
├───────────────┬─────────────────────────────────────────────┤
│ ROLE DEFAULT  │ 📧 Email — 19 types ●19 ●0 ●0  Quick set: │
│               │ [● Immediately] [● Daily] [● Stop]          │  ← Summary Bar
│ ┌───────────┐ ├─────────────────────────────────────────────┤
│ │ My Setting│ │ Notifi