# 📖 HƯỚNG DẪN NGHIÊN CỨU & KHAI THÁC BỘ AI SKILLS (SEA SKILLS)
> **Chủ sở hữu:** Coby (Strategy & Operations - FCO Team)  
> **Nguồn gốc:** Chuyển giao từ team Arena of Valor (AoV - Liên Quân Mobile) và tái cấu trúc cho FC Online (FCO)  
> **Đường dẫn tài liệu:** `Garena/sea-skills-guide.md`  

---

## 📂 1. TỔNG QUAN VỀ 2 THƯ MỤC MỚI NHẬN

Hệ thống vừa tiếp nhận 2 thư mục đóng vai trò là **"lò rèn năng lực AI" (AI Skills Forge)** để tối ưu hóa công việc của bạn tại Garena:

1.  **`ai-skill-for-non-tech/` (Thư mục Wrapper - Công cụ Quản lý):**
    *   *Bản chất:* Là một repository quản lý phiên bản và đồng bộ hóa các AI Skills.
    *   *Thành phần quan trọng:* Chứa các script tự động hóa viết bằng Python/Batch (như `sync-local.cmd`, `package-claude.cmd`) giúp người không chuyên code (Non-Tech) có thể đóng gói, cài đặt và đồng bộ hóa các AI skills giữa mã nguồn (Git) và môi trường runtime của AI Agent.
2.  **`skills/skills/` (Thư mục Source - Chứa lõi kỹ năng):**
    *   *Bản chất:* Chứa **27 kỹ năng AI** đã được chuẩn hóa theo định dạng **Canonical 4-Tier Spec** (mỗi thư mục con đều có 1 file `SKILL.md` chi tiết). Đây chính là tập hướng dẫn hành vi để AI Agent của bạn học và thực thi nhiệm vụ.

---

## 🗺️ 2. PHÂN LOẠI & MAPPING 27 SKILLS SANG BỐI CẢNH FC ONLINE (FCO)

Để bạn dễ hình dung, 27 kỹ năng này được chia thành **5 nhóm nghiệp vụ chính** phục vụ trực tiếp cho công việc của bạn tại FCO:

### Nhóm A: Thiết kế & Tối ưu hóa UI/UX (Design & Interface)
*Dành cho Coby khi làm việc với designer (Anh Thế Minh) hoặc tối ưu hóa giao diện web sự kiện.*

| Tên Skill cũ | Chức năng cốt lõi | Cách Coby tận dụng cho FC Online (FCO) |
| :--- | :--- | :--- |
| **`design-uiux`** | Thiết kế UI/UX cấp page và feature dựa trên design system. | Dùng để tự thiết kế layout nháp cho các Tab của trang VIP Revamp hoặc các monetize web event mới trước khi request Design. |
| **`clone-reference-ui`**| Sao chép UI tham chiếu để dựng lại giao diện demo. | Dùng để clone/học hỏi cấu trúc web event của Nexon (Hàn Quốc) hoặc các nhà phát hành khác về chạy thử nghiệm ở Việt Nam. |
| **`govern-layout`** | Định nghĩa cấu trúc khung trang (app shell, layout blueprint). | Quy chuẩn giao diện cho các tool vận hành nội bộ như cổng FCO Portal. |
| **`design-system-antd`**| Quản lý design language Ant Design (Antd 6 tokens). | Giữ tính đồng nhất visual khi AI dựng trang quản trị/CS tool cho FCO. |
| **`work-with-agentation`**| Nhận diện và xử lý annotation (visual feedback) trên UI. | Trao đổi visual bug trực quan với team frontend khi test giao diện. |

---

### Nhóm B: Đặc tả & Logic Nghiệp vụ (Spec & Business Logic)
*Dành cho Coby khi viết đặc tả sản phẩm (Product Spec) và brief cơ chế game cho Dev.*

| Tên Skill cũ | Chức năng cốt lõi | Cách Coby tận dụng cho FC Online (FCO) |
| :--- | :--- | :--- |
| **`write-specs`** | Viết spec chi tiết cho nội bộ PM, FE, BE, QA. | Áp dụng viết spec tích hợp các tool nội bộ (như Tool TTCN, Auto-report). |
| **`brief-logic`** | Viết mô tả logic nghiệp vụ bằng ngôn ngữ tự nhiên. | **Cực kỳ quan trọng:** Dùng để brief cho Dev về logic tính điểm chơi (Play Track), cách quay thưởng, progressive reveal mà không cần biết code. |
| **`analyze-gap`** | Phân tích chênh lệch giữa UI thật, spec và source code. | Dùng để đối chiếu trang VIP Revamp thực tế sau khi code xong so với Spec v1.0 để tìm điểm thiếu sót. |
| **`diagram-mermaid-outline`**| Vẽ sơ đồ Mermaid cho workflow, RACI, ownership. | Tự động hóa vẽ sơ đồ luồng đi của sự kiện (Event User Flow) để trình bày trong slide báo cáo gửi anh Khôi hoặc anh Chí Công. |

---

### Nhóm C: Kiểm thử & Đảm bảo Chất lượng (QA & Test Automation)
*Dành cho Coby (chủ trì QA) phối hợp cùng Khoa để kiểm thử 84+ test cases trang VIP.*

| Tên Skill cũ | Chức năng cốt lõi | Cách Coby tận dụng cho FC Online (FCO) |
| :--- | :--- | :--- |
| **`test-website`** | Test website tự động qua trình duyệt. | Tự động mở browser click test các nút claim quà của trang VIP trên môi trường Staging. |
| **`use-cdp-browser`** | Điều khiển browser qua CDP để chụp ảnh và đọc DOM. | Tự động chụp màn hình các lỗi visual UI/UX làm bằng chứng gửi Dev sửa. |
| **`review-frontend`** | Audit chất lượng frontend, design consistency. | Đánh giá độ khớp visual giữa mockup thiết kế của anh Thế Minh và sản phẩm code của team Dev. |

