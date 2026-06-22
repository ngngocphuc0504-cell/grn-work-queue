# Outline Read Scope For Large Gap Analysis

Tài liệu này hướng dẫn `analyze-gap` đọc Outline subtree đủ sâu nhưng vẫn có boundary rõ, để tránh:

- đọc nông ở page catalog rồi tự assume
- output quá dài vì đọc lan sang mọi branch
- miss child pages / level-2 descendants chứa detailed module truth

## Mục tiêu

Khi source of truth là Outline, skill phải xác định đúng một trong các loại page sau:

- `project root`
- `module catalog`
- `owner page`
- `companion page`
- `operational page`
- `archive page`

## Read Order Mặc Định

## Trường hợp 1 — User đưa project root

Đọc theo thứ tự:

1. root page
2. module catalog nếu root nói rõ đây là navigation hub
3. owner page đúng module đang xử lý
4. child pages của owner page
5. level-2 descendants nếu owner page hoặc child page cho thấy detailed rules nằm sâu hơn

Không đọc sibling modules nếu task chỉ tập trung vào 1 module.

## Trường hợp 2 — User đưa module catalog

Đọc theo thứ tự:

1. catalog page
2. owner page tương ứng
3. child pages dưới owner page
4. level-2 descendants khi có dấu hiệu deeper rules

Rule:

- catalog chỉ là **router/index page**
- không dùng catalog làm detailed truth trừ khi chính catalog chứa rule đó và không có owner page sâu hơn

## Trường hợp 3 — User đưa owner page

Đọc theo thứ tự:

1. owner page
2. child pages trực tiếp
3. level-2 descendants nếu:
   - owner page ghi `Read Next`
   - owner page mô tả workflow sâu hơn
   - child page chỉ là hub / section index
   - prose nhắc đến hidden surfaces nhưng body hiện tại chưa đủ chi tiết

## Trường hợp 4 — User đưa companion page

Đọc theo thứ tự:

1. companion page hiện tại
2. owner page nếu cần để xác định boundary
3. sibling companion pages chỉ khi owner page nói cần đọc bundle

Không tự mở rộng sang cả module subtree nếu câu hỏi chỉ nằm ở một companion page nhỏ.

## Khi nào phải descend thêm

Phải đọc child page hoặc level-2 descendant nếu có bất kỳ dấu hiệu nào sau:

- page hiện tại nói rõ `Read Next`
- có bảng / list link ra child pages
- có wording kiểu:
  - “chi tiết ở page dưới”
  - “xem page companion”
  - “workflow này được tách riêng”
  - “tab này có page riêng”
- module có settings order / numbered children như `06.01`, `06.02`, `06.03`
- prose nhắc `Add new`, click card, right panel, drawer, side sheet, inline detail nhưng body hiện tại chưa mô tả đủ

## Khi nào dừng

Dừng mở rộng khi:

- đã có owner page + child subtree đủ để inventory surfaces trong scope
- branch tiếp theo là sibling không phục vụ task hiện tại
- branch là archive / old route và không được page live dùng làm current truth

## Unknown thay vì assume

Nếu tool visibility không cho thấy rõ subtree hoặc exact child page:

- ghi `unknown`
- ghi lý do:
  - chưa thấy child tree
  - chưa đọc được linked page
  - page hiện tại chỉ hint surface

Không được:

- suy luận hidden surface từ title page
- đánh `match` chỉ vì page name và route name giống nhau

## Mapping sang local code

Khi Outline subtree đã rõ, phải map sang local code theo thứ tự:

1. route map / app shell
2. module page entry
3. sub-components và render branches
4. action-triggered surfaces

Nếu chưa xác định được local anchor tương ứng:

- dừng ở checkpoint boundary
- không compare tiếp
