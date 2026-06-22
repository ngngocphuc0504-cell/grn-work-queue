# Tài liệu đi kèm — Format Templates

---

## User Guide

Viết bằng tiếng Việt, tránh jargon kỹ thuật. Dùng thuật ngữ vận hành hàng ngày.

```markdown
# Hướng dẫn sử dụng [Tên Tool]
**Phiên bản:** x.x | **Cập nhật:** [ngày]

## Mục đích
[Tool giúp bạn làm gì, tiết kiệm thời gian như thế nào — 2-3 câu]

## Ai dùng tool này
- [Role 1]: có thể [làm A, B, C]
- [Role 2]: chỉ xem [X, Y]

## Bắt đầu nhanh
1. Truy cập [URL]
2. Đăng nhập tài khoản công ty
3. [Bước đầu tiên quan trọng nhất]

## Các việc thường làm

### [Tên công việc 1]
**Khi nào làm:** [mô tả tình huống bằng ngôn ngữ vận hành]
**Cách làm:**
1. ...
2. ...
**Kết quả:** [bạn sẽ thấy gì, hệ thống sẽ làm gì]

## Các màu sắc cảnh báo
- 🔴 Đỏ: cần xử lý ngay
- 🟡 Vàng: sắp đến deadline
- 🟢 Xanh: đang tốt, không cần xử lý

## Câu hỏi thường gặp
**Q: ...**
A: ...

## Liên hệ hỗ trợ
[Slack channel / email]
```

---

## Tech Spec

```markdown
# Tech Spec: [Tên Tool]
**Status:** Draft / Review / Approved
**PM:** | **Dev:** | **Date:**

## Overview
- Mục đích: [1-2 câu]
- Users: [số lượng, role]
- Timeline: [deadline]

## Tech Stack
- Frontend: React + Ant Design v5
- Backend: [nếu có]
- Database: [nếu có]

## Features & Scope
### In Scope
| Feature | Priority | Notes |
|---|---|---|

### Out of Scope

## Permission Matrix
| Action | Viewer | Editor | Admin |
|---|---|---|---|

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|

## Config Structure
```json
{
  "countries": ["VN", "TH", "ID"],
  "games": ["game_id_1", "game_id_2"],
  "features": {
    "export": true,
    "import": false
  }
}
```

## Non-functional Requirements
- Performance: load < 3s
- Browser: Chrome, Edge (latest 2)
```

---

## QA Checklist

```markdown
# QA Checklist: [Tool] v[x.x]
**Tester:** | **Date:** | **Env:** staging

## Functional
- [ ] Luồng chính hoạt động đúng
- [ ] Filter theo country/game hoạt động
- [ ] Export ra file đúng dữ liệu
- [ ] Permission: viewer không thấy nút edit
- [ ] Empty state hiển thị khi không có data
- [ ] Error state hiển thị khi API lỗi
- [ ] Loading state hiển thị khi fetch data

## UI
- [ ] Layout đúng trên 1920px
- [ ] Layout đúng trên 1366px
- [ ] Màu cảnh báo đỏ/vàng/xanh đúng theo target
- [ ] Badge số đỏ hiển thị đúng số lượng

## Bugs
| # | Mô tả | Severity | Status |
|---|---|---|---|
```

---

## Changelog

```markdown
# Changelog — [Tên Tool]

## [x.x.x] — YYYY-MM-DD
### Thêm mới
- 

### Cải tiến
- 

### Sửa lỗi
- 
```
