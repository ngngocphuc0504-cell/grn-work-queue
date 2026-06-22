---
name: review-frontend
description: >
  Skill audit frontend theo 4 dimension: Code Quality, Design Consistency, UI Completeness, UX Polish.
  Đây là tên mới theo vai trò của skill cũ `project-optimizer`. Skill này xuất findings,
  scorecard, và kế hoạch fix ưu tiên; không tự kiêm implementation mặc định.
---

# Review Frontend

Phân tích sâu dự án frontend theo **4 dimension**. Mỗi dimension có reference file chứa checklist chi tiết — chỉ đọc dimension cần thiết.

## Boundary

- Sở hữu: review, findings, scorecard, ship-readiness, fix plan.
- Không sở hữu: tự triển khai code fix mặc định.
- Khi user muốn triển khai fix, handoff sang `build-frontend`.

## Less is more review lens

Trong mọi review design-facing, kiểm tra thêm 5 điểm này:
- Có hơn một primary CTA cạnh tranh nhau không.
- Có subtitle/helper text/badge/card nào đang lặp lại ý đã có ở title, tab, filter, hoặc state control không.
- Có filter, metadata, hoặc settings nào nên chuyển sang progressive disclosure không.
- Có dùng wrapper/custom UI làm giao diện phức tạp hơn AntD core mà không có lợi ích rõ ràng không.
- Có màn hình data-heavy/admin/detail/form nào đang tự dựng scaffolding mà `ProTable`, `ProForm`, `ProDescriptions`, hoặc form wrappers của Pro Components sẽ đơn giản hóa rõ ràng không.
- Có section/layout nào chỉ thêm entropy mà không giúp user hoàn thành task nhanh hơn không.
- Có locale leakage nào làm system UI chrome nhảy sang ngôn ngữ khác ngoài contract không.

## 4 Dimensions

| # | Dimension | Focus | Reference |
|---|-----------|-------|-----------|
| 1 | **Code Quality** | Maintainability, structure, conventions, performance | `references/code-quality.md` |
| 2 | **Design Consistency** | Token usage, spacing, color, typography đồng nhất | `references/design-consistency.md` |
| 3 | **UI Completeness** | Fields, states, feedback, responsive, accessibility | `references/ui-completeness.md` |
| 4 | **UX Polish** | Flow, interaction, micro-UX, error handling, delight | `references/ux-polish.md` |

---

## Workflow

### Bước 0 — Xác định scope

Khi user yêu cầu optimize, cần xác định 2 trục:

#### Trục 1: Scope Level

| Level | Khi nào | Đọc gì | Output |
|-------|---------|--------|--------|
| **🌐 Project-wide** | "tối ưu dự án", "review tổng thể", "chuẩn hóa across pages" | Theme + shared components + 3-4 pages đại diện + routing | Report toàn dự án, chuẩn chung cho team follow |
| **📄 Page** | "optimize page Creator", "review page Mission" | Theme + shared components + toàn bộ files trong page folder | Report cho 1 page, so sánh với chuẩn chung |
| **📑 Sub-page / Tab** | "optimize tab Labels", "review sub-page Criteria" | Theme + shared components + parent page context + sub-page code | Report cho sub-page, verify đồng bộ với siblings |
| **🧩 Feature / Component** | "optimize popup ProgramModal", "review component DataTable" | Theme + shared components + component file + 2-3 nơi gọi component | Report cho component, verify consistent across callers |

**Cách xác định level:**
- User nói rõ → dùng level đó
- User nói chung ("tối ưu dự án") → Project-wide
- User chỉ vào file/component cụ thể → Feature level
- Không rõ → hỏi 1 câu: "Optimize tổng thể hay focus vào phần cụ thể nào?"

#### Trục 2: Dimensions

- Nếu nói cụ thể ("optimize code", "cải thiện UX") → chỉ dimension đó
- Nếu nói chung ("tối ưu dự án", "review tổng thể") → cả 4 dimensions
- Nếu không rõ → default cả 4, ưu tiên theo vấn đề tìm thấy

#### Project Context — Luôn đọc trước (bất kể level nào)

