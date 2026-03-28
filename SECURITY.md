# Security Policy

## Supported Versions

Enterprise Agents is a collection of Markdown files and a Python CLI. There is no compiled binary, no server, and no credential handling in the project itself.

| Component | Security scope |
|---|---|
| Agent `.md` files | No execution context — static text definitions |
| `agents.py` CLI | Reads/writes local files only — no network calls |
| `integrations/` output | Generated config files — no sensitive data |

## Reporting a Vulnerability

If you discover a security issue in this project (e.g., a malicious agent definition that could be exploited by an AI tool, or a CLI vulnerability), please report it responsibly.

**Do not open a public GitHub issue for security vulnerabilities.**

Instead, report it via one of:
- [GitHub Private Security Advisory](https://github.com/gagangoswami94/enterprise-agents/security/advisories/new)
- Email: (maintainer contact via GitHub profile)

Include:
1. Description of the vulnerability
2. Steps to reproduce
3. Potential impact
4. Suggested fix (if any)

We will acknowledge reports within 48 hours and aim to resolve confirmed issues within 14 days.

## Scope

This project does not handle credentials, user data, API keys, or network traffic. The primary security concern is agent content — an agent definition that instructs an AI to take harmful, deceptive, or unauthorized actions would be considered a security issue and will be removed.
