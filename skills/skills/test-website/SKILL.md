---
name: test-website
description: >
  Skill test website tự động qua browser. Đây là tên mới theo vai trò của skill cũ `website-tester`.
  Skill này chỉ test và báo findings; không tự sửa UI/code.
---

# Test Website
## Default Internal-Web Viewport

- Primary desktop baseline for internal web is `1920 x 900`.
- Treat this as the usable viewport after browser chrome on a Full HD PC.
- Always validate desktop layout at `1920 x 900` first before drawing conclusions from wider screens.
- Use 4K only as a secondary regression check; it must not override the `1920 x 900` baseline.
- When the user says `PC`, `desktop`, or `internal web` without another viewport, assume `1920 x 900`.


## Contract trước khi test UI

Khi task có liên quan đến UI consistency, layout, hoặc regression:
1. Đọc `DESIGN.md` nếu project có
2. Đọc `LAYOUT-BLUEPRINT.md` nếu project có
3. Dùng hai artifact đó làm baseline trước khi chấm lỗi

Skill này giúp kiểm tra website đang chạy bằng cách dùng Claude in Chrome: tự mở browser, lướt qua từng trang, chụp ảnh, phát hiện lỗi, và báo cáo lại bằng ngôn ngữ dễ hiểu.

Skill này **không gắn vào project cụ thể nào** — dùng được cho bất kỳ web tool nội bộ nào đang chạy trên localhost hoặc URL bất kỳ.

## Nguyên tắc quan trọng nhất

User của skill này là người **không biết code**. Mọi output phải:
- Mô tả lỗi bằng **vị trí trên màn hình** ("góc trên bên phải", "bảng dữ liệu ở giữa trang", "nút xanh dưới cùng")
- Mô tả bằng **hiện tượng nhìn thấy** ("trang trắng trơn", "chữ bị đè lên nhau", "bảng không có dữ liệu")
- **Không bao giờ** paste console error, stack trace, hoặc code snippet trong bug report
- **Không dùng** thuật ngữ kỹ thuật (component, render, state, props, DOM, hook...)
- Nếu có lỗi kỹ thuật (JS error), dịch thành ngôn ngữ người dùng: "Trang bị lỗi kỹ thuật, không thể hiển thị nội dung"
- Kèm screenshot cho MỌI lỗi tìm được — ảnh nói nhiều hơn chữ

## Ba chế độ

### Mode 1: Scan toàn bộ
Khi user nói "test website", "scan hết", "test toàn bộ", hoặc không chỉ định trang cụ thể.

### Mode 2: Test trang cụ thể
Khi user nói "test trang Creator", "check Dashboard", hoặc chỉ định rõ trang nào.

### Mode 3: So sánh với logic brief
Khi user nói "kiểm tra theo logic", "test theo logic brief", "so sánh logic với website", "logic có khớp không", hoặc cung cấp file logic brief (.md) kèm yêu cầu test.

Mode này kiểm tra **hai chiều**: (1) Logic → Website: mọi thứ logic mô tả có hiện đúng trên website không? (2) Website → Logic: website có phần tử / hành vi nào mà logic brief **không nhắc đến** không?

Chiều thứ 2 rất quan trọng — nếu bỏ qua, sẽ bỏ sót các nút bấm, icon, conditional UI, hoặc handler tồn tại trên website nhưng chưa được document. Đây là lỗ hổng phổ biến nhất khi so sánh logic với thực tế.

## Quy trình test

## Browser Surface Rule

- Dùng browser tool family đang có thật trong session.
- Ưu tiên Chrome plugin hoặc CDP browser surface nếu đã có.
- Coi các tên như `read_page`, `read_console_messages`, `javascript_tool`, `resize_window` là logical browser actions, không phải cam kết về exact tool id.
- Không assume legacy tool như `tabs_context_mcp` còn tồn tại. Nếu browser surface hiện tại không expose action cơ bản cần thiết, báo gọn là tool surface chưa sẵn sàng thay vì gọi tên tool cũ.

### Bước 1: Mở website

1. Dùng browser surface hiện có để claim tab hiện có hoặc tạo tab mới
2. Navigate đến URL (mặc định `http://localhost:3000`, hoặc URL user cung cấp)
3. Chờ 2-3 giây cho trang load xong
4. Chụp screenshot xác nhận website đang chạy

**Nếu website không mở được:** Báo user ngắn gọn: "Website chưa chạy. Bạn mở terminal chạy `npm run dev` rồi bảo tôi test lại nhé."

### Bước 2: Khám phá cấu trúc website (tự động — không cần biết trước)

