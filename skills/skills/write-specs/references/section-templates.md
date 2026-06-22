# Section Templates

Các template này là khung mặc định. Nếu local subtree đã có convention riêng, local convention thắng.

## `catalog`

### Khung gợi ý

1. Metadata block
2. `Tổng quan`
3. `Reading Order` hoặc `Module Map`
4. `Boundary`

### Vai trò

- route người đọc tới page đúng;
- làm rõ page nào giữ truth chi tiết;
- giữ page mỏng, không nhồi business detail.

## `navigation-group`

### Khung gợi ý

1. Metadata block
2. `Tổng quan`
3. `Thứ tự menu`
4. `Boundary`

### Vai trò

- giải thích nhóm menu;
- route sang các child modules;
- nhắc reader không dùng page cha này như business truth riêng.

## `shared-platform`

### Khung gợi ý

1. Metadata block
2. `Reading Order`
3. `Boundary Rule`
4. `Global Surfaces Covered`
5. `Update Trigger`

### Vai trò

- định nghĩa shared shell hoặc global patterns;
- tránh để business module lặp lại cùng một rule ở nhiều page.

## `module-owner`

### Khung gợi ý

1. Metadata block
2. `Tổng quan`
3. `Scope / Boundary`
4. `Reading Order` hoặc `Main Surfaces`
5. `Luồng chính`
6. `Roles / permissions`
7. `States / actions / triggers`
8. `Data touchpoints`
9. `Upstream / downstream`
10. `Edge cases / non-goals`
11. `Companion pages`

### Vai trò

- là entry point chính của module;
- tóm tắt đủ để PM, FE, BE, QA biết module làm gì;
- route sang child pages khi cần deeper read.

## `child-spec`

### Khung gợi ý

1. Metadata block
2. `Tổng quan`
3. `Surface covered`
4. `Flow / interaction`
5. `States / actions / triggers`
6. `Data touchpoints`
7. `Dependencies / companion pages`
8. `Edge cases / non-goals`

### Vai trò

- đi sâu đúng vào một tab hoặc sub-surface;
- không lặp lại full overview của module cha;
- chỉ giữ truth cần cho surface đó.
