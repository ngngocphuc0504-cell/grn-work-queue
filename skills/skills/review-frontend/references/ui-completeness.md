# UI Completeness — Checklist chi tiết

Dimension này đánh giá: UI có **đầy đủ** không? Không phải đẹp hay xấu (đó là Design Consistency), mà là: có thiếu gì không? Có state nào user gặp mà UI chưa handle? Có field nào cần hiển thị mà chưa render?

---

## 1. Data Display

### 1.1 Fields Coverage
- [ ] Tất cả data fields có trong model/schema đều được hiển thị ở nơi phù hợp
- [ ] Không có field "phantom" — có trong API/mock nhưng không render anywhere
- [ ] Các field quan trọng (ID, name, status, created date) luôn visible, không hide

**Cách check:** Đọc mock data / API schema → list fields. Grep mỗi field name trong render JSX. Missing = gap.

### 1.2 Format & Presentation
- [ ] Dates format nhất quán và human-readable (không raw ISO string)
- [ ] Numbers format phù hợp (thousand separator cho money, decimal cho %, compact cho large)
- [ ] Long text có truncation hoặc expand pattern (không overflow container)
- [ ] Status values map sang visual indicator (badge/pill/icon), không raw string
- [ ] Enum values hiển thị human-readable label, không technical value

### 1.3 Lists & Tables
- [ ] Column headers mô tả rõ content
- [ ] Có sort capability cho columns quan trọng (nếu data > 10 items)
- [ ] Pagination hoặc virtualization cho data > 20 items
- [ ] Page size hợp lý (10-50, không 5 hoặc 1000)
- [ ] Có total count hiển thị

---

## 2. Application States

Đây là section quan trọng nhất — hầu hết UI "thiếu" là do không handle đủ states.

### 2.1 Loading States
- [ ] Initial load có skeleton/spinner (không blank screen)
- [ ] Action loading có indicator (button loading, inline spinner)
- [ ] Không có "flash of empty content" trước khi data load
- [ ] Loading state không block toàn bộ page (chỉ block section đang load)

### 2.2 Empty States
- [ ] Danh sách rỗng có empty state message (không chỉ blank area)
- [ ] Empty state có icon/illustration (không chỉ text)
- [ ] Empty state có call-to-action nếu user có thể tạo item mới
- [ ] Search/filter kết quả rỗng có message riêng ("Không tìm thấy kết quả")

### 2.3 Error States
- [ ] API error có UI hiển thị (toast/banner/inline message)
- [ ] Form validation error hiển thị inline (không chỉ alert)
- [ ] Network error có retry option
- [ ] Partial failure có xử lý (1 trong 3 API fail → hiển thị 2, báo lỗi 1)

### 2.4 Success Feedback
- [ ] CRUD operations có success feedback (toast/notification)
- [ ] Destructive actions có confirmation dialog
- [ ] Bulk operations có progress/completion indicator

---

## 3. Navigation & Routing

### 3.1 Navigation
- [ ] Sidebar/menu highlight active item
- [ ] Breadcrumb hoặc page title cho orientation
- [ ] Back navigation khả dụng (browser back hoặc UI back button)
- [ ] Deep link hoạt động (refresh page → vẫn đúng vị trí)

### 3.2 Tabs & Sub-navigation
- [ ] Tab active state rõ ràng
- [ ] Tab count/badge nếu relevant (ví dụ: "Pending (12)")
- [ ] Tab content không reset khi switch (hoặc reset intentionally)

---

## 4. Forms

### 4.1 Input Completeness
- [ ] Tất cả fields trong form có label
- [ ] Required fields có indicator (*)
- [ ] Placeholder text hướng dẫn format/example
- [ ] Input type phù hợp (number cho số, date picker cho ngày, select cho enum)

### 4.2 Validation
- [ ] Client-side validation trước submit
- [ ] Error message cụ thể (không chỉ "Invalid input" — mà "Email phải chứa @")
- [ ] Error state clear khi user sửa
- [ ] Submit button disabled khi form invalid (hoặc enable + validate on submit)

### 4.3 Edit/Create Pattern
- [ ] Edit form pre-fill data hiện tại
- [ ] Create form clear/default values
- [ ] Unsaved changes warning khi navigate away (nếu form phức tạp)
- [ ] Cancel action rõ ràng

---

## 5. Search & Filter

### 5.1 Search
- [ ] Search input có icon hoặc placeholder chỉ rõ tìm gì
- [ ] Search realtime (debounced) hoặc có search button
- [ ] Search highlight kết quả (nếu phù hợp)
- [ ] Clear search dễ dàng (X button)

### 5.2 Filters
- [ ] Filter controls accessible (không ẩn quá sâu)
- [ ] Active filters visible (tags, pills, hoặc highlighted controls)
- [ ] Clear all filters dễ dàng
- [ ] Filter state persist khi navigate (nếu phù hợp)
- [ ] Filter result count update realtime

---

## 6. Responsive & Overflow

### 6.1 Content Overflow
- [ ] Long text có ellipsis/truncation (không overflow container)
- [ ] Long names/emails không break layout
- [ ] Table horizontal scroll khi nhiều columns
- [ ] Modal không tràn viewport (maxHeight + scroll body)

### 6.2 Responsive (nếu required)
- [ ] Layout adapt cho screen sizes phù hợp (nếu app cần responsive)
- [ ] Touch targets đủ lớn trên mobile (44x44px minimum)
- [ ] Sidebar collapse trên mobile (nếu có)

---

## 7. Accessibility Basics

Cho internal tools, accessibility có thể simplified nhưng basics vẫn cần:

### 7.1 Keyboard
- [ ] Tab navigation qua interactive elements (không bị trap)
- [ ] Enter/Space activate buttons
- [ ] Escape close modals/dropdowns
- [ ] Focus visible (outline hoặc highlight khi tab tới)

### 7.2 Screen Reader Basics
- [ ] Images có alt text (nếu có images)
- [ ] Icon-only buttons có aria-label hoặc title
- [ ] Form inputs có associated labels (htmlFor hoặc aria-label)

---

## Scoring Guide

| Pass Rate | Score |
|-----------|-------|
| 95-100% | 10/10 — UI hoàn chỉnh, mọi state đều handled |
| 85-94% | 8-9/10 — Rất đầy đủ, thiếu vài minor states |
| 70-84% | 6-7/10 — Đầy đủ cơ bản nhưng thiếu loading/empty/error states |
| 50-69% | 4-5/10 — Nhiều gaps, user sẽ gặp blank screens hoặc unhanded cases |
| < 50% | 1-3/10 — UI skeleton only, nhiều features chưa implement |

**Weight:** Application States (section 2) chiếm weight cao nhất — thiếu loading/empty/error state là issue mà user gặp thường xuyên và tạo cảm giác "app chưa xong".
