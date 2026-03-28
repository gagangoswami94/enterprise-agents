# Aider Integration

All agents are consolidated into a single `CONVENTIONS.md` file.
Aider reads this automatically when present in your project root.

## Install

```bash
cd /your/project
python /path/to/enterprise-agents/agents.py convert --tool aider
python /path/to/enterprise-agents/agents.py install --tool aider
```

## Activate an Agent

In your Aider session, reference the agent by name:

```
Use the Frontend Developer agent to refactor this component.
```

## Manual Usage

```bash
aider --read CONVENTIONS.md
```

## Regenerate

```bash
python agents.py convert --tool aider
```
