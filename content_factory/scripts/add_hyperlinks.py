# -*- coding: utf-8 -*-
"""
Script: add_hyperlinks.py
Add hyperlinks to điểm tin.docx without changing content/format.
"""

import os
import sys
import zipfile
import shutil
import re
import xml.etree.ElementTree as ET

# ─── CONFIG ───────────────────────────────────────────────────────────────────

FOLDER = r'c:\antigravity prjs\MAS-Lean-1\managed_workspaces\ws-default-career-twin\ws-default-career-twin'

# Find the file dynamically (handles unicode filename)
INPUT_FILE = None
for fname in os.listdir(FOLDER):
    if fname.endswith('.docx') and 'tin' in fname.lower():
        INPUT_FILE = os.path.join(FOLDER, fname)
        break

if not INPUT_FILE:
    print("ERROR: Could not find 'tin' docx file")
    sys.exit(1)

print(f"Found input file: {INPUT_FILE}")

OUTPUT_FILE = os.path.join(FOLDER, 'diem_tin_LINKED.docx')
UNPACK_DIR  = os.path.join(FOLDER, 'diem_tin_unpack')

# ─── HYPERLINK MAP ────────────────────────────────────────────────────────────
# (display_text, url, rid_key)
# For "Breaking Defense" which appears twice, we use different rIds
HYPERLINKS = [
    ("German Marshall Fund",
     "https://www.gmfus.org/news/2026-national-defense-authorization-act-what-europeans-need-know",
     "rIdHL001"),
    ("Council on Foreign Relations (CFR)",
     "https://www.cfr.org/articles/trump-is-pulling-troops-from-germany-the-missiles-are-a-bigger-problem",
     "rIdHL002"),
    ("IISS",
     "https://www.iiss.org",
     "rIdHL003"),
    ("ECFR",
     "https://ecfr.eu/publication/trumps-european-revolution/",
     "rIdHL004"),
    ("Ifri",
     "https://www.ifri.org/en/external-articles/external-publications/france-has-new-nuclear-doctrine-forward-deterrence-europe",
     "rIdHL005"),
    ("IW\u00a0K\u00f6ln",   # non-breaking space variant
     "https://finance.yahoo.com/news/exclusive-german-investments-us-nearly-135812989.html",
     "rIdHL006"),
    ("IW K\u00f6ln",
     "https://finance.yahoo.com/news/exclusive-german-investments-us-nearly-135812989.html",
     "rIdHL006"),
    ("DIW Berlin",
     "https://www.diw.de/de/diw_01.c.960746.de/publikationen/weekly_reports/2025_22_1/tariff_chaos_overshadowing_german_economic_recovery.html",
     "rIdHL007"),
    ("Bundesbank",
     "https://www.bundesbank.de/en/press/speeches/outlook-for-2026-in-the-light-of-multifaceted-challenges-worldwide-988530",
     "rIdHL008"),
    ("SWP Berlin",
     "https://www.swp-berlin.org/10.18449/2026S03/",
     "rIdHL009"),
    ("PBS NewsHour",
     "https://www.pbs.org/newshour/world/european-leaders-say-the-timing-of-trumps-decision-to-pull-troops-from-germany-came-as-a-surprise",
     "rIdHL010"),
    ("Defense News",
     "https://www.defensenews.com",
     "rIdHL011"),
    ("Qu\u1ef9 Qu\u1ed1c ph\u00f2ng ch\u00e2u \u00c2u (EDF)",
     "https://defence-industry-space.ec.europa.eu/eu-defence-industry/european-defence-fund-edf-official-webpage-european-commission_en",
     "rIdHL012"),
    ("CSIS",
     "https://www.csis.org/analysis/solving-europes-defense-dilemma-overcoming-challenges-european-defense-cooperation",
     "rIdHL013"),
    ("Carnegie Endowment for International Peace",
     "https://carnegieendowment.org/russia-eurasia/politika/2025/10/germany-security-role-europe",
     "rIdHL014"),
    # Breaking Defense appears twice - handle first occurrence
    ("ELSA",
     "https://breakingdefense.com/2024/07/let-it-go-long-france-joins-germany-italy-and-poland-in-new-elsa-long-range-missile-project/",
     "rIdHL015a"),
    ("Rheinmetall",
     "https://www.rheinmetall.com/en/media/news-watch/news/2026/03/2026-03-11-rheinmetall-presents-annual-report-for-2025",
     "rIdHL016"),
    ("DGAP",
     "https://dgap.org/en/research/publications/deterring-russia-military-aggression-against-europes-nato-allies-1",
     "rIdHL018"),
    ("Carnegie Endowment",
     "https://carnegieendowment.org/europe/strategic-europe/2026/01/solidarity-is-a-must-for-europe-to-ensure-its-own-security?lang=en",
     "rIdHL019"),
]

# Deduplicate by rid (IW Koln has 2 variants same rId)
UNIQUE_RELS = {}
for _, url, rid in HYPERLINKS:
    UNIQUE_RELS[rid] = url

# ─── STEP 1: UNPACK ──────────────────────────────────────────────────────────

if os.path.exists(UNPACK_DIR):
    shutil.rmtree(UNPACK_DIR)
os.makedirs(UNPACK_DIR)

with zipfile.ZipFile(INPUT_FILE, 'r') as z:
    z.extractall(UNPACK_DIR)

print(f"Unpacked to {UNPACK_DIR}")

# ─── STEP 2: PARSE EXISTING RELS ─────────────────────────────────────────────

rels_path = os.path.join(UNPACK_DIR, 'word', '_rels', 'document.xml.rels')
with open(rels_path, 'rb') as f:
    rels_content = f.read().decode('utf-8')

