# Provenance and attribution

Vyana 0.1.0 is a source-based adaptation of HKUDS/nanobot, not an independently invented implementation. The runtime, React UI, protocol, native TUI source, tests and developer documentation were imported from commit `b07b3eac244ff7faa7eeb2d4777fe54dbae1b6d2` (version 0.3.5).

Source: https://github.com/HKUDS/nanobot

Copyright (c) 2025-present Xubin Ren and the nanobot contributors. Their MIT notice is preserved in LICENSES/nanobot-MIT.txt. Vyana-specific changes are MIT licensed under LICENSE. THIRD_PARTY_NOTICES.md preserves bundled dependency and font notices. No endorsement or affiliation is claimed.

Vyana changes: product launcher/package metadata, separate ~/.vyana home, supplied logo and visible branding, automatic-updater safety guard, adaptation tests and Vyana documentation. Internal nanobot imports, protocols, many compatibility labels and developer commands intentionally remain to avoid breaking the architecture. The logo was supplied and approved for public project use by the project owner; its provenance/rights are not independently certified.

REA 6.8.0 was used in the earlier partial frontend static analysis. Source: https://github.com/morluto/rea ; MIT notice: LICENSES/rea-MIT.txt. REA is not a runtime dependency. Python was separately inspected, not analyzed by REA.

No model weights, configured credentials, native executables or dependency binaries are committed. Frontend assets are built locally from the retained source; package builds include them with applicable notices.
