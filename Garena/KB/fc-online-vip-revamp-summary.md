# 🎮 FC Online — Tóm tắt Cơ chế VIP System Revamp (Football Complex)

> **Tài liệu gốc:** [FC_Online_VIP_Revamp_v1.0_1.docx](file:///c:/Users/VEE0678/Downloads/ws-default-career-twin/ws-default-career-twin/FC_Online_VIP_Revamp_v1.0_1.docx)  
> **Trạng thái:** Tài liệu Nội bộ / Bảo mật  
> **Người tóm tắt:** Career Twin (S&O Co-worker)  
> **Ngày lập:** 08/06/2026

---

## 1. Bản chất Dự án & Mục tiêu Thay đổi

Hệ thống VIP cũ của FC Online đang gặp 4 hạn chế lớn: giao diện số liệu khô khan, chỉ tập trung vào người nạp tiền (Pay), người chơi không có lý do quay lại trang VIP ngoài việc nhận quà, và thiếu động lực duy trì thói quen lâu dài.

**Mục tiêu Revamp:**
1. **Gamification & Visual-first:** Biến trang VIP thành **Football Complex** — bản đồ 3D góc nhìn isometric (3/4). Mỗi tháng, người chơi sẽ tự động xây dựng thêm các công trình mới đại diện cho tiến trình của họ.
2. **Dual-Track:** Bổ sung song song hệ thống **Play Track** (chăm chỉ chơi game) bên cạnh **Pay Track** (nạp tiền) để vinh danh cả nhóm người chơi cống hiến thời gian.
3. **Progressive Reveal (Hiển thị cuốn chiếu):** Thay đổi cách hiển thị cây quà dài dằng dặc thành cơ chế hiển thị 3 mốc thông minh nhằm tăng sự tò mò và giảm áp lực cho người chơi.

---

## 2. Bản đồ Football Complex (Khái niệm Trung tâm)

Bản đồ khu phức hợp bóng đá của riêng người chơi sẽ phát triển dần theo thời gian. Mỗi tháng xuất hiện **2 công trình mới** tương ứng với 2 Zone:

| Khu vực (Zone) | Nội dung công trình | Logic hiển thị visual |
| :--- | :--- | :--- |
| **Pay Zone** | Sân vận động, Nhà cầu thủ, Phòng họp báo... thay đổi theo lịch 12 tháng. | **7 phiên bản visual** phụ thuộc vào cấp độ (Tier) VIP nạp tháng trước. |
| **Play Zone** | Sân tập, Phòng gym, Thư viện chiến thuật... thay đổi song song với Pay Zone. | **7 phiên bản visual** phụ thuộc vào cấp độ (Tier) Play tháng trước. |
| **SVIP Tower** | Tòa tháp đặc biệt ở vị trí nổi bật. | Unlock vĩnh viễn khi đạt mốc nạp năm **1,000,000 FC+MC**. |
| **VVIP Tower** | Tòa tháp tối thượng ở vị trí trung tâm. | Unlock vĩnh viễn khi đạt mốc nạp năm **2,000,000 FC+MC**. |
| **Hall of Fame** | Sảnh danh vọng vinh danh các Top User. | Cập nhật real-time theo tháng & tích lũy năm. |

---

## 3. Cơ chế Phân hạng VIP (Dual-Track Tiers)

### 3.1. Pay Track (Dựa trên tổng nạp FC+MC tháng trước)
Giữ nguyên logic cũ nhưng bổ sung thêm **2 tier cạnh tranh xếp hạng** ở vị trí cao nhất để kích cầu nhóm Whales (người nạp lớn):

| Tier | Mốc nạp (FC+MC) | Logic xếp hạng | Visual công trình tháng | Quà đặc biệt |
| :--- | :---: | :--- | :--- | :--- |
| **Bronze** | 200 | Đủ mốc | Cơ bản, chưa hoàn thiện | Quà đăng nhập, nạp tháng, sinh nhật, ticket hỗ trợ |
| **Silver** | 600 | Đủ mốc | Tiêu chuẩn, hoàn thiện cơ bản | Như Bronze |
| **Gold** | 1,500 | Đủ mốc | Nâng cao, hiệu ứng ánh sáng | Như Silver |
| **Platinum** | 15,000 | Đủ mốc | Cao cấp, particle effects | Mở rương VIP, Áo & Logo đặc biệt |
| **Diamond** | 50,000 | Đủ mốc | Diamond visual, diamond animation | Shop độc quyền |
| **Top 50** | — | Top 6–50 tổng nạp tháng | Elite visual, hiệu ứng lửa | Shop độc quyền |
| **Top 5** | — | Top 1–5 tổng nạp tháng | Legend visual độc nhất | Thẻ cầu thủ **Infinite Prime (Random)** |

> [!IMPORTANT]
> **Quy tắc ưu tiên thứ hạng:** `Top 5 > Top 50 > Diamond > Platinum > Gold > Silver > Bronze`. Nếu người chơi nằm trong danh sách xếp hạng cao hơn, hệ thống sẽ tự động gán visual và benefit của cấp đó.

---

### 3.2. Play Track (Dựa trên hoạt động trong game tháng trước)
Hệ thống hoàn toàn mới nhằm kích thích các chỉ số DAU, Retention và thời gian chơi game:

| Cấp độ Play | Điều kiện đạt được | Visual Play Zone | Quà tặng (Cầu thủ in-game) |
| :--- | :--- | :--- | :--- |
| **Player I** | Login 10+ ngày | Basic | Bronze Pack |
| **Player II** | Login 15+ ngày + Đá 30+ trận | Standard | Silver Pack |
| **Player III** | Login 20+ ngày + Đá 60+ trận + Hoàn thành 1 mùa giải | Advanced | Gold Pack |
| **Player IV** | Login 25+ ngày + Đá 100+ trận + Top 30% rank tháng | Premium | Elite Pack |
| **Player V** | Login 28+ ngày + Đá 150+ trận + Top 10% rank tháng | Diamond Play | Legend Pack |
| **Play Top 5** | Top 5 server về **Composite Score**: <br> $Score = (\text{Số trận} \times 0.6) + (\text{Rank} \times 0.4)$ | Legend Play | **Thẻ Infinite Prime (Random)** |

---

## 4. Cơ chế Cây Tích Lũy (Pay Tree & Play Tree)

Song song với việc tính hạng tháng, người chơi tích lũy điểm trọn đời (không reset) để nhận quà mốc.

### 4.1. Cơ chế hiển thị Progressive Reveal (Cuốn chiếu)
Để tránh làm người chơi "ngợp" trước danh sách quà quá dài, giao diện chỉ hiển thị **tối đa 3 mốc** xung quanh vị trí hiện tại:
1. **Mốc đã qua:** Thu nhỏ, hiển thị mờ, đánh dấu *"Đã nhận"*.
2. **Mốc hiện tại:** Highlight nổi bật kèm progress bar, % hoàn thành và số điểm còn thiếu.
3. **Mốc +1 (kế tiếp):** Hiển thị rõ ràng quà và điều kiện để người chơi nhìn thấy đích đến gần nhất và có động lực nạp/chơi tiếp.
4. **Mốc +2 (xa hơn):** Hiển thị mờ một phần để kích thích tò mò.
5. **Mốc +3 trở đi:** Ẩn hoàn toàn trên giao diện.

### 4.2. Pay Tree (Tổng nạp trọn đời)
* Tích lũy FC+MC từ trước đến nay.
* Các mốc: 10k → 50k → 100k → 300k → 600k → **1,000,000 (Unlock SVIP Tower)** → **2,000,000 (Unlock VVIP Tower)** → 5,000,000 → 10,000,000+.

### 4.3. Play Tree (Tổng điểm Play trọn đời)
* Tính theo công thức điểm tích lũy:
  $$\text{Điểm Play} = (\text{Tổng trận} \times 2) + (\text{Tổng ngày login} \times 10) + (\text{Số mùa giải hoàn thành} \times 500)$$
* Các mốc: 1,000 → 5,000 → 15,000 (Chơi đều ~2 năm) → 30,000 (Chơi đều ~3 năm) → 60,000 → 100,000+.

---

## 5. Tòa nhà Vinh danh & Sảnh Danh Vọng (Hall of Fame)

### 5.1. SVIP & VVIP Towers
* **Điều kiện:** Đạt 1M (SVIP) và 2M (VVIP) nạp tích lũy trong năm dương lịch (tính từ 01/01 đến 31/12).
* **Reset hàng năm:** Vào ngày 01/01 năm sau, trạng thái sẽ reset. Nếu năm mới không đạt lại mốc nạp, tòa tháp cũ sẽ chuyển sang trạng thái **"Legacy"** — hiển thị mờ hơn và đính kèm huy hiệu năm tương ứng (ví dụ: *VVIP 2026*).

### 5.2. Sảnh Danh Vọng (Hall of Fame)
* Vinh danh Top 100 Nạp Năm & Top 100 Play Năm.
* Trao danh hiệu đặc biệt hàng tháng:
  * **MVP Tháng:** Top 1 Pay Track tháng.
  * **Iron Man Tháng:** Top 1 Play Track tháng.
  * **Legend of the Year:** Top 1 Pay tổng kết cả năm (Nhận tòa nhà vinh danh độc quyền riêng biệt).

---

## 6. Lộ trình Triển khai (Roadmap)
* **Phase 1 (Tháng 1-2):** Layout Complex Map, Pay Zone công trình tháng, và Pay Tree Progressive Reveal.
* **Phase 2 (Tháng 3-4):** Tích hợp Play Zone, Play Tree, Play Tiers, và SVIP/VVIP Towers.
* **Phase 3 (Tháng 5-6):** Sảnh Danh Vọng, Danh hiệu MVP/Iron Man, Lịch sử Complex qua các tháng và tối ưu hiệu năng mobile.
