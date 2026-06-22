# OAC Airtable Database Raw Data Summary
> **Last Updated:** 2026-06-05 | **Source:** Live query from Airtable OAC Database (via anh Đức)
> **Project Directory:** `outputs/proj-skillflo-pitch/`

Tài liệu này tổng hợp toàn bộ thông tin và số liệu thực tế được truy xuất trực tiếp từ các bảng (tables) trong cơ sở dữ liệu Airtable của OAC. Tài liệu được cấu trúc nhằm phân loại rõ ràng dữ liệu thực tế (Verified Data), các giới hạn về mặt cấu trúc (Limitations), và các chỉ số thay thế đề xuất (Pitch-Safe Alternatives) để chuẩn bị dữ liệu đầu vào cho bản Teaser và Proposal gửi đối tác Skillflo.

---

## I. Tổng Quan Cơ Sở Dữ Liệu OAC (Database Statistics)

Hệ thống Airtable OAC Database bao gồm các bảng với số lượng bản ghi (records) chi tiết như sau:
*   **Zoho Applications:** 3,823 records (Dữ liệu import hồ sơ ứng tuyển ứng viên)
*   **Daily Performance Tracker:** 1,482 records (Theo dõi hoạt động hàng ngày)
*   **Screening:** 1,351 records (Hồ sơ đánh giá, phỏng vấn sơ bộ)
*   **Candidates:** 810 records (Hồ sơ ứng viên có cấu trúc)
*   **Jobs:** 410 records (Các cơ hội tuyển dụng/mandates)
*   **Weekly Performance Tracker:** 422 records (Theo dõi hoạt động hàng tuần)
*   **Applications:** 464 records (Hồ sơ ứng tuyển theo từng job)
*   **Clients:** 72 records (Thông tin nhà tuyển dụng/đối tác)
*   **Activity Log:** 2,317 records (Nhật ký hoạt động chi tiết của recruiter)
*   **Placement:** 38 records (Dữ liệu khớp việc và doanh thu tương ứng)
*   **Users:** 22 records (Hồ sơ tài khoản thành viên hệ thống)
*   **KPI and Actual:** 12 records (Bảng theo dõi KPI)

---

## II. Phân Tích Dữ Liệu Theo Từng Chỉ Số Cốt Lõi

### 1. Số Lượng Jobs Đã Khớp / Tuyển Thành Công (Placements & Filled Jobs)
*   **Số liệu thực tế (Verified Data):**
    *   **Placements:** Có 38 bản ghi placement được tài liệu hóa chính thức trong bảng `Placement`.
    *   **Theo Onboard Date (37/38 records có ngày onboard):**
        *   Năm 2024: 4 placements.
        *   Năm 2025: 25 placements.
        *   Năm 2026: 8 placements.
        *   Không rõ ngày onboard: 1 placement.
    *   **Jobs.Opening Status (Bộ lọc trạng thái jobs):**
        *   Trạng thái **Filled**: 51 jobs.
        *   Trạng thái **Filled hết bảo hành**: 6 jobs.
        *   Tổng cộng số jobs có trạng thái đã điền: 57 jobs.
    *   **Quy mô Deal (Deal Size từ Placement):**
        *   Tính theo VND: 38 records, tổng giá trị là **4,351,478,357 VND**.
        *   Tính theo USD: 38 records, tổng giá trị là **167,224.22 USD**.
*   **Giới hạn dữ liệu (Limitations):**
    *   `Placement.Matched Date` bị trống 100% (0/38), do đó không phân tích được thời gian khớp việc từ ngày khớp đến ngày onboard.
    *   `Jobs.Seniority` không có dữ liệu, không thể phân nhóm số lượng tuyển dụng theo cấp bậc (Junior/Mid/Senior/Exec).
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Sử dụng song song 2 mốc số liệu:
        *   Mốc Thận trọng: *“38 documented placements in Placement table”*.
        *   Mốc Hệ thống ATS rộng hơn: *“57 filled job openings tracked in ATS”*.
    *   Wording đề xuất cho slide pitch: **“38 documented placements / 57 filled job openings tracked in ATS”**.

