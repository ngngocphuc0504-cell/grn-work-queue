# 📝 Garena FCO — Biên bản Họp Sync-up với Supervisor (Monthly Plan)

> **Thời gian:** 09/06/2026 (Ngày thứ 2 Onboarding)  
> **Người tham gia:** Coby (S&O) & Anh Trần Minh Khôi (PM FCO / Supervisor)  
> **Tài liệu tham chiếu:** [[FCO][VN] 2026 Jun Monthly Plan - 5.Promotion_VN.csv](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/Garena/%5BFCO%5D%5BVN%5D%202026%20Jun%20Monthly%20Plan%20%20%20-%205.Promotion_VN.csv)  
> **Phân loại:** Nội bộ / Vận hành / Kế hoạch Tháng  

---

## 1. 📅 Chiến lược Lên Kế hoạch Tháng & Quý (Monthly & Quarterly Plan)

* **Chu kỳ sự kiện:** Kế hoạch tháng (Monthly plan - event summary) tóm tắt các sự kiện sẽ chạy trong tháng đó.
  * **Sự kiện tháng (Monthly Event):** Bắt đầu vào ngày **1 hàng tháng**.
  * **Sự kiện ngắn ngày (Short-term Events):** Khởi chạy từ **ngày 3 hàng tháng**, thiết kế chạy nối đuôi nhau liên tục để duy trì hoạt động của người chơi.
  * **Sự kiện đặc biệt:** Tùy theo các dịp lễ hoặc ngày kỷ niệm đặc biệt (special occasions), các sự kiện đặc thù sẽ được thiết kế kẹp vào giữa lịch trình.
* **Căn cứ lập kế hoạch:** Dựa sát vào **Lịch bảo trì (MA - Maintenance schedule)**. Khi game cập nhật mùa thẻ mới thì bắt buộc phải thiết kế sự kiện mới chạy đồng hành tương ứng.
* **Quyết định phần thưởng (Rewards):** Phần thưởng cho các sự kiện hiện tại sẽ được quyết định **thủ công (manually)** cho từng đợt để đảm bảo tính phù hợp với thị trường.
* **Kế hoạch quý:** Định kỳ **3 tháng một lần**, bộ phận vận hành (Ops) sẽ ngồi lại cùng bộ phận Marketing (MKT) để thống nhất kế hoạch cho quý tiếp theo.

---

## 2. ⚡ Kế hoạch Cụ thể Tháng 06/2026

* **Sự kiện Sinh nhật 8 tuổi (8th Anniversary):**
  * Đội ngũ phát triển (Dev team) đang hoàn thiện kỹ thuật cho sự kiện.
  * Dự kiến sự kiện sẽ lên sóng vào ngày **12/06/2026** ngay sau khi hoàn thành bảo trì định kỳ.
* **Nội dung Bảo trì ngày 12/06:**
  * Thêm IP (mùa thẻ đặc biệt **Infinity Prime**) vào game.
  * Cập nhật các bản sửa lỗi (hotfixes).
* **Cơ chế Nạp tích lũy (Top-up):**
  * Áp dụng cơ chế **3-tier topup** (người chơi nạp tiền tích lũy chạm 3 mốc để nhận quà tương ứng).
  * Chạy chương trình **Special Topup**. Mục tiêu vận hành là cố gắng duy trì tối thiểu **1 đợt Special Topup mỗi tháng**.

---

## 3. ⚙️ Quy trình Cấu hình & Định giá Vật phẩm (Item Pricing & EA Tool)

* **Công cụ thiết lập:** Sử dụng tool chuyên dụng do **EA cung cấp** để cài đặt vật phẩm, quà tặng in-game.
* **Tra cứu ID:** Sử dụng hàm **VLOOKUP** trên sheet dữ liệu hệ thống để tìm kiếm chính xác ID của từng vật phẩm.
* **Tính toán Giá trị gói (Item Value Calculation):**
  * **Công thức tính giá trị cầu thủ:**  
    $$\text{Giá trị cầu thủ (BP)} = \text{Giá thẻ (Price)} \times \text{Tỷ lệ quy đổi (Ratio)}$$
    Từ đó cộng dồn để ra tổng giá trị gói theo BP.
  * > [!WARNING]
    > **Pain Point lớn về giá trị gói:** Giá trị cầu thủ trên Thị trường chuyển nhượng (TTCN) biến động liên tục. Nếu lấy dữ liệu giá quá xa thời điểm mở bán, người chơi sẽ cảm thấy gói vật phẩm "không ngon" (giá trị thực tế thấp hơn giá trị tính toán). Do đó, quy tắc bắt buộc là **phải lấy giá cầu thủ sát ngày chạy sự kiện nhất** để bảo đảm độ chính xác tối đa.
  * **Quy đổi giá trị ra USD:** Để đánh giá chính xác độ hấp dẫn của gói (user cảm thấy ngon hay không), Ops team quy đổi tổng giá trị gói ra USD thông qua bảng tỷ giá ngoại tệ (sheet currency rate).
  * **Phương pháp quyết định:** Nghiên cứu kỹ hành vi người chơi (study behavior) để quyết định cấu trúc và giá các gói. Các phương pháp định tính khác hiện tại chưa đủ độ tin cậy.
* **Địa chỉ chạy sự kiện:** Các web events và promotions được tổ chức trên trang: [dc.fconline.garena.vn](http://dc.fconline.garena.vn)
* **Quy tắc Hiệu suất Doanh thu (Efficiency / ROI):**
  * **Công thức:**  
    $$\text{Efficiency (ROI)} = \frac{\text{Giá trị gói (USD)}}{\text{Giá bán (USD)}}$$
  * > [!IMPORTANT]
    > **Ràng buộc vận hành:** Chỉ bán những gói vật phẩm có chỉ số **Efficiency không vượt quá 2** (tức là $\text{Efficiency} \le 2.0$).

---

## 4. 📖 Cơ chế Sổ tay & Battle Pass (BP)

* **Cấu hình Battle Pass:** Được thiết lập chi tiết trong sheet sổ tay.
* **Phân loại cấu hình:**
  * **Only BP (Chỉ BP):** Phân bổ trong sheet `bp per event`, chỉ chứa tiền tệ BP trắng (tiền in-game).
  * **BP all event (BP toàn bộ):** Phân bổ trong sheet `bp all event`, chứa cả tiền BP trắng và thẻ cầu thủ.
* **Reward Payback (Hoàn trả phần thưởng):** Quyết định tỷ lệ hoàn trả (payback reward) cụ thể, xác định rõ bao nhiêu % phần thưởng là thẻ cầu thủ và bao nhiêu % là tiền BP trắng.

---

## 📅 Action Items cho Coby

1. **[ ] Nghiên cứu Kế hoạch Tháng 6 (Promotion_VN.csv):** Phân tích kỹ các mốc nạp tích lũy dài hạn và 2 đợt nạp ngắn ngày (01-04/06 và 09-12/06) để nắm rõ chỉ số Efficiency thực tế.
2. **[ ] Phối hợp QA Sự kiện Sinh nhật 8 tuổi:** Làm việc sát sao với team Dev và Ops để QA sự kiện 8th Anniversary trước giờ lên sóng ngày 12/06.
3. **[ ] Cập nhật Kiến thức Định giá:** Học cách sử dụng EA tool cấu hình vật phẩm và áp dụng công thức tính toán USD Value của gói theo tỷ giá mới nhất.
