"""
MAS 5.0 Agent Factory — Build Engine
=====================================
Reads a YAML config file, validates it against the MAS 5.0 Agent Schema,
and generates a compliant 4-file Agent folder (INDEX, IDENTITY, SOUL, RULES).

Usage:
    python build_agent.py --config path/to/config.yaml --dest .agent/agents/
"""

import os
import sys
import re
import argparse

# Force UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

try:
    import yaml
except ImportError:
    print("[FATAL] pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════
#  VALIDATION ENGINE (Implements references/validation-rules.md)
# ═══════════════════════════════════════════════════════════

PLACEHOLDERS = {"tbd", "todo", "...", "mô tả sau", "fill in", "n/a"}
VALID_TIERS = {"T2", "T3", "T4"}

def validate_config(config: dict) -> list:
    """Validate YAML config against SR + CQ + UC rules. Returns list of findings."""
    findings = []

    def fail(rule_id, field, msg, severity="CRITICAL"):
        findings.append({"rule": rule_id, "field": field, "severity": severity, "message": msg})

    # SR-01: Root key
    agent_data = config.get('agent_config')
    if not agent_data:
        fail("SR-01", "root", "Missing root key 'agent_config'")
        return findings  # Cannot continue without root

    # SR-02: Required blocks
    for block in ['meta', 'identity', 'soul', 'operating_rules']:
        if block not in agent_data:
            fail("SR-02", block, f"Missing required block: '{block}'")

    if len([f for f in findings if f['severity'] == 'CRITICAL']) > 0:
        return findings  # Cannot continue with missing blocks

    meta = agent_data.get('meta', {})
    identity = agent_data.get('identity', {})
    soul = agent_data.get('soul', {})
    rules = agent_data.get('operating_rules', {})

    # --- META Validation ---
    agent_id = meta.get('id', '')
    if not agent_id or ' ' in agent_id:
        fail("SR-03", "meta.id", f"ID is empty or contains spaces: '{agent_id}'")
    elif not re.match(r'^[A-Z0-9\-]+$', agent_id):
        fail("SR-03", "meta.id", f"ID contains invalid chars (only A-Z, 0-9, hyphen): '{agent_id}'")

    tier = meta.get('tier', '')
    if tier not in VALID_TIERS:
        fail("SR-04", "meta.tier", f"Invalid tier '{tier}'. Must be one of: {VALID_TIERS}")

    name = meta.get('name', '')
    if not name:
        fail("SR-05", "meta.name", "Agent name is empty", "MAJOR")
    elif len(name) > 60:
        fail("SR-05", "meta.name", f"Name exceeds 60 chars ({len(name)})", "MAJOR")

    parent = meta.get('parent', '')
    if not parent:
        fail("SR-06", "meta.parent", "Parent is empty", "MAJOR")
    if tier == 'T2' and parent != 'HUMAN':
        fail("SR-06", "meta.parent", f"T2 agent must have parent='HUMAN', got '{parent}'", "MAJOR")

    # --- IDENTITY Validation ---
    mission = identity.get('mission', '')
    if mission.strip().lower() in PLACEHOLDERS:
        fail("CQ-02", "identity.mission", f"Mission is a placeholder: '{mission}'")
    elif len(mission.split()) < 20:
        fail("CQ-01", "identity.mission", f"Mission too short ({len(mission.split())} words, min 20)", "MAJOR")

    allowed = identity.get('allowed_scope', [])
    if len(allowed) < 2:
        fail("CQ-03", "identity.allowed_scope", f"Need >= 2 items, got {len(allowed)}", "MAJOR")

    forbidden = identity.get('forbidden_scope', [])
    if len(forbidden) < 1:
        fail("CQ-04", "identity.forbidden_scope", f"Need >= 1 item, got {len(forbidden)}", "MAJOR")

    # --- SOUL Validation ---
    vibe = soul.get('vibe', '')
    if len(vibe.split()) < 10:
        fail("CQ-05", "soul.vibe", f"Vibe too short ({len(vibe.split())} words, min 10)", "MINOR")

    soul_rules = soul.get('rules', [])
    if len(soul_rules) < 2:
        fail("CQ-06", "soul.rules", f"Need >= 2 rules, got {len(soul_rules)}", "MAJOR")

    motto = soul.get('motto', '')
    if not motto:
        fail("CQ-07", "soul.motto", "Motto is empty", "MINOR")

    # --- OPERATING RULES Validation ---
    steps = rules.get('steps', [])
    if len(steps) < 2:
        fail("CQ-08", "operating_rules.steps", f"Need >= 2 steps, got {len(steps)}")
    else:
        for i, step in enumerate(steps):
            if not step.get('name') or not step.get('action'):
                fail("CQ-08", f"operating_rules.steps[{i}]", f"Step {i} missing 'name' or 'action'")

    io = rules.get('io_contract', {})
    for sub in ['input', 'output', 'handoff']:
        if not io.get(sub):
            fail("CQ-09", f"operating_rules.io_contract.{sub}", f"Missing '{sub}' in io_contract")

    return findings


def print_validation_report(findings: list) -> bool:
    """Print findings table. Returns True if build can proceed."""
    if not findings:
        print("[VALIDATION] All checks PASSED.")
        return True

    has_critical = any(f['severity'] == 'CRITICAL' for f in findings)
    major_count = sum(1 for f in findings if f['severity'] == 'MAJOR')

    print("\n" + "=" * 60)
    print("  VALIDATION REPORT")
    print("=" * 60)
    print(f"{'Rule':<8} {'Field':<30} {'Severity':<10} {'Message'}")
    print("-" * 60)
    for f in findings:
        sev_icon = {"CRITICAL": "X", "MAJOR": "!", "MINOR": "~"}.get(f['severity'], '?')
        print(f"[{sev_icon}] {f['rule']:<5} {f['field']:<30} {f['severity']:<10} {f['message']}")
    print("-" * 60)

    if has_critical:
        print("[REJECT] CRITICAL findings detected. Build aborted.")
        return False
    elif major_count >= 3:
        print("[REJECT] 3+ MAJOR findings. Full config review required.")
        return False
    else:
        print(f"[WARNING] {len(findings)} minor findings. Build will proceed.")
        return True


# ═══════════════════════════════════════════════════════════
#  BUILD ENGINE
# ═══════════════════════════════════════════════════════════

def construct_agent_from_yaml(yaml_path: str, dest_dir: str) -> bool:
    """Read YAML config, validate, and build Agent folder."""
    print(f"[FACTORY] Loading config: {yaml_path}")

    with open(yaml_path, 'r', encoding='utf-8') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(f"[FATAL] YAML parse error: {exc}")
            return False

    # --- Validation Gate ---
    findings = validate_config(config)
    can_build = print_validation_report(findings)
    if not can_build:
        return False

    agent_data = config['agent_config']
    meta = agent_data['meta']
    identity = agent_data['identity']
    soul = agent_data['soul']
    rules = agent_data['operating_rules']
    agent_id = meta['id']

    # --- Collision Check (UC-01) ---
    agent_dir = os.path.join(dest_dir, agent_id)
    if os.path.exists(agent_dir):
        print(f"[REJECT] UC-01: Folder already exists: {agent_dir}")
        return False

    os.makedirs(agent_dir, exist_ok=True)

    # --- Generate INDEX.md ---
    tier_num = meta['tier'].replace('T', '')
    index_content = f"""# System Instruction — {meta['name']}

> [!IMPORTANT] Override Priority: Tier {tier_num}

Đây là file điều phối (Master file) của Agent `{agent_id}`. Bắt buộc đọc các file đính kèm dưới đây để cấu thành nên thực thể hoàn chỉnh của Agent.

## 1. Bản Sắc & Nhiệm Vụ (Who are you?)

Hãy đọc `.agent/agents/{agent_id}/IDENTITY.md` để hiểu sứ mệnh và quyền hạn cốt lõi.

## 2. Linh Hồn & Thái Độ (How you communicate?)

Hãy đọc `.agent/agents/{agent_id}/SOUL.md` để thấm nhuần nguyên tắc giao tiếp và cách hành xử đặc trưng.

## 3. Quy Tắc Vận Hành (How you work?)

Hãy đọc `.agent/agents/{agent_id}/RULES.md` để tuân thủ logic nghiệp vụ, CQS và hệ thống I/O Hand-offs.

---

## Meta

| Field | Value |
|-------|-------|
| Agent ID | {agent_id} |
| Tier | {meta['tier']} |
| Version | 5.0.0 (Folder-Based) |
"""
    _write(agent_dir, 'INDEX.md', index_content)

    # --- Generate IDENTITY.md ---
    allowed_lines = "\n".join([f"- ĐƯỢC PHÉP: {s}" for s in identity.get('allowed_scope', [])])
    forbidden_lines = "\n".join([f"- KHÔNG ĐƯỢC PHÉP: {s}" for s in identity.get('forbidden_scope', [])])

    identity_content = f"""---
agent_id: {agent_id}
role: {meta['name']}
---

**Sứ mệnh (Mission):**

{identity.get('mission', '')}

**Phạm vi Cốt lõi (Core Scope):**

{allowed_lines}
{forbidden_lines}
"""
    _write(agent_dir, 'IDENTITY.md', identity_content)

    # --- Generate SOUL.md ---
    soul_rules_lines = "\n".join([f"{i+1}. {r}" for i, r in enumerate(soul.get('rules', []))])

    soul_content = f"""**Vibe & Tone (Giọng điệu):**

- {soul.get('vibe', '')}

**Quy tắc Giao tiếp (Communication Rules):**

{soul_rules_lines}

> **Châm ngôn (Motto):** "{soul.get('motto', '')}"
"""
    _write(agent_dir, 'SOUL.md', soul_content)

    # --- Generate RULES.md ---
    forbidden_lines_for_rules = "\n".join([f"- [CẤM]: {s}" for s in identity.get('forbidden_scope', [])])
    soul_rules_for_rules = "\n".join([f"- [LUẬT]: {r}" for r in soul.get('rules', [])])
    
    constraints_block = f"""> [!WARNING] AGENT CONSTITUTION (MANDATORY BOUNDARIES)
> 
> THE FOLLOWING CONSTRAINTS OVERRIDE ALL OTHER INSTRUCTIONS:
> 
{forbidden_lines_for_rules}
{soul_rules_for_rules}

"""

    steps_block = ""
    for step in rules.get('steps', []):
        steps_block += f"### Step: {step['name']}\n\n{step['action']}\n\n"

    rag_lines = "\n".join([f"- {r}" for r in rules.get('mandatory_rag', [])]) or "- (None configured)"
    ep = rules.get('epistemic_lines', {})

    rules_content = f"""{constraints_block}## Process / Workflow

{steps_block}

## I/O Contract

- **Input**: {rules.get('io_contract', {}).get('input', '')}
- **Output**: {rules.get('io_contract', {}).get('output', '')}
- **Handoff**: {rules.get('io_contract', {}).get('handoff', '')}

## KB Connectivity

**[MANDATORY RAG]**: Load before execution:

{rag_lines}

## Epistemic Coupling

> [[Authorized Workflows]]: `/{ep.get('authorized_workflows', '')}`
> [[Linked Skills]]: `[{ep.get('linked_skills', '')}]`
"""
    _write(agent_dir, 'RULES.md', rules_content)

    # --- Post-Build Verification ---
    print("\n" + "=" * 60)
    print(f"  [SUCCESS] Agent {agent_id} built successfully!")
    print("=" * 60)
    for fname in ['INDEX.md', 'IDENTITY.md', 'SOUL.md', 'RULES.md']:
        fpath = os.path.join(agent_dir, fname)
        size = os.path.getsize(fpath) if os.path.exists(fpath) else 0
        status = "OK" if size > 0 else "EMPTY!"
        print(f"  [{status}] {fname:<15} ({size:>5} bytes)")
    print(f"\n  Output: {os.path.abspath(agent_dir)}")
    return True


def _write(directory: str, filename: str, content: str):
    """Write content to file with UTF-8 encoding."""
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


# ═══════════════════════════════════════════════════════════
#  CLI ENTRYPOINT
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAS 5.0 Agent Factory — Build Engine")
    parser.add_argument('--config', type=str, required=True, help="Path to YAML config file")
    parser.add_argument('--dest', type=str, default=".", help="Destination directory for Agent folder")
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print(f"[FATAL] Config file not found: {args.config}")
        sys.exit(1)

    success = construct_agent_from_yaml(args.config, args.dest)
    sys.exit(0 if success else 1)
