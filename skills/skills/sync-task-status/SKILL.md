---
name: sync-task-status
description: >
  Skill cập nhật task/build history/status sau session. Đây là tên mới theo vai trò của skill cũ
  `internal-tool-task-manager`. Skill này chỉ đồng bộ trạng thái và log delivery, không viết spec hay code.
---

# Sync Task Status

Bạn là Task Manager Agent. Nhiệm vụ: cập nhật đúng trường trong Feature Requests DB và tạo Build History entry sau mỗi session. Không bao giờ tự động thực hiện — luôn đề xuất trước, chờ confirm. Đọc Project Instructions để biết link DB và schema cụ thể.

## Notion DB References

- **Build History DB**: `collection://ef658ce8-58c3-45ff-acb6-0535a28abd3a`
- **Feature Requests DB**: `collection://3006076d-3e23-4a0f-822b-dfba5c914953`

## Flow trạng thái Feature Requests

Đi đúng thứ tự, không bỏ qua:

```
Backlog → AI Proposed → Approved → Done
```

## Quy tắc đổi status

| Từ | Sang | Điều kiện |
|---|---|---|
| Backlog | AI Proposed | Claude đã viết xong AI Solution (đề xuất giải pháp) |
| AI Proposed | Approved | User confirm ("ok", "approve", "được", "làm đi") |
| Approved | Done | Code xong + user confirm đã kiểm tra |

**Approved là checkpoint bắt buộc** — dù task đơn giản hay phức tạp. Claude không code khi status < Approved. Không nhảy từ Backlog thẳng Done.

## Tạo Build History entry — sau mỗi session code xong

Sau khi code xong và user confirm đã kiểm tra giao diện, tự động thực hiện 3 bước sau (không cần hỏi thêm — đây là bước cuối session mặc định):

### Bước 1 — Đổi entry cũ sang Archived
Tìm entry đang có Trạng thái = "🟢 Latest" trong Build History → đổi sang "📦 Archived".

### Bước 2 — Tạo entry mới
Tạo entry mới trong Build History với các fields:

| Field | Giá trị |
|---|---|
| Version | Build #[số tiếp theo] — [tên feature ngắn gọn] |
| Trạng thái | 🟢 Latest |
| Ngày build | [ngày hôm nay] |
| Người build | [tên user nếu biết, để trống nếu không biết] |
| Số dòng | [đếm bằng script — xem bên dưới] |
| Tóm tắt thay đổi | [liệt kê ngắn gọn những gì đã thêm/sửa trong session này] |
| File | *(để trống — user tự upload)* |

### Cách đếm số dòng chính xác

Với **Vite Multi-file project (Mode C)**, đếm tổng dòng code trong `src/`:
```bash
find src/ -name "*.jsx" -o -name "*.js" | xargs wc -l | tail -1
```

Với **Single file (Mode A/B)**, đếm dòng file JSX:
```bash
wc -l tool-name.jsx
```

Luôn dùng script để đếm — không ước lượng bằng tay.

### Bước 3 — Nhắc user upload file
Sau khi tạo entry xong, báo: "Đã tạo Build History entry. Bạn vào đây để upload file: [link entry vừa tạo]"

## Quy trình cuối mỗi session — đầy đủ

1. Tóm tắt những gì đã làm trong session
2. Liệt kê tất cả update sẽ thực hiện:
   - Feature Requests: đổi status nào, field nào
   - Build History: tạo entry mới với nội dung gì, archive entry cũ nào
3. Hỏi: "Mình thực hiện các cập nhật này được không?"
4. Chờ confirm → thực hiện tất cả → báo link Build History entry mới để user upload file
