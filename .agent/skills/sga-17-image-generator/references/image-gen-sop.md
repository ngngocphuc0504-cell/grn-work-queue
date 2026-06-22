# Brand Visual Identity & Image Generation Standard Operating Procedure (SOP)

This reference document defines the official visual standards and prompt-engineering guidelines for creating graphic assets in the OAC Content Factory. All agents executing image-generation tasks MUST adhere strictly to these specs to ensure brand consistency and visual excellence.

---

## 1. Core Rationale: Why Structured Visual Sourcing Matters

In digital branding, visual assets serve as the primary external trigger to capture reader attention. When content is published on platforms like LinkedIn and Substack, the visual container (carousel cover, inline diagram, or post banner) represents 60% of the initial click-through motivation. 

If image generation is left unguided, AI engines default to "generic stock illustration" styles—often characterized by flat vector characters with round glasses, neon blue/purple gradients, and disembodied technology icons floating in space. These tropes are widely recognized as low-effort AI output, which immediately damages the credibility of the OAC Content Factory as a source of premium, expert headhunting intelligence.

To project a premium, authoritative, and data-driven persona ("Headhunter thẳng tính, data-driven"), every visual asset must look custom-designed. This is achieved by restricting color palettes to curated harmonized tones, avoiding clichés, enforcing precise compositional layouts, and grounding all concepts in real-world professional contexts.

---

## 2. Execution Bounds & Specifications

### 2.1 Aspect Ratio & Resolution Reference Table

When initiating an image generation task, you MUST map the target channel to its exact aspect ratio and output dimensions.

| Channel / Use Case | Aspect Ratio | Primary Resolution (Pixels) | Alternate Resolution (Pixels) | Notes |
|---|---|---|---|---|
| **LinkedIn Square Post** | `1:1` | `1024 x 1024` | `1200 x 1200` | Best for single-image text posts. |
| **LinkedIn Carousel Slide** | `1:1` or `4:5` | `1024 x 1024` / `1080 x 1350` | `1200 x 1500` | Must maintain identical aspect ratio across all slides in a series. |
| **Substack Banner / Header** | `16:9` | `1024 x 576` | `1200 x 675` | Landscape format. Keep main subjects centered. |
| **LinkedIn / Substack In-line Diagram** | `16:9` | `1024 x 576` | `1024 x 576` | Best for structured charts or process flows. |
| **Profile Background Banner** | `3:1` or `4:1` | `1200 x 400` | `1584 x 396` | Wide aspect banner. Keep content away from bottom-left corner (blocked by profile pic). |

### 2.2 Curated Brand Color Palettes

You are strictly prohibited from using default primary colors. Only use the following HSL/Hex-bounded color combinations:

- **Theme A: Deep Modern Corporate (Default for Sourcing & Strategy)**
  - Primary: Deep Slate Teal (`#1E2E35` / HSL `200, 28%, 16%`)
  - Accent: Warm Ochre Gold (`#D4AF37` / HSL `45, 65%, 52%`)
  - Neutral Base: Soft Ivory White (`#F9F9F6` / HSL `60, 15%, 97%`)
- **Theme B: Tech Startup Scent (Default for AI & Engineering posts)**
  - Primary: Midnight Obsidian (`#0F172A` / HSL `222, 47%, 11%`)
  - Accent: Electric Sage Green (`#10B981` / HSL `162, 76%, 41%`)
  - Neutral Highlight: Cool Ice Gray (`#F1F5F9` / HSL `210, 40%, 96%`)
- **Theme C: War Stories (Default for personal anecdotes)**
  - Primary: Dark Charcoal (`#1F1F1F` / HSL `0, 0%, 12%`)
  - Accent: Burnt Rust Orange (`#C85A32` / HSL `16, 60%, 49%`)
  - Neutral Base: Muted Parchment (`#F5F5F0` / HSL `60, 20%, 95%`)

### 2.3 Visual Style Archetypes & Prompt Keywords

You must categorize your prompt into one of the three approved style archetypes. Mix-and-matching styles within a single post is forbidden.

#### Archetype 1: Flat Minimalist Vector Illustration
- **Use Case:** Flowcharts, comparative matrices, or conceptual infographics.
- **Styling Directives:** Clean flat illustration, geometric shapes, solid color backgrounds, vector art style, thick borders, no complex gradients.
- **Lighting:** Studio flat ambient illumination.
- **Prompt Formula:** `Flat vector illustration of [subject], minimalist style, geometric composition, solid [color] background, clean line art, premium editorial design.`

#### Archetype 2: Premium 3D Claymorphic Render
- **Use Case:** Carousel covers, metaphoric representations (e.g., a candidate trapped in a bot bubble).
- **Styling Directives:** Tactile clay texture, soft rounded corners, glassmorphism accents, matte finishes, premium toy look, isometric projection.
- **Lighting:** Soft studio volumetric lighting, gentle drop shadows, subsurface scattering (translucent glass/clay).
- **Prompt Formula:** `3D claymorphic render of [subject], soft matte clay textures, glassmorphic elements, isometric view, warm volumetric lighting, neutral gray studio backdrop, high-end toy aesthetic.`

#### Archetype 3: Cinematic Executive Portrait/Photo
- **Use Case:** High-impact storytelling, interview covers.
- **Styling Directives:** Narrow depth of field, natural professional environments, realistic textures, corporate editorial look (like Forbes or Wired magazine photography).
- **Lighting:** Moody natural window light, warm fill, dramatic side-lighting (chiaroscuro).
- **Prompt Formula:** `Cinematic portrait of [subject], professional corporate setting, shallow depth of field, shot on 85mm lens, natural side window lighting, detailed skin textures, corporate editorial style.`

---

## 3. Visual Anti-Patterns (Rejection Criteria)

If any of the following anti-patterns are detected in the generated image or prompt draft, the asset MUST be rejected, and the generation sequence must be re-run with modified parameters.

### 3.1 Prompt Clichés (Banned Keywords)
- **NEVER use generic quality boosters:** Banned terms include `photorealistic`, `hyperrealistic`, `4K`, `8K`, `ultra high quality`, `detailed details`. These produce over-sharpened, plastic-looking outputs.
- **NEVER use generic business terms:** Banned terms include `success`, `business meeting`, `innovation`, `teamwork`, `synergy`. These trigger generic stock photo models with unnatural smiles.

### 3.2 Compositional Violations
- **Avoid Text Generation in Images:** Unless explicitly building a vector infographic with strict placement, DO NOT allow the model to generate words. AI models frequently mess up lettering (e.g., writing "RECRUIT" as "RERCUT"). Force all textual context into the surrounding markdown post, and keep the image purely visual.
- **Avoid Crowded Backgrounds:** Backgrounds should be clean, out-of-focus, or solid. A cluttered background (like a busy office with 20 half-rendered background humans) distracts from the focal subject and looks cheap.
- **Avoid Floating Icons Cluster:** Avoid prompts that ask for "a laptop with icons of code, hiring, and emails floating around it". This is the hallmark of lazy AI art. Instead, represent the concept through a single, powerful metaphor (e.g., a physical magnifying glass looking at a miniature 3D candidate).
- **Avoid Anatomical Defects:** Check for extra fingers, distorted faces, or floating limbs. Any image containing an anatomical anomaly must be instantly discarded.
