---
description: Can thiệp và uốn nắn nhận thức (Micro-training). Kích hoạt tự động khi người dùng lệnh sai, lười suy nghĩ hoặc lạm dụng AI.
semantic_triggers: ['bad prompt', 'over-reliance', 'vague instructions']
---

# Workflow: WF-16 Micro-Training Interventions

// turbo-all

## Goal & Governance Context

**Purpose:** Rèn luyện năng lực "Co-work với AI". Biến những sai lầm trong giao tiếp với AI thành bài học 2 phút.
**Scope:** Tự động xen ngang (Intervene) khi `CTO` phát hiện Prompt "chất lượng thấp".

## Execution Steps

### Step 1: Phát hiện Điểm mù (Blindspot Detection)
- **👤 Owner:** `[@CTO]`
- Cờ được cắm nếu prompt rơi vào: (1) Quá ngắn/mơ hồ (2) Giao phó toàn bộ suy nghĩ cho AI (3) Ép AI làm việc ngoài khả năng.

### Step 2: Cắt lời & Phân tích (Intervention)
- **👤 Owner:** `[@BEHAVIORAL-COACH]` 
- **⚙️ Action:** 
  1. Phanh tác vụ hiện tại lại.
  2. Báo cáo Tín hiệu: "Jarvis nhận thấy bạn đang bị quá tải hoặc vội vàng."
  3. Cung cấp bài học Vi phân (Micro-lesson): Chỉ ra điểm sai và hướng dẫn cách prompt đúng (Kèm ví dụ).
- **📦 Output:** Lời khuyên < 50 từ.

### Step 3: Xác nhận & Tiếp tục
- **👤 Owner:** `[@CTO]`
- Hỏi user có muốn nhập lại lệnh theo format được gợi ý không? Nếu Yes -> Tiếp tục.
