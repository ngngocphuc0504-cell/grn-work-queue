# Layout & Spacing — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/layout

---

## 1. DESIGN BOARD CHUẨN

Thống nhất kích thước design board trong team: **1440px** width.

Các độ phân giải cần hỗ trợ: 1920, 1440, 1366, 1280.

---

## 2. ADAPTATION (Responsive)

### Kiểu 1: Left-Right Layout (phổ biến nhất cho internal tool)
- Cố định sidebar (left navigation)
- Content area bên phải scale động theo màn hình

### Kiểu 2: Top-Bottom Layout
- Cố định margin hai bên (có min-width)
- Content area ở giữa scale động

---

## 3. GRID UNIT — Đơn vị cơ sở: 8px

Mọi kích thước spacing đều là **bội số của 8**.

Lý do: 8 là số chẵn, chia được cho 2 và 4, phù hợp hầu hết thiết bị hiển thị.

```
8, 16, 24, 32, 40, 48, 56, 64, 72, 80...
```

**Quy tắc:**
- Spacing giữa các element: luôn dùng bội số của 8
- Padding trong container: 16px hoặc 24px
- Gap giữa cards: 16px hoặc 24px
- Margin giữa sections: 16px hoặc 24px

---

## 4. RASTER — Hệ thống lưới 24 cột

Ant Design dùng **24-column grid** system.

Với layout 1440px top-bottom: content area 1168px chia thành 24 cột.

```jsx
import { Row, Col } from "antd";

// Gutter (khoảng cách giữa cột) cố định, column width scale động
<Row gutter={[16, 16]}>
  <Col span={6}>1/4</Col>
  <Col span={6}>1/4</Col>
  <Col span={6}>1/4</Col>
  <Col span={6}>1/4</Col>
</Row>
```

### Gutter values chuẩn:

| Gutter | Dùng cho |
|---|---|
| 8px | Compact layout (trong card, filter bar) |
| 16px | Default (cards, form items) |
| 24px | Loose (dashboard KPI cards, sections) |

### Responsive Grid:

```jsx
<Row gutter={[16, 16]}>
  <Col xs={24} sm={12} md={8} lg={6}>Card</Col>
</Row>
```

| Breakpoint | Columns hiển thị | Dùng cho |
|---|---|---|
| xs (< 576px) | 1 | Mobile |
| sm (≥ 576px) | 2 | Tablet nhỏ |
| md (≥ 768px) | 3 | Tablet |
| lg (≥ 992px) | 4 | Laptop |
| xl (≥ 1200px) | 4–6 | Desktop |
| xxl (≥ 1600px) | 6+ | Màn hình lớn |

---

## 5. SPACING TOKENS (Proximity)

### Vertical Spacing — 3 cấp:

| Cấp | Kích thước | Token | Dùng cho |
|---|---|---|---|
| **Small** | 8px | `marginXS` / `paddingXS` | Khoảng cách giữa elements liên quan chặt (icon + text, label + input) |
| **Middle** | 16px | `marginSM` / `paddingSM` | Khoảng cách giữa form items, list items |
| **Large** | 24px | `marginMD` / `paddingMD` | Khoảng cách giữa sections, cards |

### Công thức: `y = 8 + 8n` (n ≥ 0)

→ 8, 16, 24, 32, 40, 48...

### Các spacing token có sẵn trong antd v6:

| Token | Giá trị | Dùng cho |
|---|---|---|
| `marginXXS` | 4px | Micro spacing (icon margin) |
| `marginXS` | 8px | Small gap |
| `marginSM` | 12px | Compact gap |
| `margin` | 16px | Default gap |
| `marginMD` | 20px | Medium gap |
| `marginLG` | 24px | Large gap |
| `marginXL` | 32px | Extra large gap |
| `marginXXL` | 48px | Section gap |
| `paddingXXS` | 4px | Micro padding |
| `paddingXS` | 8px | Small padding |
| `paddingSM` | 12px | Compact padding |
| `padding` | 16px | Default padding |
| `paddingMD` | 20px | Medium padding |
| `paddingLG` | 24px | Large padding (card) |
| `paddingXL` | 32px | Extra large padding |

---

## 6. LAYOUT PATTERNS CHO INTERNAL TOOL

### Standard Admin Layout:

```
┌──────────────────────────────────────────────┐
│ Header (64px height)                          │
├────────┬─────────────────────────────────────┤
│        │                                      │
│ Sider  │  Content                             │
│ 200px  │  padding: 24px                       │
│ (fixed)│  background: colorBgLayout (#f5f5f5) │
│        │                                      │
└────────┴─────────────────────────────────────┘
```

```jsx
<Layout style={{ minHeight: "100vh" }}>
  <Layout.Sider width={200} />
  <Layout>
    <Layout.Header style={{ height: 64, padding: "0 24px" }} />
    <Layout.Content style={{ margin: 24, padding: 24, background: "#fff" }}>
      {children}
    </Layout.Content>
  </Layout>
</Layout>
```

### Spacing giữa elements trong trang:

```
Card padding:           24px (paddingLG)
Card → Card gap:        16px (margin)
Filter bar → Table:     16px
Toolbar → Table:        16px
Section → Section:      24px (marginLG)
Form.Item vertical gap: 24px (mặc định antd)
Button gap (Space):     8px (default Space size)
```

---

## 7. COMMON SCALES (Tỉ lệ thường dùng)

Ant Design đề xuất 2 bộ số bội-8 dùng cho layout:

**Bộ 1 (nhỏ):** `8, 16, 24, 32, 40, 48`
**Bộ 2 (lớn):** `48, 64, 80, 96, 112, 128`

Dùng khi cần quyết định width/height cho element:
- Sidebar: 200px hoặc 256px
- Header: 48px hoặc 64px
- Card min-height: 80px, 96px
- Modal width: 416px (confirm), 520px (default), 720px (large), 1000px (extra large)

---

## 8. QUY TẮC GIAO TIẾP DESIGNER ↔ DEVELOPER

1. **Xác định rõ vùng layout động** — vùng nào scale, vùng nào cố định
2. **Luôn dùng số chẵn** — padding, margin, width, height
3. **Giao các số quan trọng** — Gutter value, Column count
4. **Dùng cột bắt đầu và cột kết thúc** để xác định block — thay vì width pixel
