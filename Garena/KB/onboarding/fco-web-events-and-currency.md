# 🪙 FC Online — Cẩm nang Web Events & Hệ thống Tiền tệ (FC vs. MC)

> **Mục tiêu:** Lưu trữ kiến thức cốt lõi về hệ thống tiền tệ và các định dạng Web Event của FC Online để phục vụ công tác phân tích dữ liệu và thiết kế sự kiện.
> **Phân loại:** Tài liệu onboarding / Vận hành  
> **Cập nhật lần cuối:** 08/06/2026

---

## 1. 💵 Hệ thống Tiền tệ: FC vs. MC

FC Online vận hành với 2 loại đơn vị tiền tệ nạp chính (nạp qua cổng `napthe.vn`). Cả hai đều có thể dùng để chi tiêu trên các Web Events của Garena, nhưng có sự phân biệt rõ ràng ở môi trường in-game:

### 1.1. FC (FC Cash / FIFA Cash)
*   **Định nghĩa:** Đồng tiền chính của phiên bản **FC Online trên máy tính (PC)**.
*   **Chi tiêu:**
    *   *Trong game:* Chỉ có thể dùng để mua các gói vật phẩm, thẻ cầu thủ trong cửa hàng **In-game Shop trên PC**.
    *   *Trên Web:* Tiêu được trên tất cả các trang Web Events hỗ trợ thanh toán bằng FC.

### 1.2. MC (Mobile Cash / Mobile Coin)
*   **Định nghĩa:** Đồng tiền dành riêng cho phiên bản di động **FC Online M (Mobile)**.
    *   *Lưu ý về FC Online M:* Đây là ứng dụng giả lập đồng bộ dữ liệu thời gian thực (real-time) với bản PC, cho phép HLV quản lý đội hình, giao dịch trên TTCN và chơi chế độ Giả lập trên điện thoại.
*   **Chi tiêu:**
    *   *Trong game:* Chỉ có thể dùng để mua các gói vật phẩm trong cửa hàng **In-game Shop trên Mobile**.
    *   *Trên Web:* Tiêu được trên các trang Web Events hỗ trợ thanh toán bằng MC.

> [!IMPORTANT]
> **Điểm mấu chốt khi phân tích số liệu:** Dù cả hai loại tiền đều tham gia Web Events, nhưng doanh thu từ **FC** phản ánh hành vi của tập người chơi PC (truyền thống, hard-core), còn doanh thu từ **MC** phản ánh tập người chơi di động hoặc người chơi tranh thủ quản lý đội hình trên điện thoại.

---

## 2. 🎡 Các Định dạng Web Event Kinh điển

Garena FC Online chạy các Web Event để kích hoạt doanh thu (Monetize) chiếm 90-95% tổng doanh số. Có 4 format phổ biến nhất:

### 2.1. Bi Lắc (Foosball)
*   **Cơ chế sút & tổ hợp:** Người chơi sút bóng vào lưới để nhận ngẫu nhiên 3 huy hiệu trong số 5 loại khác nhau (*Special Prize, FC, BP, PTG, Thẻ*). Phần thưởng ingame tương ứng với tổ hợp nhận được.
*   **Lucky Star:** Cây quà tích lũy điểm sút nhận quà mốc trọn đời.
*   **Special Prize (Jackpot):** Tích tụ quỹ FC/MC của toàn server dựa trên lượng tiêu thụ. Combo 3 huy hiệu Special Prize ăn 100% bể quỹ; combo 2 huy hiệu ăn 10% bể quỹ.

### 2.2. Tỷ Phú / Tỷ Phú 2.0 (Monopoly)
*   **Cơ chế di chuyển:** Đổ xúc xắc/quay số để di chuyển trên bản đồ cờ tỷ phú. Các ô trên bàn cờ có chức năng đặc thù (Nhân đôi quà, sút bóng ngẫu nhiên, so sánh số lượt đi).
*   **Nhiệm vụ DAU:** Cung cấp lượt quay miễn phí hàng ngày khi người chơi hoàn thành nhiệm vụ thắng 1 trận in-game (Xếp hạng, Volta, Giả lập).
*   **Mục đích:** Xả BP số lượng lớn và phân phối các gói thẻ cầu thủ mới.

### 2.3. Mã Đáo Thành Công (Tết/Seasonal Event)
*   **Cơ chế bàn cờ:** Người chơi chọn "Chiến mã" đại diện cho dòng quà mong muốn và đổ xúc xắc chạy trên bàn cờ.
*   **Tích điểm đổi quà:** Nhận điểm tích lũy qua các ô để đổi trực tiếp cầu thủ trong shop sự kiện hoặc tham gia tuyển trạch đặc biệt.

### 2.4. Thánh Siêu Phẩm (Super Goal Master)
*   **Cơ chế dứt điểm:** Người chơi chọn kiểu sút (Vô-lê, đánh đầu, sút xa) tiêu tốn FC/MC để lấy quà ngẫu nhiên và tích điểm.
*   **Bốc số may mắn:** Chương trình quay số may mắn định kỳ tuần/tháng để trúng jackpot lên tới hàng chục nghìn FC.
