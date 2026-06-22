---
name: write-specs
description: Viết và cập nhật spec cho internal tool theo kiểu Outline-first, tập trung vào mô tả tính năng cho PM, FE, BE, QA và update an toàn theo từng section.
---

# Write Specs

Skill này dùng để viết hoặc cập nhật spec dev-facing cho internal tool.

Mục tiêu chính:

- viết spec rõ boundary, dễ đọc với PM nhưng vẫn đủ hữu dụng cho FE, BE, QA;
- dùng Outline làm đích viết mặc định khi project đang dùng `wiki.odp.garena.vn`;
- update page hiện có theo `section-level patch`, không overwrite toàn trang;
- luôn ghi log ở cuối page sau mỗi lần chỉnh sửa.

## Trigger map

- `write specs`, `viet specs`, `write spec`, `viet spec`
- `module spec`, `feature spec`, `canonical page`
- `owner page`, `module owner page`
- `update spec`, `cap nhat spec`, `chinh sua spec`
- `codebase to outline sync`, `sync spec voi codebase`

## Audience và target mặc định

- Audience mặc định: `PM`, `FE`, `BE`, `QA`
- Target mặc định: `Outline-first`
- Nếu project có subtree docs sẵn, phải khóa style theo chính subtree đó trước khi viết

## Language policy bắt buộc

- Viết spec bằng tiếng Việt theo mặc định.
- Chỉ giữ tiếng Anh cho:
  - thuật ngữ chuyên môn đã quen dùng trong team hoặc trong UI/codebase
  - danh từ riêng, tên page, tên module, tên component, tên field, tên API, và tên sản phẩm/hệ thống
- Không được viết cả page theo văn phong tiếng Anh chỉ vì codebase hoặc Outline đang có nhiều label tiếng Anh.
- Nếu page đang có sẵn heading hoặc label tiếng Anh là local convention của subtree, giữ nguyên phần tên riêng đó nhưng phần mô tả, rule, flow, note, và change log vẫn phải viết bằng tiếng Việt.

## Writing style bắt buộc

- Viết theo thứ tự ưu tiên:
  1. business purpose
  2. khi nào dùng / khi nào xuất hiện
  3. ảnh hưởng tới decision, action, hoặc downstream flow
  4. boundary với page khác
  5. implementation note ngắn nếu thật sự cần
- Không được viết section theo kiểu kể lại code đang render gì, field nào đang tồn tại, scaffold nào đang có, hay hook nào đang được gọi, trừ khi chi tiết đó thật sự là business rule cần giữ.
- Code chỉ là evidence để xác nhận spec. Không dùng code làm giọng văn mặc định của spec.
- Nếu một section chỉ là một phần nhỏ trong module/page, ưu tiên viết ngắn, đủ cho PM, FE, BE, QA hiểu intent và behavior thay vì mở rộng thành mô tả dài dòng.
- Chỉ viết dài khi phần đó thật sự là một surface có ownership riêng, nhiều state/action riêng, hoặc sẽ được dùng lại như reference ở nhiều page/module khác.
- Không hiểu nhầm `viết ngắn` thành bỏ qua business summary của row/card/action ở page owner. Nếu operator cần nhìn một card/row để quyết định nhanh, page owner vẫn phải nói rõ card/row đó dùng để làm gì.
- Khi UI đã thể hiện field hoặc label cụ thể, phải ưu tiên gọi đúng tên field/label đang hiển thị thay vì dùng danh từ trừu tượng. Ví dụ:
  - không viết `định danh creator` nếu UI thực tế đang dùng `Channel Name` và `Channel Link`
  - không viết `trạng thái hồ sơ` nếu UI thực tế đang dùng `Profile Status` và `Approval Status`
- Khi section mô tả row/card/list surface, phải tách rõ:
  - `exact displayed data`: field hoặc label nào đang hiện trên UI
  - `business meaning`: từng field đó giúp operator quyết định gì
  - `action meaning`: từng button/action thật đang có trên UI dùng để làm gì
