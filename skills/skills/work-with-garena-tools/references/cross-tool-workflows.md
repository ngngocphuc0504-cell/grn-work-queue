# Cross-Tool Workflows

Load this only when the user request spans more than one Garena internal system.

## Outline To Plane

Use when a spec, roadmap, or decision in Outline needs execution tracking.

1. Resolve and read the Outline source page.
2. Identify durable requirements versus temporary notes.
3. Resolve the Plane project and live taxonomy: states, labels, cycles, modules, milestones, work item types.
4. Create or update Plane work items/modules only after duplicate checks.
5. Add a short backlink or context note when useful.
6. Do not rewrite the Outline source unless the user asks for documentation sync.

## Plane To Outline

Use when delivery movement in Plane should become durable project knowledge.

1. Read the relevant Plane objects live.
2. Decide what is durable enough for Outline: decision, current state, roadmap movement, or release note.
3. Resolve the exact Outline page and section.
4. Preview the update bundle when it changes canonical or multi-page docs.
5. Update only the durable summary; do not dump ticket logs into Outline.

## Deploy App To Plane/Outline

Use after deploying or diagnosing an app.

1. Resolve deploy app project and deployment status.
2. Fetch logs/status/public URL as needed.
3. If deployment affects a tracked project, update Plane with execution status.
4. If the URL/status is durable, update Outline current-state or handoff docs.
5. Keep logs out of canonical docs unless they explain a durable decision.

## Infra To Deploy App

Use when a deployed app has infra symptoms.

1. Gather deployment status and logs.
2. Use Infra Knowledge for monitors, alerts, metrics, DB, Redis, cert, or port lookup.
3. Separate observed facts from suspected root cause.
4. Recommend or execute remediation only if a safe mutation tool exists and the user intent is explicit.

## Google Drive To Outline/Plane

Use when Drive files are source artifacts for specs, handoff, or execution.

1. Resolve Drive file/folder identity with metadata.
2. Read content only after confirming the exact file.
3. Summarize or extract the parts relevant to the target system.
4. Write concise durable content to Outline or actionable work to Plane, not raw file dumps.
