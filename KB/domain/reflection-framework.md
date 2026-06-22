# Reflection Framework

## The 3-Sentence Reflection (mandatory after every task)

```
Sentence 1 — WHAT WORKED:
"Trong task này, điều tôi làm tốt nhất là [X] vì [evidence]."

Sentence 2 — WHAT FAILED:
"Điều tôi gặp khó khăn nhất là [Y] — biểu hiện là [specific moment]."

Sentence 3 — NEXT CHANGE:
"Lần tới tôi sẽ thay đổi [Z] cụ thể bằng cách [action]."
```

## Reflection Quality Rubric (scored by REFLECTION-HARVESTER)

| Score | Criteria |
|-------|---------|
| 3/3 | Cả 3 câu có specific evidence, không chung chung |
| 2/3 | 2 câu specific, 1 câu vague |
| 1/3 | Chung chung, không có evidence — twin prompts for rewrite |
| 0/3 | Không submit — session BLOCKED from closing |

## Skill Signals from Reflection

REFLECTION-HARVESTER extracts:
- **Pattern flag:** Recurring failure mode? → add to CST PATTERN-LOG
- **Strength signal:** Consistent strength? → reinforce in CST
- **Learning intent:** Next change stated? → add to LEARNING-QUEUE
- **KI candidate:** Generalizable insight? → queue for MEMORY-CONSOLIDATOR

## Extended Reflection (weekly, optional)
Once per week, user can write extended reflection:
- Kỹ năng nào tôi thấy tiến bộ rõ nhất?
- Pattern nào tôi vẫn đang lặp lại?
- Khoảng cách lớn nhất giữa tôi hiện tại và FRT của tôi là gì?
- Tôi muốn twin tập trung challenge tôi ở điều gì tuần tới?
