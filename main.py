#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

Writes one status update, in the voice of a lost sock, to
/output/entry.txt. The gate allows 1-120 UTF-8 characters.
"""

import os

ENTRY = (
    # Premise: the sock was not eaten by the dryer -- it was
    # repurposed as a dust cloth. Its pair kept the good life.
    "Status update: I've been promoted to dust cloth. "
    "My pair still gets feet. "
    "I get the ceiling fan and existential dread."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-120")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
