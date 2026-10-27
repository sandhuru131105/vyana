"""Vyana launches the inherited Nanobot architecture, not the old demo."""
from __future__ import annotations

def main() -> None:
    from nanobot.cli.entry import main as upstream_main
    upstream_main()
