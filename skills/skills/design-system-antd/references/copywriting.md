# Copywriting — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/copywriting

---

## 1. NGUYÊN TẮC CHUNG

- **Nghĩ từ góc nhìn user** — viết về những gì user CÓ THỂ LÀM, không phải hệ thống làm gì
- **Biểu đạt nhất quán** — cùng thuật ngữ cho cùng khái niệm xuyên suốt app
- **Thông tin quan trọng lên trước** — đặt nội dung chính ở vị trí nổi bật
- **Chuyên nghiệp, chính xác, đầy đủ** — không mơ hồ
- **Ngắn gọn, thân thiện, tích cực** — tránh từ ngữ tiêu cực khi có thể

---

## 1.1 LANGUAGE SCOPE CONTRACT

- Default internal-tool contract: **system UI chrome must be English-only**
- "System UI chrome" includes page titles, navigation labels, tabs, buttons, empty states, form labels, placeholders, validation text, helper text, tooltips, system badges, modal copy, toast messages, and date labels
- Content may remain in the source language when it is user-generated, imported from external platforms, or intentionally business-facing
- Do not mix English chrome with accidental browser-locale strings in dates, calendars, or generated component copy
- If a project wants non-English system UI, that must be written explicitly in `DESIGN.md`

### Quick examples
```
✅ UI chrome: "Create topic", "Saved reports", "Data available from 18 Mar 2026 - 17 Apr 2026"
✅ Content: imported post text in Vietnamese, Thai, or Indonesian
❌ UI chrome: mixed English navigation with Chinese month names or browser-localized date labels
```

---

## 2. QUY TẮC NGÔN NGỮ

### Tập trung vào user:
```
❌ "Hệ thống đã xoá creator"
✅ "Creator đã được xoá"

❌ "Lỗi: Hệ thống không thể lưu dữ liệu"
✅ "Không thể lưu. Vui lòng thử lại."
```

### Ngắn gọn:
```
❌ "Bạn cần phải nhập địa chỉ email để có thể tiếp tục"
✅ "Vui lòng nhập email"

❌ "Bạn có muốn xác nhận xoá creator này không?"
✅ "Xoá creator này?"
```

### Dùng từ quen thuộc:
```
❌ "Invalidate session token"
✅ "Phiên đăng nhập đã hết hạn"

❌ "Query parameter không hợp lệ"
✅ "Bộ lọc không hợp lệ"
```

### Biểu đạt nhất quán:
```
❌ Trang A: "Người sáng tạo", Trang B: "Creator", Trang C: "KOL"
✅ Thống nhất dùng "Creator" xuyên suốt

❌ Trang A: "Xoá", Trang B: "Loại bỏ", Trang C: "Gỡ"
✅ Thống nhất dùng "Xoá" cho cùng hành động
```

### Đầy đủ và trực tiếp:
```
❌ "Lỗi"
✅ "Không thể tải danh sách creator. Vui lòng thử lại."

❌ "Thao tác thành công"
✅ "Đã duyệt creator thành công"
```

---

## 3. TONE (Giọng điệu)

### Gần gũi:
```
❌ "Nội dung của tôi / Nội dung của bạn" (lẫn lộn my/your)
✅ "Nội dung" hoặc "Nội dung của bạn" (nhất quán)
```

### Thân thiện, tôn trọng:
```
❌ "Bạn phải nhập tên trước khi submit"
✅ "Vui lòng nhập tên"

❌ "Bạn đã làm sai"
✅ "Thông tin chưa đúng, vui lòng kiểm tra lại"
```

### Không quá tuyệt đối:
```
❌ "Tính năng này sẽ không bao giờ bị lỗi"
✅ "Tính năng này đã được kiểm tra kỹ"

❌ "Tất cả creator đều hài lòng"
✅ "Đa số creator phản hồi tích cực"
```

---

## 4. QUY TẮC VIẾT CHỮ & DẤU CÂU

### Capitalization (cho text tiếng Anh):
- **Sentence case** cho heading, title, label, button — chỉ viết hoa chữ đầu
- **Viết hoa** tên sản phẩm, tên riêng
- **Lowercase** cho body text