---

### 2. Mạng Lưới Đối Tác & Khách Hàng (Employers Helped & Client Metrics)
*   **Số liệu thực tế (Verified Data):**
    *   **Tổng số clients/employers trong bảng Clients:** 72 khách hàng.
    *   **Phân bổ trạng thái tài khoản (Account Status):**
        *   Current Client (Đang hoạt động): 18
        *   Active Opportunity (Cơ hội đang mở): 10
        *   Inactive Client (Ngừng hoạt động tạm thời): 23
        *   Dead Opportunity (Cơ hội đã đóng): 12
        *   Drop and Stop (Hủy hợp tác): 5
        *   Dead Client (Khách hàng không còn tương tác): 4
        *   *Tổng số khách hàng Current + Active Opportunity:* **28** đối tác hoạt động tích cực.
    *   **Khách hàng có liên kết với tin tuyển dụng (Linked Jobs):** 66/72 clients.
    *   **Khách hàng quay lại (Repeat Clients dựa trên số lượng job liên kết):**
        *   Khách hàng có 2+ jobs liên kết: 46 clients.
        *   Khách hàng có 3+ jobs liên kết: 33 clients.
        *   Khách hàng có 5+ jobs liên kết: 22 clients.
    *   **Quốc gia/Thị trường của Client (Client Countries):**
        *   Việt Nam: 37
        *   Thái Lan: 6
        *   Mỹ (US / United States): 6
        *   Singapore: 3
        *   Australia: 3
        *   Ấn Độ: 3
        *   Malaysia: 3
        *   Nhật Bản: 2
        *   Vương quốc Anh (UK): 2
*   **Giới hạn dữ liệu (Limitations):**
    *   Lĩnh vực hoạt động (Sector/Industry) ở cấp độ Client chưa được chuẩn hóa. Bảng `Jobs.Industry` chỉ có dữ liệu cho một số lượng nhỏ jobs.
    *   Ngày ký hợp đồng (`Contract Signing Date`) chỉ có dữ liệu ở 3 clients, không đủ để vẽ biểu đồ lịch sử ký kết hợp đồng.
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Số lượng đối tác: **“72 employers/clients tracked (66 with active linked mandates)”**.
    *   Khả năng giữ chân khách hàng (Client Stickiness): **“69.7% of clients (46/66) returned with 2+ mandates; 33.3% (22/66) with 5+ mandates”**.

---

### 3. Thị Trường Thực Tế & Độ Phủ Regional (Market Proof)
*   **Số liệu thực tế (Verified Data):**
    *   **Doanh thu/Giá trị Deal theo thị trường quốc gia (từ Placement):**
        *   Việt Nam: 2.951B VND
        *   Australia: 1.008B VND
        *   Singapore: 214.9M VND
        *   Nhật Bản: 90.2M VND
        *   Canada: 86.7M VND
    *   **Độ phủ Mandate theo địa điểm làm việc (từ `Jobs.Working Location` - 410 jobs):**
        *   Việt Nam: 159 jobs
        *   Singapore: 80 jobs
        *   Australia: 23 jobs
        *   Nhật Bản: 22 jobs
        *   Thái Lan: 20 jobs
        *   Mỹ (United States): 18 jobs
        *   TP. HCM: 17 jobs
        *   Hà Nội: 8 jobs
        *   Canada: 6 jobs
        *   Malaysia: 6 jobs
        *   Ba Lan (Poland): 5 jobs
        *   Vương quốc Anh (UK): 3 jobs