---

### Nhóm D: Điều phối & Quản lý Phân phối (Delivery Management)
*Dành cho Coby khi điều phối tiến độ dự án liên phòng ban.*

| Tên Skill cũ | Chức năng cốt lõi | Cách Coby tận dụng cho FC Online (FCO) |
| :--- | :--- | :--- |
| **`aov-delivery-agent`**| **[Cần đổi tên thành `fco-delivery-agent`]** Điều phối vận hành AoV Card Game. | **Tái cấu trúc:** Dùng để AI tự lập kế hoạch chạy event FCO (đọc docs, tạo task, theo dõi code, chạy QA và xuất tài liệu). |
| **`ugc-delivery-agent`**| Điều phối frontend cho UGC Website. | Sử dụng làm workflow mẫu để điều phối phát triển các trang cộng đồng tự tạo nội dung (UGC). |
| **`document-delivery`** | Viết changelog, handoff doc và operational doc. | Tự động soạn thảo báo cáo bàn giao cuối tuần (Secretary Session Report) hoặc hướng dẫn CS (CS Cheat sheet). |
| **`sync-task-status`** | Đồng bộ trạng thái task, build history và delivery log. | Tự động cập nhật bảng công việc thử việc trong file `garena-tasks.md`. |

---

### Nhóm E: Tương tác với Hệ thống & Tools của Garena (Tooling & Integration)
*Dành cho Coby khi cập nhật Plane (Jira), Outline (Wiki), Notion và code tool.*

| Tên Skill cũ | Chức năng cốt lõi | Cách Coby tận dụng cho FC Online (FCO) |
| :--- | :--- | :--- |
| **`work-with-garena-tools`**| MCP gateway điều phối Plane, Outline, Demo System. | Route toàn bộ các yêu cầu cập nhật công việc nội bộ qua AI. |
| **`work-with-plane`** | Quản lý dự án, backlog trên Plane (Jira của Sea). | Tự động tạo và cập nhật các task của dự án VIP Revamp lên Plane. |
| **`work-with-outline`** | Đọc/ghi wiki Outline của Garena. | Tìm kiếm nhanh các policy về IT/Security hoặc quy trình cài đặt quà in-game của Garena trên Outline. |
| **`work-with-notion`** | Quản lý page trên Notion. | Đồng bộ note cá nhân và tài liệu ôn tập meta game. |
| **`work-with-demo-system`**| Deploy và kiểm tra database trên Demo System. | Deploy bản wireframe html chạy thử lên server demo nội bộ để gửi link cho anh Khôi duyệt. |
| **`organize-project-kb`**| Sắp xếp Outline KB theo module và trạng thái. | Dọn dẹp và tổ chức lại kho tri thức vận hành của FCO. |
| **`outline-memory-ops`**| Quản lý memory thông tin dự án trên Outline. | Đọc và lưu trữ thông tin ghi nhớ dài hạn từ wiki công ty. |
| **`manage-git`** | Thao tác Git an toàn cho PM/Ops. | Push mã nguồn các tool vận hành nội bộ (như fco-portal) lên Git Garena. |
| **`build-frontend`** | Triển khai frontend cho internal tool. | AI tự động code giao diện cho các tool vận hành phụ trợ của Coby. |
| **`manage-skills`** | Đồng bộ và publish AI skills lên Git. | Quản lý, đóng gói và chia sẻ các skill AI mới mà bạn phát minh. |

---

## ⚙️ 3. CÁCH CƠ BẢN ĐỂ COBY TẬN DỤNG & VẬN HÀNH BỘ TOOLKIT NÀY

### Bước 1: Đồng bộ hóa Skill vào môi trường chạy của Agent (Local Runtime)
Hệ thống script trong `ai-skill-for-non-tech/` cho phép bạn cài các skill này vào AI Agent (Claude/Codex) đang chạy trên máy bạn:
1.  Mở PowerShell tại thư mục `ai-skill-for-non-tech/ai-skill-for-non-tech`.
2.  Chạy lệnh sau để kiểm tra sự chênh lệch (diff) giữa thư mục nguồn và runtime của Agent:
    ```powershell
    ./sync-local.cmd --direction push --skill brief-logic --target claude
    ```
3.  Nếu muốn đồng bộ thực sự (ghi đè), thêm tham số confirm:
    ```powershell
    ./sync-local.cmd --direction push --skill brief-logic --target claude --confirm yes
    ```
*(Lưu ý: Lệnh này giúp AI Agent của bạn cập nhật ngay lập tức các chỉ dẫn hành vi mới nhất).*

### Bước 2: Đóng gói và phát hành khi cập nhật Skill
Khi bạn chỉnh sửa file `SKILL.md` của một kỹ năng nào đó trong thư mục nguồn:
1.  Chạy file `package-claude.cmd` để tự động đóng gói kỹ năng đó vào thư mục phân phối `dist/claude-skills/`.
2.  Sau đó chạy `publish-skill.cmd --skill <tên-skill>` để đẩy bản cập nhật lên hệ thống Git chung.

### Bước 3: Tách và đổi tên skill từ AoV sang FCO
Vì bộ kỹ năng này có xuất phát điểm từ team Liên Quân (AoV):
1.  Bạn có thể copy thư mục `skills/skills/aov-delivery-agent` sang thư mục mới tên là `skills/skills/fco-delivery-agent`.
2.  Mở file `SKILL.md` bên trong và sửa các thuật ngữ "AoV Card Game" thành "FCO Web Events/Monetization" để AI Agent hiểu đúng quy trình của game bóng đá thay vì game thẻ bài.
