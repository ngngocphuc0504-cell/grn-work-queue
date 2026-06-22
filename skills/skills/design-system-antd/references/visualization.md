# Visualization & Charts — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/visual
> Library: recharts (project dùng), AntV ecosystem (tham khảo)

---

## 1. NGUYÊN TẮC THIẾT KẾ CHART

### 4 nguyên tắc:

| Nguyên tắc | Mô tả |
|---|---|
| **Accuracy** | Không bóp méo, gây hiểu lầm, hoặc bỏ sót data |
| **Effective** | Truyền tải tập trung, không dư thừa, đúng Data-ink Ratio |
| **Clarity** | Rõ ràng, dễ đọc, dễ tổ chức — giúp user đạt mục tiêu nhanh |
| **Aesthetics** | Biểu đạt hoàn hảo data, dùng visual element hợp lý, không trang trí thừa |

---

## 2. CHỌN ĐÚNG LOẠI CHART

### Theo mục đích:

| Mục đích | Chart phù hợp | Ví dụ use case |
|---|---|---|
| **Time series** (xu hướng theo thời gian) | Line Chart, Area Chart | Creator growth qua tháng, revenue trend |
| **Comparison** (so sánh) | Bar Chart, Column Chart, Bubble Chart | So sánh followers giữa game, revenue per region |
| **Distribution** (phân bố) | Scatter Plot, Box Plot | Phân bố followers, phân bố age |
| **Process** (quy trình) | Funnel Chart | Conversion funnel: view → click → register |
| **Proportion** (tỷ lệ) | Pie Chart, Donut Chart, Stacked Bar | Game distribution, status breakdown |

### Khi nào dùng chart nào (quick reference):

```
Muốn thấy XU HƯỚNG?        → Line Chart
Muốn SO SÁNH giá trị?      → Bar Chart (horizontal) hoặc Column Chart (vertical)
Muốn thấy TỶ LỆ?          → Donut Chart (< 6 categories) hoặc Stacked Bar
Muốn thấy PHÂN BỐ?         → Scatter Plot
Muốn thấy QUY TRÌNH?       → Funnel Chart
Muốn thấy MỐI QUAN HỆ?    → Scatter Plot hoặc Bubble Chart
Chỉ 1 số KPI?              → Statistic component (không cần chart)
```

---

## 3. THÀNH PHẦN CỦA CHART

### Title & Notes:
- **Title** nêu chủ đề chart — ngắn gọn, mô tả data
- **Notes** ghi nguồn data — tạo tin cậy

```jsx
<Card title="Creator Growth (Tháng 1–12/2026)" extra={<span style={{ color: "rgba(0,0,0,0.45)", fontSize: 12 }}>Nguồn: Database nội bộ</span>}>
  <LineChart ... />
</Card>
```

### Axis (Trục):
- **X axis**: Thường là thời gian hoặc category
- **Y axis**: Thường là giá trị
- Label trục rõ ràng, có đơn vị

### Legend (Chú giải):
- Hiển thị ý nghĩa các visual element
- Đặt phía trên hoặc bên phải chart
- Cho phép click legend để show/hide series

### Labels (Nhãn):
- Chú thích giá trị trên data point
- Không hiện tất cả label nếu data dense — chỉ hiện khi hover

### Tooltip:
- Hiện khi hover lên data point
- Hiển thị: giá trị, đơn vị, so sánh (nếu có)

---

## 4. MÀU SẮC CHO CHART

### Default color palette (AntV):
Ant Design đề xuất bộ màu chart default, đảm bảo phân biệt rõ giữa các series.

### Quy tắc màu:
- **Categorical data**: Dùng màu khác nhau cho mỗi category
- **Sequential data**: Dùng gradient cùng hue (ví dụ: blue-1 → blue-9)
- **Diverging data**: Dùng 2 hue đối lập (ví dụ: red → blue)
- **Trend indicators**: Green = tăng, Red = giảm

