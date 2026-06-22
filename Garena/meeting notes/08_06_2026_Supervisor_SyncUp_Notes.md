# 📝 Garena FCO — Biên bản Họp Sync-up với Supervisor

> **Thời gian:** 08/06/2026 (Ngày đầu Onboarding)  
> **Người tham gia:** Coby (S&O) & Anh Trần Minh Khôi (PM FCO / Supervisor)  
> **Tài liệu gốc:** [Meeting notes - 08_06_2026.docx](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/Garena/Meeting%20notes%20-%2008_06_2026.docx)  
> **Phân loại:** Nội bộ / Vận hành  

---

## 1. 🎯 Mục tiêu Chiến lược Đội ngũ (Q3 - Q4)

### 1.1. Activeness (Độ hoạt động) — Ưu tiên số 1
* **Bối cảnh:** FC Online Việt Nam đang ở **năm thứ 8**. Việc thu hút người chơi mới (New Users) hiện nay vô cùng khó khăn.
* **Trọng tâm:** Tập trung tối ưu hóa chỉ số hoạt động của:
  1. *Current Users (Người chơi hiện tại)*: Duy trì tần suất chơi.
  2. *Churned Users (Người chơi đã rời bỏ)*: Thiết kế campaign lôi kéo quay lại.
  3. *New Users*: Hạn chế tối đa chi phí push cơ học nếu không hiệu quả.
* **Chiến dịch Đồng hành (Mùa Euro/World Cup):** 
  * Tìm cách tăng insight về user và giảm churn rate thông qua các campaign dự đoán.
  * > [!WARNING]
    > **Ràng buộc bản quyền (IP):** Tuyệt đối không nhắc trực tiếp đến tên giải đấu "World Cup" (hoặc Euro) trong các ấn phẩm truyền thông và không được cho người chơi dự đoán tỷ số trực tiếp. Phải giữ vững trải nghiệm người dùng (UX) khéo léo thông qua các cơ chế thay thế.

### 1.2. Monetization (Doanh thu)
* **Kênh doanh thu chính:** **90% - 95% doanh thu đến từ các trang Web Events**. In-game Shop chỉ đóng góp 5% - 10%.
* **Yêu cầu Format:** Đội ngũ Creative/Ops phải đề xuất tối thiểu **1 format Web Event mới mỗi quý** để làm mới trải nghiệm của người chơi.
* **Định hướng chiến lược:** Việt Nam tập trung chủ yếu vào **Penetration** (tỷ lệ người nạp tiền) thay vì tăng ARPPU (doanh thu trung bình trên mỗi người nạp) quá đà như các nước khác. 
  * *Chỉ số tham chiếu:* ARPPU tháng (A30) của FCO VN hiện tại khoảng **1 triệu VND** (thấp hơn nhiều so với các game mobile khác của Garena đang ở mức 5 - 6 triệu VND).
* **AI Adoption:** Sử dụng AI để tự động hóa lập báo cáo, dự báo hiệu suất sự kiện (event forecasting), và Social Listening (Regional team đã có tool sẵn). 
  * *Hành động:* Yêu cầu phòng IT cấp quyền truy cập ChatGPT và Claude Enterprise của công ty.

---

## 2. 🏗️ Dự án VIP Revamp (Trang VIP Mới)
* **Ngày chạy chính thức (Air date):** **01/07/2026** (Lưu ý ngày 12/06: Có thể delay launch sau khoảng 2 tuần, không nhất thiết phải air sớm 01/07).
* **Mục tiêu:** 
  * Hướng tới cả nhóm người chơi không nạp tiền (**non-pay**) để kéo chỉ số **DAU** thông qua Play Zone.
  * Hướng tới tính bền vững và dài hạn (long-term): cho phép xây dựng Complex, xây Stadium, nâng cấp công trình.
  * Nếu sau này có dự án *FC Online 2*, hệ thống VIP này phải có tính tiếp nối (continuity).
* **Nguyên tắc Thiết kế Mới (Thảo luận trong buổi họp):**
  * **Tách biệt Currency:** Play Zone (cày chay) và Pay Zone (nạp tiền) sử dụng hai loại tiền tệ riêng biệt, không thể quy đổi cho nhau. Người chơi cày chay sẽ có một hệ quy chiếu và tháp vinh danh hoàn toàn độc lập, đảm bảo họ không bị cảm giác "bị kích thích nạp tiền bằng cách nhìn thấy người nạp tiền có gì" (what could be achieved if you pay). Điều này đảm bảo tính công bằng và tôn trọng thời gian của họ.
  * **Ý tưởng tính năng công trình:** Có thể phát quà dựa trên **chức năng của địa điểm** trong Complex (Ví dụ: Sân tập huấn luyện cho thẻ tập, Trung tâm y tế cho thẻ phục hồi thể lực...).
  * **Sảnh Danh Vọng (Hall of Fame):** Dùng để tri ân Top 50 nạp lớn của năm, chủ yếu mang tính chất hiển thị vinh danh trên web để kích thích niềm tự hào (pride).
