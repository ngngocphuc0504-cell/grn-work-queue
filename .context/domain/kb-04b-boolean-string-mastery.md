# KB-04B: Boolean String Mastery — OAC Sourcing Standard
# Source: NotebookLM [OAC] — Boolean String Guide
# Distilled: 2026-04-20 | Agent: AG/OAC

> [!IMPORTANT] RAG POINTER
> Đọc file này khi cần: (1) Build/Fix Boolean string mới, (2) Troubleshoot 0 kết quả, (3) Audit chất lượng string trước khi sourcing.
> **Mục tiêu:** Đạt "Hit List" — 70–100% kết quả trang 1 là ứng viên pre-qualified.

---

## 1. LUẬT CÚ PHÁP — PHẢI NHỚ THUỘC LÒNG

| Rule | ✅ Đúng | ❌ Sai |
|---|---|---|
| Operator PHẢI VIẾT HOA | `AND`, `OR`, `NOT` | `and`, `or`, `not` |
| Cụm 2+ từ PHẢI có dấu ngoặc kép | `"Software Architect"` | `Software Architect` |
| Nhóm OR PHẢI có dấu ngoặc tròn | `(Java OR Python) AND Developer` | `Java OR Python AND Developer` |
| KHÔNG dùng wildcard `*` | `(Engineer OR Engineers OR Engineering)` | `Engineer*` |
| KHÔNG dùng dấu `-` (trừ tên) | `NOT Junior` | `-Junior` |

**Tại sao quan trọng:** LinkedIn đọc `and` thường như là keyword bình thường, không phải toán tử logic. String sẽ fail hoàn toàn mà bạn không biết lý do.

---

## 2. CHIẾN LƯỢC XÂY DỰNG STRING — BLOCK METHOD (5 Khối)

Không bao giờ nhồi tất cả vào 1 field. Tách JD thành 5 block riêng biệt:

```
[Block 1] TITLE BLOCK
  → Tất cả biến thể chức danh có thể (OR logic)
  → Dán vào: LinkedIn "Title" field
  → Bật toggle: "Current" (cực kỳ quan trọng — xem mục 4)

[Block 2] MANDATORY SKILL BLOCK
  → Kỹ năng bắt buộc (AND với Block 1)
  → VD: Java OR Python

[Block 3] ENVIRONMENT/CONTEXT BLOCK
  → Môi trường làm việc (cloud, kiến trúc, hệ thống)
  → VD: AWS OR Azure OR Microservices

[Block 4] SENIORITY/EXCLUSION BLOCK
  → Lọc cấp độ + loại trừ noise
  → VD: (Senior OR Lead) NOT (Intern OR Trainee OR Student)

[Block 5] LOCATION OVERLAY
  → Chỉ set trong filter của LinkedIn, không nhét vào string
```

---

## 3. QUY TRÌNH SPEAR-FISHING — 4 BƯỚC ITERATIVE

```
BƯỚC 1 — NARROW (Quick Wins)
  Title field: Exact title (VD: "Software Architect")
  → Mục tiêu: 50-150 kết quả. Review trang 1.

BƯỚC 2 — EXPAND (Mở rộng synonyms)
  Title field: "Software Architect" OR "Solutions Architect" OR "Technical Architect"
  → Thêm dần synonyms, đo lại match rate.

BƯỚC 3 — ZOOM IN (Thêm skill filter)
  Keywords field: Azure AND .NET
  Experience filter: 8-15 years
  → Thu hẹp xuống pool chất lượng cao.

BƯỚC 4 — BROADEN (Khi pool cạn)
  Title field: Engineer (broad)
  Keywords field: "Software Architect" AND Azure AND .NET
  → Tìm người có từ "Software Architect" trong body/description profile.
```

---

## 4. CÁC LỖI CHẾT NGƯỜI (BẮT BUỘC TRÁNH)

### 🚨 Lỗi 1: Không bật "Current" Toggle
- **Hậu quả:** LinkedIn tìm cả người từng làm role đó 10 năm trước → Phần lớn đã lên Manager/Director, không còn làm kỹ thuật.
- **Fix:** LUÔN bật "Current" khi search bằng Title field.

### 🚨 Lỗi 2: "Implicit OR" Trap (LinkedIn UX Bẫy)
- **Hành vi nguy hiểm:** Dán skill vào nhiều ô filter khác nhau → LinkedIn xử lý như OR (mở rộng pool rác).
- **Fix:** Dùng `AND` explicit trong 1 ô Keywords duy nhất.
  - ❌ Sai: Box 1: `Azure` | Box 2: `.NET`
  - ✅ Đúng: Keywords: `Azure AND .NET`

### 🚨 Lỗi 3: NOT quá mạnh tay
- **Hậu quả:** String `NOT (Junior OR Intern OR Student)` loại Senior Engineer đang *mentor* junior khỏi kết quả.
- **Fix:** Chỉ dùng NOT trong Title field, KHÔNG dùng NOT trong Keywords field.
  - ✅ Đúng: Title: `NOT (Junior OR Intern)` — Loại chức danh rác.

---

## 5. BẢNG SYNONYM CHO TECH ROLES (Dùng Ngay)

### Software Architect / Backend / System Design
```
("Software Architect" OR "Solutions Architect" OR "Technical Architect" OR "Principal Engineer" OR "Staff Engineer") AND Azure AND ("distributed systems" OR microservices OR ".NET" OR Python)
```

### Backend Engineer
```
("Backend Engineer" OR "Software Engineer" OR "Server-side Developer" OR "Systems Developer") AND (Java OR Python OR Go) AND (Microservices OR "REST API" OR SQL)
```

### Frontend Engineer
```
("Frontend Developer" OR "Web Developer" OR "UI Engineer" OR "JavaScript Developer") AND (React OR Angular OR Vue OR TypeScript OR "Next.js")
```

### Data Engineer
```
("Data Engineer" OR "Big Data Engineer" OR "Analytics Engineer" OR "ETL Developer") AND (Spark OR Hadoop OR Airflow OR Snowflake OR Python OR Scala)
```

### DevOps / SRE / Platform
```
("DevOps Engineer" OR "Site Reliability Engineer" OR "SRE" OR "Platform Engineer") AND (Kubernetes OR Terraform OR Docker OR "CI/CD") AND (AWS OR Azure OR GCP)
```

---

## 6. PASSIVE CANDIDATE FILTERS (Tầng 2 — Anti-Rác)

Thêm vào cuối Keywords string để loại "người đang tìm việc":
```
-"actively seeking" -"open to work" -"open to new opportunities" -"looking for my next role" -"job search" -"available immediately"
```

> **Khi nào dùng:** Sau khi đã có pool decent (~100+ kết quả). Nếu dùng sớm khi pool nhỏ → sẽ còn lại rất ít.

---

## 7. ACHIEVEMENT-BASED SEARCH (Tầng 3 — Tìm "Người Thực Sự Làm")

Thay vì chỉ tìm Title, tìm bằng bằng chứng thành tích trên profile:
```
Keywords: ("led migration" OR "scaled to" OR "architecture design" OR "reduced latency" OR "built from scratch" OR "led a team of" OR "technical roadmap")
```

---

*v1.0 — Distilled from NotebookLM [OAC] Boolean String Guide | 2026-04-20*
*Next Review: 2026-05-20 | Maintained by: AG/OAC*