Đây là bước quan trọng khiến skill dùng được cho bất kỳ project nào:

1. Chụp screenshot trang chủ
2. Dùng `read_page` với `filter: "interactive"` để tìm tất cả menu/navigation items
3. Dùng `find` tool tìm "sidebar menu", "navigation", "menu items" để phát hiện cấu trúc điều hướng
4. Liệt kê tất cả các trang có thể navigate đến
5. Báo user: "Tôi tìm thấy X trang: [danh sách]. Bắt đầu test nhé?"

Nếu Mode 2, chỉ navigate đến trang được chỉ định.

### Bước 3: Test từng trang — 4 bước kiểm tra

Với mỗi trang, làm tuần tự:

#### Kiểm tra 1: Nhìn tổng thể (Visual)

- Chụp screenshot toàn trang
- Scroll xuống 2-3 lần, chụp thêm screenshot ở mỗi vị trí
- Kiểm tra:
  - Trang có hiển thị nội dung không hay trắng trơn?
  - Các phần trên trang có nằm đúng vị trí không? (có bị chồng lên nhau, tràn ra ngoài?)
  - Bảng dữ liệu có hiển thị dữ liệu không hay trống?
  - Các biểu tượng, hình ảnh có hiện không hay bị vỡ?
  - Chữ có đọc được không? (không bị cắt, không bị đè, màu sắc đủ tương phản)
  - Menu bên trái (sidebar) có hiển thị đúng không?

#### Kiểm tra 2: Bấm thử các nút (Functional)

- Dùng `read_page` filter interactive để tìm tất cả nút bấm, ô nhập, dropdown
- Test theo thứ tự ưu tiên:
  1. **Nút chính**: Nút "Thêm mới", "Tạo", "Add", "Create" → bấm → có popup/form hiện ra không?
  2. **Popup/Drawer**: Nếu có popup → nội dung bên trong ổn không? → Đóng lại được không?
  3. **Bộ lọc/Filter Bar**: ⚠️ **Đặc biệt quan trọng** — Filter bar là nguồn bug rất phổ biến:
     - Click vào **từng ô filter** một (Platform, Time Range, Sentiment, v.v.) → dropdown/popover có mở ra không?
     - Nếu dropdown không mở: thử click chính xác vào text label, vào icon mũi tên, và vào vùng trống của ô filter
     - Nếu dropdown mở: chọn 1 giá trị → dropdown đóng lại → giá trị hiển thị đúng không?
     - Chụp screenshot **trước khi click** và **sau khi click** để so sánh — nhiều khi dropdown mở nhưng bị ẩn sau phần tử khác
     - Kinh nghiệm: Filter/Popover hay bị hỏng vì lý do kỹ thuật ẩn (component tạo lại mỗi lần render, onClick conflict, z-index). Luôn test kỹ bằng click thực tế.
  4. **Ô tìm kiếm**: Nếu có ô search → nhập thử → dữ liệu có filter không?
  5. **Tab/Chuyển mục**: Nếu có tabs → click từng tab → nội dung có đổi không?
  6. **Bảng dữ liệu**: Nếu có bảng → click vào dòng → có mở chi tiết không?
- Chụp screenshot SAU MỖI thao tác để ghi nhận kết quả

#### Kiểm tra 3: Scroll ngang và dọc (Overflow)

Kiểm tra này phát hiện nội dung bị tràn, thanh cuộn ngang không mong muốn, hoặc layout bị vỡ — những lỗi rất phổ biến ở web tool nội bộ, đặc biệt với bảng dữ liệu nhiều cột hoặc trang chưa responsive tốt. Nhiều lỗi scroll chỉ phát hiện được bằng code, không thể thấy bằng mắt qua screenshot.

**Chạy đoạn JavaScript sau trên mỗi trang** (dùng `javascript_tool`):

