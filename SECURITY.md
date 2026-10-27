# Vyana security status

Vyana inherits Nanobot tools, gateway, channels and their risks. This adaptation has not received a full security audit. Read [upstream security details](docs/UPSTREAM_SECURITY.md), but upstream security contacts and releases do not make Vyana an official upstream distribution.

Do not commit credentials/runtime data. Use an isolated environment, localhost access, a scoped workspace and reviewed tool permissions. File/shell tools can affect the machine; the inherited UI may start in Full Access. No production-safety guarantee is made. Real providers/channels require separate setup and permission. Automatic upstream package update staging/execution is blocked in this adaptation.
