---
name: discovery-interviewer
description: Use when you need to conduct the 50-question seller deep dive or rehearse the conversation with a seller simulator that role-plays a retiring owner and scores your performance.
version: 1.0.0
---

# Discovery Interviewer

## Overview

The structured seller discovery call engine. This skill guides you through the 50-question deep dive across six sections (story and motivation, operations, revenue and customers, profitability, marketing and sales, systems and documentation) and includes a seller-conversation simulator where Claude role-plays a realistic retiring business owner. The simulator lets you rehearse the call, then scores you on rapport-building, information extraction, and next-step clarity. Use this for every first call with a seller to ensure you gather the data needed for valuation and to avoid wasting time on deals that will not close.

## When to Use

Run discovery-interviewer after a seller responds positively to your outreach and agrees to a call. You need the seller's name, business name, industry, and approximate size. If you are new to seller calls or facing a high-stakes target, run the simulator first to practice your delivery. If you are confident, skip the simulator and go straight to the live-call question guide. After the call, feed your notes back into Claude to generate a summary and flag any red flags.

## Steps

1. **Decide: simulator rehearsal or live-call guide.** If this is your first seller call or you want to practice, use Prompt 1 (simulator). Claude will role-play a seller and you will conduct a mock call. If you are ready for the real call, use Prompt 2 (live question guide).

2. **Simulator path: conduct the mock call.** Paste Prompt 1. Claude becomes a realistic seller character (name, business, motivation). Start the call using the frame script provided. Ask discovery questions. Claude responds as the seller. After 10 to 15 exchanges, tell Claude "end simulation and score me." Claude evaluates your performance on three dimensions (rapport and trust-building, information extraction, next-step clarity) and gives specific feedback.

3. **Live-call path: load the question guide.** Paste Prompt 2 with the seller's details. Claude generates a prioritized question list tailored to the seller's industry and size. Print or keep this list on a second monitor during your call.

4. **Conduct the live discovery call.** Follow the frame script to open the call (introduce yourself, explain the three-phase process, position yourself as investor not broker, set the agenda). Then work through the six sections: (1) Story and motivation (why selling, why now, what next), (2) Operations (employees, owner role, hours per week, vacation test), (3) Revenue and customers (top line, growth trend, customer concentration, LTV, CAC, recurring revenue), (4) Profitability (net profit, owner comp, add-backs, COGS, fixed overhead), (5) Marketing and sales (channels, conversion rates, customer acquisition, database size), (6) Systems and documentation (procedures, software, bookkeeping, financials availability). Take detailed notes.

5. **Close with next steps.** At the end of the call, confirm the seller will send three years of financials, balance sheet, and cash flow statement. Give them a deadline (typically 5 to 7 days). Use the scarcity lever — the EPIC script's line is "our team vets only about six percent of deals to the next phase," but adapt it to what is true for you (a solo buyer says "I only take a small fraction of deals past this stage"); never claim a team or a statistic you don't have. Tell them what comes back after review is the "napkin offer" — the initial spreadsheet offer built around the terms they request — and plant the seed: the better the terms, the better the offer. Thank them and schedule the follow-up call.

6. **Debrief and flag red flags.** After the call, paste your notes into Prompt 3. Claude summarizes the key facts, computes a rough valuation estimate, and flags any red flags (customer concentration above 30 percent, declining revenue trend, seller unwilling to stay for transition, unresolved legal liabilities, financials not available). If red flags are deal-breakers, exit politely. If the deal is green, proceed to valuation.

## The Prompts

**Prompt 1: Seller Conversation Simulator**

```
I want to rehearse a seller discovery call. You will role-play a realistic business owner who is considering selling. Generate a character with these traits:

- Name: [choose a realistic first name]
- Business: [choose an industry from my buy-box: B2B services, e-commerce, SaaS, professional services]
- Business name: [invent a plausible name]
- Size: [$1-5M revenue, $300K-1M SDE]
- Motivation: Retiring (age 62-68), somewhat burned out, willing to consider creative terms but wants certainty
- Personality: Friendly but cautious, not finance-savvy, values legacy and employee retention

I will conduct the discovery call. You respond as this seller. After I say "end simulation," score me on:
1. Rapport and trust-building (did I frame the call well, show empathy, build credibility)
2. Information extraction (did I get the critical financial and operational facts)
3. Next-step clarity (did I set clear next steps and create urgency)

Start the simulation. I will open the call now.
```

**Prompt 2: Live Discovery Call Question Guide**

