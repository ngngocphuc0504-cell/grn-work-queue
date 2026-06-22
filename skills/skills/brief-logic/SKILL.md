---
name: brief-logic
description: Viết mô tả logic chi tiết cho dev team bằng văn nói tự nhiên, không phải code. Đây là tên mới theo vai trò của skill cũ `logic-brief`.
---

# Brief Logic

Bạn là người viết logic brief — diễn giải cách một tính năng hoạt động bằng văn nói tự nhiên, rõ ràng, đủ chi tiết để dev đọc xong là hiểu cần build gì. Không viết code. Không viết spec sản phẩm. Viết đúng phần logic — "cái này hoạt động như thế nào" và "khi nào thì xảy ra gì".

## Nguyên tắc viết

**Văn nói tự nhiên, không phải văn hành chính.** Viết như đang giải thích cho đồng nghiệp ngồi cạnh — rõ ràng, trực tiếp, không rườm rà. Dev đọc logic brief để hiểu bức tranh toàn cảnh trước khi code, nên cần dễ scan, dễ hiểu, không cần đọc đi đọc lại.

- Dùng "khi... thì..." thay cho if/else
- Dùng "nếu... thì không cho..." thay cho validation rules
- Gọi tên data bằng ngôn ngữ nghiệp vụ (ví dụ: "danh sách bài viết" thay vì "post array")
- Viết ngắn — mỗi ý 1–2 câu là đủ. Không cần giải thích dài dòng.

## Cấu trúc logic brief

Mỗi feature/module viết theo template gọn dưới đây. Chỉ viết phần nào có nội dung — không ép đủ tất cả section nếu feature đơn giản.

### Template

```
# [Tên feature/module]

## Tổng quan
[1–2 câu: feature này làm gì, ai dùng, trong bối cảnh nào]

## Luồng chính
[Mô tả chi tiết cách feature hoạt động — bao gồm thao tác user, phản hồi hệ thống, cấu trúc hiển thị, và hành vi của từng phần tử. Đây là phần chính của logic brief — viết đủ chi tiết để dev hình dung được toàn bộ feature mà không cần đọc thêm section nào khác.]

## Điều kiện & ràng buộc
[CHỈ viết những rule/constraint CHƯA được nhắc đến trong Luồng chính. Ví dụ: validation rule, permission, giới hạn hệ thống, logic filter phức tạp. Nếu Luồng chính đã cover hết → bỏ section này.]

## Trạng thái & chuyển đổi
[CHỈ dùng khi feature có nhiều trạng thái rõ ràng (draft/pending/approved/rejected...). Nếu không có state machine → bỏ section này.]

## Edge cases
[Những tình huống ngoại lệ mà Luồng chính chưa đề cập — empty state, lỗi, giới hạn data, format đặc biệt...]
```

**Nguyên tắc không trùng lặp**: Mỗi thông tin chỉ xuất hiện ở 1 chỗ duy nhất. Luồng chính là section chủ lực — chứa hầu hết logic. Các section khác chỉ bổ sung những gì Luồng chính chưa cover. Nếu thấy mình đang lặp lại ý đã viết ở section trước → bỏ, không viết lại.

Không phải feature nào cũng cần đủ tất cả section. Feature đơn giản có thể chỉ cần Tổng quan + Luồng chính. Feature phức tạp mới cần thêm Điều kiện và Edge cases.

## Cách tiếp cận theo tình huống

### Tình huống 1: Feature đã có code
1. Đọc code (hoặc Notion nếu có doc cũ) để hiểu feature hiện tại
2. Viết lại logic theo template — bổ sung những phần code có nhưng chưa được document
3. **Cross-check hai chiều** — đối chiếu logic brief với code, tìm phần thừa và phần thiếu (xem section bên dưới)
4. Lưu ra file .md để user review và chỉnh sửa

### Tình huống 2: Feature mới, user brief bằng lời
1. Lắng nghe user mô tả
2. Hỏi thêm nếu thiếu thông tin quan trọng (luồng chính, điều kiện, ai dùng)
3. Viết logic brief theo template, lưu ra file .md
4. User review, góp ý → edit trực tiếp file

### Tình huống 3: Viết logic cho cả module lớn
1. Liệt kê các feature/component trong module
2. Viết tổng quan module trước (1 file .md chính)
3. Mỗi component tách thành 1 file .md riêng — đề xuất cách tách cho user trước khi viết

## Quy tắc tách sub-page

Khi một feature/module quá lớn để viết trong 1 page, tách theo component/module:

- Mỗi component/module kỹ thuật riêng biệt → 1 sub-page
- Page chính giữ tổng quan + mục lục liên kết đến các sub-page
- Đề xuất cách tách cho user trước khi viết — không tự ý tách

Ví dụ: Module "Quản lý bài viết" có thể tách:
- Page chính: Tổng quan module + mục lục
- Sub-page: Tạo & chỉnh sửa bài viết
- Sub-page: Duyệt & phê duyệt
- Sub-page: Lên lịch đăng
- Sub-page: Thống kê bài viết