- Không được dừng ở mức “nhóm thông tin cần có” nếu code/UI đã đủ rõ để gọi ra field thật.
- Không append section kiểu `Cập nhật YYYY-MM-DD` để chứa content business lâu dài. Nội dung business đã duyệt phải được merge vào body chính của page.
- `Lịch sử cập nhật` hoặc `Change Log` chỉ được dùng để ghi tóm tắt:
  - ngày
  - phạm vi thay đổi ngắn
  - lý do ngắn
  - source checked ngắn nếu subtree cần

## Out of scope

Skill này không viết:

- `user guide`
- `operator guide`
- runbook
- changelog-only page
- session note
- handoff note
- data schema / payload / contract chi tiết

Nếu user cần một trong các loại trên, route sang skill khác phù hợp thay vì cố nhồi vào spec.

## Modes

### 1. `create-new-spec`

Dùng khi page target chưa có spec hoặc chỉ có placeholder quá mỏng.

Kết quả mong muốn:

- tạo khung spec mới đúng page role;
- bám local convention của subtree nếu có;
- thêm log entry đầu tiên ở cuối page.

### 2. `refine-existing-spec`

Dùng khi page đã có nội dung và chỉ cần sửa phần sai, cập nhật phần cũ, hoặc thêm section còn thiếu.

Kết quả mong muốn:

- giữ nguyên section đang đúng;
- chỉ vá section sai hoặc thiếu;
- append log ở cuối page.

### 3. `expand-owner-into-child-pages`

Dùng khi module owner page đã quá dày hoặc module có tab / sub-surface đủ lớn để tách riêng.

Kết quả mong muốn:

- owner page giữ vai trò hub + boundary;
- child pages đi sâu vào từng tab / sub-surface;
- không lặp lại toàn bộ module cha trong child page.

### 4. `codebase-to-outline-sync`

Dùng khi cần đọc codebase local và gap-analysis với Outline để sửa spec.

Kết quả mong muốn:

- xác định page nào `keep`, `fix`, `append`, hoặc `new child page needed`;
- nếu Outline đã có spec, chỉ patch theo section;
- log rõ source đã verify trong change log cuối page.
- nếu một section chưa đủ sâu để tách child page, viết lại nó theo kiểu business-first và ngắn gọn thay vì kể lại code.

## Page-role taxonomy

Chỉ dùng 5 role sau trong skill này:

- `catalog`
- `navigation-group`
- `shared-platform`
- `module-owner`
- `child-spec`

Đọc định nghĩa chi tiết tại:

- [spec-taxonomy.md](./references/spec-taxonomy.md)
- [section-templates.md](./references/section-templates.md)

## Framework mặc định theo page role

### `catalog`

- metadata block
- `Tổng quan`
- `Reading Order` hoặc `Module Map`
- `Boundary`

### `navigation-group`

- metadata block
- `Tổng quan`
- `Thứ tự menu`
- `Boundary`

### `shared-platform`

- metadata block
- `Reading Order`
- `Boundary Rule`
- `Global Surfaces Covered`
- `Update Trigger`

### `module-owner`

- metadata block
- `Tổng quan`
- `Scope / Boundary`
- `Reading Order` hoặc `Main Surfaces`
- `Luồng chính`
- `Roles / permissions` nếu có
- `States / actions / triggers`
- `Data touchpoints`
- `Upstream / downstream`
- `Edge cases / non-goals`
- `Companion pages`

### `child-spec`

- chỉ đi sâu vào đúng tab / sub-surface
- không lặp lại toàn module cha

## Quyết định độ sâu trước khi viết

Trước khi mở rộng bất kỳ section hay sub-surface nào, phải chốt một trong hai hướng:

### Hướng 1. `new child page needed`

Chỉ chọn khi phần đó:

- có business rule riêng đủ sâu;
- có nhiều state, action, hoặc edge case độc lập;
- có khả năng được tham chiếu lại từ nhiều page/module khác;
- hoặc nếu nhồi tiếp vào page hiện tại sẽ làm owner page mất boundary và khó đọc.

