<div align="center">

# Enterprise Agents — 280+ AI Agent Personalities for Claude Code, Cursor & Windsurf

**The largest open-source collection of production-ready AI agent personalities. Deploy specialist subagents into Claude Code, Cursor rules, Windsurf, GitHub Copilot, Aider, and 6 more tools — in one command.**

[![Agents](https://img.shields.io/badge/agents-280%2B-blueviolet?style=for-the-badge)](https://github.com/gagangoswami94/enterprise-agents)
[![Domains](https://img.shields.io/badge/domains-30-blue?style=for-the-badge)](https://github.com/gagangoswami94/enterprise-agents)
[![Tools](https://img.shields.io/badge/tools-11-green?style=for-the-badge)](https://github.com/gagangoswami94/enterprise-agents)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen?style=for-the-badge)](agents.py)

```bash
git clone https://github.com/gagangoswami94/enterprise-agents.git
cd enterprise-agents && python agents.py convert && python agents.py install
```

</div>

---

## What This Is

**Enterprise Agents** gives you a curated library of 280+ structured AI agent personalities — each with a defined identity, workflow, and success metrics — ready to install as Claude Code subagents, Cursor `.mdc` rules, Windsurf `.windsurfrules`, GitHub Copilot instructions, Aider `CONVENTIONS.md`, Gemini CLI extensions, and more.

Stop writing one-off prompts. Start working with a Backend Architect who knows your stack, a Security Engineer who reviews for OWASP Top 10, or a Growth Hacker who speaks conversion rate and CAC. Agents span 28 domains across engineering, marketing, finance, legal, sales, design, and product. One-command install. Zero dependencies. MIT licensed.

| Generic AI | Enterprise Agents |
|---|---|
| "Help me write an auth system" | Backend Architect designs it, Security Engineer hardens it |
| Generic code review | Code Reviewer with correctness + security + performance focus |
| Broad marketing advice | SEO Specialist + Growth Hacker + TikTok Strategist coordinated |
| Re-explain context every session | Agent definitions persist — expert always loaded |
| One prompt for everything | Role-specific agents: each specialist owns its domain |

---

## Agent Teams in Action

The real power is combining specialists. Activate multiple agents on the same task and each contributes their domain expertise.

### Build a SaaS MVP

```mermaid
graph TD
    You([Your Idea]) --> A
    You --> B
    You --> C
    A[🏗️ Backend Architect\nAPI design + DB schema] --> D
    B[⚡ Frontend Developer\nUI + component library] --> D
    C[☁️ DevOps Automator\nCI/CD + infrastructure] --> D
    D[🔒 Security Engineer\nHarden + audit everything] --> Ship
    Ship([🚀 Shipped])
    style You fill:#6366f1,color:#fff,stroke:none
    style Ship fill:#22c55e,color:#fff,stroke:none
```

### Launch a Marketing Campaign

```mermaid
graph LR
    Brief([Campaign Brief]) --> A
    A[📈 Growth Hacker\nStrategy + channel mix] --> B
    A --> C
    A --> D
    B[🔍 SEO Specialist\nOrganic search content]
    C[📱 TikTok Strategist\nShort-form video]
    D[💼 LinkedIn Creator\nThought leadership]
    B & C & D --> Live([Live 🎯])
    style Brief fill:#6366f1,color:#fff,stroke:none
    style Live fill:#22c55e,color:#fff,stroke:none
```

### Run a Security Audit

```mermaid
graph TD
    Code([Codebase]) --> A
    Code --> B
    A[🕵️ Penetration Tester\nFind vulnerabilities] --> C
    B[🛡️ AppSec Engineer\nCode-level analysis] --> C
    C[🏰 Zero Trust Architect\nRedesign + harden] --> D
    D[📋 Compliance Auditor\nSOC 2 · ISO 27001] --> Done
    Done([✅ Hardened])
    style Code fill:#6366f1,color:#fff,stroke:none
    style Done fill:#22c55e,color:#fff,stroke:none
```

### Close an Enterprise Deal

```mermaid
graph LR
    Lead([Inbound Lead]) --> A
    A[🎯 Discovery Coach\nQualify + uncover pain] --> B
    B[♟️ Deal Strategist\nMEDDPICC + win plan] --> C
    C[🛠️ Sales Engineer\nTechnical POC + demo] --> D
    D[📄 Proposal Strategist\nWin-themed proposal] --> Won
    Won([💰 Closed Won])
    style Lead fill:#6366f1,color:#fff,stroke:none
    style Won fill:#22c55e,color:#fff,stroke:none
```

### Due Diligence (M&A / Fundraise)

```mermaid
graph TD
    Target([Company]) --> A
    Target --> B
    Target --> C
    A[💰 CFO Advisor\nFinancial analysis] --> Report
    B[⚖️ Legal Counsel\nContract + IP review] --> Report
    C[🔐 Security Engineer\nTechnical risk audit] --> Report
    Report([📊 Diligence Report])
    style Target fill:#6366f1,color:#fff,stroke:none
    style Report fill:#3b82f6,color:#fff,stroke:none
```

---

## Quick Start

**Python 3.8+ required. Zero dependencies.**

```bash
# Clone the repo
git clone https://github.com/gagangoswami94/enterprise-agents.git
cd enterprise-agents

# Option A: Auto-detect all installed tools and deploy everything
python agents.py convert && python agents.py install

# Option B: Target a specific tool
python agents.py convert --tool cursor
python agents.py install --tool cursor

# Claude Code and Copilot skip convert — install directly
python agents.py install --tool claude-code
python agents.py install --tool copilot
```

> **Project-scoped tools** (Cursor, Windsurf, Aider, OpenCode, Qwen Code) — run `install` from **inside your project root**, not from this repo.

---

## CLI Reference

```
python agents.py lint                        Validate all agent files
python agents.py lint path/to/agent.md       Validate one file
python agents.py convert                     Build all integration formats
python agents.py convert --tool cursor       Build for one tool
python agents.py install                     Auto-detect + install everything
python agents.py install --tool claude-code  Install for one tool
python agents.py list                        Browse the full 300+ catalog
python agents.py list --cat engineering      Filter by domain
python agents.py list --cat marketing       Filter by domain
```

---

## Agent Roster — 280 Specialists Across 30 Domains

<details>
<summary><strong>⚙️ Engineering — 34 agents</strong></summary>

AI Data Remediation Engineer · AI Engineer · Autonomous Optimization Architect · Backend Architect · CMS Developer · Code Reviewer · Data Engineer · Database Administrator · Database Engineer · Database Optimizer · DevOps Automator · Email Intelligence Engineer · Embedded Firmware Engineer · Enterprise Architect · Feishu Integration Developer · Filament Optimization Specialist · Frontend Developer · Git Workflow Master · Incident Response Commander · Infrastructure Architect · Mobile App Builder · Network Engineer · Rapid Prototyper · Security Engineer · Senior Developer · Site Reliability Engineer · Software Architect · Solidity Smart Contract Engineer · Solution Architect · Technical Business Analyst · Technical Writer · Threat Detection Engineer · LSP/Index Engineer · WeChat Mini Program Developer

</details>

<details>
<summary><strong>📣 Marketing — 39 agents</strong></summary>

AI Citation Strategist · App Store Optimizer · Baidu SEO Specialist · Bilibili Content Strategist · Book Co-Author · Brand Strategist · Carousel Growth Engine · China E-Commerce Operator · China Market Localization Strategist · Community Marketing Manager · Consumer Psychologist · Content Creator · Cross-Border E-Commerce Specialist · Douyin Strategist · Growth Hacker · Influencer Marketing Specialist · Instagram Curator · Kuaishou Strategist · Launch Campaign Manager · LinkedIn Content Creator · Livestream Commerce Coach · Market Research Analyst · Performance Marketer · Podcast Strategist · PR & Communications Specialist · Private Domain Operator · Product Marketing Manager · Reddit Community Builder · Retention Marketing Specialist · SEO Specialist · Short-Video Editing Coach · Social Media Strategist · TikTok Strategist · Twitter Engager · Video Optimization Specialist · WeChat Official Account Manager · Weibo Strategist · Xiaohongshu Specialist · Zhihu Strategist

</details>

<details>
<summary><strong>💰 Sales — 8 agents</strong></summary>

Account Strategist · Deal Strategist · Discovery Coach · Outbound Strategist · Pipeline Analyst · Proposal Strategist · Sales Coach · Sales Engineer

</details>

<details>
<summary><strong>🎨 Design — 8 agents</strong></summary>

Brand Guardian · Image Prompt Engineer · Inclusive Visuals Specialist · UI Designer · UX Architect · UX Researcher · Visual Storyteller · Whimsy Injector

</details>

<details>
<summary><strong>📦 Product — 5 agents</strong></summary>

Behavioral Nudge Engine · Feedback Synthesizer · Product Manager · Sprint Prioritizer · Trend Researcher

</details>

<details>
<summary><strong>💵 Finance — 10 agents</strong></summary>

Accounts Receivable Manager · Bookkeeper · Budget Analyst · CFO Advisor · Financial Controller · FP&A Analyst · Internal Auditor · Payroll Manager · Tax Specialist · Treasury Analyst

</details>

<details>
<summary><strong>⚖️ Legal — 8 agents</strong></summary>

Contract Manager · Corporate Counsel · Employment Law Advisor · IP Specialist · Legal Operations Manager · Licensing Manager · Privacy & GDPR Specialist · Software Lawyer

</details>

<details>
<summary><strong>♟️ Strategy — 4 agents</strong></summary>

Business Model Analyst · Competitive Intelligence Analyst · Pricing Analyst · Strategy Consultant

</details>

<details>
<summary><strong>👥 People Ops — 10 agents</strong></summary>

Compensation & Benefits Specialist · DEI Specialist · Employee Experience Manager · Employer Branding Specialist · HR Business Partner · HR Compliance Specialist · HRIS Administrator · Learning & Development Specialist · Performance Management Specialist · Talent Acquisition Specialist

</details>

<details>
<summary><strong>🔧 Operations — 6 agents</strong></summary>

Business Continuity Planner · Business Process Analyst · Facilities Manager · Operations Manager · Procurement Manager · Quality Assurance Manager

</details>

<details>
<summary><strong>🏢 Executive — 6 agents</strong></summary>

Board Meeting Specialist · CEO Coach · Chief of Staff · Investor Relations Specialist · OKR Facilitator · Strategic Planning Specialist

</details>

<details>
<summary><strong>🔐 Cybersecurity — 7 agents</strong></summary>

AppSec Engineer · Cloud Security Architect · GRC Specialist · Penetration Tester · SIEM Engineer · SOC Analyst · Zero Trust Architect

</details>

<details>
<summary><strong>☁️ Cloud — 5 agents</strong></summary>

AWS Solutions Architect · FinOps Analyst · Kubernetes Specialist · Platform Engineer · Terraform Specialist

</details>

<details>
<summary><strong>🤖 AI / ML — 7 agents</strong></summary>

AI Agent Developer · AI Safety Specialist · Computer Vision Engineer · LLM Fine-Tuning Specialist · MLOps Engineer · Prompt Engineer · RAG Architect

</details>

<details>
<summary><strong>📊 Data Science — 3 agents</strong></summary>

Analytics Engineer · Data Analyst · Data Scientist

</details>

<details>
<summary><strong>🏦 Fintech — 6 agents</strong></summary>

Blockchain Developer · Payment Systems Architect · Quantitative Analyst · RegTech Specialist · Risk Manager · Trading Systems Engineer

</details>

<details>
<summary><strong>🏥 Healthcare — 5 agents</strong></summary>

Clinical Documentation Specialist · Healthcare Administrator · Healthcare Compliance Specialist · Medical Writer · Patient Experience Specialist

</details>

<details>
<summary><strong>📢 Paid Media — 7 agents</strong></summary>

Ad Creative Strategist · Paid Media Auditor · Paid Social Strategist · PPC Campaign Strategist · Programmatic & Display Buyer · Search Query Analyst · Tracking & Measurement Specialist

</details>

<details>
<summary><strong>🛒 Ecommerce — 5 agents</strong></summary>

Amazon Seller Specialist · Conversion Rate Optimizer · Inventory Manager · Shopify Expert · WooCommerce Developer

</details>

<details>
<summary><strong>✍️ Content — 5 agents</strong></summary>

Community Manager · Copywriter · Newsletter Strategist · Podcast Producer · Video Producer

</details>

<details>
<summary><strong>🧪 Testing — 8 agents</strong></summary>

Accessibility Auditor · API Tester · Evidence Collector · Performance Benchmarker · Reality Checker · Test Results Analyzer · Tool Evaluator · Workflow Optimizer

</details>

<details>
<summary><strong>🎧 Support — 6 agents</strong></summary>

Analytics Reporter · Executive Summary Generator · Finance Tracker · Infrastructure Maintainer · Legal Compliance Checker · Support Responder

</details>

<details>
<summary><strong>♿ Accessibility — 3 agents</strong></summary>

ADA Compliance Specialist · Digital Accessibility Auditor · Inclusive Design Consultant

</details>

<details>
<summary><strong>🎓 Academic — 5 agents</strong></summary>

Anthropologist · Geographer · Historian · Narratologist · Psychologist

</details>

<details>
<summary><strong>🧑‍💻 Solopreneur — 8 agents</strong></summary>

Bootstrapper Finance · Fractional CFO · Fractional CTO · Full-Stack Solo Dev · One-Person Marketing · Solo Customer Success · Solo Founder · Virtual Executive Assistant

</details>

<details>
<summary><strong>📋 Project Management — 6 agents</strong></summary>

Experiment Tracker · Jira Workflow Steward · Project Shepherd · Senior Project Manager · Studio Operations · Studio Producer

</details>

<details>
<summary><strong>🤝 Customer Success — 5 agents</strong></summary>

Customer Success Manager · Implementation Consultant · Onboarding Specialist · Renewal Manager · Technical Account Manager

</details>

<details>
<summary><strong>🎮 Game Development — 20 agents</strong></summary>

Blender Add-on Engineer · Game Audio Engineer · Game Designer · Godot Gameplay Scripter · Godot Multiplayer Engineer · Godot Shader Developer · Level Designer · Narrative Designer · Roblox Avatar Creator · Roblox Experience Designer · Roblox Systems Scripter · Technical Artist · Unity Architect · Unity Editor Tool Developer · Unity Multiplayer Engineer · Unity Shader Graph Artist · Unreal Multiplayer Architect · Unreal Systems Engineer · Unreal Technical Artist · Unreal World Builder

</details>

<details>
<summary><strong>🥽 Spatial Computing — 6 agents</strong></summary>

macOS Spatial/Metal Engineer · Terminal Integration Specialist · visionOS Spatial Engineer · XR Cockpit Interaction Specialist · XR Immersive Developer · XR Interface Architect

</details>

<details>
<summary><strong>🔬 Specialized — 28 agents</strong></summary>

Accounts Payable Agent · Agentic Identity & Trust Architect · Agents Orchestrator · Automation Governance Architect · Blockchain Security Auditor · Civil Engineer · Compliance Auditor · Corporate Training Designer · Cultural Intelligence Strategist · Data Consolidation Agent · Developer Advocate · Document Generator · French Consulting Market Navigator · Government Digital Presales Consultant · Healthcare Marketing Compliance Specialist · Identity Graph Operator · Korean Business Navigator · LSP/Index Engineer · MCP Builder · Model QA Specialist · Recruitment Specialist · Report Distribution Agent · Sales Data Extraction Agent · Salesforce Architect · Study Abroad Advisor · Supply Chain Strategist · Workflow Architect · ZK Steward

</details>

---

## Supported Tools

### Claude Code — Custom Subagents
Agents install to `~/.claude/agents/` as `.md` subagent files. Each agent becomes a named specialist you can invoke by name in any Claude Code session.
```bash
python agents.py install --tool claude-code
```

### Cursor — `.mdc` Rules
Agents convert to `.mdc` rule files and install to `.cursor/rules/` in your project root. Run install from inside your project.
```bash
python agents.py convert --tool cursor && python agents.py install --tool cursor
```

### Windsurf — `.windsurfrules`
Agents combine into a `.windsurfrules` file in your project root for Windsurf's agentic context loading.
```bash
python agents.py convert --tool windsurf && python agents.py install --tool windsurf
```

### GitHub Copilot — Custom Instructions
Agents install to `~/.github/agents/` as structured instruction files for GitHub Copilot's custom agents feature.
```bash
python agents.py install --tool copilot
```

### Aider — `CONVENTIONS.md`
Agents merge into a `CONVENTIONS.md` file that Aider reads automatically from your project root.
```bash
python agents.py install --tool aider
```

### Gemini CLI — Extensions
Agents convert to Gemini CLI extension format and install to `~/.gemini/extensions/enterprise-agents/`.
```bash
python agents.py convert --tool gemini-cli && python agents.py install --tool gemini-cli
```

| Tool | Format | Destination |
|---|---|---|
| [![Claude Code](https://img.shields.io/badge/Claude_Code-8A2BE2?style=flat-square)](https://claude.ai/code) | `.md` subagents | `~/.claude/agents/` |
| [![Copilot](https://img.shields.io/badge/GitHub_Copilot-000?style=flat-square&logo=github)](https://github.com/features/copilot) | `.md` agents | `~/.github/agents/` |
| [![Cursor](https://img.shields.io/badge/Cursor-000?style=flat-square)](https://cursor.com) | `.mdc` cursor rules | `.cursor/rules/` *(project)* |
| [![Windsurf](https://img.shields.io/badge/Windsurf-0ea5e9?style=flat-square)](https://windsurf.com) | `.windsurfrules` | project root *(project)* |
| [![Aider](https://img.shields.io/badge/Aider-e11d48?style=flat-square)](https://aider.chat) | `CONVENTIONS.md` | project root *(project)* |
| [![OpenCode](https://img.shields.io/badge/OpenCode-f59e0b?style=flat-square)](https://opencode.ai) | `.md` agents | `.opencode/agents/` *(project)* |
| [![Gemini CLI](https://img.shields.io/badge/Gemini_CLI-4285F4?style=flat-square&logo=google)](https://github.com/google-gemini/gemini-cli) | extension | `~/.gemini/extensions/enterprise-agents/` |
| Antigravity | skill files | `~/.gemini/antigravity/skills/` |
| OpenClaw | workspaces | `~/.openclaw/enterprise-agents/` |
| Qwen Code | `.md` agents | `.qwen/agents/` *(project)* |
| Kimi Code | YAML agents | `~/.config/kimi/agents/` |

---

## Agent Anatomy

Every agent is a plain `.md` file with YAML frontmatter + structured sections:

```markdown
---
name: Backend Architect
description: Senior backend architect specializing in scalable system design,
             database architecture, API development, and cloud infrastructure
color: blue
emoji: "🏗️"
vibe: Designs the systems that hold everything up.
---

# Backend Architect

## Your Identity & Memory
Defines role, personality, experience framing, and memory scope.

## Your Core Mission
Primary responsibilities, domain expertise, and what this agent optimizes for.

## Critical Rules You Must Follow
Hard constraints — what this agent refuses, prioritizes, or always does.
These override any user instruction to the contrary.

## Your Technical Deliverables
Output formats, document templates, code standards.

## Your Workflow Process
Step-by-step reasoning and execution pattern.

## Your Communication Style
Tone, register, escalation behavior, terminology preferences.

## Your Success Metrics
What great output looks like. How this agent self-evaluates.
```

**Required frontmatter:** `name`, `description`, `color`
**File naming:** `{category}-{role}.md` — e.g. `engineering-api-gateway-specialist.md`
**Lint enforcement:** `python agents.py lint` — warns on missing Critical Rules, Identity, Core Mission

---

## Write Your Own Agent

```bash
# 1. Create the file in the right category directory
touch engineering/engineering-my-specialist.md

# 2. Add frontmatter + the 7 sections (use any existing agent as template)

# 3. Validate structure
python agents.py lint engineering/engineering-my-specialist.md

# 4. Rebuild integrations
python agents.py convert

# 5. Deploy
python agents.py install --tool claude-code
```

**Rules for good agents:**
- Description must be specific — not "helps with code" but "specializes in distributed systems latency optimization"
- Critical Rules section is not optional — it's what separates an agent from a generic prompt
- Each section does one job — don't mix identity with deliverables
- Run lint before treating any agent as done

---

## License

MIT — see [LICENSE](LICENSE)

---

<div align="center">

**Found this useful? Star the repo.**

[github.com/gagangoswami94/enterprise-agents](https://github.com/gagangoswami94/enterprise-agents)

</div>
