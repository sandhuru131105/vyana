# Vyana product plan · proposed

## Confirmed request

Use REA to understand HKUDS/nanobot, plan Vyana and create a public `vyana` repository. No deployment, paid API calls or channel-account connection was requested.

## Suggested first product

A local-first personal assistant with clear Tamil explanations and visible tool actions. This is a product hypothesis, not a confirmed differentiation or market-validation result.

## First useful version

1. Local text chat with one explicitly configured provider.
2. Visible conversation history with export/delete.
3. One read-only workspace tool, scoped to a selected directory.
4. Clear permission prompts before any later write/external-send action.
5. Usage/error/cancel states and no hidden background spending.

## Exclude initially

Multi-user SaaS, billing, all channels, background automation, arbitrary shell, browser control, plugin marketplace, native TUI packaging and remote network exposure. Existing upstream features are not automatically in Vyana's MVP.

## Current deliverable

Planning documents + measured partial REA frontend analysis + backend static inventory + offline demonstration scaffold. No real AI exists yet in the scaffold. This avoids claiming a renamed upstream project is a new finished product.

## Next owner decision

Choose first experience: **local CLI chat** (simpler to test) or **browser chat UI** (more frontend work). Also choose whether to adapt MIT upstream implementation or keep a small independent implementation. Provider/budget selection is needed only before real API integration, not for the current offline demo.

## Confirmed performance goal

Low RAM/CPU is the owner's priority. See [lightweight options](LIGHTWEIGHT.md). Hardware, numeric budget and must-keep features are still unknown. No measured full-product reduction is claimed.
