# 🎮 TÀI LIỆU ĐẶC TẢ TỔNG HỢP: MEMBER WEB SYSTEM (VIP SYSTEM REVAMP)
## HỆ THỐNG LOYALTY & ENGAGEMENT TRỰC QUAN - FC ONLINE
*Tài liệu nguồn chân lý duy nhất (Single Source of Truth) của dự án*  
*Cập nhật: 09/06/2026*

---

## 1. Tổng quan hệ thống & Triết lý thiết kế

Member Web System (trước đây là VIP System Revamp) là nền tảng loyalty và engagement dành riêng cho người chơi FC Online. Hệ thống thay thế giao diện bảng biểu số liệu cũ bằng một thế giới trực quan sinh động — **Football Complex (Khu phức hợp bóng đá cá nhân)** xây dựng theo góc nhìn Isometric 3/4. 

Hệ thống hoạt động dựa trên hai cơ chế tích lũy song song độc lập nhưng hiển thị chung trên một giao diện:
1.  **Hệ thống PAY (Nạp tiền):** Dựa trên lịch sử nạp tiền tích lũy hàng tháng và trọn đời của người chơi.
2.  **Hệ thống PLAY (Chơi game):** Dựa trên các chỉ số hoạt động in-game hàng tháng và trọn đời (login, số trận, thời gian chơi).

### Triết lý thiết kế cốt lõi:
*   **Visual-First:** Mọi thứ hạng, thành tích và đặc quyền của người chơi đều được thể hiện thông qua các mô hình kiến trúc thay vì hiển thị dạng số thô.
*   **Privacy-First (Bảo vệ quyền riêng tư):** Tuyệt đối **không hiển thị số tiền nạp tuyệt đối** của người chơi trên bất kỳ giao diện nào (kể cả Hall of Fame). Tất cả số tiền nạp phải được quy đổi sang hệ thống điểm tích lũy.
*   **Progressive Reveal (Tiết lộ cuốn chiếu):** Tránh gây nản lòng cho người chơi phổ thông bằng cách chỉ hiển thị tối đa **2–3 mốc quà tiếp theo** trên cây tích lũy.
*   **Dual-Track Balance:** Khu vực PAY (Pay Zone) và PLAY (Play Zone) có diện tích hiển thị và vai trò cân bằng trên bản đồ Football Complex để ghi nhận xứng đáng cả người nạp tiền lẫn người chơi chăm chỉ.

---

## 2. Hệ thống Phân hạng song song (Dual-Track Tiers)

### 2.1. Pay Track (Tính theo tổng nạp tháng liền trước)
Kết quả nạp tiền tháng trước sẽ quyết định bậc rank, visual tòa nhà chính và bộ quà tặng (benefit) của tháng hiện tại. Rank PAY gồm **6 bậc**:

| Bậc Rank | Yêu cầu Nạp Tháng (FC) | Quy đổi VND | Trạng thái hiển thị trên UI | Đặc điểm hình thái công trình tháng | Bộ Quà tặng VIP Month |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Đồng** | $\ge 200$ FC | $\ge 100,000$ VND | Móng nhà + Tường gạch | Chỉ có móng hoặc khung thép skeleton (đang xây dựng) | 200M BP + Gói chỉ định (+3) |
| **Bạc** | $\ge 600$ FC | $\ge 300,000$ VND | Cấu trúc sơ khai | Cấu trúc sơ khai, chủ yếu là khung nhà cơ bản | 600M BP + Gói chỉ định (+5) mùa thường |
| **Vàng** | $\ge 1,500$ FC | $\ge 750,000$ VND | Cấu trúc cơ bản | Cấu trúc cơ bản đủ nhận diện, có ít chi tiết trang trí | 2B BP + Gói ngẫu nhiên (6~8) mùa hot |
| **Bạch Kim** | $\ge 15,000$ FC | $\ge 7,500,000$ VND | Cấu trúc nâng cao | Cấu trúc chính đầy đủ, thiếu các phần mở rộng | 10B BP + Gói ngẫu nhiên (7~8) + 1 Gói Phục hồi thể lực VIP |
| **Kim Cương** | $\ge 50,000$ FC | $\ge 25,000,000$ VND | Gần hoàn chỉnh, hiệu ứng đặc biệt | Gần hoàn chỉnh, có hiệu ứng ánh sáng nhẹ | 35B BP + Gói Chỉ định (+7) + Đặc quyền CS riêng |

*Mốc điểm quy đổi và nạp cụ thể có thể điều chỉnh sau khi phân tích phân bổ nạp tiền thực tế từ Dev.*

