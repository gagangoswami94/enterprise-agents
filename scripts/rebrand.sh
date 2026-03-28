#!/bin/bash
# Rebrand all agents to Enterprise Agents style
# This script adds versioning, authorship, and footer to all agent files

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Categories to process
CATEGORIES=(
    "academic"
    "design"
    "engineering"
    "game-development"
    "marketing"
    "paid-media"
    "product"
    "project-management"
    "sales"
    "spatial-computing"
    "specialized"
    "support"
    "testing"
)

# Footer to add
FOOTER='
---

## About Enterprise Agents

This agent is part of the **Enterprise Agents** collection - production-ready AI specialists designed to transform your workflow.

- **Repository**: [github.com/agents-crew](https://github.com/agents-crew)
- **License**: MIT
- **Version**: 2.0

> Built with insights from the open-source community. Enhanced for production use.
'

process_file() {
    local file="$1"
    local temp_file="${file}.tmp"

    # Check if file already has Enterprise Agents branding
    if grep -q "Enterprise Agents" "$file" 2>/dev/null; then
        echo "  [SKIP] Already branded: $file"
        return
    fi

    # Add version and author to frontmatter if not present
    if head -1 "$file" | grep -q "^---"; then
        # File has frontmatter, update it
        awk '
        BEGIN { in_frontmatter=0; added_fields=0 }
        /^---$/ && NR==1 { in_frontmatter=1; print; next }
        /^---$/ && in_frontmatter==1 {
            if (!added_fields) {
                print "version: \"2.0\""
                print "author: \"Enterprise Agents\""
            }
            in_frontmatter=0
            print
            next
        }
        in_frontmatter && /^version:/ { added_fields=1 }
        in_frontmatter && /^author:/ { added_fields=1 }
        { print }
        ' "$file" > "$temp_file"
    else
        cp "$file" "$temp_file"
    fi

    # Add Enterprise Agents header after the first heading
    sed -i.bak '0,/^# /{s/^# \(.*\)/# \1\n\n> Part of **Enterprise Agents** - Your AI Dream Team/}' "$temp_file" 2>/dev/null || \
    sed -i '' '0,/^# /{s/^# \(.*\)/# \1\
\
> Part of **Enterprise Agents** - Your AI Dream Team/}' "$temp_file"

    # Add footer if not present
    if ! grep -q "About Enterprise Agents" "$temp_file"; then
        echo "$FOOTER" >> "$temp_file"
    fi

    # Move temp file to original
    mv "$temp_file" "$file"
    rm -f "${temp_file}.bak" 2>/dev/null || true

    echo "  [OK] Rebranded: $file"
}

echo "=========================================="
echo "  Enterprise Agents - Rebranding Script"
echo "=========================================="
echo ""

total_files=0
processed_files=0

for category in "${CATEGORIES[@]}"; do
    category_path="$ROOT_DIR/$category"

    if [[ ! -d "$category_path" ]]; then
        echo "[WARN] Category not found: $category"
        continue
    fi

    echo "Processing: $category/"

    # Process all .md files in category (including subdirectories)
    while IFS= read -r -d '' file; do
        # Skip README files
        if [[ "$(basename "$file")" == "README.md" ]]; then
            continue
        fi

        ((total_files++))
        process_file "$file"
        ((processed_files++))
    done < <(find "$category_path" -name "*.md" -type f -print0)

    echo ""
done

echo "=========================================="
echo "  Rebranding Complete!"
echo "  Total files: $total_files"
echo "  Processed: $processed_files"
echo "=========================================="
