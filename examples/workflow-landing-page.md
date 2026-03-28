# Multi-Agent Workflow: Landing Page in a Day

> Ship a conversion-optimized landing page before end of business using 4 agents.

## The Scenario

You're launching **Forge** — an AI-powered code review platform that catches logic errors, security vulnerabilities, and performance bottlenecks before PRs are merged. You have a working product and a Product Hunt launch in 48 hours. You need a landing page today.

## Agent Team

| Agent | Role |
|---|---|
| Content Creator | Write all copy |
| UI Designer | Define layout, visual system, component specs |
| Frontend Developer | Build the page |
| Growth Hacker | Optimize for conversion and handle SEO basics |

---

## Morning: Copy + Design (run both in parallel)

### Step 1a — Content Creator

```
Activate Content Creator.

Write landing page copy for Forge — an AI code review tool that integrates into GitHub and GitLab PRs.

What it does:
- Reviews PRs automatically on push
- Catches logic bugs, security issues (OWASP top 10), and N+1 queries
- Explains every issue in plain English with a suggested fix
- Learns your codebase over time — fewer false positives each week

Target audience: Engineering managers and senior developers at 10-200 person companies.
Primary CTA: "Start free trial" (14 days, no credit card).
Tone: Direct, technically credible, no buzzwords. Write for engineers who are tired of hype.

Sections needed:
1. Hero — headline + 1-line subheadline + CTA button
2. Problem — what code review looks like without Forge (3 specific pain points, not generic)
3. How it works — 3 steps, each one sentence
4. What it catches — 4-6 specific issue types with a short example for each
5. Social proof — placeholder format for 2 engineering manager quotes
6. Pricing — Free (up to 3 repos), Pro ($49/month, unlimited), Team ($149/month, includes analytics)
7. Final CTA section

Rules: No passive voice. No "powerful", "seamless", or "cutting-edge". Every claim must be falsifiable.
```

### Step 1b — UI Designer (run in parallel)

```
Activate UI Designer.

Design specs for the Forge landing page (AI code review tool for engineering teams).

Aesthetic direction: Technical credibility without being a wall of text. Reference points: Vercel, Railway, Resend — clean dark UI with strong typography.

Deliver:
1. Color system — background, surface, border, text (primary/secondary/muted), accent, CTA button
2. Typography — font pairing (use Google Fonts or system fonts), heading scale (h1 through h4), body and caption sizes
3. Layout spec — section order, max-width, vertical rhythm, grid columns
4. Component specs for:
   - Hero section (with and without a product screenshot placeholder)
   - "How it works" 3-step row
   - Issue type cards (icon + title + 1-line description)
   - Pricing cards (3 tiers)
   - CTA banner
5. Responsive behavior — what collapses on mobile, what stacks

Output a spec document, not a design file.
```

---

## Midday: Build

### Step 2 — Frontend Developer

```
Activate Frontend Developer.

Build the Forge landing page from these specs.

Copy: [paste Content Creator output]
Design spec: [paste UI Designer output]

Technical requirements:
- Single index.html using Tailwind CDN (no build step needed — this ships today)
- Lightweight — no images heavier than SVG placeholders, system font fallback acceptable
- Accessible — semantic HTML, ARIA labels on interactive elements, keyboard navigable
- Working email capture form (POST to /api/waitlist, show success message on submit)
- No JavaScript frameworks — vanilla JS only for the form submit and any micro-interactions

Deliver a single clean index.html file. Comment the sections so it's easy to swap copy later.
```

---

## Afternoon: Optimize

### Step 3 — Growth Hacker

```
Activate Growth Hacker.

Review the Forge landing page for conversion rate optimization and SEO ahead of a Product Hunt launch tomorrow.

Page: [paste HTML or describe the current page structure]

Audit these 5 areas and give specific fixes, not general advice:

1. First 5 seconds — does the hero communicate the value in one read?
   What to change if no.

2. CTA placement and friction — is "Start free trial" appearing at the right moments?
   How many times should it appear? Where exactly?

3. Trust signals — what's missing that an engineering manager would look for before signing up?
   (examples: GitHub stars count, # of issues caught, company logos)

4. Product Hunt optimization — what specific copy or social proof helps with PH audience?

5. SEO basics for launch day:
   - title tag
   - meta description
   - og:title and og:description
   - Canonical URL
   - H1/H2 structure

Output: numbered list of changes, ordered by impact. Include the exact copy or code change for each.
```

---

## Timeline

| Time | Activity | Agent |
|---|---|---|
| 09:00 | Copy + design kick off (parallel) | Content Creator + UI Designer |
| 11:30 | Both outputs reviewed, build starts | — |
| 14:00 | First build complete | Frontend Developer |
| 14:30 | Conversion + SEO audit | Growth Hacker |
| 15:30 | Apply Growth Hacker changes | Frontend Developer |
| 16:30 | Final review — does it convert? | You |
| 17:00 | Deploy to Vercel | Ship |

---

## Key Patterns

**Copy and design in parallel** — They don't depend on each other. Running them simultaneously saves 2+ hours. The Frontend Developer is the merge point — they need both before starting.

**Ship-ready constraints** — The Frontend Developer is told to produce a single `index.html` with no build step. This forces a decision: no framework sprawl, ships today.

**Growth Hacker reviews output, not input** — The optimizer reviews the finished page, not the brief. This catches problems that looked fine on paper but land wrong in the browser.

**Specific over general** — Every activation prompt asks for specific changes. "Your hero might need work" is not useful. "Change the headline to lead with the outcome, not the mechanism" is.
