# 📋 Handover Brief: FC Online VIP Revamp (Football Complex)
**Session Date:** 11/06/2026

---

## 1. Tổng Quan Dự Án & Định Hướng UX/UI
Hệ thống **VIP Revamp** của FC Online chuyển dịch từ giao diện bảng biểu số liệu cũ sang concept **Football Complex** (Khu phức hợp bóng đá cá nhân hóa). Bản đồ hiển thị dạng Isometric Map 3D chéo, được xây dựng và tiến hóa theo thời gian dựa trên đóng góp kép của người chơi:
*   **Dual-Track Progression:** 
    *   **Pay Track (Lộ trình Nạp):** 7 Tier (Bronze / Silver / Gold / Platinum / Diamond / Top 50 / Top 5) tương ứng với 5 progression levels của tòa nhà chính (**Facility**) thay đổi mỗi tháng. Tích lũy qua Pay Tree trọn đời (không reset tháng).
    *   **Play Track (Lộ trình Chơi):** 5 Tier (Player I -> Player V + Play Top 5) tương ứng với 5 cấp độ của khu trang trí (**Decoration** - Central Plaza) dùng chung cho cả 12 block. Tích lũy qua Play Tree trọn đời.
*   **SVIP/VVIP Tower:** Tòa tháp đặc quyền tích lũy năm dương lịch (1M / 2M FC+MC), nằm ở góc bản đồ. Có cơ chế Legacy (reset mờ năm sau) và Bảo hiểm nạp Q4 (Carry-over).
*   **Hall of Fame:** Vinh danh Top 100 Pay/Play năm, MVP tháng. Đảm bảo bảo mật, quy đổi số tiền nạp sang điểm tích lũy.
*   **Share/Export:** Stats Card dạng Spotify Wrapped, highlight thành tích nổi bật để người chơi dễ dàng khoe thành quả.

---

## 2. Trạng Thái Công Việc Hiện Tại (Where We Are)

Dự án hiện đang dừng ở bước **Thiết kế chi tiết visual cho các khối Block (Facilities)** và **Rà soát lỗi Wireframe**.

### A. Tình trạng tìm Reference Materials cho 12 Facilities
Mỗi tháng đại diện cho 1 công trình đặc thù trên bản đồ 13 blocks (12 tháng + 1 Hall of Fame). Giao diện ban đầu sẽ launch **8 blocks active** (6 tháng đã qua + 2 tháng preview).

*   **🟢 ĐÃ CÓ Reference (6/12):**
    1.  **T1 (Training Ground):** Khu sân tập.
    2.  **T3 (Home Stadium):** Sân vận động chính.
    3.  **T4 (Scout Center):** Trung tâm trinh sát chuyển nhượng.
    4.  **T5 (Medical Center):** Trung tâm y tế / Phục hồi sức khỏe (thay thế Performance Lab ban đầu).
    5.  **T7 (Club Megastore):** Cửa hàng lưu niệm / Thương mại (thay thế Commercial Center ban đầu).
    6.  **T9 (Accommodation):** Khu ký túc xá / Nơi lưu trú cầu thủ.
*   **🔴 CHƯA CÓ Reference (6/12) - CẦN TÌM KIẾM TIẾP:**
    1.  **T2 (Youth Academy):** Học viện đào tạo trẻ.
    2.  **T6 (Tactical Center):** Trung tâm phân tích chiến thuật.
    3.  **T8 (Media Center):** Trung tâm truyền thông báo chí.
    4.  **T10 (Trophy Museum):** Bảo tàng cúp vinh quang.
    5.  **T11 (Champions Boulevard):** Đại lộ danh vọng.
    6.  **T12 (Grand Colosseum):** Đấu trường trung tâm vĩ đại.

---

