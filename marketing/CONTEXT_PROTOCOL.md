# Marketing Context Protocol

**Version**: 1.0
**Applies to**: All 58+ marketing agents in `enterprise-agents/marketing/`
**Purpose**: Ensure marketing agents share context, build on each other's decisions, and produce internally consistent playbooks.

---

## The Problem This Solves

Before this protocol, marketing agents ran in isolation. Each agent got the same initial brief but never saw what other agents decided. Result:
- Duplicate content pillars
- Conflicting tagline recommendations
- Different audience definitions in different docs
- Inconsistent pricing references
- No single source of truth

This protocol makes every marketing agent context-aware: they **read** shared project context before starting and **append** their decisions after finishing. Later agents see earlier decisions and build on them instead of reinventing.

---

## The Shared Context File

Every marketing project maintains a single file: `.marketing-context.md`

**Location**: Project root OR the marketing playbook output directory (e.g., `docs/marketing-plan/<project>/.marketing-context.md`)

**Created by**: The Marketing Orchestrator during intake
**Read by**: Every marketing agent before starting its work
**Updated by**: Every marketing agent after finishing its work

### Context File Structure

```markdown
# Marketing Context — <Project Name>

**Last updated**: YYYY-MM-DD HH:MM
**Last updated by**: <Agent Name>

## 1. Project Basics
- **Product**: <one-line description>
- **URL**: <website>
- **Category**: <SaaS / B2C app / E-commerce / etc.>
- **Stage**: <Pre-launch / Launch / Growth / Scale>
- **Team size**: <Solo / Small / Department>
- **Budget**: <$0 / <$1K / $1K-10K / $10K+>

## 2. Target Audience (owned by: Brand Strategist)
- **Primary segment**: <name + description>
- **Demographics**: <age, location, language>
- **Psychographics**: <beliefs, habits, pain points>
- **Where they hang out**: <channels>
- **Jobs to be done**: <what they hire the product for>

## 3. Positioning (owned by: Brand Strategist)
- **Positioning statement**: <For X who Y, Z is the A that B because C>
- **Category**: <what shelf you sit on>
- **Differentiation**: <1-2 things competitors can't copy>
- **Tagline**: <primary>
- **Alternative taglines**: <list>

## 4. Brand Voice (owned by: Brand Strategist)
- **Voice attributes**: <5 attributes>
- **Tone**: <context-specific variations>
- **What voice IS NOT**: <explicit boundaries>

## 5. Pricing Model (owned by: Pricing Strategist)
- **Model**: <Free / Freemium / Trial / Paid>
- **Tiers**: <name, price, features>
- **Value metric**: <what you charge based on>
- **Annual discount**: <%>

## 6. Content Pillars (owned by: Content Creator)
- **Pillar 1**: <name, %, description>
- **Pillar 2**: <name, %, description>
- **...**
- **Signature format**: <the primary content format>
- **Publishing cadence**: <posts per week>
- **Primary channels**: <Instagram, YouTube, etc.>

## 7. Channel Strategy (owned by: Social Media Strategist / Solo Marketing)
- **Primary channel (80%)**: <platform + why>
- **Secondary channels (20%)**: <platforms>
- **Channels NOT pursuing**: <with reason>

## 8. Funnel & Conversion (owned by: Page CRO / Signup Flow)
- **Landing page**: <URL + key decisions>
- **Signup flow**: <decisions made>
- **Aha moment**: <activation event definition>
- **Conversion rate targets**: <current + goal>

## 9. Measurement (owned by: Analytics Tracking Engineer)
- **Tools**: <GA4, Mixpanel, PostHog, etc.>
- **Primary conversion event**: <event name>
- **Key metrics to track**: <list>
- **Dashboards**: <what exists>

## 10. Growth Loops (owned by: Referral Program Designer / Growth Hacker)
- **Viral mechanics**: <what exists>
- **Referral program**: <structure>
- **K-factor target**: <number>

## 11. Open Decisions
List any decisions NOT yet made that later agents will need to resolve.
- [ ] <decision>
- [ ] <decision>

## 12. Agent Execution Log
A running log of every agent that has contributed, in order:
| Date/Time | Agent | Output File | Key Decisions |
|-----------|-------|-------------|---------------|
| YYYY-MM-DD HH:MM | Brand Strategist | 01-brand-strategy.md | Defined primary audience as X; chose tagline Y |
| YYYY-MM-DD HH:MM | Pricing Strategist | 02-pricing-strategy.md | Chose freemium with 3 tiers: Sadhak/Bhakt/Arjun |
```

---

## Agent Responsibilities

Every marketing agent MUST follow this protocol.

### Before Starting Work

1. **Check for context file**: Look for `.marketing-context.md` in the project root and in `docs/marketing-plan/<project>/`.
2. **Read it fully if it exists**: Absorb all previous decisions. Do NOT skim.
3. **Honor existing decisions**: If the context says primary audience is "Seeking Millennials 25-40," do NOT propose a different audience. Build on that.
4. **If context file does NOT exist**: You are likely the first agent. Ask the user if this is a new playbook. If yes, create the context file with basic project info and proceed.