#### Vinh danh Top 50 PAY hàng tháng:
*   **Top 50** user nạp nhiều nhất tháng được vinh danh trong danh sách Elite tại Hall of Fame.
*   **Top 5** trong nhóm này sẽ được nhận thêm quà ngẫu nhiên đặc biệt (ví dụ: Thẻ cầu thủ Infinite Prime).
*   Danh sách này reset hoàn toàn vào ngày 1 hàng tháng.

---

### 2.2. Play Track (Tính theo hoạt động chơi game tháng liền trước)
Rank Play hàng tháng được tính dựa trên **Composite Play Score** tổng hợp từ 3 chỉ số chính:
*   **Số ngày đăng nhập (Login Days):** Số ngày có phiên login vào game trong tháng.
*   **Số trận thi đấu (Total Matches):** Tổng số trận đã đá trong tháng.
*   **Thời gian chơi (Playtime):** Tổng thời gian chơi tính bằng giây/phút (không tính thời gian idle treo máy).

$$\text{Điểm Play Tháng} = (\text{Số ngày login} \times A) + (\text{Số trận} \times B) + (\text{Playtime giây} \times C)$$
*(Hệ số A, B, C sẽ xác định sau khi phân tích tương quan dữ liệu để tránh chênh lệch lấn át giữa các chỉ số).*

#### Phân bậc Rank PLAY hàng tháng & Quà tặng:
Sử dụng hệ thống danh xưng riêng biệt hoàn toàn với rank PAY (gồm 5 Cấp). Không thay đổi hình dáng kiến trúc công trình theo rank như PAY để tối ưu workload. Thay vào đó, công trình phụ PLAY của tháng đó sẽ có visual cố định, và rank Play của người chơi được thể hiện qua **Cúp Vàng / Bạc / Đồng gắn nổi bật trên công trình**:

| Bậc Rank PLAY | Yêu cầu Điểm Play | Cúp Visual trên Map | Quà tặng Vật phẩm dự kiến (Monthly Item) |
| :---: | :

## 3. Cây tích lũy trọn đời (Lifetime Trees) & Trải nghiệm Cây Quà

Điểm tích lũy trọn đời (lifetime) được cộng dồn kể từ khi tạo tài khoản và không bị reset theo tháng. Bộ quà tặng trên cây (one-time reward) được cập nhật định kỳ 6 tháng/lần.

### 3.1. Cơ chế Progressive Reveal kết hợp tính năng "Showroom"
Giao diện mặc định của cây quà chỉ hiển thị tối đa 3 mốc xung quanh người chơi để tối giản UI:
1.  **Mốc đã nhận:** Hiển thị mờ, đánh dấu *"Đã nhận"*, thu nhỏ.
2.  **Mốc hiện tại:** Highlight nổi bật kèm progress bar, % tiến độ và số điểm còn thiếu.
3.  **Mốc +1 (kế tiếp):** Hiển thị rõ quà và điều kiện đạt để tạo động lực.
4.  **Mốc +2 (xa hơn):** Hiển thị mờ một phần để kích thích tò mò.
5.  **Mốc từ +3 trở đi:** Ẩn hoàn toàn khỏi giao diện chính.

> [!TIP]
> **Đề xuất bổ sung - Nút "Showroom" (Full Rewards Preview):**
> Nhằm kích thích nhóm người chơi VIP lớn (Whales) có mục tiêu rướn dài hạn, bổ sung một nút nhỏ **"Xem toàn bộ mốc quà"** (View Full Roadmap). Khi click, hệ thống sẽ mở một cửa sổ popup (modal) hiển thị danh sách tất cả các mốc quà trọn đời từ thấp đến cao cùng trạng thái (Khóa/Mở khóa) để kích thích mong muốn chinh phục mà không làm rối giao diện chính.

---

### 3.2. Tính năng bổ sung: Activity Snapshot (Play Tree Page)
Để tăng tính minh bạch, khi người chơi toggle xem **PLAY Tree**, hệ thống sẽ tích hợp một bảng thông tin hoạt động thực tế nằm ngay dưới tiến độ của mốc hiện tại.

