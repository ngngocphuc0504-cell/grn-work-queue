# Hệ thống màu sắc — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/colors
> Package: `@ant-design/colors`

---

## 1. NGUYÊN TẮC CHUNG

- **KHÔNG hardcode màu** — luôn dùng design token của antd hoặc tham chiếu palette chuẩn
- Mỗi palette có **10 shade** (1 = nhạt nhất, 10 = đậm nhất), **shade 6 là màu chính (primary)**
- Dùng `ConfigProvider` theme token để override, không dùng inline style với hex trực tiếp
- Khi cần màu nhạt hơn/đậm hơn → dùng shade khác trong cùng palette, KHÔNG tự chỉnh opacity

---

## 2. BRAND COLOR (Primary)

Màu chính mặc định của Ant Design là **Blue-6: `#1677ff`**

```jsx
// Override qua ConfigProvider
<ConfigProvider theme={{ token: { colorPrimary: "#1677ff" } }}>
```

Các token tự động sinh từ colorPrimary:
- `colorPrimaryBg` — background nhạt (tương đương shade 1)
- `colorPrimaryBgHover` — hover background (shade 2)
- `colorPrimaryBorder` — border (shade 3)
- `colorPrimaryBorderHover` — hover border (shade 4)
- `colorPrimaryHover` — hover state (shade 5)
- `colorPrimary` — primary (shade 6)
- `colorPrimaryActive` — active/pressed (shade 7)
- `colorPrimaryTextHover` — text hover (shade 8)
- `colorPrimaryText` — text (shade 9)
- `colorPrimaryTextActive` — text active (shade 10)

---

## 3. FUNCTIONAL COLORS (Màu chức năng)

Dùng để biểu thị trạng thái, thông báo, kết quả.

| Chức năng | Token | Hex (shade 6) | Dùng khi |
|---|---|---|---|
| **Success** | `colorSuccess` | `#52c41a` (green-6) | Thành công, hoàn thành, active, online |
| **Warning** | `colorWarning` | `#faad14` (gold-6) | Cảnh báo, chờ xử lý, pending |
| **Error** | `colorError` | `#ff4d4f` (red-5) | Lỗi, thất bại, xoá, nguy hiểm |
| **Info** | `colorInfo` | `#1677ff` (blue-6) | Thông tin, gợi ý, link |

Mỗi functional color cũng có bộ token tương tự primary:
- `colorSuccessBg`, `colorSuccessBorder`, `colorSuccessHover`, `colorSuccessActive`...
- `colorWarningBg`, `colorWarningBorder`, `colorWarningHover`, `colorWarningActive`...
- `colorErrorBg`, `colorErrorBorder`, `colorErrorHover`, `colorErrorActive`...
- `colorInfoBg`, `colorInfoBorder`, `colorInfoHover`, `colorInfoActive`...

### Mapping với component

```jsx
// Alert
<Alert type="success" />  // → colorSuccess
<Alert type="warning" />  // → colorWarning
<Alert type="error" />    // → colorError
<Alert type="info" />     // → colorInfo

// Tag — dùng preset name
<Tag color="success">Đã duyệt</Tag>
<Tag color="warning">Chờ duyệt</Tag>
<Tag color="error">Bị từ chối</Tag>

// Badge
<Badge status="success" />
<Badge status="warning" />
<Badge status="error" />

// Result
<Result status="success" />
<Result status="warning" />
<Result status="error" />
<Result status="info" />

// message / notification
message.success("Thành công");
message.warning("Cảnh báo");
message.error("Lỗi");
message.info("Thông tin");
```

---

## 4. NEUTRAL COLORS (Màu trung tính)

Dùng cho text, icon, border, background, divider. Ant Design dùng **rgba black** với các mức opacity.

### Text

| Token | Giá trị | Dùng cho |
|---|---|---|
| `colorText` | `rgba(0, 0, 0, 0.88)` | Text chính (title, body) |
| `colorTextSecondary` | `rgba(0, 0, 0, 0.65)` | Text phụ (description, caption) |
| `colorTextTertiary` | `rgba(0, 0, 0, 0.45)` | Text placeholder, disabled label |
| `colorTextQuaternary` | `rgba(0, 0, 0, 0.25)` | Text disabled |

