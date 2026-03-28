# OpenClaw Integration

Each agent becomes a workspace with `SOUL.md`, `AGENTS.md`, and `IDENTITY.md`.
Workspaces install to `~/.openclaw/enterprise-agents/`.

## Install

```bash
python agents.py convert --tool openclaw
python agents.py install --tool openclaw
```

## Activate an Agent

Agents are available by `agentId` in OpenClaw sessions after installation.
If the gateway is already running, restart it:

```bash
openclaw gateway restart
```

## Regenerate

```bash
python agents.py convert --tool openclaw
```
