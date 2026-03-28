# Multi-Agent Workflow: Security Audit Sprint

> Audit a production codebase for vulnerabilities, compliance gaps, and architecture risk — and produce an actionable remediation plan in one week.

## The Scenario

**Company:** Forge — a B2B code review platform with 3,200 customers and a public API.
**Trigger:** An enterprise prospect's security team is asking for a pentest report before signing a $180K deal. The last audit was 18 months ago. The engineering team has shipped 40+ releases since then.
**Timeline:** 5 days. One shot at passing the prospect's security review.

## Agent Team

| Agent | Role in this workflow |
|---|---|
| Security Engineer | Lead the audit — threat model, code review, and final report |
| Penetration Tester | Simulate external attacks against the API and auth flows |
| Code Reviewer | Static analysis of the codebase for injection, auth bugs, and data exposure |
| Compliance Auditor | Evaluate SOC 2 Type II and GDPR posture |
| Backend Architect | Assess infrastructure and secrets management |

---

## The Workflow

### Day 1: Threat Model + Scope

**Step 1 — Activate Security Engineer**

```
Activate Security Engineer.

Company: Forge — B2B code review platform.
Stack: Node.js API, React frontend, PostgreSQL, AWS (ECS, RDS, S3), Cloudflare WAF.
Users: 3,200 business customers, public API with OAuth 2.0.
Trigger: Enterprise prospect security review before $180K contract.

Produce a threat model for Forge. Cover:
1. Attack surface map — entry points, trust boundaries, data flows
2. Top 10 threats by severity (use STRIDE framework)
3. Which OWASP Top 10 categories apply to our stack
4. Audit scope: what to test in 5 days vs. what needs a full pentest engagement

This becomes the brief for the rest of the audit team.
```

**Step 2 — Activate Compliance Auditor (in parallel)**

```
Activate Compliance Auditor.

Company: Forge — B2B SaaS, code review platform. 3,200 business customers.
Data processed: source code repositories, user credentials, billing data.
Geography: US customers primarily, ~400 in EU.
Existing certifications: none yet — this is a pre-audit.

Evaluate our posture against:
1. SOC 2 Type II — which Trust Services Criteria apply and what evidence gaps exist
2. GDPR — EU customer data obligations, DPA requirements, breach notification
3. What a procurement security questionnaire will ask us and which answers will fail

Deliver a gap analysis ranked by likelihood to block the deal.
```

---

### Day 2: Code + Infrastructure Review

**Step 3 — Activate Code Reviewer**

```
Activate Code Reviewer.

Performing a security-focused code review for Forge (Node.js API, PostgreSQL).

Here's the threat model: [paste Security Engineer output]

Focus areas based on the threat model:
1. SQL injection — parameterized queries, ORM usage
2. Authentication flows — JWT validation, session handling, token expiry
3. Authorization — role checks, multi-tenant data isolation (can Customer A access Customer B's repos?)
4. Input validation — all external inputs sanitized before use
5. Secrets — hardcoded API keys, credentials in environment handling
6. Dependency audit — known CVEs in package.json

For each finding: severity (Critical / High / Medium / Low), file and line reference, and a specific fix.
```

**Step 4 — Activate Backend Architect**

```
Activate Backend Architect.

Security review of Forge's infrastructure. Node.js on AWS ECS, RDS PostgreSQL, S3, Cloudflare WAF.

Here's the threat model: [paste Security Engineer output]

Audit:
1. Secrets management — are we using AWS Secrets Manager or environment variables in plaintext?
2. Network segmentation — is RDS publicly accessible? Are internal services isolated?
3. IAM roles — principle of least privilege, no wildcard permissions
4. S3 bucket policies — public exposure risk, encryption at rest
5. Logging and monitoring — CloudTrail, VPC flow logs, alerting on anomalies
6. Backup and recovery — RTO/RPO for a ransomware scenario

Flag anything that would fail a SOC 2 audit.
```

---

### Day 3: External Attack Simulation

**Step 5 — Activate Penetration Tester**

```
Activate Penetration Tester.

Target: Forge public API (OAuth 2.0, REST endpoints). Authorized security assessment.
Here's the threat model and code review findings: [paste Security Engineer + Code Reviewer output]

Simulate an external attacker who has:
- A valid free-tier Forge account
- The public API documentation
- Knowledge of common SaaS attack patterns

Test vectors:
1. IDOR — can I access other customers' repositories by manipulating IDs?
2. OAuth flow — token leakage, PKCE bypass, redirect_uri manipulation
3. Rate limiting — can I brute-force the login endpoint or API keys?
4. Mass assignment — can I escalate my own role through the API?
5. JWT attacks — algorithm confusion, weak secret brute force

For each test: what you tried, what you found, severity, and reproduction steps.
```

---

### Day 4: Remediation Planning

**Step 6 — Activate Security Engineer**

```
Activate Security Engineer.

We have all audit findings. Now build the remediation plan.

Code review findings: [paste Code Reviewer output]
Infrastructure findings: [paste Backend Architect output]
Pentest findings: [paste Penetration Tester output]
Compliance gaps: [paste Compliance Auditor output]

Deliver:
1. Consolidated findings ranked by severity and exploitability
2. Remediation plan with effort estimates (quick wins vs. multi-week projects)
3. What we fix before the prospect review vs. what we document as roadmap
4. The executive summary: 1 page suitable for the prospect's security team
5. What we truthfully answer on a security questionnaire with our current posture
```

---

### Day 5: Report + Questionnaire Response

**Step 7 — Activate Compliance Auditor (final)**

```
Activate Compliance Auditor.

Here's the consolidated audit report: [paste Security Engineer final output]
Here's the prospect's security questionnaire (40 questions, enterprise healthcare vendor).

Draft our responses to the security questionnaire.
For strong answers: be specific and confident.
For gaps we haven't fixed yet: draft honest answers that contextualize without overpromising.

Flag any question we should escalate to legal before submitting.
```

---

## Key Patterns

1. **Threat model first** — Security Engineer runs before anyone else. A code reviewer without a threat model is guessing what to look for.
2. **Parallel tracks on Day 1** — Compliance Auditor runs simultaneously with the Security Engineer because the gap analysis informs priorities but doesn't depend on the threat model.
3. **Code and infrastructure reviewed separately** — Code Reviewer focuses on application logic, Backend Architect focuses on cloud posture. Combining them creates blind spots.
4. **External simulation after internal review** — Pentest runs after the code review so the attacker simulation is informed by what we already know is weak.
5. **Security Engineer owns synthesis** — Individual specialists produce findings. Security Engineer consolidates into a single ranked report. Stakeholders don't want five separate documents.
6. **Honest questionnaire answers** — The goal is to pass the deal, not create false confidence. Compliance Auditor explicitly handles the gap between current state and ideal state.

## Tips

- The prospect's security questionnaire is the real deliverable. Work backwards from it to prioritize the audit scope.
- If the Code Reviewer finds a Critical IDOR issue, don't wait for Day 4 — fix it immediately and re-test.
- "Roadmap item" is an acceptable answer on a questionnaire if you have a timeline. "We're working on it" is not.
