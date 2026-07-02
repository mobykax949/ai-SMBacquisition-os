---
name: aq-analyzer
description: Use when qualifying a deal after first contact. Runs the 13-criterion AQ Score (location, seller finance, broker, long listing, margin, history, FF&E, multiple, leased space, own property, staff, inventory, training) with red/yellow/green ratings and a go/pass/dig-deeper verdict.
version: 1.0.0
---

# AQ Analyzer

## Overview

Run the 13-criterion Acquisition Qualification Score on a business after your first call or after reviewing a broker listing. You will rate each criterion green (favorable), yellow (unknown or neutral), or red (unfavorable), then get a go/pass/dig-deeper verdict and the 2 highest-leverage questions to ask on the next call. This is the fast filter that tells you whether to keep spending time on a deal before you enter deep due diligence. The AQ Score is Roland Frasier's canonical screen from the EPIC Network framework.

## When to Use

- You just had a discovery call with a business owner and need to decide if you should pursue the deal
- You found a BizBuySell or broker listing that looks interesting and want to run a structured qualification
- You have 5 warm leads and need to rank them by deal quality to prioritize your time
- You want to exit a bad deal early before wasting weeks on valuation and LOI prep

## Steps

1. **Gather available information on the business.** You need: location, asking price or revenue, years in business, profitability estimate, whether it is broker-listed, how long it has been listed (if on-market), whether the seller mentioned financing, property ownership status, employee count, and whether the seller offers training or transition support. If you do not have all of this after the first call, mark those criteria yellow and plan follow-up questions.

2. **Open your Claude Acquisition Engine Project.** Make sure the AQ Score criteria file is uploaded to Project Knowledge (see claude-acquisition-setup skill). If not, paste the 13 criteria into the chat: location, seller finance, broker, long listing, margin, history, FF&E, multiple, leased space, own property, staff, inventory, training.

3. **Paste the business details into Claude and ask for the AQ Score.** Use this prompt pattern: "You are a deal analyst. I need to run the AQ Score on this business. Here are the details: [paste business name, location, revenue, asking price, years in business, broker yes/no, days listed if applicable, profitability estimate, property owned yes/no/unknown, employee count, seller training offered yes/no/unknown]. Rate each of the 13 AQ criteria green/yellow/red and return a table with criterion, rating, evidence, and brief note."

4. **Review the ratings and identify reds.** Red on margin (unprofitable or margin under 10%), red on history (under 5 years old or declining revenue), red on multiple (asking 5x+ SDE), or red on staff (100% owner-dependent with no team) are serious flags. One red is not an automatic pass, but 3+ reds usually means the deal is not worth pursuing. Yellow means you need more information. Green is favorable.

5. **Ask Claude for the verdict.** Prompt: "Based on the AQ Score table above, give me a verdict: go (pursue this deal), pass (walk away), or dig deeper (gather more info before deciding). Explain the verdict in 2-3 sentences and highlight the biggest risk and the biggest opportunity."

6. **Ask Claude for the 2 highest-leverage next questions.** Prompt: "What are the 2 most important questions I should ask the seller on the next call to turn yellow ratings into green or red? Prioritize questions that de-risk the deal or confirm deal-breakers early." These questions focus your second call and avoid wasting time on low-priority details.

7. **Save the AQ Score as a file.** Download the analysis as markdown and save it as `aq-score-<business-name>-YYYY-MM-DD.md` in your acquisitions folder. If you decide to pass on the deal, note the reason in the file and archive it. If you decide to pursue, this file becomes the foundation for valuation and LOI prep.

## The Prompts

```
Prompt 1: Run the 13-criterion AQ Score

You are a deal qualification analyst. I need to run the AQ Score on a business I am evaluating. Here are the details:

Business Name: [name]
Location: [city, state]
Revenue: [amount or range]
Asking Price: [amount]
Years in Business: [number]
Broker Listed: [yes/no]
Days on Market: [number or N/A if off-market]
Profitability: [SDE estimate or unknown]
Property Owned: [yes/no/unknown]
Employees: [count]
Seller Training Offered: [yes/no/unknown]

Rate each of the 13 AQ criteria (location, seller finance, broker, long listing, margin, history, FF&E, multiple, leased space, own property, staff, inventory, training) as green (favorable), yellow (unknown/neutral), or red (unfavorable). Return a table: criterion, rating, evidence, note. Use the AQ Score file uploaded to this Project for the rating definitions.
```

```
Prompt 2: Generate go/pass/dig verdict and risk/opportunity summary

You are a deal strategist. Based on the AQ Score table above, give me a verdict: go (pursue this deal), pass (walk away now), or dig deeper (need more info). Explain the verdict in 2-3 sentences. Highlight: (1) the biggest risk (the red or yellow flag most likely to kill the deal), and (2) the biggest opportunity (the green factor or upside that makes this deal worth pursuing if risks are manageable).
```

```
Prompt 3: Generate the 2 highest-leverage follow-up questions

You are a discovery call strategist. Based on the AQ Score above, what are the 2 most important questions I should ask the seller on the next call? Prioritize questions that: (1) turn yellow ratings into green or red (close information gaps), or (2) confirm or rule out deal-breakers early (margin, owner-dependence, declining revenue). Format: Question 1: [question]. Why it matters: [1 sentence]. Question 2: [question]. Why it matters: [1 sentence].
```

## The Loop

Run the AQ Score after every discovery call or listing review. If the verdict is "dig deeper," schedule a second call with the 2 follow-up questions and re-run the AQ Score after that call. Some deals move from yellow-heavy (unknowns) to green-heavy (favorable) after one conversation. Others move from yellow to red (unfavorable) and you exit. The AQ Score is not a one-time snapshot. Update it as you learn more. Save each version with a date stamp so you can track how the deal evolved.

## Pitfalls

- **Rating everything yellow because you do not want to make a decision.** Yellow means you genuinely do not know. If the seller told you the business is profitable but would not share the exact SDE, that is yellow on margin. If the seller said "we are barely breaking even," that is red, not yellow. Be honest with the ratings.
- **Passing on a deal because of one red when the rest is green.** One red is a risk, not an automatic no. If the business is red on "leased space" (short lease term) but green on everything else, you can negotiate a lease extension as a condition of the deal. Three reds or a red on a non-negotiable criterion (margin, history, multiple) is when you pass.
- **Running the AQ Score before the first call.** Six of the 13 criteria can be pre-scored from public data (location, broker, history, own property, staff, inventory). The other 7 require seller conversation. Do not guess. Mark them yellow and ask on the call.
- **Not saving the AQ Score outside Claude.** If you run 10 AQ Scores in one chat and do not download the files, you will lose them when you close Claude. Save each one as a markdown file with the business name and date. This builds a deal library you can reference later.
- **Skipping the follow-up questions step.** The AQ Score tells you what is wrong or unknown. The follow-up questions tell you how to fix it. If you run the score, get a "dig deeper" verdict, and then do not ask the 2 priority questions on the next call, you wasted the analysis.

## Output

A markdown file with the business name, 13-criterion AQ Score table (criterion, rating, evidence, note), go/pass/dig verdict with risk and opportunity summary, and the 2 highest-leverage follow-up questions for the next call. Save as `aq-score-<business-name>-YYYY-MM-DD.md` in your acquisitions folder. If you pursue the deal, this file feeds into valuation and LOI prep. If you pass, archive it with the reason noted so you do not re-evaluate the same deal 3 months later.
