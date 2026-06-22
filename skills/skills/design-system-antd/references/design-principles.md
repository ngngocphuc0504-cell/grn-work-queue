# Design Principles — Ant Design 6 for Internal Tools

Tài liệu này chuyển design values của Ant Design thành rule dùng được ngay cho internal website.

---

## 1. FOUR DESIGN VALUES

### Natural
- Giảm cognitive load bằng layout quen thuộc, scan nhanh, ít bất ngờ
- Dùng cấu trúc phẳng, hierarchy rõ, label dễ hiểu
- Không bắt user giải mã UI chỉ để hoàn thành tác vụ quen thuộc

### Certain
- Cùng loại page phải có cùng structure, spacing, component behavior
- Không tạo thêm một design system song song bên cạnh AntD
- Token, state và interaction phải nhất quán giữa nhiều project

### Meaningful
- Mỗi action phải rõ mục tiêu và kết quả
- Mọi thao tác phải có feedback phù hợp
- Không thêm subtitle, helper text, card chrome, animation nếu không giúp hoàn thành task

### Growing
- Pattern phải mở rộng sang module mới mà không cần phát minh lại
- Ưu tiên abstractions ổn định: page type, shell, filter bar, table, overlay, state patterns
- Project-specific override chỉ được tác động phần brand/business wording, không phá foundation

---

## 2. TEN PRACTICAL PRINCIPLES

### Proximity
- 8px: micro gap
- 16px: gap mặc định trong cùng nhóm
- 24px: gap giữa sections
- Group gần nhau khi chúng thuộc cùng một decision hoặc flow

### Alignment
- Một page nên có số ít alignment lines rõ ràng
- Text trái, số phải, status giữa nếu cần scan
- Form label và field phải có cấu trúc ổn định

### Contrast
- Dùng contrast để tạo hierarchy, không để trang trông “ồn”
- 1 primary action mỗi nhóm
- Thông tin phụ phải mờ hơn, nhưng vẫn đủ đọc

### Repetition
- Lặp lại pattern đúng để user không phải học lại
- List page giống list page
- Detail page giống detail page
- Overlay cùng loại dùng cùng footer logic, padding, width logic

### Make it Direct
- Nếu task ngắn và cục bộ, ưu tiên inline edit hoặc overlay
- Tránh điều hướng nhiều bước chỉ để sửa một field đơn giản

### Stay on the Page
- Ưu tiên `Modal`, `Drawer`, `Tabs`, `Collapse`, expandable area
- Chỉ chuyển route khi context mới thực sự lớn hoặc cần deep-link riêng

### Keep it Lightweight
- Công cụ quan trọng phải hiện rõ
- Không ẩn action quan trọng sau nhiều tầng hover/menu
- Expose filter/search/action gần ngữ cảnh sử dụng

### Provide an Invitation
- CTA phải nhìn ra được là click được
- Empty state phải cho biết bước tiếp theo
- Disabled state nên có lý do khi có thể

### Use Transition
- Dùng transition ngắn, có ý nghĩa
- Không tạo motion phức tạp trong internal tool
- Transition để giữ context, không để “trang trí”

### React Immediately
- Mọi interaction phải có phản hồi
- <300ms: phản hồi tức thì
- 300ms–2s: loading state
- >2s: skeleton/progress/hint

---

## 3. INTERNAL TOOL TRANSLATION

| Page type | Điều user cần cảm thấy |
|---|---|
| List page | Tìm, lọc, so sánh, hành động nhanh |
| Detail page | Thấy đủ ngữ cảnh, không bị lạc |
| Form/config page | Điền đúng, ít lỗi, không mệt |
| Dashboard | Quét nhanh, biết ưu tiên gì |
| Moderation/review page | Quyết định nhanh, rủi ro thấp |

---

## 4. NON-NEGOTIABLE RULES

- Không hardcode visual language trái AntD token nếu không có lý do dự án rõ ràng
- Không xây `BaseUI` như hệ UI song song
- Không tạo custom component mới khi AntD core đã giải quyết tốt
- Không mix nhiều pattern cho cùng một loại page
- Không ẩn action chính sau dropdown nếu action đó là task cốt lõi
