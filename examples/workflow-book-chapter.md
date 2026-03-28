# Workflow: AI-First Book Chapter Development

> A focused single-agent workflow for turning rough founder notes into a structured, voice-authentic chapter draft.

## When to Use This

Use this when you have a clear point of view on something but not a clean draft. Raw material might be voice memos, bullet points, a LinkedIn post that got traction, or a talk you gave. The goal is not to rewrite your thinking — the goal is to make it readable without losing what makes it yours.

## Agent Used

| Agent | Role |
|---|---|
| Book Co-Author | Transforms source material into a versioned chapter draft with editorial notes and explicit revision asks |

---

## Example Activation

This example is for a book aimed at technical founders and engineering leaders on building AI-native products — not AI features bolted onto existing products, but products that would be impossible without AI at the core.

```
Activate Book Co-Author.

Book context:
Title working draft: "Native — Building Products That AI Makes Possible"
Audience: Technical founders, engineering leads, CTOs at startups and scale-ups.
Core argument of the book: Most companies are adding AI features to existing products.
  The companies that win the next decade are building products where AI isn't a feature
  — it's the product. The architecture, the business model, and the go-to-market all
  look different when you start from AI-native rather than bolt it on.

Chapter: Chapter 3 — "The Retrofit Trap"
Chapter goal: Explain why retrofitting AI onto an existing product is harder than
  it looks, often produces worse results than a greenfield AI-native build, and
  signals a product strategy problem, not just a technical one.

Raw material:
- Voice note (transcribed): "The thing nobody talks about is that legacy data
  architecture is the real killer. You can't RAG your way out of a fragmented
  data model. I've seen this at three companies now — they spend 6 months on the
  AI layer and then realize the actual problem is that their core data is in five
  different schemas maintained by different teams who don't talk to each other."

- LinkedIn thread that got 800 likes: "Adding an AI assistant to your product
  is not an AI strategy. It's a UI upgrade. The companies winning with AI right
  now aren't the ones with the best LLM — they're the ones who redesigned their
  data model 18 months ago and are now running inference on clean, structured,
  proprietary data that no one else has."

- Example I want to include: A fintech I talked to that spent $1.2M on an AI
  underwriting feature. The model was fine. But the training data was transaction
  records from 4 acquired companies that had never been normalized. The AI was
  learning from noise. They scrapped the feature after 9 months.

- Contrasting example: A competitor (won't name them) that started from scratch
  with AI-native data architecture. Same problem space. Shipped in 5 months,
  charging 40% premium over the incumbent.

Positioning angle for this chapter: The retrofit trap isn't a technology problem.
  It's a decision-making problem. Leaders choose the retrofit because it feels
  lower risk. The chapter argues the opposite — the retrofit is higher risk,
  it just hides the risk until later.

Produce:
1. Chapter objective and how it fits the book's arc
2. Any clarification questions before you draft (ask them now, not mid-draft)
3. Chapter 3 — Version 1, ready for author review
4. Editorial notes: what assumptions are made, what needs a real example or citation
5. Three specific revision requests for next session
```

---

## Expected Output Structure

The Book Co-Author should return five distinct sections:

**1. Chapter Objective**
A 2-3 sentence statement of what this chapter accomplishes and what the reader should believe by the end of it that they didn't before.

**2. Clarification Questions**
Specific things the author needs to answer before a second draft: missing examples, unclear positions, gaps in the argument.

**3. Chapter Draft — Version 1**
Full prose draft in first-person voice. Structured with a clear opening, argument, examples, and close. 1,500-2,500 words.

**4. Editorial Notes**
What claims are asserted without evidence. What examples are thin. Where the voice sounds generic. Where the argument has a logic gap.

**5. Revision Requests for Next Session**
3-5 specific asks: "Find a real data point for the claim about retrofit costs" or "The fintech example needs a concrete outcome — what happened to the product?"

---

## Quality Bar

- First-person voice throughout — reads like the author, not a writing assistant
- Every claim tied to source material or explicitly flagged as an assumption
- No business book clichés: "in today's fast-paced world", "unlock potential", "paradigm shift"
- The chapter has one thesis it earns, not five it gestures at
- Ends with explicit revision questions — not "great job, what next?"

---

## Revision Loop

After the first draft, the workflow continues:

```
Activate Book Co-Author.

Here is Version 1 of Chapter 3: [paste draft]
Here are your editorial notes from last session: [paste notes]

Author feedback:
- The fintech example is strong. Keep it as the centerpiece.
- The contrasting example is thin — I don't want to name the competitor.
  Replace with a hypothetical that's clearly labeled as such.
- The opening paragraph doesn't grab. I want it to start with a question
  that the reader has been avoiding asking themselves.
- The argument in section 2 goes too long. Tighten it by 30%.

Produce Version 2. Show editorial notes again for whatever remains unresolved.
```

The loop continues until the chapter is ready for a developmental editor.
