# Deploy App

Use for Demo System / deploy app tasks: create project, import repo, upload ZIP, run deployment checks, deploy, inspect status/logs, restart/stop, public URL, and database setup.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `deploy_app_create_project`
- `deploy_app_import_repo`
- `deploy_app_upload_zip`
- `deploy_app_run_deployment_check`
- `deploy_app_deploy`
- `deploy_app_get_deployment_status`
- `deploy_app_get_logs`
- `deploy_app_restart`
- `deploy_app_stop`
- `deploy_app_get_public_url`
- `deploy_app_create_managed_database`
- `deploy_app_set_external_database_url`
- `deploy_app_get_database_status`
- `deploy_app_list_project_databases`
- `deploy_app_delete_project_database`

The 2026-06-15 MCP admin screenshot showed 16 tools; discover the current surface before assuming the missing tool.

## Deployment Workflow

1. Resolve or create the project.
2. Import a repository or upload a ZIP; do not mix both unless the user asks.
3. Configure database only if the app needs one.
4. Run deployment check before deploy.
5. Deploy only after check output is acceptable or the user explicitly accepts the risk.
6. Poll deployment status, fetch logs if not healthy, then fetch public URL.
7. Record durable status in Plane/Outline only when the user asks or the deployment outcome is relevant to the broader project.

## Database Workflow

- Use managed database for simple demos and prototypes unless the user provides an external database URL.
- Read database status after create/set/delete.
- Treat database deletion as destructive and require explicit user intent.

## Safety

- Never deploy from an unverified source path or repository guess.
- Never stop, restart, or delete database resources without explicit intent.
- If deployment succeeds but app behavior is uncertain, verify through browser testing or the relevant app test skill.