```jsx
// Màu cho recharts (project dùng)
const CHART_COLORS = [
  "#1677ff",  // blue (primary)
  "#52c41a",  // green
  "#faad14",  // gold
  "#ff4d4f",  // red
  "#722ed1",  // purple
  "#13c2c2",  // cyan
  "#fa541c",  // volcano
  "#eb2f96",  // magenta
];

// Trend colors
const TREND_UP = "#52c41a";    // green
const TREND_DOWN = "#ff4d4f";  // red
const TREND_FLAT = "rgba(0,0,0,0.45)";
```

---

## 5. CHART RESPONSIVE

### Nguyên tắc:
- Chart phải responsive theo container width
- Khi container nhỏ: ẩn bớt label, giảm data points, đơn giản hoá
- Axis label có thể xoay khi không đủ chỗ

```jsx
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, Legend } from "recharts";

// Luôn wrap trong ResponsiveContainer
<ResponsiveContainer width="100%" height={300}>
  <LineChart data={data}>
    <XAxis dataKey="month" />
    <YAxis />
    <Tooltip />
    <Legend />
    <Line type="monotone" dataKey="creators" stroke="#1677ff" />
    <Line type="monotone" dataKey="missions" stroke="#52c41a" />
  </LineChart>
</ResponsiveContainer>
```

---

## 6. CHART INTERACTION

### 3 cấp độ tương tác:

| Cấp | Mục đích | Ví dụ |
|---|---|---|
| **Data Acquisition** (Lấy data) | Tổng quan, nhìn nhanh | Hover tooltip, pan/zoom |
| **Information Processing** (Xử lý) | Filter, focus | Click legend to toggle, brush select |
| **Knowledge Flow** (Đào sâu) | Phân tích chi tiết | Click data point → navigate to detail |

Phương châm: **"Tổng quan trước → Focus filter → Chi tiết khi cần"**

---

## 7. DASHBOARD CHART PATTERNS

### KPI Card + Mini Chart:
```jsx
<Card>
  <Statistic title="Tổng Creator" value={1234} />
  <ResponsiveContainer width="100%" height={60}>
    <AreaChart data={sparklineData}>
      <Area type="monotone" dataKey="value" stroke="#1677ff" fill="#e6f4ff" />
    </AreaChart>
  </ResponsiveContainer>
</Card>
```

### Layout chuẩn:
```
Row 1: KPI Cards (4 columns)
Row 2: Main Chart (16 col) + Side Chart (8 col)
Row 3: Table (recent data)
```

```jsx
<Row gutter={[16, 16]}>
  {/* KPI Cards */}
  <Col xs={24} sm={12} lg={6}><KPICard /></Col>
  <Col xs={24} sm={12} lg={6}><KPICard /></Col>
  <Col xs={24} sm={12} lg={6}><KPICard /></Col>
  <Col xs={24} sm={12} lg={6}><KPICard /></Col>
</Row>
<Row gutter={[16, 16]} style={{ marginTop: 16 }}>
  {/* Charts */}
  <Col xs={24} lg={16}>
    <Card title="Trend"><LineChart /></Card>
  </Col>
  <Col xs={24} lg={8}>
    <Card title="Distribution"><PieChart /></Card>
  </Col>
</Row>
```

---

## 8. QUY TẮC CHO INTERNAL TOOL

1. **Dùng recharts** (project tech stack) — không mix library
2. **Luôn wrap `ResponsiveContainer`** — chart phải responsive
3. **Chart trong Card** — có title mô tả, ghi nguồn nếu cần
4. **Tooltip là bắt buộc** — user cần xem giá trị chính xác khi hover
5. **Legend cho multi-series** — dễ phân biệt
6. **Không quá 6 series** trên 1 chart — quá nhiều gây rối
7. **Pie/Donut chart**: tối đa 5–6 categories, gộp còn lại vào "Khác"
8. **Y axis bắt đầu từ 0** (trừ khi có lý do rõ ràng) — tránh misleading
9. **Loading state cho chart** — Skeleton hoặc Spin trong khi fetch data
