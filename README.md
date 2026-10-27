<p align="center"><img src="webui/public/brand/vyana-logo.png" width="160" alt="Vyana logo"></p>

# Vyana

Nanobot design + architecture அடிப்படையில் உருவாக்கப்படும் Vyana personal AI assistant.

**இப்போது:** actual upstream Python runtime + React/TypeScript WebUI source உள்ளது. இது பழைய offline demo மட்டும் இல்லை. இது Nanobot-ன் source-based adaptation; original architecture/credits பாதுகாக்கப்பட்டுள்ளது. Model/provider configure செய்யாமல் AI பதில் கிடைக்காது.

**Verified:** Linux Python 3.11 editable install, production frontend build, local gateway + browser bootstrap, 3,745 selected core tests passed (2 skipped), 5 Vyana boundary tests passed. Windows compatibility, real model calls, external channels, native TUI binaries, Docker and 2 CPU / 4 GB performance இன்னும் test செய்யப்படவில்லை. No deployment or paid model calls.

## Architecture

React WebUI / CLI / channels → gateway + message bus → session/context → provider + agent/tool loop → SQLite/history → streamed response. See [architecture](docs/ARCHITECTURE.md) and [build status](docs/BUILD_STATUS.md).

Internal `nanobot` Python imports/protocol names remain deliberately intact. Product launcher is `vyana`; data defaults to `~/.vyana`. Install into a separate virtual environment, not an existing Nanobot environment.

## Source setup

Requires Python 3.11+ and Node.js/npm for building the UI from source. The following commands use a normal shell; Python activation differs by OS.

```sh
git clone https://github.com/sandhuru131105/vyana.git
cd vyana
python -m venv .venv
```

Windows PowerShell: `.venv\Scripts\Activate.ps1` (subject to your execution policy). Linux: `source .venv/bin/activate`. Then:

```sh
python -m pip install -e .
cd webui
npm ci --ignore-scripts
npm run build
cd ..
python -m vyana --help
python -m vyana webui
```

Follow local first-run setup. Select and configure a provider/model before requesting AI responses. Fees, account terms and privacy depend on that choice; no provider or credentials are included. Browser UI is local by default. Do not expose it publicly without reviewing authentication and access controls.

## Safety and limits

Inherited file/shell tools can modify files and run commands. The UI can show **Full Access** by default. Review access mode, tool permissions, workspace restrictions and [security notes](SECURITY.md) before connecting a model. Do not give an untrusted model broad access to personal/work files. Channels, automation and paid integrations are not configured by this build.

Automatic upstream update execution/staging is blocked in Vyana so a Nanobot release cannot silently overwrite this adaptation. Source updates must be reviewed from this Vyana repo. Upstream installers/release scripts and Docker files are retained for reference, not verified Vyana distribution channels.

## Project notes

- [Build status and deviations](docs/BUILD_STATUS.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Source reverse engineering](docs/REVERSE_ENGINEERING.md)
- [REA scope and evidence](docs/REA_METHOD.md)
- [Deferred low-resource work](docs/LIGHTWEIGHT.md)
- [Roadmap](docs/ROADMAP.md)
- [Attribution](NOTICE.md) and [third-party notices](THIRD_PARTY_NOTICES.md)
- [Upstream guide](docs/UPSTREAM_README.md), describing Nanobot behavior and commands, not verified Vyana releases

Original learning demo is retained as `python -m vyana.demo` for reference; it is not the main application. Hardware and OS targets remain unbenchmarked; architecture first, optimization later.
