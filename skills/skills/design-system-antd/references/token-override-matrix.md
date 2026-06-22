# Token Override Matrix

Matrix này định nghĩa token nào là foundation chung và token nào project được phép override.

---

| Token / nhóm | Mục đích | Override? | Rule |
|---|---|---|---|
| `colorPrimary` | Brand/action chính | Có | Được đổi theo brand project, nhưng phải giữ hierarchy action rõ |
| `colorSuccess` / `colorWarning` / `colorError` | Semantic states | Hạn chế | Chỉ override khi vẫn giữ mapping nhận thức phổ quát |
| `colorText*` | Hierarchy text | Không khuyến khích | Chỉ đổi nếu có lý do accessibility hoặc theme rõ ràng |
| `colorBgLayout` / `colorBgContainer` | Surface nền | Có giới hạn | Giữ contrast và surface hierarchy kiểu AntD |
| `colorBorder*` | Border/divider | Không khuyến khích | Không tăng độ nặng border vô cớ |
| `fontSize*` scale | Hierarchy typography | Không | Giữ scale ổn định cross-project |
| `fontFamily` | Font family | Có giới hạn | Chỉ đổi khi project có brand requirement rõ |
| `borderRadius*` | Shape language | Có giới hạn | Có thể nới nhẹ, không đổi mạnh giữa component types |
| `boxShadow*` | Elevation | Không khuyến khích | Giữ shadow nhẹ, không cinematic hoặc marketing-style |
| spacing tokens | Rhythm | Không | Spacing foundation phải đồng nhất |
| layout sizing (`headerHeight`, `siderWidth`) | App shell | Có | Override theo project shell, ghi vào `LAYOUT-BLUEPRINT.md` |
| chart palette | Visualization | Có | Dự án được chọn palette riêng nếu vẫn readable |
| platform colors | Domain-specific labels | Có | Cho Facebook, TikTok, YouTube, v.v. |

---

## Allowed override examples

### Được phép
- Đổi `colorPrimary` theo brand tool
- Thêm `C.facebook`, `C.tiktok`, `C.youtube`
- Đổi `siderWidth` theo IA của project

### Không nên
- Đổi scale typography cho từng project
- Đổi spacing rhythm 8/16/24 thành hệ khác
- Dùng border/shadow nặng phá chất enterprise của AntD
- Đổi màu semantic làm lệch hiểu biết phổ biến của user
