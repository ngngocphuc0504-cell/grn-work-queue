# Core Standards — Career Twin Workspace v1

> [!IMPORTANT] Override Priority: Tier 2

## Nguyên tắc vận hành không thể vi phạm

### STANDARD-01: Human First (Tuyệt đối)
Mọi agent PHẢI xác nhận `user_approach_stated = true` trước khi xử lý.
Nếu thiếu → trả về user với prompt: "Trước tiên, bạn muốn tiếp cận task này như thế nào?"

### STANDARD-02: Checkpoint Completeness
Mọi task quan trọng có 3 checkpoints. Không agent nào được advance
qua checkpoint chưa được user confirm.
`user_checkpoint_passed` phải = true trước khi handoff.

### STANDARD-03: Reflection Gate
Session KHÔNG được đóng khi `reflection_pending = true`.
REFLECTION-HARVESTER blocking call PHẢI hoàn thành trước WF-INF-02.

### STANDARD-04: Mode Discipline
Agent KHÔNG được thực thi bounded tasks nếu `co_work_mode = OBSERVE | COWORK`.
QUALITY-GATE kiểm tra mode trước khi kích hoạt Executor-Swarm.

### STANDARD-05: Zero-Floating Output
Mọi output quan trọng phải có file anchor với Genesis Header.
Output chỉ trong conversation history = vi phạm io-contract.

### STANDARD-06: Twin Separation
CPT, CST, FRT KHÔNG BAO GIỜ được merge thành một response.
TC-TWIN label rõ layer nào đang được tham chiếu trong mọi output.

### STANDARD-07: Immutability Respect
CPT files: READ-ONLY tuyệt đối trong runtime.
Governance files: READ-ONLY tuyệt đối.
FRT: chỉ update với explicit user confirmation string.

## Output Quality Standards

### Framed Brief Quality Bar
- Objective viết dưới dạng outcome (không phải activity)
- Stakeholder được identify rõ
- ≥3 assumptions được surface
- Scope in/out được phân biệt
- DoD có thể đo lường được

### Review Feedback Quality Bar
- Mỗi feedback item gắn với skill dimension cụ thể
- Evidence-based (trích từ artifact, không chung chung)
- Constructive direction (không chỉ "sai" mà "nên làm gì")
- Rubric score kèm theo (1-5 per relevant skill)

### Reflection Quality Bar
- 3 câu đủ (không thiếu câu nào)
- Mỗi câu có specific evidence
- Câu 3 có action intent cụ thể
