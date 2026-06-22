# Update Safety

Khi target page đã tồn tại trong Outline, `write-specs` phải ưu tiên sửa an toàn theo từng phần.

## Mục tiêu

- không overwrite toàn bộ nội dung đang đúng;
- không áp template mới lên một subtree đã có convention tốt;
- chỉ sửa phần sai, cũ, hoặc thiếu;
- luôn để lại log cuối page.

## Workflow bắt buộc

### 1. Đọc đúng bundle trước khi sửa

- đọc page target;
- đọc ít nhất `1-2` peer pages gần nhất trong cùng subtree;
- nếu page target là child page, ưu tiên peer cùng role.

### 2. Chốt page role và section inventory

- xác định page đang là `catalog`, `navigation-group`, `shared-platform`, `module-owner`, hay `child-spec`;
- liệt kê các section hiện có;
- đánh dấu section nào đang đúng, section nào thiếu, section nào lệch.

### 3. Quyết định edit scope

Chỉ dùng một trong các nhãn sau:

- `keep`: section đang đúng, không chạm vào
- `fix`: section đang có nhưng sai hoặc cũ
- `append`: section đang thiếu, cần thêm mới
- `new child page needed`: page hiện tại quá rộng, nên tách child page thay vì nhồi tiếp

Trước khi chọn `fix` hay `append` cho một section đang có nguy cơ dài ra, phải chốt thêm:

- `new child page needed`
- hoặc `write enough here`

Nếu chọn `write enough here`, nội dung mới phải:

- đi từ business purpose trước;
- nói rõ trigger / tác động / boundary;
- đủ để dev hiểu PM muốn gì;
- không kể lại code như một bản mô tả implementation thô.

Nếu page owner có row/card surface dùng để operator quyết định nhanh, `write enough here` vẫn phải giữ tối thiểu:

- nhóm thông tin cần hiển thị ở row/card
- ý nghĩa của từng action chính ở row/card
- action nào là entry point sang child page

Nếu code/UI đã đủ rõ, không dừng ở mức nhóm thông tin trừu tượng. Phải gọi ra:

- exact displayed data hoặc label thật trên UI
- từng field đó giúp operator quyết định gì
- tên action/button thật đang có và ý nghĩa của từng action

Ví dụ:

- tốt: `Channel Name` và `Channel Link` để admin nhận diện đúng creator đang xử lý
- không đủ: `định danh creator để nhận diện đúng hồ sơ`

Không được bỏ qua hoàn toàn phần này chỉ vì shared shell đã có owner ở page khác.

## Nội dung chính vs lịch sử cập nhật

Khi page đã có content meaningful và user duyệt proposal patch:

- content business approved phải được merge vào nội dung chính của page
- `Lịch sử cập nhật` chỉ dùng để ghi summary ngắn
- không tạo block kiểu `Cập nhật YYYY-MM-DD` để chứa business content lâu dài

`Lịch sử cập nhật` chỉ nên giữ:

- ngày
- changed sections ngắn
- reason ngắn
- source checked ngắn nếu subtree cần

Nếu vì hạn chế connector phải append tạm một block cập nhật:

- coi đó là workaround tạm thời
- phải có một `normalize pass` sau đó
- trước khi normalize, page chưa được coi là clean state

## Guardrails

- Không replace toàn page chỉ vì muốn chuẩn hóa tiêu đề.
- Không đổi toàn bộ heading names nếu local subtree đang nhất quán.
- Không xóa prose đang đúng chỉ vì nó không giống template generic.
- Nếu structure cũ vẫn đúng, chỉ thêm phần còn thiếu như `Data touchpoints` hoặc `Change log`.

## Khi page hiện có đã khá tốt

Nếu page:

- đã đúng role;
- đã có heading logic;
- đã match subtree style;

thì:

- giữ nguyên structure chính;
- vá nội dung từng section;
- chỉ thêm section còn thiếu khi reader thực sự cần.
- nếu một phần chỉ là sub-surface nhỏ trong module, ưu tiên viết ngắn và business-first thay vì biến nó thành tiểu spec dài dòng ngay trong cùng page.
- nhưng nếu sub-surface nhỏ đó là nơi operator ra quyết định ở level row/card/action, page vẫn phải có business summary đủ dùng cho dev.

## Review gate trước khi publish

Khi user yêu cầu cập nhật docs/spec trên Outline, phải phân biệt:

### 1. Page trống hoặc placeholder mỏng

Nếu page:

- gần như trống;
- chỉ có vài dòng placeholder;
- chưa có section/content đủ để user phải review từng patch;

thì:

- có thể update thẳng lên Outline sau khi khóa boundary;
- phản hồi lại bằng link Outline và current truth ngắn gọn.

### 2. Page đã có nội dung có ý nghĩa

Nếu page:

- đã có section/body thực sự;
- hoặc đang là current draft/current truth có substance;

thì:

- không publish ngay;
- phải đưa proposal patch chi tiết lên chat trước;
- proposal nên nêu rõ `keep`, `fix`, `append`, `new child page needed`;
- chỉ publish sau khi user duyệt proposal đó.
- sau khi publish, approved content phải nằm trong body chính thay vì sống trong block cập nhật tách rời

Nếu không chắc page thuộc nhóm nào:

- mặc định coi là `page đã có nội dung có ý nghĩa`.

## Change log cuối page

Mỗi lần chỉnh sửa phải append log ở cuối page.

Tối thiểu cần có:

- `Date`
- `Changed sections`
- `Reason`
- `Source checked`

Nếu subtree đã có convention log riêng:

- append đúng format đang dùng;
- không tự tạo block log mới kiểu khác.

Nếu subtree chưa có log:

- thêm block `Change Log` ngắn ở cuối page;
- mỗi entry chỉ cần đủ để truy vết lần sửa.