### Border

| Token | Giá trị | Dùng cho |
|---|---|---|
| `colorBorder` | `#d9d9d9` | Border chính (input, card, table) |
| `colorBorderSecondary` | `#f0f0f0` | Border nhẹ (divider, split) |

### Background

| Token | Giá trị | Dùng cho |
|---|---|---|
| `colorBgContainer` | `#ffffff` | Nền container (card, modal, drawer) |
| `colorBgElevated` | `#ffffff` | Nền popup (dropdown, tooltip) |
| `colorBgLayout` | `#f5f5f5` | Nền layout (page background) |
| `colorBgSpotlight` | `rgba(0, 0, 0, 0.85)` | Nền tooltip text |
| `colorBgMask` | `rgba(0, 0, 0, 0.45)` | Overlay mask (modal backdrop) |

### Fill

| Token | Giá trị | Dùng cho |
|---|---|---|
| `colorFill` | `rgba(0, 0, 0, 0.15)` | Fill đậm nhất |
| `colorFillSecondary` | `rgba(0, 0, 0, 0.06)` | Fill trung bình |
| `colorFillTertiary` | `rgba(0, 0, 0, 0.04)` | Fill nhẹ (hover background) |
| `colorFillQuaternary` | `rgba(0, 0, 0, 0.02)` | Fill cực nhẹ |

### Icon & Divider

| Token | Giá trị | Dùng cho |
|---|---|---|
| `colorIcon` | `rgba(0, 0, 0, 0.45)` | Icon mặc định |
| `colorIconHover` | `rgba(0, 0, 0, 0.88)` | Icon hover |
| `colorSplit` | `rgba(5, 5, 5, 0.06)` | Divider, separator |

---

## 5. BASE COLOR PALETTES (12 bảng màu cơ sở)

Tổng cộng 120 màu = 12 palettes × 10 shades. **Shade 6 = màu chính** của mỗi palette.

### Red (Đỏ) — Lỗi, nguy hiểm, xoá
| Shade | Hex |
|---|---|
| red-1 | `#fff1f0` |
| red-2 | `#ffccc7` |
| red-3 | `#ffa39e` |
| red-4 | `#ff7875` |
| red-5 | `#ff4d4f` ← colorError |
| red-6 | `#f5222d` |
| red-7 | `#cf1322` |
| red-8 | `#a8071a` |
| red-9 | `#820014` |
| red-10 | `#5c0011` |

### Volcano (Cam đỏ)
| Shade | Hex |
|---|---|
| volcano-1 | `#fff2e8` |
| volcano-2 | `#ffd8bf` |
| volcano-3 | `#ffbb96` |
| volcano-4 | `#ff9c6e` |
| volcano-5 | `#ff7a45` |
| volcano-6 | `#fa541c` |
| volcano-7 | `#d4380d` |
| volcano-8 | `#ad2102` |
| volcano-9 | `#871400` |
| volcano-10 | `#610b00` |

### Orange (Cam)
| Shade | Hex |
|---|---|
| orange-1 | `#fff7e6` |
| orange-2 | `#ffe7ba` |
| orange-3 | `#ffd591` |
| orange-4 | `#ffc069` |
| orange-5 | `#ffa940` |
| orange-6 | `#fa8c16` |
| orange-7 | `#d46b08` |
| orange-8 | `#ad4e00` |
| orange-9 | `#873800` |
| orange-10 | `#612500` |

### Gold (Vàng đậm) — Warning
| Shade | Hex |
|---|---|
| gold-1 | `#fffbe6` |
| gold-2 | `#fff1b8` |
| gold-3 | `#ffe58f` |
| gold-4 | `#ffd666` |
| gold-5 | `#ffc53d` |
| gold-6 | `#faad14` ← colorWarning |
| gold-7 | `#d48806` |
| gold-8 | `#ad6800` |
| gold-9 | `#874d00` |
| gold-10 | `#613400` |

### Yellow (Vàng)
| Shade | Hex |
|---|---|
| yellow-1 | `#feffe6` |
| yellow-2 | `#ffffb8` |
| yellow-3 | `#fffb8f` |
| yellow-4 | `#fff566` |
| yellow-5 | `#ffec3d` |
| yellow-6 | `#fadb14` |
| yellow-7 | `#d4b106` |
| yellow-8 | `#ad8b00` |
| yellow-9 | `#876800` |
| yellow-10 | `#614700` |

