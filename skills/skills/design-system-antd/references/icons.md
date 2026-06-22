# Icons — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/icon

---

## 1. NGUYÊN TẮC THIẾT KẾ ICON

- **Rõ ràng, trực quan, đơn giản** — icon dễ nhận diện hơn sẽ dễ hiểu hơn
- **Nhất quán style** — tất cả icon trong UI phải cùng style (chi tiết, góc nhìn, stroke weight)

---

## 2. PHÂN LOẠI ICON

### System Icons (Icon hệ thống)
Dùng cho thao tác phổ biến: save, edit, delete, search, close...

**Đặc điểm:**
- Kích thước nhỏ (14px–20px)
- Stroke weight thống nhất: 72px (trên grid 1024×1024)
- Góc bo: radius 72px
- Phong cách phẳng, không có chiều sâu

**Naming convention:**
- Icon outline: suffix `-outlined` (ví dụ: `DeleteOutlined`)
- Icon filled: suffix `-filled` (ví dụ: `DeleteFilled`)
- Icon two-tone: suffix `-twotone` (ví dụ: `DeleteTwoTone`)

### Business Icons (Icon nghiệp vụ)
Dùng cho trang giới thiệu, dashboard decorative, empty state...

**Đặc điểm:**
- Kích thước lớn hơn: 32px (min), 48px, 64px (max)
- Chi tiết phong phú hơn
- Có thể single-color (neutral) hoặc double-color (neutral + primary, primary ≤ 40%)

---

## 3. SIZING RULES

| Context | Icon Size | Spacing |
|---|---|---|
| Inline với text 12px | 12px | 8px gap |
| Inline với text 14px | 14px | 8px gap |
| Button icon | 14px–16px | Tự động (antd Button) |
| Table action | 14px | 8px gap |
| Menu item | 16px | 10px gap |
| Card header | 16px–20px | 8px gap |
| Empty state / decorative | 48px–64px | — |

---

## 4. COLOR RULES

- **Màu icon = màu text xung quanh** — mặc định
- **Trạng thái khác biệt** — dùng functional color:
  - Success: `colorSuccess` (#52c41a)
  - Warning: `colorWarning` (#faad14)
  - Error/Danger: `colorError` (#ff4d4f)
  - Info/Primary: `colorPrimary` (#1677ff)
- **Disabled icon**: `colorTextQuaternary` (rgba(0,0,0,0.25))

```jsx
// Màu theo context
<DeleteOutlined style={{ color: "#ff4d4f" }} />      // Danger action
<CheckCircleOutlined style={{ color: "#52c41a" }} />  // Success
<InfoCircleOutlined style={{ color: "#1677ff" }} />   // Info
```

---

## 5. SỬ DỤNG TRONG ANT DESIGN 6

### Import icons:
```jsx
import {
  SearchOutlined,
  PlusOutlined,
  DeleteOutlined,
  EditOutlined,
  EyeOutlined,
  DownloadOutlined,
  UploadOutlined,
  FilterOutlined,
  ReloadOutlined,
  SettingOutlined,
  ExportOutlined,
  CopyOutlined,
  CheckCircleOutlined,
  CloseCircleOutlined,
  ExclamationCircleOutlined,
  InfoCircleOutlined,
  ArrowUpOutlined,
  ArrowDownOutlined,
} from "@ant-design/icons";
```

### Icon phổ biến cho Internal Tool:

| Hành động | Icon | Component |
|---|---|---|
| Tìm kiếm | 🔍 | `SearchOutlined` |
| Thêm mới | + | `PlusOutlined` |
| Xoá | 🗑 | `DeleteOutlined` |
| Sửa | ✏️ | `EditOutlined` |
| Xem chi tiết | 👁 | `EyeOutlined` |
| Download/Export | ⬇ | `DownloadOutlined` / `ExportOutlined` |
| Upload | ⬆ | `UploadOutlined` |
| Filter | 🔽 | `FilterOutlined` |
| Refresh/Reload | 🔄 | `ReloadOutlined` |
| Settings | ⚙ | `SettingOutlined` |
| Copy | 📋 | `CopyOutlined` |
| Success | ✅ | `CheckCircleOutlined` |
| Error | ❌ | `CloseCircleOutlined` |
| Warning | ⚠ | `ExclamationCircleOutlined` |
| Info | ℹ | `InfoCircleOutlined` |
| Trend up | ↑ | `ArrowUpOutlined` |
| Trend down | ↓ | `ArrowDownOutlined` |

### Custom SVG Icon:
```jsx
import Icon from "@ant-design/icons";

const CustomSvg = () => (
  <svg viewBox="0 0 1024 1024" width="1em" height="1em" fill="currentColor">
    {/* SVG path */}
  </svg>
);

// Sử dụng
<Icon component={CustomSvg} />
<Button icon={<Icon component={CustomSvg} />}>Custom</Button>
```

### Icon-only Button — bắt buộc có aria-label:
```jsx
<Button icon={<DeleteOutlined />} aria-label="Xoá creator" />
<Tooltip title="Xoá creator">
  <Button icon={<DeleteOutlined />} />
</Tooltip>
```

---

## 6. BEST PRACTICES CHO INTERNAL TOOL

1. **Ưu tiên Outlined style** — nhẹ nhàng, phù hợp internal tool. Filled chỉ dùng khi cần nhấn mạnh
2. **Luôn kèm text** cho action quan trọng — icon-only chỉ cho action phổ biến (edit, delete) khi có tooltip
3. **Không dùng quá nhiều icon** trên cùng 1 row — gây rối mắt
4. **Consistent sizing** — cùng context thì cùng size icon
5. **KHÔNG dùng icon thay text** cho label — internal tool cần rõ ràng hơn consumer app
