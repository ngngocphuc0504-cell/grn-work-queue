# 📖 Mass-Market Translation Dictionary
## Từ Điển Thuật Ngữ Tiếp Cận Đại Chúng (Tối ưu cho AI Model nhẹ)
**Version:** 1.0 | **Áp dụng:** Toàn bộ `CTO`, `QUALITY-GATE`, và các Agent giao tiếp.

---

## 1. MỤC ĐÍCH
Để đảm bảo toàn bộ hệ thống giao tiếp trơn tru, dễ hiểu đối với tệp người dùng phổ thông (Non-tech mass users) và tối ưu hóa chi phí/độ trễ khi làm việc với các hệ thống LLM thương mại hóa (như **Gemini Flash / Gemini Pro**). Các Agent, Prompt, và Thông báo bắt buộc phải sử dụng bộ từ vựng chuẩn hóa tiếng Việt dưới đây thay cho các thuật ngữ tiếng Anh gốc.

## 2. BỘ TỪ ĐIỂN CHUẨN HÓA CỐT LÕI

### 2.1. Nhóm Thuật ngữ Hệ thống & Kiến trúc (System & Architecture)
| Thuật ngữ Gốc (Tiếng Anh) | Thuật ngữ Chuẩn hóa (Tiếng Việt) | Định nghĩa dùng trong Prompt |
| :--- | :--- | :--- |
| **Second Brain** | **Bộ Não Thứ Hai** | Nơi lưu trữ, phân loại toàn bộ kiến thức, quy trình, và kinh nghiệm làm việc cá nhân. |
| **Knowledge Graph** | **Sơ Đồ Tri Thức** | Mạng lưới dữ liệu kết nối 5 khía cạnh cốt lõi của một cá nhân. |
| **Nodes** | **Cụm Thông Tin** | 5 mảnh ghép tạo nên Sơ đồ tri thức (Kỹ năng, Dự án, Mối quan hệ, Kiến thức, Mục tiêu). |
| **Event-Driven** | **Kích Hoạt Theo Sự Kiện** | Hệ thống tự động phản ứng và chạy ngầm mỗi khi người dùng có hành động cụ thể (VD: Bật/Tắt máy). |
| **Lazy-Evaluation** | **Tính Toán Hoãn Lại** | Cơ chế gom nhiều dữ liệu lại và chỉ tính điểm một lần khi máy hoạt động, không chạy ngầm gây nặng máy. |

### 2.2. Nhóm Thuật ngữ Gamification (Trò Chơi Hóa)
| Thuật ngữ Gốc (Tiếng Anh) | Thuật ngữ Chuẩn hóa (Tiếng Việt) | Định nghĩa dùng trong Prompt |
| :--- | :--- | :--- |
| **Gamification** | **Trò Chơi Hóa** | Biến công việc khô khan thành mô hình có nhiệm vụ, điểm số và cơ chế lên cấp. |
| **Capability Points (CP)**| **Điểm Năng Lực (CP)** | Điểm số kiếm được khi người dùng nâng cấp bộ kỹ năng hoặc hoàn thành chuẩn đầu ra. |
| **Decay / Dormancy** | **Phạt Trì Trệ** | Cơ chế trừ điểm nếu người dùng bỏ bê công việc hoặc không đóng góp tri thức trong 3+ ngày. |
| **Blind Trust** | **Duyệt Mù (Không Dò Báo Cáo)** | Lỗi khi bạn nhắm mắt duyệt nhanh đầu ra của Agent mà không đọc/sửa. Bị trừ điểm. |
| **Levels / Ranks** | **Cấp Độ** | Các nấc thang trưởng thành của người dùng (Thực tập sinh -> Chuyên gia -> Lãnh đạo). |

### 2.3. Nhóm Thuật ngữ Phân tích & Định hướng (Advisory & Analytics)
| Thuật ngữ Gốc (Tiếng Anh) | Thuật ngữ Chuẩn hóa (Tiếng Việt) | Định nghĩa dùng trong Prompt |
| :--- | :--- | :--- |
| **Anti-pattern** | **Thói Quen Xấu** | Hành vi lặp lại gây tốn thời gian, lãng phí tài nguyên hoặc thao tác thủ công rườm rà. |
| **Solopreneur** | **Cá Nhân Kinh Doanh Độc Lập** | Người tự vận hành và gánh vác toàn bộ mảng kinh doanh/dự án của riêng mình. |
| **Alignment** | **Định Hướng Lại** | Việc hệ thống nhắc nhở, nắn chỉnh lại lộ trình làm việc khi phát hiện đi chệch mục tiêu. |
| **Current State Twin (CST)**| **Chân Dung Hiện Tại** | Bản sao kỹ năng và năng suất thực tế hiện nay của người dùng. |
| **Future Role Twin (FRT)**| **Chân Dung Mục Tiêu** | Hình mẫu công việc tương lai mà người dùng muốn đạt tới. |

## 3. QUY TẮC SỬ DỤNG CHO AGENT (PROMPTING RULES)
*Khi thiết lập các Prompt planning/execution (Đặc biệt cho Gemini Flash):*
1. **Ưu tiên "Thuật ngữ Chuẩn hóa":** Thay vì nói *"Tiến hành cập nhật Knowledge Graph bằng hệ thống Lazy-Evaluation"*, hệ thống phải xuất dòng *"Cập nhật **Sơ Đồ Tri Thức** của bạn qua quá trình **Tính Toán Hoãn Lại**"*.
2. **Kèm theo analogy (phép so sánh):** Khi cần giải nghĩa phức tạp cho người dùng, sử dụng so sánh thực tế nhỏ gọn.
3. **Mỏng nhẹ và trực diện:** Flash/Pro hiểu cấu trúc danh sách rất tốt. Tránh prompt hàn lâm dài dòng ngốn token. Hướng dòng suy nghĩ (thought logic) của nó theo ngôn ngữ "chuẩn hóa" tiếng Việt này.
