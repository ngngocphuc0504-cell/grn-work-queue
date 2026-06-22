# Spec Taxonomy

`write-specs` chỉ dùng 5 page roles. Không tự invent thêm role mới nếu chưa có lý do mạnh từ local subtree.

## 1. `catalog`

### Dấu hiệu nhận biết

- page đứng ở đầu cây docs của một product hoặc domain;
- nhiệm vụ chính là route người đọc;
- có canonical order hoặc module list;
- không giữ toàn bộ truth chi tiết của từng module.

### Dùng để

- giới thiệu module map;
- nêu reading order;
- chỉ boundary ở level product.

### Không dùng để

- mô tả business rules chi tiết;
- thay cho module owner page;
- nhét hidden surfaces của từng module.

## 2. `navigation-group`

### Dấu hiệu nhận biết

- page đại diện cho một nhóm menu hoặc nhóm settings;
- tree con thường chứa nhiều module thật bên dưới;
- bản thân page cha không phải business surface độc lập.

### Dùng để

- giải thích vì sao nhóm menu này tồn tại;
- nêu thứ tự menu;
- route sang child specs đúng.

### Không dùng để

- mô tả sâu từng child module;
- trộn rule của nhiều child vào cùng một page cha;
- giả vờ coi page cha là một module nghiệp vụ riêng.

## 3. `shared-platform`

### Dấu hiệu nhận biết

- page mô tả app shell, pattern dùng chung, global rule, hoặc shared infrastructure;
- nội dung áp dụng cho nhiều module;
- không thuộc một business module cụ thể.

### Dùng để

- định nghĩa boundary của shared surfaces;
- gom global patterns như app shell, search, filter, toolbar, table actions;
- chỉ rõ khi nào module-spec cần link ngược về page này.

### Không dùng để

- thay cho từng module owner page;
- chứa logic nghiệp vụ đặc thù của từng module con.

## 4. `module-owner`

### Dấu hiệu nhận biết

- page đại diện cho một module hoặc major feature;
- là entry point chính để đọc truth của module;
- có thể có child pages nếu module lớn.

### Dùng để

- giữ overview, scope, boundary, flow chính, states, roles;
- route sang child pages;
- mô tả `data touchpoints` ở mức đủ hiểu hành vi.

### Không dùng để

- ôm hết chi tiết của mọi tab nếu module đã có child split rõ;
- thay cho changelog hay session notes.

## 5. `child-spec`

### Dấu hiệu nhận biết

- page con của `module-owner`;
- đi sâu vào một tab, sub-surface, flow phụ, hoặc detail area;
- chỉ nên mang phần truth thuộc surface đó.

### Dùng để

- mở sâu hidden surfaces và actions của từng tab;
- làm rõ states, triggers, validation, và boundary cục bộ;
- giữ detail để owner page không quá dày.

### Không dùng để

- lặp lại toàn bộ overview của module cha;
- copy metadata và prose dài từ owner page chỉ để đủ form.
