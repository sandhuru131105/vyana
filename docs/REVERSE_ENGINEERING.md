# Nanobot reverse-engineering report

27 October 2026 · source snapshot `b07b3eac244ff7faa7eeb2d4777fe54dbae1b6d2`

## முடிவு

Nanobot ஒரு Python personal-assistant framework. தற்போதைய snapshot-ல் core Python runtime, React/TypeScript web UI, CLI/native-TUI integration, channel adapters, LLM providers, tool registry, sessions, memory மற்றும் automation உள்ளன. README feature list மட்டும் வைத்து இந்த முடிவு இல்லை: கீழே உள்ள implementation paths மற்றும் AST inventory ஆய்வு செய்யப்பட்டன. Target application அல்லது model calls ஓடவில்லை; runtime correctness/performance verify செய்யப்படவில்லை.

## Evidence levels

- **REA-static:** selected frontend files parsed by REA 6.8.0; no app execution.
- **Python-AST:** 541 Python files parsed with stdlib `ast.parse`; 0 syntax errors under the analysis interpreter. This is not typechecking or runtime testing.
- **Manual-source:** named source functions/data flows read directly.
- **Proposal:** Vyana implementation choices, not upstream behavior or a user-approved feature promise.

## Feature → implementation → what we know

| Feature | Source evidence | Finding / limit |
|---|---|---|
| Entry / CLI | `pyproject.toml`, `nanobot/cli/entry.py` | `nanobot = nanobot.cli.entry:main`; entry dispatches agent/root commands and native TUI candidates. Python >=3.11. |
| Message routing | `nanobot/bus/queue.py:MessageBus` | Async inbound/outbound queues decouple channels and core. Queue delivery is not proof of external delivery. |
| Agent orchestration | `nanobot/agent/loop.py:AgentLoop`, `_run_agent_loop` | Runtime/session/context ownership; delegates iteration to shared runner. |
| Model + tool loop | `nanobot/agent/runner.py`, `tools/execution.py` | Provider response can request tools; `execute_tool_calls` supplies results for continued iterations. Providers need separate setup. |
| Tools | `nanobot/agent/tools/registry.py:ToolRegistry` | Tool definitions, lookup, validation and execution plumbing. Source includes file, shell, web, cron, MCP and subagent integrations; no tool was executed in this review. |
| Provider abstraction | `nanobot/providers/base.py`, `factory.py`, `registry.py` | Multiple provider adapters and model routing, not a bundled model. No price/free-access guarantee. |
| Sessions | `nanobot/session/manager.py`, `sqlite_store.py` | Session manager uses SQLite store; `sessions.sqlite3` is the persisted database. Older JSONL migration code also exists. Do not simplify current storage to only JSONL. |
| Context and memory | `nanobot/agent/context.py`, `memory.py` | Transcript/context construction plus archive/consolidation components. Quality and recall not benchmarked. |
| UI transport | `webui/src/lib/nanobot-client.ts`, `runtime.ts` | WebSocket client; optional native host bridge; streamed events and run-state projection. Static presence is not runtime success. |
| Web gateway routes | `nanobot/webui/ws_http.py:GatewayHTTPHandler` | Session, workspace, automation and settings routes. No live server started. |
| Browser UI | `webui/package.json`, `src/main.tsx`, `src/App.tsx` | React 18, TypeScript, Vite and UI/rendering dependencies. REA scoped frontend run plus source inspection. |
| Automation/channels | `nanobot/cron/`, `nanobot/triggers/`, `nanobot/channels/` | Source adapters include Telegram, WhatsApp, Slack and others. Each needs credentials/policies; none was connected. |

## Concrete message journey

1. A channel or local UI receives input and forms a routed inbound message.
2. Message bus/core runtime assigns a session and selected model runtime.
3. Context/history/tool definitions form the provider request.
4. Provider returns text or tool calls.
5. Tool registry validates and dispatches eligible calls; runner receives results and continues within limits.
6. Session/checkpoint state persists; outbound events/text are projected back to the interface.

This is a source-grounded architectural trace, not an end-to-end observed run. Error/retry/cancellation and provider-specific paths add branches.

## REA actually ran

Evidence id: `ev_ba783f2c59a17c45b2054ebf849f9820d0fbea8192aae997e2fa1d3cfdc3fb98`.

Selected inputs: package.json, src/main.tsx, src/App.tsx, src/lib/nanobot-client.ts, src/lib/http.ts, src/lib/runtime.ts within webui.

- 685 relevant inventoried files; 679 outside selected-source analysis.
- 5 JavaScript/TypeScript source files parsed; 0 parse failures.
- 23,084 AST nodes visited; 416 findings recorded by the analyzer.
- Graph coverage: **partial**, not a complete application reconstruction.
- Static relationships do not prove execution, reachability or behavioral equivalence.
- `packages/client-events` imports outside the webui root and unselected modules need separate tracing.

The Python backend was NOT analyzed by that REA JavaScript workflow. We used explicit Python AST/manual review instead. See REA_METHOD.md for reproduction and evidence-summary integrity caveats.

## What this does not establish

No full runtime/security audit, no model quality/cost benchmark, no channel delivery test, no upstream test-suite pass claim, no native TUI binary analysis, no behavioral-equivalence claim. Source availability and MIT do not grant rights to third-party brands, accounts or services.

## Source links

- https://github.com/HKUDS/nanobot
- https://github.com/HKUDS/nanobot/blob/main/pyproject.toml
- https://github.com/HKUDS/nanobot/blob/main/nanobot/agent/loop.py
- https://github.com/HKUDS/nanobot/blob/main/nanobot/session/sqlite_store.py
- https://github.com/HKUDS/nanobot/blob/main/webui/package.json
- https://github.com/HKUDS/nanobot/blob/main/LICENSE

These main-branch links may move; the recorded commit and file hashes identify the reviewed snapshot.
