# Do / Don't cho Internal Tool dùng AntD

---

## Do

- Dùng Pro Components có chọn lọc khi chúng giảm wrapper hoặc boilerplate rõ ràng

- Dùng `DESIGN.md` làm visual/system contract
- Dùng `LAYOUT-BLUEPRINT.md` làm structural contract
- Dùng AntD core components trước khi nghĩ đến custom UI
- Giữ page types lặp lại nhất quán giữa nhiều project
- Dùng token thay vì hardcode màu, spacing, radius
- Giữ 1 primary action mỗi nhóm
- Dùng overlay để giữ context khi task ngắn
- Thêm empty/loading/error/confirmation states đầy đủ
- Cho phép business wrapper nếu wrapper chỉ compose AntD

## Don't

- Không thay simple screens sang Pro Components nếu không có lợi ích rõ ràng

- Không duy trì `BaseUI` như hệ UI song song
- Không đề xuất `InputField`, `SelectField`, `SearchableSelect` như foundation mặc định
- Không tạo nhiều visual style cho cùng một component type
- Không hardcode spacing/màu nếu đã có token
- Không dùng dropdown để giấu action chính
- Không dùng text mơ hồ như `OK`, `Submit`, `Action` khi label cụ thể hơn là cần thiết
- Không thêm helper text nếu UI đã tự giải thích đủ
- Không override semantic colors theo sở thích thẩm mỹ
- Không đổi typography scale và spacing rhythm theo từng project
