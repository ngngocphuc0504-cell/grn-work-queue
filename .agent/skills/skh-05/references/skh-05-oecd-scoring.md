# SKH-05 OECD Co-Work Scoring Method

## 1. Trục Đo Lường OECD (Human Oversight vs Blind Trust)
Việc sử dụng Agentic AI đòi hỏi sự uỷ quyền (Delegation). Tuy nhiên, mức độ uỷ quyền phải đi đôi với sự kiểm duyệt.

### Blind Trust (Thất bại chuẩn OECD)
- Dấu hiệu: Human gửi prompt mơ hồ -> Agent trả một khối văn bản dài -> Human gõ "Duyệt" hoặc "Lưu lại".
- Hậu quả: Mất dần quyền kiểm soát hệ thống, triệt tiêu tư duy phê phán.
- Điểm: Tối đa 2/5 (Critical Review = 1/5).

### Meaningful Human Oversight (Đạt chuẩn OECD)
- Dấu hiệu: Bắt Agent bóc tách vấn đề -> Human chỉnh sửa lại Cấu trúc (Approach) -> Agent thực thi -> Human review sửa từ ngữ/lập luận -> Chốt.
- Hậu quả: Human giữ cương vị "Kiến trúc sư hệ thống".
- Điểm: Điểm tuyệt đối (Critical Review = 5/5).

## 2. Tiêu chí Chấm điểm Mới (Solopreneur Lens)
| Điểm | Mô tả hành vi Co-work | Action Whitelist Check |
|---|---|---|
| **Level 1** | Human tự làm hết, AI chỉ tra cứu Wikipedia. Hoặc Human mù quáng copy/paste toàn bộ lời AI. | N/A |
| **Level 2** | Human giao task, AI làm, Human nhận nhưng không thèm đọc kỹ (Blind Trust). | Bypass Action Gate |
| **Level 3** | Human phân tách task rõ ràng (Bounded). AI làm, Human có feedback sửa lỗi cơ bản. | Tuân thủ Gate |
| **Level 4** | Human giao task dưới chuẩn Solopreneur (Đóng gói workflow thành Service). Human reject các ý kiến chung chung của AI. | Thiết lập Rule chặt |
| **Level 5** | Meaningful Oversight. Human điều khiển đa Agent, review chuẩn, bóc tách layer T3/T4 sắc sảo. Nâng cấp hệ thống sau 1 chu kỳ. | Master Whitelist |

*Luật: Bất kỳ khi nào tính SKH-05, phải kết hợp ma trận này với công thức nội hàm cũ của Skill.*
