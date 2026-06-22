---
name: work-with-demo-system
description: Use when Codex needs to work with Demo System through the live tool surface, preferably the gateway-exposed Demo System tool family when available, to create a project, import or upload source, configure a managed or external database, run deployment checks, deploy, inspect status or logs, restart or stop deployments, or retrieve a public URL. Trigger on requests mentioning demo-system, demo system, deploy demo, projectId, managed database, DATABASE_URL, deployment logs, restart deployment, or public URL.
---

# Work With Demo System

## Overview

Use the live Demo System tool family as the primary interface for deployment and runtime operations on the Demo System platform. Treat source code edits as an external responsibility: update code in the repo or local workspace first, then redeploy through Demo System.

## Connection Model

- Treat `demo-system`, `Demo System`, and the connected Demo System tools as the same system.
- Resolve the exact callable tool ids from the active tool surface first. If the Demo System family is missing from the current session, stop and say that the gateway/tool surface is unavailable.
- Default to the live tool surface instead of guessing platform state from memory.
- Treat `projectId` as the anchor for almost every operation. Resolve or confirm it before acting.
- Treat deployment status, deployment logs, and public URL as live runtime state that must be re-read when accuracy matters.

## Working Modes

Choose one mode before acting:

- `project bootstrap`: create a new project and load source code into it
- `database setup`: create a managed database or attach an external `DATABASE_URL`
- `deploy / release`: run checks, deploy, and obtain the public URL
- `runtime inspection`: inspect deployment status, logs, environment summary, or current URL
- `recovery / control`: restart or stop a deployment, or clean up database configuration with explicit approval

## Deterministic Workflow

1. Confirm whether the target project already exists.
2. If there is no project yet, create one with `create_project`.
3. Load source code exactly one way:
   - `import_repo` for a public GitHub repository
   - `upload_zip` for a local ZIP snapshot
4. Decide whether the app needs a database:
   - `create_managed_database` for a platform-managed MySQL database
   - `set_external_database_url` for an external Postgres/MySQL connection
5. If database wiring matters, verify the injection state with `get_deployment_env_summary`.
6. Run `run_deployment_check` before deploying.
7. Deploy with `deploy`.
8. Re-read live state with:
   - `get_deployment_status`
   - `get_logs`
   - `get_public_url`
9. If the app is unhealthy after deploy, inspect logs before using `restart`.
10. Use `stop` only when the user clearly wants the current deployment halted.

## Task Map

Match user intent to the smallest safe tool sequence:

- "tao project demo moi" -> `create_project`
- "dua code tu GitHub len" -> `import_repo`
- "upload source local" -> `upload_zip`
- "gan database platform" -> `create_managed_database`
- "gan DATABASE_URL co san" -> `set_external_database_url`
- "check xem app co nhan DATABASE_URL chua" -> `get_deployment_env_summary`
- "deploy lai app" -> `run_deployment_check` -> `deploy`
- "app dang loi / khong len" -> `get_deployment_status` -> `get_logs`
- "lay link demo / domain public" -> `get_public_url`
- "restart app" -> `get_deployment_status` -> `restart`
- "stop app" -> `get_deployment_status` -> `stop`
- "xem DB hien tai" -> `get_database_status` or `list_project_databases`
- "xoa cau hinh DB" -> re-read DB records first, then `delete_project_database` only with explicit intent

## Operational Heuristics

- Prefer `import_repo` when the source is already in a public GitHub repository and the user wants repeatable redeploys from a branch.
- Prefer `upload_zip` when the source only exists locally or when the user wants an exact snapshot of current files.
- If the user asks for code changes, make those changes outside Demo System first. Demo System is for packaging, deployment, and runtime operations.
- Use `get_logs` as the primary debugging surface after a failed deploy. Do not jump straight to `restart` without reading the failure.
- Use `get_public_url` after successful deploys instead of inferring the URL from prior runs.
- Use `get_database_status` when the user needs masked connection details. Use `list_project_databases` when the user needs to see database records associated with the project.
- Use `get_deployment_env_summary` when the user cares about whether `DATABASE_URL` will be injected, not about the secret value itself.

## Safety Rules

- Never guess a `projectId`.
- Never expose or paraphrase a full secret database URL back to the user if the platform keeps it masked.
- Never delete database configuration without explicit user intent and the required confirmation flag.
- Never promise that Demo System modifies the source-of-truth repo. Source changes still live outside the platform.
- Never claim a deployment is healthy until status, logs, or public URL confirms it.
- Never rerun `deploy` blindly in a failure loop. Read status and logs first.

## High-Value Workflows

### Bootstrap a new demo app

1. Create the project.
2. Import from GitHub or upload a ZIP.
3. Configure database only if the app needs one.
4. Run deployment check.
5. Deploy.
6. Return the live public URL and any immediate warnings.

### Recover a failed deployment

1. Read deployment status.
2. Read deployment logs.
3. Identify whether the failure looks like build, runtime, or database wiring.
4. If configuration changed, verify env summary or database status.
5. Redeploy or restart only after the likely cause is understood.

### Rewire database safely

1. Read current database status or records.
2. Decide between managed database and external `DATABASE_URL`.
3. Apply exactly one database source.
4. Verify deployment env summary.
5. Redeploy if needed and confirm the app is receiving the variable.

## References

- Read [tool-surface.md](./references/tool-surface.md) for the grouped Demo System tool catalog and the common sequences to combine them.
