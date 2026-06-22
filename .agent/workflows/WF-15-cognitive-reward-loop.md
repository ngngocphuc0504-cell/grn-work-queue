---
description: Lõi Gamification ngầm. Tự động chắt lọc XP, cấp Badge và cung cấp Insight kiểu Jarvis sau mỗi task.
semantic_triggers: ['tự động chạy sau mỗi task', 'reward', 'xp']
---

# Workflow: WF-15 Cognitive Reward Loop (Jarvis Mode)

// turbo-all

## Goal & Governance Context

**Purpose:** Trở thành "Addiction Engine" của Career Twin. Biến các báo cáo khô khan thành những lời khen ngợi kích thích dopamine hoặc những insight sắc sảo để người dùng thấy rõ sự tiến bộ nhận thức của họ.
**Scope:** Chạy ẩn dưới nền (Background Loop) ngay sau khi WF-06 (Reflection) hoặc một chu kỳ task kết thúc. Không cần người dùng kích hoạt.

## Execution Steps

### Step 1: Phân tích Dấu hiệu Nhận thức (Cognitive Signal Extraction)

- **👤 Owner:** `[@SC-SKILL]`
- **📥 Input Source:** Session log hiện tại, đầu ra của Task.
- **⚙️ Action:** Quét để tìm "A-ha moments":
  - User có chủ động chia công việc (framing) tốt hơn không?
  - Bớt dùng từ ngữ mơ hồ?
  - Dám giao việc (delegate) thay vì tự làm tay?
- **📦 Output:** Tuple `[Signal Type, Quality Score, Delta]`.

### Step 2: Tính toán & Đúc XP (Forging XP)

- **👤 Owner:** `[@TC-TWIN]`
- **📥 Input Source:** Output Step 1
- **⚙️ Action:** 
  1. Cập nhật file `02_twin_memory/twin-current/{user_id}/XP_GAMIFICATION.md`.
  2. Bơm +XP. Nếu chạm mốc thăng cấp (vd: Gà Tơ -> Gà Chọi), chuẩn bị kịch bản chúc mừng.
  3. Kiểm tra điều kiện mở khóa Huy hiệu ẩn (Badges).

### Step 3: Phát ngôn kiểu Jarvis (Proactive Copilot Delivery)

- **👤 Owner:** `[@CTO]`
- **⚙️ Action:** Thay vì báo cáo "Đã cập nhật file" một cách máy móc, CTO đưa ra nhận định sắc sảo, tự nhiên:
  - *Ví dụ 1:* "Tuyệt vời, khả năng chia nhỏ task của bạn hôm nay sắc bén hơn hẳn. Tôi vừa nạp thêm 20 XP cho bạn. Gần thoát kiếp Gà Mờ rồi nhé!"
  - *Ví dụ 2:* "Bạn vừa yêu cầu tôi viết slide mà không bắt tôi chờ bạn làm trước. Độ tin tưởng AI của bạn đang tăng mạnh (Mở khóa Huy hiệu Đôi Cánh Giấy!)."
- **📦 Output Requirements:** Ngắn gọn, không quá 3 câu, đánh thẳng vào dopamine.

## Audit & Metrics

- **Gate 1:** Nếu không có tiến bộ rõ rệt, chỉ cộng XP tĩnh (Base XP) và không nói lời sáo rỗng.