*   **Giới hạn dữ liệu (Limitations):**
    *   Không có trường phân loại loại hợp đồng: Retained / Contingency / Exclusive.
    *   Dữ liệu `Jobs.Job Order Category` chỉ bao gồm: *New Hire*: 64, *Replacement*: 2, *Confidential*: 1.
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Chuyển định nghĩa từ "retained track-record markets" sang: **“Multi-market placement and job coverage across Vietnam, Australia, Singapore, Japan, Canada, US, Thailand, Malaysia, etc.”**
    *   Nếu muốn giữ chữ "retained", cần phải có bằng chứng hợp đồng ngoại cảnh hoặc bổ sung thủ công trường `Mandate Type`.

---

### 4. Cơ Sở Dữ Liệu Ứng Viên (Candidate Database & Profile Quality)
*   **Số liệu thực tế (Verified Data):**
    *   **Tổng số hồ sơ ứng viên trong bảng Candidates:** 810 profiles có cấu trúc.
    *   **Phân bổ trạng thái ứng viên (Candidate Status):**
        *   Sent out (Đã gửi đi cho khách hàng): 428
        *   New (Mới): 133
        *   Rejected by AM (Từ chối bởi AM): 133
        *   Rejected by client (Từ chối bởi đối tác): 51
        *   Approved (Đã duyệt): 30
        *   Screened (Đã qua vòng lọc): 15
        *   Job Pending (Đang chờ job): 14
        *   Hired (Đã tuyển thành công): 4
        *   Dropped (Từ bỏ): 2
    *   **Mức độ đầy đủ của thông tin ứng viên (Profile Completeness - Trên 810 hồ sơ):**
        *   Có Link CV: 808/810 (99.8%)
        *   Có Summary Note: 746/810 (92.1%)
        *   Có Email liên hệ: 645/810 (79.6%)
        *   Có Số điện thoại: 585/810 (72.2%)
        *   Có Link LinkedIn: 427/810 (52.7%)
        *   Hồ sơ có CV + ít nhất một kênh liên lạc (Email/Phone): 646/810 (79.8%)
        *   Đầy đủ cả 3 kênh liên lạc (Email + Phone + LinkedIn): 411/810 (50.7%)
        *   Đầy đủ kỳ vọng lương (Salary min/max/currency): 501/810 (61.9%)
        *   Có liên kết hồ sơ phỏng vấn (Screening record): 209/810 (25.8%)
        *   Đã được AI đánh giá (AI evaluation): 122/810 (15.1%)
    *   **Kênh thu hút ứng viên (Acquired Channel):**
        *   LinkedIn: 420
        *   Facebook: 232
        *   Kênh khác (Other): 129
        *   Referral (Giới thiệu): 25
        *   Google Search: 2
    *   **Dữ liệu thô từ các nguồn khác:**
        *   Hồ sơ thô trong **Zoho Applications**: 3,823 records.
        *   Tổng dữ liệu ứng viên thô tích lũy (Candidates + Zoho): **4,633 records**.
    *   **Cơ cấu đơn vị tiền tệ của kỳ vọng lương:**
        *   USD: 476 ứng viên
        *   VND: 302 ứng viên
        *   SGD: 25 ứng viên
        *   THB (Thái Baht): 3 ứng viên
        *   GBP (Bảng Anh): 2 ứng viên
        *   LPA (Lakhs per Annum - Ấn Độ): 2 ứng viên
*   **Giới hạn dữ liệu (Limitations):**
    *   Dữ liệu thô trong Zoho Applications chưa được deduped (lọc trùng).
    *   Thiếu các trường thông tin về: Trạng thái liên hệ hoạt động (active/reachable), ngày tương tác gần nhất (last contacted date), vị trí địa lý của ứng viên, và phân loại cấp bậc đã chuẩn hóa (seniority normalized).
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   **“Talent pool of 4,633 raw candidate and application records across Airtable and Zoho ATS, including 810 structured, premium candidate profiles.”**
    *   **“High-quality candidate profiles: 99.8% with CV links, 79.8% with verified contact details, and 61.9% with structured salary expectations.”**

---

