# Build status - 27 October 2026

## Imported implementation

Pinned Nanobot source: b07b3eac244ff7faa7eeb2d4777fe54dbae1b6d2. Python runtime, React UI, common client protocol, session/SQLite, providers, tools, channel adapters, native TUI source and tests are retained. This is an attributed adaptation, not an original rewrite or audited equivalent product.

## Verified locally

- Linux x86_64, Python 3.11.17: editable `vyana-ai` 0.1.0 install succeeds.
- Production wheel built, installed into a second clean environment; Vyana version and bundled branded UI checked.
- `python -m vyana --help` and `--version` launch inherited commands.
- React/TypeScript production build passes. Large chunk warnings remain.
- Selected tests: agent, providers, sessions, bus and previous demo tests: **3,745 passed, 2 skipped**. Separate Vyana tests: **5 passed**. Full upstream suite was NOT run; updater tests expect upstream behavior and are not a Vyana pass claim.
- Local localhost gateway, provider unconfigured, Dream/heartbeat disabled only in temporary verification config: bootstrap HTTP 200; desktop and mobile UI rendered. No prompt sent, no LLM calls or external channel connection. Temporary gateway stopped after inspection.
- Logo inspected at 32/48/96/256 px and in actual browser UI. Supplied artwork retains its profile/colors; white-margin crop used for icons. Mobile sidebar is collapsed by inherited design.

## Deliberate Vyana changes

Vyana command/package metadata, default ~/.vyana instance directory, supplied logo/favicon/app assets, visible product copy, and update execution/staging guards. Internal nanobot modules/protocols remain. Existing nanobot compatibility commands are installed too. Default workspace follows Vyana home, but inherited prompts/docs can still mention Nanobot. Upstream update-check metadata and help references may still describe upstream; do not use upstream release installers for Vyana.

## Not verified

Windows runtime, OS version/architecture support matrix, native TUI binaries, packaged desktop app, Docker/deployment, real provider/authentication behavior, channel delivery, every tool, complete test suite, dependency vulnerability/security audit, local-model fit or resource improvement. No model account, API keys or paid access are supplied. This is a working source adaptation baseline, not production certification.

Requested resource/OS targets are pending future implementation/benchmarks. Architecture is retained first; no feature-removal or fixed-RAM promise was made. Local source-build success does not prove compatibility or low memory on another machine.
