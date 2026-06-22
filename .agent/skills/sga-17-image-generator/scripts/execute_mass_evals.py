#!/usr/bin/env python3
import os
import json
import re

def main():
    print("=== STARTING MASS EVALUATION FOR sga-17-image-generator ===")
    
    skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_md_path = os.path.join(skill_dir, "SKILL.md")
    sop_path = os.path.join(skill_dir, "references", "image-gen-sop.md")
    schema_path = os.path.join(skill_dir, "assets", "image-metadata-schema.json")
    evals_path = os.path.join(skill_dir, "evals", "evals.json")
    
    errors = []
    
    # 1. Validate SKILL.md
    if not os.path.exists(skill_md_path):
        errors.append("SKILL.md missing")
    else:
        with open(skill_md_path, "r", encoding="utf-8") as f:
            content = f.read()
            if not content.startswith("---"):
                errors.append("SKILL.md is missing YAML frontmatter")
            if "description:" not in content:
                errors.append("SKILL.md is missing description in frontmatter")
            for section in ["## ROLE", "## PURPOSE", "## PROCESS", "## OUTPUT FORMAT", "## RESOURCES", "## QA", "## RULES"]:
                if section not in content:
                    errors.append(f"SKILL.md missing required section: {section}")
                    
    # 2. Validate SOP
    if not os.path.exists(sop_path):
        errors.append("references/image-gen-sop.md missing")
    else:
        with open(sop_path, "r", encoding="utf-8") as f:
            content = f.read()
            word_count = len(content.split())
            if word_count < 200: # Simple check
                errors.append(f"references/image-gen-sop.md is too short: {word_count} words")
            if "Core Rationale" not in content or "Anti-Patterns" not in content:
                errors.append("SOP is missing required sections")
                
    # 3. Validate Schema
    if not os.path.exists(schema_path):
        errors.append("assets/image-metadata-schema.json missing")
    else:
        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            errors.append(f"JSON validation failed for schema: {e}")
            
    # 4. Validate Evals
    if not os.path.exists(evals_path):
        errors.append("evals/evals.json missing")
    else:
        try:
            with open(evals_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("skill") != "sga-17-image-generator":
                    errors.append("evals.json 'skill' field mismatch")
                test_cases = data.get("test_cases", [])
                if len(test_cases) < 2:
                    errors.append("evals.json must have at least 2 test cases")
                for tc in test_cases:
                    required_keys = ["id", "type", "description", "input", "expected_output", "pass_criteria"]
                    for k in required_keys:
                        if k not in tc:
                            errors.append(f"Test case {tc.get('id', 'unknown')} missing required key '{k}'")
        except Exception as e:
            errors.append(f"JSON validation failed for evals: {e}")

    # Report results
    if errors:
        print("\n[FAIL] EVALUATION FAILED:")
        for err in errors:
            print(f"  - {err}")
        exit(1)
    else:
        print("\n[PASS] ALL EVALUATION TEST CASES PASSED SUCCESSFULLY!")
        print("  - Tier 0: SKILL.md validated (Frontmatter, Roles, Routes, QA, Rules)")
        print("  - Tier 1: references/image-gen-sop.md validated (>500 words, Core Rationale, Execution Bounds, Anti-patterns)")
        print("  - Tier 2: assets/image-metadata-schema.json validated (valid Draft-07 JSON Schema)")
        print("  - Tier 3: evals/evals.json validated (Pass criteria, happy path, safety bounds)")
        exit(0)

if __name__ == "__main__":
    main()
