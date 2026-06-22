# 📋 Project Brief: FC Online VIP Revamp (proj-vip-revamp)

> **Chủ quản:** Coby (Strategy & Operations)  
> **Người duyệt / Supervisor:** Anh Trần Minh Khôi (PM FCO)  
> **Mục tiêu:** Vận hành, thiết kế và tối ưu hóa hệ thống VIP Revamp mới chuẩn bị cho ngày ra mắt.  
> **Hạn chót launch:** Dự kiến 01/07/2026 (Lưu ý ngày 12/06: Có thể linh động lùi launch khoảng 2 tuần để tối ưu thiết kế và QA, không nhất thiết phải air sớm 01/07).  
> **Trạng thái hiện tại:** Đã hoàn thành bộ References kiến trúc cho 6/12 công trình chính gửi Design Lead; đã log 8 lỗi Wireframe vào Master QA Checklist; đang đợi Design lên bản vẽ concept chi tiết.  

---

## 1. 🎯 Tổng Quan & Concept Thiết Kế

Concept cốt lõi của dự án VIP Revamp lần này là **Football Complex** (Khu phức hợp bóng đá cá nhân hóa). 

Khu phức hợp này sẽ được xây dựng và phát triển dần theo thời gian thực tế, phản ánh trực tiếp hành trình đầu tư nạp thẻ (Pay) và cống hiến chơi game (Play) dài hạn của từng huấn luyện viên, thay vì cơ chế reset hoàn toàn mỗi tháng như hệ thống VIP cũ.

---

## 2. 🏗️ Cấu Trúc Hệ Thống VIP Mới (Dual Track)

Hệ thống vận hành theo mô hình **Đường chạy kép (Dual Track)** song song để đảm bảo cân bằng game và giữ chân cả người chơi nạp thẻ lẫn cày chay:

### A. Pay Track (Lộ trình Nạp tích lũy)
Tích lũy dài hạn qua **Pay Tree** (không reset hàng tháng).
*   **7 Tier phân hạng:** Bronze / Silver / Gold / Platinum / Diamond / Top 50 / Top 5.
*   **SVIP/VVIP Tower:** Mốc nạp năm (1M FC+MC cho SVIP và 2M FC+MC cho VVIP). Tháp sẽ hiển thị cố định ở một góc trong Complex dưới dạng biểu tượng Tower đặc quyền, có cơ chế "Legacy" (mờ đi khi qua năm mới) và Bảo hiểm nạp Q4 (Carry-over).

### B. Play Track (Lộ trình Chơi tích lũy)
Tích lũy dài hạn qua **Play Tree** (không reset hàng tháng, tách biệt hoàn toàn tiền tệ với Pay Zone để giữ tính công bằng).
*   **5 Tier phân hạng:** Player I → Player II → Player III → Player IV → Player V.
*   **Play Top:** Bậc vinh danh cao nhất (Play Top 5).

---

## 3. 🏟️ Cơ Chế Hoạt Động Của Football Complex

Bản đồ Complex hiển thị dưới dạng Isometric Map góc nhìn chéo từ trên xuống:
*   **13 Blocks tổng cộng:** Gồm 12 Block công trình đại diện cho 12 tháng trong năm + 1 Block cố định dành cho Sảnh Danh Vọng (**Hall of Fame**).
*   **Lộ trình Launch đợt đầu (Phase 1):** 6 tháng đã qua (build xong) + 2 tháng kế tiếp (hiển thị preview) = **8 Blocks active**.
*   **Cấu trúc 2 Layer của mỗi Block:**
    1.  **Facility (Cơ sở vật chất - Pay-driven):** Tòa nhà chính của tháng đó. Có **5 cấp độ thiết kế (progression levels)** tương ứng với mức độ nạp thẻ (Bronze $\rightarrow$ Diamond).
    2.  **Decoration (Trang trí xung quanh - Play-driven):** Các chi tiết ngoại cảnh (Central Plaza) như cây cối, đài phun nước, thảm cỏ. Có **5 cấp độ thiết kế** tiến hóa dựa trên thời gian/tier chơi game của User.
*   **Độ mượt mà của Progression:**
    *   *Chiều ngang (Thời gian):* Sang tháng mới sẽ mở khoá thêm 1 slot đất mới trên bản đồ.
    *   *Chiều dọc (Tier):* Nạp/chơi càng nhiều thì nâng cấp tòa nhà và ngoại cảnh càng hoành tráng.
