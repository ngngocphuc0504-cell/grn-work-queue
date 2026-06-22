# 📖 ONBOARDING GUIDE — OAC Headhunt 360°
# Cẩm nang dành cho Thành viên Mới
# Version: 1.0 | Last Updated: 2026-04-28

> [!IMPORTANT]
> Đây là tài liệu **bắt buộc đọc** trước khi bắt đầu làm việc với hệ thống.
> Ước tính thời gian đọc: **15 phút**.
> Sau khi đọc xong, chạy lệnh `/MAS-01-onboard-tutorial` để hoàn tất đăng ký vào hệ thống.

---

## 1. Giới thiệu hệ thống

### OAC Headhunt 360° là gì?

**OAC Headhunt 360°** là hệ thống Agentic AI chuyên biệt cho ngành Executive Search & Selection, được xây dựng trên nền tảng **Antigravity AI IDE**. Hệ thống này thay thế phần lớn công việc thủ công trong quy trình tuyển dụng — từ phân tích JD, viết Boolean Search, tạo outreach message, đến brief phỏng vấn và đàm phán offer.

### Tại sao dùng Antigravity thay vì ChatGPT thông thường?

| Vấn đề với ChatGPT thông thường | Giải pháp của Antigravity |
|---|---|
| Mỗi lần mở tab mới → mất hết context | Session có bộ nhớ, nạp lại context tự động |
| Phải copy-paste thủ công | Đọc/ghi file trực tiếp vào workspace |
| Không biết quy trình nội bộ OAC | Được train bằng Knowledge Base riêng của OAC |
| Không tích hợp được tool ngoài | Kết nối NotebookLM, chạy script Python, v.v. |

### Vai trò của Agent trong quy trình tuyển dụng

Agent **KHÔNG** thay thế bạn — Agent là **Trợ lý Nghiên cứu cấp cao** giúp bạn:
- Tiết kiệm 2-4 giờ/ngày trên các tác vụ lặp lại
- Chuẩn hóa chất lượng output (không phụ thuộc vào ngày tốt/xấu)
- Lưu trữ kiến thức của team để người mới onboard nhanh hơn

---

## 2. Cấu trúc Folder Chuẩn

> [!NOTE]
> Tham chiếu thực tế: xem folder `outputs/TASK-02_Maritime-Safety_Software-Architect/` để hiểu cấu trúc chuẩn.

```
ws-oac-headhunt-360/
│
├── 📁 .agent/
│   ├── workflows/          ← 17+ Workflows đang hoạt động (các lệnh /slash)
│   └── skills/             ← Skills chuyên biệt (Boolean Search, CV Formatting...)
│
├── 📁 .context/
│   ├── domain/
│   │   ├── INDEX.md        ← Master Router KB — ĐỌC ĐẦU TIÊN khi cần tìm KB
│   │   ├── kb-01-bd-fee-model.md         ← Mô hình phí & hợp đồng
│   │   ├── kb-02-bd-outreach-sequence.md ← Chuỗi tiếp cận BD 30 ngày
│   │   ├── kb-03-competency-framework.md ← Khung năng lực Korn Ferry
│   │   ├── kb-04-sourcing-pipeline.md    ← Pipeline ứng viên & Boolean X-Ray
│   │   ├── kb-05-offer-warranty.md       ← Đàm phán Offer & Warranty 30-60-90
│   │   └── kb-06-market-intelligence.md  ← Tình báo thị trường & Positioning OAC
│   ├── PROJECT.md          ← Mô tả workspace tổng quan
│   └── BLUEPRINT_INTAKE_FINAL.md
│
├── 📁 inputs/
│   ├── raw_jds/            ← Đặt PDF JD gốc từ Client vào đây trước
│   └── linkedin_profiles/  ← Đặt PDF LinkedIn ứng viên vào đây để batch-parse
│
├── 📁 outputs/
│   ├── TASK-XX_[Client]_[Role]/   ← Mỗi Job Order = 1 thư mục riêng
│   │   ├── JOB_DETAIL.md          ← Overview nhanh của Job
│   │   ├── JOB_ORDER_SCHEMA.md    ← Chi tiết phân tích JD (Must-have, Timeline)
│   │   ├── PERSONA_ARRAY.md       ← 3 Archetype Ứng viên
│   │   ├── WF09_Job_Intake/       ← Output của /DEL-01-job-intake
│   │   ├── WF10_Job_Sourcing/     ← Output của /DEL-02-job-sourcing
│   │   │   ├── BOOLEAN_STRINGS.md
│   │   │   └── CANDIDATE_TRACKER.csv
│   │   ├── WF11_Candidate_Pitch/  ← Output của /DEL-04-candidate-pitch
│   │   ├── WF12_Interview_Prep/   ← Output của /DEL-05-interview-prep
│   │   ├── WF13_Offer_Management/ ← Output của /DEL-06-offer-management
│   │   └── WF15_Warranty/         ← Output của /DEL-08-warranty-check
│   └── session_records/
│       └── [TenUser]/             ← Session report hàng ngày, mỗi user 1 subfolder
│
├── 📄 PIPELINE_TRACKER.md  ← Dashboard tổng quan toàn bộ Jobs đang chạy
├── 📄 ONBOARDING_GUIDE.md  ← File này
└── 📁 scripts/             ← Script tự động hóa (batch-parse, nlm-init...)
```

