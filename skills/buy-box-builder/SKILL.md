---
name: buy-box-builder
description: Use when building acquisition criteria across 3 lanes (conservative/target/aggressive) and scoring verticals by recurring revenue, fragmentation, boomer ownership, AI-modernization upside, and entry multiple.
version: 1.0.0
---

# Buy Box Builder

## Overview

Build a disciplined acquisition filter that defines exactly what you buy and what you pass. You will create criteria across three lanes (conservative, target, aggressive) to avoid mission creep, then score 8-10 verticals on five factors: recurring revenue, market fragmentation, boomer ownership, AI-modernization upside, and entry multiple. The output is a ranked vertical list and a buy box document that feeds every other skill in this pack.

## When to Use

- You are starting acquisition work and need to define what you are looking for
- You have a vague idea ("I want to buy a small business") but no specific filter
- You are spreading your search too wide and getting distracted by deals outside your zone
- You want to stress-test your criteria against 10 real businesses before committing time to sourcing

## Steps

**Step 0 — Anchor on the number you need (do this first).** Start from the annual income (SDE) you need this business to pay you, plus your 5-year net-worth goal. Given typical owner margins in your candidate verticals, reverse-engineer the revenue range that produces that SDE and set your SDE floor from it. This is the EPIC move — the buy box is built *backward from your required number*, not forward from a listing you liked. (Need $300K SDE but the vertical pays owners ~$150K? You are hunting $3M+ revenue, not $1M — or a higher-margin vertical.) **And if you are financing the purchase, debt service comes out of SDE before you get paid:** on a typical SBA 7(a) structure, annual loan payments can absorb roughly a third of SDE, so set the SDE floor at your income need *plus* expected debt service (e.g., needing $250K income on a leveraged deal usually means a ~$400K SDE floor, not $250K). Have your lender confirm the actual payment. Also capture the industries you are drawn to or have an edge in; they feed your interest multiplier in Step 3 and your auto-pass list in Step 4.

> **Real-estate verticals price differently.** For asset-based verticals (self-storage, car washes, laundromats, RV/boat storage, mobile-home parks), read the "entry multiple" factor as **cap rate / NOI**, not SDE multiple — you are buying real estate with an operating overlay, financed via SBA-504 or real-estate debt, not a $0-down seller note. These are **1031-eligible** (see the 1031 dual-track in Step 6): if you are deploying 1031 equity, size the deal off your equity and the cap rate, and anchor on cash-on-cash return rather than an SDE floor.

1. **Define your three lanes.** Conservative is the safe deal you would take today. Target is the ideal fit. Aggressive is the stretch deal that requires more work or risk but has big upside. Write these in a table with 8 rows: geography, revenue, SDE, employees, business age, owner profile, financing, and vertical focus. Example: Conservative might be Orange County only, $1-2M revenue, $200-300K SDE, existing manager on staff. Aggressive might expand to San Diego, $3-5M revenue, owner-dependent but strong brand.

2. **Score 8-10 verticals on the five factors.** Use a 1-5 scale for each factor. Recurring revenue: does the business have contracted or repeat customers (5) or one-off projects (1)? Fragmentation: are there 500+ small operators in your geography (5) or 10 dominant chains (1)? Boomer ownership: is the average owner 60+ and ready to retire (5) or 35 and growing (1)? AI-modernization upside: can you automate scheduling, invoicing, lead management, and reporting (5) or is it high-touch professional services (2)? Entry multiple: do businesses sell at 2.0-2.5x SDE (5) or 4.0x+ (1)?

3. **Calculate a composite score for each vertical.** Add the five factors, then multiply by your personal interest or capability (1-3x multiplier). If you have zero interest in laundromats, multiply by 1. If you already know the pool service industry, multiply by 3. Rank the verticals from highest to lowest composite score.

4. **Write the buy box document.** Use the template: geography, revenue range, SDE floor, employee count, business age, owner profile, financing structure, top 3 verticals (from your scoring), and 3 automatic pass criteria (things you will never touch, like home-based businesses, franchises, or single-customer dependence). Keep it to 1 page.

5. **Stress-test the buy box against 10 real businesses.** Go to BizBuySell, search your top vertical + geography, and pull 10 active listings. Run each through your buy box. How many pass? If zero pass, your criteria are too narrow. If all 10 pass, your criteria are too loose. Adjust revenue, SDE, or geography until 3-5 of the 10 pass. This confirms your box is realistic.

