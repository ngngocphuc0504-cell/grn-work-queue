---
name: discover-product
description: >
  Skill discovery và planning cho internal tool. Đây là tên mới theo vai trò của skill cũ
  `internal-product-dev`. Skill này sở hữu scope, user flow, module breakdown, và build plan;
  không chọn token/component chi tiết và không viết code.
---

# Discover Product
## Discovery và planning cho web tool nội bộ — Garena ecosystem

---

## PHẠM VI SKILL NÀY

Skill này chỉ xử lý **discovery + scope + plan build** (PM mindset).
Khi cần viết code → kích hoạt **build-frontend** để chọn output mode và build.

| Skill | Trách nhiệm |
|---|---|
| **discover-product** (skill này) | Discovery, Q&A, session plan, module spec, rollout priorities |
| **build-frontend** | Output modes (A/B/C), code conventions, file structure, self-review |
| **design-uiux** | UI decisions, component choice, UX evaluation, feature proposals |
| **sync-task-status** | Feature request status + Build History entries |
| **document-delivery** | Feature specs, changelogs, business docs |

---

## NGUYÊN TẮC CỐT LÕI

1. **Hỏi đúng trước, code sau** — Không bao giờ bắt đầu code khi chưa confirm business logic
2. **Liệt kê impacted areas** — Mỗi khi thêm/sửa feature, chủ động list tất cả điểm liên đới và hỏi confirm trước khi xử lý
3. **Auto-save sau mỗi lần sửa** — Luôn xuất file sau mỗi lần cập nhật, không chờ user hỏi
4. **Lời ưu tiên hơn diagram** — Khi text prompt mâu thuẫn với ảnh/diagram, theo text prompt
5. **Module-first thinking** — Mọi thứ đều build dạng module: bật/tắt được, config được theo game/team/country
6. **Người dùng cuối là thước đo thành công** — Thiết kế phục vụ người dùng thực tế, không phải stakeholder
7. **Less is more** — cắt bớt scope, copy, và UI surface không phục vụ action chính; một màn hình chỉ nên có một mục tiêu nổi bật
8. **Khóa ngôn ngữ chrome sớm** — phải chốt ngay từ discovery: system UI chrome dùng ngôn ngữ nào; mặc định internal tool là English-only

---

## DESIGN SYSTEM OVERVIEW

### Phân loại user & design approach

| User type | Ví dụ | Design approach | Màu sắc |
|---|---|---|---|
| **Internal** | MKT, Ops, Data, Game team | Pure Ant Design 6 foundation + thin business wrappers | Ant Design token palette |
| **External** | Creator, Community leader, Người chơi | Flexible (đề xuất theo context) | Open, theo brand |

### Component Strategy

| Loại component | Dùng gì | Ví dụ |
|---|---|---|
| **Foundation UI** | Ant Design 6 + selective Pro Components | Button, Input, Select, Table, Form, DatePicker, Tabs, Modal, Drawer, ProTable, ProForm, ProDescriptions |
| **Business wrappers** | Thin wrapper trên AntD | PageContainer, FilterBar, QuickFilterPills, EntityStatusTag |

> Chi tiết code implementation của Design Tokens (T, C, S, LAYOUT), AntD-first rules, và khi nào nên dùng Pro Components → xem **build-frontend**

### Layout chuẩn cho internal tool

Vì nhân viên dùng nhiều tool → layout phải **nhất quán** để quen thuộc:

```
┌─────────────────────────────────────────┐
│  [Logo] [Tool Name]    [Search] [User]  │  ← Header cố định
├──────────┬──────────────────────────────┤
│          │  [Breadcrumb]                │
│  Sidebar │  [Page Title] [Actions]      │
│  Menu    │  [Filter Bar]                │
│  (fixed) │  [Content Area]              │
│          │                              │
└──────────┴──────────────────────────────┘
```

- Sidebar: fixed left, collapsible
- Header: fixed top
- Content: scrollable, padding theo design tokens

### Tham khảo UX/UI theo loại tool

Khi bắt đầu build, **đề xuất 2-3 reference cụ thể** và giải thích tại sao phù hợp:

| Loại tool | Reference nên tham khảo |
|---|---|
| Social media management | Sprout Social, Hootsuite, Buffer |
| Ads management | Meta Ads Manager, Google Ads |
| Data dashboard / analytics | Mixpanel, Amplitude, Looker |
| Content / creative management | Notion, Coda, Airtable |
| Task / project management | Asana, ClickUp, Linear |
| Community / creator management | Circle, Mighty Networks |
| Game ops / event config | Jira, custom ops tools |
| CRM / CS platform | Zendesk, Intercom |
| Campaign management | HubSpot, Marketo |