---

## 3. Quy trình làm việc chuẩn (Vòng đời 1 Job Order)

```
JD Nhận về → /DEL-01-job-intake → /DEL-02-job-sourcing → /DEL-04-candidate-pitch
           → /DEL-05-interview-prep → /DEL-06-offer-management → /DEL-08-warranty-check
```

### Chi tiết từng bước:

| Bước | Lệnh | Input cần có | Output tạo ra |
|---|---|---|---|
| 1. Intake | `/DEL-01-job-intake` | JD từ Client (PDF/text) | `JOB_ORDER_SCHEMA.md`, `PERSONA_ARRAY.md`, `JOB_CALIBRATION_STRATEGY.md` |
| 2. Sourcing | `/DEL-02-job-sourcing` | Output Intake | `BOOLEAN_STRINGS.md`, `CANDIDATE_TRACKER.csv` |
| 3. Batch Parse CV | `/DEL-03-batch-parse` | PDF LinkedIn ứng viên | Update `CANDIDATE_TRACKER.csv` |
| 4. Outreach | `/DEL-04-candidate-pitch` | Profile ứng viên | `BLIND_PROFILE_*.md` |
| 5. Call Script | `/DEL-10-job-script-call` | Profile + JD | `CALL_SCRIPT_*.md` |
| 6. Interview | `/DEL-05-interview-prep` | Lịch phỏng vấn + profile | `INTERVIEW_BRIEF_*.md` |
| 7. Offer | `/DEL-06-offer-management` | Offer letter + thông tin UV | Script đàm phán |
| 8. Warranty | `/DEL-08-warranty-check` | Ngày onboarding UV | `WARRANTY_CHECKIN_*.md` |