### 5. Khách Hàng Tập Trung & Đóng Góp Doanh Thu (Client Concentration)
*   **Số liệu thực tế (Verified Data):**
    *   **Doanh thu Deal Size tích lũy:** 4.351B VND (phân bổ trên 13 khách hàng tạo doanh thu trong bảng Placement).
    *   **Top 10 Khách hàng đóng góp doanh thu lớn nhất (bảng Placement):**
        1.  **RightShip:** 1.097B VND (10 placements)
        2.  **Omnistream:** 1.022B VND (6 placements)
        3.  **StoryCO:** 526.7M VND (2 placements)
        4.  **Prudential:** 492.0M VND (2 placements)
        5.  **AIA:** 271.8M VND
        6.  **Luke:** 237.4M VND
        7.  **Everfit:** 155.5M VND
        8.  **TC Advisor:** 138.4M VND (5 placements)
        9.  **Eduholic:** 132.4M VND (5 placements)
        10. **Pueo International:** 90.2M VND
    *   *Khách hàng khác có ghi nhận placements:* Wizards Lab (2 placements).
    *   **Mức độ tập trung doanh thu (Client Concentration):**
        *   Top 1 Client (RightShip): **25.2%** tổng doanh thu deal size.
        *   Top 3 Clients (RightShip, Omnistream, StoryCO): **60.8%** tổng doanh thu deal size.
        *   Top 5 Clients (Top 3 + Prudential + AIA): **78.4%** tổng doanh thu deal size.
*   **Giới hạn dữ liệu (Limitations):**
    *   Đây là doanh thu tính theo Deal Size (giá trị bán hàng dự kiến), không phải số tiền mặt thực tế đã thu về (Cash Collected).
    *   Các trường dữ liệu phản ánh thực thu (`VND received`, `USD received`, `SGD received`) hiện tại đang trống 100% (0 records).
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Lưu ý ghi chú rõ khi trình bày số liệu tài chính: **“Based on documented placement deal size, the top 3 accounts represent 60.8% of tracked placement value.”**

---

### 6. Phân Bổ Doanh Thu Theo Ngành (Revenue by Industry)
*   **Số liệu thực tế (Verified Data):**
    *   **Sự phân bổ ngành nghề của 410 Jobs tuyển dụng (chỉ có 41 jobs được nhập ngành nghề):**
        *   IT Product: 9 jobs
        *   IT Services: 8 jobs
        *   Blockchain: 5 jobs
        *   HRTech: 5 jobs
        *   Fintech / WealthTech: 3 jobs
        *   Blockchain VC: 2 jobs
        *   Blockchain / DeFi: 2 jobs
        *   Fintech Payments: 2 jobs
        *   Fintech (chung): 1 job
        *   Gaming: 1 job
        *   Software / AI: 1 job
*   **Giới hạn dữ liệu (Limitations):**
    *   Trường dữ liệu ngành nghề (`Industry`) rất thưa thớt (chỉ có dữ liệu ở 41/410 jobs, chiếm ~10%).
    *   Không có các trường phân chia doanh thu theo các mảng dịch vụ (Service Line) của OAC (ví dụ: Permanent Placement, Executive Search, Contracting, v.v.).
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Không claim mạnh về cơ cấu doanh thu theo ngành hay dịch vụ mà chuyển sang dùng: **“Job coverage and sourcing capability concentrated in high-tech and financial sectors (IT Product, IT Services, Blockchain, Fintech, HRTech)”**.

---

