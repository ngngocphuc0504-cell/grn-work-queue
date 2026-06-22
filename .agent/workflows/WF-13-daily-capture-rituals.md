---
description: "Giao tiếp hàng ngày, phân luồng các lệnh Capture vào đúng mảng logic của Second Brain"
---

# WF-13: Daily Capture Rituals & Routing

## 1. Metadata
- **Owned By:** Coordinator Agent
- **Assigned Skills:** `sga-08-setup-architect`, `skh-05`
- **Execution Mode:** Quick Reactive

## 2. Description
Hệ thống điều phối dòng lệnh nhanh (Quick Capture) mỗi ngày. Giúp User duy trì tương tác dưới 5 phút/ngày ở các góc độ: Check-in, Task, Knowledge, Networking, Learning, Brainstorm.

## 3. Prerequisites
- Đã thiết lập structure Daily Input ở WF-00.
- User gửi prompt theo cấu trúc của Guideline Phase 3.

## 4. Execution Steps

### [ROUTING LAYER] Phân loại Intent
Ngay khi User gửi một quick prompt, xác định loại hình:
1. **A. Morning / Evening Check-in:** Xử lý bằng cách gọi Cập nhật ưu tiên trên Task Board.
2. **B. Task Capture:** Kích hoạt ngay `WF-01` để frame task (Zero-Native avoidance).
3. **C. Knowledge / Learning Capture:**
   - Dịch dữ liệu thành KI (Knowledge Item).
   - Gọi `sga-08` để định cỡ và map KI vào 1 trong 5 Nodes của Second Brain.
   - Trả lời xác nhận nhanh (Ví dụ: "Đã lưu vào Node KNOWLEDGE/Project_X").
4. **D. Networking Capture:**
   - Đánh giá Relationship strength.
   - Auto-draft Email/Message theo Tone Voice nếu được yêu cầu.
5. **F. Brainstorm:**
   - Áp dụng "Devil's Advocate" (Challenge assumptions).
   - Nối thẳng vào GAP-MAP.

### [VALIDATION LAYER]
- *Rule-Gate:* Nếu thông tin rác (Ví dụ: Learning nhưng không ra insight hành động), yêu cầu User làm sắc bén nội dung trước khi tống vào Knowledge Graph.

## 5. Expected Outputs
- Knowledge Graph được nuôi tự động liên tục.
- Tiết kiệm thời gian tương tác (Micro-interactions < 3 phút).
