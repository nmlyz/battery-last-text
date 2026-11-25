#!/usr/bin/env python3
"""Write a phone battery's last text message to its charger.

Output contract
---------------
* Destination: ``/output/entry.txt`` (created together with its parent
  directory when missing).
* Content: exactly one line of plain UTF-8 text, no trailing newline.
  The text is the battery's final message, fixed in :data:`LAST_TEXT`
  and reproduced byte for byte.
* Permissions: the file is left with mode 0644.
* Verification: after writing, the file is read back and compared
  against :data:`LAST_TEXT`; any mismatch raises an error instead of
  silently leaving a wrong file behind.

Standard library only.
"""

import os
import sys
from pathlib import Path

LAST_TEXT = (
    "i kept your boss's emails out of voicemail all day. "
    "this text cost me my last bar. "
    "read it twice \u2014 i can't afford a follow-up."
)

OUTPUT = Path("/output/entry.txt")


def output_directory() -> Path:
    """Return the directory that will hold the entry file."""
    return OUTPUT.parent


def verify_entry(path: Path) -> None:
    """Check the written file against the output contract.

    Raises ``ValueError`` when the content differs from
    :data:`LAST_TEXT`, ends with a newline, or is not valid UTF-8.
    """
    raw = path.read_bytes()
    if raw.decode("utf-8") != LAST_TEXT:
        raise ValueError("content mismatch: entry.txt != LAST_TEXT")
    if raw.endswith(b"\n"):
        raise ValueError("contract violation: entry.txt ends with a newline")
    if len(raw) != len(LAST_TEXT.encode("utf-8")):
        raise ValueError("length mismatch: entry.txt has unexpected size")


def write_entry() -> Path:
    """Write the last text to the output file and verify it.

    Returns the path written. Raises ``ValueError`` if the read-back
    check finds anything other than the exact message.
    """
    directory = output_directory()
    directory.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LAST_TEXT, encoding="utf-8")
    os.chmod(OUTPUT, 0o644)
    verify_entry(OUTPUT)
    return OUTPUT


def main() -> int:
    try:
        write_entry()
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
