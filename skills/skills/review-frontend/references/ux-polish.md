# UX Polish — Checklist chi tiết

Dimension này đánh giá: trải nghiệm sử dụng có **mượt** không? UI có thể đầy đủ (UI Completeness ✅) nhưng awkward to use. UX Polish là layer cuối cùng biến "feature đủ" thành "dùng thích".

Phân biệt với UI Completeness: UI Completeness hỏi "có thiếu gì không?", UX Polish hỏi "cái có sẵn có dùng tốt không?"

---

## 1. Information Architecture

### 1.1 Layout Hierarchy
- [ ] Thông tin quan trọng nhất ở vị trí nổi bật nhất (top-left hoặc center)
- [ ] Visual hierarchy rõ ràng: title > subtitle > body > metadata
- [ ] Related information grouped together (proximity principle)
- [ ] Không quá 3 level nested containers (card trong card trong card)

### 1.2 Content Priority
- [ ] Primary action dễ tìm nhất (nổi bật, đúng vị trí convention)
- [ ] Secondary actions không compete với primary (size/color thấp hơn)
- [ ] Destructive actions có visual warning (red, separated, confirm)
- [ ] Metadata/auxiliary info de-emphasized (smaller, lighter color)

### 1.3 Information Density
- [ ] Density phù hợp với audience:
  - Internal tool / power user: density cao OK (compact tables, dense forms)
  - Consumer app: density thấp (spacious, focused)
- [ ] Không quá sparse (wasted space, user phải scroll nhiều)
- [ ] Không quá dense (overwhelming, khó scan)
- [ ] Critical info đọc được mà không cần hover/click (avoid "hidden by default")

---

## 2. Interaction Patterns

### 2.1 Click & Action
- [ ] Interactive elements trông clickable (cursor pointer, hover state, color cue)
- [ ] Non-interactive elements không trông clickable (no hover state trên static text)
- [ ] Click target đủ lớn (tối thiểu 32x32 px, lý tưởng 40x40 cho touch)
- [ ] Double-click prevention cho destructive/submit actions
- [ ] Single-click cho common actions, multi-step cho dangerous actions

### 2.2 Feedback Timing
- [ ] Instant feedback cho clicks (< 100ms — visual state change)
- [ ] Loading indicator cho actions > 300ms
- [ ] Progress indicator cho actions > 2s
- [ ] Timeout/error cho actions > 10s (không để user chờ mãi)

### 2.3 Undo & Recovery
- [ ] Destructive actions có confirm dialog (delete, reset, override)
- [ ] Undo capability cho common actions (nếu phù hợp — toast + undo button)
- [ ] Form data không mất khi accident navigate (hoặc có warning)
- [ ] Browser back không gây data loss

---

## 3. Workflow Efficiency

### 3.1 Common Tasks
- [ ] Tác vụ thường xuyên nhất hoàn thành trong ít bước nhất
- [ ] Không có unnecessary confirmation/dialog cho routine actions
- [ ] Batch/bulk operations cho repetitive tasks
- [ ] Keyboard shortcuts cho power users (nếu phù hợp)

### 3.2 Data Entry
- [ ] Auto-focus vào first input khi open form/modal
- [ ] Tab order logic (trên xuống dưới, trái sang phải)
- [ ] Enter submit form (khi context rõ ràng)
- [ ] Smart defaults (pre-fill values người dùng hay chọn)
- [ ] Auto-complete/suggestions cho common inputs

### 3.3 Context Preservation
- [ ] Filter state giữ nguyên khi navigate giữa detail → list
- [ ] Scroll position giữ nguyên khi back từ detail
- [ ] Tab state giữ nguyên khi switch tabs
- [ ] Sort order giữ nguyên khi data update

---

## 4. Visual Feedback

### 4.1 State Communication
- [ ] User luôn biết "đang ở đâu" (active nav, breadcrumb, page title)
- [ ] User luôn biết "đã làm gì" (success toast, status update)
- [ ] User luôn biết "đang xảy ra gì" (loading, progress, pending)
- [ ] User luôn biết "cần làm gì" (CTA rõ ràng, empty state guidance)

