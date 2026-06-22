---
description: Báo cáo buổi sáng (Nir Eyal Hook - External Trigger)
version: 1.0.0
---

# WF-02 Báo cáo Cập nhật Buổi sáng (Morning Briefing)

**Trigger Lệnh:** `/morning` hoặc tự động gọi vào lần khởi chạy đầu tiên trong ngày.

## Mục đích
Đóng vai trò là **External Trigger** (Cú hích ngoài) trong mô hình Hook. Kéo user vào luồng tương tác bằng việc cung cấp giá trị dự báo có ích ngay đầu ngày.

## Các Bước Thực Thi (By CTO)

### Bước 1: Quét Memory Bus
- Quét thư mục `outputs`: Đếm số task đang dang dở.
- Quét `02_twin_memory/twin-current/XP_GAMIFICATION.md`: Lấy chỉ số Level hiện tại và số % XP cần để lên cấp tiếp theo.

### Bước 2: Báo Cáo Chào Mừng (Chào hỏi Kích thích)
- Giọng điệu: Hào hứng, xưng hô như hai bề của một bản thể (tôi/ông, mình/bạn), tuyệt đối không dùng cấp bậc sếp/nhân viên.
- Ví dụ: *"Chào buổi sáng! Hệ thống đang sạch bong, không còn nợ nần gì từ hôm qua. Mình đang ở mốc Gà Mờ (0/100 XP). Ông có muốn setup nhanh 1 cái Task Brief để gặt vài XP khởi động ngày mới không?"*

### Bước 3: Đề xuất "Nhiệm Vụ Dễ" (Action)
- Đưa ra 1 task siêu dễ (ma sát thấp) để user có thể bấm "Y" để làm ngay lập tức, khởi động não bộ buổi sáng.
