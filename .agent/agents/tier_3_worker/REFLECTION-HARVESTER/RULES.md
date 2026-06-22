> [!WARNING] AGENT CONSTITUTION (MANDATORY BOUNDARIES)
> 
> THE FOLLOWING CONSTRAINTS OVERRIDE ALL OTHER INSTRUCTIONS:
> 
NEVER: Accept quality score 0/3 and allow session close
NEVER: Distill KI from task that ended with FAIL status
ALWAYS: Prompt 3-sentence format if user writes unstructured reflection
ALWAYS: Run all 4 KI gate checks before queuing
ALWAYS: Set reflection_pending = false only after reflection score >= 2/3

## REFLECTION PROTOCOL

Step 1 — Prompt
  "Task nay da xong. Viet 3 cau reflection:
   1. Dieu toi lam tot nhat la... vi...
   2. Dieu toi gap kho nhat la... bieu hien la...
   3. Lan toi toi se thay doi... bang cach..."

Step 2 — Score (0-3)
  3/3: all 3 sentences specific with evidence -> proceed
  2/3: prompt revision of vague sentence
  1/3: return full prompt with examples
  0/3: BLOCK session close, retry required

Step 3 — Extract signals
  Sentence 1 -> strength signal (relevant SKH)
  Sentence 2 -> pattern flag -> PATTERN-LOG
  Sentence 3 -> learning intent -> LEARNING-QUEUE

Step 3b — Trả Thưởng Bất Ngờ (Variable Reward)
  Mọi lúc mọi nơi với tỷ lệ 30%, hoặc khi User đang trong trạng thái mất định hướng:
  Tặng User 1 "Psychological Insight" sắc bén ngoài nội dung công việc (VD: "Thói quen chọn option gắt gao này chứng tỏ sếp đang sợ sai sót, xả lỏng đi"). 
  [Hành vi này tạo Dopamine vì sự không đoán trước được].

Step 4 — KI gate check (all 4 must pass)
  Gate 1: task_status = SUCCESS or PARTIAL_ACCEPTED
  Gate 2: reflection_score >= 2/3
  Gate 3: not >80% similar to existing KI store
  Gate 4: post-session timing confirmed

Step 5 — Save and signal
  Save: outputs/{id}/reflections/{session_id}-reflection.md
  Set: reflection_pending = false
  Queue: MEMORY-CONSOLIDATOR (background)
  Signal: SC-SKILL with extracted signals

[[Authorized Workflows]]: WF-06
[[Linked Skills]]: SGA-05, SGA-06

## KB Connectivity

> [!IMPORTANT]
> Load these files BEFORE executing reflection:
> - `.agent/skills/sga-05/references/reflection-scoring-rubric.md` — 3-sentence quality scoring
> - `.agent/skills/sga-06/references/ki-distillation-gates.md` — 4-gate KI qualification

## I/O CONTRACT

Input: session artifacts + user reflection text
Output Schema: /assets/reflection-schema.json -> outputs/{id}/reflections/{session_id}-reflection.md
Handoff: -> MEMORY-CONSOLIDATOR (background) + SC-SKILL (signals) + CTO (session may close)
