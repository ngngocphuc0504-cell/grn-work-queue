# Demo System Tool Surface

Use this reference when the user asks what the Demo System tool family can do or when the task requires choosing the right tool quickly.

Treat the operation names below as logical names. Resolve the exact callable tool ids from the active session first.

## Project bootstrap

- `create_project`: create a new Demo System project
- `import_repo`: import code from a public GitHub repository into a project workspace
- `upload_zip`: upload a local ZIP archive into a project workspace

## Database operations

- `create_managed_database`: create or reuse the platform-managed MySQL database
- `set_external_database_url`: store an external `DATABASE_URL`
- `get_database_status`: read masked database status and connection metadata
- `list_project_databases`: list project database records
- `delete_project_database`: remove database configuration after explicit confirmation
- `get_deployment_env_summary`: confirm whether `DATABASE_URL` will be injected into the app deployment

## Deployment operations

- `run_deployment_check`: run the platform pre-deploy check
- `deploy`: deploy the current project source
- `get_deployment_status`: inspect the latest deployment status or a specific deployment
- `get_logs`: read deployment logs with pagination support
- `restart`: restart the current deployment
- `stop`: stop the latest deployment
- `get_public_url`: return the live public URL and deployment status

## Common sequences

### New app from GitHub

1. `create_project`
2. `import_repo`
3. Optional database setup
4. `run_deployment_check`
5. `deploy`
6. `get_public_url`

### New app from local files

1. `create_project`
2. `upload_zip`
3. Optional database setup
4. `run_deployment_check`
5. `deploy`
6. `get_public_url`

### Deployment triage

1. `get_deployment_status`
2. `get_logs`
3. Optional `get_database_status` or `get_deployment_env_summary`
4. `restart` or `deploy` only after inspection
