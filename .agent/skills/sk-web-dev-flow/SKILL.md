---
name: sk-web-dev-flow
description: >
  Quy trình phát triển Web App chuẩn của team: Stitch (Design UX/UI) -> AI Studio (Code logic & UI integration) -> Antigravity (Debug, Fix & Deploy).
---

## BỐI CẢNH & QUY TRÌNH (WEB DEV FLOW)

Quy trình phát triển web app sẽ đi qua 3 giai đoạn chính để tận dụng tối đa sức mạnh của các tool AI khác nhau:

1. **Giai đoạn 1: Thiết kế UX/UI (Stitch)**
   - Sử dụng Stitch để draft giao diện (UI) và trải nghiệm người dùng (UX).
   - *Đầu ra:* Các bản thiết kế giao diện dạng hình ảnh (screenshots) hoặc code UI thô mang tính thẩm mỹ cao.

2. **Giai đoạn 2: Lập trình Logic & Tích hợp (Google AI Studio)**
   - Đưa toàn bộ Product Spec (Yêu cầu tính năng, kiến trúc) và hình ảnh prototype từ Stitch vào AI Studio.
   - Prompt AI Studio tham chiếu thiết kế từ ảnh để xuất ra bộ source code hoàn chỉnh (frontend, logic, styling, database connection).
   - *Đầu ra:* File nén dự án hoặc bộ source code hoàn chỉnh.

3. **Giai đoạn 3: Hoàn thiện & Deploy (Antigravity)**
   - Tải source code từ AI Studio về môi trường local.
   - Sử dụng Antigravity workspace để chạy thử (npm run dev), debug lỗi, refactor code, và tinh chỉnh UI.
   - Deploy sản phẩm cuối cùng.

## CÁC BƯỚC THỰC THI (ACTIONABLE STEPS)

Khi User yêu cầu làm 1 Web App mới, Agent cần tuân thủ quy trình sau:

### Bước 1: Thu thập Yêu cầu & Viết Spec
- Phân tích ý tưởng của user, đặt câu hỏi làm rõ (tham khảo SGA-01).
- Chốt Product Spec (PRD) gồm: Tech stack, Data schema, Features, UI rules.

### Bước 2: Chuẩn bị Prompt cho Stitch
- Viết 1 prompt chi tiết, rõ ràng mô tả bố cục (layout), màu sắc (color scheme), các thành phần UI (buttons, cards, inputs) để user copy paste vào Stitch tạo giao diện chính (thường là màn hình Dashboard).

### Bước 3: Chuẩn bị Prompt cho AI Studio
- Viết 1 prompt tổng hợp bao gồm:
  - Spec đầy đủ (PRD, Tech stack, Schema).
  - Lời nhắc AI Studio NHÌN vào ảnh đính kèm (từ Stitch) để code giao diện giống hệt.
  - Hướng dẫn cấu trúc thư mục.

### Bước 4: Support Debug trên Antigravity
- Sau khi user mang code từ AI Studio về, Agent chuyển sang role Debugger/Fixer.
- Đọc lỗi terminal, kiểm tra source code, sửa lỗi logic, và điều chỉnh UI bị lệch.
