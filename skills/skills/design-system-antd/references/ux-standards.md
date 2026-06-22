# UX Standards cho Internal Tool — Ant Design 6 Core

Checklist và pattern chuẩn cho mọi trạng thái UX trong internal tool dùng Ant Design core.

---

## 1. Empty States

### Quy tắc
- Mọi vùng dữ liệu phải có empty state
- Empty state phải phân biệt:
  - chưa có data
  - search/filter không ra kết quả
  - không có quyền
  - lỗi tải data
- Nếu user có action tiếp theo hợp lệ, thêm CTA

### Table trống
```jsx
import { Empty, Button, Table } from "antd";

<Table
  locale={{
    emptyText: (
      <Empty
        image={Empty.PRESENTED_IMAGE_SIMPLE}
        description="Chưa có creator nào"
      >
        <Button type="primary">Thêm creator đầu tiên</Button>
      </Empty>
    ),
  }}
/>
```

### Search không có kết quả
```jsx
<Empty
  image={Empty.PRESENTED_IMAGE_SIMPLE}
  description={`Không tìm thấy kết quả cho "${searchTerm}"`}
/>
```

### Không có quyền
```jsx
import { Result, Button } from "antd";

<Result
  status="403"
  title="Không có quyền"
  subTitle="Bạn chưa được cấp quyền truy cập khu vực này."
  extra={<Button type="primary">Về trang chủ</Button>}
/>
```

---

## 2. Loading States

### Quy tắc chung
- <300ms: không cần hiện loading riêng
- 300ms–2s: `Spin`, `Button loading`, `Table loading`
- >2s: ưu tiên `Skeleton` hoặc hint text
- >10s: thêm progress hoặc messaging rõ hơn

### Page loading
```jsx
import { Spin } from "antd";

<Spin spinning={loading} tip="Đang tải dữ liệu...">
  <PageContent />
</Spin>
```

### Table loading
```jsx
<Table
  loading={loading}
  columns={columns}
  dataSource={data}
/>
```

### Submit loading
```jsx
<Button type="primary" loading={submitting} onClick={handleSave}>
  Lưu
</Button>
```

### Skeleton loading
```jsx
import { Card, Skeleton } from "antd";

<Card>
  <Skeleton loading={loading} active paragraph={{ rows: 3 }}>
    <ActualContent />
  </Skeleton>
</Card>
```

---

## 3. Error States

### Inline API error
```jsx
import { Alert, Button } from "antd";

{error && (
  <Alert
    type="error"
    showIcon
    message="Không tải được dữ liệu"
    description={error.message || "Vui lòng thử lại sau."}
    action={<Button size="small" onClick={retry}>Thử lại</Button>}
  />
)}
```

### Fatal error
```jsx
import { Result, Button, Space } from "antd";

<Result
  status="500"
  title="Có lỗi xảy ra"
  subTitle="Hệ thống gặp sự cố. Vui lòng thử lại sau."
  extra={
    <Space>
      <Button type="primary" onClick={retry}>Thử lại</Button>
      <Button>Về trang chủ</Button>
    </Space>
  }
/>
```

### Form validation
```jsx
import { Form, Input } from "antd";

<Form.Item
  name="email"
  label="Email"
  rules={[
    { required: true, message: "Vui lòng nhập email" },
    { type: "email", message: "Email không hợp lệ" },
  ]}
>
  <Input />
</Form.Item>
```

---

## 4. Confirmation Patterns

### Hành động thường nhưng rủi ro
```jsx
import { Button, Popconfirm, message } from "antd";

<Popconfirm
  title="Xoá creator này?"
  description="Hành động này không thể hoàn tác."
  okText="Xoá"
  cancelText="Huỷ"
  okButtonProps={{ danger: true }}
  onConfirm={async () => {
    await removeCreator(id);
    message.success("Đã xoá");
  }}
>
  <Button danger size="small">Xoá</Button>
</Popconfirm>
```

### Hành động lớn
```jsx
import { Modal, message } from "antd";

Modal.confirm({
  title: "Đăng mission cho toàn bộ creator?",
  content: "Hành động này sẽ gửi thông báo hàng loạt và không thể thu hồi.",
  okText: "Đăng ngay",
  cancelText: "Huỷ",
  onOk: async () => {
    await publishMission();
    message.success("Đã đăng mission");
  },
});
```

### Unsaved changes
- Dùng `beforeunload` khi user rời browser/tab
- Dùng route guard nếu project router hỗ trợ
- Chỉ hiện confirm khi thật sự có thay đổi chưa lưu

---

## 5. Notification Patterns

### Khi nào dùng gì

| Trường hợp | Dùng |
|---|---|
| Thành công / lỗi ngắn | `message` |
| Cần detail hoặc action | `notification` |
| Cảnh báo gắn với vùng nội dung | `Alert` |

### Message
```jsx
message.success("Đã lưu cấu hình");
message.error("Không thể lưu cấu hình");
```

### Notification
```jsx
notification.info({
  message: "Import hoàn tất",
  description: "124 bản ghi đã được thêm thành công.",
});
```

---

## 6. Table UX

### Bắt buộc cho table production
- `loading`
- `rowKey`
- empty state
- pagination khi data dài
- sort/filter nếu user cần scan/compare
- ellipsis cho text dài
- format số/ngày nhất quán

### Mặc định pagination
```jsx
pagination={{
  current: page,
  pageSize: 20,
  total,
  showSizeChanger: true,
  showTotal: (count) => `Tổng ${count} mục`,
}}
```

---

## 7. Form UX

### Quy tắc
- Label rõ nghĩa, ngắn gọn
- Chỉ thêm helper text khi thiếu nó sẽ gây mơ hồ
- Dùng `rules` để validation declarative
- Button submit phải có loading state
- Form dài phải chia group bằng `Tabs`, `Collapse` hoặc section cards

### Modal/Drawer form
- Header cố định
- Body là vùng duy nhất có scroll
- Footer cố định
- Input widths phải ổn định trong cùng một form

---

## 8. Responsive & Accessibility

### Responsive
- Internal tool vẫn ưu tiên desktop-first
- `Row` / `Col` hoặc `Flex` phải collapse hợp lý ở `xs` / `sm`
- Filter bar dài phải wrap, không đẩy ngang
- Table nhỏ màn hình: ưu tiên ẩn cột phụ hơn là nhồi chật

### Accessibility
- Focus state phải nhìn thấy rõ
- Icon-only button phải có `aria-label` hoặc `Tooltip`
- Không dùng màu là tín hiệu duy nhất cho status
- Placeholder không thay thế label

---

## 9. Checklist nhanh

- Có empty state đúng ngữ cảnh chưa?
- Có loading state cho fetch và submit chưa?
- Có error state inline và fatal chưa?
- Hành động nguy hiểm có confirm chưa?
- Toast/notification dùng đúng loại chưa?
- Table và form có đủ state production chưa?
- Responsive có wrap/collapse ổn chưa?