*   **Vị trí hiển thị:** Bên dưới progress bar và phân số điểm của mốc hiện tại.
*   **Triết lý:** *"Show, don't tell"*. Chỉ hiển thị số liệu thuần túy để người chơi tự đối chiếu, không đưa ra lời khuyên hay nhắc nhở gây áp lực.
*   **Bố cục dữ liệu hiển thị:**
    *   **Cột "Tháng này":** Số trận đã chơi, Số ngày login, Playtime (phút) của tháng hiện tại.
    *   **Cột "Tháng trước" (Baseline):** Số trận, số ngày login, playtime của tháng trước để người chơi tự so sánh với chính mình.
    *   **Dòng "Từ đầu năm":** Tổng trận đấu, tổng ngày login từ 01/01 đến hiện tại (không hiển thị playtime vì con số sẽ quá lớn).

```text
┌─────────────────────────────────────────┐
│ ▶  Mốc hiện tại — 5,000 điểm           │
│    Gói quà Play 5K ⭐                   │
│    [████████████░░░] 3,240 / 5,000 đ    │
│    ⚡ Còn thiếu 1,760 điểm             │
│                                         │
│    ── Hoạt động của bạn ─────────────── │
│    Tháng này       Tháng trước          │
│    82 trận         95 trận              │
│    28 ngày login   26 ngày              │
│    2,400 phút      2,810 phút           │
│                                         │
│    Từ đầu năm: 570 trận · 160 ngày     │
└─────────────────────────────────────────┘
```

---

### 3.3. Quy tắc Định giá Vật phẩm & Logic Hiển thị Giá trị Quà (Reward Valuation & Display Rules)
Nhằm kiểm soát rủi ro về mặt Sentiment (tránh việc người chơi cảm thấy bị "treo đầu dê bán thịt chó" do giá trị vật phẩm gacha bị thổi phồng ảo trên TTCN), hệ thống áp dụng các nguyên tắc định giá và hiển thị sau:

