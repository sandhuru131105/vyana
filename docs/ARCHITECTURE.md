# Architecture

## Upstream Nanobot · observed source structure

```text
CLI / web UI / messaging channel
              |
       message routing / gateway
              |
       session + context builder
              |
          AgentRunner <----> model provider
              |
        ToolRegistry / tools
              |
  session persistence + outbound events
              |
           user interface
```

Core: Python; UI: React/TypeScript/Vite; session persistence: SQLite in this snapshot. External model endpoints, channel credentials and optional integrations are distinct boundaries.

## Vyana · proposed incremental design

```text
Stage 0 (present): Offline CLI -> deterministic demo response
Stage 1: CLI -> provider interface -> fake provider / explicit real-provider opt-in
Stage 2: bounded agent loop -> read-only tools -> tool results -> model
Stage 3: sessions + export/delete -> local persistence
Stage 4: React UI -> authenticated local API / event stream
Stage 5: one approved channel + automation
```

Keep provider calls separate from UI, persistence and tool execution so tests use fakes. Do not let a model response invoke arbitrary Python or shell strings. Tools must have typed input, bounded output and an explicit authority policy. Never put API keys in browser bundles.

## Suggested module ownership (future, not all implemented)

- `cli`: input/output only.
- `providers`: request/response adapter and usage/cost metadata.
- `agent`: iteration budget, cancellation and tool-result loop.
- `tools`: schemas, allowlists, approval policy, safe execution.
- `sessions`: local data model, migration, export and delete.
- `api`: authentication and transport, not direct arbitrary tool access.
- `webui`: presentation, pending/error states, trace visibility.

## Decisions still open

Primary audience and unique benefit; local-only versus hosted; first model provider and budget; first tool; browser UI versus CLI priority; whether later to fork upstream code or continue an independent small implementation. Do not rename upstream import/package/config paths blindly. Vyana is the product/repo name, not proof that a full Python package rename is complete.
