# Vyana

**Status: reverse-engineering plan + small offline learning scaffold. Not a finished Nanobot replacement.**

Vyana என்பது [HKUDS/nanobot](https://github.com/HKUDS/nanobot)-ஐ புரிந்துகொண்டு உருவாக்கத் தொடங்கும் personal AI assistant project. இந்த repo-வில் architecture analysis, REA evidence summary, build roadmap மற்றும் API key தேவையில்லாத offline CLI demo உள்ளன.

## இப்போது என்ன உள்ளது?

- Nanobot source snapshot-க்கு பொருந்தும் architecture மற்றும் feature map.
- REA 6.8.0 மூலம் உண்மையில் செய்த **selected frontend static analysis**.
- Python backend-க்கு தனியாக செய்த AST + manual source review.
- Vyana product plan, security boundaries மற்றும் acceptance tests.
- Original Python CLI scaffold: `/help`, `/about`, `/quit`; மற்ற text-க்கு தெளிவான demo reply மட்டும்.

**இன்னும் இல்லை:** real AI replies, provider integration, tools, memory persistence, browser UI, channels, authentication, deployment. Nanobot-ன் full renamed copy அல்ல. REA full Python backend-ஐ analyze செய்ததாகக் கூறவில்லை.

## Quick start · Python 3.11+

```sh
python -m pip install -e .
vyana --about
vyana
```

Install இல்லாமலும் repo root-ல்:

```sh
PYTHONPATH=src python -m vyana --about
PYTHONPATH=src python -m vyana
PYTHONPATH=src python -m unittest discover -s tests -v
```

இப்போது எல்லாம் offline. API key, network call, shell execution அல்லது model charge இல்லை.

## படிக்க வேண்டிய வரிசை

1. [Product plan](docs/PRODUCT_PLAN.md) - நம்ம version-ன் proposed scope.
2. [Reverse engineering](docs/REVERSE_ENGINEERING.md) - upstream எப்படி வேலை செய்கிறது.
3. [Architecture](docs/ARCHITECTURE.md) - components மற்றும் message flow.
4. [Roadmap](docs/ROADMAP.md) - அடுத்த milestones + done criteria.
5. [Security](SECURITY.md) - safe defaults மற்றும் public-repo விதிகள்.
6. [Low RAM/CPU plan](docs/LIGHTWEIGHT.md) - confirmed priority, proposed approach, no benchmark claim.
7. [REA method](docs/REA_METHOD.md) - உண்மையில் ஓடிய command, scope, limitations.

## Source & credits

- Upstream: HKUDS/nanobot, Python package version **0.3.5**.
- Reviewed commit: `b07b3eac244ff7faa7eeb2d4777fe54dbae1b6d2`.
- Analysis date: **27 October 2026**.
- Upstream authors: **Xubin Ren and the nanobot contributors**. Their work is not claimed as original Vyana code.
- REA: [morluto/rea](https://github.com/morluto/rea), package `rea-agents@6.8.0`, MIT, copyright morluto.
- [License](LICENSE), [upstream license](LICENSES/nanobot-MIT.txt), [attribution](NOTICE.md), [third-party notes](THIRD_PARTY_NOTICES.md).

Vyana name is the requested working project name. Trademark/domain availability has not been checked. No affiliation with HKUDS, Nanobot, or REA is implied. No deployment or paid service is configured.
