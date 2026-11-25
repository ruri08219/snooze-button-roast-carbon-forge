#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Standard library only.
"""
import os
import sys

ENTRY = "You ring at 6 AM on a Saturday \u2014 the only thing you have ever woken up is my hatred for you."
MAX_CHARS = 200


def validate(text):
    """Return an error string, or None when the entry is valid."""
    if not text or not text.strip():
        return "entry is empty or whitespace-only"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the %d cap" % (len(text), MAX_CHARS)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if any(ord(c) < 0x20 or ord(c) == 0x7F for c in text):
        return "entry contains a control character"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not valid UTF-8-encodable text"
    return None


def main():
    err = validate(ENTRY)
    if err:
        print("invalid entry: %s" % err, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Round-trip verification: what was written is exactly the entry.
    with open(path, "rb") as f:
        if f.read() != data:
            print("round-trip verification failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
