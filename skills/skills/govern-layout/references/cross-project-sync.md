# Cross-Project Layout Sync

Hướng dẫn đồng bộ layout giữa nhiều web projects. Đảm bảo user chuyển từ Tool A sang Tool B vẫn thấy giao diện quen thuộc.

---

## 1. NGUYÊN TẮC

### Shared vs Project-specific

Layout blueprint có 2 lớp:

| Lớp | Ví dụ | Sync across projects? |
|-----|-------|----------------------|
| **Structural** | Sidebar width, header height, content padding, card border-radius, spacing rules | **Có** — phải giống nhau |
| **Content** | Menu items, page-specific patterns, branding colors, logo | **Không** — khác nhau theo project |

### Quy tắc vàng
> Khi user mở project B lần đầu, họ phải biết cách navigate ngay lập tức vì layout trông giống project A mà họ đã dùng quen.

Điều này có nghĩa:
- Sidebar ở cùng vị trí, cùng width, cùng behavior (collapse/expand)
- Header ở cùng vị trí, cùng height, cùng utilities layout
- Content area cùng padding, cùng background
- Table, filter, modal, drawer cùng patterns
- Chỉ khác: menu items, branding, data content

---

## 2. 3 CẤP ĐỘ SYNC

Có 3 cấp độ sync, từ nhẹ → nặng. Chọn cấp phù hợp:

| Cấp | Approach | Effort | Consistency |
|-----|----------|--------|-------------|
| **L1: Blueprint only** | Copy LAYOUT-BLUEPRINT.md, enforce bằng review | Thấp | Trung bình (phụ thuộc người follow) |
| **L2: Shared tokens** | Import chung `layout-tokens.js` | Trung bình | Cao cho spacing/sizing |
| **L3: Shared component** | Import `AdminLayout` package (Mode C) | Cao ban đầu, thấp sau đó | Rất cao — code enforce |

**Recommend:** Bắt đầu L1 → khi có 2+ projects thì lên L3.

---

## 3. QUY TRÌNH SYNC

### Scenario A: Có project gốc (Source of Truth)

Project gốc đã có blueprint → export cho projects mới.

```
Step 1: Scan project gốc → tạo LAYOUT-BLUEPRINT.md (Mode A)
Step 2: Copy LAYOUT-BLUEPRINT.md sang project mới
Step 3: Adjust content layer:
        - Đổi project name
        - Đổi menu items
        - Đổi branding nếu cần (logo, accent color)
        - GIỮ NGUYÊN structural layer
Step 4: Build project mới theo adjusted blueprint (Mode B enforce)
```

**Nâng cấp lên L3:** Dùng Mode C để generate AdminLayout component từ blueprint → package thành shared library → mọi project import.

### Scenario B: Không có project gốc (Start from Standard)

Chưa có project nào hoàn thiện → dùng standard layout.

```
Step 1: Đọc shell-patterns.md → chọn shell type
Step 2: Đọc page-layout-catalog.md → note các patterns sẽ dùng
Step 3: Tạo LAYOUT-BLUEPRINT.md từ standard values
Step 4: Adjust cho project-specific needs
Step 5: Build theo blueprint (Mode B enforce)
Step 6: Sau khi project A hoàn thiện → dùng nó làm source of truth cho project B
```

### Scenario C: Sync ngược (Project mới có cải tiến → apply lại project cũ)

```
Step 1: Diff blueprint project A vs project B
Step 2: Identify improvements (ví dụ: project B có filter bar tốt hơn)
Step 3: Cập nhật master blueprint
Step 4: Apply ngược vào project A (Mode B enforce with updated blueprint)
```

### Scenario D: Shared AdminLayout component (L3 — recommended cho 2+ projects)

```
Step 1: Dùng Mode C → generate AdminLayout từ blueprint
Step 2: Publish thành internal package (@garena/admin-layout)
Step 3: Mỗi project: npm install @garena/admin-layout
Step 4: Mỗi project chỉ cần define: routes + logo + title + headerRight
Step 5: Shell consistency tự động — code enforce, không cần review
Step 6: Page-level consistency → vẫn dùng blueprint + Mode B
```

Xem chi tiết implementation tại **references/admin-layout-component.md**.

---

## 3. SHARED LAYOUT TOKEN FILE

Để enforce consistency across projects ở mức code, tạo 1 shared layout config:

