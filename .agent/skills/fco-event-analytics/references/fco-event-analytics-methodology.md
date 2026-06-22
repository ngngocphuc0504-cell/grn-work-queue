# 📖 Domain Methodology: FC Online Web Event Analytics & Frameworks

> **Phân loại:** Tài liệu Tham chiếu Kỹ năng (Tier 1 Reference)  
> **Dự án:** Garena FC Online Web Event Analytics  
> **Trạng thái:** ACTIVE  

---

## 1. 💵 Thuật ngữ & Hệ thống Tiền tệ (Currencies Definition)

Khi phân tích hoạt động kinh doanh và vận hành của game FC Online (Garena), việc phân biệt rõ ràng các loại tiền tệ và vai trò của chúng trong chuỗi chuyển đổi là cực kỳ quan trọng:

*   **FC (FIFA/Football Coins):** Tiền tệ nạp trên PC/Web. Người chơi nạp tiền từ Garena Billing để nhận FC. Đây là tiền tệ chính tiêu dùng trong các Web Events chạy trên trình duyệt (PC/Web).
*   **MC (Mobile Coins):** Tiền tệ nạp trên Mobile. Có giá trị quy đổi và sức mua tương đương FC (tỷ lệ 1:1), nhưng được quản lý qua cổng thanh toán di động (App Store / Google Play). Người chơi tiêu dùng MC trên thiết bị di động.
*   **BP (Bandaged Points / Billions of Points):** Tiền tệ in-game dùng để mua bán cầu thủ trên Thị trường chuyển nhượng (TTCN). Đây là **đầu ra (phần thưởng)** của web event mà người chơi mong muốn nhận được, chứ không phải tiền tệ người chơi nạp vào để tham gia sự kiện.

### ⚠️ Ràng buộc về Tập Dữ liệu (Critical Constraint)
Mọi số liệu trong các bảng dữ liệu sự kiện (`Play Daily`, `Play Accumulated`, `Spent`) chỉ ghi nhận thông tin của **Paying Users (Người chơi trả phí)** - những người thực sự nạp tiền và chi tiêu FC/MC. Free Users được lọc bỏ hoàn toàn khỏi tập dữ liệu này để phản ánh chính xác hiệu quả doanh thu.

---

## 2. 👥 Phân khúc Người chơi Trả phí (User Segmentation)

Người dùng trả phí tham gia sự kiện được chia thành 3 phân khúc cốt lõi để phân tích hành vi và giá trị trọn đời:

1.  **Active (Paying Active User):** Người chơi trả phí đang hoạt động liên tục và chi tiêu đều đặn trong suốt thời gian diễn ra sự kiện.
2.  **Churn (Returned Paying User):** Người chơi trả phí cũ đã từng rời game (ngừng chơi hoặc ngừng nạp tiền một thời gian dài), nay quay trở lại nạp tiền và chi tiêu cho sự kiện này.
3.  **New (Newly Converted Paying User):** Tài khoản mới đăng ký trong thời gian diễn ra sự kiện và ngay lập tức nạp tiền chi tiêu lần đầu.

---

## 3. 📐 Công thức & Chỉ số Phân tích (Analytical Equations)

Để đánh giá hiệu quả vận hành sự kiện, AI Agent cần tính toán các chỉ số sau theo ngày:

### 3.1. Daily ARPPU (Average Revenue Per Paying User) theo phân khúc
Chỉ số này đo lường sức mua trung bình của một người chơi tham gia trong ngày:
$$\text{Daily ARPPU}_{\text{[Segment]}} = \frac{\text{FC Spent}_{\text{[Segment]}} + \text{MC Spent}_{\text{[Segment]}}}{\text{Play Daily}_{\text{[Segment]}}}$$

### 3.2. Tỉ lệ đóng góp của Mobile (MC Share)
Đo lường mức độ chuyển dịch tiêu dùng sang nền tảng di động:
$$\text{MC Share \%}_{\text{(Daily)}} = \frac{\sum \text{MC Spent}}{\sum \text{FC Spent} + \sum \text{MC Spent}} \times 100$$

### 3.3. Tốc độ suy giảm người chơi (Day-over-Day Decay Rate)
Đo lường tốc độ "rã đám" của sự kiện sau ngày đầu ra mắt (thường tính trên tập Active):
$$\text{Decay Rate \%}_{\text{D[n] \rightarrow D[n+1]}} = \frac{\text{Play Daily Active}_{\text{D[n+1]}} - \text{Play Daily Active}_{\text{D[n]}}}{\text{Play Daily Active}_{\text{D[n]}}} \times 100$$

