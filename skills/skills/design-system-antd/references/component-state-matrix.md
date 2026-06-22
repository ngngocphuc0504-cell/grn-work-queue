# Component State Matrix

Matrix này giúp agent giữ state behavior nhất quán giữa nhiều project.

---

## 1. Buttons

| State | Treatment |
|---|---|
| Default | Theo token mặc định |
| Hover | Tăng nổi bật vừa đủ, không quá “glow” |
| Active | Nhấn rõ nhưng ngắn |
| Loading | Khóa action lặp, spinner rõ |
| Disabled | Mờ, không click; giải thích bằng tooltip nếu cần |

## 2. Input / TextArea

| State | Treatment |
|---|---|
| Default | Border chuẩn, background container |
| Focus | Focus ring rõ, không chỉ đổi màu border nhẹ |
| Error | Dùng state error của `Form.Item` |
| Disabled | Mờ hơn nhưng vẫn đọc được |
| Read-only | Nền fill nhẹ, không giả disabled nếu vẫn cần đọc |

## 3. Select

| State | Treatment |
|---|---|
| Default | Như input |
| Focus / open | Có focus/active feedback rõ |
| Searchable | Chỉ dùng khi list lớn hoặc async |
| Multi-select | Tag/pill không được quá ồn |
| Disabled | Theo disabled pattern chung |

## 4. Table

| State | Treatment |
|---|---|
| Loading | `loading` prop hoặc wrapper rõ |
| Empty | `locale.emptyText` hoặc `Empty` |
| Hover row | Nhẹ, không làm row “nhảy” |
| Selected row | Highlight rõ nhưng không quá nặng |
| Sort active | Có visual cue rõ |

## 5. Tabs

| State | Treatment |
|---|---|
| Default | Chỉ 1 kiểu tab cho cùng context |
| Active | Dễ nhận biết, giữ hierarchy |
| Hover | Nhẹ |
| Disabled | Hiếm dùng; nếu có phải có lý do |

## 6. Modal / Drawer

| State | Treatment |
|---|---|
| Open | Focus rõ vào overlay |
| Busy submit | Footer button loading |
| Overflow content | Chỉ body scroll |
| Destructive confirm | Footer label cụ thể, không dùng “OK” chung chung |

## 7. Tag / Badge

| State | Treatment |
|---|---|
| Informational | Màu nhẹ, không giành primary attention |
| Success / warning / error | Theo semantic tokens |
| Count badge | Ngắn gọn, không dùng badge như paragraph |

## 8. Navigation

| State | Treatment |
|---|---|
| Active item | Rõ user đang ở đâu |
| Hover item | Gợi ý click, không lấn active |
| Open submenu | Hierarchy rõ |
| Collapsed shell | Label vẫn recoverable qua tooltip hoặc context |
