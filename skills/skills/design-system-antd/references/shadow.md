# Shadow & Elevation — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/shadow

---

## 1. NGUYÊN TẮC

Shadow mô phỏng khoảng cách giữa các layer, giúp user hiểu phân cấp UI.
Nguồn sáng hướng từ trên xuống → shadow chủ yếu đổ xuống dưới.

---

## 2. HỆ THỐNG 4 TẦNG (Elevation Levels)

| Level | Mô tả | Ví dụ component | Shadow |
|---|---|---|---|
| **Layer 0** | Trên nền, không nổi | Input, Table cell | Không có shadow |
| **Layer 1** | Nổi nhẹ (hover/float) | Card hover, Popover | Shadow nhẹ |
| **Layer 2** | Nổi trung bình (mở rộng) | Dropdown, Select panel, DatePicker panel | Shadow trung bình |
| **Layer 3** | Nổi cao (di chuyển độc lập) | Modal, Dialog, Drawer | Shadow đậm |

---

## 3. SHADOW TOKENS

### Ant Design 6 tokens:

```jsx
<ConfigProvider theme={{
  token: {
    // Shadow mặc định
    boxShadow: '0 1px 2px 0 rgba(0, 0, 0, 0.03), 0 1px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px 0 rgba(0, 0, 0, 0.02)',

    // Shadow cho card
    boxShadowCard: '0 1px 2px -2px rgba(0, 0, 0, 0.16), 0 3px 6px 0 rgba(0, 0, 0, 0.12), 0 5px 12px 4px rgba(0, 0, 0, 0.09)',

    // Shadow cho dropdown/popup
    boxShadowSecondary: '0 6px 16px 0 rgba(0, 0, 0, 0.08), 0 3px 6px -4px rgba(0, 0, 0, 0.12), 0 9px 28px 8px rgba(0, 0, 0, 0.05)',

    // Shadow cho drawer/modal
    boxShadowDrawerRight: '6px 0 16px 0 rgba(0, 0, 0, 0.08), 3px 0 6px -4px rgba(0, 0, 0, 0.12), 9px 0 28px 8px rgba(0, 0, 0, 0.05)',
    boxShadowDrawerLeft: '-6px 0 16px 0 rgba(0, 0, 0, 0.08), -3px 0 6px -4px rgba(0, 0, 0, 0.12), -9px 0 28px 8px rgba(0, 0, 0, 0.05)',
    boxShadowDrawerUp: '0 -6px 16px 0 rgba(0, 0, 0, 0.08), 0 -3px 6px -4px rgba(0, 0, 0, 0.12), 0 -9px 28px 8px rgba(0, 0, 0, 0.05)',
    boxShadowDrawerDown: '0 6px 16px 0 rgba(0, 0, 0, 0.08), 0 3px 6px -4px rgba(0, 0, 0, 0.12), 0 9px 28px 8px rgba(0, 0, 0, 0.05)',
  },
}}>
```

### Kỹ thuật 3-layer shadow:

Ant Design dùng **3 lớp shadow** chồng nhau để tạo hiệu ứng mềm mại, tự nhiên:
```css
box-shadow:
  /* Layer 1: tight, dark */ 0 1px 2px -2px rgba(0,0,0,0.16),
  /* Layer 2: medium */      0 3px 6px 0 rgba(0,0,0,0.12),
  /* Layer 3: wide, light */  0 5px 12px 4px rgba(0,0,0,0.09);
```

---

## 4. HƯỚNG SHADOW THEO CONTEXT

| Hướng | Dùng cho |
|---|---|
| **Xuống dưới** (phổ biến nhất) | Component bên trong page, dropdown, popover |
| **Lên trên** | Bottom navigation, bottom toolbar |
| **Sang trái** | Right sidebar, right drawer, fixed table column (right) |
| **Sang phải** | Left sidebar, left drawer, fixed table column (left) |

---

## 5. QUY TẮC CHO INTERNAL TOOL

1. **KHÔNG tự viết shadow** — dùng token của antd hoặc để component tự xử lý
2. **Card default** — không cần shadow nếu có border. Chỉ thêm shadow khi hover hoặc elevated state
3. **Modal, Drawer** — antd tự có shadow, không cần thêm
4. **Table fixed column** — antd tự thêm shadow cho scroll indicator
5. **Popover, Dropdown** — antd tự xử lý shadow

### Card hover shadow (nếu cần):

```jsx
const cardStyle = {
  transition: "box-shadow 0.3s",
  cursor: "pointer",
};

// Hover state (dùng CSS hoặc onMouseEnter)
const hoverShadow = "0 1px 2px -2px rgba(0,0,0,0.16), 0 3px 6px 0 rgba(0,0,0,0.12), 0 5px 12px 4px rgba(0,0,0,0.09)";
```
