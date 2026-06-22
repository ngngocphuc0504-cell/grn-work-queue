# Migration Map

Use this file when maintaining older Garena tool-specific skills after `work-with-garena-tools` exists.

## Keep As Deep Companions

These skills contain deeper operational rules and should not be deleted in the first migration pass:

- `work-with-outline`: deep Outline read/write, subtree, duplicate page, and batch repair rules.
- `work-with-plane`: deep Plane execution, Plane/Outline sync, modules/cycles/pages/intake rules.
- `work-with-demo-system`: deep deploy app behavior if present in the local skill set.
- `work-with-agentation`: separate visual feedback workflow; not a gateway router replacement.
- `outline-memory-ops`: specialized memory commands; keep separate from normal Outline work.
- `organize-project-kb`: specialized Outline restructuring skill; keep separate from normal Outline edits.
- `plane-daily-project-health`: scheduled/digest workflow; keep separate from generic Plane work.

## Thin Wrapper Candidates

After the router has been used successfully, these can become thin wrappers that point to this skill plus their deep reference files:

- `work-with-outline`
- `work-with-plane`
- `work-with-demo-system`

Do not thin them until their unique rules are either preserved in their own references or intentionally delegated.

## Cleanup Rules

- Do not delete a runtime skill copy by hand. Update repo first, then package and sync.
- Full `package-claude.cmd` must remove stale ZIPs for deleted repo skills.
- `sync-local.cmd --direction push --target both` aligns Codex and Claude runtime folders after repo changes.
- Before deleting or renaming a skill, list expected old runtime folders and confirm there is no still-useful behavior that only exists there.
