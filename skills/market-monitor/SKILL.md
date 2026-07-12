---
name: market-monitor
description: Use when running a weekly scan of on-market listings (BizBuySell, broker sites) inside your buy box. Provides asking-price comps for valuation anchoring and flags new deals worth evaluating.
version: 1.0.0
---

# Market Monitor

## Overview

Run a weekly web search scan of on-market business listings across BizBuySell, BizQuest, and local broker sites. You will filter results by your buy box criteria (geography, revenue, vertical), track asking prices as valuation comps, and flag new listings that deserve an AQ Score. This is not your primary sourcing channel (off-market and broker relationships are better), but it is the safety net that catches good deals you might otherwise miss and gives you real market pricing data to anchor negotiations.

## When to Use

- You need current asking-price comps for businesses in your target verticals to anchor valuation
- You want to see what is actively listed in your geography and verticals without manually checking 5 broker sites
- You are negotiating a deal and need to know what similar businesses are listed for
- You want a weekly discipline to stay aware of market activity and spot new opportunities

## Steps

1. **Set a recurring Monday morning calendar reminder.** Call it "Weekly Market Monitor" and block 30 minutes. Consistency matters. If you skip 3 weeks, you lose pricing trend awareness and miss time-sensitive opportunities.

2. **Open Claude and start a chat in your Acquisition Engine Project.** Confirm your buy box is uploaded to Project Knowledge. If not, paste your criteria: your geography, revenue range, SDE floor, and verticals (e.g., Orange County CA, $1-5M, $200K+, hood cleaning / laundromats / pool service).

3. **Ask Claude to web search for new listings in your top 3 verticals.** Use this prompt pattern: "Web search BizBuySell, BizQuest, and [my state] business broker sites for listings in these verticals: [my top 3 verticals]. Filter to [my geography]. Revenue [my range] preferred. Return a table: business name (or description if name not disclosed), city, revenue, asking price, SDE if disclosed, days listed, source with a link. Limit to listings posted in the last 30 days."

   **Evidence rule — listings must be real.** Listing marketplaces often block automated crawlers, so web search may return summaries, stale results, or nothing — and a model asked for a table it cannot fill is at risk of inventing plausible-looking listings. Accept a listing into your scan ONLY if it comes with a source link you can open and verify. If the search comes back thin, do the reliable version: open BizBuySell/BizQuest yourself, run your saved search, and paste the listing text (or screenshots) into the chat — then have Claude build the table, screen, and multiples from what you pasted. Never negotiate or anchor off a listing you have not seen with your own eyes.

4. **Screen the results against your buy box.** Ask Claude: "From the table above, flag listings that match my buy box: $1-5M revenue, $200K+ SDE, 10+ years in business, Orange County location. Mark pass/fail for each and note the reason if fail (e.g., revenue too low, wrong geography, franchise)."

5. **Calculate asking multiples for comps.** For listings that disclose both asking price and SDE, divide asking price by SDE to get the multiple. Prompt: "For listings where SDE is disclosed, calculate the asking multiple (asking price / SDE). Add a column to the table. What is the average asking multiple for businesses in each vertical? Are any listings priced significantly below or above the average?"

6. **Flag listings worth deeper evaluation.** Prompt: "Which 2-3 listings from the filtered table are worth running an AQ Score on? Prioritize: asking multiple under 3.0x SDE, days listed over 90 (motivated seller), seller financing mentioned, or real estate included. Return the top 3 with a 1-sentence reason for each."

7. **Save the scan results.** Download as markdown and save as `market-monitor-YYYY-MM-DD.md` in a folder like `acquisitions/market-scans/`. Track the file weekly. After 4-8 weeks, you will have a pricing trend dataset. If asking multiples are rising, the market is heating up. If days-listed averages are increasing, sellers are getting more realistic.

8. **Run AQ Scores on the top 2-3 flagged listings.** Use the aq-analyzer skill. If a listing passes the AQ Score, reach out to the broker or seller the same day. On-market deals move fast. A listing that has been up for 120 days and just dropped the asking price will get multiple offers within a week of the price cut.

## The Prompts

```
Prompt 1: Weekly web search for new on-market listings

You are a market intelligence analyst. I need a weekly scan of on-market business listings in my target verticals and geography. Web search BizBuySell, BizQuest, and Southern California business broker sites for listings in: kitchen hood cleaning, pool service, laundromats, car washes, landscape maintenance. Filter to Orange County and San Diego. Revenue $1-5M preferred. Return a table: business name or description, city, asking price, revenue, SDE (if disclosed), days listed, listing source. Focus on listings posted or updated in the last 30 days.
```

```
Prompt 2: Calculate asking multiples and identify outliers

You are a valuation analyst. From the table above, calculate the asking multiple (asking price divided by SDE) for every listing where SDE is disclosed. Add this as a new column. Then calculate the average asking multiple per vertical. Flag any listings priced 20%+ below the vertical average (potential deals) or 50%+ above (overpriced, likely to sit). Return the updated table sorted by asking multiple ascending.
```

```
Prompt 3: Flag top 3 listings for AQ Score evaluation

You are a deal prioritization expert. From the filtered listings that passed my buy box, which 3 are most worth running an AQ Score on this week? Prioritize: (1) asking multiple under 3.0x SDE, (2) days listed over 90 (seller motivation signal), (3) seller financing mentioned in the listing, (4) real estate owned and included in sale. Return the top 3 with business name, asking price, and a 1-sentence reason why it is worth evaluating.
```

## The Loop

Run this every Monday. After 4 weeks, review your saved scans and look for patterns. Are certain verticals getting more expensive? Are listings sitting longer (days listed increasing)? Is seller financing becoming more common or less? Use this data to adjust your buy box or shift focus to a different vertical. If you see the same listing appear in 4 consecutive scans with no price drop, that seller is not motivated. If a listing drops the asking price by 20% between week 2 and week 3, call the broker immediately. Market monitor is not just deal sourcing. It is competitive intelligence and pricing education.

## Pitfalls

- **Treating on-market as your primary sourcing channel.** On-market listings are already being shopped to every buyer with a checkbook. You are competing at full asking price with 10 other buyers. Off-market (deal-finder skill) and pre-market broker relationships (broker-finder skill) are where you find the real edge. Market monitor is the backup, not the main hunt.
- **Getting distracted by listings outside your buy box.** If you see a cool restaurant in Los Angeles for $8M and it is outside your geography and revenue range, do not spend 2 hours researching it. Stick to the filter. The buy box exists to keep you disciplined.
- **Not saving the weekly scans.** If you run this in Claude every Monday but never download the results, you have no pricing trend data and no record of which deals you already evaluated. Save every scan as a dated markdown file.
- **Skipping weeks.** If you run market monitor once a month instead of weekly, you will miss price drops and new listings. A motivated seller who drops the price and adds seller financing will get an offer within days. If you only check monthly, you are too late.
- **Not running AQ Scores on flagged listings.** The market monitor finds the deals. The AQ Score qualifies them. If you flag 3 good listings every week but never run the AQ Score, you are doing market research, not deal sourcing. Follow through.

## Output

A weekly markdown file with a table of on-market listings filtered by your buy box, asking multiples calculated, and 2-3 flagged listings worth deeper evaluation. Save as `market-monitor-YYYY-MM-DD.md` in your acquisitions folder. After 4-8 weeks, you will have a pricing trend dataset and a library of comps to use in negotiations. For flagged listings, follow up with the aq-analyzer skill the same day.
