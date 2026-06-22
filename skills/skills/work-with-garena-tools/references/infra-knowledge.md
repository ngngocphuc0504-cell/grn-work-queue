# Infra Knowledge

Use for infrastructure inventory, server metrics, fleet utilization, monitors, certificates, alerts, databases, schemas, Redis, colocation, and port lookup.

## Known Callable Surface

Discovered via `garena-vn-mcp-gw`:

- `infra_knowledge_get_server`
- `infra_knowledge_search_servers`
- `infra_knowledge_get_server_metrics`
- `infra_knowledge_get_utilization`
- `infra_knowledge_get_fleet_metrics`
- `infra_knowledge_get_web_monitors`
- `infra_knowledge_get_fleet_web_metrics`
- `infra_knowledge_get_fleet_certs`
- `infra_knowledge_search_alerts`
- `infra_knowledge_get_alert_history`
- `infra_knowledge_get_database`
- `infra_knowledge_search_databases`
- `infra_knowledge_get_schema`
- `infra_knowledge_search_schema`
- `infra_knowledge_find_colocation`
- `infra_knowledge_get_fleet_db_metrics`
- `infra_knowledge_search_redis_databases`
- `infra_knowledge_get_redis_host_stats`
- `infra_knowledge_search_redis_key_prefixes`
- `infra_knowledge_search_by_port`

The 2026-06-15 MCP admin screenshot showed 20 tools, matching this discovered list.

## Workflow

1. Start with search when the user gives a fuzzy hostname, service, database, schema, Redis prefix, or port.
2. Use exact get tools after resolving the candidate.
3. For incidents, gather monitor/alert history plus metrics rather than relying on one signal.
4. For database/schema questions, separate database identity from schema/table lookup.
5. For capacity questions, use fleet metrics/utilization before drilling into one host.

## Safety

- Treat infra data as operationally sensitive. Share only what is needed for the task.
- Do not infer root cause from a single metric. State confidence and missing signals.
- If the user asks for a change/remediation and no mutation tool exists, provide a read-only diagnostic and recommended next action.