### 4.2 Hover & Focus States
- [ ] Tất cả interactive elements có hover state
- [ ] Hover state consistent across cùng loại element
- [ ] Row hover trong table/list (highlight background)
- [ ] Focus state visible (keyboard navigation)

### 4.3 Transitions
- [ ] State changes có transition mượt (không "nhảy" đột ngột)
- [ ] Modal/drawer open/close có animation
- [ ] Loading → content transition smooth (không layout shift)
- [ ] Tab switch smooth (không flash of empty)

---

## 5. Error Prevention

### 5.1 Input Validation
- [ ] Real-time validation (validate as user types, hoặc on blur)
- [ ] Constraint visualization (character count, min/max hint)
- [ ] Disabled options explained (tooltip on disabled button)
- [ ] Format hints trước khi user nhập sai (placeholder, label text)

### 5.2 Dangerous Actions
- [ ] Delete/remove: confirm dialog với entity name
- [ ] Bulk actions: show count ("Xóa 12 items?")
- [ ] Irreversible actions: extra friction (type to confirm, hoặc delay)
- [ ] No double-submit (disable button after click, or debounce)

### 5.3 Recovery
- [ ] Error messages có actionable guidance ("Thử lại" button, "Kiểm tra lại X")
- [ ] Form errors không clear user input
- [ ] Session timeout: save draft hoặc warning trước

---

## 6. Micro-UX Details

Những chi tiết nhỏ tạo cảm giác "polished":

### 6.1 Text & Copy
- [ ] Button labels action-oriented ("Lưu thay đổi" thay vì "OK")
- [ ] Error messages human-friendly (không technical jargon)
- [ ] Confirmation messages specific ("Đã xóa Program 'ABC'" thay vì "Đã xóa")
- [ ] Tooltip text helpful (không repeat label — add extra info)

### 6.2 Visual Polish
- [ ] Icons consistent (cùng set, cùng style — outline vs filled)
- [ ] Avatar/placeholder consistent (same style initials, same colors)
- [ ] Status colors meaningful (green=good, red=bad, yellow=caution — not random)
- [ ] Whitespace breathing room (elements không bị "chật")

### 6.3 Edge Cases
- [ ] Single item list không awkward ("1 item" không "1 items")
- [ ] Zero state different from loading state
- [ ] Long names/values handled gracefully (truncate + tooltip)
- [ ] Copy to clipboard cho IDs, URLs, code snippets (nếu phù hợp)

---

## 7. Internal Tool Specific (nếu áp dụng)

### 7.1 Power User Features
- [ ] Table columns resizable hoặc configurable (nếu nhiều data)
- [ ] Export data capability (CSV, Excel)
- [ ] View toggle (card ↔ table) cho list views
- [ ] Advanced filter/search cho complex queries

### 7.2 Operational Safety
- [ ] Confirm trước actions ảnh hưởng nhiều users/items
- [ ] Audit trail visible (who changed what, when)
- [ ] Role-based UI (ẩn actions user không có quyền — không show rồi disable)
- [ ] Dry-run/preview cho batch operations (nếu phù hợp)

---

### 6.4 Less-is-more checks
- [ ] Subtitle/helper text only appears when removing it would create ambiguity or operational risk
- [ ] Summary copy does not repeat tab counts, selected chips, checkbox state, or other already-visible control state
- [ ] Tooltip/help text adds new information instead of restating the label or title

## Scoring Guide

| Pass Rate | Score |
|-----------|-------|
| 95-100% | 10/10 — Polished, feels professional and delightful |
| 85-94% | 8-9/10 — Smooth experience, minor rough edges |
| 70-84% | 6-7/10 — Functional but some awkward interactions |
| 50-69% | 4-5/10 — Usable but friction in common workflows |
| < 50% | 1-3/10 — Frustrating, user has to fight the UI |

**Weight:** Workflow Efficiency (section 3) và Error Prevention (section 5) quan trọng nhất cho internal tools — staff dùng hàng ngày, 1 friction point nhỏ × 100 lần/ngày = big pain.
