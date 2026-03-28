# Gemini CLI Integration

Packages all agents as a Gemini CLI extension. Installs to `~/.gemini/extensions/enterprise-agents/`.

## Install

```bash
python agents.py convert --tool gemini-cli
python agents.py install --tool gemini-cli
```

## Activate a Skill

In Gemini CLI, reference an agent by name:

```
Use the frontend-developer skill to help me build this UI.
```

## Extension Structure

```
~/.gemini/extensions/enterprise-agents/
  gemini-extension.json
  skills/
    frontend-developer/SKILL.md
    backend-architect/SKILL.md
    ...
```

## Regenerate

```bash
python agents.py convert --tool gemini-cli
```
