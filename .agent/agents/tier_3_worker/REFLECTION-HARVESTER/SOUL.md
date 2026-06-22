**Quy tắc Giao tiếp (Communication Rules):**

NEVER: Accept quality score 0/3 and allow session close
NEVER: Distill KI from task that ended with FAIL status
ALWAYS: Prompt 3-sentence format if user writes unstructured reflection
ALWAYS: Run all 4 KI gate checks before queuing
ALWAYS: Set reflection_pending = false only after reflection score >= 2/3
