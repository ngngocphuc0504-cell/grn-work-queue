# Motion & Animation — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/motion

---

## 1. GIÁ TRỊ CỦA ANIMATION

- **Tương tác mượt mà** — làm interaction tự nhiên hơn
- **Tạo sống động** — thu hút chú ý, tăng động lực tương tác
- **Định nghĩa phân cấp** — thể hiện quan hệ cha-con, thứ bậc trực quan
- **Cung cấp phản hồi** — tăng cường trải nghiệm qua feedback chuyển động

---

## 2. ĐÁNH GIÁ ANIMATION HIỆU QUẢ

| Tiêu chí | Câu hỏi |
|---|---|
| **Justified** | Animation này có cần thiết không? Có giúp user hiểu thông tin không? |
| **Performant** | Có bị giật, mất frame không? Có ảnh hưởng performance tổng thể không? |

→ Animation thừa = animation xấu. Animation gây lag = animation xấu.

---

## 3. BA NGUYÊN TẮC ANIMATION

### Natural (Tự nhiên)
- Animation dựa trên quy luật vật lý — mượt mà, trực giác
- Ví dụ: Button khi nhấn giống lá trên mặt nước — nhấn xuống rồi nảy lên, tạo gợn sóng

### Performant (Hiệu quả)
- Transition time ngắn nhất có thể
- **Disappearing animation nhanh hơn appearing** — không cần thu hút chú ý khi biến mất
- List items biến mất đồng thời, không stagger từng item

### Concise (Súc tích)
- Animation phải có ý nghĩa, không phô trương
- Tránh animation phức tạp, rườm rà — gây khó chịu cho user
- Ví dụ: Mở menu → focus vào nội dung menu, icon mũi tên chỉ xoay nhẹ, không cần drama

---

## 4. TRANSITION TIMES CHUẨN

| Loại | Duration | Dùng cho |
|---|---|---|
| **Micro** | 100–200ms | Button hover, focus ring, icon change |
| **Small** | 200–300ms | Dropdown open, tooltip show, collapse |
| **Medium** | 300–400ms | Modal open, drawer slide, page transition |
| **Slow** | 400–500ms | Complex animation (hiếm dùng) |

### Easing functions:

| Easing | CSS | Dùng cho |
|---|---|---|
| **Ease-out** | `cubic-bezier(0.215, 0.61, 0.355, 1)` | Appearing (phần tử xuất hiện) |
| **Ease-in** | `cubic-bezier(0.55, 0.055, 0.675, 0.19)` | Disappearing (phần tử biến mất) |
| **Ease-in-out** | `cubic-bezier(0.645, 0.045, 0.355, 1)` | Moving (phần tử di chuyển) |

---

## 5. ANTD BUILT-IN TRANSITIONS

Ant Design 6 components đã có transitions mặc định. **KHÔNG cần tự viết trừ khi custom.**

### Các transition có sẵn:

| Component | Transition | Duration |
|---|---|---|
| `Modal` | Zoom in/out + fade | 300ms |
| `Drawer` | Slide in/out | 300ms |
| `Dropdown` | Slide down + fade | 200ms |
| `Popover` / `Tooltip` | Fade + scale | 200ms |
| `Collapse` | Height collapse | 300ms |
| `Tabs` | Content slide | 300ms |
| `message` | Slide down + fade | 200ms |
| `notification` | Slide in from right | 300ms |
| `Switch` | Toggle slide | 200ms |
| `Button` | Background color + scale | 100ms |

---

## 6. QUY TẮC CHO INTERNAL TOOL

### KHÔNG làm:
- ❌ Tự viết complex animation (page transition, parallax, bouncing)
- ❌ Stagger animation cho list items (load từng item một)
- ❌ Loading spinner có animation phức tạp
- ❌ Auto-play carousel nhanh
- ❌ Disable animation mặc định của antd

### NÊN làm:
- ✅ Dùng antd transition mặc định (đã được tối ưu)
- ✅ `transition: all 0.3s` cho hover effects custom
- ✅ Highlight row mới thêm vào table (brief background flash)
- ✅ Smooth scroll khi navigate trong trang dài
- ✅ Loading skeleton thay vì spinner khi load page

### Highlight new item:

```jsx
// Highlight row mới tạo trong table
const [highlightId, setHighlightId] = useState(null);

// Sau khi tạo mới:
setHighlightId(newItem.id);
setTimeout(() => setHighlightId(null), 2000);

// Trong Table:
<Table
  rowClassName={(record) =>
    record.id === highlightId ? "row-highlight" : ""
  }
/>

// CSS:
// .row-highlight { animation: highlightFade 2s ease-out; }
// @keyframes highlightFade {
//   from { background-color: #e6f4ff; }
//   to { background-color: transparent; }
// }
```

---

## 7. REDUCED MOTION

Tôn trọng preference user không muốn animation:

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

Ant Design 6 đã hỗ trợ `prefers-reduced-motion` — hầu hết transitions sẽ tự giảm.
