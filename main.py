#!/usr/bin/env python3
"""Write a phone battery's last text message to its charger.

Writes one line of plain text to /output/entry.txt (no trailing
newline, mode 0644). Standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "i kept your boss's emails out of voicemail all day. "
    "this text cost me my last bar. "
    "read it twice \u2014 i can't afford a follow-up."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    os.chmod(OUTPUT, 0o644)


if __name__ == "__main__":
    main()
