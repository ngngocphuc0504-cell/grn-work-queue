# KB-04: Pipeline Tìm Nguồn & Boolean X-Ray Sourcing
# Source: Global Executive Search Sourcing Methodology (Loxo, Fullenrich, RecruitBPM)

> [!IMPORTANT] RAG POINTER
> Agent tải file này khi cần: (1) Xây dựng Boolean Search String,
> (2) Quản lý CRM Pipeline giai đoạn, (3) Phân loại Long List → Short List,
> (4) Xử lý ứng viên Silver Medalist (tuyến 2).

---

## 1. Pipeline Chuẩn (11 Giai Đoạn)

| Giai Đoạn | Mô Tả | % Lọc Điển Hình |
|---|---|---|
| **Sourced** | Tên được thêm vào hệ thống qua Research | 100% (Toàn bộ) |
| **Contacted** | Đã gửi outreach; đang theo dõi phản hồi | 100% → 60% response |
| **Screened** | Đã hoàn thành cuộc gọi sơ bộ | 60% → 40% qualified |
| **Long List** | Pool ban đầu được xây dựng (50–80 tên) | 40% pool |
| **Short List** | 3–7 ứng viên tinh lọc trình Client | < 10% từ Long List |
| **Interviewing** | Đang trong vòng phỏng vấn Client | 3–7 ứng viên |
| **Under Consideration** | Finalist; quản lý kỳ vọng và hứng thú | 2–3 ứng viên cuối |
| **Offer/Negotiation** | Đang trong giai đoạn chốt lương | 1–2 ứng viên |
| **Hired/Placed** | Đã ký hợp đồng, ngày bắt đầu đã xác nhận | 1 ứng viên |
| **Warranty** | Theo dõi 30-60-90 ngày post-placement | 1 ứng viên |
| **Silver Medalist/Nurture** | Ứng viên tốt nhưng không được chọn lần này | Toàn bộ còn lại |

---

## 2. Boolean X-Ray Sourcing (Chuẩn 3 Tầng)

### Tầng 1 — X-Ray Google vào LinkedIn
```
site:linkedin.com/in ("[Chức danh 1]" OR "[Chức danh 2]") AND ("[Ngành]" OR "[Tech Stack]") 
AND ("[Keyword năng lực]") -intitle:jobs -inurl:jobs -"looking for" -"open to work"
```
**Ví dụ thực chiến:**
```
site:linkedin.com/in ("Sales Director" OR "VP Sales" OR "Head of Sales") 
AND ("SaaS" OR "B2B") AND ("scaling" OR "P&L" OR "ARR") 
-intitle:jobs -inurl:jobs -"actively seeking"
```

### Tầng 2 — Lọc Passive Candidates
Bổ sung vào chuỗi `NOT` operator để loại bỏ "kẻ thả CV":
```
-"actively seeking" -"available for opportunities" -"open to new roles" 
-"looking for my next" -"seeking a new challenge" -"job search"
```

### Tầng 3 — Achievement-Based Search (Năng Lực Bằng Thành Tích)
Thay vì chỉ tìm Title, tìm theo bằng chứng thành tích:
```
("led strategy" OR "scaled from" OR "turnaround" OR "P&L responsibility" OR "promoted to")
```

### Weight Operator `^` (Dành Cho ATS/CRM Nâng Cao - Loxo)
```
("SaaS" ^ 5 OR "B2B")  
→ Ứng viên có "SaaS" trong profile được coi là relevant hơn 5× so với chỉ có "B2B"
```

---

## 3. Hypothesis → Test → Refine Loop

Không bao giờ viết Boolean String hoàn hảo ngay lần đầu. Thực hiện theo chu trình:

```
Bước 1 (Broad): Tìm với Title + 1 Industry Term. Mục tiêu: 200+ kết quả.
Bước 2 (Analyze): Review 20-30 kết quả đầu. Note các từ không liên quan xuất hiện.
Bước 3 (Prune): Thêm những từ rác vào NOT list. Mục tiêu: 50-80 kết quả chất lượng.
Bước 4 (Template): Lưu String đã lọc làm "Search Template" cho JD tương tự.
```

---

## 4. Silver Medalist Nurture Protocol

Ứng viên tốt nhưng không được chọn = Tài sản Dài Hạn quan trọng.

**Lịch Giữ Liên Hệ:**
- Tháng 1 sau Placement: Gửi email chia sẻ market insight liên quan đến ngành của họ.
- Tháng 3: LinkedIn comment vào post của họ. Ghi nhận thành tựu mới.
- Tháng 6: Check-in ngắn. "Khi nào có role phù hợp, tôi muốn bạn là người đầu tiên biết."
- Tháng 12: Đề xuất cụ thể nếu có mandate mới phù hợp.
