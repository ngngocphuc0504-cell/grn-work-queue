# Shell Patterns — App Shell Catalog

Catalog các kiểu app shell phổ biến cho internal tool. Dùng làm baseline khi project chưa có blueprint, hoặc khi bắt đầu project mới.

---

## 1. SHELL TYPE: SIDEBAR + HEADER (Phổ biến nhất)

Layout chuẩn cho internal tool có nhiều modules.

```
┌──────────────────────────────────────────────────┐
│ [Logo]           Header              [User Menu] │
├──────────┬───────────────────────────────────────┤
│          │  Breadcrumb (optional)                 │
│ Sidebar  │───────────────────────────────────────│
│ (fixed)  │                                       │
│          │  Content Area                          │
│          │  (scrollable)                          │
│          │                                       │
│          │                                       │
├──────────┤                                       │
│ [User]   │                                       │
└──────────┴───────────────────────────────────────┘
```

### Sidebar specs

| Property | Standard | Compact | Wide |
|----------|----------|---------|------|
| Width (expanded) | 200px | 180px | 240–256px |
| Width (collapsed) | 64px | 48px | 80px |
| Background | Dark (#001529) hoặc White (#fff) | Same | Same |
| Logo area height | 48–64px | 40px | 64px |

**Dark sidebar** (phổ biến cho Garena tools):
- Background: `#001529` hoặc dark gradient
- Menu text: `rgba(255,255,255,0.65)` → active: `#fff`
- Active item: left border accent (blue `#1677ff`) + bg highlight `rgba(255,255,255,0.08)`
- Hover: bg `rgba(255,255,255,0.04)`
- Divider: `rgba(255,255,255,0.08)`
- Icons: level 1 only, 16–20px

**Light sidebar**:
- Background: `#fff` + right border `#f0f0f0`
- Menu text: `rgba(0,0,0,0.88)` → active: `colorPrimary`
- Active item: bg `colorPrimaryBg` + left border `colorPrimary`

### Sidebar menu structure

```
Level 1: Icon + Label (collapse → icon only)
  Level 2: Label only (indent 24px)
    Level 3: Label only (indent 48px) — tránh nếu có thể
```

Quy tắc menu:
- Tối đa 3 levels depth — sâu hơn → dùng tabs trong page thay vì thêm menu level
- Menu item label: 2–4 từ, tiếng Việt hoặc tiếng Anh (đồng nhất)
- Badge/count: hiển thị ở menu items cần attention (ví dụ: "Pending 5")
- Bottom section: user info (avatar + name + role) + settings/logout

### Header specs

| Property | Standard | Compact |
|----------|----------|---------|
| Height | 48–64px | 40px |
| Background | `#fff` | `#fff` |
| Border bottom | `1px solid #f0f0f0` | Same |
| Content padding | `0 16px` hoặc `0 24px` | `0 12px` |

Header content zones:
```
[Left]                    [Center]                    [Right]
Breadcrumb / Page title   Global search (optional)    Language, Notifications, User
```

Nếu sidebar đã có menu → header KHÔNG cần navigation. Header chỉ chứa:
- Breadcrumb (nếu có detail pages) hoặc page title
- Global search (nếu project cần)
- Utilities: language switch, notification bell, user avatar dropdown

### Content area specs

| Property | Value | Lý do |
|----------|-------|-------|
| Padding | 16–24px all sides | Tạo breathing room |
| Background | `#f5f5f5` (colorBgLayout) | Phân biệt với card content |
| Overflow | auto (vertical) | Content scrollable |
| Min height | `calc(100vh - headerHeight)` | Full viewport |

---

## 2. SHELL TYPE: TOP NAV + CONTENT

Ít phổ biến hơn. Dùng khi ít modules (< 8) và flat navigation.

```
┌──────────────────────────────────────────────────┐
│ [Logo]  [Nav1] [Nav2] [Nav3]         [User Menu] │
├──────────────────────────────────────────────────┤
│                                                   │
│  Content Area (centered, max-width)               │
│                                                   │
└──────────────────────────────────────────────────┘
```

Specs:
- Header height: 48–64px
- Nav items: horizontal Menu, max 8 items
- Content max-width: 1200px (centered)
- Content padding: 24px

---

## 3. SHELL TYPE: TOP NAV + SIDEBAR

Hybrid cho app rất lớn. Top nav chọn module, sidebar chọn page trong module.

```
┌──────────────────────────────────────────────────┐
│ [Logo]  [Module1] [Module2] [Module3] [User Menu]│
├──────────┬───────────────────────────────────────┤
│          │                                       │
│ Sub-nav  │  Content Area                          │
│ (sidebar)│                                       │
│          │                                       │
└──────────┴───────────────────────────────────────┘
```

Dùng khi: Module có sub-navigation phức tạp nhưng modules chính ít (3–6).

---

## 4. CONSISTENCY RULES CHO SHELL

Dù dùng shell type nào, các rules sau luôn áp dụng:

### Rule 1: Shell is constant
App shell KHÔNG thay đổi giữa các pages. Sidebar + header luôn giống nhau. Chỉ content area thay đổi.

Ngoại lệ cho phép:
- Login page (không có shell)
- Public pages (có thể dùng simplified shell)
- Print view (không có shell)

### Rule 2: Active state rõ ràng
User phải biết đang ở page nào chỉ bằng nhìn sidebar/header. Menu item active phải có visual khác biệt rõ (background, border, hoặc color).

### Rule 3: Responsive nhất quán
Nếu sidebar collapse trên mobile → tất cả pages đều collapse sidebar. Không có page nào "đặc biệt" giữ sidebar expanded.

### Rule 4: Transition smooth
Chuyển page → content area thay đổi, shell giữ nguyên. Không flash, không re-render shell.

---

## 5. DARK SIDEBAR REFERENCE (Garena Style)

Dựa trên screenshots UGC Website:

```css
/* Sidebar */
--sidebar-bg: #001529;
--sidebar-width: 200px;
--sidebar-collapsed-width: 64px;

/* Menu */
--menu-item-height: 40px;
--menu-item-padding: 0 16px;
--menu-text-color: rgba(255, 255, 255, 0.65);
--menu-text-active: #ffffff;
--menu-item-active-bg: rgba(255, 255, 255, 0.08);
--menu-item-active-border: 3px solid #1677ff;
--menu-item-hover-bg: rgba(255, 255, 255, 0.04);
--menu-icon-size: 18px;
--menu-group-divider: rgba(255, 255, 255, 0.08);

/* User section (bottom) */
--user-section-height: 56px;
--user-section-border-top: 1px solid rgba(255, 255, 255, 0.08);

/* Header */
--header-height: 48px;
--header-bg: #ffffff;
--header-border-bottom: 1px solid #f0f0f0;
--header-padding: 0 24px;

/* Content */
--content-padding: 16px; /* hoặc 24px */
--content-bg: #f5f5f5;
```

---

## 6. SCANNING CHECKLIST

Khi scan app shell, xác nhận từng item:

- [ ] Sidebar width (expanded + collapsed)
- [ ] Sidebar background + text colors
- [ ] Sidebar menu structure (levels, icons, badges)
- [ ] Sidebar active/hover states
- [ ] Sidebar bottom section (user info)
- [ ] Header height + background
- [ ] Header content (left, center, right)
- [ ] Header border/shadow
- [ ] Breadcrumb: enabled? format? position?
- [ ] Content area padding
- [ ] Content area background
- [ ] Content area min-height
- [ ] Footer: enabled? content?
- [ ] Shell behavior on resize (responsive)
- [ ] Shell transition (page change animation)
