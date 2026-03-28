# Multi-Agent Workflow: Production Incident Response

> Contain a production incident, communicate clearly under pressure, and produce a post-mortem that prevents recurrence — in under 4 hours.

## The Scenario

**Company:** Capsule — HR software platform, 3,200 business customers.
**Incident:** 2:47 AM. PagerDuty fires. The background jobs queue has stalled. Employee onboarding workflows are frozen for 340 customers. No new hires are receiving their day-one access credentials. It's Sunday.
**On-call engineer:** Priya. She's been with the company 4 months.

This is a P1. Every minute costs customer trust.

## Agent Team

| Agent | Role in this workflow |
|---|---|
| Incident Response Commander | Structure the response, own communication, drive to resolution |
| SRE | Diagnose the technical failure, coordinate the fix |
| Backend Architect | Assess root cause and architecture risk |
| Support Responder | Draft customer communication |
| Technical Writer | Write the post-mortem |

---

## The Workflow

### Phase 1: First 15 Minutes — Declare and Contain

**Step 1 — Activate Incident Response Commander**

```
Activate Incident Response Commander.

ACTIVE P1 INCIDENT. Do not ask clarifying questions — give me the playbook immediately.

What we know:
- Background jobs queue stalled at 02:47 AM
- 340 customers affected — employee onboarding workflows frozen
- No errors visible in Sentry yet
- Database CPU is normal, Redis queue depth is climbing
- On-call engineer: Priya (4 months tenure, first P1 solo)

Give me right now:
1. The first 3 actions Priya should take in the next 5 minutes
2. Who else needs to be paged immediately (roles, not names)
3. The incident Slack channel message to post NOW (not a polished write-up — the 2-line status)
4. When does customer communication need to go out? What's the trigger?
5. How do we know this is contained vs. still spreading?
```

**Step 2 — Activate SRE**

```
Activate SRE.

P1 in progress. Background jobs queue stalled. Redis queue depth climbing, DB CPU normal, no Sentry errors.
Stack: Node.js workers, Bull queue on Redis, PostgreSQL, AWS ECS.

Diagnostic runbook — what Priya should check in order:
1. Redis health: what commands to run to inspect queue state
2. Worker process: how to check if workers are running and connected
3. Job inspection: how to view stuck jobs, check for poison pill messages
4. Quick remediation options if workers are hung: safe restart procedure
5. Rollback decision: under what conditions should she roll back the last deploy?

Include exact commands. Priya is experienced but this is her first P1.
```

---

### Phase 2: 15–60 Minutes — Diagnose and Fix

**Step 3 — Activate Backend Architect**

```
Activate Backend Architect.

We've stabilized the immediate incident (workers restarted, queue processing again).
Now identify the root cause.

Context:
- Last deploy was Friday 4pm: upgraded Bull queue library from 3.x to 4.x
- Queue stalled at 2:47 AM — ~10 hours after deploy
- Stuck jobs: all were "send-credentials" type, all had the same retry count (5)
- Workers came back after restart, processed the backlog in ~18 minutes

Assess:
1. What likely caused the Bull 3.x → 4.x upgrade to create delayed stall behavior?
2. Why would it fail after 10 hours rather than immediately?
3. Is there a data-level issue — jobs stuck in a bad state in Redis that could re-trigger?
4. What's the blast radius if this happens again before we fix it?
5. The fix: what do we deploy Monday morning, and what do we defer to a proper sprint?
```

---

### Phase 3: Customer Communication

**Step 4 — Activate Support Responder**

```
Activate Support Responder.

We need to communicate about a production incident that affected 340 customers.

Incident summary:
- Background jobs stalled from 02:47 AM to 04:31 AM (104 minutes)
- Impact: employee onboarding workflows paused — new hires did not receive day-one access credentials during this window
- Resolution: all stalled jobs processed, credentials delivered, systems normal
- Root cause: a library upgrade introduced a behavior change in job retry logic

Drafts needed:
1. In-app banner (max 25 words) — currently showing to all affected customers
2. Email to affected customers — empathetic, direct, no jargon. What happened, impact, what we did, what they should do now.
3. Status page update (statuspage.io format) — technical but accessible
4. Response template for support tickets that will come in Monday morning

Tone: accountable, not defensive. We are not minimizing the impact.
```