### Hướng 2. `write enough here`

Chọn khi phần đó:

- chỉ là một phần trong module/page hiện tại;
- chưa đủ sâu để thành một spec độc lập;
- hoặc hiện tại chỉ cần mô tả đủ để dev hiểu PM muốn gì, action nào bị ảnh hưởng, và boundary nằm ở đâu.

Khi đã chọn `write enough here`, chỉ viết đủ:

- mục đích business;
- điều kiện xuất hiện / trigger;
- tác động lên action hoặc decision;
- UI expectation ở mức vừa đủ;
- implementation note ngắn nếu cần.

Nếu page owner có list/card decision surface, tối thiểu phải trả lời:

- ở level row/card, operator cần nhìn nhóm thông tin gì để ra quyết định
- mỗi action chính ở level row/card dùng để làm gì
- action nào chỉ là entry point sang child page

Nếu local UI/code đã đủ rõ, thay 3 câu hỏi trên bằng câu trả lời cụ thể hơn:

- row/card đang hiển thị chính xác field nào
- từng field đó giúp operator xác nhận hay quyết định điều gì
- từng action button đang có thật trên row/card dùng để làm gì

Không cần liệt kê pixel-level anatomy, nhưng cũng không được bỏ trống business summary của row/card/action.

Không mở rộng thêm chỉ vì code hiện đang có nhiều field, mock handler, scaffold, hay conditional render.

## Update policy bắt buộc

Khi page Outline đã có spec:

1. Đọc page target và ít nhất `1-2` peer pages gần nhất trong cùng subtree.
2. Xác định page role hiện tại và local convention của subtree.
3. So nội dung theo section, không so mơ hồ theo cảm giác.
4. Giữ nguyên section đang đúng.
5. Chỉ sửa section sai hoặc cũ.
6. Chỉ thêm section còn thiếu khi thực sự cần.
7. Không replace toàn bộ page chỉ vì muốn đồng bộ khung.
8. Luôn append change log ở cuối page.
9. Nếu nội dung mới là business truth của page, phải merge vào section chính; không đẩy vào block cập nhật tạm.
10. `Lịch sử cập nhật` chỉ giữ summary log, không giữ content business chi tiết.

## Review và publish rule bắt buộc

Khi user yêu cầu viết, sửa, hoặc cập nhật specs/docs trên Outline, phải tách đúng 2 trường hợp:

### Trường hợp A - page Outline đang trống hoặc chỉ là placeholder mỏng

Điều kiện nhận diện:

- page gần như chưa có body hữu ích;
- chỉ có vài dòng placeholder;
- hoặc content mỏng đến mức không có đủ section để review thực chất.

Cách xử lý:

- được phép đưa thẳng nội dung vào Outline nếu boundary và source đã khóa đủ;
- sau khi update xong, phản hồi ngắn gọn và trả lại link Outline làm current truth;
- không cần đẩy một bản đề xuất dài lên chat trước chỉ để review wording.

### Trường hợp B - page Outline đã có docs/spec có ý nghĩa

Điều kiện nhận diện:

- page đã có structure, section, hoặc content đủ để được coi là current draft/current truth;
- dù content còn cũ, lệch, hoặc mixed language, nhưng vẫn là một page có substance.

Cách xử lý:

- không tự publish ngay chỉ vì đã có draft local;
- phải đưa đề xuất thay đổi chi tiết lên chat trước để user review;
- proposal phải nêu rõ:
  - section nào `keep`
  - section nào `fix`
  - section nào `append`
  - section nào cần `new child page needed`
- chỉ publish sau khi user duyệt trên chat.
- sau khi user duyệt, nội dung approved phải được gắn vào body chính của page
- `Lịch sử cập nhật` chỉ ghi tóm tắt lượt sửa, không được trở thành nơi chứa nội dung business mới

Rule ưu tiên:

- nếu khó phân biệt giữa `placeholder` và `existing meaningful content`, mặc định xử lý theo nhánh an toàn hơn là `existing meaningful content`.