*   **Triết lý "Decent Bronze":** Visual design của các toà nhà Bronze (cấp thấp) vẫn được thiết kế tươm tất, chỉn chu để người chơi không có cảm giác "xấu hổ" khi khoe bản đồ.
*   **Tính năng Share/Export:** Thiết kế tính năng **Stats Card** lấy cảm hứng từ *Spotify Wrapped* (tóm tắt các mốc thành tích nổi bật nhất thay vì chụp ảnh thô toàn bộ map) để người chơi dễ dàng chia sẻ lên MXH.

---

## 4. 📂 Danh Sách 12 Facilities & Trạng Thái References (Cập nhật 12/06/2026)

Dựa trên tài liệu references chi tiết tại [[FCO VIP] Facilities Design references.pptx](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/Garena/%5BFCO%20VIP%5D%20Facilities%20Design%20references.pptx), dưới đây là bảng quy hoạch 12 tháng và tiến độ tìm tài liệu tham khảo:

| Tháng | Tên Facility | Cấp độ progression trong PPTX | Trạng thái References (References Status) | Ghi chú & Chi tiết kiến trúc |
|---|---|---|---|---|
| **T1** | **Training Ground** | Tòa số 2 (Slide 10-11) | 🟢 ĐÃ CÓ (Bronze - Diamond) | Sân đơn cỏ cơ bản $\rightarrow$ 2 sân + phòng thay đồ $\rightarrow$ "Pitch Matrix" campus (sân trong nhà + ngoài trời, bảo dưỡng tự động). |
| **T2** | **Youth Academy** | Tòa số 3 (Slide 13-14) | 🟡 ĐÃ CÓ (Khuyết Lv4 Platinum) | Sân nhỏ + kho thiết bị $\rightarrow$ Nhà học viện trung bình mái ngói đỏ $\rightarrow$ Elite campus (Học viện Crystal Palace). *Cần thêm ref cho Lv4*. |
| **T3** | **Home Stadium** | Tòa số 1 (Slide 4-8) | 🟢 ĐÃ CÓ (Bronze - Diamond) | Sân cỏ trống $\rightarrow$ Khán đài 1-2 tầng $\rightarrow$ Khán đài kín 4 mặt $\rightarrow$ Sân Turf Moor (Lv4) $\rightarrow$ Mega-stadium Allianz Arena/Santiago Bernabeu (Lv5). |
| **T4** | **Scout Center** | Chưa có trong PPTX | 🔴 CHƯA CÓ | Trung tâm trinh sát chuyển nhượng. Cần tìm bổ sung. |
| **T5** | **Medical Center** | Tòa số 4 (Slide 16-17) | 🟢 ĐÃ CÓ (Bronze - Diamond) | Phòng khám 2 tầng xanh trắng $\rightarrow$ Có sảnh đón $\rightarrow$ 3 tầng kính có bể thủy trị liệu $\rightarrow$ Cryo trên mái $\rightarrow$ "Sleep Hotel" hồi phục có bể bơi vô cực. |
| **T6** | **Tactical Center** | Chưa có trong PPTX | 🔴 CHƯA CÓ | Trung tâm phân tích chiến thuật. Cần tìm bổ sung. |
| **T7** | **Club Megastore** | Tòa số 6 (Slide 21-22) | 🟢 ĐÃ CÓ (Bronze - Diamond) | Kiosk nhỏ navy $\rightarrow$ Cửa hàng độc lập $\rightarrow$ Carolina Core FC retail $\rightarrow$ Flagship store kính 3 phần có tháp thương hiệu. |
| **T8** | **Media Center** | Chưa có trong PPTX | 🔴 CHƯA CÓ | Trung tâm truyền thông báo chí. Cần tìm bổ sung. |
| **T9** | **Accommodation** | Tòa số 8 (Slide 25-26) | 🟡 ĐÃ CÓ (Khuyết Lv5 Diamond) | Ký túc xá module vàng ấm $\rightarrow$ Khối nhà 2 tầng $\rightarrow$ Khách sạn 3 tầng $\rightarrow$ Boutique hotel có vườn thượng uyển. *Cần lên ý tưởng cho Lv5*. |
| **T10** | **Trophy Museum** | Tòa số 5 (Slide 18) | 🔴 CHƯA CÓ | Bảo tàng cúp. Slide 18 note: Dạng building thương mại tiêu chuẩn, visual đi theo branding của Club. Cần chốt visual direction. |
| **T11** | **Champions Boulevard**| Chưa có trong PPTX | 🔴 CHƯA CÓ | Đại lộ danh vọng. Cần tìm bổ sung. |
| **T12** | **Grand Colosseum** | Chưa có trong PPTX | 🔴 CHƯA CÓ | Đấu trường trung tâm vĩ đại. Cần tìm bổ sung. |