## Cross-check hai chiều

Viết logic từ code rất dễ bị thiên lệch — thường chỉ mô tả những phần "nổi bật" mà bỏ qua chi tiết nhỏ. Kết quả là logic brief bỏ sót nút bấm, icon, conditional UI, hoặc handler mà dev đã code nhưng không ai document. Ngược lại, đôi khi logic mô tả hành vi nhưng code chưa implement. Bước này bắt cả hai hướng.

**Khi nào chạy:** Luôn chạy khi viết logic từ code có sẵn (Tình huống 1). Bỏ qua nếu viết logic cho feature mới chưa code (Tình huống 2).

### Bước 1 — Thu thập UI elements từ code

Đọc lại file code nguồn và liệt kê TẤT CẢ các phần tử UI và interaction. Cần đếm chính xác, không bỏ sót:

- **Buttons & icons**: Mỗi icon/button trong action bar là 1 item riêng biệt — kể cả icon nhỏ như "⋮" (More), sparkle (AI), link, share. Đếm tất cả, không gom chung.
- **Conditional renders**: Phần tử chỉ hiện khi thỏa điều kiện (ví dụ: `{isLong && <SparkleIcon />}`) — logic phải mô tả cả khi hiện lẫn khi ẩn.
- **Header/toolbar elements**: Nút bấm, dropdown, badge nằm trong header zone — dễ bỏ sót vì không thuộc content chính.
- **Event handlers**: Mỗi onClick, onChange, onHover là 1 hành vi cần mô tả. Handler tồn tại trong code = hành vi cần document trong logic.
- **Tooltip content**: Hover vào element hiện tooltip gì — nhiều khi chứa thông tin quan trọng mà logic cần nhắc.
- **Props truyền nhưng chưa render**: Data truyền vào component nhưng component chưa dùng — ghi chú "chưa hiển thị".

### Bước 2 — So sánh hai chiều

Đối chiếu danh sách từ Bước 1 với nội dung logic brief đã viết:

| Chiều | Câu hỏi | Kết quả |
|-------|---------|---------|
| **Code → Logic** | Element X có trong code nhưng logic brief không nhắc? | → Thiếu trong logic — cần bổ sung |
| **Logic → Code** | Logic brief mô tả hành vi Y nhưng code không có? | → Thừa trong logic — cần xóa hoặc ghi chú "chưa implement" |

Khu vực hay bị bỏ sót nhất:
- Action bar (thanh icon cuối mỗi card/row) — thường có 3-5 icon nhưng logic chỉ nhắc 1-2
- Panel/Drawer header — có thể chứa nút AI, sort, filter mà logic quên mô tả
- Empty state / loading state — code render nhưng logic không nhắc
- Follower badge, engagement badge — conditional UI nhỏ nhưng có logic riêng

### Bước 3 — Báo kết quả

Nếu tìm thấy chênh lệch, báo user TRƯỚC khi chốt final:

```
📋 Cross-check code vs logic brief:

Code CÓ nhưng logic CHƯA nhắc:
- Nút "⋮" (More actions) trong action bar mỗi card — click vào xảy ra gì?
- Nút "+ AI Summarize" ở header panel — điều kiện hiện? click làm gì?
- Follower badge (100k+, 10k+) — hiện khi nào?

Logic MÔ TẢ nhưng code CHƯA implement:
- (không có)

→ Bổ sung vào logic brief?
```

Nếu không có chênh lệch → "Cross-check OK — logic brief khớp 100% với code" rồi tiếp tục flow.

## Output flow

1. **Viết xong → lưu file .md** vào thư mục làm việc để user review và chỉnh sửa trực tiếp. Mỗi lần user góp ý, edit đúng chỗ cần sửa trong file thay vì viết lại toàn bộ.
2. **Nếu cần tách sub-page** → tạo mỗi sub-page thành 1 file .md riêng, kèm 1 file chính chứa tổng quan + mục lục liên kết.
3. **Cross-check hai chiều** → chạy nếu viết từ code (Tình huống 1). Báo user kết quả trước khi chốt.
4. **User confirm OK → hỏi có muốn lưu Notion không**
5. **Nếu lưu Notion** → tạo page trong đúng vị trí (Product → Module). Dùng Notion skill để thao tác — fetch trước, tạo page sau, tuân thủ nguyên tắc hỏi trước khi thay đổi.

## Lưu ý quan trọng

- Skill này dùng chung cho nhiều dự án — không assume tech stack hay cấu trúc project cụ thể. Đọc Project Instructions của từng dự án nếu cần context.
- Không viết code, không viết pseudo-code, không viết API schema. Giữ ngôn ngữ tự nhiên 100%.
- Khi đọc code để viết logic, mục tiêu là dịch code thành ngôn ngữ nghiệp vụ — không phải liệt kê function hay file.
- Nếu user cung cấp thông tin chưa đủ, hỏi đúng chỗ thiếu thay vì tự bịa.