#### 3.3.1. Đồng nhất hóa Hệ số Chiết khấu (Standardized Discount Multipliers)
Bắt buộc áp dụng hệ số chiết khấu thống nhất cho giá trị BP của vật phẩm dựa trên biên độ gia cố (cấp cộng), thay vì thay đổi hệ số tùy tiện theo từng tầng (floor):
*   **Gói chỉ định cụ thể `(+8)` (Guaranteed +8):** Áp dụng hệ số **`0.5` hoặc `0.6`** (chỉ chiết khấu nhẹ tương ứng với giá trị tối thiểu của thẻ cấp thấp nhất nhận được và giá trị trung bình của thẻ cấp cao nhất. Điều này giúp quản lý kỳ vọng của người chơi và tránh khiếu nại.

#### 3.3.3. Ưu tiên cơ cấu gói hẹp ở các Tầng VIP cao
Để duy trì độ tin cậy của hệ thống VIP đối với nhóm khách hàng nạp lớn (Whales):
*   Ở các tầng VIP cao (Floor 6-8), hạn chế tối đa việc phân bổ gói ngẫu nhiên biên độ rộng `(6~8)`.
*   Khuyến khích thay thế bằng các gói **Chỉ định cộng cụ thể `(+7)` hoặc `(+8)`** kết hợp thêm BP trắng để bù đắp giá trị. Việc này giúp nâng hệ số chiết khấu lên `0.5 - 0.6` (độ tin cậy cao) thay vì giữ ở mức `0.3` (khiến người chơi cảm thấy giá trị ảo).

---

### 3.4. Bảng Quy hoạch Cây tích lũy trọn đời - Pay Track (Chia nhỏ khoảng Gap)
Để kích thích và duy trì động lực cho người chơi ở mọi phân khúc, khoảng cách nạp (PAY Gap) được chia nhỏ tối ưu. Trần tích lũy trọn đời (Cap) được thiết lập ở mức **20 Tỷ VND** (điều chỉnh từ mốc 100 Tỷ VND để phù hợp với thực tế Top nạp server hiện tại là ~10 Tỷ VND, tạo đích rướn khả thi hơn). Từ mốc 1 Tỷ VND trở lên, mức nạp tăng đều đặn **1 Tỷ VND mỗi tầng**:

| Tầng | Mốc Tích lũy (VND) | Điểm Quy đổi (1K = 1đ) |
| :---: | :--- | :--- |
| **Tầng 1** | **$100,000$ VND** | $100$ điểm |
| **Tầng 2** | **$200,000$ VND** | $200$ điểm |
| **Tầng 3** | **$300,000$ VND** | $300$ điểm |
| **Tầng 4** | **$500,000$ VND** | $500$ điểm |
| **Tầng 5** | **$1,000,000$ VND** | $1,000$ điểm |
| **Tầng 6** | **$2,000,000$ VND** | $2,000$ điểm |
| **Tầng 7** | **$3,000,000$ VND** | $3,000$ điểm |
| **Tầng 8** | **$5,000,000$ VND** | $5,000$ điểm |
| **Tầng 9** | **$10,000,000$ VND** | $10,000$ điểm |
| **Tầng 10**| **$15,000,000$ VND** | $15,000$ điểm |
| **Tầng 11**| **$20,000,000$ VND** | $20,000$ điểm |
| **Tầng 12**| **$30,000,000$ VND** | $30,000$ điểm |
| **Tầng 13**| **$50,000,000$ VND** | $50,000$ điểm |
| **Tầng 14**| **$75,000,000$ VND** | $75,000$ điểm |
| **Tầng 15**| **$100,000,000$ VND**| $100,000$ điểm|
| **Tầng 16**| **$150,000,000$ VND**| $150,000$ điểm|
| **Tầng 17**| **$200,000,000$ VND**| $200,000$ điểm|
| **Tầng 18**| **$300,000,000$ VND**| $300,000$ điểm|
| **Tầng 19**| **$500,000,000$ VND**| $500,000$ điểm|
| **Tầng 20**| **$750,000,000$ VND**| $750,000$ điểm|
| **Tầng 21**| **$1,000,000,000$ VND**| $1,000,000$ điểm|
| **Tầng 22**| **$2,000,000,000$ VND**| $2,000,000$ điểm|
| **Tầng 23**| **$3,000,000,000$ VND**| $3,000,000$ điểm|
| **Tầng 24**| **$4,000,000,000$ VND**| $4,000,000$ điểm|
| **Tầng 25**| **$5,000,000,000$ VND**| $5,000,000$ điểm|
| **Tầng 26**| **$6,000,000,000$ VND**| $6,000,000$ điểm|
| **Tầng 27**| **$7,000,000,000$ VND**| $7,000,000$ điểm|
| **Tầng 28**| **$8,000,000,000$ VND**| $8,000,000$ điểm|
| **Tầng 29**| **$9,000,000,000$ VND**| $9,000,000$ điểm|
| **Tầng 30**| **$10,000,000,000$ VND**| $10,000,000$ điểm|
| **Tầng 31**| **$11,000,000,000$ VND**| $11,000,000$ điểm|
| **Tầng 32**| **$12,000,000,000$ VND**| $12,000,000$ điểm|
| **Tầng 33**| **$13,000,000,000$ VND**| $13,000,000$ điểm|
| **Tầng 34**| **$14,000,000,000$ VND**| $14,000,000$ điểm|
| **Tầng 35**| **$15,000,000,000$ VND**| $15,000,000$ điểm|
| **Tầng 36**| **$16,000,000,000$ VND**| $16,000,000$ điểm|
| **Tầng 37**| **$17,000,000,000$ VND**| $17,000,000$ điểm|
| **Tầng 38**| **$18,000,000,000$ VND**| $18,000,000$ điểm|
| **Tầng 39**| **$19,000,000,000$ VND**| $19,000,000$ điểm|
| **Tầng Cap**| **$20,000,000,000$ VND**| $20,000,000$ điểm|

---

### 3.5. Bảng Quy hoạch Cây tích lũy trọn đời - Play Track
Điểm Play tích lũy trọn đời được tính cộng dồn (1 trận = 1đ, 1 ngày login = 10đ, 10 phút chơi = 1đ). Trần tích lũy năm (Cap) được thiết lập ở mức **50,000 điểm Play** (reset hàng năm). Bảng quy đổi dưới đây hiển thị số điểm và **số ngày chơi tương đương** giả định một người chơi trung bình hoạt động **3 trận/ngày (mỗi trận 10 phút, tổng cộng 30 phút và 1 lần đăng nhập = 16 điểm/ngày)**. Nếu người chơi hoạt động 65-70% số ngày trong năm (~240-250 ngày), họ sẽ đạt khoảng **Tầng 31 - Tầng 32** (cách mốc cuối 8-9 tầng):

| Tầng | Mốc Tích lũy (Điểm Play) | Số ngày chơi tương đương (16đ/ngày) |
| :---: | :--- | :--- |
| **Tầng 1** | **$50$ điểm** | ~3 ngày |
| **Tầng 2** | **$100$ điểm** | ~6 ngày |
| **Tầng 3** | **$150$ điểm** | ~9 ngày |
| **Tầng 4** | **$200$ điểm** | ~13 ngày |
| **Tầng 5** | **$250$ điểm** | ~16 ngày |
| **Tầng 6** | **$300$ điểm** | ~19 ngày |
| **Tầng 7** | **$350$ điểm** | ~22 ngày |
| **Tầng 8** | **$400$ điểm** | ~25 ngày |
| **Tầng 9** | **$500$ điểm** | ~31 ngày (~1 tháng) |
| **Tầng 10**| **$600$ điểm** | ~38 ngày |
| **Tầng 11**| **$700$ điểm** | ~44 ngày |
| **Tầng 12**| **$800$ điểm** | ~50 ngày |
| **Tầng 13**| **$900$ điểm** | ~56 ngày |
| **Tầng 14**| **$1,000$ điểm** | ~63 ngày (~2 tháng) |
| **Tầng 15**| **$1,150$ điểm** | ~72 ngày |
| **Tầng 16**| **$1,300$ điểm** | ~81 ngày |
| **Tầng 17**| **$1,450$ điểm** | ~91 ngày |
| **Tầng 18**| **$1,600$ điểm** | ~100 ngày |
| **Tầng 19**| **$1,750$ điểm** | ~109 ngày |
| **Tầng 20**| **$1,900$ điểm** | ~119 ngày (~4 tháng) |
| **Tầng 21**| **$2,050$ điểm** | ~128 ngày |
| **Tầng 22**| **$2,200$ điểm** | ~137 ngày |
| **Tầng 23**| **$2,350$ điểm** | ~147 ngày |
| **Tầng 24**| **$2,500$ điểm** | ~156 ngày |
| **Tầng 25**| **$2,650$ điểm** | ~166 ngày |
| **Tầng 26**| **$2,800$ điểm** | ~175 ngày |
| **Tầng 27**| **$3,000$ điểm** | ~188 ngày |
| **Tầng 28**| **$3,200$ điểm** | ~200 ngày |
| **Tầng 29**| **$3,400$ điểm** | ~213 ngày |
| **Tầng 30**| **$3,600$ điểm** | ~225 ngày |
| **Tầng 31**| **$3,800$ điểm** | ~238 ngày (Đạt ~65% số ngày/năm) |
| **Tầng 32**| **$4,000$ điểm** | ~250 ngày (Đạt ~68% số ngày/năm) |
| **Tầng 33**| **$4,150$ điểm** | ~259 ngày |
| **Tầng 34**| **$4,300$ điểm** | ~269 ngày |
| **Tầng 35**| **$4,450$ điểm** | ~278 ngày |
| **Tầng 36**| **$4,600$ điểm** | ~288 ngày |
| **Tầng 37**| **$4,700$ điểm** | ~294 ngày |
| **Tầng 38**| **$4,800$ điểm** | ~300 ngày |
| **Tầng 39**| **$4,900$ điểm** | ~306 ngày |
| **Tầng Cap**| **$5,000$ điểm** | ~313 ngày (Đạt ~85% số ngày/năm) |

---

### 3.6. Cơ chế Tách biệt & Hoạt động độc lập (Decoupled Battle Pass Logic)
Để tối ưu hóa trải nghiệm người dùng và kiểm soát tài nguyên thiết kế, hệ thống phân tách hoàn toàn thành hai lớp logic độc lập:

1. **Vòng lặp tháng (Monthly Facility Progression):**
   * Hoạt động nạp/chơi trong tháng T sẽ quyết định hình dáng công trình (PAY Facility) và mức Cúp vinh danh (PLAY Decoration) của tháng đó.
   * Vào ngày 1 của tháng T+1, công trình này sẽ được "đóng băng" (frozen) vĩnh viễn trên bản đồ của người chơi, đóng vai trò là một mốc lịch sử.
2. **Vòng lặp tích lũy (Lifetime Battle Pass Progression):**
   * Điểm nạp (1K VND = 1đ) và điểm chơi (1 trận = 1đ, 1 login = 10đ, 10 phút playtime = 1đ) cộng dồn vĩnh viễn không reset tháng.
   * 40 mốc PAY và 40 mốc PLAY được thiết kế theo dạng **Battle Pass (Roadmap)** độc lập.
   * Việc đạt các mốc này **không làm thay đổi visual của các công trình tháng**, mà thay vào đó sẽ mở khóa các **phần tử ngoại cảnh dùng chung** (Central Plaza Lv1-5, lát đá, tượng đài) và các **công trình vinh danh độc lập** ở góc bản đồ (SVIP Tower, VVIP Twin Tower).
   * Cơ chế này giúp giao diện bản đồ tiến hóa sinh động theo thâm niên nạp/chơi của user mà không gây xung đột visual của các tòa nhà lịch sử tháng.

---
## 4. Tính năng Dream City (City-Building)

Mỗi tháng, người chơi tự động nhận được **2 công trình** tương ứng với thành tích tháng trước đó của mình: một tòa nhà chính đại diện cho PAY track và một công trình phụ đại diện cho PLAY track.

### 4.1. Phân kỳ mở rộng theo Area (Khu vực)
Để tránh cảm giác trống trải và hụt hẫng khi người chơi mới bắt đầu, Dream City được chia làm các khu vực (Area) và mở rộng dần theo thời gian. Phase 1 khi ra mắt sẽ tập trung hoàn thiện **Area 1 (Tháng 1-6)**:

| Tháng | Công trình PAY (Tòa nhà chính) | Công trình phụ PLAY (Visual cố định + gắn Cúp) |
| :---: | :--- | :--- |
| **Tháng 1** | Sân vận động chính (Main Stadium) | Sân vận động phụ |
| **Tháng 2** | Ký túc xá cầu thủ (Player Residence) | Khu tập luyện |
| **Tháng 3** | Tháp trung tâm (Central Tower) | Đài phun nước / Quảng trường |
| **Tháng 4** | Khu gym & sức khỏe (Gym & Health) | Hồ bơi |
| **Tháng 5** | Khu massage & spa | Phòng y tế |
| **Tháng 6** | Sport Mall | Supermarket / Khu ăn uống |

*Area 2 (Tháng 7-12) sẽ được thiết kế mở rộng dựa trên dữ liệu vận hành thực tế của Area 1.*

### 4.2. Logic chốt và khóa công trình
Vào ngày 1 của tháng T, hệ thống đọc dữ liệu xếp hạng của tháng T-1. Công trình tháng T-1 sẽ tự động xuất hiện trên bản đồ của user với visual rank đạt được và **tồn tại vĩnh viễn không thay đổi**. Nếu tháng đó user không đạt điều kiện nạp/chơi, công trình vẫn xuất hiện ở hình thái thấp nhất (Đồng/Cúp Đồng) chứ không bị trống ô đất.

---

## 5. Tòa tháp vinh danh năm (SVIP & VVIP Towers)

Đây là các công trình đặc biệt nằm ở góc bản đồ, đại diện cho tổng nạp tích lũy của cả năm dương lịch (từ 01/01 đến 31/12), không reset theo tháng.

*   **SVIP Tower:** Mở khóa vĩnh viễn khi tổng nạp năm đạt **1,000,000 FC+MC**. Visual tháp hoành tráng, có hiệu ứng ánh sáng động và hiển thị tên người chơi công khai.
*   **VVIP Tower:** Mòa nhà tối thượng mở khóa khi tổng nạp năm đạt **2,000,000 FC+MC**. Vị trí đắc địa nhất bản đồ, animated 24/7.

### 5.1. Cơ chế Legacy (Reset năm)
Vào ngày 01/01 hàng năm, thanh tích lũy năm reset về 0. Nếu trong năm mới người chơi chưa đạt lại mốc nạp, tòa tháp cũ của năm cũ sẽ tự động chuyển sang trạng thái **"Legacy"**: visual mờ đi, đính kèm badge năm tương ứng (ví dụ: *VVIP 2026*).

### 5.2. Cơ chế Bảo hiểm Mốc nạp (Khắc phục ức chế cuối năm)
Để tránh trường hợp người chơi đạt mốc VVIP vào tháng 11 hoặc 12 chỉ được trải nghiệm tòa tháp rực rỡ 1-2 tháng trước khi bị reset sang Legacy, hệ thống áp dụng cơ chế bảo hiểm sau:
*   **Bảo lưu mốc Q4 (Q4 Carry-over):** Bất kỳ người chơi nào đạt mốc SVIP/VVIP trong **Quý 4 (từ 01/10 đến 31/12)** sẽ được bảo lưu trạng thái Active rực rỡ của tòa tháp suốt cả năm dương lịch tiếp theo, không bị chuyển sang trạng thái Legacy mờ vào ngày 01/01.

---

## 6. Cấu trúc UI - 3 Tab chính & Tính năng tương tác

Giao diện trang Member Web gồm 3 Tab chính với bố cục chức năng cụ thể:

### Tab 1: Kiến trúc hiện tại (Current Month - Giao diện chính)
*   **Isometric Map (Trung tâm):** Hiển thị 2 công trình đang xây của tháng hiện tại (PAY + PLAY).
*   **Tiến trình tháng:** Thanh progress hiển thị điểm nạp PAY và điểm chơi PLAY tích lũy trong tháng hiện tại cùng mốc rank kế tiếp.
*   **Benefit hàng tháng:** Danh sách các đặc quyền in-game và out-game tương ứng với rank hiện tại.
*   **Top 50 status:** Badge highlight hiển thị nếu user đang nằm trong Top 50 nạp của server.

> [!IMPORTANT]
> **Tính năng tích hợp: Daily Gift trên Map (Interactive Building)**
> Thay vì nhận quà điểm danh qua một nút bấm độc lập vô hồn, công trình của tháng hiện tại trên Map sẽ đóng vai trò là nơi "sản xuất" và nhận quà hàng ngày.
> *   *Cơ chế:* Khi có quà hàng ngày chưa claim, building của tháng hiện tại sẽ có một **chấm đỏ (red dot) kèm hiệu ứng phát sáng nhẹ (pulse glow)**.
> *   *Tương tác:* Người chơi click trực tiếp vào building để mở modal claim quà. Sau khi nhận, building sẽ có hiệu ứng animation phát hạt (particles) ngắn tùy thuộc vào tier rank.
> *   *Quà sinh nhật:* Trong tháng sinh nhật của user, map sẽ xuất hiện decoration phụ (confetti/banner). Click vào để claim quà sinh nhật đặc biệt.

---

### Tab 2: Khu phức hợp (Dream City Overview)
*   Hiển thị cityscape toàn cảnh khu phức hợp bóng đá tích lũy của người chơi từ đầu năm đến nay.
*   Tháng đã hoàn thành hiển thị công trình sáng rõ kèm badge rank đã đạt. Click vào từng tháng để xem chi tiết lịch sử rank, chỉ số đạt được và quà đã nhận.
*   Tháng hiện tại hiển thị ở trạng thái đang xây dựng (active animation). Tháng chưa tới hiển thị dạng xám/ẩn (locked).
*   **Social visit (Phase 2):** Cho phép chia sẻ ảnh chụp Dream City lên mạng xã hội hoặc bấm "Ghé thăm" thành phố của bạn bè lấy từ danh sách bạn bè trực tiếp trong game.

---

### Tab 3: Sảnh vinh dự (Hall of Fame)
*   **Vinh danh cá nhân:** Bảng lịch sử ghi nhận tất cả cấp bậc rank PAY và PLAY mà người chơi đã đạt được qua từng tháng từ đầu năm.
*   **Vinh danh toàn server:** 
    *   Bảng xếp hạng Top nạp (PAY) và Top chơi (PLAY) theo tháng và tổng năm (cập nhật real-time).
    *   Vinh danh **MVP Tháng** (Top 1 PAY tháng) và **Iron Man Tháng** (Top 1 PLAY tháng).
    *   Vinh danh **Legend of the Year** (Top 1 nạp cả năm) - người chơi này sẽ có visual tòa tháp vinh danh độc nhất vô nhị.
*   *Lưu ý bảo mật:* Hall of Fame tuyệt đối không hiển thị số tiền nạp, chỉ hiển thị số điểm quy đổi hoặc rank symbol.

---

## 7. Cơ chế Onboarding & Khoảnh khắc chuyển giao

### 7.1. Trải nghiệm người chơi mới (Empty State - REC 1)
Để tránh tình trạng người chơi mới truy cập vào trang web chỉ thấy một bãi đất trống rỗng gây hụt hẫng (cold start):
*   Bản đồ sẽ hiển thị dưới dạng **"công trường đang thi công" (construction site)**: các ô đất trống có giàn giáo (scaffolding) và outline mờ của công trình tháng 1.
*   Hệ thống tự động kích hoạt một **onboarding tooltip** ngắn gọn (2-3 bước) giới thiệu về Pay Zone, Play Zone, cách tích lũy điểm để xây dựng thành phố.

### 7.2. Khoảnh khắc sang tháng mới (New Month Moment - REC 2)
Vào lần đầu tiên người chơi truy cập trang web trong tháng mới:
*   Hệ thống không mở pop-up làm phiền mà sử dụng hiệu ứng visual ngay trên map: highlight ô đất của tháng mới bằng animation nhấp nháy hoặc badge "New!".
*   Kích hoạt hoạt họa chốt công trình tháng trước: công trình tháng trước từ trạng thái đang xây dựng chuyển sang hoàn thành rực rỡ theo visual rank đã đạt được.

---

## 8. Logic hiển thị & Yêu cầu dữ liệu API

### 8.1. Các trường thông tin API game cần cung cấp:
*   `current_month_topup`: Tổng tiền nạp tháng này (quy đổi sang điểm để hiển thị).
*   `lifetime_topup`: Tổng tiền nạp tích lũy trọn đời từ lúc tạo tài khoản (quy đổi sang điểm).
*   `yearly_topup`: Tổng nạp tích lũy năm dương lịch (để tính SVIP/VVIP và Legacy).
*   `current_month_login_days`: Số ngày login game trong tháng.
*   `current_month_matches`: Tổng số trận đấu trong tháng.
*   `current_month_playtime`: Tổng thời gian chơi game trong tháng (tính bằng giây).
*   `account_creation_date`: Ngày tạo tài khoản (để tính thâm niên trên cây quà Play).
*   `friend_list`: Danh sách bạn bè in-game (cho tính năng social ở Phase 2).

> [!CAUTION]
> **Rủi ro kỹ thuật về dữ liệu Playtime:**
> Việc track thời gian chơi game thực tế trừ đi thời gian treo máy (idle) từ game client PC là cực kỳ phức tạp. Nếu team API xác nhận không thể lấy dữ liệu playtime thực tế chính xác 100%, hệ thống sẽ sử dụng công thức dự phòng (fallback):
> $$\text{Playtime quy đổi} = \text{Tổng số trận đấu trong tháng} \times 15\text{ phút (900 giây)}$$

---

## 9. Khung kịch bản kiểm thử (QA Checklist Framework)

Đội ngũ QA cần tập trung kiểm thử các kịch bản cốt lõi sau trên môi trường Staging:

*   **TC-001 (Tính đúng hạng PAY):** Đảm bảo hệ thống tự động gán đúng 1 trong 6 bậc rank BAY (Đồng, Bạc, Vàng, Bạch Kim, Kim Cương, Whale) dựa trên điểm tích lũy nạp tiền quy đổi tháng trước.
*   **TC-002 (Kích hoạt Rank Whale):** Kiểm tra điều kiện nạp đạt mốc 850+ điểm để kích hoạt rank Whale và hiển thị visual công trình đẹp nhất.
*   **TC-003 (Vinh danh Top 50 PAY):** Xác nhận hệ thống lọc chính xác Top 50 user nạp nhiều nhất tháng; kiểm tra cơ chế chọn ngẫu nhiên Top 5 nhận quà random đặc biệt.
*   **TC-004 (Tính điểm Play hàng tháng):** Chạy thử công thức tính điểm Play tổng hợp (kết hợp Login, Matches, Playtime). Đảm bảo hệ thống tự động gán đúng bậc rank Play (Siêng năng cấp 1, 2, 3...) tháng này dựa trên kết quả tháng trước.
*   **TC-005 (Đủ điều kiện Play Top):** Kiểm tra cơ chế gửi tặng sổ tay (notebook) tháng mới cho Top user Play hàng tháng và quà tương ứng cho các bậc dưới.
*   **TC-006 (Ẩn/Hiện Cuốn chiếu - Cây quà):** Xác nhận giao diện cây quà chỉ hiển thị 3 mốc (Mốc hiện tại highlight, Mốc +1 hiển thị rõ điều kiện, Mốc +2 hiển thị mờ, Mốc +3 trở đi ẩn hoàn toàn).
*   **TC-007 (Nút Showroom Cây quà):** Click nút "Xem toàn bộ mốc quà" mở popup hiển thị đầy đủ danh sách mốc và quà mà không làm vỡ giao diện chính.
*   **TC-008 (SVIP & VVIP Towers):** Đảm bảo tháp SVIP xuất hiện khi tích lũy năm đạt 1M, và tháp VVIP xuất hiện khi đạt 2M. Kiểm tra cơ chế bảo hiểm Q4 (giữ trạng thái active trọn năm sau nếu đạt mốc trong Q4).
*   **TC-009 (Cơ chế Legacy):** Mô phỏng ngày 01/01 năm sau: tháp năm cũ chuyển sang visual mờ đi kèm badge năm cũ (ví dụ: VVIP 2026).
*   **TC-010 (Bảo mật số tiền nạp):** Đảm bảo tuyệt đối không có API hay giao diện nào hiển thị số tiền nạp thực tế (chỉ hiển thị điểm quy đổi).
*   **TC-011 (Interactive Building - Daily Gift):** Kiểm tra hiệu ứng red dot + pulse glow trên building tháng hiện tại khi chưa nhận quà ngày, click để claim quà, và kiểm tra hiệu ứng sinh ra hạt particle sau khi nhận.