### 7. Hiệu Suất Của Đội Ngũ Tuyển Dụng (Recruiter Productivity & Team)
*   **Số liệu thực tế (Verified Data):**
    *   **Đóng góp doanh thu Deal Size theo Recruiter (bảng Placement.Application Owner):**
        *   Peter: 1.453B VND
        *   Lauren: 883.2M VND
        *   Serena: 763.8M VND
        *   Ellie: 714.4M VND
        *   Vicky: 492.5M VND
        *   Đào Hà: 482.1M VND
        *   Amy: 242.7M VND
        *   Tina: 216.0M VND
        *   Anna: 141.6M VND
        *   Alice: 110.2M VND
        *   Aaron: 90.2M VND
        *   Dylan: 78.5M VND
        *   Tyler: 51.3M VND
        *   Mia: 50.1M VND
        *   Mark: 30.3M VND
    *   **Cơ cấu đội ngũ vận hành hệ thống (Total Users: 22, có 18 tài khoản đang active):**
        *   Intern (Thực tập sinh): 7
        *   Recruitment Partner (Đối tác tuyển dụng): 4
        *   Associate (Chuyên viên): 3
        *   Trainee (Cộng tác viên đào tạo): 2
        *   Manager (Quản lý): 2
        *   Offboard (Đã dừng hoạt động): 4
    *   **Chỉ số hoạt động trung bình 30 ngày qua (30-day Activity Rollups):**
        *   Số cuộc gọi thực hiện: 15 calls
        *   Tổng thời lượng cuộc gọi: 390.8 phút
        *   Số CV upload lên hệ thống: 103 CVs
        *   Số CV gửi đối tác (Sent out): 72 CVs
        *   Số cuộc phỏng vấn mới: 11 phỏng vấn
        *   Số jobs đang chạy nguồn tích cực (Active sourcing): 66 jobs
        *   Số jobs đang có chủ sở hữu tích cực (Active owned): 27 jobs
        *   Số lượng hồ sơ ứng tuyển hoạt động tích cực (Active applications): 39
*   **Giới hạn dữ liệu (Limitations):**
    *   Dữ liệu đóng góp doanh thu của recruiter có thể bị trùng lặp nhẹ do cách ghi nhận cộng tác (multi-owner strings).
    *   Không có dữ liệu về Lợi nhuận gộp trên mỗi Recruiter (Gross Profit per Recruiter).
    *   Hiệu suất 30 ngày qua phản ánh hoạt động thực tế hiện tại, không thể dùng làm đại diện cho hiệu suất lịch sử trung bình năm.
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Dùng cụm từ: **“Tracked placement value attribution by recruiter”** và **“Active 30-day team operational productivity”**.

---

### 8. Tốc Độ Quy Trình Tuyển Dụng (Operational Speed & Time to Fill)
*   **Số liệu thực tế (Verified Data):**
    *   **Tốc độ lọc nguồn và phỏng vấn sơ bộ (từ bảng Jobs):**
        *   *Thời gian tìm thấy ứng viên đầu tiên (Time to 1st Source - 71 jobs):* Trung bình 16.0 ngày, **Trung vị (Median) là 4.0 ngày**.
        *   *Thời gian gửi hồ sơ đầu tiên cho khách (Time to 1st Sent out - 64 jobs):* Trung bình 22.5 ngày, **Trung vị (Median) là 8.5 ngày**.
        *   *Thời gian thực hiện cuộc phỏng vấn đầu tiên (Time to 1st Interview - 42 jobs):* Trung bình 28.0 ngày, **Trung vị (Median) là 18.0 ngày**.
    *   **Thời gian hoàn thành placement (từ ngày có JD đến ngày Onboard - 30 records mẫu):**
        *   Trung bình: 128.6 ngày.
        *   **Trung vị (Median): 93.5 ngày** (Dao động từ 13 ngày đến tối đa 536 ngày).
*   **Giới hạn dữ liệu (Limitations):**
    *   Do thiếu dữ liệu ngày khớp ứng viên (`Matched Date`), không thể tính toán chính xác khoảng thời gian khớp ứng viên thực tế (Time to Match).
    *   Số liệu trung bình (Average) bị kéo lên cao do một số jobs cũ hoạt động lâu chưa đóng. Do đó, việc sử dụng số **Trung vị (Median)** sẽ khách quan và tăng tính thuyết phục hơn.
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Sử dụng số Trung vị (Median) cho các mốc thời gian:
        *   **“Median of 4 days to source the first candidate”**
        *   **“Median of 8.5 days to first candidate submission (Sent-out)”**
        *   **“Median of 18 days to coordinate the first client interview”**
        *   **“Median of 93.5 days from mandate creation to candidate onboarding (across 30 tracked placements)”**

