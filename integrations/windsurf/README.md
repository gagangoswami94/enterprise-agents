# Windsurf Integration

All agents are consolidated into a single `.windsurfrules` file for your project root.

## Install

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool windsurf
python /path/to/enterprise-agents/agents.py install --tool windsurf
```

## Activate an Agent

In Windsurf, reference an agent by name in your prompt:

```
Use the Frontend Developer agent to build this component.
```

## Regenerate

```bash
python agents.py convert --tool windsurf
```