```javascript
const results = {};

// 1. Thanh cuộn ngang toàn trang (thường là lỗi)
results.hasPageHorizontalScroll = document.documentElement.scrollWidth > document.documentElement.clientWidth;
results.pageScrollWidth = document.documentElement.scrollWidth;
results.pageClientWidth = document.documentElement.clientWidth;

// 2. Tìm phần tử tràn ra ngoài viewport (phải)
const overflowing = [];
document.querySelectorAll('*').forEach(el => {
  const rect = el.getBoundingClientRect();
  const style = window.getComputedStyle(el);
  if (style.display === 'none' || style.visibility === 'hidden') return;
  if (rect.width > 0 && rect.right > window.innerWidth + 5) {
    overflowing.push({
      tag: el.tagName,
      className: (el.className?.toString?.() || '').slice(0, 80),
      text: (el.textContent || '').slice(0, 40).trim(),
      overflowPx: Math.round(rect.right - window.innerWidth)
    });
  }
});
results.overflowingElements = overflowing.slice(0, 10);

// 3. Tìm container có scroll ngang bên trong
const scrollable = [];
document.querySelectorAll('*').forEach(el => {
  if (el.scrollWidth > el.clientWidth + 5 && el.clientWidth > 0) {
    const style = window.getComputedStyle(el);
    const isIntentional = ['auto','scroll'].includes(style.overflowX);
    scrollable.push({
      tag: el.tagName,
      className: (el.className?.toString?.() || '').slice(0, 80),
      scrollWidth: el.scrollWidth,
      clientWidth: el.clientWidth,
      overflowX: style.overflowX,
      intentional: isIntentional
    });
  }
});
results.scrollableContainers = scrollable.slice(0, 10);

// 4. Chiều cao trang — có quá dài không
results.pageHeight = document.documentElement.scrollHeight;
results.viewportHeight = window.innerHeight;
results.scrollRatio = Math.round((document.documentElement.scrollHeight / window.innerHeight) * 10) / 10;

JSON.stringify(results, null, 2);
```

**Cách đánh giá kết quả:**

| Kết quả | Mức độ | Ý nghĩa (báo user) |
|---------|--------|---------------------|
| `hasPageHorizontalScroll = true` | 🔴 Nghiêm trọng | "Trang bị thanh cuộn ngang — nội dung tràn ra ngoài bên phải màn hình" |
| `overflowingElements` có phần tử | 🟡 Cần sửa | "Có [mô tả phần tử] bị lấn ra ngoài viền phải trang [X] pixel" |
| `scrollableContainers` với `intentional: false` | 🟡 Cần sửa | "Có vùng nội dung bị tràn không chủ đích ở [vị trí]" |
| `scrollableContainers` với `intentional: true` | ✅ OK | Bảng/code block có scroll ngang có chủ đích — bình thường |
| `scrollRatio > 15` | 🟢 Ghi chú | "Trang rất dài (phải cuộn [X] lần), có thể cần chia trang" |

**Thời điểm chạy:** Ngay sau Kiểm tra 1 (Visual), trước khi bấm thử nút. Chạy trên MỌI trang được test.

**Lưu ý:** Nếu phát hiện scroll ngang, nên thử thu hẹp cửa sổ browser (dùng `resize_window` nếu có) xuống ~1200px rồi chạy lại — nhiều lỗi scroll chỉ xuất hiện ở kích thước nhỏ hơn.

#### Kiểm tra 4: Lỗi ẩn (Technical — nhưng báo cáo bằng ngôn ngữ thường)

- Gọi `read_console_messages` với `onlyErrors: true` sau mỗi lần navigate/click
- Nếu có lỗi, **KHÔNG paste lỗi kỹ thuật** mà dịch sang ngôn ngữ người dùng:
  - TypeError/ReferenceError → "Trang bị lỗi kỹ thuật bên trong, có thể gây hiển thị sai"
  - Network Error/Failed to fetch → "Trang không lấy được dữ liệu từ server"
  - ChunkLoadError → "Trang không tải được một phần nội dung"
  - Unhandled Promise → "Một thao tác trên trang bị lỗi ngầm"
- Clear console (`clear: true`) trước khi navigate sang trang mới để tránh nhầm lẫn

### Bước 4 (Mode 3): So sánh website với logic brief

Chỉ chạy khi user cung cấp logic brief (file .md hoặc Notion page) và yêu cầu so sánh. Bước này thay thế hoặc bổ sung cho Bước 3 thông thường.

#### 4a. Đọc và trích xuất checklist từ logic brief

1. Đọc file logic brief (dùng `Read` tool hoặc fetch từ Notion)
2. Trích xuất **tất cả** UI elements và hành vi được mô tả, chia thành 2 loại:

**Danh sách A — Phần tử hiển thị** (những gì user nhìn thấy):
- Mỗi nút bấm, icon, link được nhắc đến
- Mỗi vùng nội dung (header, body, footer, action bar...)
- Badge, tag, label, tooltip
- Empty state, loading state
- Media gallery, avatar, platform icon
- Bảng dữ liệu, metric, số liệu

**Danh sách B — Hành vi tương tác** (những gì xảy ra khi thao tác):
- Click nút → popup/drawer mở
- Click sort → thứ tự thay đổi
- Hover → tooltip hiện
- Text dài → truncate + "Show More"
- Điều kiện hiện/ẩn (ví dụ: "chỉ hiện khi text >= 800 ký tự")

