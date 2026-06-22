# UI Surface Taxonomy And Detection Checklist

`analyze-gap` phải inventory theo **surface**, không chỉ theo page/file/component.

## Surface Classes

## 1. `route`

Dấu hiệu:

- có path riêng
- có menu item / sidebar item
- có breadcrumb riêng

Ví dụ:

- `/creator`
- `/reward`
- `/system`

## 2. `section`

Dấu hiệu:

- block lớn trong một route
- heading / card group / split layout
- không cần tab key riêng

Ví dụ:

- summary block
- metrics block
- settings cluster

## 3. `tab`

Dấu hiệu:

- tab strip
- segmented control
- switching state kiểu `activeTab`

Ví dụ:

- review tab
- profile tab
- config tab

## 4. `card-launched view`

Dấu hiệu:

- click card mở view khác nhưng không đổi route
- click tile mở drawer / detail / nested state

Ví dụ:

- click creator card mở detail drawer
- click dashboard card mở filtered surface

## 5. `drawer/modal`

Dấu hiệu:

- overlay
- state open/close
- add/edit/create/approve flow

Ví dụ:

- create modal
- edit drawer
- reject modal

## 6. `right panel / detail side sheet`

Dấu hiệu:

- panel bên phải
- record detail mở từ click row/item
- không hẳn là modal overlay full

Ví dụ:

- side sheet xem detail creator
- right panel xem config detail

## 7. `inline expanded state`

Dấu hiệu:

- row expand
- accordion
- show more / details inline

Ví dụ:

- expand JSON preview
- expanded audit row

## 8. `row action / bulk action`

Dấu hiệu:

- action menu trên row
- selection toolbar
- multi-select batch actions

Ví dụ:

- edit / delete / approve per row
- bulk approve / export

## 9. `shared global pattern`

Dấu hiệu:

- dùng xuyên nhiều module
- thuộc app shell / platform layer

Ví dụ:

- global search
- common filter surface
- shared toolbar contract

## Detection Checklist

Khi inventory code hoặc specs, phải scan ít nhất các trigger dưới đây:

- `Add new`
- `Create`
- `Edit`
- `Delete`
- `Approve`
- `Reject`
- `View detail`
- card click
- table row click
- row action menu
- bulk selection
- filter chip
- smart filter
- toolbar CTA
- empty state CTA
- retry CTA
- side drawer
- modal launcher
- right panel
- expand/collapse

## Evidence Requirements

Mỗi surface phải có 2 loại evidence nếu muốn mark `match`:

- **Spec evidence**
  - page title
  - heading
  - section wording
  - workflow steps
  - matrix / table row
- **Code evidence**
  - route key/path
  - file path
  - render branch
  - handler / trigger
  - imported overlay component

## Stub Heuristics

Surface nên bị mark `stub` nếu có nhiều dấu hiệu sau:

- có surface name nhưng content cực mỏng
- có modal/drawer shell nhưng thiếu field/action chính
- có tab name nhưng tab content chỉ là placeholder
- có detail panel nhưng chỉ hiện vài field cơ bản trong khi spec mô tả sâu
- có list/table nhưng thiếu row actions hoặc hidden surfaces liên quan

## Unknown Heuristics

Mark `unknown` nếu:

- spec hint surface nhưng chưa đọc exact section
- code có file nhưng chưa trace render path
- tool visibility không cho thấy child page / deeper subtree
- interaction entry point có vẻ tồn tại nhưng chưa xác nhận được open state