6. **Add the dual-path note if using a 1031 exchange.** If you have 1031 equity to deploy, split your buy box into two tracks: real-estate-based businesses (car wash, laundromat, tree farm, recycling plant, storage facility) for the 1031 equity, and operating businesses (hood cleaning, water purification, landscape, pool, insurance brokers) for SBA 7(a) + seller note. The 1031 track is on a hard 45-day identification / 180-day close clock. Operating businesses run continuously with no deadline. (1031 exchanges are tax law with hard edges — engage a Qualified Intermediary and CPA before the clock starts; nothing in this skill is tax advice.)

7. **Save the buy box as markdown.** File it as `buy-box.md` and upload it to your Claude Acquisition Engine Project (see claude-acquisition-setup skill). This file becomes the filter for every deal-finder, market-monitor, and AQ-analyzer run.

## The Prompts

```
Prompt 1: Build the three-lane criteria table

You are a business acquisition strategist. I need to define my buy box across three lanes: conservative (safe, take today), target (ideal fit), aggressive (stretch, higher risk/reward). Create a table with 8 rows: geography, revenue, SDE, employees, business age, owner profile, financing, vertical focus. For each row, write conservative, target, and aggressive criteria. Use these starting points: geography starts [my home market, e.g. Orange County only] and expands to [adjacent market, e.g. Orange County + San Diego]; revenue starts [$1-2M] and expands to [$3-5M]; SDE starts [$200-300K, anchored on the income I need — see Step 0] and expands to [$300K-1M]; business age is always 10+ years. Return the table in markdown.
```

```
Prompt 2: Score 10 verticals on the five factors

You are a vertical analysis expert. I am evaluating these verticals for acquisition focus: [list YOUR 8-10 candidate verticals — e.g., kitchen hood cleaning, home water purification (service/rental model), laundromats (own building), landscape maintenance, pool service, car wash (real estate based), aquarium maintenance, insurance brokers, tree farms, recycling plants — swap in the industries from your own Step 0 list]. Score each vertical 1-5 on: (1) recurring revenue clarity, (2) market fragmentation (more small operators = higher score), (3) boomer ownership prevalence, (4) AI-modernization upside, (5) low entry multiple (2.0-2.5x SDE = 5, 4.0x+ = 1). Return a table: vertical, 5 factor scores, total. Rank by total descending.
```

```
Prompt 3: Stress-test the buy box against 10 real listings

You are a deal analyst. I need to validate my buy box against real market data. Web search BizBuySell for "[my geography] [my top vertical] for sale" (e.g., "Orange County pool service for sale"). Pull 10 active listings with revenue, asking price, and SDE if disclosed — every listing must come from a real page with a link I can open; if search cannot retrieve live listings, tell me and I will open BizBuySell myself and paste the listing details here instead. Never invent a listing. Run each through my buy box criteria: [my revenue range], [my SDE floor], [my age minimum], [my owner profile], located in [my geography]. Return a table: business name, revenue, SDE, age, pass/fail, reason if fail. How many of 10 passed? If under 3, suggest which criterion to loosen.
```

## The Loop

After you build the initial buy box, run the stress-test every 2-3 weeks as you learn more about the market. If you find that your top vertical has no available deals, re-run the vertical scoring and pick number 2 or 3. If you keep seeing deals at 4.0x SDE but your box assumes 2.5x, adjust your expectations or pick a different vertical. The buy box is not static. It evolves as you gather real pricing data and talk to sellers. Update `buy-box.md` and re-upload to Claude Project Knowledge every time you make a change.

## Pitfalls

- **Building criteria around one cool deal you saw.** Do not reverse-engineer your buy box from a single listing. Score verticals objectively first, then filter deals.
- **Ignoring the stress-test step.** If you skip step 5, you will waste weeks chasing deals that do not exist at your price range or in your geography. The stress-test catches impossible boxes before you start outreach.
- **Setting SDE floors based on what you need to live, not what the market pays.** If you need $300K to replace your W2 but the market pays owners $150K SDE in your target vertical, you are looking at $3M+ revenue businesses, not $1M. Adjust revenue range or pick a higher-margin vertical.
- **Forgetting the 70% Rule.** Roland Frasier's rule: you should be able to kill 70% of bad deals in the first call. If your buy box is so loose that everything sounds interesting, you will waste time on discovery calls that go nowhere. Tighten the criteria until 7 of 10 listings are obvious passes.
- **Not separating 1031 real estate track from operating business track.** If you have 1031 equity, you cannot use it to buy an operating business without real estate. The like-kind rule forces the equity into land and building only. Track these separately or you will miss the 45-day identification window chasing the wrong deals.

## Output

A ranked vertical list with composite scores, a 1-page buy box document covering geography/revenue/SDE/age/owner profile/financing/top 3 verticals/3 auto-pass criteria, and a stress-test table showing how many of 10 real listings passed your filter. Save the buy box as `buy-box.md` and upload it to Claude Project Knowledge. This file feeds every deal analysis and sourcing run from here forward.