* **Nhiệm vụ của Coby:** 
  * Làm việc với các team: Design, Video, Dev (Code lead/Dev lead là anh Tú).
  * **Coby chịu trách nhiệm chính về phần QA (kiểm thử) và tối ưu hóa thiết kế (design optimization) cho trang web VIP trước khi launch.**
  * Tạm thời chốt logic hiện tại để dev kịp làm cho kịp ngày 1/7, các ý tưởng bổ sung sẽ test và nâng cấp sau.

---

## 3. 🃏 Mùa Thẻ Mới: Infinity Prime (Ra mắt 11 - 12/06/2026)
Hệ thống thẻ đặc biệt có tuổi đời vận hành trong **6 tháng**. Đây là mùa thẻ đặc thù kết hợp giữa dòng Prime và Item Trade Market (ITM).

### 3.1. Cơ chế nâng cấp & Vòng quay
* **Nâng cấp thẻ:** Có 3 layer nâng cấp dựa trên chỉ số OVR cơ bản +1.
* **Cơ chế Token:** Đổi từ thẻ ITM ra token để quay. Tỷ lệ ra cầu thủ cực phẩm (chance) < 1%.
* **Vòng quay Bạc (Silver Spin):** Phân phối thẻ +5 và +6 (mở 5 cầu thủ IP cho free user quay miễn phí).
* **Vòng quay Vàng (Gold Spin) & Pity System (Hệ thống bảo hiểm):** 
  * Quay đủ số lần quy định ($N$ lần) chắc chắn sẽ mở ra nhóm cầu thủ bao gồm: Lucio, Marchisio, Essien, Quang Hải (QH - free) và Ronaldo de Lima (Béo - dành cho nhóm đua top).
* **Đặc tính độc quyền (Exclusive Features):**
  * Có **Action Shot** và **Special Animation** riêng biệt khi mở thẻ.
  * Cầu thủ mở ra sẽ được **đánh số thứ tự (Serial Number/Limited Edition)** để tăng giá trị sưu tầm. 
  * > [!WARNING]
    > Nếu cầu thủ này được đem lên Thị trường chuyển nhượng giao dịch mua bán, **số thứ tự giới hạn này sẽ biến mất vĩnh viễn**.
  * Bảng xếp hạng hàng tháng (Monthly Leaderboard) vinh danh 5 - 10 user đứng đầu.

### 3.2. Liên kết với VIP System
* Top 5 - 10 VIP hàng tháng sẽ được nhận thẻ Infinity Prime. Số lượng thẻ phân phối qua kênh VIP này cực kỳ ít nhằm đảm bảo tính khan hiếm và giữ giá trị thẻ trên thị trường.

---

## 4. 📝 Kế hoạch Hành động của Coby (Action Items)

| Nhiệm vụ | Stakeholder liên quan | Thời hạn | Ghi chú |
| :--- | :--- | :---: | :--- |
| **QA/Test trang VIP Revamp** | Anh Tú (Code Lead), Team Design & Dev | Trước 01/07/2026 | Theo dõi sát sao phần test, lập checklist QA và feedback giao diện. (Có thể linh động lùi launch khoảng 2 tuần). |
| **Request Quyền Truy cập AI** | IT Support HCM | Tuần đầu tiên | Xin quyền truy cập Claude Enterprise & ChatGPT Team của tập đoàn. |
| **Tìm hiểu Mùa thẻ Infinity Prime** | Product Team | Trước 11/06/2026 | Hiểu rõ cơ chế Pity, tỉ lệ quay và cách thức quy đổi token trước khi thẻ chính thức launch. |
| **Book Lịch Họp Weekly** | Anh Khôi (PM FCO) | Trước 12/06/2026 | Thiết lập lịch họp định kỳ cập nhật tiến độ công việc. |
| **Chơi Game 2-3h/ngày** | Bản thân | Hàng ngày | Bắt buộc để trở thành hard-core gamer, hiểu sentiment và core gameplay. |
