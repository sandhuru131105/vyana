# Vyana architecture

Vyana now follows the actual Nanobot implementation pinned in NOTICE.md. The previous independent CLI-first proposal is superseded by the architecture-first request.

```text
React WebUI / CLI / messaging channel
                 |
         gateway + MessageBus
                 |
      session + context builder
                 |
   AgentLoop / runner <----> LLM provider
                 |
        ToolRegistry / tools
                 |
 SQLite/session persistence + outbound events
                 |
             interface
```

- Python runtime: `nanobot/agent`, `bus`, `providers`, `session`, `config`.
- Web gateway: `nanobot/webui` and channel WebSocket adapter.
- UI: `webui` React/TypeScript; shared events in `packages/client-events`.
- Native terminal source: `tui`, retained but binaries not built/tested here.
- Vyana launch boundary: `src/vyana/cli.py` delegates to `nanobot.cli.entry`.
- Default home: `~/.vyana`, explicit `--home` remains supported.
- Models/providers and optional channels remain external boundaries needing configuration.

Retaining modules does not enable or authorize their real-world use. File/shell tools are inherited and can be powerful. Automatic upstream update staging/execution is blocked so Vyana is not overwritten with a Nanobot package. See BUILD_STATUS.md for inspected/tested boundaries and unverified areas.
