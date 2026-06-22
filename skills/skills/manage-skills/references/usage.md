# Usage Notes

## Example intents

- `setup may nay de dung bo skill chung`
- `cap nhat skill manage-skills`
- `tao skill moi cho workflow cua toi`
- `dong bo manage-skills vao codex va claude de toi test`
- `sync tat ca skill trong repo vao Claude Code`
- `dong goi manage-skills de upload vao Claude/Cowork`
- `publish manage-skills len git`

## Command mapping

- Bootstrap: `bootstrap.cmd`
- Create/update/delete skill flow:
  1. Edit repo copy at `skills/manage-skills/...`
  2. Refresh Claude upload artifacts: `package-claude.cmd`
  3. Preview repo -> both runtimes: `sync-local.cmd --direction push --skill manage-skills --target both`
  4. Confirm repo -> both runtimes: `sync-local.cmd --direction push --skill manage-skills --target both --confirm yes`
- Preview repo -> both runtimes: `sync-local.cmd --direction push --skill manage-skills --target both`
- Confirm repo -> both runtimes: `sync-local.cmd --direction push --skill manage-skills --target both --confirm yes`
- Preview Codex -> repo: `sync-local.cmd --direction pull --skill manage-skills --target codex`
- Confirm Codex -> repo: `sync-local.cmd --direction pull --skill manage-skills --target codex --confirm yes`
- Preview all repo skills to Claude: `sync-local.cmd --direction push --target claude`
- Package for Claude: `package-claude.cmd --skill manage-skills`
- Package all repo skills: `package-claude.cmd`
- Publish preview: `publish-skill.cmd --skill manage-skills`
- Publish confirm: `publish-skill.cmd --skill manage-skills --confirm yes`

## Claude package invariant

`dist/claude-skills` is generated from `skills/`. After creating, updating, renaming, or deleting a skill, run `package-claude.cmd` so every upload ZIP is refreshed and stale ZIPs are removed.

## Safety reminder

Never overwrite immediately. Always preview with `sync-local.cmd` or `publish-skill.cmd` first, then rerun with `--confirm yes` only after checking the diff.
For routine skill updates, never edit the copies under `%USERPROFILE%\\.codex\\skills` or `%USERPROFILE%\\.claude\\skills` first. Edit repo first, then sync both runtimes.
