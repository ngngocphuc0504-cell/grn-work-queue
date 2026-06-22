# 📊 FC Online — Quy trình & Phương pháp thiết lập Kế hoạch Tháng (Monthly Plan Methodology)

> **Phân loại:** Tài liệu Vận hành Chuẩn (SOP)  
> **Người cập nhật:** Coby (S&O) & Career Twin Co-worker  
> **Cập nhật lần cuối:** 09/06/2026  
> **Trạng thái:** ACTIVE  

---

## 1. 📅 Nhịp độ Vận hành & Lịch Bảo trì (Event Pacing & MA Schedule)

Nhịp độ chạy sự kiện khuyến mại (Promotion/Event) của Garena FC Online Việt Nam tuân theo các nguyên tắc cốt lõi sau:

* **Sự kiện Tháng (Monthly Event):** Khởi chạy cố định vào **ngày 1 hàng tháng**, kéo dài suốt cả tháng.
* **Chuỗi sự kiện ngắn ngày (Short-term Events):** Khởi chạy từ **ngày 3 hàng tháng**, chạy gối đầu nối đuôi nhau liên tục (back-to-back) để đảm bảo activeness không bị đứt gãy.
* **Căn cứ theo lịch bảo trì (MA Schedule):** Mọi kế hoạch sự kiện đều phải khớp với lịch bảo trì định kỳ của nhà phát triển (Nexon). 
  * > [!IMPORTANT]
    > **Mối liên hệ giữa Mùa Thẻ & Sự kiện:** Khi game bảo trì để cập nhật mùa thẻ mới (ví dụ: Infinity Prime), Ops team bắt buộc phải cho ra mắt sự kiện mới đồng hành cùng thời điểm đó để kích cầu.
* **Sự kiện đặc biệt (Special Occasion):** Lịch trình sự kiện sẽ được linh hoạt lồng ghép các sự kiện đặc biệt (như Sinh nhật game, Tết, hè) vào các mốc thời gian cụ thể.
* **Thiết lập phần thưởng (Rewards):** Được quyết định thủ công (manually) theo từng sự kiện, điều chỉnh linh hoạt theo meta game và biến động thị trường.
* **Lập kế hoạch Quý:** Cứ **3 tháng một lần**, bộ phận Ops và Marketing (MKT) sẽ họp chung để xây dựng kế hoạch tổng thể cho quý tiếp theo.

---

## 2. ⚙️ Quy trình Cấu hình Vật phẩm & Tra cứu ID (EA Tool & VLOOKUP)

