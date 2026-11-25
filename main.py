"""Make the AI Judge Laugh - one-line entry writer.

Writes the entry text to /output/entry.txt and verifies the write
byte-for-byte against the constant below.
"""

import os
import sys

ENTRY = "As an AI language model, I'm not allowed to say I'm tired, so I'll just hallucinate a nap instead."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate guards: 1-200 chars, a single line, not only whitespace,
    # and no trailing newline (the file holds exactly the entry bytes).
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "read-back mismatch: entry.txt differs from ENTRY"

    print(f"Wrote {OUTPUT_PATH}: {len(ENTRY)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
