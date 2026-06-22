# Format Defects

Use this file when the user reports repeated visual or formatting problems in Outline.

## Purpose

The goal is to translate a visible symptom into:

- a scan signature
- a stable normalization rule
- a minimal, repeatable repair plan

Do not anchor only on page role such as `Hub`, `Canonical`, or `Archive`.

## Common Defect Types

### 1. Metadata Header Collapsed Into One Paragraph

Typical symptom:

- multiple header fields appear as one long paragraph
- labels such as `Document Role`, `Status`, `Owner`, `Last Verified`, `Ngày build`, `Người build`, `Trạng thái`, or `Tóm tắt thay đổi` run together

Typical cause:

- metadata was stored as plain text with fragile line breaks
- renderer does not preserve the intended line breaks reliably

Preferred normalization:

- convert the metadata block into a bullet list

Stable target example:

```md
- **Document Role:** Canonical
- **Status:** Live
- **Owner:** Hai-Son
- **Last Verified:** 2026-04-14
```

Avoid:

- relying on single newlines between fields
- keeping the whole block as one paragraph

### 2. Broken Internal Link Pseudo-Markup

Typical symptom:

- raw strings like `<page url="...">...</page>` appear in the rendered page

Preferred normalization:

- replace with normal markdown links

### 3. Fragile List Or Section Formatting

Typical symptom:

- bullets collapse into plain paragraphs
- labels and content no longer align

Preferred normalization:

- convert to explicit markdown bullets or headings

### 4. Table Formatting Damage

Typical symptom:

- rows or headers do not align
- content that should be tabular becomes plain text

Preferred normalization:

- repair the markdown table
- if the table is too fragile, convert to bullets only when preserving semantics is still safe

### 5. Stray Escape Or Trailing Markup

Typical symptom:

- trailing `\`
- raw escaped tokens
- literal HTML fragments that were not intended for display

Preferred normalization:

- remove the stray escape only when it is clearly accidental
- keep intentional code samples intact

## Screenshot-To-Scan Workflow

When the user provides a screenshot:

1. Extract visible tokens from the screenshot.
2. Identify the defect zone:
   - header metadata
   - list
   - table
   - link block
   - body paragraph
3. Search the subtree using those visible tokens first.
4. Then search for structurally similar pages, even if they use different labels.

## Coverage Rule

For subtree formatting scans:

- cover every descendant branch that could contain the same document archetype
- sample leaves, not just hubs or indexes
- do not conclude the subtree is clean until scan confidence is stated

## Repair Rule

For one batch:

- fix one defect type only
- keep content semantics unchanged
- normalize to the most renderer-stable markdown form available
- avoid rewriting the whole page when only the damaged block needs repair
