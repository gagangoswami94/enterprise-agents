# Cursor Integration

Converts all agents into Cursor `.mdc` rule files. Rules are **project-scoped** — install from your project root.

## Install

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool cursor
python /path/to/enterprise-agents/agents.py install --tool cursor
```

This creates `.cursor/rules/<agent-slug>.mdc` files in your project.

## Activate a Rule

In Cursor, reference an agent in your prompt:

```
@frontend-developer Review this React component for performance issues.
```

Or enable a rule as always-on by editing its frontmatter:

```yaml
---
description: Expert frontend developer...
globs: "**/*.tsx,**/*.ts"
alwaysApply: true
---
```

## Regenerate

```bash
python agents.py convert --tool cursor
```
