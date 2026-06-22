# Typography — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/font

---

## 1. FONT FAMILY

Ant Design dùng system font stack — ưu tiên font hệ thống, hiển thị tốt trên mọi platform.

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
  'Helvetica Neue', Arial, 'Noto Sans', sans-serif,
  'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji';
```

**Quy tắc:**
- KHÔNG override font-family trừ khi brand yêu cầu
- Hiển thị số thẳng hàng: dùng `font-variant-numeric: tabular-nums` (quan trọng cho table số liệu)

---

## 2. BASE FONT SIZE

Ant Design 6 dùng **14px** làm base font size.

Lý do: Dựa trên khoảng cách đọc màn hình (50cm) và góc đọc tối ưu (0.3°), 14px cho trải nghiệm đọc tốt nhất trên đa số monitor.

```jsx
<ConfigProvider theme={{ token: { fontSize: 14 } }}>
```

---

## 3. FONT SCALE & LINE HEIGHT

10 cấp font size, lấy cảm hứng từ thang âm ngũ cung. Line height = fontSize + 8.

| Token / Cấp | Font Size | Line Height | Dùng cho |
|---|---|---|---|
| `fontSizeSM` | 12px | 20px | Caption, hint text, tag nhỏ |
| `fontSize` (base) | 14px | 22px | Body text, form label, table cell |
| `fontSizeLG` | 16px | 24px | Card title, section title nhỏ |
| `fontSizeXL` | 20px | 28px | Page title, modal title |
| `fontSizeHeading5` | 16px | 24px | Card/panel heading |
| `fontSizeHeading4` | 20px | 28px | Sub-section heading |
| `fontSizeHeading3` | 24px | 32px | Section heading |
| `fontSizeHeading2` | 30px | 38px | Major page heading |
| `fontSizeHeading1` | 38px | 46px | Hero heading (hiếm dùng) |

### Quy tắc Internal Tool:

- **Giới hạn 3–5 cấp font size** trong 1 trang
- Phổ biến nhất: 12px (caption) → 14px (body) → 16px (card title) → 20px (page title)
- KHÔNG dùng heading cấp 1–2 (38px, 30px) — quá to cho internal tool

---

## 4. FONT WEIGHT

Chỉ dùng **3 mức** — giữ nguyên tắc kiềm chế:

| Weight | Giá trị | Dùng khi |
|---|---|---|
| **Regular** | 400 | Body text, label, description — mặc định |
| **Medium** | 500 | Card title, table header, emphasis |
| **Semibold** | 600 | Chỉ cho tiếng Anh bold, hiếm dùng |

**Quy tắc:**
- KHÔNG dùng bold (700) cho body text tiếng Việt — khó đọc
- Medium (500) là đủ để nhấn mạnh heading và title

---

## 5. FONT COLOR

Xem chi tiết tại **colors.md** — phần Neutral Colors > Text.

| Vai trò | Token | Light | Dark |
|---|---|---|---|
| Heading / Body | `colorText` | `rgba(0,0,0,0.88)` | `rgba(255,255,255,0.85)` |
| Secondary | `colorTextSecondary` | `rgba(0,0,0,0.65)` | `rgba(255,255,255,0.65)` |
| Placeholder | `colorTextTertiary` | `rgba(0,0,0,0.45)` | `rgba(255,255,255,0.45)` |
| Disabled | `colorTextQuaternary` | `rgba(0,0,0,0.25)` | `rgba(255,255,255,0.25)` |

**WCAG:** Text chính contrast ≥ 7:1 (AAA). Text phụ 0.45 chỉ cho hint, KHÔNG cho nội dung quan trọng.

---

## 6. TYPOGRAPHY COMPONENT

```jsx
import { Typography } from "antd";
const { Title, Text, Paragraph, Link } = Typography;

// Title — 5 levels
<Title level={4}>Page Title</Title>     // 20px
<Title level={5}>Section Title</Title>  // 16px

// Text variants
<Text>Default</Text>
<Text type="secondary">Secondary</Text>
<Text type="success">Success</Text>
<Text type="warning">Warning</Text>
<Text type="danger">Danger</Text>
<Text strong>Bold</Text>

// Ellipsis
<Paragraph ellipsis={{ rows: 2, expandable: true }}>Long text...</Paragraph>

// Copyable
<Paragraph copyable>Copy me</Paragraph>
```

### Khi nào dùng Typography component:

| Tình huống | Dùng | Không dùng |
|---|---|---|
| Page title | `<Title level={4}>` | `<span style>` |
| Description | `<Text type="secondary">` | `<span style={{ color }}>` |
| Long text ellipsis | `<Paragraph ellipsis>` | CSS tự viết |
| Text cần copy | `<Paragraph copyable>` | Custom copy button |

---

## 7. TEMPLATE TYPOGRAPHY CHO INTERNAL TOOL

```
Page Title:     20px / medium (500) / colorText
Section Title:  16px / medium (500) / colorText
Card Title:     16px / medium (500) / colorText
Body Text:      14px / regular (400) / colorText
Table Cell:     14px / regular (400) / colorText
Table Header:   14px / medium (500) / colorText
Label:          14px / regular (400) / colorText
Caption/Hint:   12px / regular (400) / colorTextSecondary
Tag Text:       12px / regular (400)
Disabled:       14px / regular (400) / colorTextTertiary
```
