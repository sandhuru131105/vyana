# Build roadmap

Milestones are proposed sequence, not delivery-date promises.

## M0 · present foundation

- Public repo and honest status, provenance/licenses, source analysis.
- Offline CLI smoke tests, no keys or target execution.
- Done: `--about`, `/help`, empty/normal input, EOF and `/quit` tested.

## M1 · provider boundary

- Define Message, ModelResponse, ToolCall and Provider protocols.
- Fake provider tests first; then one opt-in real provider.
- Done: normal response, timeout, quota/auth error, cancellation; no credentials in logs; model/budget selected before paid calls.

## M2 · safe agent loop

- Typed read-only tool; max iterations, request/response limits, cancellation.
- Done: malformed args, unknown tool, denied path, symlink escape and size limit tests. No arbitrary shell or message send.

## M3 · local sessions

- SQLite schema/migrations, history, export/delete and privacy notice.
- Done: reload, migration, concurrent-write/error, export/delete tests; secrets excluded from chat logs.

## M4 · web UI

- React chat, stream status, retry/cancel, visible tool trace and settings.
- Done: API authentication, localhost default, origin policy, secret-free frontend bundle, accessible mobile/desktop checks and backend contract tests.

## M5 · one integration

- Pick one channel only after an access-control and sender/recipient policy exists.
- Done: duplicate delivery/retry tests, allowlist and permissions, redacted logs, explicit sending authority, operating-cost review.

## Release gate

License audit for copied assets/dependencies; tests with fake providers; documented security boundaries; reproducible build; no live keys/runtime data; rollback path. Never label source analysis as a passed runtime/security audit.
