# Validation Rules — Agent Factory Input Guardrails

> Tài liệu tham chiếu cho `mas5-agent-factory` skill.
> Chứa toàn bộ quy tắc kiểm tra lỗi input YAML trước khi đúc Agent.
> Agent PHẢI nạp file này khi thực thi Route VALIDATE.

---

## 1. Core Rationale

Validation là lớp phòng thủ đầu tiên chống **Ghost Agent** (Agent bị tạo ra nhưng thiếu sót cấu trúc, hoạt động bất thường). Mọi YAML config PHẢI đi qua validation gate trước khi script `build_agent.py` được phép chạy. Nguyên tắc: **REJECT sớm còn hơn đúc sai rồi phải xóa.**

---

## 2. Validation Rules Matrix

### 2.1 Structural Rules (SR)

| Rule ID | Field | Check | Severity | Action on Fail |
|---------|-------|-------|----------|----------------|
| SR-01 | Root | `agent_config` key tồn tại | CRITICAL | REJECT ngay lập tức |
| SR-02 | Root | Đúng 4 blocks: `meta`, `identity`, `soul`, `operating_rules` | CRITICAL | REJECT — báo block nào thiếu |
| SR-03 | `meta.id` | Không rỗng, không chứa dấu cách, chỉ A-Z, 0-9, và dấu gạch ngang | CRITICAL | REJECT |
| SR-04 | `meta.tier` | Giá trị thuộc tập `{T2, T3, T4}` | CRITICAL | REJECT |
| SR-05 | `meta.name` | ≤ 60 ký tự, không rỗng | MAJOR | WARNING + auto-truncate |
| SR-06 | `meta.parent` | Không rỗng. Nếu `tier=T2` → parent PHẢI = `"HUMAN"` | MAJOR | REJECT nếu T2 mà parent ≠ HUMAN |

### 2.2 Content Quality Rules (CQ)

| Rule ID | Field | Check | Severity | Action on Fail |
|---------|-------|-------|----------|----------------|
| CQ-01 | `identity.mission` | ≥ 20 từ (word count) | MAJOR | WARNING — yêu cầu LLM mở rộng |
| CQ-02 | `identity.mission` | Không chứa placeholder: `"TBD"`, `"TODO"`, `"Mô tả sau"`, `"..."` | CRITICAL | REJECT |
| CQ-03 | `identity.allowed_scope` | ≥ 2 items trong list | MAJOR | REJECT |
| CQ-04 | `identity.forbidden_scope` | ≥ 1 item trong list | MAJOR | REJECT |
| CQ-05 | `soul.vibe` | ≥ 10 từ | MINOR | WARNING |
| CQ-06 | `soul.rules` | ≥ 2 items | MAJOR | REJECT |
| CQ-07 | `soul.motto` | ≤ 15 từ, không rỗng | MINOR | WARNING — auto-trim |
| CQ-08 | `operating_rules.steps` | ≥ 2 steps, mỗi step có cả `name` và `action` | CRITICAL | REJECT |
| CQ-09 | `operating_rules.io_contract` | 3 sub-fields (`input`, `output`, `handoff`) đều không rỗng | CRITICAL | REJECT |

### 2.3 Uniqueness & Collision Rules (UC)

| Rule ID | Check | Severity | Action on Fail |
|---------|-------|----------|----------------|
| UC-01 | `meta.id` chưa tồn tại trong thư mục `dest` (destination) | CRITICAL | REJECT — báo collision |
| UC-02 | `meta.id` khác với ID của `meta.parent` | CRITICAL | REJECT — self-reference loop |
| UC-03 | Tier hợp lệ theo hierarchy: T4 phải có parent T3, T3 phải có parent T2 | MAJOR | WARNING — ghi log |

### 2.4 Hierarchy Coherence Rules (HC)

| Rule ID | Check | Severity | Action on Fail |
|---------|-------|----------|----------------|
| HC-01 | Nếu `tier=T4` → `parent` PHẢI là ID kết thúc bằng `W[0-9]+` (Worker-level) | MAJOR | WARNING |
| HC-02 | Nếu `tier=T3` → `parent` PHẢI thuộc Coordinator hoặc `HUMAN` | MAJOR | WARNING |
| HC-03 | `steps` không trùng lặp `name` trong cùng 1 config | MINOR | WARNING |

---

## 3. Error Response Protocol

Khi validation fail, Agent PHẢI:
1. **Dừng ngay** — không gọi `build_agent.py`
2. **Hiển thị bảng lỗi** có cấu trúc:

```markdown
## ❌ Validation Failed

| Rule | Field | Issue | Fix Required |
|------|-------|-------|--------------|
| SR-03 | meta.id | Chứa dấu cách: "GOV W01" | Đổi thành "GOV-W01" |
| CQ-02 | identity.mission | Chứa placeholder "TBD" | Viết mission thật |
```

3. **Đề xuất sửa** — cung cấp YAML đã sửa nếu lỗi có thể auto-fix (SR-05, CQ-05, CQ-07)
4. **Yêu cầu user xác nhận** — trước khi re-validate lần 2

---

## 4. Severity Escalation Matrix

| Severity | Count Threshold | Escalation |
|----------|----------------|------------|
| CRITICAL | ≥ 1 | Hard REJECT. Không đúc. |
| MAJOR | ≥ 3 | Soft REJECT. Yêu cầu review toàn bộ config. |
| MINOR | Any | WARNING only. Vẫn cho phép đúc nhưng ghi log. |
| CRITICAL + MAJOR combo | Any | Hard REJECT + đề xuất viết lại config từ đầu. |
