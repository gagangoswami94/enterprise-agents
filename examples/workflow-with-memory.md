# Multi-Agent Workflow: SaaS MVP with Persistent Memory

> The same MVP workflow from [workflow-saas-mvp.md](workflow-saas-mvp.md), upgraded with an MCP memory server. No more copy-paste handoffs between agents.

## The Problem with Manual Handoffs

In the standard workflow, every agent transition looks like this:

```
Activate Backend Architect.

Sprint plan: [paste Sprint Prioritizer output]
Research brief: [paste UX Researcher output]

Design the API and database schema for VerifyAI...
```

You are the relay. You copy outputs between agents, maintain state between sessions, and hope nothing gets lost when a session times out. It works for a 4-week single-session build. It breaks when:

- Sessions time out and you lose 2 hours of output
- Three agents need the same context simultaneously
- A Reality Checker rejects a deliverable and you need to trace back what went wrong
- The project runs across multiple days and you're re-establishing context each morning

## The Fix

With an MCP memory server connected, agents store deliverables and retrieve context automatically:

```
Activate Backend Architect.

Project: VerifyAI. Recall the sprint plan and research brief stored by previous agents.
Stack: Node.js, Express, PostgreSQL. Design the API and database schema.
Store your schema and endpoint list when done, tagged for the frontend-developer.
```

The agent searches memory, finds what previous agents stored, and continues from there. You pass the objective, not the context.

## Setup

Install any MCP-compatible memory server that supports `remember`, `recall`, and `search` operations. See [integrations/mcp-memory/README.md](../integrations/mcp-memory/README.md) for setup.

---

## The Workflow: VerifyAI with Memory

Same product as [workflow-saas-mvp.md](workflow-saas-mvp.md): an automated employee background verification platform for HR teams. 4 weeks to MVP.

## Agent Team

| Agent | Role |
|---|---|
| Sprint Prioritizer | Define weekly deliverables |
| UX Researcher | Validate the problem, identify must-have features |
| Backend Architect | API design, data model, integrations |
| Frontend Developer | React dashboard |
| Growth Hacker | Pilot customer acquisition strategy |
| Reality Checker | Milestone gates |

---

## Week 1: Discovery + Architecture

### Step 1 — Sprint Prioritizer

```
Activate Sprint Prioritizer.

Project: VerifyAI — automated background verification for HR teams.
Timeline: 4 weeks to MVP with 3-5 paying pilot customers.
Stack: Next.js, Node.js, PostgreSQL, Railway + Vercel.

Break into 4 weekly sprints with deliverables and acceptance criteria.
Store your sprint plan in memory tagged: verifyai, sprint-plan, week-1.
```

The Sprint Prioritizer produces the plan and stores it tagged with `verifyai` and `sprint-plan`.

### Step 2 — UX Researcher (run in parallel)

```
Activate UX Researcher.

Product: Automated background verification for HR teams at 50-500 person companies.
Competitors: Checkr, Sterling, HireRight.

Identify: table-stakes features, competitor gaps, one differentiator to own.
Output: 1-page research brief.
Store in memory tagged: verifyai, research-brief, ux-researcher.
```

The UX Researcher stores the brief tagged with `verifyai` and `research-brief`.

### Step 3 — Backend Architect

```
Activate Backend Architect.

Project: VerifyAI. Recall the sprint plan and research brief stored by previous agents.

Design:
1. PostgreSQL schema
2. REST API endpoint list
3. Async job queue design for verification workflows
4. Auth strategy (we'll use Clerk)

Store each deliverable tagged: verifyai, backend-architect, api-spec, frontend-developer.
```

The Backend Architect recalls both prior outputs from memory — no copy-paste from you. It stores the schema and API spec tagged so the Frontend Developer can find it automatically.

### Reality Check — End of Week 1

