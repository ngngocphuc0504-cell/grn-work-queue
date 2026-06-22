---
name: analyze-gap
description: >
  Skill phân tích chênh lệch source → target cho migration, rebuild, hoặc đối chiếu codebase với specs
  trong Outline. Dùng khi cần so sánh hai bản code/project, catalog module với UI thật, hoặc một
  module owner page với local code để tìm phần còn thiếu và xuất report handoff rõ ràng.
---

# Analyze Gap

Phân tích chênh lệch giữa **source of truth** và **target implementation**, rồi bàn giao danh sách fix sang `build-frontend` hoặc skill triển khai phù hợp.

Skill này phải ưu tiên:

- evidence hơn assumption
- đọc đúng boundary trước khi so sánh
- chia nhỏ theo checkpoint khi scope lớn
- so sánh theo **UI surfaces thực tế**, không chỉ theo page/sub-page
- tách rõ `shared shell`, `business summary`, và `deep detail owner` trước khi kết luận gap

## Khi nào dùng

Skill này xử lý 4 nhóm việc chính:

1. **Migration / rebuild**
   - So sánh source code gốc với bản migration hoặc rebuild.
2. **Catalog alignment**
   - So sánh module catalog / owner tree trong Outline với IA thật của website hoặc app shell.
3. **Module deep compare**
   - So sánh một module owner page trong Outline với local code của module đó.
4. **Re-verify after fix**
   - Chạy lại cùng matrix sau khi fix để cập nhật trạng thái còn thiếu / đã khớp.

## Mặc định đầu vào

Khi nhận task, phải tự chuẩn hóa scope thành 4 ý sau:

- **Target project / module** là gì
- **Spec truth** nằm ở đâu
  - Outline root
  - module catalog
  - owner page
  - subtree cụ thể
- **Local code target** là folder / route / page / component nào
- **Comparison mode** là gì
  - `catalog-alignment`
  - `module-deep-compare`
  - `re-verify-after-fix`

### Auto-defaults

- Nếu user đưa **Outline link** hoặc nhắc `Outline` / `wiki.odp.garena.vn`:
  - mặc định bật **Outline mode**
- Nếu scope có dấu hiệu lớn:
  - nhiều module
  - module có nhiều child pages
  - tree nhiều level
  - codebase nhiều routes / many files
  - mặc định chạy **phased checkpoints**
- Nếu user chỉ nói chung chung “so local code với specs”:
  - mặc định ưu tiên `module-deep-compare`
  - chỉ dùng `catalog-alignment` nếu source chính là catalog / IA page

## Run Modes

## 1. `catalog-alignment`

Dùng khi cần đối chiếu:

- module catalog trong Outline
- owner tree / settings order / canonical order
- live website IA
- sidebar / routes / shell-level navigation

Mục tiêu:

- tìm module thiếu
- tìm module thừa / rename drift
- phát hiện level-2 module chưa được map
- phát hiện shared patterns không nên bị nhầm thành module độc lập

Output chính:

- `Catalog Alignment Matrix`
- danh sách mismatch theo navigation / owner page / route / shared pattern

## 2. `module-deep-compare`

Dùng khi cần đối chiếu:

- một owner page trong Outline
- descendants của owner page đó
- local route / page / module code tương ứng

Mục tiêu:

- bóc đúng toàn bộ UI surfaces của module
- phát hiện hidden surfaces như drawer, modal, right panel, row action
- phân biệt `missing`, `stub`, `partial`, `unknown`, `match`

Output chính:

- `Module Surface Inventory`
- `Detailed Diff Matrix`
- `Fix Backlog`

## 3. `re-verify-after-fix`

Dùng sau khi code đã được sửa.

Mục tiêu:

- dùng lại cùng scope, cùng matrix, cùng taxonomy
- cập nhật status thay vì viết lại report từ đầu
- giữ continuity giữa trước và sau fix

Output chính:

- matrix đã cập nhật
- phần còn hở
- phần đã match có evidence mới

## Workflow Bắt Buộc

Không được nhảy thẳng vào compare nếu chưa xong phase trước.

## Phase 1 — Boundary + owner route

Mục tiêu:

- xác định đúng source of truth
- xác định đúng local code anchor
- xác định đúng mode

Phải làm:

- resolve project root / module root
- nếu có Outline:
  - xác định page được đưa vào là root, catalog, owner page, hay chỉ là companion page
- xác định local code anchors:
  - route map
  - page entry
  - app shell / sidebar
  - module folder
- check xem đã có report cũ chưa

Stop rule:

- chưa rõ owner page hoặc local anchor thì **không compare**
- phải dừng ở `unknown / need owner route`

Checkpoint output:

- scope ngắn
- mode đã chọn
- spec anchor
- code anchor
- phần chưa rõ nếu có

