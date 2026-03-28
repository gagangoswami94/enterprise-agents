## What does this PR do?

<!-- One sentence summary -->

## Agent information (for new/updated agents)

| Field | Value |
|---|---|
| Agent name | |
| Category | `engineering` / `marketing` / `finance` / ... |
| File path | `category/category-agent-name.md` |

## Motivation

Why is this agent needed? What gap does it fill?

## Testing

How have you tested this agent? Include real-world use cases or prompts you tried.

## Checklist

- [ ] Agent follows the required frontmatter format (`name`, `description`, `color`)
- [ ] All three recommended sections present: Identity, Core Mission, Critical Rules
- [ ] File name matches convention: `{category}-{role}.md`
- [ ] `python agents.py lint path/to/agent.md` passes with no errors
- [ ] Tested with at least one AI tool in a real scenario
- [ ] No generated output files committed (`integrations/` is gitignored)

## For non-agent PRs

- [ ] Discussed in a GitHub Discussion before implementation
- [ ] Changes do not bulk-modify existing agent files without prior alignment