# ─── STEP 3: READ DOCUMENT XML ───────────────────────────────────────────────

doc_path = os.path.join(UNPACK_DIR, 'word', 'document.xml')
with open(doc_path, 'rb') as f:
    doc_bytes = f.read()

doc_str = doc_bytes.decode('utf-8')

# ─── STEP 4: INJECT HYPERLINKS INTO XML STRING ───────────────────────────────
# Strategy: find each anchor text in <w:t> and wrap the enclosing <w:r>...</w:r>
# with <w:hyperlink r:id="..." w:history="1">...</w:hyperlink>

W_NS  = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
R_NS  = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'

def wrap_run_with_hyperlink(xml_str, anchor_text, rid):
    """
    Find <w:t>...anchor_text...</w:t> patterns, locate the parent <w:r>
    block, and wrap it with a w:hyperlink element. Preserves rPr.
    Handles cases where the text is the full content of a <w:t> element.
    Only replaces first occurrence if anchor_text appears once.
    """

    # Escape for use in regex
    escaped = re.escape(anchor_text)

    # Pattern: match a complete <w:r>...<w:t ...>ANCHOR</w:t>...</w:r>
    # We look for <w:r> blocks that contain our anchor text
    # This handles both <w:t>TEXT</w:t> and <w:t xml:space="preserve">TEXT</w:t>
    pattern = r'(<w:r\b[^>]*>(?:(?!</w:r>).)*?<w:t(?:[^>]*)>' + escaped + r'</w:t>(?:(?!</w:r>).)*?</w:r>)'

    replacement = (
        f'<w:hyperlink r:id="{rid}" w:history="1">'
        r'\1'
        '</w:hyperlink>'
    )

    new_str, count = re.subn(pattern, replacement, xml_str, count=1, flags=re.DOTALL)

    if count:
        print(f"  ✓ Linked '{anchor_text}' → {rid}")
    else:
        print(f"  ✗ NOT FOUND: '{anchor_text}' — trying alternate pattern")
        # Try simpler: just find the <w:t> content anywhere
        simple_pat = r'(<w:t(?:[^>]*)>' + escaped + r'</w:t>)'
        simple_rep = (
            f'<w:hyperlink r:id="{rid}" w:history="1">'
            '<w:r>'
            r'\1'
            '</w:r>'
            '</w:hyperlink>'
        )
        new_str, count2 = re.subn(simple_pat, simple_rep, xml_str, count=1, flags=re.DOTALL)
        if count2:
            print(f"    → Alternate pattern matched for '{anchor_text}'")
        else:
            print(f"    → SKIPPED: '{anchor_text}' not found in document")

    return new_str


# Apply all hyperlinks
# Note: "Breaking Defense" appears twice — handle separately
print("\nInjecting hyperlinks...")

# First pass: all except Breaking Defense
for anchor, url, rid in HYPERLINKS:
    doc_str = wrap_run_with_hyperlink(doc_str, anchor, rid)

# Breaking Defense — 2 occurrences with different URLs
# First occurrence
bd_url1 = "https://breakingdefense.com/2024/07/let-it-go-long-france-joins-germany-italy-and-poland-in-new-elsa-long-range-missile-project/"
bd_url2 = "https://breakingdefense.com/2026/04/rheinmetall-and-destinus-to-combine-forces-in-new-missile-systems-joint-venture/"

# Already handled via ELSA above. Now handle "Breaking Defense" text specifically:
doc_str = wrap_run_with_hyperlink(doc_str, "Breaking Defense", "rIdHL015a")
doc_str = wrap_run_with_hyperlink(doc_str, "Breaking Defense", "rIdHL017")

# ─── STEP 5: WRITE UPDATED DOCUMENT XML ──────────────────────────────────────

with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(doc_str)

print(f"\nUpdated document.xml written.")

# ─── STEP 6: ADD RELATIONSHIPS TO RELS FILE ──────────────────────────────────

# Add all new hyperlink rels (only if not already present)
new_rels_lines = []
for rid, url in UNIQUE_RELS.items():
    if rid not in rels_content:
        new_rels_lines.append(
            f'  <Relationship Id="{rid}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
            f'Target="{url}" TargetMode="External"/>'
        )

# Also add Breaking Defense 2nd occurrence
bd_entries = {
    "rIdHL015a": bd_url1,
    "rIdHL017":  bd_url2,
}
for rid, url in bd_entries.items():
    if rid not in rels_content:
        new_rels_lines.append(
            f'  <Relationship Id="{rid}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
            f'Target="{url}" TargetMode="External"/>'
        )

if new_rels_lines:
    insert_point = rels_content.rfind('</Relationships>')
    rels_content = (
        rels_content[:insert_point]
        + '\n'.join(new_rels_lines) + '\n'
        + rels_content[insert_point:]
    )

with open(rels_path, 'w', encoding='utf-8') as f:
    f.write(rels_content)

print(f"Updated rels file with {len(new_rels_lines)} new relationships.")

# ─── STEP 7: REPACK TO DOCX ──────────────────────────────────────────────────

if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

with zipfile.ZipFile(OUTPUT_FILE, 'w', zipfile.ZIP_DEFLATED) as zout:
    for root_dir, dirs, files in os.walk(UNPACK_DIR):
        for file in files:
            file_path = os.path.join(root_dir, file)
            arcname = os.path.relpath(file_path, UNPACK_DIR)
            zout.write(file_path, arcname)

print(f"\n✅ Done! Output: {OUTPUT_FILE}")

# Cleanup
shutil.rmtree(UNPACK_DIR)
print("Cleaned up temp directory.")
