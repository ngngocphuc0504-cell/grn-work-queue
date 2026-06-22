# Button Usage — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/buttons

---

## 1. NGUYÊN TẮC THIẾT KẾ

- **Hướng dẫn user** đạt hành động mong muốn
- **Ngăn ngừa lỗi** — button nguy hiểm phải có xác nhận

---

## 2. CÁC LOẠI BUTTON

### Button thường:

| Loại | Component | Mức nhấn mạnh | Dùng khi |
|---|---|---|---|
| **Primary** | `<Button type="primary">` | Cao nhất | Hành động chính: Lưu, Tạo, Duyệt |
| **Default** | `<Button>` | Trung bình | Hành động phụ: Huỷ, Reset, Filter |
| **Text** | `<Button type="text">` | Thấp | Hành động nhẹ: Xem thêm, Link |
| **Icon** | `<Button icon={<.../>}>` | Tuỳ | Tiết kiệm không gian |
| **Dashed** | `<Button type="dashed">` | Thấp | Hướng dẫn thêm nội dung |

### Button đặc biệt:

| Loại | Component | Dùng khi |
|---|---|---|
| **Danger** | `<Button danger>` | Xoá, reject — hành động rủi ro |
| **Ghost** | `<Button ghost>` | Trên nền tối/có màu |
| **Link** | `<Button type="link">` | Như hyperlink nhưng dạng button |

---

## 3. QUY TẮC NHẤN MẠNH (Emphasis)

### Tối đa 1 Primary Button mỗi nhóm:
```jsx
// ✅ Đúng
<Space>
  <Button>Huỷ</Button>
  <Button type="primary">Lưu</Button>
</Space>

// ❌ Sai — 2 primary buttons
<Space>
  <Button type="primary">Huỷ</Button>
  <Button type="primary">Lưu</Button>
</Space>
```

### Sắp xếp theo mức quan trọng:
- Button ít quan trọng hơn → đặt **bên trái / phía trên**
- Button quan trọng nhất → đặt **bên phải / phía dưới**
- User đọc từ trái sang phải → hành động chính cuối cùng = ít sai sót

---

## 4. VỊ TRÍ ĐẶT BUTTON (Placement)

### Theo reading pattern:

| Vị trí | Ví dụ | Pattern |
|---|---|---|
| **Header** (đầu trang) | Toolbar: "Thêm mới", "Export" | Z-pattern — CTA ở góc phải trên |
| **Body** (trong form) | Inline action | F-pattern |
| **Footer** (cuối form/modal) | "Huỷ", "Lưu" | Conversation flow |

### Modal / Drawer footer:
```jsx
// Conversation flow: Cancel → OK (phải sang trái = tiến về trước)
<Modal
  footer={[
    <Button key="cancel" onClick={onClose}>Huỷ</Button>,
    <Button key="ok" type="primary" onClick={onSave}>Lưu</Button>,
  ]}
/>
```

### Page toolbar:
```jsx
// CTA bên phải
<div style={{ display: "flex", justifyContent: "space-between" }}>
  <span style={{ fontSize: 16, fontWeight: 500 }}>Danh sách Creator</span>
  <Space>
    <Button icon={<ExportOutlined />}>Xuất CSV</Button>
    <Button type="primary" icon={<PlusOutlined />}>Thêm Creator</Button>
  </Space>
</div>
```

### Navigation flow (Steps):
```jsx
// Back bên trái, Next bên phải
<div style={{ display: "flex", justifyContent: "flex-end", gap: 8 }}>
  <Button onClick={prev}>Quay lại</Button>
  <Button type="primary" onClick={next}>Tiếp theo</Button>
</div>
```

---

## 5. BUTTON GROUP

### Spacing:
- Dùng `<Space>` — default gap 8px
- Buttons cùng nhóm logic nên gần nhau
- Tách nhóm khác bằng khoảng trống hoặc divider

### Collapse khi nhiều actions:
```jsx
import { Dropdown, Button } from "antd";

// ≤ 3 actions: hiện hết
<Space>
  <Button onClick={approve}>Duyệt</Button>
  <Button onClick={edit}>Sửa</Button>
  <Button danger onClick={del}>Xoá</Button>
</Space>

// > 3 actions: collapse vào dropdown
<Space>
  <Button type="primary" onClick={approve}>Duyệt</Button>
  <Dropdown menu={{ items: [
    { key: "edit", label: "Sửa" },
    { key: "export", label: "Xuất" },
    { key: "delete", label: "Xoá", danger: true },
  ]}}>
    <Button>Thêm <DownOutlined /></Button>
  </Dropdown>
</Space>
```

---

## 6. BUTTON LABELS

### Quy tắc:
- Dùng **động từ** mô tả kết quả hành động
- Ngắn gọn: 1–3 từ
- Cho hành động rủi ro: nhấn mạnh hậu quả

| Hành động | Label chuẩn | Tránh |
|---|---|---|
| Tạo mới | "Thêm Creator" | "Thêm mới" (thiếu context) |
| Lưu | "Lưu" | "Gửi" (trừ khi thật sự gửi đi) |
| Huỷ | "Huỷ" | "Đóng" (trừ khi chỉ đóng) |
| Xoá | "Xoá" | "OK" (trong confirm delete) |
| Duyệt | "Duyệt" hoặc "Approve" | "Xác nhận" (quá chung) |
| Từ chối | "Từ chối" | "Reject" (trừ khi app tiếng Anh) |
| Xuất file | "Xuất CSV" | "Export" |

### Confirm dialog buttons — dùng từ cụ thể:
```jsx
// ✅ Đúng — nói rõ hành động
Modal.confirm({
  title: "Xoá creator này?",
  okText: "Xoá",           // Cùng từ với title
  cancelText: "Huỷ",
  okButtonProps: { danger: true },
});

// ❌ Sai — "OK" không rõ nghĩa
Modal.confirm({
  title: "Xoá creator này?",
  okText: "OK",
  cancelText: "Cancel",
});
```

---

## 7. BUTTON STATES

| State | Mô tả | Khi nào |
|---|---|---|
| **Default** | Bình thường | |
| **Hover** | Đổi màu nhẹ | Mouse hover |
| **Active/Pressed** | Đậm hơn | Đang click |
| **Loading** | Icon xoay + disabled | Đang submit |
| **Disabled** | Mờ, không click được | Chưa đủ điều kiện |

```jsx
<Button type="primary" loading={submitting} disabled={!isValid}>
  Lưu
</Button>
```

### Disabled button — luôn có lý do:
```jsx
// ✅ Dùng Tooltip giải thích tại sao disabled
<Tooltip title="Vui lòng điền đầy đủ form trước khi lưu">
  <Button type="primary" disabled>Lưu</Button>
</Tooltip>
```
