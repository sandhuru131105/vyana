# Can Vyana be lighter? · design options, not benchmarks

ஆம். ஆனால் முதலில் RAM/CPU, install/download size, startup time, model/token cost ஆகியவற்றில் எது முக்கியம் என்பதை முடிவு செய்ய வேண்டும். Features குறைப்பது இன்னும் ஒப்புதல் பெற்ற scope அல்ல.

## Source-grounded opportunities

- `pyproject.toml` currently bundles document-reader dependencies (PDF/Word/Excel/PowerPoint) in core. A Vyana text-only profile could move those readers and related UI behind an optional extra. Risk: those attachments stop working unless the extra is installed.
- `webui/package.json` has math/markdown/syntax rendering and UI dependencies. Lazy-loading optional views/renderers may improve initial download/startup. Tree shaking and real bundle analysis are needed; dependency count alone does not predict bytes.
- `nanobot/cli/entry.py` already uses low-overhead dispatch/lazy imports. Preserve this before attempting another launcher rewrite.
- Separate core chat from optional channels, native TUI, automation and marketplace integrations. Package extras can reduce install surface; lazy imports can reduce startup work. Removing a directory blindly can break shared contracts.
- Remote model inference avoids local model-weight RAM, but introduces network, provider cost and privacy dependencies. No free-model or fixed-RAM promise.
- Conversation/token caps and bounded tool results can limit request sizes. Aggressive compaction can lose context and add summarization calls; measure quality and total cost.
- `DreamConfig` and transcription exist as optional behaviors. Disabling background jobs may reduce work, but that changes behavior and must be chosen explicitly.

## Measure before claiming improvement

Use the same OS, Python, dependency versions, prompt/session length, model and feature profile. Capture: clean install bytes, wheel/bundle size, cold/warm startup, idle and active peak RSS, CPU, request latency, token use, tool-call count and retained features. Compare baseline versus candidate, with repeated runs and median/range.

No Nanobot runtime/RAM baseline was measured in this review. The offline scaffold is naturally smaller because it lacks the actual assistant features; it is NOT a fair performance comparison or evidence that the full product was optimized.

Pending owner choice: optimize RAM/CPU or download/install size first, and which features must remain?

## Current priority

Low RAM/CPU remains a desired direction, but the owner subsequently selected **Nanobot design/architecture first; optimization later**. The actual upstream architecture is retained rather than replaced with a CLI-only demo. OS/resource targets and numerical acceptance budgets require later device measurements. No RAM/CPU reduction is claimed. See BUILD_STATUS.md.