---

### Phase 4: Post-Mortem

**Step 5 — Activate Technical Writer**

```
Activate Technical Writer.

Writing the internal post-mortem for the Capsule P1 incident.

Incident data:
- Timeline: [paste from incident Slack channel — key events and timestamps]
- Root cause: Bull 3.x → 4.x upgrade changed retry exhaustion behavior; workers entered a deadlock state after processing 5 retries on malformed jobs
- Contributing factors: no staging environment tests for queue behavior under retry pressure; deploy on Friday afternoon; no alerting on queue depth until depth exceeded 500 (threshold too high)
- Impact: 340 customers, 104 minutes, ~600 onboarding workflows delayed
- Resolution: worker restart, queue drain, hotfix to Bull config deployed Sunday 6 AM
- What went right: Priya escalated correctly, Redis queue depth alert eventually fired, rollback path was clear

Post-mortem format:
1. Summary (3 sentences — what happened, why, how we fixed it)
2. Timeline (table: time, event, who)
3. Root cause analysis (5 Whys)
4. Contributing factors
5. Impact
6. What went well
7. Action items (owner, priority, due date)

Action items must be specific and assigned. "Improve monitoring" is not an action item.
```

---

### Phase 5: Prevention

**Step 6 — Activate SRE**

```
Activate SRE.

Post-mortem complete. Now build the runbook so this class of incident never goes to a junior on-call engineer without a guide.

Incident type: background job queue stall
Root cause pattern: dependency upgrade + delayed failure under retry pressure

Deliver:
1. Alert tuning — what Redis queue depth threshold actually warrants a page? What's normal vs. warning vs. critical?
2. Pre-deploy checklist for any dependency upgrade touching the job queue
3. Queue stall runbook — step-by-step for any on-call engineer, no SRE experience required
4. Synthetic canary job — a lightweight job we can run every 5 minutes to detect queue stalls before customers do
5. Friday deploy policy recommendation — should we have a change freeze window?
```

---

## Timeline

| Time | Phase | Action |
|---|---|---|
| T+0 (02:47) | Alert fires | PagerDuty pages Priya |
| T+5 | Declare | Incident Commander playbook, Slack channel opened |
| T+10 | Diagnose | SRE runbook, Priya begins triage |
| T+45 | Contain | Workers restarted, queue draining |
| T+60 | Communicate | Customer email + status page update |
| T+104 | Resolve | All affected jobs processed, incident closed |
| T+24h | Post-mortem | Draft complete, circulated to team |
| T+48h | Review | Post-mortem reviewed, action items assigned |
| T+72h | Prevention | Runbooks updated, alerts tuned |

---

## Key Patterns

1. **Commander first, then specialist** — Incident Response Commander gives structure before the SRE goes deep on diagnosis. Without structure, the responder improvises sequencing under stress.
2. **Communication runs in parallel with the fix** — The Support Responder drafts customer communication while engineers are debugging. Waiting for resolution to communicate loses trust.
3. **Post-mortem is a Technical Writer job, not an engineering job** — Engineers know what happened. Technical Writers know how to write it clearly, use 5 Whys correctly, and produce action items that don't evaporate.
4. **Action items are owned and dated** — "Improve monitoring" is not an action item. "Set Redis queue depth alert threshold to 50 jobs (currently 500) by Thursday — owner: Priya" is.
5. **Prevention is the last step, not an afterthought** — SRE runbook and alert tuning happen after the incident is fully documented, not during the chaos.
6. **Empathy before explanation** — Support Responder's email leads with what customers experienced, not with the technical cause. Customers care about their employees' onboarding, not Bull.js retry semantics.

## Tips

- Run Steps 1 and 2 as fast as possible — structure and diagnosis happen within the first 15 minutes or they don't happen at all.
- The incident Slack channel is your timeline. Log everything in real time: actions taken, hypotheses rejected, commands run. The Technical Writer will use it.
- Post-mortems are not blame documents. If an action item says "Priya should have done X," reframe it: "We need a runbook so any on-call engineer knows to do X."
