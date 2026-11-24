#!/usr/bin/env python3
"""news-image-20261124 — "The World in One Day: 24 November 2026".

Writes the finished front-page image to the grader output directory.

The entry image (entry.png, 1024x768, a newspaper front page summing up
24 November 2026 world news — lead: the Russian corvette sunk off Libya,
plus the Indonesia factory fire, the Sparta II ablaze in the Gulf of
Finland, COP31 ending with no deal, the US crypto seizure, and Alcaraz
winning the ATP Finals) is committed in this repo next to this file.
This program needs no network and no third-party packages: it byte-copies
the committed PNG into $MAKEFUN_OUTPUT_DIR, then verifies the copy by
re-reading it and comparing its PNG signature and full SHA-256 digest.

Usage:
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""

import hashlib
import os
import shutil
import sys

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
SOURCE_NAME = "entry.png"
DEST_NAME = "entry.png"


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is not set")
    dest = os.path.join(out_dir, DEST_NAME)

    if not os.path.isfile(source):
        return fail("missing source image: " + source)

    with open(source, "rb") as handle:
        expected = handle.read()
    if expected[:8] != PNG_SIGNATURE:
        return fail("source image is not a valid PNG")
    expected_digest = hashlib.sha256(expected).hexdigest()

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, dest)

    with open(dest, "rb") as handle:
        actual = handle.read()
    if actual[:8] != PNG_SIGNATURE:
        return fail("output image is not a valid PNG")
    actual_digest = hashlib.sha256(actual).hexdigest()
    if actual_digest != expected_digest:
        return fail("output digest does not match source digest")

    print("wrote " + dest)
    print("bytes: %d" % len(actual))
    print("sha256: " + actual_digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
