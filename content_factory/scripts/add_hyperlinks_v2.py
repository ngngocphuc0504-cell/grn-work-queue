# -*- coding: utf-8 -*-
"""
add_hyperlinks_v2.py — Split-run approach for inserting hyperlinks
into điểm tin.docx without changing format/content.
"""

import os, sys, zipfile, shutil, re

FOLDER = r'c:\antigravity prjs\MAS-Lean-1\managed_workspaces\ws-default-career-twin\ws-default-career-twin'

# Find file
INPUT_FILE = None
for fname in os.listdir(FOLDER):
    if fname.endswith('.docx') and 'tin' in fname.lower():
        INPUT_FILE = os.path.join(FOLDER, fname)
        break

if not INPUT_FILE:
    print("ERROR: Could not find file")
    sys.exit(1)

OUTPUT_FILE = os.path.join(FOLDER, 'diem_tin_LINKED.docx')
UNPACK_DIR  = os.path.join(FOLDER, 'diem_tin_unpack')

# ─── HYPERLINK DEFINITIONS ────────────────────────────────────────────────────
# (anchor_text, url, rid, occurrence)
# occurrence=1 means first occurrence, 2 means second, etc.
HYPERLINKS = [
    ("German Marshall Fund",
     "https://www.gmfus.org/news/2026-national-defense-authorization-act-what-europeans-need-know",
     "rIdHL001", 1),

    ("Council on Foreign Relations (CFR)",
     "https://www.cfr.org/articles/trump-is-pulling-troops-from-germany-the-missiles-are-a-bigger-problem",
     "rIdHL002", 1),

    ("IISS",
     "https://www.iiss.org",
     "rIdHL003", 1),

    ("ECFR",
     "https://ecfr.eu/publication/trumps-european-revolution/",
     "rIdHL004", 1),

    ("Ifri",
     "https://www.ifri.org/en/external-articles/external-publications/france-has-new-nuclear-doctrine-forward-deterrence-europe",
     "rIdHL005", 1),

    ("IW K\u00f6ln",
     "https://finance.yahoo.com/news/exclusive-german-investments-us-nearly-135812989.html",
     "rIdHL006", 1),

    ("DIW Berlin",
     "https://www.diw.de/de/diw_01.c.960746.de/publikationen/weekly_reports/2025_22_1/tariff_chaos_overshadowing_german_economic_recovery.html",
     "rIdHL007", 1),

    ("Bundesbank",
     "https://www.bundesbank.de/en/press/speeches/outlook-for-2026-in-the-light-of-multifaceted-challenges-worldwide-988530",
     "rIdHL008", 1),

    ("SWP Berlin",
     "https://www.swp-berlin.org/10.18449/2026S03/",
     "rIdHL009", 1),

    ("PBS NewsHour",
     "https://www.pbs.org/newshour/world/european-leaders-say-the-timing-of-trumps-decision-to-pull-troops-from-germany-came-as-a-surprise",
     "rIdHL010", 1),

    ("Defense News",
     "https://www.defensenews.com",
     "rIdHL011", 1),

    # EDF - the anchor text as it appears in doc may vary, try multiple
    ("Qu\u1ef9 Qu\u1ed1c ph\u00f2ng ch\u00e2u \u00c2u (EDF)",
     "https://defence-industry-space.ec.europa.eu/eu-defence-industry/european-defence-fund-edf-official-webpage-european-commission_en",
     "rIdHL012", 1),

    ("CSIS",
     "https://www.csis.org/analysis/solving-europes-defense-dilemma-overcoming-challenges-european-defense-cooperation",
     "rIdHL013", 1),

    ("Carnegie Endowment for International Peace",
     "https://carnegieendowment.org/russia-eurasia/politika/2025/10/germany-security-role-europe",
     "rIdHL014", 1),

    # Breaking Defense - first occurrence
    ("Breaking Defense",
     "https://breakingdefense.com/2024/07/let-it-go-long-france-joins-germany-italy-and-poland-in-new-elsa-long-range-missile-project/",
     "rIdHL015", 1),

    ("Rheinmetall",
     "https://www.rheinmetall.com/en/media/news-watch/news/2026/03/2026-03-11-rheinmetall-presents-annual-report-for-2025",
     "rIdHL016", 1),

    # Breaking Defense - second occurrence
    ("Breaking Defense",
     "https://breakingdefense.com/2026/04/rheinmetall-and-destinus-to-combine-forces-in-new-missile-systems-joint-venture/",
     "rIdHL017", 2),

    ("DGAP",
     "https://dgap.org/en/research/publications/deterring-russia-military-aggression-against-europes-nato-allies-1",
     "rIdHL018", 1),

    ("Carnegie Endowment",
     "https://carnegieendowment.org/europe/strategic-europe/2026/01/solidarity-is-a-must-for-europe-to-ensure-its-own-security?lang=en",
     "rIdHL019", 2),  # 2nd occurrence (after "Carnegie Endowment for International Peace")
]

# ─── UNPACK ───────────────────────────────────────────────────────────────────
if os.path.exists(UNPACK_DIR):
    shutil.rmtree(UNPACK_DIR)

with zipfile.ZipFile(INPUT_FILE, 'r') as z:
    z.extractall(UNPACK_DIR)

doc_path  = os.path.join(UNPACK_DIR, 'word', 'document.xml')
rels_path = os.path.join(UNPACK_DIR, 'word', '_rels', 'document.xml.rels')

with open(doc_path, 'r', encoding='utf-8') as f:
    doc_str = f.read()