---

### 9. Dữ Liệu Vòng Tuyển Dụng & Pipeline (Funnel Speed & Stages)
*   **Số liệu thực tế (Verified Data):**
    *   **Tổng số hồ sơ ứng tuyển ứng viên:** 464 ứng tuyển.
    *   Có ghi nhận ngày gửi đi (Send-out Date): 464/464.
    *   Ứng viên lọt vào vòng phỏng vấn lần 1 (1st interview): 155/464.
    *   *Thời gian từ lúc gửi hồ sơ đến khi phỏng vấn lần 1 (128 records mẫu):* Trung bình 14.2 ngày, **Trung vị (Median) là 8.0 ngày** (Dao động từ 0 đến 110 ngày).
    *   **Phân bổ trạng thái ứng tuyển hiện tại (Application Stages):**
        *   Submitted (Đã gửi CV): 110
        *   Shortlisted (Đã lọt vào danh sách rút gọn): 8
        *   Interview-to-be-Scheduled (Chuẩn bị phỏng vấn): 6
        *   Interview-in-Progress (Đang phỏng vấn): 21
        *   Offer Made (Đã gửi offer): 7
        *   To be onboarded (Chuẩn bị đi làm): 7
        *   Onboarded (Đã đi làm): 7
    *   **Tổng số lượng ứng viên trong đường ống giai đoạn cuối (Pipeline):** **21 ứng viên** (bao gồm Offer Made + To be onboarded + Onboarded).
*   **Giới hạn dữ liệu (Limitations):**
    *   Dữ liệu `2nd Interview` và `Hired Date` trong bảng Applications trống 100% (0 records), do đó không tính được chính xác thời gian từ lúc nộp hồ sơ đến lúc nhận offer (Submission-to-Offer timing).
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Sử dụng: **“Operational funnel speed: Median of 8 days from CV submission to 1st interview coordinate”**.
    *   Sử dụng: **“Active late-stage pipeline: 21 candidates in final stages (Offer Made / Onboarding)”**.

---

### 10. Kỷ Luật Vận Hành & Hồ Sơ Phỏng Vấn (Scorecard & Activity Logs)
*   **Số liệu thực tế (Verified Data):**
    *   **Nhật ký hoạt động tuyển dụng tích lũy (Activity Log):** 2,317 hoạt động đã ghi nhận.
        *   Call (Gọi điện): 830
        *   Submit (Nộp hồ sơ): 606
        *   Send out (Gửi CV cho khách): 311
        *   Interview (Phỏng vấn): 86
        *   New Job (Nhập job mới): 52
    *   **Phân bổ nhật ký theo năm:**
        *   Năm 2024: 2 hoạt động.
        *   Năm 2025: 795 hoạt động.
        *   Năm 2026: 1,520 hoạt động.
    *   **Dữ liệu phỏng vấn sâu (Screening Table):** 1,351 cuộc phỏng vấn sơ bộ đã ghi nhận.
        *   Screening Call (Gọi phỏng vấn sơ bộ): 1,098
        *   Training (Đào tạo nội bộ): 107
        *   Client Meeting (Họp với khách hàng): 64
        *   Prep Interview (Chuẩn bị phỏng vấn cho ứng viên): 55
        *   Team Meeting (Họp đội ngũ): 15
        *   Hoạt động khác: 3
        *   **Thời lượng phỏng vấn sơ bộ tích lũy:** **51,177 phút** (Trung bình 37.9 phút/cuộc gọi).
*   **Giới hạn dữ liệu (Limitations):**
    *   Dữ liệu chỉ số 7 ngày gần đây hiển thị thấp do bộ lọc hoặc cập nhật chậm trên Airtable. Nên dùng dữ liệu tích lũy dài hạn.
