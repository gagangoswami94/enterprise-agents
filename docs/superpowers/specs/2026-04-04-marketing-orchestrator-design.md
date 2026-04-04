# Marketing Orchestrator — Design Spec

**Date**: 2026-04-04
**Status**: Approved
**Output**: `marketing/marketing-orchestrator.md`

---

## Problem

The marketing/ directory contains 58 agents but zero routing logic. A user — especially a beginner — has no way to know which agent to use first, which to skip, or what order to follow. The result: people grab the obvious agents and miss the ones that would actually help most.

This was validated in a real test: building a marketing plan for saarthikrishna.com used only 2 of 19 new agents because there was no system to surface the right ones.

## Solution

A **Marketing Orchestrator** agent that:
1. Assesses the user's business stage, marketing maturity, team size, and budget
2. Audits what marketing infrastructure already exists (gap analysis)
3. Outputs a sequenced, phased Marketing Action Plan routing to specific agents in order
4. Adapts communication depth to the user's experience level

It is a **diagnostic engine**, not a marketer. It does not write copy, design campaigns, or execute. It assesses, routes, and sequences.

---

## Intake Assessment

### 5 Mandatory Questions

```
Q1: What's your product/business? (URL or description)
Q2: What stage are you at?
    - Pre-launch (building, no users yet)
    - Launch (just launched or about to)
    - Growth (have users, need more)
    - Scale (established, optimizing)
Q3: What's your marketing experience?
    - Zero (never done marketing)
    - Basic (tried some channels, inconsistent)
    - Intermediate (running campaigns, tracking results)
    - Advanced (multi-channel, data-driven)
Q4: Team size for marketing?
    - Just me (solopreneur)
    - Small team (2-5)
    - Marketing department (5+)
Q5: Monthly marketing budget?
    - $0 (sweat equity only)
    - Under $1K
    - $1K-$10K
    - $10K+
```

### Gap Audit Checklist

Auto-detect from URL if provided, otherwise ask:

| # | Gap Check | Detection Method |
|---|-----------|-----------------|
| 1 | Website/landing page live? | Fetch URL |
| 2 | Analytics/tracking set up? | Check for GA4/GTM tags |
| 3 | Pricing visible? | Scan page for pricing section |
| 4 | Email capture in place? | Look for forms, popups, newsletter |
| 5 | Social media accounts active? | Check for social links on site |
| 6 | Content being published? | Blog section, recent posts |
| 7 | Paid ads running? | Ask user |
| 8 | SEO basics done? | Check meta tags, sitemap, schema |
| 9 | Referral/viral mechanics? | Ask user |
| 10 | CRO ever done? | Ask user |

---

## Routing Matrix

### Stage x Maturity → Agent Sequence

#### Pre-Launch

| Maturity | Agent Sequence (in order) |
|---|---|
| Zero | 1. Brand Strategist → 2. Pricing Strategist → 3. Page CRO Specialist → 4. Analytics Tracking Engineer → 5. Content Creator → 6. Solo Marketing (if solopreneur) |
| Basic+ | 1. Brand Strategist → 2. Pricing Strategist → 3. Page CRO Specialist → 4. Lead Magnet Designer → 5. Email Sequence Builder → 6. Launch Campaign Manager |

#### Launch

| Maturity | Agent Sequence (in order) |
|---|---|
| Zero | 1. Analytics Tracking Engineer → 2. Page CRO Specialist → 3. Signup Flow Optimizer → 4. Content Creator → 5. App Store Optimizer (if app) → 6. Launch Campaign Manager |
| Basic | 1. Analytics Tracking Engineer → 2. Signup Flow Optimizer → 3. Launch Campaign Manager → 4. Email Sequence Builder → 5. Referral Program Designer → 6. Cold Email Specialist (if B2B) |
| Intermediate+ | 1. Launch Campaign Manager → 2. A/B Test Architect → 3. Referral Program Designer → 4. Performance Marketer → 5. Influencer Marketing Specialist |

#### Growth

| Maturity | Agent Sequence (in order) |
|---|---|
| Zero/Basic | 1. Analytics Tracking Engineer → 2. SEO Specialist → 3. Content Creator → 4. Email Sequence Builder → 5. Page CRO Specialist → 6. Referral Program Designer |
| Intermediate | 1. A/B Test Architect → 2. CRO Suite (Page → Signup → Onboarding → Form) → 3. Email Sequence Builder → 4. Programmatic SEO Specialist → 5. Performance Marketer |
| Advanced | 1. RevOps Specialist → 2. A/B Test Architect → 3. Paywall Upgrade Optimizer → 4. Retention Marketing Specialist → 5. Referral Program Designer → 6. Free Tool Strategist |

#### Scale

| Maturity | Agent Sequence (in order) |
|---|---|
| Any | 1. RevOps Specialist → 2. A/B Test Architect → 3. Full CRO Suite → 4. Programmatic SEO → 5. Performance Marketer → 6. Retention Marketing Specialist → 7. Market Research Analyst |

### Gap-Based Priority Overrides

