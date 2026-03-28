# Integrations

This directory contains converted agent formats for all supported AI coding tools.
The source of truth is always the category directories (`engineering/`, `marketing/`, etc.).
Never edit files here directly — regenerate them with the CLI.

## Supported Tools

- **[Claude Code](#claude-code)** — `.md` agents, direct install
- **[GitHub Copilot](#github-copilot)** — `.md` agents, direct install
- **[Antigravity](#antigravity)** — `SKILL.md` per agent
- **[Gemini CLI](#gemini-cli)** — extension + `SKILL.md` files
- **[OpenCode](#opencode)** — `.md` agent files (project-scoped)
- **[OpenClaw](#openclaw)** — `SOUL.md` + `AGENTS.md` + `IDENTITY.md` workspaces
- **[Cursor](#cursor)** — `.mdc` rule files (project-scoped)
- **[Aider](#aider)** — `CONVENTIONS.md` (project-scoped)
- **[Windsurf](#windsurf)** — `.windsurfrules` (project-scoped)
- **[Kimi Code](#kimi-code)** — YAML agent specs

## Quick Install

```bash
# Install for all auto-detected tools
python agents.py install

# Install for a specific tool
python agents.py install --tool claude-code
python agents.py install --tool antigravity
python agents.py install --tool openclaw
```

For project-scoped tools (Cursor, Windsurf, Aider, OpenCode, Qwen), run from your target project root.

## Regenerate After Editing Agents

```bash
python agents.py convert
```

---

## Claude Code

Agents install directly as `.md` files — no conversion needed.

```bash
python agents.py install --tool claude-code
```

---

## GitHub Copilot

Agents copy directly to `~/.github/agents/` and `~/.copilot/agents/`.

```bash
python agents.py install --tool copilot
```

---

## Antigravity

Each agent becomes a skill in `~/.gemini/antigravity/skills/`.

```bash
python agents.py install --tool antigravity
```

---

## Gemini CLI

Packaged as a Gemini CLI extension in `~/.gemini/extensions/enterprise-agents/`.

```bash
python agents.py convert --tool gemini-cli
python agents.py install --tool gemini-cli
```

---

## OpenCode

Project-scoped — run from your project root.

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool opencode
python /path/to/enterprise-agents/agents.py install --tool opencode
```

---

## OpenClaw

Each agent becomes a workspace with `SOUL.md`, `AGENTS.md`, and `IDENTITY.md`.

```bash
python agents.py convert --tool openclaw
python agents.py install --tool openclaw
```

---

## Cursor

Project-scoped — run from your project root.

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool cursor
python /path/to/enterprise-agents/agents.py install --tool cursor
```

---

## Aider

All agents consolidated into a single `CONVENTIONS.md` in your project root.

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool aider
python /path/to/enterprise-agents/agents.py install --tool aider
```

---

## Windsurf

All agents consolidated into `.windsurfrules` in your project root.

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool windsurf
python /path/to/enterprise-agents/agents.py install --tool windsurf
```

---

## Kimi Code

Agents install to `~/.config/kimi/agents/`.

```bash
python agents.py convert --tool kimi
python agents.py install --tool kimi
```
