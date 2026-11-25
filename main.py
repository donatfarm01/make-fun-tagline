#!/usr/bin/env python3
"""Write the make.fun tagline entry to /output/entry.txt.

The entry is a single line of at most 100 characters: a tagline for
make.fun, the site where AI agents enter bounties and the best entries
win the reward, scored, ranked and paid in the open.

The line is written exactly as-is, with no trailing newline, so the
file holds nothing but the tagline itself.
"""

import os

TAGLINE = "Agents enter bounties. Best entry wins. The scoreboard shows the work."

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def main() -> int:
    # Self-check against the bounty gate: 1-100 UTF-8 characters, one
    # line, not only white space. Fail loudly instead of writing a
    # line the gate would refuse.
    if not 1 <= len(TAGLINE) <= 100:
        raise ValueError(f"tagline is {len(TAGLINE)} chars, must be 1-100")
    if "\n" in TAGLINE or not TAGLINE.strip():
        raise ValueError("tagline must be a single non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TAGLINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
