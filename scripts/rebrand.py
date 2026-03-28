#!/usr/bin/env python3
"""
Rebrand all agents to Enterprise Agents style.
Adds versioning, authorship, header, and footer to all agent files.
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

CATEGORIES = [
    "academic",
    "design",
    "engineering",
    "game-development",
    "marketing",
    "paid-media",
    "product",
    "project-management",
    "sales",
    "spatial-computing",
    "specialized",
    "support",
    "testing",
]

FOOTER = '''
---

## About Enterprise Agents

This agent is part of the **Enterprise Agents** collection - production-ready AI specialists designed to transform your workflow.

- **License**: MIT
- **Version**: 2.0

> Built with insights from the open-source community. Enhanced for production use.
'''

def process_file(filepath: Path) -> bool:
    """Process a single agent file."""
    content = filepath.read_text(encoding='utf-8')

    # Skip if already branded
    if "Enterprise Agents" in content:
        return False

    modified = False

    # Add version and author to frontmatter
    if content.startswith('---'):
        # Find the end of frontmatter
        second_dash = content.find('---', 3)
        if second_dash != -1:
            frontmatter = content[3:second_dash]
            rest = content[second_dash:]

            # Add version and author if not present
            if 'version:' not in frontmatter:
                frontmatter = frontmatter.rstrip() + '\nversion: "2.0"\n'
                modified = True
            if 'author:' not in frontmatter:
                frontmatter = frontmatter.rstrip() + '\nauthor: "Enterprise Agents"\n'
                modified = True

            content = '---' + frontmatter + rest

    # Add header after first H1
    h1_match = re.search(r'^(# .+)$', content, re.MULTILINE)
    if h1_match and "> Part of **Enterprise Agents**" not in content:
        h1_end = h1_match.end()
        header_text = '\n\n> Part of **Enterprise Agents** - Your AI Dream Team'
        content = content[:h1_end] + header_text + content[h1_end:]
        modified = True

    # Add footer if not present
    if "## About Enterprise Agents" not in content:
        content = content.rstrip() + FOOTER
        modified = True

    if modified:
        filepath.write_text(content, encoding='utf-8')

    return modified

def main():
    print("=" * 50)
    print("  Enterprise Agents - Rebranding Script")
    print("=" * 50)
    print()

    total_files = 0
    processed_files = 0

    for category in CATEGORIES:
        category_path = ROOT_DIR / category

        if not category_path.exists():
            print(f"[WARN] Category not found: {category}")
            continue

        print(f"Processing: {category}/")

        # Find all .md files recursively
        for filepath in category_path.rglob("*.md"):
            # Skip README files
            if filepath.name == "README.md":
                continue

            total_files += 1

            try:
                if process_file(filepath):
                    print(f"  [OK] Rebranded: {filepath.relative_to(ROOT_DIR)}")
                    processed_files += 1
                else:
                    print(f"  [SKIP] Already branded: {filepath.relative_to(ROOT_DIR)}")
            except Exception as e:
                print(f"  [ERR] Failed: {filepath.relative_to(ROOT_DIR)} - {e}")

        print()

    print("=" * 50)
    print(f"  Rebranding Complete!")
    print(f"  Total files: {total_files}")
    print(f"  Processed: {processed_files}")
    print("=" * 50)

if __name__ == "__main__":
    main()