Dù optimize ở level nào, **luôn đọc project context trước** để có baseline đối chiếu:

1. **Theme/tokens file** — chuẩn color, spacing, typography của dự án
2. **Shared components** (AntD wrappers, Layout) — component patterns chung
3. **1-2 page/module đã hoàn thiện** (nếu đang optimize module mới) — làm reference cho "chuẩn chung"

Lý do: khi optimize 1 popup, cần biết các popup khác trong dự án trông thế nào để đảm bảo consistency. Khi làm xong page mới, cần verify nó match existing pages.

Không hỏi thêm trừ khi thiếu thông tin quan trọng. Nếu cần hỏi → gộp 1 câu duy nhất.

### Bước 1 — Scan & Analyze

Đọc reference files cho dimensions đã chọn, rồi scan code theo từng checklist.

**Chiến lược scan theo scope level:**

#### 🌐 Project-wide scan
1. **Theme/tokens file** → baseline cho Design Consistency
2. **Shared components** (AntD wrappers, Layout) → pattern chính
3. **Entry points** (App.jsx, routing) → architecture overview
4. **3-4 pages đại diện** → scan chi tiết từng dimension
5. **Cross-page consistency** — so sánh patterns giữa các pages:
   - Tất cả tables có cùng style không?
   - Tất cả modals có cùng layout không?
   - Tất cả empty states có cùng pattern không?
6. Xuất "**Project Standards**" — danh sách chuẩn chung phát hiện được, dùng làm baseline cho future optimizations

#### 📄 Page-level scan
1. Đọc project context (theme + shared components)
2. Đọc **toàn bộ files** trong page folder
3. Scan theo checklist
4. **Sync check**: so sánh với 1-2 existing pages → page mới có match chuẩn chung không?
   - Cùng table header style?
   - Cùng filter bar pattern?
   - Cùng modal form layout?
   - Cùng empty state component?

#### 📑 Sub-page / Tab scan
1. Đọc project context + parent page (index.jsx)
2. Đọc sub-page/tab code
3. Scan theo checklist
4. **Sibling sync check**: so sánh với các tabs/sub-pages cùng level
   - Tab A dùng card grid, tab B dùng table — intentional hay inconsistent?
   - Tab A có search/filter, tab B không — thiếu hay không cần?
   - Tab A có empty state, tab C không — gap

#### 🧩 Feature / Component scan
1. Đọc project context + component file
2. **Grep tất cả nơi gọi component** — component được dùng ở đâu, truyền props gì
3. Scan theo checklist (focus: Code Quality + Design Consistency)
4. **Usage consistency check**: component có behave giống nhau ở mọi nơi không?
   - Popup A được gọi với full props, popup B thiếu vài props → inconsistent
   - Component render khác nhau tùy context — intentional (responsive) hay bug?

**Grep patterns cho common issues (áp dụng mọi level):**
   - Hardcoded colors: `/#[0-9a-f]{3,6}/i` ngoài token file
   - Hardcoded spacing: `/padding:\s*\d+px/` ngoài token
   - Magic numbers: `/\d{2,}/ ` trong style props
   - Console.log: `/console\.(log|warn|error)/`
   - TODO/FIXME: `/TODO|FIXME|HACK|XXX/`
   - Inline styles trùng lặp (copy-paste patterns)
   - Components > 300 dòng (candidate for split)

**Với mỗi issue tìm thấy, ghi nhận:**
```
ISSUE: Mô tả ngắn
DIMENSION: Code | Design | UI | UX
SEVERITY: 🔴 Critical | 🟡 Medium | 🟢 Minor
LOCATION: file:line (hoặc pattern nếu nhiều nơi)
EVIDENCE: Code snippet / số liệu cụ thể
FIX: Hành động cần làm
RISK: Thấp / Trung / Cao (khả năng gây side-effect)
EFFORT: ~X dòng hoặc ~X phút
```

### Bước 2 — Scoring

Chấm điểm mỗi dimension theo thang 10, dựa trên tỷ lệ pass checklist items:

| Điểm | Ý nghĩa |
|-------|---------|
| 9-10 | Production-ready, ít hoặc không có issue |
| 7-8 | Tốt, chỉ có minor issues |
| 5-6 | Trung bình, có medium issues cần xử lý |
| 3-4 | Yếu, nhiều issues ảnh hưởng chất lượng |
| 1-2 | Nghiêm trọng, cần refactor lớn |

**Scoring phải có evidence** — không chấm cảm tính. Mỗi điểm trừ phải gắn với issue cụ thể.

### Bước 3 — Report

Tạo file `{PROJECT}-OPTIMIZE-REPORT.md` trong workspace folder:

```markdown
# {Project} — Optimization Report ({ngày})

## Scorecard
| Dimension | Score | Issues | Top Priority |
|-----------|-------|--------|-------------|
| Code Quality | X/10 | 🔴x 🟡y 🟢z | [issue chính] |
| Design Consistency | X/10 | 🔴x 🟡y 🟢z | [issue chính] |
| UI Completeness | X/10 | 🔴x 🟡y 🟢z | [issue chính] |
| UX Polish | X/10 | 🔴x 🟡y 🟢z | [issue chính] |
| **Overall** | **X/10** | | |

## Dimension 1 — Code Quality (X/10)

### 🔴 Critical Issues
#### CQ-01: {Tên issue}
- **Vị trí:** file:line
- **Vấn đề:** Mô tả cụ thể + evidence
- **Impact:** Tại sao quan trọng
- **Fix:** Hành động cụ thể
- **Effort:** ~X dòng | Risk: Thấp/Trung/Cao

### 🟡 Medium Issues
[same format]

### 🟢 Minor Issues
[same format]

### ✅ Highlights
[Những điểm tốt đáng giữ — quan trọng để không vô tình phá khi optimize]

## Dimension 2 — Design Consistency (X/10)
[same structure]

## Dimension 3 — UI Completeness (X/10)
[same structure]

## Dimension 4 — UX Polish (X/10)
[same structure]

---

## Sync Check (cho Page / Sub-page / Feature level)
[Section này chỉ xuất hiện khi scope KHÔNG phải project-wide]

### So sánh với chuẩn chung
| Pattern | Project Standard | Target | Match? |
|---------|-----------------|--------|--------|
| Table header style | Bold, bg #fafafa, uppercase | Bold, bg #f5f5f5 | 🟡 Gần match — adjust bg |
| Modal form layout | Label 100px right-align + flex input | Label top-align + full-width | 🔴 Khác pattern |
| Empty state | EmptyState component + icon + CTA | Plain text "No data" | 🔴 Thiếu component |
| Card padding | T.paddingLG (24px) | 16px hardcoded | 🟡 Gần — dùng token |
| Filter bar | SmartFilter inline, top of content | Dropdown hidden | 🔴 Khác pattern |

### Sibling Comparison (cho sub-page/tab)
| Aspect | Tab A (Review) | Tab B (Profile) | Target Tab | Đồng bộ? |
|--------|---------------|-----------------|------------|----------|
| Layout | Card + Table toggle | Card + Table toggle | Card only | 🔴 Thiếu table view |
| Filter | SmartFilter + ProgramMultiSelect | SmartFilter + ProgramMultiSelect | Không có | 🔴 Thiếu filter |
| Empty state | EmptyState component | EmptyState component | Không có | 🔴 Thiếu |
| Pagination | CardPaginator | CardPaginator | Không có | 🟡 Cần thêm nếu data > 20 |

## Dimension 4 — UX Polish (X/10)
[same structure]

---

## Kế hoạch triển khai

Sắp xếp theo: Risk thấp trước → cao sau, grouped by file để minimize context switch.

### Phase 1 — Quick Wins (🟢 Low Risk)
| # | Issue | File | Effort | Dimension |
|---|-------|------|--------|-----------|
| 1 | ... | ... | ~X dòng | Code/Design/UI/UX |

### Phase 2 — Medium Impact (🟡 Medium Risk)
[same table]

### Phase 3 — Major Refactors (🔴 High Risk)
[same table]

**Tổng effort ước tính:** ~X dòng thay đổi across Y files

## Cross-Dimensional Dependencies
[Khi issues từ dimensions khác nhau liên quan đến nhau — ví dụ: fix color tokens (Design) cũng fix code duplication (Code)]
| Fix | Unblocks | Lý do |
|-----|----------|-------|
| DC-01: Consolidate colors | CQ-02: Remove local TAG_COLOR_MAP | Cùng root cause |
| ... | ... | ... |

## Ship Readiness
| Category | Issues | Ship Decision |
|----------|--------|--------------|
| 🚫 Ship Blockers | [list issues gây crash/mất data] | Fix trước khi deploy |
| ⚠️ Ship with Caution | [list issues ảnh hưởng UX nhưng không crash] | Deploy + fix trong sprint sau |
| 📋 Polish Later | [list issues nice-to-have] | Backlog |
```

