# Skill Signal Specification

## What is a Skill Signal?

Skill Signal là dữ liệu đo lường năng lực được trích tự động từ:
1. Task artifact quality (rubric-scored by REVIEW-COACH)
2. Co-work compliance (checkpoint completion rate)
3. Reflection quality (REFLECTION-HARVESTER assessment)

## 5-Dimension Rubric (per skill)

| Level | Description | Evidence |
|-------|------------|---------|
| 1 | Làm theo hướng dẫn | Cần twin dẫn từng bước |
| 2 | Dùng template đúng | Áp dụng framework với ít sai sót |
| 3 | Tự framing/analysis khá ổn | Chủ động, ít cần nhắc nhở |
| 4 | Phản biện twin, tối ưu workflow | Chất vấn twin output, propose improvements |
| 5 | Tự thiết kế cách làm mới | Tạo ra approach mới phù hợp context |

## Signal Generation per Task

```json
{
  "task_id": "string",
  "session_id": "string",
  "signals": {
    "skh_01_work_framing": { "delta": 0.0, "evidence": "string" },
    "skh_02_evidence_reasoning": { "delta": 0.0, "evidence": "string" },
    "skh_03_execution_control": { "delta": 0.0, "evidence": "string" },
    "skh_04_communication": { "delta": 0.0, "evidence": "string" },
    "skh_05_ai_cowork": { "delta": 0.0, "evidence": "string" }
  },
  "compliance_score": 0.0,
  "reflection_submitted": true,
  "generated_at": "ISO-8601"
}
```

## Aggregation Rules

- Skill Maturity Index = rolling weighted average (last 10 tasks per skill)
- Weight: recent tasks × 1.5, older tasks × 1.0
- Update frequency: after every task completion (background)
- Minimum tasks before stable reading: 5 per skill dimension