## Phase 2 — Spec subtree inventory

Mục tiêu:

- inventory đầy đủ surfaces được mô tả trong spec subtree

Phải đọc:

- owner page
- child pages liên quan trực tiếp
- level-2 descendants nếu owner page hoặc child page nói rằng có deeper rules
- linked companion pages nếu chính owner page bảo phải đọc tiếp

Phải inventory:

- headings
- module sections
- child pages
- level-2 descendants
- tables / matrices / workflow steps
- secondary surfaces mô tả trong prose
  - `Add new`
  - click card
  - row click
  - action menu
  - right panel
  - detail side sheet
  - modal / drawer
  - inline expanded state

Rule:

- module catalog page chỉ được coi là **routing/index page**, không mặc định là detailed truth
- nếu spec chỉ gợi ý surface nhưng chưa đọc đến section exact:
  - status = `unknown`
  - không được tự kết luận `match` hay `missing`

Stop rule:

- nếu subtree còn page quan trọng chưa đọc mà surface phụ thuộc page đó:
  - đưa vào `Open Unknowns / Need More Read`

Checkpoint output:

- `Spec Surface Inventory`
- danh sách page đã đọc
- danh sách page/surface còn `unknown`

## Phase 3 — Code surface inventory

Mục tiêu:

- inventory UI surfaces thật đang tồn tại trong code

Phải scan:

- route/page entry
- imported sub-components
- conditional render branches
- tab definitions
- card click handlers
- row action handlers
- modal / drawer imports
- right panel / detail side sheet
- inline expand / collapse states
- bulk actions
- shared global patterns

Phải verify render path:

- component có tồn tại không đủ; phải check nó có **được gọi thật** hay không
- import nhưng không render = orphan / dead path
- inline stub ở entry file có thể đang override full component ở file khác

Phải inventory theo surface, không chỉ theo file:

- route
- section
- tab
- row/card summary surface
- card-launched view
- drawer/modal
- right panel / detail side sheet
- inline expanded state
- row action / bulk action
- shared global pattern

Stop rule:

- nếu chưa trace được render path từ entry file đến surface:
  - đánh `unknown render path`
  - không tự nâng thành `match`

Checkpoint output:

- `Code Surface Inventory`
- evidence file/path cho từng surface

## Phase 4 — Surface matching

Mục tiêu:

- so sánh spec surfaces với code surfaces bằng evidence hai phía

Với mỗi surface trong spec inventory:

1. Tìm counterpart trong code inventory
2. So evidence:
   - spec evidence: page / section / table / workflow / prose
   - code evidence: route / file / render branch / interaction entry point
   - shared-owner evidence: shared-platform page hoặc global pattern page đã sở hữu surface đó hay chưa
3. Đánh status:
   - `match`
   - `partial`
   - `stub`
   - `missing`
   - `unknown`

### Shared-owner cross-check bắt buộc

Trước khi kết luận một module page `partial` hoặc `missing`, phải check xem surface đó có đã được sở hữu bởi shared-platform subtree hay chưa.

Áp dụng đặc biệt cho các surface thường được đóng gói reusable contract:

- shared filter surface
- page-top action cluster
- card/table toggle
- selection toolbar
- bulk action shell
- CSV/export affordance
- drawer/modal shell
- right-panel shell

Rule:

- Nếu module subtree không mô tả chi tiết các surface trên, nhưng chúng đã có owner page rồi trong `00 Global UI Patterns & Platform` hoặc subtree shared-platform tương đương:
  - không được coi đó là gap của module page chưa đủ
  - phải ghi chú `covered by shared-platform owner`
  - module compare chỉ tiếp tục đánh giá phần `module-specific delta`
- Chỉ mark `partial` hoặc `missing` ở module page nếu:
  - module có hành vi riêng vượt ra khỏi shared contract
  - hoặc boundary của module page buộc phải giữ rule riêng cho surface đó
- Nếu chưa verify được shared-owner page:
  - mark `unknown shared ownership`
  - không đẩy thành backlog của module

### Business-summary salvage bắt buộc

Sau khi một surface được xác nhận là `covered by shared-platform owner`, không được dừng ở kết luận “module không còn gap”.

Phải chạy thêm một bước để trả lời:

1. shared shell nào đã được owner ở page khác
2. business meaning nào vẫn phải được giữ ở page hiện tại
3. detail nào phải route sang child page hoặc deep surface khác

Áp dụng đặc biệt cho:

- row/card summary surface
- card-level status signals
- row/card action semantics
- click target mở drawer / modal / detail panel
- module-specific CTA ý nghĩa riêng nhưng đang reuse shared shell

Rule:

- shared shell có owner riêng không đồng nghĩa page hiện tại được bỏ qua hoàn toàn phần card/row
- nếu operator ra quyết định ở level row/card, page owner vẫn phải giữ:
  - nhóm thông tin cần thấy ở row/card
  - ý nghĩa nghiệp vụ của từng action chính ở row/card
  - action nào chỉ là entry point sang child page
- chỉ được bỏ qua một surface ở page owner khi:
  - nó là shared chrome thuần túy
  - và không mang business signal riêng của module

Khi emit matrix, với các surface liên quan đến row/card/action phải ghi rõ:

- `shared owner`
- `business summary owner`
- `deep detail owner`

Ngoài ownership, phải ghi thêm:

- `exact displayed data`
- `action buttons present`

Rule chi tiết cho row/card/list surfaces:

- nếu UI đã hiện field/label cụ thể, không được chỉ ghi abstract grouping như `định danh`, `trạng thái hồ sơ`, `tín hiệu compliance`
- phải gọi tên field hoặc label thật đang hiện trên UI, ví dụ:
  - `Channel Name`
  - `Channel Link`
  - `Profile Status`
  - `Approval Status`
- với mỗi field hoặc label thật, phải ghi ngắn gọn field đó giúp operator xác nhận hay quyết định điều gì
- với mỗi action button đang có thật trên row/card, phải ghi rõ ý nghĩa của action đó

Khi emit matrix hoặc gap summary cho owner page có row/card/list surface, không đủ nếu chỉ nói:

- `nhóm thông tin cần có`
- `action semantics còn mỏng`

Phải emit tối thiểu:

- row/card đang hiển thị chính xác data nào
- data nào còn thiếu trong spec owner page
- button/action nào còn thiếu meaning trong spec owner page

Nếu page hiện tại còn thiếu phần `business summary owner`:

- không được kết luận `match`
- phải đánh `partial` hoặc `append needed` tùy output mode

Nếu page Outline đã có content meaningful và gap chỉ là cách trình bày/merge nội dung:

- emit thêm patch disposition cho từng item:
  - `keep as-is`
  - `rewrite into main body`
  - `log only in update history`
- không đề xuất giữ content business ở một block cập nhật tách rời nếu intent thật là chuẩn hóa body chính

### Hard anti-assumption rules

- Không bao giờ mark `match` nếu không có:
  - **spec evidence**
  - **code evidence**
- Nếu spec mới hint surface nhưng chưa có exact section:
  - mark `unknown`
- Nếu code có component nhưng chưa trace được render path:
  - mark `unknown` hoặc `orphaned`, không mark `match`
- Nếu target chỉ đúng page shell nhưng thiếu hidden surfaces:
  - không mark page-level `match`
- Nếu module catalog và owner page conflict:
  - owner page thắng
- Nếu Outline / connector không đủ visibility:
  - ghi rõ `needs deeper read`

## Phase 5 — Gap report

Mục tiêu:

- output ngắn, có structure, ưu tiên matrix và action backlog

Report mặc định phải có:

- scope confirmation ngắn
- phase checkpoint summaries
- evidence-based diff matrix
- `Open Unknowns / Need More Read`
- prioritized `Fix Backlog`

Không default xuất essay dài.

### Doc-safe output cho spec update

Khi output này sẽ được dùng để sửa docs hoặc Outline pages, phải thêm một lớp phân loại edit scope.

Mỗi section hoặc candidate change phải được gắn đúng một nhãn:

- `keep`
- `fix`
- `append`
- `new child page needed`

Rule bắt buộc:

- nếu Outline đã có spec, chỉ recommend patch theo section;
- không recommend overwrite toàn page;
- section đang đúng phải giữ là `keep`, không kéo vào backlog chỉ vì khác template;
- nếu page cha đang bị quá dày, ưu tiên `new child page needed` thay vì nhồi thêm prose.

## UI Surface Taxonomy

Đây là taxonomy bắt buộc. Không tự co hẹp thành page/sub-page.

| Surface class | Định nghĩa ngắn | Trigger thường gặp |
|---|---|---|
| `route` | Màn hình có route hoặc menu entry riêng | sidebar click, direct URL |
| `section` | Khối chức năng nằm trong 1 page | scroll section, block title |
| `tab` | View chuyển bằng tab key | tab click, segmented control |
| `card-launched view` | Surface mở ra sau khi click card/tile | card click |
| `drawer/modal` | Overlay dạng drawer, modal, popup | add, edit, quick action |
| `right panel / detail side sheet` | Panel chi tiết bên phải | row click, item click |
| `inline expanded state` | Nội dung mở rộng trong cùng page/list | expand row, show more |
| `row action / bulk action` | Hành động trên item/table selection | kebab menu, action bar |
| `shared global pattern` | Pattern cross-module ở app shell | global search, toolbar, filters |