```javascript
// shared-layout-tokens.js
// Import file này vào mọi project trong ecosystem

export const LAYOUT = {
  // Shell
  sidebar: {
    width: 200,
    collapsedWidth: 64,
    bg: '#001529',
  },
  header: {
    height: 48,
    bg: '#ffffff',
    borderBottom: '1px solid #f0f0f0',
  },
  content: {
    padding: 16,
    bg: '#f5f5f5',
  },

  // Page patterns
  card: {
    padding: 24,
    borderRadius: 8,
    gap: 16,        // gap giữa cards
  },
  filterBar: {
    marginBottom: 16,
    style: 'inline',  // 'inline' | 'vertical' | 'collapsible'
  },
  table: {
    paginationPosition: 'bottomRight',
    showSizeChanger: true,
    defaultPageSize: 20,
  },

  // Overlays
  modal: {
    small: 416,
    default: 520,
    large: 720,
    xlarge: 1000,
  },
  drawer: {
    default: 600,
    wide: 800,
  },

  // Spacing
  spacing: {
    xs: 4,
    sm: 8,
    md: 16,
    lg: 24,
    xl: 32,
    xxl: 48,
  },
};
```

Mỗi project import file này → dùng `LAYOUT.sidebar.width` thay vì hardcode `200`.
Khi đổi 1 chỗ (ví dụ sidebar width 200 → 220) → tất cả projects update theo.

---

## 4. SYNC CHECKLIST

Khi setup project mới trong ecosystem, verify:

### Shell layer
- [ ] Sidebar type matches source (dark/light, width, collapse behavior)
- [ ] Header height + layout matches
- [ ] Content padding + background matches
- [ ] Logo area same dimensions (khác logo, nhưng cùng size)

### Page patterns layer
- [ ] List page: filter bar position + style matches
- [ ] List page: table pagination style matches
- [ ] List page: primary action button position matches
- [ ] Detail page: header + info + tabs structure matches
- [ ] Form: modal/drawer width matches
- [ ] Form: layout style (vertical/horizontal) matches

### Overlay layer
- [ ] Modal sizes match (small, default, large)
- [ ] Drawer width + placement match
- [ ] Footer button layout match (Cancel + OK alignment)

### Spacing layer
- [ ] Card padding matches
- [ ] Section gaps match
- [ ] Grid gutter matches
- [ ] Filter → table gap matches

### Behavior layer
- [ ] Sidebar collapse behavior matches
- [ ] Responsive breakpoints match
- [ ] Loading states cùng pattern
- [ ] Empty states cùng pattern
- [ ] Error handling cùng pattern

---

## 5. ECOSYSTEM BLUEPRINT

Khi manage nhiều projects, maintain 1 master blueprint:

```
ecosystem-layout/
├── MASTER-BLUEPRINT.md          # Structural rules (shared)
├── shared-layout-tokens.js      # Code-level tokens
└── projects/
    ├── ugc-website.md           # Project-specific overrides
    ├── ads-manager.md           # Project-specific overrides
    └── social-listening.md      # Project-specific overrides
```

Master blueprint chứa structural rules.
Per-project files chỉ chứa content-layer differences (menu, branding, specific page patterns).

### Diff format

```markdown
## UGC Website — Overrides

### Menu structure
- Dashboard
- Creator (Approval Center, Creator Profile, Criteria, Label, Program Config)
- Mission (Create Mission, Manage Mission Post, ...)
- Reward Request
- Shop Config (Gift Code, Redeem, Shop Item, ...)
- Website (Banner Config, Article, Media Library, ...)
- Notification (Admin Notification, User Notification)
- System (Admin, Permission Group, Params, Error Codes)
- UGC Config (Workflow, Registration Config, ...)

### Branding
- Logo: Garena Creator Program
- Accent: #1677ff (blue)
- Sidebar: dark theme (#001529)

### Specific patterns
- Dashboard: Action Center with overdue warnings
- Creator: Card grid with platform-colored headers
- Reward Request: Card grid with status-colored borders
```

---

## 6. VERSIONING

Blueprint nên có version:

```markdown
> Blueprint version: 2.1
> Breaking changes from 2.0: sidebar width 200px → 220px
> Compatible with: UGC Website v3+, Ads Manager v1+
```

Khi update structural rules → tăng minor version.
Khi thay đổi lớn (ví dụ đổi shell type) → tăng major version.

Các project không bắt buộc update ngay, nhưng nên track "đang ở blueprint version nào" để biết gap.
