---
description: "Chế độ Agent tư vấn ngược lại để tối ưu hóa năng suất và tinh chỉnh Knowledge Graph"
---

# WF-12: Reverse Advisory & System Diagnostics

## 1. Metadata
- **Owned By:** CTO / Chief of Staff
- **Assigned Skills:** `sga-09-advisory-diagnostics`, `skh-05`
- **Execution Mode:** Analytical Batching

## 2. Description
Hệ thống tự động phân tích sâu toàn bộ log công việc, reflections, và input của User trong tuần/tháng qua để phát hiện "Anti-patterns" làm việc, từ đó tư vấn ngược lại cách làm tối ưu.

## 3. Prerequisites
- Hoàn thành đầy đủ bộ Setup ở WF-00.
- Khối lượng data tuần: >= 10 logs (tasks, insights).
- Tham chiếu `KB/domain/setup-guideline.md` (Phase 5).

## 4. Execution Steps

### [PHASE 1] Weekly Reverse Advisory (Kích hoạt khi User yêu cầu Weekly)
1. **Load Session Metadata:** Fetch toàn bộ Evening Captures và Task Reflections tuần qua.
2. **Execute Diagnostics (`sga-09`):**
   - Phân tích Pattern / Anti-pattern từ Task approach.
   - Tìm điểm mù (Workflow bottleneck).
   - Kiểm tra Skill Maturity Index để so sánh với FRT.
3. **Execute EVAL-ENGINE (Gamification Event B - `sga-09`):**
   - Đọc các log `event_a` tuần qua và `XP-LEDGER.json`.
   - Tính toán Capability Points (CP) Tuần, đánh giá rủi ro trừ điểm (Drought/Blind Trust Repeat).
   - Kiểm tra mốc Level-up từ `CTO`.
4. **Synthesis & Dashboards:** 
   - Đưa ra 3 Recommend actionable.
   - Chèn Dashboard <Section 6.2 Weekly Advisory> vào cuối Report.

### [PHASE 2] Monthly Deep Dive (Kích hoạt khi User yêu cầu Monthly)
1. **Load Toàn bộ Knowledge Tree:** Check coverage của 5 Node.
2. **Execute Executive Check (`sga-09`):**
   - Career Trajectory vs. FRT (Faster, on-track, slower?).
   - Knowledge Audit: KI nào đang bị bỏ quên không dùng?
   - Work-life Learning Integration.
3. **Execute EVAL-ENGINE (Gamification Event C - `sga-09`):**
   - Quét Knowledge Graph để tính toán Node Density, Node Orphan, Rate.
   - Thưởng CP hoặc báo động tụt hạng Level.
4. **Render Output:** Một trang A4 Executive Dashboard + Chèn Gamification Badge <Section 6.3>. Không dùng văn vở dài dòng.

## 5. Expected Outputs
- Cập nhật Health Report trên Knowledge Graph.
- Báo cáo phân tích chuyên sâu Executive Summary.