Workflow chi tiết nằm ở:

- [update-safety.md](./references/update-safety.md)

## Data policy

Trong skill này, phần data chỉ được viết ở mức `data touchpoints`.

Chỉ nên nêu:

- module đọc dữ liệu gì;
- module ghi hoặc cập nhật dữ liệu gì;
- rule / limit / dependency dữ liệu nào làm thay đổi behavior;
- upstream / downstream nào cần biết khi đọc spec.

Không đi vào:

- field-level schema;
- payload request / response;
- backend contract chi tiết;
- migration logic.

## Workflow bắt buộc

### Phase 1. Khóa boundary

- xác định target project / module / subtree;
- xác định page role;
- xác định source of truth bundle;
- xác định local code anchors nếu task có sync với codebase.

### Phase 2. Khóa local convention

- đọc page target;
- đọc peer pages gần nhất cùng subtree;
- mirror metadata labels, heading style, và link conventions của project đó.

### Phase 3. Chọn mode đúng

- `create-new-spec`
- `refine-existing-spec`
- `expand-owner-into-child-pages`
- `codebase-to-outline-sync`

### Phase 4. Draft hoặc patch

- nếu page mới: viết theo role template;
- nếu page cũ: patch theo section;
- nếu module lớn: tách owner page và child pages theo đúng boundary.
- nếu page target là `placeholder` hoặc gần trống: có thể update thẳng lên Outline rồi trả link current truth;
- nếu page target đã có docs/spec có ý nghĩa: phải đưa proposal chi tiết lên chat trước khi publish.
- trước khi mở rộng một section, phải chốt `new child page needed` hay `write enough here`.
- nếu là `write enough here`, giữ section ngắn, business-first, không mô tả thuần code.
- nếu section liên quan đến row/card/list surface:
  - ghi exact displayed data trước
  - rồi mới ghi business meaning và action meaning
- nếu page target đã có content meaningful:
  - patch approved content vào body chính
  - chỉ để một dòng/tóm tắt ngắn trong `Lịch sử cập nhật`
- nếu vì hạn chế connector phải append tạm một block cập nhật:
  - phải ghi rõ đây là workaround tạm
  - phải quay lại làm một `normalize pass`
  - chưa coi page là `clean published` cho đến khi content đã được fold vào body chính

### Phase 5. Append change log

Mọi thay đổi đều phải có log cuối page, tối thiểu gồm:

- thời gian;
- phần nào đã đổi;
- tóm tắt ngắn nội dung đổi;
- vì sao đổi;
- source nào đã verify.

### Phase 6. Báo kết quả

Báo ngắn gọn:

- page nào đã được tạo hoặc sửa;
- mode đã dùng;
- page nào là current truth sau khi update;
- còn unknown nào nếu chưa đủ evidence.

Nếu chưa publish vì đang chờ user review:

- nói rõ đây là `proposal for chat review`
- không mô tả như thể Outline đã là current truth mới

## UGC Website heuristics

Dùng corpus này khi project là `ugc-website` hoặc layout gần tương tự:

- `06 Settings` là `navigation-group`, không phải business module riêng
- `00 Global UI Patterns & Platform` là `shared-platform`, không phải sidebar module
- `05 Website` và `06.03 UGC Config` là `module-owner` có child specs rõ
- code routes top-level không map 1-1 hoàn toàn với Outline tree
- hidden surfaces cũng là spec surface:
  - tabs
  - drawer
  - modal
  - detail panel
  - form subpage

Đọc map cụ thể tại:

- [ugc-website-spec-map.md](./references/ugc-website-spec-map.md)

## Phối hợp với skill khác

- Dùng `work-with-outline` khi cần đọc hoặc cập nhật page trên `wiki.odp.garena.vn`
- Dùng `analyze-gap` khi cần compare codebase local với Outline trước khi vá spec
- Không đẩy task sang `document-delivery` nếu user đang yêu cầu spec dev-facing