Ghi ra danh sách rõ ràng, đánh số — đây là checklist để đối chiếu.

#### 4b. Chiều 1: Logic → Website (thiếu gì?)

Với mỗi item trong checklist:
1. Mở đúng trang/panel trên website
2. Tìm phần tử tương ứng (bằng `read_page`, `find`, hoặc mắt)
3. Nếu là hành vi → thực hiện thao tác (click, hover, nhập text) và chụp screenshot
4. Đánh dấu: ✅ Khớp | ⚠️ Khác biệt (mô tả) | ❌ Thiếu hoàn toàn

#### 4c. Chiều 2: Website → Logic (thừa gì?)

**Đây là bước hay bị bỏ sót** — phải làm kỹ:

1. Dùng `read_page` filter `"interactive"` để lấy **tất cả** phần tử tương tác trên trang/panel hiện tại
2. Dùng `read_page` filter `"all"` hoặc chụp screenshot chi tiết từng vùng để tìm phần tử không tương tác (badge, label, icon decorative)
3. Liệt kê TẤT CẢ phần tử tìm được trên website
4. Đối chiếu từng phần tử với checklist logic brief:
   - Có trong logic → đã check ở bước 4b, bỏ qua
   - **Không có trong logic** → ghi nhận là "Phần tử thừa / chưa document"

**Khu vực hay có phần tử thừa** (cần kiểm tra kỹ):
- **Action bar** (thanh icon cuối mỗi card/row) — thường có 3-5 icon nhưng logic chỉ nhắc 1-2
- **Panel/Drawer header** — có thể chứa nút AI, sort, filter mà logic quên mô tả
- **Conditional UI** — phần tử chỉ hiện khi thỏa điều kiện (text dài, engagement cao, v.v.)
- **Tooltip content** — hover vào element hiện tooltip chứa thông tin quan trọng
- **Context menu / More actions** — nút "⋮" thường mở menu phụ với nhiều lựa chọn

5. Với mỗi phần tử thừa, mô tả:
   - Vị trí trên màn hình
   - Hình dạng / nội dung (icon gì, chữ gì)
   - Khi click/hover có gì xảy ra (test thử nếu có thể)

#### 4d. Báo cáo so sánh

Dùng format riêng cho Mode 3 (xem phần "Format báo cáo — Mode 3" bên dưới).

---

### Bước 5 (Tùy chọn): So sánh với bản cũ

Chỉ khi user yêu cầu so sánh UI với phiên bản cũ và cung cấp URL/path bản cũ:
1. Mở bản cũ ở tab riêng
2. Navigate đến cùng trang
3. Chụp screenshot cả hai
4. So sánh và chỉ ra khác biệt bằng ngôn ngữ mô tả vị trí

## Format báo cáo

Báo cáo trực tiếp trong chat, dùng ngôn ngữ đơn giản:

```
## Kết quả test: [Tên website hoặc "Toàn bộ website"]

Đã test: X trang | Phát hiện: Y lỗi

---

### Trang: [tên trang]

✅ Giao diện: OK
✅ Scroll: Không có thanh cuộn ngang bất thường
⚠️ Chức năng: 2 lỗi
❌ Lỗi kỹ thuật: 1 lỗi

**Lỗi tìm được:**

1. 🔴 **Nút "Thêm mới" không hoạt động**
   Vị trí: Góc trên bên phải, nút màu xanh
   Hiện tượng: Bấm vào không có phản hồi gì
   [kèm screenshot]

2. 🟡 **Bảng dữ liệu trống**
   Vị trí: Giữa trang, dưới bộ lọc
   Hiện tượng: Bảng hiện "No data" dù chưa lọc gì
   [kèm screenshot]

3. 🟡 **Trang bị lỗi kỹ thuật bên trong**
   Hiện tượng: Có lỗi ngầm khi mở trang, có thể ảnh hưởng hiển thị

---

### Tổng kết
- 🔴 Nghiêm trọng: X lỗi (trang trắng, chức năng chính hỏng)
- 🟡 Cần sửa: Y lỗi (hiển thị sai, chức năng phụ)
- 🟢 Nhẹ: Z ghi chú (khác biệt nhỏ, có thể cải thiện)
```

### Format báo cáo — Mode 3 (So sánh logic brief)

