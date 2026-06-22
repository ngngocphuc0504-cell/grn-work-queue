# Component Mapping — Legacy Custom/BaseUI → Ant Design 6 Core

Tài liệu này chỉ dùng cho **migration legacy**. Foundation mặc định của bộ skill vẫn là **Pure AntD**.

---

## Policy note

- Foundation mặc định là Ant Design 6.
- `ProTable`, `ProForm`, `ProDescriptions`, `ModalForm`, `DrawerForm`, và `StepsForm` được phép dùng nếu chúng giảm custom scaffolding rõ ràng.
- Không dùng Pro Components như blanket replacement cho mọi page đơn giản.

## 1. Migration Principles

1. Không tạo custom component mới nếu AntD core đã giải quyết được
2. Ưu tiên thay thế theo page impact:
   - Table + filter
   - Form + validation
   - Modal / Drawer
   - Layout shell
3. Sau migration, pattern mới phải bám `DESIGN.md` và `LAYOUT-BLUEPRINT.md`

---

## 2. Buttons

| Legacy | AntD core |
|---|---|
| `Btn` | `Button` |
| `Btn type="primary"` | `Button type="primary"` |
| `Btn danger` | `Button danger` |
| `Btn size="sm"` | `Button size="small"` |
| `Btn loading` | `Button loading` |
| `Btn block` | `Button block` |

---

## 3. Inputs & Field Wrappers

| Legacy | AntD core |
|---|---|
| `InputField` | `Input` |
| `TextArea` | `Input.TextArea` |
| `FieldInput error={msg}` | `Form.Item rules + Input` |
| custom number field | `InputNumber` |
| custom search input | `Input.Search` |

### Example
```jsx
// Trước
<FieldInput value={name} onChange={setName} error={error.name} />

// Sau
<Form.Item
  name="name"
  rules={[{ required: true, message: "Vui lòng nhập tên" }]}
>
  <Input />
</Form.Item>
```

---

## 4. Selects

| Legacy | AntD core |
|---|---|
| `SelectField` | `Select` |
| `SearchableSelect` | `Select showSearch` |
| custom multi-select | `Select mode="multiple"` |
| custom tags input | `Select mode="tags"` |
| `ProgramMultiSelect` | `Select mode="multiple"` + options |

### Rule
- Fixed list nhỏ: `Select`
- List lớn / async: `Select showSearch`
- Không dùng native `<select>` cho internal tool production

---

## 5. Date & Time

| Legacy | AntD core |
|---|---|
| custom date input | `DatePicker` |
| date range custom | `DatePicker.RangePicker` |
| month picker custom | `DatePicker picker="month"` |
| custom time input | `TimePicker` |

Lưu ý: AntD dùng `dayjs`.

---

## 6. Table & Filter

| Legacy | AntD core |
|---|---|
| `DataTable` | `Table` |
| `SmartFilter` | `Form` inline phía trên `Table` |
| custom pagination state | `Table pagination` |
| row action inline custom | `Space` + `Button` / `Popconfirm` |

### Example
```jsx
<Card>
  <Form layout="inline" onFinish={handleSearch}>
    <Form.Item name="keyword">
      <Input allowClear placeholder="Tìm kiếm..." />
    </Form.Item>
    <Form.Item name="status">
      <Select allowClear options={statusOptions} />
    </Form.Item>
    <Form.Item>
      <Button type="primary" htmlType="submit">Tìm</Button>
    </Form.Item>
  </Form>

  <Table
    rowKey="id"
    loading={loading}
    columns={columns}
    dataSource={data}
    pagination={{ current: page, pageSize: 20, total }}
  />
</Card>
```

---

## 7. Form & Validation

| Legacy | AntD core |
|---|---|
| `FormField` | `Form.Item` |
| manual field state | `Form.useForm()` |
| manual validation | `rules` |
| manual submit object build | `onFinish(values)` |

### Example
```jsx
<Form layout="vertical" onFinish={handleSubmit}>
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

  <Button type="primary" htmlType="submit">Lưu</Button>
</Form>
```

---

## 8. Modal / Drawer

| Legacy | AntD core |
|---|---|
| `Modal open title onClose` | `Modal open title onCancel` |
| custom side panel | `Drawer` |
| custom confirm popup | `Popconfirm` hoặc `Modal.confirm` |

### Rule
- Modal/Drawer chỉ có body scroll
- Footer dùng AntD `Button`
- Action nguy hiểm phải có confirm

---

## 9. Layout

| Legacy | AntD core |
|---|---|
| `AdminPageLayout` | `Layout` + `Sider` + `Header` + `Content` |
| custom breadcrumb | `Breadcrumb` |
| custom tabs shell | `Tabs` |
| dashboard grid custom | `Row` / `Col` / `Flex` |

---

## 10. Feedback & States

| Legacy | AntD core |
|---|---|
| `ToastProvider` / `useToast()` | `message` / `notification` |
| `EmptyState` | `Empty` |
| `LoadingSkeleton` | `Skeleton` |
| `ErrorBanner` | `Alert` |
| custom status pill | `Tag` hoặc `Badge` |

---

## 11. Icons

| Legacy | AntD core |
|---|---|
| inline icon wrappers | `@ant-design/icons` |
| custom svg icon | `Icon component={...}` |

---

## 12. Migration End State

Khi migration xong:
- Không còn `InputField`, `SelectField`, `SearchableSelect`, `BaseUI` là foundation mặc định
- Shared wrappers còn lại phải là business wrapper mỏng
- Visual language và state behavior phải bám `DESIGN.md`