Sau khi tạo report → chia sẻ link file + tóm tắt ngắn:
- Overall score
- Số issues theo severity
- Top 3 priorities
- Ship readiness verdict

### Bước 4 — Handoff Fix

Sau khi user duyệt plan (hoặc nói "làm đi"):

1. Chốt thứ tự ưu tiên fix theo severity và effort.
2. Bàn giao danh sách issue sang `build-frontend` hoặc agent triển khai.
3. Giữ lại report làm baseline để re-review sau khi code xong.
4. Với issue rủi ro cao, ghi rõ test cần chạy sau fix.

### Bước 5 — Verify

Sau khi fix xong:
1. Re-scan các checklist items đã fail
2. Cập nhật score trong report
3. Tóm tắt: before vs after score

---

## Nguyên tắc quan trọng

### Không optimize quá mức
- Nếu code đang hoạt động tốt và readable → đừng refactor chỉ vì "có thể clean hơn"
- Mỗi thay đổi phải có lý do rõ ràng (performance, maintainability, consistency, UX)
- Giữ nguyên patterns mà team đã quen — consistency quan trọng hơn "best practice" trừu tượng

### Respect existing architecture
- Đọc kỹ project conventions trước khi đề xuất thay đổi
- Nếu dự án dùng inline styles → optimize inline styles, không đề xuất chuyển CSS modules
- Nếu dự án dùng design tokens → mọi fix phải dùng tokens, không hardcode

### Evidence-based
- Mọi issue phải có code evidence cụ thể (file, line, snippet)
- Không báo issue dựa trên "best practice" chung chung mà không thấy trong code thực tế
- Score phải justify được — nếu ai hỏi "tại sao 6/10?" phải trả lời được ngay

### Fix kèm template code
- Khi đề xuất thêm UI element (empty state, loading, error) → cung cấp JSX snippet cụ thể dùng đúng components có sẵn trong project, không chỉ mô tả
- Khi đề xuất sửa style → cung cấp exact token thay thế (ví dụ: `#7c3aed` → `T.colorPrimary`)
- Khi đề xuất refactor → code before/after ngắn gọn

### Score interpretation rõ ràng
Score đi kèm interpretation thực tế:
- 9-10: Production-ready, chỉ cần minor polish
- 7-8: Functional, ship được nhưng nên fix medium issues trong sprint sau
- 5-6: Cần work trước khi ship — user experience sẽ bị ảnh hưởng
- 3-4: Cần refactor đáng kể — nhiều rough edges
- 1-2: Prototype stage, chưa ready cho end users

### Preserve what works
- Ghi nhận ✅ Highlights — những pattern tốt trong code
- Đảm bảo fix không phá những phần đang hoạt động
- Nếu không chắc → nói rõ risk và hỏi user

---

## Adaptive behavior

Skill này hoạt động cho mọi dự án frontend:
- **React / Vue / Angular / Svelte** — adjust checklist theo framework
- **Inline styles / CSS Modules / Tailwind / Styled Components** — adjust design consistency checks
- **Internal tool / Consumer app / Landing page** — adjust UX expectations (internal tool: density cao, error tolerance thấp; consumer: accessibility, mobile-first)
- **Single file / Multi-file** — adjust code quality checks tương ứng

Nếu dự án thuộc Garena ecosystem internal tool → kết hợp thêm conventions từ `build-frontend`, `design-uiux`, `design-system-antd`, và `govern-layout` khi có.
