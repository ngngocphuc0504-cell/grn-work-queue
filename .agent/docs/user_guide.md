# OAC BD Warm-Up Hub — User Guide

Chào mừng team OAC BD đến với **Warm-Up Hub**! Dưới đây là hướng dẫn sử dụng công cụ để quản lý quá trình warm-up email cá nhân của bạn.

---

## 1. Dành cho Member (Thành viên)

### Đăng nhập
1. Truy cập vào đường link hệ thống: `[Điền URL Production vào đây]`
2. Click **Sign in with Google**.
3. **Lưu ý:** Bạn chỉ có thể đăng nhập bằng email `@onearw.com`. Nếu dùng email cá nhân, hệ thống sẽ từ chối truy cập.

### Dashboard Chính (Today's Tasks)
Mỗi ngày, hãy vào màn hình chính để thực hiện các nhiệm vụ:
- **Tiến độ Warm-Up:** Bạn sẽ thấy mình đang ở ngày bao nhiêu trong chu kỳ 28 ngày, và mục tiêu gửi email hôm nay là bao nhiêu.
- **Tính năng Script Cá Nhân:** Hệ thống đã chuyển sang dùng Personal Scripts. Bạn có thể tự quản lý các đoạn script của riêng mình.
- **Campaign Emails:** Sử dụng chức năng **Copy Emails** để lấy nhanh danh sách email người nhận.
- **Gửi Email Nhanh:** Bấm **Draft in Gmail** để hệ thống tự động mở cửa sổ soạn thảo Gmail (qua `mailto:`) với các thông tin đã được copy, giúp tiết kiệm thời gian chuyển tab.

### Báo cáo Hằng Ngày (Daily Log)
Sau khi hoàn tất việc gửi email, hãy cập nhật tiến độ:
- Kéo xuống phần **Log form** trên màn hình chính.
- Nhập số lượng email bạn đã gửi thành công, số reply nhận được.
- Check vào ô "Có email nào bị vào Spam không?" nếu có.
- **Lưu ý:** Mỗi ngày chỉ được submit log 1 lần.

---

## 2. Dành cho Team Admins

Admin có toàn quyền quản lý tiến độ và kịch bản cho team. Hiện tại quyền Admin được set cứng cho các email sau:
- `oac.vn@onearw.com`
- `lauren.luu@onearw.com`
- `ellie.tran@onearw.com`

### Quản lý Script
- Admin có thể truy cập **Script Library** để upload, chỉnh sửa và xóa các mẫu script toàn cục nếu cần.
- Hỗ trợ trình soạn thảo **Rich Text (TipTap)**: bạn có thể bôi đậm, in nghiêng, chèn link... và thành viên khi copy sẽ giữ nguyên định dạng đó sang Gmail.

### Quản lý Tiến Độ Team (Team Dashboard)
- Admin có thể xem được Dashboard toàn team: tổng số lượng email đã gửi, tỷ lệ đạt KPI của các member.
- Bảng chi tiết log (số liệu gửi, reply, spam flag) của từng thành viên.

---

## 3. Quy trình Copy `firestore.rules` (Chỉ dành cho Admin thiết lập ban đầu)
Nếu hệ thống yêu cầu cấu hình lại quyền truy cập database:
1. Mở file `firestore.rules` (đã được lưu trong bộ source code).
2. Đăng nhập vào [Firebase Console](https://console.firebase.google.com).
3. Chọn Project **oac-bd-warmup**.
4. Cột bên trái, chọn **Firestore Database** -> Chọn Tab **Rules**.
5. Xóa hết nội dung cũ, Copy toàn bộ nội dung từ file `firestore.rules` và Paste vào đó.
6. Click **Publish**.

---
*Chúc team OAC có một đợt Warm-up thành công và đạt hiệu suất cao nhất!*
