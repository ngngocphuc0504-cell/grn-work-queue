---
name: manage-skills
description: Use to manage shared AI skills: bootstrap a machine, sync repo skills to Codex or Claude Code, package Claude/Cowork ZIPs, or publish a skill to Git.
---

# Manage Skills

Use this skill when the user is managing the shared skill repository rather than editing product code.

## Trigger map

- `setup may moi`, `cai skill repo`, `khoi tao may` -> run `bootstrap.cmd`
- `sync local`, `dong bo skill de test`, `nap skill vao codex`, `nap skill vao claude` -> run `sync-local.cmd`
- `tao skill`, `tao skill moi`, `create skill`, `new skill` -> create the repo copy first, then package Claude ZIPs and sync local runtimes when ready
- `cap nhat skill`, `sua skill`, `update skill`, `kiem tra skill`, `review skill`, `dieu chinh rule skill`, `cap nhat rule skill` -> edit or inspect the repo copy first, then package Claude ZIPs and sync to both runtimes when changes are made
- `xoa skill`, `rename skill`, `doi ten skill` -> update the repo copy first, then run the full Claude package command so stale ZIPs are removed
- `dong goi skill cho Claude`, `tao zip upload Cowork`, `package skill Claude` -> run `package-claude.cmd`
- `publish skill`, `chot skill`, `day skill len git` -> run `publish-skill.cmd`

## Clarify only when required

Ask one short question if the request is missing a required target:

- for `sync-local`: which skill, and whether the runtime target is `codex`, `claude-code`, or `both`
- for create/update/delete skill: which skill, if the skill name is missing
- for `package-claude`: which skill, or whether to package all repo-managed skills
- for `publish`: which skill to publish

Do not ask for extra clarification on `bootstrap`. For `sync-local`, follow the preview + `--confirm yes` flow and only overwrite when the user explicitly wants the sync applied.
For create/update/delete skill, do not ask which runtime or package target to update unless the user explicitly wants an exception; default to packaging all Claude ZIPs and syncing both Codex and Claude after the repo edit is done.
Do not ask for confirmation on `package-claude`; just return the archive path.

## Execution rules

Run commands from the repository root using the Windows launchers:

- `bootstrap.cmd`
- `sync-local.cmd --direction push --skill <name> --target codex|claude|claude-code|both`
- `sync-local.cmd --direction pull --skill <name> --target codex|claude|claude-code`
- `sync-local.cmd --direction push --skill <name> --target both --confirm yes`
- `package-claude.cmd --skill <name>`
- `package-claude.cmd`
- `publish-skill.cmd --skill <name>`

Create/update/delete-skill workflow:

1. Edit the skill only inside the repo under `skills/<name>/...`.
2. Do not treat `%USERPROFILE%\\.codex\\skills` or `%USERPROFILE%\\.claude\\skills` as editable sources for routine updates.
3. Run `package-claude.cmd` from the repo root after the repo edit. Use the full command, not `--skill`, when a skill was created, renamed, deleted, or when the user asks for all packages to stay in sync.
4. Confirm `dist/claude-skills/*.zip` matches the repo-managed folders under `skills/`. Full packaging removes stale ZIP archives that no longer have matching source skill folders.
5. After packaging, preview sync from repo to `both`.
6. Unless the user asked for preview only or named a different target explicitly, apply the sync to `both` with `--confirm yes`.
7. Report that repo, `dist/claude-skills`, Codex local, and Claude local are now aligned.

Claude package invariant:

- `dist/claude-skills` must be treated as a generated upload artifact mirror of `skills/`.
- Never leave a repo skill edit finished without refreshing the Claude ZIP package.
- Prefer `package-claude.cmd` after any skill-management change because it updates all ZIPs and removes stale archives.
- Use `package-claude.cmd --skill <name>` only for an explicit single-skill upload request when no create, rename, or delete happened.

Source-of-truth rule:

- Internal git remote `origin` is canonical.
- The local repo is the only editable local source.
- Runtime folders under `%USERPROFILE%` are sync targets by default, but can be used as a pull source only through the explicit preview + confirm flow.
- For create/update/delete skill, repo first is mandatory. Package Claude ZIPs and sync back to Codex and Claude only after the repo copy is updated.

Sync safety:

- `sync-local` is preview-first for both directions.
- The first run returns a diff preview only.
- Only run the overwrite when the user explicitly wants it, using `--confirm yes`.
- For `pull`, require a single runtime source. Never fan-in from `both` in one step.
- For create/update/delete skill, the user request counts as intent to package Claude ZIPs and sync the finished repo change back to both runtimes unless they explicitly ask for preview-only behavior.

## Windows Encoding And Console Verification Rules

When working with the skill repo on Windows, treat file encoding and console rendering as separate concerns.

File editing safety:

- Never use `Get-Content` + `Set-Content` to rewrite `SKILL.md`, `.md`, `.yaml`, `.json`, or source files inside the skill repo.
- Prefer `apply_patch` for manual edits.
- If a full-file rewrite is unavoidable, use explicit UTF-8 read/write APIs only.
- After editing files that contain Vietnamese or other non-ASCII text, verify the file from disk with UTF-8-aware tooling instead of trusting terminal output alone.

Console verification safety:

- PowerShell can display UTF-8 text incorrectly even when the file bytes are correct.
- If terminal output looks mojibake, do not assume the repo or runtime file is broken yet.
- Confirm with one of these before deciding a sync is bad:
  - compare file hashes between repo and runtime
  - read the file through Python with `python -X utf8`
  - scan for mojibake byte-like sequences rather than single letters, which can also appear inside valid Vietnamese words
- If repo and runtime hashes match and UTF-8 verification is clean, treat the issue as console rendering only.

Windows launcher rule:

- If PowerShell blocks a `.ps1` wrapper, use the corresponding `.cmd` launcher instead.
- For Node-based commands on this machine, prefer forms like `npm.cmd ...` rather than `npm ...` when running from PowerShell.

## Publish safety

Publishing is always a two-step flow:

1. Run `publish-skill.cmd --skill <name>` without `--confirm` to get the preview.
2. Summarize the diff in short Vietnamese.
3. Ask the user for explicit confirmation.
4. Only after approval, run `publish-skill.cmd --skill <name> --confirm yes`.

If the user declines, stop without pushing any changes.

## Response style

- Keep summaries short and operational.
- Prefer Vietnamese when the user is speaking Vietnamese.
- Report `status`, changed targets, and next step after each command.
