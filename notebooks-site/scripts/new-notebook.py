#!/usr/bin/env python3
"""
new-notebook.py — Quickly create a new notebook entry.
Usage: python3 scripts/new-notebook.py "My Topic Title"
"""

import sys
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
NOTEBOOKS_DIR = ROOT / "notebooks"


def slugify(title):
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = slug.strip('-')
    return slug


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/new-notebook.py \"My Topic Title\"")
        sys.exit(1)

    title = " ".join(sys.argv[1:])
    slug = slugify(title)
    filename = NOTEBOOKS_DIR / f"{slug}.md"

    if filename.exists():
        print(f"File already exists: {filename}")
        sys.exit(1)

    now = datetime.now().strftime("%d %b %Y %H:%M")

    content = f"""---
title: {title}
date: {now}
---

# {title}

*[Start your notes here.]*

## References

## See Also
"""

    filename.write_text(content, encoding="utf-8")
    print(f"Created: {filename}")
    print(f"Edit it, then run: python3 scripts/build.py")


if __name__ == "__main__":
    main()
