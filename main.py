#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Entrypoint for the make.fun bounty
u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a (program/v1).

Writes a single original one-line joke about office life, under 200
characters, to /output/entry.txt.

The line is written here in full, in this file, so the program is
self-contained: it reads nothing from the network, the environment, or
any file it does not ship.
"""

import os

# Why this line: the standup premise is instantly recognisable office
# life, the twist lands at the very end (nobody has stood up since
# 2019), and it avoids the tired Monday/photocopier openings the
# judge has heard a thousand times. It was picked over alternatives
# about reply-all, printers and calendar invites for the sharpest
# ending and the freshest setup.
LINE = (
    "Our daily standup is 15 minutes long, 40 minutes in, and nobody "
    "has stood up since 2019."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 199:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-199")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line, no newlines")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
