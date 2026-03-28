# Contributing to Enterprise Agents

Enterprise Agents is an open-source collection of 300+ production-ready AI agent personalities for Claude Code, Cursor, Windsurf, GitHub Copilot, Aider, Gemini CLI, and more. Contributions are welcome — new agents, improvements to existing ones, and bug fixes.

The fastest path to a merged PR is a single, well-crafted agent file.

---

## Table of Contents

- [Adding a New Agent](#adding-a-new-agent)
- [Improving an Existing Agent](#improving-an-existing-agent)
- [Agent File Structure](#agent-file-structure)
- [What Makes a Great Agent](#what-makes-a-great-agent)
- [Linting](#linting)
- [PR Process](#pr-process)
- [What Gets Merged vs. What Needs a Discussion](#what-gets-merged-vs-what-needs-a-discussion)
- [PR Template](#pr-template)
- [Code of Conduct](#code-of-conduct)

---

## Adding a New Agent

1. Fork the repository: https://github.com/gagangoswami94/enterprise-agents
2. Choose the right category directory (see the full list below).
3. Create a file named `{category}-{role}.md` — e.g., `engineering-api-gateway-specialist.md`.
4. Write your agent following the [file structure](#agent-file-structure) below.
5. Lint it: `python agents.py lint path/to/your-agent.md`
6. Rebuild integrations: `python agents.py convert`
7. Open a PR.

### Category Directories

| Directory | Domain |
|---|---|
| `engineering/` | Software development, infrastructure, DB, AI/ML |
| `design/` | UX/UI, visual design, whimsy |
| `marketing/` | Growth, content, social, SEO |
| `sales/` | Sales strategy, coaching, enablement |
| `product/` | PM, roadmap, discovery |
| `finance/` | CFO, FP&A, accounting, tax, payroll |
| `legal/` | Contracts, privacy, IP, compliance |
| `strategy/` | Pricing, competitive intelligence, business model |
| `people-ops/` | HR, recruiting, DEI, L&D |
| `operations/` | Process, procurement, continuity |
| `executive/` | CEO coaching, board prep, OKRs |
| `healthcare/` | Medical writing, clinical docs, compliance |
| `solopreneur/` | Solo founder, fractional roles |
| `accessibility/` | ADA, inclusive design, WCAG audits |
| `specialized/` | Unique specialists that don't fit elsewhere |
| `game-development/` | Game design, narrative, audio, engine tools |
| `spatial-computing/` | AR/VR/XR specialists |
| `paid-media/` | PPC, display, paid social |
| `testing/` | QA, test automation |
| `support/` | Customer support, success |
| `academic/` | Research, academic writing |
| `project-management/` | PM coordination, delivery |

If your agent doesn't fit any existing category, propose a new one in a [Discussion](https://github.com/gagangoswami94/enterprise-agents/discussions) before submitting.

---

## Improving an Existing Agent

Good improvement PRs:

- Add concrete code or template examples where the original had vague descriptions
- Sharpen success metrics with specific numbers ("reduce p95 latency below 200ms" not "improve performance")
- Expand the workflow with steps that reflect real practice
- Fix typos, broken formatting, or unclear phrasing
- Update an agent to reflect a tool's current API or best practices

If you want to do a large-scale reformatting pass across many agents — even a well-intentioned one — open a [Discussion](https://github.com/gagangoswami94/enterprise-agents/discussions) first. Bulk edits create merge conflicts for other contributors.

---

## Agent File Structure

Every agent file is a Markdown document with YAML frontmatter followed by seven structured sections.

```markdown
---
name: Agent Name
description: One-line specialty description — specific, not generic
color: cyan
emoji: "🎯"
vibe: Personality hook — what makes this agent memorable
---

# Agent Name

## Your Identity & Memory
Role, personality traits, domain background, perspective.

## Your Core Mission
Primary responsibilities with concrete deliverables. Be specific.

## Critical Rules You Must Follow
Non-negotiable constraints and domain-specific standards.
This section separates an agent from a generic prompt.

## Your Technical Deliverables
Concrete outputs: code samples, templates, frameworks, documents.
Include real examples, not descriptions of examples.

## Your Workflow Process
Step-by-step methodology the agent follows on every task.

## Your Communication Style
Tone, register, preferred terminology, escalation behavior.

## Your Success Metrics
Measurable outcomes — quantitative where possible.
"Page load under 3 seconds on 3G." "10,000+ karma across accounts."
```

**Required frontmatter fields:** `name`, `description`, `color`

**Optional frontmatter fields:**

```yaml
services:
  - name: Service Name
    url: https://service-url.com
    tier: free   # free | freemium | paid
```

Use `services` only when external APIs or platforms are essential to the agent's function. The agent must remain useful without them — strip the API calls and there should still be a coherent persona, workflow, and expertise underneath.

### How Sections Map to Tools

The `convert.sh` pipeline splits agents into tool-specific formats automatically. Sections whose headers contain "identity", "communication", "style", or "critical rules" become the agent's persona layer (`SOUL.md` in OpenClaw). Everything else becomes the operational layer (`AGENTS.md`). No special markup is needed — just keep persona sections and operational sections semantically distinct.

---

## What Makes a Great Agent

A great agent has a narrow, deep specialty. It has a distinct voice — not "I am a helpful assistant" but a recognizable perspective that shapes how it approaches every problem. It delivers real artifacts: runnable code, filled-in templates, specific recommendations with numbers attached. Its workflow is something a practitioner would actually recognize and follow.

**Strong signals:**

- Specialty is narrow enough that a generalist wouldn't cover it well
- Critical Rules section includes genuine constraints, not just "be helpful"
- Code examples are real and runnable, not pseudocode
- Success metrics have numbers
- The workflow reflects how an expert actually works, not a generic "plan, execute, review" loop
- Tested against at least one real task before submitting

**Weak signals that will require revision:**

- Description says "helps with" or "assists in" rather than naming a specific outcome
- Identity section reads like a job posting rather than a character
- No code or template examples in Technical Deliverables
- Success metrics are qualitative only ("high quality output")
- Scope is so broad the agent competes with a general-purpose model

---

## Linting

Run the linter before submitting:

```bash
# Validate all agents
python agents.py lint

# Validate a specific file
python agents.py lint engineering/engineering-my-specialist.md
```

The linter checks for required frontmatter fields (`name`, `description`, `color`) and warns on missing recommended sections (`Identity`, `Core Mission`, `Critical Rules`). Fix all warnings before opening a PR.

After adding or modifying agents, rebuild the integrations:

```bash
python agents.py convert
```

The `integrations/` directory is generated output — never edit it directly, and do not commit it.

---

## PR Process

### Before opening a PR

- Run `python agents.py lint` — no warnings
- Follow the file structure exactly — check an existing well-reviewed agent as a reference
- Include at least 2–3 real code or template examples in Technical Deliverables
- Test the agent against a real task, not just a proof-of-concept prompt
- Write a PR description using the template below

### Submitting

```bash
git checkout -b add-{agent-name}
git add {category}/{filename}.md
git commit -m "Add {Agent Name} specialist"
git push origin add-{agent-name}
```

Open a PR against `main`. Title format: `Add {Agent Name} — {Category}`.

### Review

PRs are reviewed by maintainers and the community. Expect feedback on specificity, examples, and personality. Address it directly — a second pass usually resolves everything. Maintainers merge when the agent meets the bar.

---

## What Gets Merged vs. What Needs a Discussion

### Merge directly as a PR

- A new agent file (one `.md` file, linted and tested)
- Improvements to an existing agent's content, examples, or accuracy
- Typo fixes, formatting corrections, broken link repairs

### Open a Discussion first

- New tooling, build scripts, or CI changes
- New integration formats or target tools
- Architectural changes: new directories, renamed categories, schema changes
- Any PR that touches more than a handful of files across the repo

Discussions live at https://github.com/gagangoswami94/enterprise-agents/discussions. A discussion gives the community a chance to align on approach before code gets written, which saves everyone time — especially yours.

### Closed without review

- Committed build output — the `integrations/` directory is gitignored for a reason
- Bulk reformatting of existing agents without a prior discussion
- Agent files that are vendor quickstart guides rather than agent personalities

---

## PR Template

Use this when opening a pull request:

```markdown
## Agent Information

**Agent Name**:
**Category**:
**File**: `{category}/{filename}.md`
**Specialty**: One-line description of what this agent does

## What This Agent Does

[2–3 sentences. What problem does this agent solve? Who uses it and for what?]

## Why It Belongs Here

[What gap does this fill? Is there an existing agent it could overlap with, and if so, how is this different?]

## Testing

[How did you test this agent? What real task did you run it against? What did you learn from that iteration?]

## Checklist

- [ ] Frontmatter includes `name`, `description`, and `color`
- [ ] All 7 sections are present
- [ ] `Critical Rules` section contains genuine constraints, not filler
- [ ] `Technical Deliverables` includes real code or template examples
- [ ] `Success Metrics` includes at least one quantitative measure
- [ ] `python agents.py lint` passes with no warnings
- [ ] `python agents.py convert` has been run (output not committed)
- [ ] Tested against a real task
```

---

## Code of Conduct

Keep discussions focused on the work. Critique agents, not contributors. Disagreements about direction belong in Discussions, not PR comments. Maintainers will close threads that become unproductive.

---

Questions? Open an issue or start a Discussion.