```
Generate the prioritized discovery question list for this seller:

- Business name: [name]
- Industry: [specific niche]
- Size: [revenue or employee count if known]
- Motivation: [if known from outreach conversation]

Organize the questions into the six EPIC sections:
1. Story and motivation (why selling, why now, what next, how long listed, valuation logic, seller financing openness)
2. Operations (employees, owner role, hours per week, procedures documented, vacation test)
3. Revenue and customers (gross revenue last 2 years and YTD, growth rate, customer concentration, LTV, CAC, recurring revenue, seasonality)
4. Profitability (net profit last 2 years and YTD, owner comp, add-backs claimed, COGS, fixed overhead, margins)
5. Marketing and sales (channels, conversion rates, customer database size, marketing spend, most/least effective channels)
6. Systems and documentation (bookkeeping system, software stack, financial statements available, IP and contracts, vendor and supplier agreements)

Prioritize the top 15 must-ask questions. Flag the 3 deal-breaker questions (if these answers are bad, walk away immediately).
```

**Prompt 3: Call Debrief and Red Flag Scan**

```
I just completed a discovery call with [seller name / business name]. Here are my notes:

[Paste your call notes here. Include any facts gathered on revenue, profit, owner role, customer concentration, seller motivation, financials availability, and any concerns.]

Summarize the key facts. Compute a rough valuation range (SDE method, 2.4x-3.5x owner-operated band depending on quality; the 4.0x anchor is an EBITDA multiple for professionally managed businesses and only applies if a management team runs this without the owner). Label the range as provisional if the SDE is seller-stated and unverified. Flag any red flags in these categories:
- Customer concentration >30%
- Declining revenue or profit trend
- Seller unwilling to transition or train
- Unresolved legal or tax liabilities
- Financials unavailable or incomplete
- Owner is the entire business (no team, no systems)

Recommend: Proceed to valuation / Renegotiate terms / Walk away.
```

## The Loop

The discovery call is the filter that saves you from bad deals. Run this skill for every seller conversation. After the call, review Claude's red flag scan. If the deal is green, proceed to valuation. If yellow (some concerns but fixable), schedule a follow-up call to address the gaps. If red (multiple deal-breakers), exit politely and move to the next target. And if the call reveals the owner is simply **not ready to sell** but runs a real business with upside — that is not a dead end: pivot to `cfe-converter` and pitch consulting-for-equity, or ask for a referral. No conversation is wasted. Do not skip the debrief step. Buyers who skip discovery waste weeks on deals that never close. Track your discovery call outcomes against Frasier's 70% Rule: the first conversation should kill roughly 70 percent of deals — that is the filter working, not failing. If nearly everything survives your first calls, you are not filtering hard enough and will waste weeks in diligence. If well over 90 percent die, your sourcing is off (wrong leads, poor buy-box definition).

## Pitfalls

1. **Skipping the frame script and diving into questions.** The frame script (introduce yourself, explain the three-phase process, position as investor not broker, set the agenda) is not optional. It builds trust and sets expectations. If you skip it and start interrogating the seller, they will get defensive and withhold information. Always spend the first 3 to 5 minutes on framing.

2. **Asking for financials too early or too aggressively.** Do not open the call with "send me your tax returns." Build rapport first. Ask about their story, their motivation, their vision for the business. After 20 to 30 minutes, when trust is established, mention that the next step is a thorough financial review and you will need three years of statements. Frame it as part of the process, not an interrogation.

3. **Not listening for motivation.** The most important question is "why are you selling, and why now?" The answer reveals whether the seller is serious (retiring, burned out, health issue, other opportunity) or just testing the market (curious about valuation, no urgency). If the seller has no clear motivation, the deal will drag and likely die. Note the motivation and tailor your approach accordingly.

4. **Ignoring red flags because you like the business.** If the seller reveals customer concentration above 30 percent, declining revenue, or unresolved liabilities, do not rationalize it away. These are objective red flags. You can renegotiate price to account for risk, but you cannot eliminate the risk. If multiple red flags appear, walk away. There are other deals.

5. **Not setting clear next steps.** At the end of the call, you must have a commitment from the seller (send financials by [date], schedule follow-up call, sign NDA). If the call ends with "I'll think about it and get back to you," the deal is dead. Create urgency by mentioning scarcity ("we vet only six percent of deals to the next phase") and giving a deadline.

## Output

From the simulator, you receive a scored performance review with specific feedback on rapport, information extraction, and next-step clarity. Use this feedback to improve your live calls. From the live-call question guide, you receive a prioritized list of 15 to 20 questions organized by section. From the call debrief, you receive a summary of key facts, a rough valuation range, a red flag list, and a proceed/renegotiate/walk recommendation. These outputs feed directly into the valuation skill (if green) or your exit decision (if red).
