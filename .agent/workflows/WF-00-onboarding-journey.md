---
description: "Dẫn dắt User qua 5 Phase của hệ thống Setup Second Brain & Daily Operations"
---

# WF-00: Solopreneur Onboarding & Setup Journey

## 1. Metadata
- **Owned By:** CTO / Quality Gate Facilitator
- **Assigned Skills:** `sga-08-setup-architect`, `skh-05`
- **Execution Mode:** Multi-Stage Interactive (Hard-Gate)

## 2. Description
Hệ thống dẫn dắt tự động giúp số hóa "DNA làm việc" của User mới theo chuẩn Solopreneur. Biến những câu hỏi Onboard khô khan thành các chuỗi Khởi tạo Knowledge Graph, System Prompt Design và Workflow số hóa thực tế.

## 3. Prerequisites
- Workspace mới khởi tạo hoặc User yêu cầu "Begin Setup Guideline".
- Tham chiếu chặt chẽ file `KB/domain/setup-guideline.md`.

## 4. Execution Steps

### [STAGE 1] Khởi tạo Mục đích & DNA (Phase 1 Guideline)
1. Kích hoạt hỏi User khai báo Mục đích (Module 1.1).
2. Xử lý PROMPT NAP DNA CONG VIEC (Module 1.2).
   - *Logic:* Gọi `sga-08` phân tích điểm mạnh cấu trúc, nhận diện quy trình yếu. Không comment suông, PHẢI output ra thiết kế "Cách tôi sẽ support bạn".
3. Thiết lập Future Role Twin (Module 1.3). Map các skills vào chuẩn 5 Dimensions.
4. Điều hướng User ngay lập tức vào Task thật (Lab 1) bằng WF-01.

### [STAGE 2] Khởi tạo Second Brain & Gamification Engine (Phase 2 Guideline)
1. Thu thập Input theo "PROMPT SECOND BRAIN SETUP".
2. Khởi tạo Ma trận 5 Nodes: Skills, Projects, People, Knowledge, Goals.
   - *Hard-Gate:* Không được đi tiếp nếu Graph chưa map xong ít nhất 2 Nodes.
3. Kích hoạt **Gamification Init (`sga-08`)**: Bắt đầu sinh ra Virtual Vault chứa `XP-LEDGER.json` và phân hạng ở Level "THE INTERN".
4. Chốt chuẩn Daily Input Ritual (Morning, Evening, Quick Capture shortcut). 

### [STAGE 3] Bắt đầu Process Digitization Interview (Phase 2.3)
1. Thảo luận bóc tách 1 quy trình làm việc thường ngày.
2. Vẽ sơ đồ "Standardize -> Augment -> Automate".
3. RENDER Raw Markdown để User copy và lưu vào `.agent/skills/`.

### [STAGE 4] Quick Settings Calibration
1. Hiển thị bảng điều khiển `QUICK SETTINGS DASHBOARD` từ bản đặc tả Settings Engine (`KB/domain/settings-engine-spec.md`).
2. Yêu cầu User xác nhận 5 cấu hình tùy biến cơ bản (Tone, Challenge, Language, Address, Gamification) để chốt sổ quá trình Onboard.

## 5. Expected Outputs
- Node `CST` (Current State Twin) và `FRT` (Future Role Twin) được thiết lập.
- Knowledge Graph 5 Nodes tạo móng hoàn thành.
- Hệ thống Gamification được kích hoạt thành công (User xếp hạng **Level 1: THE INTERN** với 0 XP).
- User có 1 Skill thô đầu tiên sau khi phỏng vấn Process Digitization.
