# UGC-Flavored Example For Outline-Heavy Gap Analysis

Đây là ví dụ tham chiếu để `analyze-gap` hiểu cách một product có Outline tree lớn map sang local code. Ví dụ này chỉ là mẫu đọc, không phải hard dependency.

## Bối cảnh

Project:

- `UGC Website`

Outline anchors thường gặp:

- root: `UGC Website`
- catalog: `11 Canonical — Module Catalog`
- owner pages: `02 Creator`, `03 Mission`, `06 Settings`
- level-2 settings pages:
  - `06.01 Shop Config`
  - `06.02 Notification`
  - `06.03 UGC Config`
  - `06.04 System`

Local code anchors thường gặp:

- `src/routes/appRoutes.jsx`
- `src/components/AdminPageLayout.jsx`
- `src/pages/Creator/*`
- `src/pages/Reward/*`
- `src/pages/Notification/*`
- `src/pages/UGCConfig/*`
- `src/pages/System/*`

## Ví dụ A — `catalog-alignment`

Mục tiêu:

- so catalog với app IA thật

Spec evidence:

- `11 Canonical — Module Catalog`
- phần `Thứ tự canonical`
- phần `Settings Order`

Code evidence:

- `src/routes/appRoutes.jsx`
- `src/components/AdminPageLayout.jsx`

Những gì phải detect:

- `00 Global UI Patterns & Platform` là **shared global pattern**, không phải business route riêng
- `06 Settings` là parent grouping trong spec, nhưng local code đang thể hiện qua settings menu path + grouped route keys
- level-2 settings surfaces map xuống:
  - `06.01 Shop Config` ↔ route `/reward` với label `Shop Config`
  - `06.02 Notification` ↔ route `/notification`
  - `06.03 UGC Config` ↔ route `/ugc-config`
  - `06.04 System` ↔ route `/system`

Điểm dễ miss:

- route technical name và menu label có thể khác nhau
- settings subtree có thể được render theo group chứ không phải parent route độc lập
- shared global patterns không có menu item riêng nhưng vẫn là part of canonical truth

## Ví dụ B — `module-deep-compare` cho Creator

Mục tiêu:

- so owner page / subtree của `02 Creator` với local Creator module

Spec side cần đọc:

- owner page `02 Creator`
- child pages / companion pages mô tả tabs, actions, config, hidden detail flows

Code side anchors:

- `src/pages/Creator/index.jsx`
- `src/pages/Creator/CreatorTabs.jsx`
- `src/pages/Creator/CreatorDrawer.jsx`
- `src/pages/Creator/CreatorModals.jsx`
- `src/pages/Creator/CreatorCard.jsx`

Surface classes phải inventory:

- route
- tabs
- card-launched view
- drawer/modal
- right panel / detail side sheet
- row action / bulk action

Điểm dễ miss:

- file modal tồn tại nhưng chưa chắc được gọi đúng render path
- click card có thể mở drawer/detail side sheet mà không đổi route
- page shell có đủ nhưng hidden surfaces phía sau action buttons còn thiếu

### Lưu ý riêng cho `02.03 Creator Profile`

Trong `Creator Profile`, các surface sau rất dễ bị gắn nhầm thành gap của `02.03`:

- smart filter
- card/table toggle
- selection toolbar
- CSV export
- generic row/card action shell

Nhưng đây trước tiên là `shared list-framework surfaces` đã có owner ở:

- `00.03.01 Shared Filter Surface`
- `00.03.02 Page Top Bar / Right Action Cluster`
- `00.03.03 Table Selection Toolbar / Bulk Actions`
- `00.03.04 Card Action Overflow`

Vì vậy:

- không được kết luận `02.03` còn mỏng chỉ vì page này không restate generic list shell
- phải tách generic shell ra khỏi module-specific action meaning
- chỉ coi là gap của `02.03` nếu action hoặc behavior riêng của profile chưa được mô tả

## Ví dụ C — `module-deep-compare` cho Shop Config

Mục tiêu:

- so `06.01 Shop Config` với local reward domain / shop config surface

Spec side:

- `06.01 Shop Config`
- companion pages nếu có workflow inventory/distribution/history/point log

Code side anchors:

- `src/pages/Reward/index.jsx`
- `src/pages/Reward/rewardShared.js`
- route `/reward` trong `appRoutes.jsx`

Surface classes phải inventory:

- route
- top tabs
- inline expanded state
- row action / bulk action
- modal
- detail/history views

Điểm dễ miss:

- route `/reward` nhưng operator-facing label là `Shop Config`
- top tabs có thể đúng nhưng hidden detail/history surfaces vẫn thiếu
- inline expand kiểu JSON/detail preview là một surface riêng, không được gộp mơ hồ vào “table có đủ”

## Điều ví dụ này muốn nhấn mạnh

- Đừng dừng ở page title hoặc route name.
- Phải map:
  - Outline page role
  - owner/child structure
  - local route
  - hidden UI surfaces
- Nếu subtree sâu mà tool chưa đọc hết:
  - output `unknown / need deeper read`
  - không tự kết luận parity