*   **T7 - Performance Tech Centre (Slide 23):** Thuộc nhóm building thương mại tiêu chuẩn, không cần kiến trúc đặc thù, thiết kế tương tự Megastore/Museum nhưng thay đổi màu nhận diện thương hiệu.

---

## 5. 🛠️ Rà Soát Wireframe & Kế Hoạch QA (Cập nhật 12/06/2026)

Toàn bộ **8 lỗi thiết kế Wireframe** đã được tích hợp và phân loại cụ thể vào file Master Checklist [VIP_Revamp_QA_Checklist.xlsx](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/VIP_Revamp_QA_Checklist.xlsx) theo 4 tư duy kiểm thử nghiệp vụ để chuẩn bị cho quá trình QA:

1.  **Vị trí SVIP/VVIP Tower (ID: `WF-01` - UI/UX Layout):** Wireframe vẽ ở top corners, spec yêu cầu bottom-right.
2.  **Tên mốc trên Pay Tree (ID: `WF-02` - Boundary Value Testing):** Đang hiện tên Tier thay vì hiển thị số mốc nạp tích lũy (FC/MC).
3.  **Hiển thị mốc "3,240" (ID: `WF-03` - System Integration):** Gây hiểu lầm cho user là mốc quà, thực chất đây là số điểm hiện tại của người chơi.
4.  **Mốc đầu của Pay Tree (ID: `WF-04` - Boundary Value Testing):** Wireframe vẽ mốc đầu là 1,000 FC, spec chuẩn yêu cầu là 10,000 FC.
5.  **Cây quà Progressive Reveal (ID: `WF-05` - UI/UX Layout):** Thiếu hiệu ứng làm mờ (faded) ở mốc +2 để gợi ý quà tiếp theo.
6.  **Badge Top 50 / Top 5 (ID: `WF-06` - UI/UX Layout):** Chưa có thiết kế mock-state cụ thể khi User đạt thứ hạng này.
7.  **Lặp chỉ số % (ID: `WF-07` - UI/UX Layout):** Trùng lặp con số 82% hiển thị cho 2 tiến trình khác nhau trên UI.
8.  **Scope "Lịch sử Complex" (ID: `WF-08` - Scope Boundaries):** Chưa chốt rõ ràng nút này sẽ code ở Phase 1 (MVP) hay lùi lại sang Phase 3.

---

## 📝 Các Quyết Định Chưa Chốt (Follow-up Decisions)

*   **Quyết định 1:** Xác nhận việc dùng **Accommodation** thay thế cho **Club HQ** ở tháng T9 có được chấp thuận chính thức không.
*   **Quyết định 2:** Thống nhất lại vị trí hiển thị chuẩn của tòa tháp đôi **SVIP & VVIP Tower** trên Wireframe.
*   **Quyết định 3:** Chốt scope của nút **"Lịch sử Complex"** sẽ được code luôn trong Phase 1 hay đợi các phase sau.

---

## 📂 Danh Sách File Đầu Ra Đã Tạo (Handover Assets)

*   [member-web-system-comprehensive-spec.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/member-web-system-comprehensive-spec.md): Tài liệu đặc tả tổng hợp (Single Source of Truth) của dự án.
*   [qa-testing-playbook.md](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/qa-testing-playbook.md): Quy trình QA & Testing chi tiết cùng tri thức vận hành.
*   [VIP_Revamp_QA_Checklist.xlsx](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/01_project_data/proj-vip-revamp/VIP_Revamp_QA_Checklist.xlsx): File Master Checklist gồm 84 test cases + 8 lỗi Wireframe mới cập nhật.
