"""Deterministic CLI: no network, model, shell or saved history."""
from __future__ import annotations
import argparse
ABOUT = "Vyana 0.0.1 | Offline demo only. No AI provider, tools or saved history."
HELP = "Commands: /help, /about, /quit. Other text gets a demo response, not AI."
MAX_INPUT = 4000

def reply(text: str) -> str:
    text = text.strip()
    if not text:
        return "Type a message or /help."
    if len(text) > MAX_INPUT:
        return f"Message too long. Limit: {MAX_INPUT} characters."
    if text == "/help":
        return HELP
    if text == "/about":
        return ABOUT
    if text == "/quit":
        return "Bye."
    if text.startswith("/"):
        return "Unknown command. Use /help."
    return "Demo மட்டும்: message received. Real AI integration is not built yet."

def main() -> None:
    parser = argparse.ArgumentParser(description=ABOUT)
    parser.add_argument("--about", action="store_true")
    args = parser.parse_args()
    print(ABOUT)
    if args.about:
        return
    print(HELP)
    while True:
        try:
            text = input("You> ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            return
        print(f"Vyana> {reply(text)}")
        if text.strip() == "/quit":
            return
