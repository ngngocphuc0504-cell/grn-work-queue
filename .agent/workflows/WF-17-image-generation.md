---
description: Workflow để gọi sinh ảnh/đồ họa thương hiệu theo quy chuẩn Brand Identity.
---

# Workflow: Image Generation (WF-17)

## Goal & Governance Context
**Purpose:** Generate high-quality, brand-aligned visual assets (carousels, diagrams, icons, headers) for Content Factory publications while maintaining structural logging.
**Scope:** Active operational workflow triggered by explicit user prompt or during execution phases.

- **👤 Owner:** `[@CONTENT-WRITER]` or `[@QUALITY-GATE]`
- **🛠 Skill Target:** `[sga-17-image-generator]`

## Steps

### Step 1: Intake & Parse Requirements
- Parse the user's prompt (e.g. subject, layout, target channel).
- Check if aspect ratio and style are specified. If not, follow the default style and aspect ratio matching rules defined in [image-gen-sop.md](file:///c:/antigravity%20prjs/MAS-Lean-1/managed_workspaces/ws-default-career-twin/ws-default-career-twin/.agent/skills/sga-17-image-generator/references/image-gen-sop.md).

### Step 2: Prompt Optimization & Quality Check
- Apply [image-gen-sop.md](file:///c:/antigravity%20prjs/MAS-Lean-1/managed_workspaces/ws-default-career-twin/ws-default-career-twin/.agent/skills/sga-17-image-generator/references/image-gen-sop.md) rules to strip out banned LLM quality booster words.
- Inject specific lighting terms, materials (matte clay, glassmorphic), camera lens details, or color themes matching the brand guidelines.

### Step 3: Tool Invocation
- Invoke `nanobanana.generate_image` (if MCP is connected) or fallback to `generate_image` tool.
- Supply optimized prompt and exact target width/height dimensions.

### Step 4: Asset Logging & Verification
- Save the resulting image under `content_factory/assets/images/` using the date prefix format.
- Output the image as a markdown block.
- Log the generation metadata, ensuring it matches the JSON validation schema in [image-metadata-schema.json](file:///c:/antigravity%20prjs/MAS-Lean-1/managed_workspaces/ws-default-career-twin/ws-default-career-twin/.agent/skills/sga-17-image-generator/assets/image-metadata-schema.json).