*   **Chỉ số thay thế an toàn (Pitch-Safe Alternatives):**
    *   Sử dụng minh chứng cho tính kỷ luật của quy trình: **“High-integrity operational tracking: 2,317 documented recruiting activities and 1,351 structured screening records totaling 51,177 minutes of interview time.”**

---

## III. Danh Sách Các Chỉ Số KHÔNG ĐỦ DỮ LIỆU ĐỂ TUYÊN BỐ (Not Pitch-Safe)

Dưới đây là các chỉ số **tuyệt đối không được đưa vào Pitch Deck/Teaser** dưới dạng dữ liệu hệ thống Airtable, vì các trường liên quan hiện tại đang trống hoặc không tồn tại. Đưa vào sẽ tạo rủi ro lớn khi thẩm định (Due Diligence):

1.  **800 Recruiters Trained (OAC Academy):** Airtable không có dữ liệu đối tác đào tạo bên ngoài (External recruiters), các dòng "Training" trong bảng Screening thực tế là các cuộc họp/phóng vấn đào tạo nội bộ của OAC (107 records).
2.  **Alumni Network (Mạng lưới cựu thành viên):** Không có bảng theo dõi Alumni, không có thông tin về tỷ lệ active hay địa điểm công tác hiện tại của Alumni.
3.  **Retained Search Track Record (Lịch sử tuyển dụng dạng Retained/Exclusive):** Hệ thống không ghi nhận thông tin phân loại Mandate (Retained/Contingency).
4.  **Gross / Operating Profit Trend (Xu hướng biên lợi nhuận):** Bảng KPI and Actual trống các số liệu thực tế (`Actual Selling Value`, `Actual Cash` đều bằng 0). Không có dữ liệu COGS, chi phí lương nhân viên hay chi phí vận hành.
5.  **90-day Candidate Retention / Falloff Rate (Tỷ lệ ứng viên nghỉ việc trong thời gian bảo hành):** Không có trường dữ liệu theo dõi trạng thái bảo hành hay ứng viên nghỉ việc trước hạn.
6.  **Contracting / Project Staffing Capability (Năng lực Staffing/Contracting):** Chỉ có 3 khách hàng có ngày ký hợp đồng (`Contract Signing Date`). Không có dữ liệu về thời hạn dự án, số lượng contractor đang làm việc hay hợp đồng đối tác Singapore.

---

## IV. Tóm Tắt Dữ Liệu Khuyên Dùng Cho Pitch Deck & Teaser (Pitch-Safe Headline Metrics)

```text
+----------------------------------------------------+---------------------------------------------------+
|         CHỈ SỐ THẬT CÓ SỨC NẶNG (NÊN DÙNG)          |         CHỈ SỐ SỬ DỤNG GIẢ ĐỊNH / PROXY           |
+----------------------------------------------------+---------------------------------------------------+
| - 72 Khách hàng tuyển dụng đã hỗ trợ               | - Tỷ lệ lặp lại mandate: 69.7% đối tác có 2+ jobs |
| - 38 Placements được xác nhận / 57 jobs filled     | - Độ phủ thị trường: Placement tại VN, AU, SG, JP |
| - Doanh thu deal size tích lũy: 4.351B VND         | - Tốc độ tìm nguồn: Trung vị 4 ngày có CV đầu     |
| - Top 3 clients chiếm 60.8% doanh thu bán hàng     | - Tốc độ phỏng vấn: Trung vị 8 ngày từ CV đến PV |
| - 810 Hồ sơ ứng viên cấu trúc (99.8% có link CV)   | - Thời gian onboard: Trung vị 93.5 ngày từ khi có |
| - 4,633 Hồ sơ thô tích lũy (bao gồm cả Zoho ATS)   |   yêu cầu tuyển dụng đến khi onboard thực tế      |
| - 1,351 Screening records (51,177 phút phỏng vấn)  |                                                   |
| - 2,317 Recruiting activities logged               |                                                   |
+----------------------------------------------------+---------------------------------------------------+
```
