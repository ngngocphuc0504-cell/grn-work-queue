# MAS 5.0 Agent YAML Configuration Schema — Definitive Reference

> Tài liệu tham chiếu chính thức cho skill `mas5-agent-factory`.
> Agent PHẢI nạp file này trước khi sinh ra bất kỳ YAML config nào để đảm bảo schema compliance.

---

## 1. Core Rationale

Trong MAS 5.0, mỗi Agent không còn là 1 file Markdown đơn lẻ. Agent được phân mảnh thành 4 file nhận thức riêng biệt nằm trong 1 thư mục:

```text
[Agent-ID]/
├── INDEX.md      — Điều phối tổng, kéo context từ 3 file còn lại
├── IDENTITY.md   — Sứ mệnh, quyền hạn, ranh giới scope
├── SOUL.md       — Nhân cách, giọng điệu, motto
└── RULES.md      — Logic nghiệp vụ, I/O contract, epistemic coupling
```

Để tạo ra cấu trúc này một cách **deterministic** (không phụ thuộc vào LLM tự do viết Markdown), hệ thống sử dụng cơ chế **Schema-Driven Generation**: LLM chỉ xuất 1 file YAML config nhẹ, sau đó script Python đọc YAML và đúc ra 4 file chuẩn.

Tại sao YAML chứ không phải JSON?
- Claude sinh YAML chính xác hơn JSON (ít lỗi escape quotes)
- Con người đọc YAML dễ hơn khi review trước khi đúc
- YAML hỗ trợ multi-line string tự nhiên (cho mission dài, rules phức tạp)

---

## 2. Schema Definition (Execution Bounds)

### 2.1 Top-Level Structure

```yaml
agent_config:           # Root key — BẮT BUỘC
  meta:                 # Block 1 — Metadata hành chính
  identity:             # Block 2 — Sứ mệnh & phạm vi
  soul:                 # Block 3 — Nhân cách & giao tiếp
  operating_rules:      # Block 4 — Logic vận hành
```

Mọi file YAML sinh ra PHẢI có đúng 4 block con nằm dưới `agent_config`. Thiếu bất kỳ block nào → REJECT.

### 2.2 Block `meta` (Bắt buộc, 4 fields)

| Field | Type | Required | Constraint | Example |
|-------|------|----------|------------|---------|
| `id` | string | ✅ | Kebab-upper format: `[PREFIX]-[WNUM]-[SNUM]` hoặc `[PREFIX]-[WNUM]`. Không chứa dấu cách. | `GOV-W01-S03` |
| `name` | string | ✅ | Tên vai trò human-readable, ≤ 60 ký tự | `"Component Builder"` |
| `tier` | string | ✅ | Chỉ chấp nhận: `T2`, `T3`, `T4` | `"T4"` |
| `parent` | string | ✅ | ID của Agent cấp trên trực tiếp. T2 agent → parent = `"HUMAN"` | `"GOV-W01"` |

### 2.3 Block `identity` (Bắt buộc, 3 fields)

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `mission` | string | ✅ | ≥ 20 từ. Mô tả mục tiêu tối thượng. CẤM dùng placeholder. |
| `allowed_scope` | list[string] | ✅ | ≥ 2 items. Mỗi item bắt đầu bằng động từ hành động. |
| `forbidden_scope` | list[string] | ✅ | ≥ 1 item. Chỉ rõ các vùng đặc quyền của Agent/Tier khác. |

### 2.4 Block `soul` (Bắt buộc, 3 fields)

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `vibe` | string | ✅ | ≥ 10 từ. Mô tả phong cách giao tiếp đặc trưng. |
| `rules` | list[string] | ✅ | ≥ 2 items. Quy tắc giao tiếp cụ thể, imperative. |
| `motto` | string | ✅ | 1 câu châm ngôn hành động. ≤ 15 từ. |

### 2.5 Block `operating_rules` (Bắt buộc, 4 fields)

| Field | Type | Required | Constraint |
|-------|------|----------|------------|
| `steps` | list[{name, action}] | ✅ | ≥ 2 steps. Mỗi step phải có cả `name` và `action`. |
| `io_contract` | {input, output, handoff} | ✅ | Cả 3 sub-fields đều bắt buộc. |
| `mandatory_rag` | list[string] | Optional | Danh sách path tới KB files cần load trước khi chạy. |
| `epistemic_lines` | {authorized_workflows, linked_skills} | Optional | Wiring tới workflows và skills liên quan. |

---

## 3. Anti-Patterns (Cái CẤM Tuyệt Đối)

| Anti-Pattern | Ví dụ | Hậu quả |
|-------------|-------|---------|
| **AP-01: Placeholder Mission** | `mission: "Mô tả sau"` hoặc `mission: "TBD"` | Agent không biết mình tồn tại để làm gì → hallucinate scope |
| **AP-02: Empty Scope Lists** | `allowed_scope: []` | Agent mất ranh giới → can thiệp vào vùng đặc quyền của Agent khác |
| **AP-03: Generic Vibe** | `vibe: "Thân thiện"` | Không đủ differentiation → tất cả Agent nói giống nhau |
| **AP-04: Copy-Paste Steps** | Steps của Agent này trùng 100% với Agent khác | 2 Agent tranh nhau xử lý cùng 1 nhiệm vụ (resource collision) |
| **AP-05: Missing Handoff** | `handoff: ""` | Output bị "rơi" — không Agent nào nhận tiếp |
| **AP-06: ID Collision** | 2 Agent cùng `id: GOV-W01-S03` | Registry conflict, QUEUE routing sai Agent |
| **AP-07: Tier Mismatch** | `tier: T2` nhưng `parent: GOV-W01` (T3) | Vi phạm Hierarchy — con không thể cao hơn cha |

---

## 4. Validation Decision Tree

```text
START → Kiểm tra root key "agent_config"?
  ├─ NO  → REJECT: "Missing root key agent_config"
  └─ YES → Kiểm tra 4 blocks (meta, identity, soul, operating_rules)?
       ├─ Thiếu block nào → REJECT: "Missing block: [tên]"
       └─ Đủ 4 blocks → Kiểm tra Required Fields từng block
            ├─ Thiếu field → REJECT: "Missing field [block].[field]"
            └─ Đủ fields → Kiểm tra Constraints
                 ├─ mission < 20 từ → WARNING: "Mission quá ngắn"
                 ├─ allowed_scope < 2 items → REJECT: "Scope thiếu"
                 ├─ tier not in [T2,T3,T4] → REJECT: "Invalid tier"
                 ├─ steps < 2 → REJECT
                 └─ ALL PASS → ✅ VALID — Proceed to build
```
