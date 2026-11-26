#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun bounty entry.

Writes exactly one emoji to the path in OUTPUT_PATH
(default /output/entry.txt): a smiling face with smiling eyes.

Why this emoji: it is warm at first glance, readable by a stranger
of any age or background with no context, gentle rather than loud,
and it feels chosen for the moment instead of being the first smiley
that comes to mind. No intimacy, sarcasm or flirtation — just a
kind, open smile from someone unknown.

Deterministic: no input, no network, no randomness, no time or
environment dependence beyond OUTPUT_PATH. Every run writes the
same single emoji.
"""

import os

EMOJI = "\U0001F60A"  # 😊 smiling face with smiling eyes

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def resolve_output_path() -> str:
    """Return the output path, honouring OUTPUT_PATH when set."""
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)


def main() -> None:
    output_path = resolve_output_path()
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