## 3. Các Lỗi Wireframe Cần Fix (8 Issues)
Quá trình rà soát Wireframe phát hiện 8 điểm sai spec cần được điều chỉnh:
1.  **Vị trí SVIP/VVIP Tower:** Spec yêu cầu hiển thị ở góc dưới bên phải (**bottom-right**), nhưng wireframe đang vẽ ở các góc phía trên (**top corners**).
2.  **Tên mốc trên Pay Tree:** Đang hiển thị tên Tier thay vì hiển thị **số mốc nạp tích lũy** (FC/MC).
3.  **Hiển thị mốc "3,240":** Gây hiểu lầm cho user là mốc milestone quà, thực chất đây là **số điểm hiện tại** của người chơi.
4.  **Mốc đầu của Pay Tree:** Wireframe hiển thị là 1,000 FC, spec chuẩn yêu cầu là **10,000 FC**.
5.  **Progressive Reveal:** Thiếu hiệu ứng làm mờ (faded) ở mốc **+2** để gợi ý quà tiếp theo.
6.  **Badge Top 50 / Top 5:** Chưa có thiết kế mock-state cụ thể khi User đạt thứ hạng này.
7.  **Lặp chỉ số %:** Con số `82%` đang xuất hiện ở 2 nơi khác nhau trên UI với 2 ý nghĩa khác nhau.
8.  **Scope "Lịch sử Complex":** Chưa xác định nút này sẽ code ở **Phase 1** (MVP) hay lùi lại sang **Phase 3**.

---

## 4. Các Quyết Định Chưa Chốt (Follow-up Decisions)
*   **Quyết định 1:** Xác nhận việc dùng **Accommodation** thay thế cho **Club HQ** ở tháng T9 có được chấp thuận chính thức không.
*   **Quyết định 2:** Thống nhất lại vị trí hiển thị chuẩn của tòa tháp đôi **SVIP & VVIP Tower** trên Wireframe.
*   **Quyết định 3:** Chốt scope của nút **"Lịch sử Complex"** sẽ được code luôn trong Phase 1 hay đợi các phase sau.

---

## 5. Danh Sách Tài Liệu & File Bàn Giao
Hệ thống files hiện có sẵn trong thư mục `01_project_data/proj-vip-revamp/`:
*   [member-web-system-comprehensive-spec.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/member-web-system-comprehensive-spec.md): Tài liệu đặc tả tổng hợp (Single Source of Truth) của dự án.
*   [project-brief.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/project-brief.md): Tóm tắt định hướng và phân chia đầu việc.
*   [qa-testing-playbook.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/qa-testing-playbook.md): Quy trình QA & Testing chi tiết cùng tri thức vận hành.
*   [VIP_Revamp_QA_Checklist.xlsx](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/VIP_Revamp_QA_Checklist.xlsx): Master Checklist gồm 84 test cases chia theo 4 tư duy kiểm thử (BVT, Phá hoại, Tương thích, Tích hợp).
*   *Lưu ý:* Cần bổ sung file Excel quy hoạch 12 facilities, 5 mức progression levels và đặt tên (`Football_Complex_Facility_Plan.xlsx`) khi có đủ thông tin reference.

---

## 6. Kế Hoạch Cho Agent Tiếp Theo (Next Steps for Gemini)
1.  **Tìm kiếm & Đề xuất Reference Materials** cho 6 công trình còn thiếu (Youth Academy, Tactical Center, Media Center, Trophy Museum, Champions Boulevard, Grand Colosseum). Nên tìm các hình ảnh isometric, kiến trúc bóng đá hiện đại hoặc sci-fi/futuristic phù hợp với game bóng đá.
2.  **Khắc phục 8 lỗi Wireframe** bằng cách làm việc với designer/dev hoặc cập nhật spec tương ứng.
3.  **Làm việc với Supervisor/PM** để chốt 3 quyết định còn bỏ ngỏ ở Mục 4.
4.  **Hoàn thiện File `Football_Complex_Facility_Plan.xlsx`** ghi nhận chi tiết mô tả kiến trúc 5 cấp độ của cả 12 công trình.
