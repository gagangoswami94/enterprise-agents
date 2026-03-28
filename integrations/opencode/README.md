# OpenCode Integration

Agents are `.md` files with YAML frontmatter stored in `.opencode/agents/`.
Named colors are mapped to hex. All agents use `mode: subagent` for on-demand invocation.

## Install

Project-scoped — run from your project root:

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool opencode
python /path/to/enterprise-agents/agents.py install --tool opencode
```

## Activate an Agent

```
@frontend-developer help build this component.
@reality-checker review this PR.
```

## Global Install

```bash
mkdir -p ~/.config/opencode/agents
cp integrations/opencode/agents/*.md ~/.config/opencode/agents/
```

## Regenerate

```bash
python agents.py convert --tool opencode
```