> [!IMPORTANT]
> **Quy trình Sourcing với Custom GPT:** Sau khi chạy xong `/DEL-01-job-intake` và có file `INTAKE_BRIEF.md`, hãy copy toàn bộ nội dung file này và paste vào link [OAC Boolean Strings Expert Custom GPT](https://chatgpt.com/g/g-6a1024709d8c819180115fc4b6f87d8a-oac-boolean-strings-expert) để nhận kết quả chuỗi Boolean Search nhanh và chuẩn xác nhất.

> [!WARNING]
> Mỗi Job Order phải được tạo subfolder riêng theo format `TASK-XX_[Client]_[Role]` trước khi bắt đầu. Không để output của nhiều job lẫn lộn vào nhau.

---

## 4. Workflow BD (Business Development)

| Bước | Lệnh | Mô tả |
|---|---|---|
| Thẩm định lead | `/BD-01-audit-lead` | Chấm điểm khách hàng tiềm năng (MEDDIC) |
| Lập hồ sơ khách | `/BD-02-prospect` | Phân tích sâu công ty, chẩn đoán pain point |
| Thiết kế campaign | `/BD-03-campaign` | Kế hoạch tiếp cận đa kênh 4-5 touchpoints |
| Viết outreach | `/BD-04-outreach` | Email + LinkedIn DM tàng hình cho C-Level |
| Gửi proposal | `/BD-05-proposal` | Brief + Proposal sau Discovery Call |

---

## 5. Workflow Marketing

| Lệnh | Mô tả | Tần suất |
|---|---|---|
| `/MKT-01-monthly-plan` | Lịch content 4 tuần | Đầu tháng |
| `/MKT-02-brand-content` | 3 ý tưởng content LinkedIn (Insight/Story/Education) | Hàng tuần |
| `/MKT-03-job-post` | Bài đăng tuyển LinkedIn + Facebook | Mỗi khi có job mới |

---

## 6. Session Management (BẮT BUỘC)

> [!WARNING]
> Luôn chạy `/MAS-03-start-session` ở đầu mỗi ngày và `/MAS-04-end-session` ở cuối ngày.
> KHÔNG bỏ qua — session report là dữ liệu training cho team và cơ sở review hiệu suất.

| Lệnh | Dùng khi nào | Tác dụng |
|---|---|---|
| `/MAS-03-start-session` | **Đầu mỗi ngày** | Nạp context, xác nhận user identity, xem pending tasks |
| `/MAS-02-checkpoint-session` | Giữa session (sau 2-3 tiếng) | Lưu tạm tiến độ, không đóng session |
| `/MAS-04-end-session` | **Cuối mỗi ngày** | Tạo session report, lưu vào `outputs/session_records/` |

---

## 7. Batch Parse LinkedIn Profiles (Tự động hóa)

Khi nhận được CV PDF của ứng viên từ LinkedIn:

**Bước 1:** Đặt tất cả file PDF vào đúng thư mục của task:
```
outputs/TASK-XX_[Client]_[Role]/LinkedIn Profiles/
```

**Bước 2:** Gõ lệnh:
```
/DEL-03-batch-parse --task TASK-XX
```

**Script `batch_parse_v2.py` sẽ tự động:**
1. **PDF → Markdown** — dùng thư viện `pymupdf4llm` (chạy offline, không cần API)
2. **Markdown → JSON** — Gemini AI phân tích fit level so với JD
3. **JSON → CSV** — điền vào `CANDIDATE_TRACKER.csv`
4. **Xóa PDF gốc** tự động sau khi parse thành công

> [!NOTE]
> **Không cần cài extension ngoài.** Chỉ cần `pip install pymupdf4llm` một lần.
> Phần Gemini AI (bước phân tích fit) cần `GEMINI_API_KEY` trong file `.env`.

---

## 8. Lần đầu dùng — Checklist

- [ ] Đọc xong tài liệu này (✓ bạn đang ở đây)
- [ ] Chạy `/MAS-01-onboard-tutorial` để đăng ký thông tin cá nhân
- [ ] Chạy `/MAS-03-start-session` để khởi động phiên làm việc đầu tiên
- [ ] Xem `PIPELINE_TRACKER.md` để biết các Job Order đang active
- [ ] Thử một workflow: copy-paste JD vào chat và gõ `/DEL-01-job-intake`
- [ ] Cuối ngày: chạy `/MAS-04-end-session` để tạo session report đầu tiên

---

## 9. Hỏi & Đáp nhanh

**Q: Tôi quên gõ `/MAS-03-start-session`, vẫn làm việc bình thường được không?**
A: Được, nhưng Agent sẽ không có context về user identity và pending tasks từ hôm trước. Nên gõ ngay khi nhớ ra.

**Q: File PDF CV tôi scan bị lỗi chữ, batch parse có hoạt động không?**
A: `pymupdf4llm` xử lý được hầu hết PDF, nhưng scan chất lượng thấp có thể bị mất chữ. Nếu bị lỗi, thử dùng `/DEL-04-candidate-pitch` và paste text thủ công.

**Q: Tôi muốn thêm Job Order mới vào PIPELINE_TRACKER, làm thế nào?**
A: Gõ `/DEL-01-job-intake` và cung cấp JD. Agent sẽ tự động tạo subfolder và update Tracker.

**Q: Script batch_parse_v2.py báo lỗi API key?**
A: Kiểm tra file `.env` có dòng `GEMINI_API_KEY=your_key_here` chưa. Hỏi admin để lấy key.

---

*Tài liệu này được tạo tự động bởi OAC Headhunt 360° | Version 1.0 | 2026-04-28*