### Lime (Xanh lá nhạt)
| Shade | Hex |
|---|---|
| lime-1 | `#fcffe6` |
| lime-2 | `#f4ffb8` |
| lime-3 | `#eaff8f` |
| lime-4 | `#d3f261` |
| lime-5 | `#bae637` |
| lime-6 | `#a0d911` |
| lime-7 | `#7cb305` |
| lime-8 | `#5b8c00` |
| lime-9 | `#3f6600` |
| lime-10 | `#254000` |

### Green (Xanh lá) — Success
| Shade | Hex |
|---|---|
| green-1 | `#f6ffed` |
| green-2 | `#d9f7be` |
| green-3 | `#b7eb8f` |
| green-4 | `#95de64` |
| green-5 | `#73d13d` |
| green-6 | `#52c41a` ← colorSuccess |
| green-7 | `#389e0d` |
| green-8 | `#237804` |
| green-9 | `#135200` |
| green-10 | `#092b00` |

### Cyan (Xanh ngọc)
| Shade | Hex |
|---|---|
| cyan-1 | `#e6fffb` |
| cyan-2 | `#b5f5ec` |
| cyan-3 | `#87e8de` |
| cyan-4 | `#5cdbd3` |
| cyan-5 | `#36cfc9` |
| cyan-6 | `#13c2c2` |
| cyan-7 | `#08979c` |
| cyan-8 | `#006d75` |
| cyan-9 | `#00474f` |
| cyan-10 | `#002329` |

### Blue (Xanh dương) — Primary, Info
| Shade | Hex |
|---|---|
| blue-1 | `#e6f4ff` |
| blue-2 | `#bae0ff` |
| blue-3 | `#91caff` |
| blue-4 | `#69b1ff` |
| blue-5 | `#4096ff` |
| blue-6 | `#1677ff` ← colorPrimary, colorInfo |
| blue-7 | `#0958d9` |
| blue-8 | `#003eb3` |
| blue-9 | `#002c8c` |
| blue-10 | `#001d66` |

### Geekblue (Xanh tím)
| Shade | Hex |
|---|---|
| geekblue-1 | `#f0f5ff` |
| geekblue-2 | `#d6e4ff` |
| geekblue-3 | `#adc6ff` |
| geekblue-4 | `#85a5ff` |
| geekblue-5 | `#597ef7` |
| geekblue-6 | `#2f54eb` |
| geekblue-7 | `#1d39c4` |
| geekblue-8 | `#10239e` |
| geekblue-9 | `#061178` |
| geekblue-10 | `#030852` |

### Purple (Tím)
| Shade | Hex |
|---|---|
| purple-1 | `#f9f0ff` |
| purple-2 | `#efdbff` |
| purple-3 | `#d3adf7` |
| purple-4 | `#b37feb` |
| purple-5 | `#9254de` |
| purple-6 | `#722ed1` |
| purple-7 | `#531dab` |
| purple-8 | `#391085` |
| purple-9 | `#22075e` |
| purple-10 | `#120338` |

### Magenta (Hồng cánh sen)
| Shade | Hex |
|---|---|
| magenta-1 | `#fff0f6` |
| magenta-2 | `#ffd6e7` |
| magenta-3 | `#ffadd2` |
| magenta-4 | `#ff85c0` |
| magenta-5 | `#f759ab` |
| magenta-6 | `#eb2f96` |
| magenta-7 | `#c41d7f` |
| magenta-8 | `#9e1068` |
| magenta-9 | `#780650` |
| magenta-10 | `#520339` |

---

## 6. QUY TẮC SỬ DỤNG MÀU TRONG INTERNAL TOOL

### Status Tag Colors

