# Data Format — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/data-format

---

## 1. MỤC TIÊU

Chuẩn hoá cách hiển thị dữ liệu — đảm bảo user hiểu nhanh, chính xác, nhất quán.

---

## 1.1 DEFAULT UI LOCALE CONTRACT

- Default internal-tool system UI locale: **English**
- Dates, times, relative time, calendar labels, and numeric formatting in system UI must not depend on browser or OS locale
- Use explicit locale configuration in `ConfigProvider`, date library setup, and shared formatting utilities
- Multilingual content is allowed only for business content, not for system chrome

---

## 2. SỐ (Numerical Values)

### Phân cách hàng nghìn:
```
✅ 1,234,567
❌ 1234567
```

### Đơn vị:
```
✅ 1,234 followers     (viết thường, có khoảng trắng)
✅ 78.5%               (không khoảng trắng trước %)
✅ 12/100              (progress dạng phân số)
```

### Component hỗ trợ:
```jsx
import { Statistic } from "antd";

// Tự format số
<Statistic title="Followers" value={1234567} />           // → 1,234,567
<Statistic title="Tỉ lệ" value={78.5} suffix="%" />      // → 78.5%
<Statistic title="Revenue" value={9800} prefix="$" />      // → $9,800

// InputNumber format
<InputNumber
  formatter={(value) => `${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
  parser={(value) => value.replace(/,/g, "")}
/>
```

---

## 3. TIỀN TỆ (Amount)

### Format: `Ký hiệu tiền tệ + số`

| Loại | Format | Ví dụ |
|---|---|---|
| VND | đ hoặc VND | đ1,234,000 hoặc 1,234,000 VND |
| USD | $ | $1,234.00 |
| Số lớn | Viết tắt | $1.2M (million), $3.5B (billion) |

### Quy tắc:
- Luôn hiện 2 chữ số thập phân cho USD: $1,234.00
- VND không cần thập phân: đ1,234,000
- Số lớn viết tắt: M (Million), B (Billion) — hoặc Mill., Bill.

---

## 4. THỜI GIAN TUYỆT ĐỐI (Absolute Time)

### Format mặc định cho system UI tiếng Anh:

| Loại | Format | Ví dụ |
|---|---|---|
| Ngày | YYYY-MM-DD | 2026-04-05 |
| Ngày + giờ | YYYY-MM-DD HH:mm | 2026-04-05 14:30 |
| Ngày + giờ + giây | YYYY-MM-DD HH:mm:ss | 2026-04-05 14:30:45 |
| Khoảng ngày | YYYY-MM-DD ~ YYYY-MM-DD | 2026-04-01 ~ 2026-04-30 |
| Date label with month name | DD MMM YYYY | 05 Apr 2026 |
| Date range with month name | DD MMM YYYY - DD MMM YYYY | 18 Mar 2026 - 17 Apr 2026 |

### 24-hour vs 12-hour:
- **Internal tool**: Dùng 24-hour (14:30) — rõ ràng hơn
- **Consumer-facing**: Có thể dùng 12-hour (2:30 PM)

### dayjs format strings:
```jsx
import dayjs from "dayjs";
import "dayjs/locale/en";

dayjs.locale("en");

dayjs(date).format("YYYY-MM-DD");           // 2026-04-05
dayjs(date).format("YYYY-MM-DD HH:mm");     // 2026-04-05 14:30
dayjs(date).format("YYYY-MM-DD HH:mm:ss");  // 2026-04-05 14:30:45
dayjs(date).locale("en").format("DD MMM YYYY"); // 05 Apr 2026
dayjs(date).format("DD/MM/YYYY");            // 05/04/2026 (nếu cần)
```

---

## 5. THỜI GIAN TƯƠNG ĐỐI (Relative Time)

| Khoảng cách | Hiển thị |
|---|---|
| < 1 phút | "Vừa xong" |
| < 1 giờ | "X phút trước" |
| < 24 giờ | "X giờ trước" |
| > 24 giờ, cùng năm | "MM-DD HH:mm" |
| > 1 năm | "YYYY-MM-DD HH:mm" |

### Khi nào dùng relative time:
- **Activity feed, timeline, notification** — dùng relative
- **Table cell, form display** — dùng absolute
- **Report, analytics** — dùng absolute

```jsx
// Utility function
const formatRelativeTime = (dateStr) => {
  const diff = dayjs().diff(dayjs(dateStr), "minute");
  if (diff < 1) return "Vừa xong";
  if (diff < 60) return `${diff} phút trước`;
  if (diff < 1440) return `${Math.floor(diff / 60)} giờ trước`;
  if (dayjs(dateStr).isSame(dayjs(), "year")) {
    return dayjs(dateStr).format("MM-DD HH:mm");
  }
  return dayjs(dateStr).format("YYYY-MM-DD HH:mm");
};
```

---

## 6. DỮ LIỆU ẨN (Data Redaction)

Bảo vệ thông tin nhạy cảm. Thay ký tự bằng `*`.

### Mức độ ẩn:

| Mức | Mô tả | Ví dụ |
|---|---|---|
| **Ẩn hoàn toàn** | Thay tất cả bằng `***` | Dùng cho data nhạy cảm cao |
| **Ẩn một phần** | Giữ đầu/cuối, ẩn giữa | Cho phép nhận diện |

### Rules theo loại dữ liệu:

| Loại | Cấp bảo mật | Format | Ví dụ |
|---|---|---|---|
| Tên người | Thấp | Ẩn tên (giữ họ) | Nguyễn **** |
| Số điện thoại | Trung bình | Ẩn 4 số giữa | 0912****567 |
| Email | Trung bình | Ẩn trước @ | ng****@gmail.com |
| CMND/CCCD | Cao | Ẩn 6 số giữa | 012******890 |
| Số tài khoản | Cao | Chỉ hiện 4 số cuối | **** **** **** 1234 |
| Địa chỉ | Trung bình | Ẩn số nhà, đường | ****, Quận 1, TP.HCM |

---

## 7. TRẠNG THÁI DỮ LIỆU

### Empty state — không có data:
```
Hiển thị: --
(hoặc dùng component <Empty /> cho vùng lớn)
```

```jsx
// Table cell trống
render: (val) => val ?? "--"

// Descriptions item trống
<Descriptions.Item label="Phone">{phone || "--"}</Descriptions.Item>
```

### Loading state:
- Dùng `<Skeleton />` khi đang tải data
- KHÔNG hiển thị "0" hoặc trống khi data chưa load xong

---

## 8. QUY TẮC CHUNG CHO INTERNAL TOOL

1. **Nhất quán format** xuyên suốt app — đặc biệt ngày tháng và số
2. **Tạo utility functions** chung cho format number, date, currency
3. **Dùng dayjs** cho mọi xử lý ngày tháng (antd DatePicker yêu cầu)
3.1 **Khóa locale rõ ràng** cho dayjs và component library; không để runtime tự suy ra locale
4. **Table cell trống** → `--` (không để trống hoàn toàn)
5. **Số lớn** → viết tắt (1.2K, 3.5M) trong dashboard, số đầy đủ trong detail
6. **Currency** → luôn hiện ký hiệu tiền tệ, không để user phải đoán