## Detection Checklist Bắt Buộc

Khi scope là UI/module, phải scan ít nhất các trigger sau:

- `Add new`
- `Create`
- `Edit`
- `View detail`
- card click
- table row click
- row action menu
- bulk action bar
- filter chip / smart filter
- side drawer
- right panel
- modal launcher
- empty state CTA
- error/retry CTA

Nếu không scan nhóm trigger này thì chưa đủ điều kiện kết luận “module đã cover đủ”.

## Severity Và Status

### Status

- `match`
  - spec và code khớp, có evidence 2 phía
- `partial`
  - có surface tương ứng nhưng thiếu một phần behavior hoặc content
- `stub`
  - có surface nhưng quá mỏng, chỉ là placeholder hoặc simplified shell
- `missing`
  - spec có surface nhưng code chưa có counterpart
- `unknown`
  - chưa đủ evidence hoặc chưa đọc tới đúng subtree / render path

### Severity

- `critical`
  - thiếu route, core tab, primary workflow, hoặc hidden surface bắt buộc của flow chính
- `medium`
  - có frame nhưng thiếu behavior, action, data view, panel phụ quan trọng
- `minor`
  - naming drift, label drift, formatting drift, shared pattern mismatch nhỏ

## Output Format

Ưu tiên dùng templates trong `references/output-templates.md`.

Output tối thiểu:

1. scope confirmation
2. phase summary ngắn
3. matrix chính
4. unknowns
5. backlog

## Outline Mode Rules

Khi dùng Outline mode:

- ưu tiên gateway-exposed Outline tools thay vì browse web UI
- coi tên operation trong các skill Outline là logical operations; resolve exact callable tool ids từ tool surface hiện tại
- inventory theo subtree, không đọc lan sang sibling branches nếu chưa cần
- chỉ follow companion pages khi owner page bảo phải đọc tiếp
- nếu tool visibility không đủ để xác nhận subtree:
  - ghi rõ limitation
  - đẩy sang `unknown / needs deeper read`

Đọc thêm:

- [outline-read-scope.md](./references/outline-read-scope.md)
- [ui-surface-taxonomy.md](./references/ui-surface-taxonomy.md)
- [output-templates.md](./references/output-templates.md)
- [ugc-outline-example.md](./references/ugc-outline-example.md)

## Catalog Alignment Rules

Khi chạy `catalog-alignment`, phải kiểm tra:

- canonical order
- module owner mapping
- settings decomposition / level-2 structure
- route vs menu label drift
- shared UI/platform page không bị nhầm thành business module

Các mismatch thường gặp:

- module có trong catalog nhưng chưa có route/menu
- route/menu có nhưng chưa có owner page hoặc naming drift
- settings subtree có level-2 items trong Outline nhưng local app chỉ flatten
- shared global pattern nằm trong Outline nhưng code lại rải rác không được nhận diện

## Module Deep Compare Rules

Khi chạy `module-deep-compare`, phải bóc ít nhất:

- route/page shell
- tabs / segmented views
- primary table/list/cards
- hidden overlays
- detail panels
- row actions / bulk actions
- shared filter / toolbar / search patterns

Sau khi inventory xong, phải tách 2 nhóm:

- `shared-platform reused surfaces`
- `module-specific surfaces`

Không được gộp chung hai nhóm này rồi kết luận module page “còn mỏng”.

Với các surface kiểu list shell như filter, card/table toggle, selection, export, toolbar:

- check subtree `00` trước
- nếu đã có shared owner, module page chỉ cần nói phần module-specific action hoặc data contract
- phần generic shell không phải backlog của module

Không được dừng ở:

- “page này có tồn tại”
- “component này có file”
- “tab name giống”

Phải trả lời được:

- surface nào spec có mà code chưa có
- surface nào code có nhưng chưa trace được về spec
- surface nào mới chỉ là stub

## Re-verify After Fix

Khi chạy lại sau fix:

- reuse scope cũ
- giữ nguyên taxonomy cũ
- update matrix cũ theo status mới
- đánh dấu rõ:
  - `resolved`
  - `still open`
  - `unknown pending deeper read`

## Handoff sang skill triển khai

Sau khi gap report xong, không tự nhảy sang implement nếu user chưa yêu cầu.

Handoff phải gồm:

- surface / gap name
- severity
- spec evidence
- code evidence
- target file hoặc route
- hướng fix ngắn
- risk / unknown nếu còn

## Guardrails cuối

- Không để output quá dài rồi tự assume nốt phần chưa đọc.
- Scope lớn thì checkpoint sớm, không one-pass.
- Khi thiếu visibility, nói `unknown`.
- Khi cần xuống level sâu hơn, follow subtree thay vì phỏng đoán từ page title.