```
Activate Reality Checker.

Project: VerifyAI, end of week 1.
Recall all deliverables stored for this project.

Evaluate:
1. Is the architecture scoped for a 4-week solo build?
2. Any blocking decisions not yet made?
3. Highest-risk assumption in the current plan?

Store your verdict tagged: verifyai, reality-check, week-1.
GO / NO-GO with evidence required.
```

The Reality Checker has access to the sprint plan, research brief, and architecture — everything stored in week 1 — without any copy-paste from you.

---

## Week 2: Core Build

### Step 4 — Backend Architect

```
Activate Backend Architect.

Project: VerifyAI. Recall your approved architecture from week 1.
Recall the Reality Checker's week-1 verdict for any changes to scope.

Implement:
1. Database migrations
2. Verification request CRUD
3. Job queue worker (mock API responses)
4. Webhook delivery system

Store implementation notes tagged: verifyai, backend-architect, week-2, frontend-developer.
```

### Step 5 — Frontend Developer (mid-week 2)

```
Activate Frontend Developer.

Project: VerifyAI. Recall the API spec and schema stored by the Backend Architect.

Build:
- Dashboard: verification request list with status badges
- New Request form: candidate info, check types, deadline
- Request detail: status timeline

Stack: Next.js 14, TypeScript, Tailwind, shadcn/ui.
Store progress tagged: verifyai, frontend-developer, week-2.
```

---

## Week 3: Auth + Growth

### Step 6 — Frontend Developer (adds auth)

```
Activate Frontend Developer.

Project: VerifyAI. Recall your week-2 progress.
Add Clerk authentication — org-scoped data, HR Admin and HR Manager roles.

Store updated state tagged: verifyai, frontend-developer, week-3.
```

### Step 7 — Growth Hacker (parallel)

```
Activate Growth Hacker.

Project: VerifyAI — launching in 2 weeks to 3-5 pilot HR teams.
Recall the research brief and any product context from previous agents.

Deliver:
- Cold outreach message (email + LinkedIn DM)
- Where to find HR managers right now
- Pilot pricing structure
- 5-minute demo script

Store launch plan tagged: verifyai, growth-hacker, pilot-plan.
```

---

## Week 4: Launch

### Step 8 — Final Reality Check

```
Activate Reality Checker.

Project: VerifyAI, ready for pilot launch.
Recall all deliverables and verdicts stored for this project.

Evaluate production readiness — core flow, multi-customer load, day-1 gaps.
Store your final verdict tagged: verifyai, reality-check, launch.
GO / NO-GO with evidence required.
```

---

## When a Deliverable Gets Rejected

In the standard workflow, a Reality Checker rejection means explaining the problem to the responsible agent from scratch. With memory, the recovery is tighter:

```
Activate Backend Architect.

Project: VerifyAI. The Reality Checker flagged issues with the webhook delivery design.
Recall the Reality Checker's week-2 verdict and your current implementation.
Address the specific issues raised and store your updated implementation.
```

The Backend Architect sees exactly what was flagged, recalls its own prior work, and produces a fix — without you manually tracking what changed between versions.

---

## Before vs. After

| Aspect | Standard Workflow | With Memory |
|---|---|---|
| Handoffs | Copy-paste full output between agents | Agents recall what they need automatically |
| Context loss | Session timeout loses everything | Memories persist across sessions and days |
| Multi-agent context | Compile and paste context from N agents | Agent searches memory by project tag |
| QA failure recovery | Describe the problem from scratch | Agent recalls the verdict and its own prior work |
| Multi-day projects | Re-establish context every session | Agent picks up where it left off |

---

## Tagging Convention

Consistent tagging is what makes recall work:

- Tag every memory with the **project name** (`verifyai`) — this is the primary search key
- Tag the **producing agent** (`backend-architect`) — lets agents search for their own prior work
- Tag the **consuming agent** (`frontend-developer`) — lets the next agent find what was prepared for them
- Tag the **week or phase** (`week-2`) — enables rollback to a specific checkpoint

Any MCP-compatible memory server that supports `remember`, `recall`, `search`, and `rollback` operations works with this workflow.