```jsx
// CHUẨN — dùng preset name, KHÔNG hardcode hex
const STATUS_COLORS = {
  // Trạng thái tích cực
  active: "green",
  approved: "green",
  published: "green",
  online: "green",
  completed: "green",

  // Trạng thái chờ
  pending: "gold",
  reviewing: "gold",
  processing: "orange",
  draft: "default",

  // Trạng thái tiêu cực
  rejected: "red",
  failed: "red",
  banned: "red",
  expired: "red",
  offline: "default",

  // Trạng thái thông tin
  new: "blue",
  in_progress: "blue",
  scheduled: "cyan",
  archived: "purple",
};

<Tag color={STATUS_COLORS[status]}>{label}</Tag>
```

### Background Highlights

```jsx
// Dùng shade 1 (nhạt nhất) cho row highlight, card tint
// Ví dụ: row có lỗi
style={{ background: "#fff1f0" }}  // red-1

// Ví dụ: card thành công
style={{ background: "#f6ffed" }}  // green-1

// Ví dụ: info highlight
style={{ background: "#e6f4ff" }}  // blue-1
```

### Text Colors theo ngữ cảnh

```jsx
// Text chính
style={{ color: "rgba(0, 0, 0, 0.88)" }}   // colorText

// Text phụ / mô tả
style={{ color: "rgba(0, 0, 0, 0.45)" }}   // colorTextTertiary

// Text link
style={{ color: "#1677ff" }}                // colorPrimary

// Text lỗi / nguy hiểm
style={{ color: "#ff4d4f" }}                // colorError

// Text thành công
style={{ color: "#52c41a" }}                // colorSuccess
```

### Trend Indicators (Dashboard)

```jsx
// Tăng — dùng green
<ArrowUpOutlined style={{ color: "#52c41a" }} />    // green-6
<Statistic valueStyle={{ color: "#52c41a" }} />

// Giảm — dùng red
<ArrowDownOutlined style={{ color: "#ff4d4f" }} />   // red-5
<Statistic valueStyle={{ color: "#ff4d4f" }} />

// Không đổi — dùng neutral
<span style={{ color: "rgba(0, 0, 0, 0.45)" }}>0%</span>
```

---

## 7. DARK MODE

Khi dùng `theme.darkAlgorithm`, Ant Design **tự động đảo ngược** các shade:
- Light mode: shade 1 = nhạt, shade 10 = đậm
- Dark mode: shade tự điều chỉnh để phù hợp nền tối

```jsx
import { ConfigProvider, theme } from "antd";

<ConfigProvider theme={{ algorithm: theme.darkAlgorithm }}>
  <App />
</ConfigProvider>
```

Neutral colors trong dark mode:
- `colorText` → `rgba(255, 255, 255, 0.85)`
- `colorTextSecondary` → `rgba(255, 255, 255, 0.65)`
- `colorTextTertiary` → `rgba(255, 255, 255, 0.45)`
- `colorBgContainer` → `#141414`
- `colorBgLayout` → `#000000`
- `colorBorder` → `#424242`

**Quy tắc**: Nếu dùng design token (không hardcode), dark mode sẽ tự hoạt động.

---

## 8. CONFIGPROVIDER — CÁCH OVERRIDE MÀU

```jsx
<ConfigProvider theme={{
  token: {
    // Brand
    colorPrimary: "#1677ff",

    // Functional
    colorSuccess: "#52c41a",
    colorWarning: "#faad14",
    colorError: "#ff4d4f",
    colorInfo: "#1677ff",

    // Neutral
    colorText: "rgba(0, 0, 0, 0.88)",
    colorTextSecondary: "rgba(0, 0, 0, 0.65)",
    colorBgContainer: "#ffffff",
    colorBgLayout: "#f5f5f5",
    colorBorder: "#d9d9d9",

    // Other
    borderRadius: 6,
    fontSize: 14,
  },
}}>
```

---

## 9. PLATFORM BRAND COLORS — NGOẠI LỆ DUY NHẤT

Platform social media có brand colors riêng (Facebook blue, YouTube red...). Đây là ngoại lệ duy nhất được phép dùng ngoài antd palette, vì giúp user nhận diện platform nhanh.

**Điều kiện bắt buộc:**
- Phải centralize trong 1 file config duy nhất (ví dụ: `tokens.js`, `platforms.js`)
- Mọi component hiển thị platform badge/tag phải import từ config, không hardcode
- Phần background nhạt: dùng `color + "18"` (opacity 10%) hoặc tạo bg từ config

```js