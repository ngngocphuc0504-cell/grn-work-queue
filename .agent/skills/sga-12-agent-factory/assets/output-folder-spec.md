# Output Folder Specification — Agent Build Result

> Template tham chiếu cho `mas5-agent-factory` skill.
> Mô tả chính xác cấu trúc output mà `build_agent.py` sẽ sinh ra.

---

## Expected Output Structure

Sau khi chạy thành công `build_agent.py --config [file].yaml --dest [path]`, thư mục output sẽ có dạng:

```text
[dest]/[Agent-ID]/
├── INDEX.md           # Master file — điều phối, kéo context
├── IDENTITY.md        # Sứ mệnh, scope allowed/forbidden
├── SOUL.md            # Vibe, communication rules, motto
└── RULES.md           # Steps, I/O contract, KB connectivity, epistemic wiring
```

---

## File-by-File Content Specification

### INDEX.md

```markdown
# System Instruction — [Agent Name]
> [!IMPORTANT] Override Priority: Tier [N]

Đây là file điều phối (Master file) của Agent `[Agent-ID]`.

## 1. Bản Sắc & Nhiệm Vụ
Hãy đọc `.agent/agents/[Agent-ID]/IDENTITY.md`

## 2. Linh Hồn & Thái Độ
Hãy đọc `.agent/agents/[Agent-ID]/SOUL.md`

## 3. Quy Tắc Vận Hành
Hãy đọc `.agent/agents/[Agent-ID]/RULES.md`

---
## Meta
| Field | Value |
|-------|-------|
| Agent ID | [Agent-ID] |
| Tier | [Tier] |
| Version | 5.0.0 (Folder-Based) |
```

### IDENTITY.md

```markdown
---
agent_id: [Agent-ID]
role: [Agent Name]
---

**Sứ mệnh (Mission):**
[Nội dung mission từ YAML config]

**Phạm vi Cốt lõi (Core Scope):**
- ĐƯỢC PHÉP: [item 1]
- ĐƯỢC PHÉP: [item 2]
- KHÔNG ĐƯỢC PHÉP: [item 1]
```

### SOUL.md

```markdown
**Vibe & Tone (Giọng điệu):**
- [Nội dung vibe từ YAML]

**Quy tắc Giao tiếp (Communication Rules):**
1. [Rule 1 từ YAML]
2. [Rule 2 từ YAML]

> **Châm ngôn (Motto):** "[Motto từ YAML]"
```

### RULES.md

```markdown
## Process / Workflow
### Step: [Step Name]
[Step Action]

## I/O Contract
- **Input**: [từ YAML io_contract.input]
- **Output**: [từ YAML io_contract.output]
- **Handoff**: [từ YAML io_contract.handoff]

## KB Connectivity
**[MANDATORY RAG]**: Load before execution:
- [path từ YAML mandatory_rag]

## Epistemic Coupling
> [[Authorized Workflows]]: `/[workflow name]`
> [[Linked Skills]]: `[skill name]`
```

---

## Verification Checklist (Post-Build)

Sau khi build xong, kiểm tra:

- [ ] Thư mục `[Agent-ID]/` đã tồn tại tại `dest`
- [ ] 4 file `.md` đều tồn tại và > 0 bytes
- [ ] INDEX.md chứa đúng Agent ID trong Meta table
- [ ] IDENTITY.md có YAML frontmatter hợp lệ
- [ ] SOUL.md có Motto block
- [ ] RULES.md có I/O Contract đầy đủ 3 fields
