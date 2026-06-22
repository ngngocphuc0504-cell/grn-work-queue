---
description: Tiếp nhận và đóng khung task mới — đảm bảo user approach-first trước khi twin tham gia.
---

# Workflow: WF-01 Task Intake & Framing

- **👤 Owner:** `[@TASK-FRAMER]` (via CTO routing)
- **🛠 Skill Target:** `[sga-01]`, `[skh-01]`

## Assigned Skills

> [!IMPORTANT]
> Bắt buộc phải Load các kỹ năng sau trước khi chạy luồng:
> - **`sga-01`**: Task Framing Methodology — đảm bảo 5-element framing protocol
> - **`skh-01`**: Work Framing Signal — đo lường user skill maturity qua chất lượng brief

## Goal & Governance Context

- **Purpose:** Biến mọi task ý tưởng thô thành framed brief chuẩn chỉnh — NHƯNG chỉ SAU KHI user đã tự state approach trước. Twin challenge thinking, không thay thế thinking.
- **Scope:** Chỉ cho phép tạo brief trong `outputs/{id}/project-brief.md`. KHÔNG được phép tự execute task.
- **Mode Required:** Any (OBSERVE: twin demo framing; COWORK+: collaborative framing)

## Execution Steps

### Step 1: Verify User Approach (CTO)

1. Check `user_approach_stated = true` trong user message
2. IF missing → Return prompt: "Trước tiên, approach của bạn với task này là gì?"
3. IF present → Proceed

### Step 2: Consult Twin for CST Context (TASK-FRAMER)

1. Query TC-TWIN: "What recurring patterns does user have with [task type]?"
2. Load CST snapshot từ `02_twin_memory/twin-current/` via view_file
3. Extract relevant pattern history để personalize challenge questions

### Step 3: Apply BA Consulting & Design Thinking (TASK-FRAMER)

1. Phân tích ngữ cảnh từ Step 1 & 2 để nhận diện: Đây là chữa triệu chứng (Symptom) hay chữa nguyên nhân gốc (Root-cause)?
2. Phân loại mức độ lặp (Frequency):
   - **Nếu là Ad-hoc (Làm 1 lần):** Cung cấp 2-3 Option giải quyết nhanh. Phân tích Rủi ro và Ưu/Nhược điểm cho từng Option.
   - **Nếu là Recurring (Lặp đi lặp lại):** Kích hoạt "Mồi hệ thống hóa". Đề xuất User đóng gói Task này thành một Skill hoặc Agent mới bằng cách sử dụng `WF-14-capability-upgrade`. Đưa thêm Option làm tay truyền thống để so sánh sự lãng phí.
3. Xuất trình BA Analysis cho User và **DỪNG LẠI CHỜ (WAIT)** User chốt Option.
4. Chỉ cất bước sang Step 4 khi User đã nói rõ họ chọn con đường nào.

### Step 4: Run 5-Element Framing Check (TASK-FRAMER)

1. Dựa trên Option User vừa chọn, verify presence of each element:
   - □ Objective stated as OUTCOME (not activity)
   - □ Stakeholders AND their Definition of Done identified
   - □ ≥3 assumptions explicitly surfaced
   - □ Scope boundary clear (what's IN, what's OUT)
   - □ DoD measurable and testable

### Step 5: Challenge 1 Assumption (TASK-FRAMER)

1. Select the riskiest assumption from Step 4
2. Ask: "Nếu assumption này sai, điều gì xảy ra?"
3. WAIT for user response before proceeding — do NOT auto-continue

### Step 6: Thay nghén Workspace & Chốt Brief (TASK-FRAMER)

1. User confirms each element — TASK-FRAMER drafts iteratively.
2. Apply Genesis Header to output file.
3. **MANDATORY WORKSPACE SCAFFOLDING:** Nếu là một Task/Project mới hoàn toàn, hệ thống BẮT BUỘC phải tạo một thư mục chuyên biệt tại `outputs/{project_id}/` với cấu trúc lõi:
   - `01_input/`: Lưu trữ các tài liệu đầu vào, reference, và yêu cầu gốc.
   - `02_process/`: Lưu trữ các bản nháp (drafts), research notes, và file trung gian.
   - `03_output/`: Chỉ chứa thành phẩm cuối cùng (Deliverables) đã nghiệm thu (DoD).
4. Save bản Brief v1 vào: `outputs/{project_id}/01_input/project-brief.md`.
5. Tuyệt đối KHÔNG ĐƯỢC tạo file bừa bãi ngoài root directory. Mọi file sinh ra trong quá trình thực thi tiếp theo đều phải nhét đúng vào thư mục tương ứng của Task đó.

### Step 7: Skill Signal Extraction

1. Extract SKH-01 (work_framing): score based on completeness + quality of user's own brief
2. Extract SKH-05 (ai_cowork): score based on whether user engaged vs skipped framing
3. Signal → SC-SKILL via CTO

## Audit & Metrics (Quality Gates)

- **Gate 1 (Brief Completeness):** All 5 framing elements present in final brief. Missing any = FAIL → loop to Step 3.
- **Gate 2 (User Confirmation):** User typed "Tôi xác nhận brief này" or equivalent → proceed.
- **Metrics:** Framing completeness score (0-5), assumption challenge engagement (boolean)

## Output Format

```text
📋 FRAMED BRIEF — [Project Name]

🎯 Objective: [Outcome statement]
👥 Stakeholders: [List] | DoD: [Criteria]
⚠️ Assumptions: [≥3 listed]
📐 Scope: IN: [list] | OUT: [list]
✅ DoD: [Measurable criteria]

💡 Challenged Assumption: [Which one + user's response]
```

## Troubleshooting

| Vấn đề | Xử lý |
|---------|--------|
| User refuses to state approach | CTO blocks entry. Log bypass_count +1. |
| User can't identify assumptions | TASK-FRAMER provides 3 common examples from CST patterns |
| Brief exceeds scope boundary | TASK-FRAMER splits into sub-tasks |
