# QA Checklist Format

## Template

```markdown
# QA Checklist: [Tên Tool] v[x.x]
**Tester:** | **Date:** | **Environment:** staging / prod

## Functional Testing
- [ ] Đăng nhập thành công với tài khoản hợp lệ
- [ ] Đăng nhập thất bại hiển thị lỗi rõ ràng
- [ ] [Core feature 1] hoạt động đúng luồng chính
- [ ] [Core feature 1] xử lý edge case: dữ liệu rỗng
- [ ] [Core feature 1] xử lý edge case: dữ liệu lớn
- [ ] Filter / search hoạt động đúng
- [ ] Export (nếu có) tạo file đúng format

## Permission Testing
- [ ] Role Viewer không thấy nút edit/delete
- [ ] Role Editor có thể lưu thay đổi
- [ ] Admin có đủ quyền

## UI/UX Testing
- [ ] Responsive trên màn hình 1920px
- [ ] Responsive trên màn hình 1366px
- [ ] Loading state hiển thị khi fetch data
- [ ] Empty state hiển thị khi không có data
- [ ] Error state hiển thị khi API lỗi
- [ ] Không có broken layout khi text dài

## Performance
- [ ] First load < 3 giây
- [ ] Filter/search response < 1 giây

## Bugs tìm thấy
| # | Mô tả | Severity | Status |
|---|---|---|---|
| 1 | ... | High/Med/Low | Open |
```

---

# Changelog Format

## Template

```markdown
# Changelog — [Tên Tool]

## [x.x.x] — YYYY-MM-DD
### Thêm mới
- [Tính năng mới]

### Cải tiến
- [Cải tiến tính năng cũ]

### Sửa lỗi
- [Bug đã fix]

### Breaking Changes (nếu có)
- [Thay đổi ảnh hưởng người dùng]
```
