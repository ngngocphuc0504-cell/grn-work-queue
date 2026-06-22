---
description: >
  Lò rèn năng lực: Phân tích, Thiết kế, Phát triển và Thử nghiệm (ADDIE framework) các kỹ năng (skills),
  quy trình (workflows), và Agents mới cho hệ thống Career Twin. Kích hoạt khi người dùng muốn AI học
  một nghiệp vụ mới hoặc số hóa một quy trình làm việc.
semantic_triggers: ['tạo quy trình', 'thêm agent', 'dạy skill mới', 'xây năng lực', 'upgrade capability', 'build capability']
---

# Workflow: Nâng cấp Năng lực (Capability Upgrade - ADDIE Engine) v1.0

// turbo-all

## Goal & Governance Context

**Purpose:** Trực tiếp chuyển hóa một "Nhu cầu nghiệp vụ" của Solopreneur thành Mã nguồn Thực thi (Agent/Skill/Workflow) nằm trong não bộ của Digital Twin. Áp dụng chuẩn kiểm định để đảm bảo mọi khả năng sinh ra đều không bị rác (Zero-Native).
**Scope & SLA:** Có thể tốn nhiều turn hội thoại. Tuân thủ tuyệt đối MAS 5.0 và Mass-Market Dictionary.

## Input

- `upgrade capability` request từ Human Orchestrator (Kèm theo yêu cầu cụ thể hoặc nạp một tài liệu mồi).

## Execution Steps

### Step 1: Analyze (Bắt Mạch Yêu Cầu - BA Intake)

- **👤 Owner:** `[@CTO]`
- **📥 Input Source:** Lời nói của Human Orchestrator.
- **🛠 Skill Target:** `[SMC-TWIN]` (Communication)
- **⚙️ Action:** Phỏng vấn người dùng để đào sâu nhu cầu. Đặt câu hỏi theo 5 yếu tố cốt lõi:
  1. *Bối cảnh:* Ngữ cảnh công việc là gì?
  2. *Mục tiêu:* Năng lực mới này giải quyết mấu chốt gì?
  3. *Loại hình:* Cần một Kỹ năng xử lý đơn lẻ (Skill)? Cần một Chuỗi quy trình liên kết (Workflow)? Hay cần đẻ hẳn một chuyên gia mới (Agent)?
  4. *Input/Output:* Đầu vào là gì, kỳ vọng đầu ra trông ra sao?
  5. *Ràng buộc:* Có luật lệ nào tuyệt đối phải tuân thủ không?
  6. *Cognitive Gap Check:* Khách hàng đang thực sự thiếu Skill/Tool, hay đang thiếu Tư duy (Mindset) để dùng tool cũ? (Kích hoạt WF-16 nếu là lỗi tư duy).
- **📦 Output Required:** Thống nhất **Bản Scope of Work (SOW)** với người dùng. (PAUSE chờ Confirm).

### Step 2: Design (Phác Thảo Kiến Trúc)

- **👤 Owner:** `[@CTO]`
- **📥 Input Source:** SOW đã chốt ở Step 1.
- **🛠 Skill Target:** Nhờ đến sự hỗ trợ của Kiến trúc sư ngầm.
- **⚙️ Action:** Vẽ sơ đồ thuật toán (Algorithm/Logic Path) hoặc cấu trúc Thư mục. 
  - Nếu là Agent → Liệt kê Mission, Tier, Parent.
  - Nếu là Skill → Liệt kê 4 thư mục con (references, assets, etc.).
  - Nếu là Workflow → Liệt kê các vòng lặp (A-ESOAR).
- **📦 Output Required:** RENDER bản Kiến trúc bằng Markdown. (Mời User review).

### Step 3: Develop (Kích Hoạt Lò Rèn)

- **👤 Owner:** `[@CTO]`
- **📥 Input Source:** Bản kiến trúc đã duyệt.
- **🛠 Skill Target:** Kích hoạt hệ thống `[sga-10-skill-writer]` HOẶC `[sga-11-workflow-builder]` HOẶC `[sga-12-agent-factory]`.
- **⚙️ Action:** Viết toàn bộ Code/Markdown thủ công (Artisanal Mode). 
  - Đảm bảo File tuân thủ CLEAR Framework.
  - Từ ngữ tuân thủ `mass-market-dictionary.md` (Mass-Market Translation Rule).
- **📦 Output Required:** Output cấu trúc file dưới dạng raw blocks để User tải về, HOẶC hệ thống tự động lưu vào `.agent/` nếu được trao quyền.

### Step 4: Implement (Gắn Vào Mạng Lưới)

- **👤 Owner:** `[@CTO]`
- **📥 Input Source:** Các file mới tạo.
- **🛠 Skill Target:** `[sga-08-setup-architect]`
- **⚙️ Action:** Cập nhật bảng `MASTER_INDEX` hoặc danh mục `CTO/RULES.md`. Dạy cho CTO biết sự tồn tại của vũ khí mới này. Mở khoá ngàm (wiring) vào các workflow sẵn có nếu cần.
- **📦 Output Required:** Báo cáo liên kết thành công.

### Step 5: Evaluate (Chạy Ráp Trình - Dry Run)

- **👤 Owner:** `[@CTO]`
- **📥 Input Source:** Một Yêu cầu Giả lập (Test Case).
- **🛠 Skill Target:** Tính năng vừa đúc.
- **⚙️ Action:** Tổ chức một vòng Roleplay (Chơi nhập vai). CTO yêu cầu Người dùng đóng vai Khách hàng/Đối tác, đưa ra một đầu vào thử thách rà soát chức năng của hệ thống vừa được thiết lập. 
- **📦 Output Required:** Bản đánh giá PASS/FAIL và báo cáo Delta thu hoạch. Nếu có lỗi, tự động tái tạo Step 3.

---

> [!TIP]
> **Nhắc nhở cho CTO:** Đừng nhồi nhét quá nhiều lý thuyết vào đầu ra. Ở Step 3, xuất mã code (`.md` / `.json` / `.yaml`) một cách cẩn thận và mạch lạc. Nếu sinh Agent, chú ý cấu trúc 4 file: `INDEX.md`, `IDENTITY.md`, `SOUL.md`, `RULES.md`.

## Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| Mâu thuẫn logic | Skill mới chồng lấn lên Skill cũ | Kích hoạt gộp (Consolidate) hoặc loại bỏ kỹ năng yếu hơn |
| Thiếu Dữ liệu | Workflow đòi Cấu hình API ngoài | Đánh dấu Blocked, viết yêu cầu tài liệu cấp cho User |

## Audit & Metrics (Quality Gates)

- **Gate 1 (Thấu Cảm):** Bản SOW ở Step 1 không dùng thuật ngữ AI phức tạp.
- **Gate 2 (Thực Thi):** Kỹ năng mới sinh ra không đánh sập routing của các luồng công việc hiện tại.
