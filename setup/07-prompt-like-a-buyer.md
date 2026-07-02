# Prompt Like a Buyer

*Reading time: ~10 min. Outcome: Write owner-level prompts using RCTF — Role, Context, Task, Format.*

The difference between "Claude summarized this" and "Claude delivered a deal-ready analysis" is the prompt. Good prompts are specific, structured, and tell Claude what outcome you need. The RCTF framework makes this automatic.

## RCTF: Role / Context / Task / Format

| Component | What it is | Why it matters |
|---|---|
| **Role** | Who Claude is acting as. | "You are an acquisition analyst" gets better results than no role. Claude reasons like the role you assign. |
| **Context** | Background Claude needs to do the task right. | Your buy box, the AQ criteria, the business details. Without context, Claude guesses. |
| **Task** | The specific job you want done. | "Score this business" is vague. "Score this business against my 13 AQ criteria and flag any reds" is clear. |
| **Format** | How you want the output structured. | Table, bullet list, markdown file, memo sections. Specifying format prevents Claude from rambling. |

## Three acquisition examples: weak vs. owner-level

### Example 1: Qualifying a target

**Weak prompt:**
> "Is this a good business?"

**Why it is weak:** No context (good for what?), no criteria (good by what standard?), no format (how should Claude answer?).

**Owner-level prompt (RCTF):**
> **Role:** You are an acquisition analyst evaluating small B2B businesses.  
> **Context:** My buy box: B2B professional services, $1-5M revenue, $300-1M SDE, owner-operated, Orange County CA. My AQ criteria: 13 green/yellow/red checks (location, seller finance, margin, staff, own property, training, etc.).  
> **Task:** Score this CIM against my AQ criteria. Flag any reds and recommend go/no-go.  
> **Format:** Deliver as a table with 13 rows (criterion / score / notes), followed by a summary paragraph.

**Why it works:** Claude knows the role (analyst), has the criteria (AQ scorecard), knows the task (score and recommend), and knows the output format (table + summary). No guessing.

---

### Example 2: Building a valuation model

**Weak prompt:**
> "What is this business worth?"

**Why it is weak:** No context (worth based on what comps?), no method (multiple of revenue? SDE? EBITDA?), no format.

**Owner-level prompt (RCTF):**
> **Role:** You are a valuation analyst specializing in small business acquisitions.  
> **Context:** This is a $2.3M revenue, $680K SDE B2B consulting firm in Orange County. Industry standard multiples: owner-operated businesses trade at 2.4x SDE, professionally managed at 4.0x EBITDA.  
> **Task:** Build a 3-comp valuation model. Pull comparable sales from the web (B2B professional services, $1-3M revenue, last 24 months). Normalize for SDE. Give me a fair-value range and explain any adjustments.  
> **Format:** Deliver as a markdown table with columns: Business / Revenue / SDE / Sale Price / Multiple / Notes. Follow with a summary paragraph: fair-value range, recommended offer, reasoning.

**Why it works:** Claude knows the method (SDE multiples + comps), knows where to source data (web search, B2B services, recent sales), and knows the output format (table + summary). You get a comp model, not a guess.

---

### Example 3: Drafting a financing structure

**Weak prompt:**
> "How can I buy this business with no money down?"

**Why it is weak:** No context (business details? seller motivation?), no method (which funding strategies?), no format.

**Owner-level prompt (RCTF):**
> **Role:** You are a creative deal-structuring advisor specializing in no-money-down acquisitions.  
> **Context:** This is a $1.8M asking price B2B consulting firm. Owner is 68, wants to retire, open to seller financing. The business does $2.1M revenue, $620K SDE. I have access to the 13 EPIC funding strategy families (seller financing, earnouts, consulting offsets, pre-sale promotions, asset carveouts, etc.).  
> **Task:** Build a financing STACK using 3-5 strategies to get to $0 cash at closing. Include seller financing (5-year note), earnout (tied to revenue retention), and consulting offset (owner stays on as advisor, fee applied to purchase price). Show the math: how much each strategy covers, what the seller receives at closing vs. over time.  
> **Format:** Deliver as a markdown table with columns: Strategy / Amount / Terms / Timing. Follow with a narrative explaining the seller's perspective (why this structure works for them) and the risk mitigations.

**Why it works:** Claude knows the funding families (EPIC strategies), has the business details (price, SDE, owner motivation), knows the task (STACK to $0 cash), and knows the format (table + narrative). You get a real structure, not theory.

---

## The pattern

Every owner-level prompt follows RCTF:
1. **Role:** "You are a [acquisition analyst / valuation expert / deal structuring advisor]."
2. **Context:** Buy box, AQ criteria, business details, seller motivation, your constraints.
3. **Task:** The specific job (score, value, structure, research, draft).
4. **Format:** Table, memo, markdown file, bullet list, artifact.

## What good looks like when you prompt like a buyer

- You get deal-ready outputs on the first try, not vague summaries.
- Claude uses your criteria (AQ scorecard, funding families, buy box) without you re-explaining them.
- The output is structured and actionable (tables, memos, scorecards), not rambling paragraphs.
- You can save the prompt as a skill and re-run it on every new target.

Next: **Models and Plans** — how to pick the right Claude model tier and when to upgrade.
