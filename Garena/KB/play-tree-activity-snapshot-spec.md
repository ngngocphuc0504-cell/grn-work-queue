# Feature Spec & Recommendations — FC Online VIP Revamp
> **Phạm vi tài liệu này:** Các gap trong brief v1.0.1 cần bổ sung vào thiết kế.

---

# PART A — Feature: Activity Snapshot (Play Tree Page)

> **Trạng thái trong brief v1.0.1:** Chưa có. Brief section 4.1 chỉ define công thức tính điểm Play Tree, không có UX spec cho việc hiển thị lại hoạt động của người chơi.

## 1. Mô tả

Hiển thị **lịch sử hoạt động thực tế** của người chơi ngay trong Play Tree node hiện tại, giúp họ tự đối chiếu điểm tích lũy với những gì đã làm — không recommend, không gợi ý, chỉ show data.

## 2. Vị trí đặt

**Màn hình:** Play Tree Page (Screen 2), khi toggle về Play Tree.

**Vị trí:** Bên trong **current milestone node**, ngay dưới progress bar và fraction "X / Y điểm".

```
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

## 3. Dữ liệu hiển thị

### Cột "Tháng này"
| Metric | Nguồn dữ liệu |
|---|---|
| Số trận đã chơi | Game session logs, tháng hiện tại |
| Số ngày đăng nhập | Login records, tháng hiện tại |
| Tổng thời gian chơi (phút) | Session duration sum, tháng hiện tại |

### Cột "Tháng trước"
Cùng 3 metrics, tháng liền trước — để người chơi tự so sánh, không cần thêm label hay nhận xét.

### Dòng "Từ đầu năm"
- Tổng trận từ 01/01 đến hiện tại
- Tổng ngày login từ 01/01 đến hiện tại
- Không hiển thị phút — số sẽ quá lớn và ít ý nghĩa trong khung năm

## 4. Triết lý thiết kế

- **Show, don't tell.** Không có dòng nào dạng "Bạn cần chơi thêm X trận". Người chơi đọc số liệu và tự rút ra kết luận.
- **Tháng trước làm baseline tự nhiên.** So sánh với chính mình tháng trước thực tế hơn và ít áp lực hơn.
- **Compact.** Section này là context bổ trợ — font nhỏ hơn, màu nhạt hơn so với reward info phía trên.
- **Play Tree only.** Pay Tree không cần vì FC+MC nạp là single-source metric, đã rõ ràng.

## 5. Ghi chú triển khai

- Thời gian chơi (phút) cần confirm với Nexon Korea về data availability qua API.
- Số trận và ngày login đã available vì đang được dùng trong Play Tier calculation.
- Thuần display — không ảnh hưởng logic tính điểm hay tier.

---

# PART B — Feature: Daily Gift trên Map (Interactive Building)

> **Trạng thái trong brief v1.0.1:** Chưa có. Trang VIP hiện tại có "Quà hàng ngày", "Quà sinh nhật", "Quà rương may mắn", "VIP Shop" — không cái nào được đưa vào brief revamp.

## 1. Concept

Thay vì một button riêng biệt, **building current month trên map là nơi người chơi tương tác để nhận quà hàng ngày**. Building "produce" quà mỗi ngày, giống như cơ sở thật sự đang hoạt động.

Điều này biến daily login từ "vào tab → click button → thoát" thành "vào map → thấy building sáng lên → interact" — thế giới cảm giác sống hơn.

## 2. Chi tiết từng loại quà

### Quà hàng ngày
- **Trigger:** Building của tháng hiện tại (ô T7 nếu đang là tháng 7) hiển thị **red dot + pulse glow** khi có quà chưa nhận
- **Interaction:** Click vào building → modal nhỏ xuất hiện để claim
- **Feedback:** Sau khi claim → animation ngắn trên building (ánh sáng, particles tùy tier)
- **Cả 2 zone:** Pay Zone building và Play Zone building của tháng hiện tại đều có thể có daily gift riêng (cần confirm với PM)

### Quà sinh nhật
- **Trigger:** Trong tháng sinh nhật của người chơi, một decoration đặc biệt overlay lên map (banner, confetti nhẹ)
- **Interaction:** Click vào decoration → modal claim gift
- **Chỉ hiện** trong tháng sinh nhật, không clutter thường ngày

### Quà rương may mắn + VIP Shop
- Đặt trong **footer bar**, cạnh nút Sảnh Danh Vọng
- Frequency thấp hơn daily gift → không cần prime real estate trên map
- Footer: `[🏆 Sảnh Danh Vọng]  [🎰 Rương May Mắn]  [🛒 VIP Shop]`

## 3. Ghi chú

- Cần define: Daily gift có khác nhau theo tier không? (VIP Gold nhận quà tốt hơn Bronze?)
- Cần define: Nếu người chơi không có tier (chưa nạp tháng này), building có còn daily gift không?
- Visit mode: Building của người khác không có red dot / interaction — chỉ visual

---

# PART C — Recommendations (Giữ lại)

## REC 1 — Empty State / New User Experience *(Critical — Phase 1)*

**Gap:** Brief im lặng hoàn toàn về trường hợp người chơi mới — 12 ô đất trống mỗi zone, cây quà ở 0 điểm, không có tier. Cold start tệ nhất có thể.

**Đề xuất:**
- Bản đồ hiển thị dạng "construction site" — scaffolding/outline của công trình tháng 1, chưa hoàn thiện
- Onboarding tooltip ngắn giải thích Pay Zone / Play Zone
- Không cần full tutorial — đủ để người chơi hiểu họ đang nhìn vào cái gì

## REC 2 — New Month Moment *(Engagement — Phase 1)*

**Gap:** Brief spec rõ logic monthly building nhưng không có UX cho khoảnh khắc transition sang tháng mới — vốn là lý do lớn nhất để quay lại trang.

**Đề xuất:** Khi người chơi vào trang lần đầu trong tháng mới:
- Highlight ô đất mới mở (pulse animation hoặc "New!" badge)
- Show tier tháng trước đã được "chốt" → công trình vừa xây với visual tier nào
- Không cần pop-up — một visual cue trên map là đủ

---

## Bảng tổng hợp

| # | Feature / Rec | Loại | Priority |
|---|---|---|---|
| Part A | Activity Snapshot | Feature bổ sung | Phase 1 |
| Part B | Daily Gift on Map | Feature bổ sung — core engagement | Phase 1 |
| REC 1 | Empty State | Gap cần fill | 🔴 Critical |
| REC 2 | New Month Moment | Engagement hook | 🟠 High |
