# The Three Modes

*Reading time: ~9 min. Outcome: Know when to ask a quick question, when to request deep analysis, and when to run a long agentic job.*

Not every task needs the same level of effort. A quick definition takes 5 seconds. A full deal analysis takes 20 minutes. Knowing which mode to use saves time and gets better results.

## The three modes

| Mode | When to use | How long it takes | Example prompt |
|---|---|---|---|
| **Quick Q&A** | Single-fact lookups, definitions, clarifications, simple calculations. | Seconds to 1 minute. | "What is SDE vs EBITDA?" / "Calculate the multiple if revenue is $2.1M and asking price is $4.8M." |
| **Deep analysis** | Evaluating one target, building a comp model, scoring a business against your AQ criteria, drafting a financing structure. | 5–15 minutes. | "Score this CIM against my AQ criteria and flag any reds." / "Build a 3-comp valuation model for this business." |
| **Long agentic job** | Sourcing a target list, researching a vertical, building a multi-business scorecard, drafting a full deal memo with comps and financing options. | 15–45 minutes. | "Find 20 B2B service businesses in Orange County meeting my buy box, score each, pull comps, and write the target list." |

## Quick Q&A — when you just need an answer

Use this mode for:
- Terminology questions ("What is a wraparound note?").
- Fast calculations ("If SDE is $420K and the asking price is $1.05M, what is the multiple?").
- Clarifying a concept ("Explain the 70% Rule in one paragraph.").

**What the prompt looks like:**
> "What is the difference between SDE and EBITDA?"

> "Calculate the valuation multiple: $2.3M revenue, $680K SDE, asking price $1.7M."

Claude answers in one turn. No research, no multi-step reasoning.

## Deep analysis — when you need Claude to think

Use this mode for:
- Scoring a target against your AQ criteria.
- Building a valuation model with comps.
- Drafting a financing structure (STACK of multiple strategies).
- Reviewing a CIM or financials and flagging reds.

**What the prompt looks like:**
> "I am uploading a CIM for a $2.1M revenue B2B consulting firm. Score it against my AQ criteria (13 green/yellow/red checks). Flag any reds and recommend whether to pursue."

> "Build a 3-comp valuation model for this HVAC business. Pull comps from the web (B2B home services, $1-3M revenue, last 24 months), normalize for SDE, and give me a fair-value range."

Claude will research, reason, and structure the output (often as an artifact). Expect 5-15 minutes depending on how much research is required.

## Long agentic job — when you need Claude to run the whole task

Use this mode for:
- Sourcing a target list (find businesses, score them, pull comps, write the report).
- Vertical research (industry trends, competitive landscape, acquisition opportunities).
- Multi-business scorecard (run AQ scoring on 10-20 targets and rank them).
- Full deal memo (valuation, comps, financing STACK, negotiation strategy, red flags, recommendation).

**What the prompt looks like:**
> "Find 20 B2B professional services businesses in Orange County CA meeting my buy box ($1-5M revenue, $300K-1M SDE, owner-operated). For each: pull the listing, score AQ criteria, flag reds. Rank by attractiveness and deliver the target list as a markdown table."

> "I am uploading financials for a $3.2M revenue IT consulting firm. Build a full deal memo: (1) 3-comp valuation model, (2) AQ scorecard, (3) financing STACK using seller financing + earnout + consulting offset, (4) negotiation strategy (walk-away/realistic/dream), (5) red flags and mitigations, (6) go/no-go recommendation."

Claude will break the task into steps, research, analyze, and deliver a complete report. Expect 15-45 minutes. You can walk away and come back when it is done.

## Acquisition examples (one task, three modes)

**Task: Evaluate a $2.1M B2B consulting business.**

| Mode | Prompt | Output |
|---|---|---|
| **Quick Q&A** | "Is a 40% EBITDA margin good for a B2B consulting firm?" | One-paragraph answer: "Yes, 40% is strong. Industry average is 20-30%. This suggests pricing power or operational efficiency. Confirm it is sustainable and not dependent on one customer." |
| **Deep analysis** | "Score this CIM against my AQ criteria and recommend go/no-go." | AQ scorecard (13 criteria, green/yellow/red), red flags highlighted, recommendation with reasoning. 5-10 minutes. |
| **Long agentic job** | "Build a full deal memo: valuation, comps, financing STACK, negotiation strategy, reds, recommendation." | 8-page memo with sections: executive summary, valuation model (3 comps), AQ scorecard, financing STACK (5 strategies), negotiation range (walk-away/realistic/dream), red flags + mitigations, go/no-go. 20-30 minutes. |

## What good looks like when you know the modes

- You do not waste time asking for a full analysis when you just need a definition.
- You do not try to run a long agentic job with a weak one-sentence prompt.
- You match the task to the mode and get the result faster.

Next: **Prompt Like a Buyer** — how to write owner-level prompts that get deal-ready outputs.