* **EA Setting Tool:** Công cụ do EA cung cấp để thiết lập cấu hình thuộc tính, vật phẩm và cơ chế nhận quà của game.
* **VLOOKUP ID:** Khi thiết lập sự kiện, Ops team sử dụng hàm VLOOKUP để đối chiếu ID vật phẩm trên hệ thống, đảm bảo không xảy ra sai sót khi cấu hình đầu ra quà tặng.
* **Địa chỉ chạy sự kiện:** Các web events và promotions được tổ chức trên trang: [dc.fconline.garena.vn](http://dc.fconline.garena.vn)

---

## 3. 💵 Phương pháp Định giá Gói Vật phẩm (Item Pricing & Valuation)

Định giá các gói vật phẩm in-game là mảng nghiệp vụ tối quan trọng nhằm cân bằng giữa mục tiêu doanh thu và sentiment của người chơi:

### 3.1. Công thức tính Giá trị gói theo BP
$$\text{Giá trị cầu thủ (BP)} = \text{Giá thẻ (Price)} \times \text{Tỷ lệ quy đổi (Ratio)}$$
$$\text{Tổng giá trị gói (BP)} = \sum \text{Giá trị cầu thủ (BP)}$$

* **Thẻ Price:** Giá trị giao dịch của cầu thủ trên Thị trường chuyển nhượng (TTCN).
* **Ratio (Tỷ lệ):** Hệ số điều chỉnh dựa trên độ hiếm và khả năng nâng cấp của thẻ.

### 3.2. Pain Point về biến động giá và giải pháp quy đổi USD
* > [!WARNING]
  > **Pain Point:** Giá trị cầu thủ trên TTCN biến động liên tục từng ngày. Nếu lấy dữ liệu giá quá xa thời điểm chạy sự kiện, giá trị gói hiển thị sẽ bị lệch so với thực tế, khiến người chơi cảm thấy gói vật phẩm "không ngon" (overpriced).
  * **Giải pháp:** Phải lấy giá cầu thủ **sát ngày chạy sự kiện nhất** để tính toán.
  * **Quy đổi ra USD:** Để đánh giá chính xác gói vật phẩm có hấp dẫn người chơi hay không, tổng giá trị gói (BP) sẽ được quy đổi ra **USD** dựa trên bảng tỷ giá ngoại tệ (sheet currency rate).
  * **Hành vi người chơi:** Quyết định thiết kế gói dựa trên việc nghiên cứu hành vi người chơi (study behavior). Các phương pháp định tính khác chưa đủ độ tin cậy.

---

## 4. 📈 Chỉ số Hiệu quả Vận hành (Efficiency / ROI Limit)

Chỉ số Efficiency (ROI) là thước đo hiệu quả tài chính của gói vật phẩm bán ra:

$$\text{Efficiency} = \frac{\text{Tổng giá trị gói quy đổi (USD)}}{\text{Giá bán gói (USD)}}$$

* > [!IMPORTANT]
  > **Quy tắc trần Efficiency (Efficiency Limit):** Chỉ bán các gói vật phẩm có chỉ số **Efficiency không vượt quá 2** (tức là $\text{Efficiency} \le 2.0$). Nếu vượt quá ngưỡng này, nền kinh tế in-game sẽ bị lạm phát nhanh chóng, làm giảm giá trị thẻ mà người chơi đang sở hữu.

---

## 5. 📖 Cấu trúc Battle Pass (Sổ tay) & Reward Payback

* **Battle Pass (Sổ tay):** Cấu hình phân phối quà theo mốc tiến trình nằm trong sheet sổ tay.
* **Phân loại Battle Pass:**
  * **BP per event (Only BP):** Chỉ chứa tiền tệ BP trắng.
  * **BP all event:** Chứa cả tiền BP trắng và thẻ cầu thủ.
* **Reward Payback (Hoàn trả phần thưởng):** Xác định tỷ lệ hoàn trả của sự kiện, chỉ định cụ thể bao nhiêu % quà hoàn trả dưới dạng thẻ cầu thủ và bao nhiêu % là BP trắng.

---

## 🔍 Case Study Thực tế: Kế hoạch Tháng 06/2026

Tham chiếu dữ liệu từ file: [[FCO][VN] 2026 Jun Monthly Plan - 5.Promotion_VN.csv](file:///c:/Users/VEE0678\Downloads\ws-default-career-twin\ws-default-career-twin\Garena\[FCO][VN] 2026 Jun Monthly Plan   - 5.Promotion_VN.csv)

### 1. Mốc Nạp Tích lũy Dài hạn (Long-term Topup)
* **Thời gian:** 01/06 - 30/06 (Cả tháng 6)
* **Mốc 500 FC:** Gồm các gói thẻ (UT, JNM, DC OVR 111+ (+8), v.v.) và 15,000 tỷ BP. 
  * *Tổng giá trị gói:* 47,614 tỷ BP (~$4.31). 
  * *Efficiency:* **1.28** (Thỏa mãn ràng buộc $\le 2.0$).
* **Mốc 1000 FC:** Gồm các gói thẻ (CU, 24EP 108+ (+8), v.v.) và 20,000 tỷ BP.
  * *Tổng giá trị gói:* 59,116 tỷ BP (~$5.35).
  * *Efficiency:* **1.37** (Thỏa mãn ràng buộc $\le 2.0$).
* **Mốc 2000 FC:** Gồm các gói thẻ (GRU 106+ (6~8), v.v.) và 30,000 tỷ BP.
  * *Tổng giá trị gói:* 71,239 tỷ BP (~$6.44).
  * *Efficiency:* **1.37** (Thỏa mãn ràng buộc $\le 2.0$).

### 2. Sự kiện Nạp Ngắn hạn (Short-term Topup)
* **Đợt 1: 01/06 - 04/06 (Đầu tháng)**
  * **Mốc 40 FC/MC:** Efficiency **1.66**
  * **Mốc 100 FC/MC:** Efficiency **1.78**
  * **Mốc 200 FC/MC:** Efficiency **1.76**
* **Đợt 2: 09/06 - 12/06 (Chạy đồng hành cùng đợt bảo trì ra mắt thẻ Infinity Prime ngày 12/06)**
  * **Mốc 40 FC/MC:** Efficiency **1.62**
  * **Mốc 100 FC/MC:** Efficiency **1.64**
  * **Mốc 200 FC/MC:** Efficiency **1.74**
  * *Nhận xét:* Các đợt nạp ngắn hạn có Efficiency cao hơn các mốc tích lũy dài hạn nhằm kích thích người chơi nạp nhanh trong thời gian ngắn.

### 3. Ngân sách Quà tặng Vật lý (Merchandise Budget)
Tháng 6 ghi nhận ngân sách quà tặng vật chất phục vụ sự kiện cộng đồng/eSports đạt **480,500,000 VND** bao gồm:
* Tay cầm chơi game: 20 chiếc (Tổng trị giá: 60,000,000 VND)
* Cúp lưu niệm: 20 chiếc (Tổng trị giá: 100,000,000 VND)
* Bàn phím cơ: 100 chiếc (Tổng trị giá: 200,000,000 VND)
* Kê tay bàn phím: 100 chiếc (Tổng trị giá: 80,000,000 VND)
* Lót chuột: 100 chiếc (Tổng trị giá: 10,000,000 VND)
* Hộp quà sự kiện: 100 chiếc (Tổng trị giá: 500,000 VND)
* Áo thun sự kiện: 72 chiếc (Tổng trị giá: 30,000,000 VND)