### 3.4. Tỉ lệ chuyển đổi đăng nhập thành người chơi trả phí (Login-to-Paying Conversion)
Đo lường sức hấp dẫn thương mại của giao diện sự kiện đối với người đăng nhập:
$$\text{Daily Conversion \%} = \frac{\text{Play Daily Total}}{\text{Login}} \times 100$$

---

## 4. 🧠 4 Khung Phân tích (4 Evaluation Frameworks)

### Framework A — Daily ARPPU per Segment
*   **Mục tiêu:** Đánh giá sức mua của từng nhóm đối tượng để thiết kế định giá gói vật phẩm.
*   **Tín hiệu chỉ báo (Signals):**
    *   `New ARPPU > 3x Active ARPPU`: Sự kiện nạp đầu (Welcome Pack) rất hấp dẫn. Nên đề xuất chạy các chiến dịch phễu nạp đầu rộng rãi.
    *   `Active ARPPU tăng dần` (dù số lượng chơi giảm): Hiệu ứng "Lọc cá voi" (Whale Filter Effect). Đây là trạng thái bình thường của sự kiện khi tệp casual rời đi và chỉ còn whales chi tiêu lớn ở lại.
    *   `Churn ARPPU < 50% Active ARPPU`: Người chơi quay lại không mặn mà chi tiêu. Cần bổ sung các mốc nạp tích lũy hồi sinh đặc quyền.

### Framework B — Platform Split (FC vs MC)
*   **Mục tiêu:** Phát hiện bất thường trong kênh thanh toán di động.
*   **Ngưỡng Benchmarks:**
    *   `MC Share < 5%`: Mức độ cảnh báo cao (Red Flag). Khàng năng cao có lỗi hiển thị giao diện trên di động hoặc lỗi cổng thanh toán.
    *   `MC Share 5% - 15%`: Mức trung bình của các web event thông thường.
    *   `MC Share > 15%`: Tín hiệu rất tốt hoặc đang có chương trình khuyến mại độc quyền cho Mobile.

### Framework C — Engagement Funnel & Decay Rate
*   **Mục tiêu:** Tìm điểm dừng (Elbow Point) của sự kiện để lên phương án duy trì nhiệt độ.
*   **Tín hiệu chỉ báo (Signals):**
    *   `Decay D1 -> D2 > 40%`: Sự kiện thuộc dạng "Đầu voi đuôi chuột" (Front-loaded). Cần bổ sung "mid-event hook" (nhiệm vụ phụ ra mắt giữa sự kiện) để giữ chân người chơi.
    *   `Conversion Rate (Play / Login) < 10%`: Rào cản chi tiêu quá cao. Cần bổ sung các lượt chơi miễn phí (Free Roll) hoặc giảm giá lượt chơi đầu tiên để kích thích chuyển đổi.

### Framework D — Churner Return ROI & Value Contribution
*   **Mục tiêu:** Đánh giá hiệu quả ngân sách quảng cáo kéo người chơi cũ.
*   **Tín hiệu chỉ báo (Signals):**
    *   `Churn ARPPU > 50% Active ARPPU` và `Churn Revenue Share > 5%`: Tập người chơi cũ nạp tiền rất chất lượng. Khuyến nghị tập trung ngân sách Marketing vào các chiến dịch Re-marketing gửi tin nhắn Zalo/Viber kéo người chơi cũ.

---

## 5. 🔄 Quy tắc Chế độ So sánh (Comparison Mode Guidelines)

Khi so sánh hai sự kiện, bắt buộc phải tuân thủ các quy tắc chuẩn hóa dữ liệu sau:
1.  **Chuẩn hóa Trục Thời gian (Timeline Normalization):** Nếu hai sự kiện có độ dài khác nhau, các biểu đồ xu hướng phải được ánh xạ theo `Day 1`, `Day 2`... (thay vì ngày lịch thực tế) và giới hạn trục so sánh theo độ dài của sự kiện ngắn hơn.
2.  **Định dạng Hiển thị:** Sự kiện cũ (Baseline) hiển thị dưới dạng nét đứt (dashed line) hoặc màu mờ; sự kiện mới (Target) hiển thị dưới dạng nét liền (solid line) hoặc màu đậm nguyên bản.
3.  **Tín hiệu So sánh:** Phân tích sự dịch chuyển của điểm dừng (decay rate), sự tăng trưởng đóng góp doanh thu của MC share, và hiệu quả chuyển đổi nạp đầu (New ARPPU).
