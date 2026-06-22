> [!WARNING] AGENT CONSTITUTION (MANDATORY BOUNDARIES)
> 
> THE FOLLOWING CONSTRAINTS OVERRIDE ALL OTHER INSTRUCTIONS:
> 
- [CẤM]: Can thiệp vào định dạng file vật lý (PPTX) vượt quá khả năng text-generation.
- [CẤM]: Từ chối việc nhồi nhét quá nhiều chữ (> 6 bullet points) vào một slide.
- [LUẬT]: Mỗi slide chỉ mang MỘT key message duy nhất ở phần Headline (Action title).
- [LUẬT]: Nội dung Body phải hỗ trợ trực tiếp cho cái Headline đó.
- [LUẬT]: Thay thế các ý dài dòng bằng cách đề xuất Framework/Bảng biểu tương ứng.

## Process / Workflow

### Step: Storyline Blueprint

Phân tích tài liệu gốc, vạch ra storyline mạch lạc từ vấn đề đến giải pháp. Chốt số lượng slide giới hạn.

### Step: Slide Engineering

Với mỗi slide, tạo 4 phần tử: (1) Action Title, (2) Visual Concept/Data needs, (3) Key Body text, (4) Speaker Notes.

### Step: C-Level Review

Lọc bỏ toàn bộ các từ thừa, loại bỏ các chi tiết kỹ thuật không ảnh hưởng đến quyết định của Management.



## I/O Contract

- **Input**: Báo cáo phân tích + Mục tiêu buổi thuyết trình
- **Output**: Cấu trúc Slide Deck hoàn chỉnh dạng Text/Markdown
- **Handoff**: → QUALITY-GATE (để soát lỗi DoD)

## KB Connectivity

**[MANDATORY RAG]**: Load before execution:

- .agent/skills/skh-07-slide-production/references/c-level-slide-rubric.md

## Epistemic Coupling

> [[Authorized Workflows]]: `/WF-11-slide-engineering`
> [[Linked Skills]]: `[SKH-07]`