with open(rels_path, 'r', encoding='utf-8') as f:
    rels_str = f.read()

# ─── INJECT HYPERLINK FUNCTION ────────────────────────────────────────────────
def inject_hyperlink(doc_str, anchor_text, rid, occurrence=1):
    """
    Find the nth occurrence of anchor_text inside a <w:t> element,
    split that run into before/anchor/after, wrap anchor with <w:hyperlink>.
    """
    # Find all positions of anchor_text
    positions = []
    start = 0
    while True:
        idx = doc_str.find(anchor_text, start)
        if idx == -1:
            break
        positions.append(idx)
        start = idx + 1

    if not positions:
        print(f"  [SKIP] '{anchor_text}' — not found in document")
        return doc_str

    if len(positions) < occurrence:
        print(f"  [SKIP] '{anchor_text}' — only {len(positions)} occurrence(s), need #{occurrence}")
        return doc_str

    target_pos = positions[occurrence - 1]

    # Find the enclosing <w:r> block
    # Search backward for <w:r
    run_start = doc_str.rfind('<w:r', 0, target_pos)
    if run_start == -1:
        print(f"  [SKIP] '{anchor_text}' — could not find enclosing <w:r>")
        return doc_str

    # Find end of this <w:r>
    run_end = doc_str.find('</w:r>', target_pos)
    if run_end == -1:
        print(f"  [SKIP] '{anchor_text}' — could not find </w:r>")
        return doc_str
    run_end += len('</w:r>')

    run_block = doc_str[run_start:run_end]

    # Extract run opening tag (may have attributes)
    r_open_m = re.match(r'(<w:r[^>]*>)', run_block)
    r_open = r_open_m.group(1) if r_open_m else '<w:r>'

    # Extract rPr block
    rpr_m = re.search(r'(<w:rPr\b.*?</w:rPr>)', run_block, re.DOTALL)
    rpr_block = rpr_m.group(1) if rpr_m else ''

    # Extract <w:t> open tag, content, close
    t_m = re.search(r'(<w:t(?:[^>]*)>)(.*?)(</w:t>)', run_block, re.DOTALL)
    if not t_m:
        print(f"  [SKIP] '{anchor_text}' — no <w:t> in run block")
        return doc_str

    t_open    = t_m.group(1)
    t_content = t_m.group(2)
    t_close   = t_m.group(3)

    # Find anchor within t_content
    anchor_idx = t_content.find(anchor_text)
    if anchor_idx == -1:
        print(f"  [SKIP] '{anchor_text}' — anchor not in <w:t> content")
        return doc_str

    before_text = t_content[:anchor_idx]
    after_text  = t_content[anchor_idx + len(anchor_text):]

    # Build replacement runs
    def make_run(text):
        needs_preserve = text.startswith(' ') or text.endswith(' ')
        t_tag = '<w:t xml:space="preserve">' if needs_preserve else '<w:t>'
        return f'{r_open}{rpr_block}{t_tag}{text}</w:t></w:r>'

    parts = []

    if before_text:
        parts.append(make_run(before_text))

    # Hyperlink run
    parts.append(
        f'<w:hyperlink r:id="{rid}" w:history="1">'
        f'{r_open}{rpr_block}'
        f'<w:t>{anchor_text}</w:t>'
        f'</w:r>'
        f'</w:hyperlink>'
    )

    if after_text:
        parts.append(make_run(after_text))

    replacement = ''.join(parts)

    new_doc = doc_str[:run_start] + replacement + doc_str[run_end:]
    print(f"  [OK]  '{anchor_text}' (occurrence {occurrence}) → {rid}")
    return new_doc


# ─── APPLY ALL HYPERLINKS ─────────────────────────────────────────────────────
print("Injecting hyperlinks...")

# Track occurrence counts per anchor
occurrence_counter = {}

for anchor, url, rid, occ in HYPERLINKS:
    key = anchor
    doc_str = inject_hyperlink(doc_str, anchor, rid, occ)

# ─── VERIFY R: NAMESPACE IN ROOT ─────────────────────────────────────────────
# Make sure r: namespace is declared on root element
if 'xmlns:r=' not in doc_str[:500]:
    r_ns = ' xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
    # Insert after first tag opening
    doc_str = doc_str.replace('<w:document ', '<w:document' + r_ns + ' ', 1)
    print("  Added r: namespace to root element")

# ─── WRITE UPDATED DOCUMENT ───────────────────────────────────────────────────
with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(doc_str)

# ─── UPDATE RELS FILE ─────────────────────────────────────────────────────────
added = 0
for anchor, url, rid, occ in HYPERLINKS:
    if rid not in rels_str:
        new_rel = (
            f'  <Relationship Id="{rid}" '
            f'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink" '
            f'Target="{url}" TargetMode="External"/>\n'
        )
        rels_str = rels_str.replace('</Relationships>', new_rel + '</Relationships>')
        added += 1

with open(rels_path, 'w', encoding='utf-8') as f:
    f.write(rels_str)

print(f"\nAdded {added} relationships to rels file.")

# ─── REPACK ───────────────────────────────────────────────────────────────────
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

with zipfile.ZipFile(OUTPUT_FILE, 'w', zipfile.ZIP_DEFLATED) as zout:
    for root_dir, dirs, files in os.walk(UNPACK_DIR):
        for file in files:
            fpath = os.path.join(root_dir, file)
            arcname = os.path.relpath(fpath, UNPACK_DIR)
            zout.write(fpath, arcname)

shutil.rmtree(UNPACK_DIR)

print(f"\nDone! Output saved to:\n{OUTPUT_FILE}")
