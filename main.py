#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers (make.fun, main account).

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt. Pure standard library, deterministic:
the same bytes on every run.
"""
import os

LINE = "Beware the code that works on the first try; it is only saving its failure for demo day."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