### During Work

1. **Reference context decisions explicitly**: In your output document, cite which decisions from the context file you're building on. Example: "Per the brand strategy (01-brand-strategy.md), the primary audience is Seeking Millennials. This content strategy targets that segment..."
2. **Flag conflicts**: If you disagree with an earlier decision, do NOT silently override it. Add a note: "Note: This recommendation conflicts with the pricing decision in context file section 5. Recommend discussing with user before finalizing."
3. **Stay in your lane**: If another agent owns a section of the context (see the "owned by" tags), you can reference it but NOT rewrite it.

### After Finishing Work

1. **Update the context file**: Add a new entry to Section 12 (Agent Execution Log) with date, agent name, output file, and key decisions made.
2. **Fill in your owned section**: If you own a section (e.g., Brand Strategist owns Section 3 Positioning), populate it with your decisions.
3. **Add to Open Decisions if needed**: If your work surfaces new questions for later agents, list them in Section 11.
4. **Update "Last updated" metadata** at the top of the context file.

---

## The Playbook Editor (Reconciliation Agent)

After all agents in a playbook have run, the Marketing Playbook Editor runs last. Its job:

1. Read the context file
2. Read all output documents (01-brand-strategy.md, 02-pricing-strategy.md, etc.)
3. Find conflicts between documents (e.g., Doc 03 and Doc 04 defining different content pillars)
4. Produce a reconciliation report listing conflicts and proposing resolutions
5. Update the context file with final, unified decisions
6. Optionally, produce a single consolidated playbook document

The Playbook Editor has the authority to flag contradictions but NOT to silently rewrite specialist agents' work. Its output is a reconciliation report + unified context, not edits to individual docs.

---

## Example Context File Lifecycle

```
Time 1: User invokes Marketing Orchestrator
    → Orchestrator runs intake (5 questions + gap audit)
    → Orchestrator CREATES .marketing-context.md with basic project info
    → Orchestrator routes to agent sequence

Time 2: Brand Strategist runs
    → READS .marketing-context.md (sees basic info only)
    → Produces 01-brand-strategy.md
    → UPDATES .marketing-context.md with Sections 2, 3, 4 filled in
    → Adds execution log entry

Time 3: Pricing Strategist runs
    → READS .marketing-context.md (sees basic info + brand decisions)
    → Uses brand positioning to inform pricing psychology
    → Produces 02-pricing-strategy.md
    → UPDATES .marketing-context.md with Section 5 filled in
    → Adds execution log entry

Time 4: Content Creator runs
    → READS .marketing-context.md (sees brand + pricing)
    → Designs content pillars that ALIGN with brand voice and pricing tiers
    → Produces 03-content-strategy.md
    → UPDATES Section 6 with pillars
    → Adds execution log entry

Time 5: Instagram Curator runs
    → READS .marketing-context.md (sees brand + pricing + content pillars)
    → Does NOT reinvent content pillars — executes Doc 03's pillars on Instagram specifically
    → Produces 04-instagram-strategy.md focused ONLY on Instagram-specific tactics
    → NO overlap with Doc 03
    → Adds execution log entry

...continues...

Time N: Marketing Playbook Editor runs
    → READS .marketing-context.md + all output docs
    → Checks for conflicts
    → Produces reconciliation report
    → Finalizes context file
```

---

## Protocol Enforcement

Every marketing agent's file should include a reference to this protocol in its "Critical Rules" section. The reference looks like:

```markdown
### Context Protocol (MANDATORY)
This agent follows the Marketing Context Protocol defined in
`marketing/CONTEXT_PROTOCOL.md`.

Before starting:
- Read `.marketing-context.md` if it exists (project root or docs/marketing-plan/)
- Honor all decisions made by previous agents
- Cite which prior decisions you're building on

After finishing:
- Update `.marketing-context.md` with your decisions in your owned section
- Add an entry to the Agent Execution Log
- Flag any conflicts with earlier decisions as Open Decisions

Do NOT silently override earlier agent decisions.
```

---

## Ownership Map

Which agent owns which context section:

| Context Section | Owning Agent |
|-----------------|-------------|
| 1. Project Basics | Marketing Orchestrator (intake) |
| 2. Target Audience | Brand Strategist |
| 3. Positioning | Brand Strategist |
| 4. Brand Voice | Brand Strategist |
| 5. Pricing Model | Pricing Strategist |
| 6. Content Pillars | Content Creator |
| 7. Channel Strategy | Social Media Strategist / Solo Marketing |
| 8. Funnel & Conversion | Page CRO + Signup Flow Optimizer + Onboarding CRO |
| 9. Measurement | Analytics Tracking Engineer |
| 10. Growth Loops | Referral Program Designer + Growth Hacker |
| 11. Open Decisions | All agents can add, Playbook Editor resolves |
| 12. Agent Execution Log | All agents append |

Other agents (Instagram Curator, SEO Specialist, Email Sequence Builder, etc.) READ the context but do not own primary sections. They contribute platform-specific execution layered on top of owned decisions.