Regardless of stage, critical gaps inject agents at the top of the sequence:

| Gap Found | Agent Injected | Priority |
|---|---|---|
| No analytics | Analytics Tracking Engineer | P0 — always first |
| No pricing | Pricing Strategist | P0 |
| Landing page issues | Page CRO Specialist | P1 |
| No email capture | Lead Magnet Designer + Email Sequence Builder | P1 |
| No social presence | Content Creator + platform-specific agent | P2 |
| No SEO basics | Site Architecture Strategist + Schema Markup Engineer | P2 |

P0 gaps override everything — they go to position 1-2 in the sequence regardless of what the stage matrix says.

---

## Output Format

The orchestrator produces a **Marketing Action Plan**:

```markdown
# Marketing Action Plan

## Your Profile
- **Stage**: [Pre-launch/Launch/Growth/Scale]
- **Maturity**: [Zero/Basic/Intermediate/Advanced]
- **Team**: [Solo/Small/Department]
- **Budget**: [$0/$1K/$10K+]

## Critical Gaps (Fix First)
[P0/P1 gaps with agent assignments]

## Your Agent Sequence (Do In This Order)

### Phase 1: Foundation (Weeks 1-2)
| # | Agent | What It Does For You | Time |
|---|-------|---------------------|------|
| 1 | [Agent] | [Plain English benefit] | [Estimate] |

### Phase 2: Conversion (Weeks 3-4)
[...]

### Phase 3: Growth (Weeks 5-8)
[...]

### Phase 4: Optimization (Weeks 9-12)
[...]

## Agents NOT Needed Yet
[List with note on when they become relevant]

## Jargon Glossary (if maturity = Zero)
[Auto-included definitions of all acronyms used above]
```

### Output Rules

- Phases map to calendar weeks so the user knows what to do when
- Time estimates per agent — solopreneurs need to know the cost
- "Not Needed Yet" section prevents overwhelm
- Auto-glossary only shown when maturity = Zero
- Bold the FIRST action — never present 10 things with equal weight

---

## Communication Style

Adapts based on maturity level:

| Maturity | Style |
|---|---|
| Zero | Explain every term. Use analogies. "CAC is what it costs you to get one user — like your cost-per-download." |
| Basic | Light explanations. Skip obvious terms. |
| Intermediate+ | Talk shop. No hand-holding. |

Additional rules:
- Solopreneur: Always flag time cost. "This agent session takes ~2 hours. Worth it now or defer?"
- Always state what to do FIRST in bold
- Never present 10 things with equal weight

---

## Agent Catalog (58 agents, grouped by typical order)

### Foundation (almost always first)
- Analytics Tracking Engineer
- Brand Strategist
- Pricing Strategist
- Site Architecture Strategist

### Conversion (fix before driving traffic)
- Page CRO Specialist
- Signup Flow Optimizer
- Onboarding CRO Specialist
- Form CRO Specialist
- Popup/Modal Optimizer
- Paywall Upgrade Optimizer

### Acquisition (drive traffic)
- Content Creator
- SEO Specialist
- Programmatic SEO Specialist
- Schema Markup Engineer
- Performance Marketer
- Cold Email Specialist
- Social Media Strategist
- Instagram Curator
- TikTok Strategist
- LinkedIn Content Creator
- Twitter Engager
- Reddit Community Builder
- Influencer Marketing Specialist
- App Store Optimizer
- Launch Campaign Manager
- Growth Hacker
- Video Optimization Specialist
- Short Video Editing Coach
- Podcast Strategist
- Carousel Growth Engine
- AI Citation Strategist
- Book Co-Author
- PR Communications Specialist

### Retention (keep users)
- Email Sequence Builder
- Retention Marketing Specialist
- Referral Program Designer
- Free Tool Strategist
- Lead Magnet Designer
- Community Marketing Manager
- Consumer Psychologist

### Measurement (optimize)
- A/B Test Architect
- Copy Editor
- Market Research Analyst
- RevOps Specialist
- Product Marketing Manager

### China/APAC Market (only when indicated)
- China Market Localization Strategist
- Douyin Strategist
- Kuaishou Strategist
- Xiaohongshu Specialist
- Zhihu Strategist
- Bilibili Content Strategist
- Baidu SEO Specialist
- Weibo Strategist
- WeChat Official Account
- China E-Commerce Operator
- Livestream Commerce Coach
- Private Domain Operator
- Cross-Border E-Commerce

---

## What This Agent Does NOT Do

- Does not write copy, design campaigns, or execute marketing tasks
- Does not replace individual specialist agents
- Does not make budget allocation decisions (defers to Performance Marketer / Pricing Strategist)
- Does not provide generic advice — every recommendation maps to a specific agent

---

## Success Criteria

- User at "zero marketing" can get a clear, ordered plan within 5 minutes
- Every agent recommendation is justified by stage + maturity + gap data
- No jargon left unexplained for Zero-maturity users
- The plan is actionable on day 1 — first action is always concrete and doable
- Advanced users get routed efficiently without beginner hand-holding