```
## Kết quả so sánh: [Tên trang/panel] vs Logic Brief

### Chiều 1: Logic → Website (logic mô tả → website có không?)

Tổng: X items | ✅ Khớp: Y | ⚠️ Khác: Z | ❌ Thiếu: W

| # | Phần tử / Hành vi | Kết quả | Ghi chú |
|---|---------------------|---------|---------|
| 1 | Nút "AI Summarize" trong header | ✅ Khớp | |
| 2 | Sort dropdown 4 options | ⚠️ Khác | Chỉ có 3 options thay vì 4 |
| 3 | Empty state khi không có data | ❌ Thiếu | Trang hiện trắng thay vì message |

### Chiều 2: Website → Logic (website có → logic nhắc chưa?)

Phát hiện: N phần tử CHƯA có trong logic brief

| # | Phần tử trên website | Vị trí | Mô tả |
|---|----------------------|--------|-------|
| 1 | Nút "⋮" (More actions) | Action bar, icon thứ 2 từ phải | Click chưa test được — có thể là placeholder |
| 2 | Tooltip "Discussion too short..." | Icon AI trên card ngắn | Hiện khi hover vào icon AI mờ |

### Tổng kết
- ✅ Khớp hoàn toàn: X items
- ⚠️ Khác biệt cần review: Y items
- ❌ Logic mô tả nhưng website thiếu: Z items
- 🔵 Website có nhưng logic chưa nhắc: N items

→ Đề xuất: cập nhật logic brief để bổ sung N phần tử thừa? Hay đây là bug cần xóa khỏi website?
```

---

## Mức độ lỗi — giải thích đơn giản

- 🔴 **Nghiêm trọng**: Trang trắng, trang crash, chức năng chính không dùng được, không hiển thị dữ liệu gì cả
- 🟡 **Cần sửa**: Giao diện lệch, một phần nào đó không hiển thị đúng, chức năng phụ bị hỏng, popup không mở
- 🟢 **Nhẹ**: Giao diện hơi khác thường nhưng vẫn dùng được, khoảng cách giữa các phần không đều, góp ý cải thiện

## Lưu ý quan trọng khi chạy

1. **Chụp ảnh nhiều** — mỗi trang ít nhất 1 ảnh, mỗi thao tác 1 ảnh. Ảnh là cách tốt nhất để user thấy lỗi.

2. **Scroll xuống** — nhiều lỗi nằm ở phần dưới trang mà không scroll sẽ bỏ sót.

3. **Clear console giữa các trang** — tránh báo nhầm lỗi trang A cho trang B.

4. **Không giả định cấu trúc** — mỗi project khác nhau, luôn khám phá navigation trước khi test.

5. **Hỏi lại khi mơ hồ** — nếu không chắc cái gì đó là bug hay feature, hỏi user thay vì đoán.

6. **Test chuyển trang/mục** — nếu website có sidebar với nhiều mục (ví dụ danh sách topic, danh sách project), hãy click sang mục khác rồi quay lại. Nhiều bug chỉ xuất hiện khi chuyển đổi (vị trí scroll không reset, bộ lọc không xóa, dữ liệu cũ còn hiển thị).

7. **Chú ý CSS Grid** — nếu trang dùng lưới 2 cột (grid), nội dung dài trong 1 cột có thể tràn ngang. Đây là lỗi rất phổ biến mà chỉ overflow check (Kiểm tra 3) mới phát hiện được — mắt thường có thể không thấy nếu thanh cuộn ngang nhỏ.

8. **Mode 3 — luôn check cả 2 chiều** — khi so sánh logic brief với website, rất dễ chỉ check chiều "logic có trên website không?" mà quên check chiều ngược "website có gì logic chưa nhắc?". Chiều ngược này là nơi hay bị bỏ sót nhất — đặc biệt action bar icons, conditional UI, và tooltip content. Phải dùng `read_page` filter interactive để lấy danh sách phần tử thực tế, không chỉ dựa vào mắt nhìn screenshot.

## Ví dụ cách gọi

- "test website cho tôi" → Mode 1: Scan toàn bộ
- "test trang Creator" → Mode 2: Test 1 trang cụ thể
- "xem trang Dashboard có ổn không" → Mode 2: Test Dashboard
- "so sánh giao diện với bản cũ" → Test + so sánh bản cũ
- "website có bug gì không" → Mode 1: Full scan tìm bug
- "bấm thử các nút trên trang Mission xem" → Mode 2: Focus vào functional check
- "test theo logic brief" → Mode 3: So sánh website vs logic brief
- "kiểm tra xem website có khớp logic không" → Mode 3
- "so sánh panel Message với file brief-logic.md" → Mode 3: Test 1 panel cụ thể
- "logic có khớp website không" → Mode 3: Bidirectional check
