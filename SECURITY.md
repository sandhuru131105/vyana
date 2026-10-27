# Vyana security status

This is an early offline scaffold, not an audited AI assistant. Do not use it for sensitive work or expose a future development server publicly.

Current CLI performs no network, model, file-write, shell or external-message operations. It prints demo text and does not save chat history.

Future implementation must keep secrets server-side/outside git; default to localhost; require authentication before remote binding; scope filesystem reads; deny symlink/path escapes; bound time, bytes and model/tool iterations; implement cancellation; require appropriate approval for writes, messages, purchases and account changes; and test prompt-injection resistance. OS isolation is separate from prompt instructions. Nanobot's security documentation says its optional command sandbox does not restrict network access; do not treat copying a config as a complete sandbox.

No provider/API key is required by this scaffold. Never commit `.env`, real config, chat databases, tokens, logs or private workspace contents. An `.env.example` must contain placeholders only. If a secret is accidentally published, revoke it immediately; deleting the latest line does not erase Git history.

Upstream guidance: https://github.com/HKUDS/nanobot/blob/main/SECURITY.md

No private vulnerability-reporting mailbox has been designated for Vyana yet. Do not post credentials or private data in public issues.