### Actionable Data — Chuẩn hiển thị

Đặc biệt quan trọng với nhóm MKT — dùng thuật ngữ vận hành, không dùng jargon kỹ thuật:

- 🔴 Đỏ (colorError): dưới target / cần xử lý ngay → highlight, đặt lên đầu, có nút action
- 🟡 Vàng (colorWarning): cảnh báo / sắp deadline
- 🟢 Xanh (colorSuccess): đạt target / ổn
- Mỗi metric → có action button đi kèm ngay tại chỗ

---

## PHASE 1: DISCOVERY

### 1.1 Phân tích input đầu vào

Nhận input → xác định ngay:
- **Loại tool**: internal hay external user?
- **Loại input**: text / diagram / ảnh giao diện / file tài liệu
- **Scope**: tool mới hay cải tiến?
- **Kết nối ecosystem**: tool này tương tác với tool nào khác?

### 1.2 Bộ câu hỏi Discovery

**Nhóm A — Bắt buộc hỏi:**
- Ai dùng tool này? (role, team, internal/external)
- Luồng chính: họ vào tool để làm gì, theo thứ tự nào?
- Action quan trọng nhất họ cần làm được là gì?
- Data đến từ đâu? (API / nhập tay / import / DB)
- Có multi-role/permission không?
- System UI chrome dùng ngôn ngữ nào? Nếu không có yêu cầu khác, mặc định là English-only
- Content có được phép multilingual không, hay cũng phải English-only?

**Nhóm B — Hỏi nếu chưa rõ:**
- Có rule logic theo country/game/team không?
- Metrics nào là nội bộ/nhạy cảm?
- Cần module nào từ Standard Module Library?
- Có target/threshold để hiển thị màu cảnh báo không?

**Nhóm C — Để cuối, hỏi khi gần xong:**
- Cần tài liệu đi kèm không?
- Nếu có i18n thật sự, phạm vi là content layer hay cả system UI chrome?

### 1.3 Tóm tắt + Session Plan trước khi code

```
## Tôi hiểu như sau:
- Tool: [tên] phục vụ [đối tượng — internal/external]
- UI chrome language: [English mặc định hoặc override đã chốt]
- Content language policy: [source language allowed / English-only / mixed by module]
- Reference UX nên tham khảo: [Tool A] vì [lý do], [Tool B] vì [lý do]
- Luồng chính: [A → B → C]
- Users & roles: [role 1] → [action], [role 2] → [action]
- Data source: [nguồn]
- Modules cần dùng: [list từ Standard Library]
- Config theo: [country / game / team]
- Actionable metrics: [list với màu cảnh báo]

## Session plan:
- Session 1: [Layout + Navigation + Module X]
- Session 2: [Core feature Y]
- Session 3: [Feature Z + Polish + locale verification]

Confirm không? Tôi sẽ bắt đầu Session 1.
```

**Không code cho đến khi user confirm.**

---

## PHASE 2: BUILD

### 2.1 Thứ tự build trong 1 session

1. Layout & navigation (sidebar, header, breadcrumb)
2. Standard modules cần thiết (từ library)
3. Core business logic của feature
4. Mock data với đúng field name thực tế
5. Empty state / loading / error handling
6. **→ Chuyển sang Code Agent để chọn output mode và xuất file**

### 2.2 Impacted Areas Check

Mỗi khi thêm/sửa bất kỳ feature nào, **bắt buộc** chạy checklist và báo cho user:

```
Ví dụ: Thêm "filter theo country"
→ Các điểm có thể bị ảnh hưởng:
  □ Permission: user có bị giới hạn theo country không?
  □ Data display: các table/card khác có cần filter theo country không?
  □ Export: file export có cần thêm cột country không?
  □ Config: country list lấy từ đâu?
  □ Default filter: country mặc định là gì?
  □ Saved views: view đã save có bị ảnh hưởng không?
Thêm tất cả hay chỉ một số?
```

Luôn **liệt kê hết rồi hỏi confirm** — không tự xử lý ngầm.

### 2.3 Module hóa — props-driven

```jsx
// ✅ Đúng: behavior qua props
<DataTable
  filterByCountry={true}
  allowExport={hasPermission('export')}
  frozenColumns={['name', 'status']}
/>

// ❌ Sai: hardcode behavior
<DataTable /> // với logic country hardcode bên trong
```

---

## PHASE 3: STANDARD MODULE LIBRARY

