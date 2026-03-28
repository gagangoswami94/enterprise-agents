# Multi-Agent Workflow: B2B SaaS MVP

> Go from idea to shippable product in 4 weeks using 6 coordinated specialists.

## The Scenario

You're building **VerifyAI** — an automated employee background verification platform for HR teams at mid-size companies. Current workflow: HR managers email PDF requests to third-party agencies and wait 5-10 days. Your product automates the request, tracking, and delivery into a single dashboard with webhook integrations.

Timeline: 4 weeks to a working MVP with paying pilot customers.

## Agent Team

| Agent | Role |
|---|---|
| Sprint Prioritizer | Define weekly deliverables and scope the MVP |
| UX Researcher | Validate the problem and identify must-have features |
| Backend Architect | Design the API, data model, and integrations |
| Frontend Developer | Build the React dashboard |
| Growth Hacker | Plan the pilot customer acquisition strategy |
| Reality Checker | Gate each milestone before moving to the next |

---

## Week 1: Discovery + Architecture

### Step 1 — Sprint Prioritizer

```
Activate Sprint Prioritizer.

Product: VerifyAI — automated background verification for HR teams.
Timeline: 4 weeks to MVP with 3-5 paying pilot customers.

Core features needed:
- HR manager submits verification request (candidate name, type of check, deadline)
- System routes to the appropriate data source or third-party API
- Real-time status tracking dashboard
- Webhook notifications when checks complete
- Simple role-based access (HR manager, HR admin, candidate)

Stack: Next.js + TypeScript, Node.js API, PostgreSQL, deployed on Railway + Vercel.
Team: Solo developer.

Break this into 4 weekly sprints. Each sprint needs: goal, deliverables, acceptance criteria, and what gets cut if we fall behind.
```

### Step 2 — UX Researcher (run in parallel with Step 1)

```
Activate UX Researcher.

I'm building an automated background verification platform for HR teams at companies with 50-500 employees.

Current tools in market: Checkr, Sterling, HireRight.
Pain point hypothesis: HR managers spend 3-4 hours per hire managing the back-and-forth with verification vendors.

Run a quick competitive analysis and give me:
1. What Checkr/Sterling/HireRight do well — what's table stakes
2. Where they fall short (look at G2 reviews, complaints, workarounds)
3. One specific gap VerifyAI could own as a differentiator
4. The 3 features HR managers would need to see in a demo to say yes

Output: 1-page brief. No filler.
```

### Step 3 — Backend Architect

```
Activate Backend Architect.

Building VerifyAI — automated employee background verification.

Sprint plan: [paste Sprint Prioritizer output]
Research brief: [paste UX Researcher output]

Design the backend architecture:
Stack: Node.js, Express, PostgreSQL, BullMQ for job queues.
External integrations: Stripe (billing), SendGrid (notifications), one mock verification API for MVP.

Deliver:
1. PostgreSQL schema — all tables, relationships, indexes
2. REST API endpoint list with request/response shapes
3. Job queue design for async verification workflows
4. Auth strategy (we'll use Clerk for auth — design the user/org model around it)
5. One paragraph on what NOT to build in week 1
```

### Reality Check — End of Week 1

```
Activate Reality Checker.

VerifyAI — end of week 1 gate.

Deliverables produced:
- Sprint plan: [paste]
- Research brief: [paste]
- Backend architecture: [paste]

Questions:
1. Is the architecture scoped correctly for a 4-week solo build?
2. Are there any critical decisions we haven't made that will block week 2?
3. What's the highest-risk assumption in the current plan?

Give a GO / NO-GO for moving to build phase. Require specific evidence for each concern raised.
```

---

## Week 2: Core Backend + Auth

### Step 4 — Backend Architect continues

```
Activate Backend Architect.

Architecture is approved. Now implement:

1. Database migrations (use the schema from week 1)
2. Verification request CRUD — create, read, update status
3. The job queue worker that processes verification requests against the mock API
4. Webhook delivery system — fires to customer endpoints on status change

Constraints:
- No auth middleware yet (Clerk integration is week 3)
- Mock the verification API responses — don't integrate a real one yet
- Every endpoint needs basic input validation

Deliver working code with a README for local setup.
```

### Step 5 — Frontend Developer (starts mid-week 2)

```
Activate Frontend Developer.

Building the VerifyAI React dashboard.

Backend spec: [paste Backend Architect API output]
Design direction: Clean, minimal, enterprise-appropriate. Think Linear but for HR.

Week 2 scope — build these pages only:
1. Dashboard: list of verification requests with status badges
2. New Request form: candidate name, check types (criminal, employment, education), deadline
3. Request detail: full timeline of status updates

Stack: Next.js 14, TypeScript, Tailwind CSS, shadcn/ui components.
Connect to the backend API. Use mock data where the API isn't ready yet.

No auth yet — hardcode a test user session for now.
```

---

## Week 3: Auth + Integrations + Landing Page

### Step 6 — Frontend Developer adds auth

```
Activate Frontend Developer.

Add Clerk authentication to the VerifyAI dashboard:
- Sign up / sign in flow
- Organization-scoped data (HR managers only see their company's requests)
- Role gates: HR Admin can manage team members, HR Manager can create/view requests

[paste current frontend codebase structure]

After auth works, add the notification preferences page: email + webhook configuration per organization.
```

### Step 7 — Growth Hacker (runs in parallel with auth work)

```
Activate Growth Hacker.

Product: VerifyAI — launching in 2 weeks to 3-5 pilot HR teams.
Target: HR managers and HR directors at tech companies with 50-500 employees.

I need 3-5 paid pilot customers before launch. Budget: $0 outbound tools, 10 hours of my time.

Deliver:
1. Exact outreach message (cold email + LinkedIn DM version) — specific to HR pain around verification delays
2. Where to find these HR managers (communities, LinkedIn searches, Slack groups)
3. Pilot pricing structure — what to charge, what to include, what success looks like
4. The 5-minute demo script that gets a yes
5. Objection handling for "we already use Checkr"
```

---

## Week 4: Polish + Launch

### Step 8 — Final Reality Check

```
Activate Reality Checker.

VerifyAI is ready for pilot launch. Full production readiness assessment.

What's live:
- URL: [staging URL]
- Auth: Clerk configured, test org created
- Core flow: request submission → queue processing → status updates → webhooks
- Stripe: billing configured, $299/month pilot plan active
- Monitoring: Sentry error tracking, Railway metrics dashboard
- Test: end-to-end test with mock verification completed successfully

Evaluate:
1. Is the core user flow — from sign-up to first completed verification — working without hand-holding?
2. What breaks if 5 pilot customers onboard simultaneously?
3. What's missing that a pilot customer would notice in day 1?

GO / NO-GO for inviting first pilot customer. Evidence required for each point.
```

---

## Key Patterns

**Sequential handoffs with full context** — Backend Architect needs both the sprint plan and research brief. Paste full outputs, never summarize.

**Parallel tracks that merge** — UX Researcher and Sprint Prioritizer run in week 1 simultaneously. Backend Architect waits for both before starting.

**Scope discipline** — Backend Architect explicitly defines what NOT to build. Sprint Prioritizer defines what gets cut if behind. This prevents scope creep from killing the timeline.

**Two Reality Checks** — One at end of week 1 (before writing any code) and one before launch. The first saves more time than any other step.

**Growth runs early** — Growth Hacker starts in week 3, not week 4. Finding pilot customers takes time; the pipeline needs to be building while you finish the product.
