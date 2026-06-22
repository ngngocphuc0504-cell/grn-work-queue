# Design Consistency — Checklist chi tiết

Dimension này đánh giá mức độ **đồng nhất** về visual design across toàn bộ dự án. Một dự án "đẹp" nhưng mỗi page một kiểu → score thấp. Một dự án "đơn giản" nhưng mọi thứ thống nhất → score cao.

---

## 1. Color System

### 1.1 Token Usage
- [ ] Tất cả colors được reference qua design tokens (T.colorX, C.xxx) — không hardcode hex/rgb
- [ ] Có token file tập trung (tokens.js, theme.js, variables.css)
- [ ] Semantic colors đúng intent: primary cho CTA, success cho positive, error cho negative, warning cho caution

**Cách check:** Grep `/#[0-9a-fA-F]{3,8}/` và `/rgb\(|rgba\(/` ngoài token file. Mỗi match = potential violation.

### 1.2 Color Consistency
- [ ] Cùng status (Active/Approved/Success) dùng cùng color across pages
- [ ] Cùng action type (primary, secondary, danger) dùng cùng color
- [ ] Background shading nhất quán (section bg, card bg, hover bg)
- [ ] Text colors nhất quán (primary text, secondary text, placeholder)

**Cách check:** Grep từng status keyword và check color gán cho nó. So sánh cross-file.

### 1.3 Platform/Brand Colors
- [ ] Nếu có platform colors (TikTok, YouTube, Facebook...) → dùng từ constants, không hardcode
- [ ] Chart colors dùng palette thống nhất

---

## 2. Typography

### 2.1 Font Size Scale
- [ ] Dùng design token font sizes (T.fontSize, T.fontSizeSM, T.fontSizeLG...)
- [ ] Không có font-size "lẻ" (13px, 15px, 17px) ngoài scale
- [ ] Heading hierarchy rõ ràng: page title > section title > card title > body text
- [ ] Cùng level heading dùng cùng size across pages

**Cách check:** Grep `fontSize:` và list unique values. Bao nhiêu giá trị ngoài token set?

### 2.2 Font Weight
- [ ] Weight dùng từ scale nhất quán (400 normal, 500 medium, 600 semibold, 700 bold)
- [ ] Không quá 3-4 weight variants trong toàn project
- [ ] Label/heading dùng weight nhất quán (tất cả section title cùng weight)

### 2.3 Line Height & Letter Spacing
- [ ] Line height theo token (T.lineHeight) hoặc consistent values
- [ ] Paragraph text đủ line height (≥ 1.5)
- [ ] Dense text (tables, lists) có thể dùng tighter (1.3-1.4) nhưng nhất quán

---

## 3. Spacing System

### 3.1 Token Usage
- [ ] Padding/margin dùng token values (T.padding, T.paddingSM, SP.xxx)
- [ ] Gap values từ spacing scale
- [ ] Không có magic numbers (padding: 7, margin: 13, gap: 11)

**Cách check:** Grep `padding:|margin:|gap:` → list unique values. So với token set.

### 3.2 Spacing Patterns
- [ ] Card padding nhất quán (tất cả cards cùng internal padding)
- [ ] Section spacing nhất quán (gap giữa sections cùng across pages)
- [ ] Form field spacing nhất quán (gap giữa label-input, giữa rows)
- [ ] Table cell padding nhất quán

**Cách check:** So sánh padding values trong Card components, Section components, Form components across files.

### 3.3 Grid/Layout Consistency
- [ ] Grid column count nhất quán (card grid 3-col ở mọi nơi, hoặc responsive pattern chung)
- [ ] Sidebar width cố định (nếu có)
- [ ] Max-width cho content areas nhất quán

---

## 4. Border & Shadow

### 4.1 Border
- [ ] Border radius dùng token (T.borderRadius, T.borderRadiusLG)
- [ ] Không mix sharp corners (0px) và rounded (8px) cho cùng loại element
- [ ] Border color từ token (T.colorBorder, T.colorBorderSecondary)
- [ ] Divider style nhất quán (solid vs dashed, color, thickness)

### 4.2 Shadow
- [ ] Shadow dùng token (T.boxShadow, T.boxShadowSecondary)
- [ ] Shadow hierarchy: card < dropdown < modal (depth tăng dần)
- [ ] Không có shadow "lạ" ngoài token set

---

## 5. Component Visual Patterns

### 5.1 Buttons
- [ ] Primary/Secondary/Danger buttons có visual style nhất quán across pages
- [ ] Button sizes nhất quán (không file A dùng size="small", file B dùng custom height)
- [ ] Icon button vs text button vs icon+text — pattern nhất quán

### 5.2 Cards
- [ ] Card style nhất quán (border, shadow, radius, padding, background)
- [ ] Card header pattern nhất quán (nếu có)
- [ ] Card hover effect nhất quán (nếu có)

### 5.3 Tables
- [ ] Header style nhất quán (background, font-weight, text-transform)
- [ ] Row hover style nhất quán
- [ ] Cell padding nhất quán
- [ ] Column width strategy nhất quán (fixed vs flex)

### 5.4 Modals/Drawers
- [ ] Header style nhất quán (font-size, font-weight, divider)
- [ ] Footer pattern nhất quán (button alignment, spacing)
- [ ] Width strategy nhất quán (fixed px, % of viewport, responsive)
- [ ] Overlay/backdrop style nhất quán

### 5.5 Tags/Badges/Pills
- [ ] Color mapping nhất quán (cùng status → cùng color/style)
- [ ] Size nhất quán (không mix large tags với tiny tags)
- [ ] Shape nhất quán (tất cả tags cùng border-radius)

### 5.6 Forms
- [ ] Input field height nhất quán (controlHeight token)
- [ ] Label style nhất quán (position, weight, color, alignment)
- [ ] Placeholder text style nhất quán
- [ ] Required indicator style nhất quán (*, red, bold)
- [ ] Error message style nhất quán (color, position, font-size)

---

### 5.7 Redundant Copy
- [ ] Subtitle/helper/summary text only appears when it adds information not already visible in the title, label, tab count, checkbox state, or placeholder
- [ ] Selected state is shown once through the strongest UI signal instead of repeated in a second text layer
- [ ] Dense internal tool panels avoid descriptive filler copy when the controls already explain themselves

## 6. Animation & Transition

### 6.1 Motion Tokens
- [ ] Transition duration dùng token (MOTION.fast, MOTION.mid...)
- [ ] Không mix fast (0.1s) và slow (0.5s) cho cùng loại interaction
- [ ] Easing function nhất quán

### 6.2 Pattern Consistency
- [ ] Hover effects cùng pattern (opacity change, background change, shadow lift — pick one or few)
- [ ] Modal open/close animation nhất quán
- [ ] Page transition nhất quán (nếu có)

---

## Scoring Guide

| Pass Rate | Score |
|-----------|-------|
| 95-100% | 10/10 — Design system hoàn hảo |
| 85-94% | 8-9/10 — Rất nhất quán, vài exception nhỏ |
| 70-84% | 6-7/10 — Khá nhất quán nhưng có inconsistency rõ |
| 50-69% | 4-5/10 — Nhiều inconsistency, visual "lộn xộn" |
| < 50% | 1-3/10 — Không có design system rõ ràng |

**Weight:** Token usage items quan trọng hơn (mỗi hardcoded value = debt tích lũy). Component pattern items cũng critical vì user nhận ra ngay "page A khác page B".
