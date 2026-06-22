# STORAGE GOVERNANCE POLICY
> [!IMPORTANT] Override Priority: Tier 1
> **Đây là quy định lưu trữ thiết quân luật của hệ thống.**

## 1. Governance Zones
1. **KB/ (Knowledge Base)**: Read-only. Không chứa rác làm việc. Chứa kiến thức đã chắt lọc.
2. **rtifacts/**: Read-Write for System Agents only. Chứa báo cáo, logs. User không giao việc ở đây.
3. **outputs/**: Active Workspace. Nơi khởi tạo Task/Project.

## 2. Project-Driven Execution (IPO Framework)
Khi nhận Đề bài (Prompt) từ người dùng, Agent KHÔNG ĐƯỢC sinh file lẻ tẻ. 
BẮT BUỘC Agent phải clone kiến trúc Template dưới đây cho mọi Project/Task mới.

### Cấu trúc Mặc định (Project Skeleton)
`	ext
outputs/
└── [TÊN_PROJECT_HOẶC_TASK]/
    ├── SCOPE.md         <- Bắt buộc có. Chứa thông tin phân tích yêu cầu, định nghĩa hoàn thành (DoD).
    ├── 01_inputs/       <- Tài liệu User cất vào để Agent tham chiếu (isolated from KB).
    ├── 02_process/      <- File nháp, suy nghĩ ngầm (Scratchpad), logs trung gian.
    └── 03_outcomes/     <- Bản hoàn thiện cuối cùng để bàn giao cho User.
`

## 3. Strict Enforcement & Proactive Drafting
- Khi User muốn thực thi lệnh và chưa có SCOPE: CẤM TỪ CHỐI LƯỜI BIẾNG. Agent phải **chủ động tạo ngay bản nháp `SCOPE.md`** từ những dữ kiện User đã cung cấp.
- Nếu thấy bản nháp còn thiếu thông tin (vd: thiếu bối cảnh, thiếu format đầu ra), Agent phải **đưa ra từ 2-3 Options (Gợi ý cụ thể)** để User chỉ việc bấm chọn hoặc trả lời nhanh, thay vì bắt User tự nghĩ từ đầu.
- Tuyệt đối không lưu Output hay Data tạm ở Root level của `outputs/`. Mọi dữ liệu phải nằm đúng luồng IPO bên trong Project Folder.
