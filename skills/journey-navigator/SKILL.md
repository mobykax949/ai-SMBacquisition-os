---
name: journey-navigator
description: Use when starting with the playbook, or whenever your situation changes, to build your acquirer profile and get the strategy that fits where you actually are in the journey. Run this BEFORE the buy-box builder.
version: 1.0.0
---

# The Journey Navigator

## Overview

Not every buyer should run the same play. An owner modernizing their existing business hunts differently than a first-time searcher, and a searcher chasing a platform company runs a different strategy than one collecting bolt-ons or marketing assets. This skill interviews you, writes your acquirer profile, diagnoses where you are in the journey, and recommends the strategy and skill path that fits — before you build a buy box aimed at the wrong target.

## When to Use

- Your first session with the playbook (run this before anything else)
- Your situation changed: you closed a deal, sold something, raised capital, or moved
- You feel pulled between strategies and need the trade-offs named
- You own a business and can't decide whether to modernize, bolt on, or hunt a platform

## The Journey Stages

The interview places you in one of five stages. Each has a different best move.

| Stage | You are | The play | Skill path |
|---|---|---|---|
| **1. Owner-Operator** | You own a business; it depends on you | Modernize FIRST. Lift margin, remove yourself, raise the multiple before buying anything | Scalable-with-AI track → modernization-audit, then return here |
| **2. Owner-Acquirer** | You own a business that runs; you want growth | Hunt BOLT-ONS: smaller add-ons in or adjacent to your vertical that your existing operation absorbs | buy-box-builder (bolt-on lane) → deal-finder |
| **3. First-Time Searcher (building)** | No business yet, limited capital or credibility | Start with $0-TRAFFIC ASSETS: buy marketing assets, lists, content properties, or small digital properties that generate leads and cash before a platform buy | buy-box-builder (asset lane) → market-monitor |
| **4. Platform Searcher** | Capital + financing ready (SBA, seller-note capable), hunting the foundation company | Hunt the PLATFORM: the $1-5M cash-flowing business that becomes the base of the roll-up | Full path: buy-box → deal-finder → aq-analyzer → close |
| **5. Roll-Up Operator** | You own the platform; now you consolidate | Bolt-on acquisitions around the Acquisition Wheel: competitors, media, teams, products, supply, IP, recurring revenue | deal-finder per spoke → deal-stacker → integrate |

**Bolt-on vs platform is the distinction most first-time buyers miss.** A platform must stand alone: management capable of running without you, clean financials, fundable. A bolt-on can be smaller, messier, and cheaper, because your existing operation supplies what it lacks. Different screens, different multiples, different risk.

## Steps

1. **Run the interview.** Paste Prompt 1. Claude asks one question at a time; answer honestly. Done when Claude has: ownership status, capital picture, financing readiness, **required income/SDE target**, skills/background, **industries of interest**, geography, hours available, and risk tolerance.

2. **Review your profile.** Claude writes `my-profile.md`. Read it and correct anything wrong. Done when the profile says something true about you in every section.

3. **Get your stage + strategy.** Claude places you in a stage, names the recommended play, AND names the strongest alternative with the trade-off (you should always see the road not taken). Done when you can say in one sentence which play you're running and why.

4. **Save the profile to your Project.** Upload `my-profile.md` to project knowledge. Every other skill reads it — the buy-box builder pre-fills from it, the deal-stacker knows your capital, the Deal Advisor knows your situation. Done when the file is in project knowledge.

5. **Follow your skill path.** The stage table above tells you which skill to open next. Done when your next session starts with the right skill, not the default one.

## The Prompts

**Prompt 1: The Intake Interview**

```
Act as an acquisition strategist running an intake interview. Ask me ONE question at a time, wait for my answer, then ask the next. Cover:

1. Do I currently own a business? (What, revenue, does it run without me?)
2. Capital available to invest, and am I SBA-eligible / financing ready?
3. How much annual income (owner cashflow / SDE) do I need this business to produce — now, and my 5-year net-worth goal? (This sizes the buy box.)
4. My professional background and operating skills
5. Which industries or business types am I drawn to, already understand, or have an edge in — and any I'd never buy?
6. Geography: where I live, how far I'll operate
7. Hours per week I can give this
8. Risk tolerance: steady cash flow vs. bigger swing
9. What I actually want in 5 years: income, an empire, a sellable asset?

Then: write my acquirer profile as a document I can save (my-profile.md), place me in one of these journey stages — Owner-Operator, Owner-Acquirer, First-Time Searcher (building), Platform Searcher, Roll-Up Operator — and recommend my strategy: modernize first, bolt-on hunting, $0-traffic asset building, platform search, or roll-up consolidation. Name the strongest ALTERNATIVE strategy too and the trade-off between them.
```

**Prompt 2: The Strategy Stress-Test**

```
Here is my profile: [paste my-profile.md]. You recommended [strategy]. Argue AGAINST it: what does this path assume about me that might be wrong? What failure mode is most likely for someone in my exact situation? What would have to be true for the alternative ([alternative]) to be the better play? Then give me your final recommendation.
```

**Prompt 3: The Re-Navigation (run after any major change)**

```
My situation changed: [what happened — closed a deal / sold the business / new capital / moved]. Here is my current profile: [paste]. Re-run the stage diagnosis. Has my stage changed? Should my strategy change? Update my-profile.md and tell me what skill to open next.
```

## The Loop

Interview → profile → stage + strategy → stress-test the recommendation (Prompt 2) → save → re-navigate whenever the situation changes (Prompt 3). Your profile is a living file, not a one-time quiz.

## Pitfalls

1. **Skipping straight to the buy box.** A buy box built without a stage diagnosis aims at the wrong target class — the most common expensive mistake is a first-time searcher screening platform companies they can't finance or run.
2. **Owner-operators buying instead of fixing.** If your current business still depends on you daily, a second business doubles the dependency, not the income. Modernize first; the multiple lift on what you own is the cheapest deal you'll ever do.
3. **Confusing bolt-on and platform screens.** A bolt-on can fail the standalone tests (thin management, single-customer risk) and still be a great buy for you. Score it as a bolt-on, not a broken platform.
4. **Answering the interview aspirationally.** State capital you have, not capital you hope to raise. The strategy only fits if the profile is true.
5. **Never re-running it.** Stages change. After every close, sale, or capital event, run Prompt 3 — yesterday's strategy may now be the wrong one.

## Output

`my-profile.md` saved to project knowledge: your acquirer profile, journey stage, chosen strategy with the named alternative, and the skill path to follow. Every other skill in the pack reads this file.
