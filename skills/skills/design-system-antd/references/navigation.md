# Navigation Patterns — Ant Design 6

> Tài liệu tham khảo: https://ant.design/docs/spec/navigation

---

## 1. MỤC TIÊU THIẾT KẾ

- Cung cấp đủ **gợi ý thị giác và ngữ cảnh** — tránh user bị lạc
- **Nhất quán** hình thức và hành vi — giảm cognitive load
- **Tối thiểu chuyển trang** — giảm số lần chuyển trang cần thiết cho 1 task

---

## 2. CÁC LOẠI NAVIGATION

### Side Navigation (phổ biến nhất cho Internal Tool)

Thanh menu dọc bên trái. Linh hoạt, mở rộng dễ dàng, phù hợp cấu trúc sâu.

```jsx
import { Layout, Menu } from "antd";

<Layout.Sider width={200}>
  <Menu
    mode="inline"
    selectedKeys={[currentPath]}
    openKeys={openKeys}
    onOpenChange={setOpenKeys}
    items={[
      {
        key: "creators",
        icon: <UserOutlined />,
        label: "Creator",
        children: [
          { key: "/creators/list", label: "Danh sách" },
          { key: "/creators/pending", label: "Chờ duyệt" },
        ],
      },
      {
        key: "missions",
        icon: <FlagOutlined />,
        label: "Mission",
        children: [
          { key: "/missions/list", label: "Danh sách" },
          { key: "/missions/create", label: "Tạo mới" },
        ],
      },
    ]}
    onClick={({ key }) => navigate(key)}
  />
</Layout.Sider>
```

**Quy tắc:**
- Menu depth tối đa **3 cấp** — sâu hơn gây khó navigate
- Menu item label **ngắn gọn** — 2–4 từ
- Dùng icon cho menu cấp 1 — giúp nhận diện nhanh
- `selectedKeys` sync với URL — user luôn biết đang ở đâu

### Top Navigation

Menu ngang phía trên. Layout gọn gàng nhưng giới hạn số lượng items.

```jsx
<Layout.Header>
  <Menu
    mode="horizontal"
    selectedKeys={[currentSection]}
    items={[
      { key: "dashboard", label: "Dashboard" },
      { key: "creators", label: "Creator" },
      { key: "missions", label: "Mission" },
      { key: "settings", label: "Cài đặt" },
    ]}
  />
</Layout.Header>
```

**Dùng khi:** Ít menu items (< 8), cấu trúc flat, không cần sub-menu sâu.

### Kết hợp Top + Side:

```
Top Nav:  Chọn module chính (Creator, Mission, Analytics, Settings)
Side Nav: Navigation chi tiết trong module đó
```

---

## 3. BREADCRUMB

Cho user biết vị trí hiện tại trong hierarchy.

```jsx
import { Breadcrumb } from "antd";

<Breadcrumb items={[
  { title: <a href="/">Trang chủ</a> },
  { title: <a href="/creators">Creator</a> },
  { title: "Chi tiết Creator" },  // Item cuối không có link
]} />
```

**Quy tắc:**
- Hiển thị tối đa **3 cấp** — sâu hơn thì ẩn bớt
- Item cuối cùng: **không có link** (vì đang ở đó)
- **Tránh dùng breadcrumb** khi trang đã có sidebar navigation rõ ràng — tránh redundancy
- Hữu ích nhất cho **detail pages** truy cập từ list page

---

## 4. TABS

Phân loại nội dung trong cùng trang — chuyển đổi nhanh giữa các view.

### Các kiểu Tabs:

| Kiểu | Dùng khi | Component |
|---|---|---|
| **Basic** (line) | Điều khiển nội dung toàn trang | `<Tabs>` |
| **Card** | Điều khiển phần trang, có border | `<Tabs type="card">` |
| **Pill** (nút) | Trong card, section nhỏ | `<Segmented>` |

```jsx
import { Tabs, Segmented } from "antd";

// Basic tabs — page level
<Tabs items={[
  { key: "overview", label: "Tổng quan", children: <Overview /> },
  { key: "missions", label: "Mission", children: <MissionList /> },
  { key: "rewards", label: "Reward", children: <RewardList /> },
]} />

// Segmented — filter/toggle trong card
<Segmented
  options={["Tất cả", "Đang chạy", "Đã kết thúc"]}
  onChange={(val) => setFilter(val)}
/>
```

**Quy tắc:**
- Tab label **ngắn gọn** — 1–3 từ
- Số lượng tabs: **3–7** là tối ưu
- Tab mặc định: chọn tab user cần thấy đầu tiên

---

## 5. STEPS

Hướng dẫn user thực hiện task theo workflow định sẵn.

```jsx
import { Steps } from "antd";

// Horizontal — 2–5 bước, title ngắn (< 12 ký tự)
<Steps
  current={currentStep}
  items={[
    { title: "Thông tin" },
    { title: "Cấu hình" },
    { title: "Xác nhận" },
  ]}
/>

// Vertical — nhiều bước, có description dài
<Steps
  direction="vertical"
  current={currentStep}
  items={[
    { title: "Tạo mission", description: "Nhập thông tin cơ bản" },
    { title: "Chọn creator", description: "Chọn nhóm creator tham gia" },
    { title: "Cài đặt reward", description: "Cấu hình phần thưởng" },
  ]}
/>
```

**Quy tắc:**
- Horizontal: **2–5 bước**, title < 12 ký tự
- Vertical: Đặt bên trái trang, vị trí cố định
- Cho phép quay lại bước trước
- Hiển thị trạng thái rõ ràng (done, current, upcoming)

---

## 6. PAGINATION

Phân trang cho data lớn.

```jsx
import { Table } from "antd";

<Table
  pagination={{
    current: page,
    pageSize: 20,
    total: totalCount,
    showSizeChanger: true,              // Cho phép đổi page size
    showTotal: (total) => `Tổng ${total} mục`,
    pageSizeOptions: [10, 20, 50, 100],
    onChange: (page, pageSize) => fetchData({ page, pageSize }),
  }}
/>
```

### Loại pagination:

| Loại | Dùng khi |
|---|---|
| **Full** (default) | Hầu hết table — user cần biết tổng số |
| **Simple** | Trong card, popup — ít hơn 10 trang |
| **Mini** | Trong card nhỏ, floating layer |
| **Load more** | Feed, timeline — không cần page number |

**Quy tắc:**
- **Default pageSize: 20** — cân bằng giữa data exposure và performance
- Nếu < 1 trang: **ẩn pagination**
- Luôn hiện `showTotal` — user biết có bao nhiêu data
- Cache vị trí scroll khi user quay lại từ detail page

---

## 7. QUY TẮC NAVIGATION CHO INTERNAL TOOL

1. **Side navigation là default** — phù hợp cấu trúc phức tạp của internal tool
2. **URL = trạng thái** — mỗi trang có URL riêng, user có thể bookmark/share
3. **Highlight active menu item** — user luôn biết đang ở đâu
4. **Collapse sidebar** — cho phép thu gọn sidebar để có thêm content space
5. **Consistent back behavior** — browser back button phải hoạt động đúng
6. **Deep link support** — URL chứa params filter/sort, share được