```
✅ "Creator management"        (sentence case)
❌ "Creator Management"        (title case — tránh)
❌ "CREATOR MANAGEMENT"        (all caps — tránh)
```

### Dấu câu:
- **Label, title, tooltip, tip**: KHÔNG dùng dấu chấm cuối
- **Button text**: KHÔNG dùng dấu chấm
- **Table cell text**: KHÔNG dùng dấu chấm
- **Description text**: Có thể dùng dấu chấm
- **Dấu chấm than (!)**: Dùng cực kỳ tiết kiệm — chỉ cho success/celebration

```
✅ Label: "Tên Creator"          (không dấu chấm)
✅ Button: "Lưu"                 (không dấu chấm)
✅ Tooltip: "Click để sửa"      (không dấu chấm)
✅ Description: "Creator đã được duyệt thành công."  (có dấu chấm)
✅ Message: "Đã lưu thành công!"  (dấu chấm than OK cho success)
```

### Số:
- Dùng **chữ số Ả Rập** (1, 2, 3...) thay vì viết chữ (một, hai, ba...)
- Dùng dấu phẩy ngăn cách hàng nghìn: 1,234,567

---

## 5. TEMPLATE COPY CHO INTERNAL TOOL

### Button labels:

| Hành động | Copy chuẩn | Tránh |
|---|---|---|
| Tạo mới | "Thêm [đối tượng]" hoặc "Tạo [đối tượng]" | "Thêm mới" (thiếu context) |
| Lưu | "Lưu" | "Submit" |
| Huỷ | "Huỷ" | "Cancel" |
| Xoá | "Xoá" | "Delete" (trừ khi app tiếng Anh) |
| Tìm kiếm | "Tìm" hoặc "Tìm kiếm" | "Search" |
| Reset filter | "Reset" hoặc "Đặt lại" | "Xoá bộ lọc" |
| Export | "Xuất CSV" hoặc "Xuất file" | "Export" |

### Confirmation dialogs:

```
Title:       "[Hành động] [đối tượng] này?"
             → "Xoá creator này?"
             → "Duyệt mission này?"

Description: "[Hậu quả của hành động]."
             → "Creator sẽ bị xoá khỏi hệ thống."
             → "Mission sẽ được gửi đến tất cả creator."

OK button:   "[Hành động]" (cùng từ với title)
             → "Xoá"
             → "Duyệt"

Cancel:      "Huỷ"
```

### Error messages:

```
API error:   "Không thể [hành động]. Vui lòng thử lại."
             → "Không thể tải dữ liệu. Vui lòng thử lại."

Validation:  "Vui lòng [yêu cầu]"
             → "Vui lòng nhập email"
             → "Vui lòng chọn game"

Format:      "[Field] không hợp lệ"
             → "Email không hợp lệ"
             → "Số điện thoại không hợp lệ"
```

### Success messages:

```
Create:  "Đã tạo [đối tượng] thành công!"
Edit:    "Đã cập nhật thành công!"
Delete:  "Đã xoá [đối tượng]!"
Approve: "Đã duyệt thành công!"
```

### Empty states:

```
No data:     "Chưa có [đối tượng] nào"
             → "Chưa có creator nào"
             + CTA: "Thêm Creator đầu tiên"

No results:  "Không tìm thấy kết quả cho \"[keyword]\""
             + Hint: "Thử từ khoá khác hoặc bỏ bớt bộ lọc"
```

### Helper / subtitle text:

```
Only add helper or subtitle text when the UI would become ambiguous without it.

Don't repeat the obvious:
   Title: "AI Configuration"
   Tabs: "My Skills (1)", "My Knowledge (2)"
   Helper: "1 skill selected • 2 knowledge bases selected"

Keep only the controls that already communicate the state.
```

### Placeholder text:

```
Search:      "Tìm kiếm [đối tượng]..."
             → "Tìm kiếm creator..."

Select:      "Chọn [đối tượng]"
             → "Chọn game"

Input:       "Nhập [đối tượng]"
             → "Nhập tên creator"
```
