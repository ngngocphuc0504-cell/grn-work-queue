# Code Quality — Checklist chi tiết

Mỗi item dưới đây là 1 điểm kiểm tra. Khi scan code, đánh giá pass/fail cho từng item áp dụng được. Items không áp dụng (ví dụ: "API calls" trong project không có API) → bỏ qua, không tính vào score.

---

## 1. Component Architecture

### 1.1 Component Size
- [ ] Không có component > 300 dòng (candidate for split)
- [ ] Không có component > 500 dòng (must split)
- [ ] Mỗi component có 1 responsibility rõ ràng
- [ ] Shared/reusable logic được extract thành hooks hoặc helpers

**Cách check:** Đếm dòng mỗi component. Grep `export (function|const)` để liệt kê.
**Tại sao quan trọng:** Component lớn khó debug, khó test, khó review. Khi có bug, phải đọc hết 500 dòng thay vì 80 dòng.

### 1.2 File Organization
- [ ] Mỗi file < 500 dòng (lý tưởng < 300)
- [ ] File name phản ánh nội dung (ProgramModal.jsx chứa ProgramModal)
- [ ] Không có file "misc", "utils" chứa quá nhiều thứ không liên quan
- [ ] Index file chỉ orchestrate, không chứa quá nhiều business logic

**Cách check:** `wc -l` per file. Scan file content vs file name.

### 1.3 Import/Export Hygiene
- [ ] Không có unused imports
- [ ] Không có circular dependencies
- [ ] Named exports có tên descriptive
- [ ] Barrel files (index.js re-exports) không quá sâu

**Cách check:** Grep mỗi import name → verify nó xuất hiện trong file body (ngoài import line).

---

## 2. State Management

### 2.1 State Placement
- [ ] State được đặt ở component gần nhất cần nó (không lift lên quá cao)
- [ ] State dùng chung 2+ siblings → lift lên parent đúng cách
- [ ] Không có derived state (state tính được từ state khác → dùng useMemo)
- [ ] Không có state đồng bộ thủ công (2 state luôn cùng thay đổi → gộp)

**Tại sao quan trọng:** State placement sai → re-render không cần thiết, prop drilling sâu, bug khó trace.

### 2.2 Side Effects
- [ ] useEffect có dependency array đúng (không thiếu, không thừa)
- [ ] Cleanup function cho subscriptions, timers, listeners
- [ ] Không có useEffect chỉ để sync state (nên dùng useMemo hoặc tính trực tiếp)
- [ ] Fetch data có loading/error state

### 2.3 Refs
- [ ] Ref dùng cho DOM access, không cho state (trừ khi cần avoid re-render)
- [ ] Ref không null-check bị bỏ qua (ref.current có thể null)

---

## 3. Code Conventions

### 3.1 Naming
- [ ] Components: PascalCase
- [ ] Hooks: useCamelCase
- [ ] Constants: UPPER_SNAKE_CASE hoặc camelCase (consistent)
- [ ] Event handlers: handleX / onX (consistent)
- [ ] Boolean: isX, hasX, canX, shouldX
- [ ] Naming nhất quán across files (không file A dùng `isOpen`, file B dùng `open` cho cùng concept)

### 3.2 Consistency
- [ ] Cùng pattern cho cùng use case (ví dụ: tất cả modals dùng cùng open/close pattern)
- [ ] Import order consistent (react → libraries → local components → local utils → styles)
- [ ] Cùng style khai báo: arrow function vs function declaration (pick one, stick with it)

### 3.3 Dead Code
- [ ] Không có commented-out code blocks (> 3 dòng)
- [ ] Không có console.log/warn/error (ngoài error boundary)
- [ ] Không có TODO/FIXME lâu (check git blame nếu có)
- [ ] Không có unused functions/variables

**Cách check:** Grep `console.`, `// TODO`, `// FIXME`, `// HACK`. Grep `/*` multiline blocks.

---

## 4. Performance

### 4.1 Rendering
- [ ] useMemo cho expensive calculations (sort/filter large arrays)
- [ ] useCallback cho handlers truyền xuống child components (nếu child dùng React.memo)
- [ ] Không create new objects/arrays trong JSX props (gây re-render)
- [ ] Key props đúng (không dùng index cho lists có thể reorder)
- [ ] Lazy load cho heavy components (React.lazy + Suspense)

### 4.2 Data
- [ ] Không fetch trong loop
- [ ] Không re-compute cùng data nhiều lần (memoize)
- [ ] Large lists dùng virtualization hoặc pagination
- [ ] Images có proper sizing (không load 2000px image cho 200px container)

### 4.3 Bundle
- [ ] Không import toàn bộ library khi chỉ cần 1 function (ví dụ: `import _ from 'lodash'` → `import debounce from 'lodash/debounce'`)
- [ ] Dynamic imports cho routes/pages (code splitting)

---

## 5. Error Handling

### 5.1 Runtime Safety
- [ ] Optional chaining cho nested object access (data?.user?.name)
- [ ] Default values cho destructured props
- [ ] Array methods có null/undefined check trước (.map, .filter, .reduce)
- [ ] Type coercion có intent rõ ràng (Number(x), String(x), Boolean(x))

### 5.2 Error Boundaries
- [ ] Có Error Boundary bọc routes/pages chính
- [ ] Error state có UI phù hợp (không blank screen)

### 5.3 Edge Cases
- [ ] Empty state khi data = []
- [ ] Loading state khi data đang fetch
- [ ] Null/undefined props không gây crash

---

## Scoring Guide

Đếm items áp dụng và items pass:

| Pass Rate | Score |
|-----------|-------|
| 95-100% | 10/10 |
| 85-94% | 8-9/10 |
| 70-84% | 6-7/10 |
| 50-69% | 4-5/10 |
| 30-49% | 2-3/10 |
| < 30% | 1/10 |

Adjust ±1 dựa trên severity: nếu ít items fail nhưng toàn critical → trừ thêm. Nếu nhiều items fail nhưng toàn minor → bớt trừ.