> Các module lặp đi lặp lại — build nhất quán qua tất cả tool.
> Chi tiết implementation: `components/standard-modules.md`

### Navigation & Layout
- `AppLayout` — Sidebar + Header + Content
- `SidebarMenu` — Collapsible, active state, icon, badge số thông báo
- `LanguageSwitcher` — chỉ dùng khi product contract thật sự yêu cầu multilingual system UI; không coi là default module

### Data Display
- `DataTable` — Bảng dữ liệu: freeze cột, sort/filter, ẩn/hiện cột, full-screen mode
- `CardView` / `TableView` — Toggle giữa 2 chế độ xem
- `MetricCard` — KPI card với màu đỏ/vàng/xanh theo target
- `ActionableSummary` — Danh sách việc cần làm: badge đỏ + nút action ngay

### Filter & Search
- `GlobalSearch` — Thanh tìm kiếm toàn trang
- `FilterBar` — Combo: country, game, date range, status, team
- `DefaultFilter` — Auto-apply khi vào trang
- `SavedViews` — Lưu bộ filter hiện tại để truy cập nhanh

### Export & Import
- `ExportButton` — Tải CSV/Excel với filter hiện tại
- `ImportPanel` — Upload → validate → preview → confirm

### Access & Permission
- `PermissionGate` — Wrapper: hiện/ẩn theo role/action
- `AccessManager` — Quản lý quyền theo action granular

### Workflow & Notification
- `WorkflowTracker` — Trạng thái quy trình (pending → review → approved)
- `NotificationCenter` — Bell icon + panel thông báo
- `AlertBadge` — Badge đỏ số lượng cần xử lý

---

## PHASE 4: DOCUMENTATION

Chỉ tạo khi user yêu cầu. Hỏi sau khi build xong.

| Tài liệu | Audience | Ngôn ngữ |
|---|---|---|
| User Guide | End user | VI, tránh jargon kỹ thuật |
| Tech Spec | Dev team | VI/EN |
| QA Checklist | QA / PM | VI |
| Changelog | All stakeholders | VI |

Chi tiết format: xem `references/` folder.
Khi cần viết doc → kích hoạt **document-delivery**.

---

## PHASE 5: ITERATION

1. **UI tweak** → sửa trực tiếp + xuất file
2. **Logic thay đổi** → chạy Impacted Areas Check trước
3. **Scope mở rộng** → mini-discovery cho feature mới
4. Không xóa tính năng cũ trừ khi user nói rõ
5. Giữ nguyên mock data structure và module architecture
6. **Luôn xuất file sau mỗi lần sửa**

---

## CHECKLIST TRƯỚC KHI DELIVER

- [ ] Đã confirm business logic với user?
- [ ] Đề xuất reference tool UX phù hợp?
- [ ] Đề xuất session plan cho dự án phức tạp?
- [ ] Layout nhất quán (sidebar + header cố định)?
- [ ] Actionable metrics có màu đỏ/vàng/xanh + action button?
- [ ] Modules props-driven, không hardcode behavior?
- [ ] Mock data dùng field name thực tế?
- [ ] TODO comments đánh dấu đúng chỗ cần API?
- [ ] i18n comments để sẵn (chưa implement)?
- [ ] Impacted Areas Check đã chạy cho mọi thay đổi?
- [ ] File đã xuất và present cho user?

---

## NAVIGATION IA ADDENDUM

Ap dung cho moi internal tool, dac biet khi de xuat menu bar, sidebar, app shell navigation:

- Navigation phai duoc quyet dinh theo `workflow` cua nguoi dung, khong theo repo structure, route count, hay module ky thuat.
- Top-level nav la tai nguyen hiem: chi cap cho daily jobs va workspaces can quay lai thuong xuyen.
- Admin/config/integration/permission/system pages mac dinh phai duoc group duoi node cha nhu `Settings` hoac `Admin`, khong flatten vao sidebar neu khong co ly do product ro rang.
- `Create` / `New` flows mac dinh la CTA trong workspace owner page, khong phai menu item thuong truc, tru khi flow do la mot workspace doc lap co tan suat su dung cao.
- Trong discovery summary, phai ghi ro 4 thu:
  - `Navigation model`: workflow-first / flat / admin-forward
  - `Top-level nav`
  - `Grouped nav`
  - `CTA-only flows`
- Neu task co lien quan den navigation, bo cau hoi discovery phai cover them:
  - page nao la `daily-use workspace`
  - page nao la `config/admin`
  - flow nao chi nen la CTA
  - thu tu uu tien menu can phan anh workflow nao
