---
name: deal-finder
description: Use when sourcing off-market acquisition targets. Combines Claude web search with user-pasted Google Maps data to find operating businesses, flag succession signals, screen against buy box, and pre-score 6 of 13 AQ criteria.
version: 1.0.0
---

# Deal Finder

## Overview

Find off-market acquisition targets that have not listed with a broker. You will use Claude web search to identify businesses in a vertical and city, paste Google Maps results to enrich the list, then flag no-website, long-tenure, and succession-age signals. The skill screens candidates against your buy box, ranks them by succession likelihood, and pre-scores 6 of the 13 AQ criteria (location, broker, history, own property, staff, inventory) before you make first contact. This is the volume sourcing engine that feeds your pipeline.

## When to Use

- You need 20-50 off-market leads in a specific vertical and geography
- You want to find boomer-owned, owner-dependent businesses before they list with a broker
- You are tired of competing with other buyers on BizBuySell at full asking price
- You need to build a cold-outreach list for email, LinkedIn, or direct mail campaigns

## Steps

1. **Pick one vertical and one city from your buy box.** Example: kitchen hood cleaning in Orange County, or pool service in Irvine. Do not try to search multiple verticals at once. One vertical, one city, one run.

2. **Ask Claude to web search for businesses in that vertical and city.** Use this pattern: "Web search for kitchen hood cleaning companies in Irvine California. Return a list of 20+ businesses with name, address, phone, and website if available." Claude will search Google and return a structured list. If it only finds 5-10, expand the city to the full county or add adjacent cities.

3. **Open Google Maps and search the same query.** Type "kitchen hood cleaning near Irvine CA" into Google Maps. Scroll through the results and copy the top 30-50 business names, addresses, and phone numbers into a text file or spreadsheet. Google Maps often shows businesses that do not rank in web search, especially older owner-operated ones with no SEO.

4. **Paste the Google Maps list into the Claude chat.** Tell Claude: "Here is a list of 40 businesses from Google Maps. Cross-reference with your web search results. For each business, flag: (1) has website yes/no, (2) website looks modern/dated/none, (3) Google review count and recency, (4) estimated years in business from reviews or web search. Return a table."

5. **Ask Claude to identify succession signals.** Prompt: "From the table above, flag businesses with these signals: no website OR dated website, 10+ years in business, 20+ Google reviews but no online booking. These are likely boomer-owned, owner-dependent, and un-modernized. Rank them by succession likelihood (combination of age, no website, high review count). Return the top 15."

6. **Screen the top 15 against your buy box.** If your buy box requires $1-5M revenue, use review count and employee estimates as a proxy. A business with 200+ reviews and 10-20 employees is likely in the $1-5M range. A business with 10 reviews and 2 employees is under $500K. Ask Claude: "Estimate revenue for each of the top 15 based on review count, years in business, and industry benchmarks. Flag which ones likely fall in the $1-5M revenue range."

7. **Pre-score 6 AQ criteria for the screened list.** You can fill these before the first call: location (does it match your geography?), broker (no, it is off-market), history (10+ years = green, under 5 = red), own property (YOU check county assessor records or Google Street View for a standalone building — Claude cannot view Street View, so feed it what you see), staff (LinkedIn or website team page), inventory (hood cleaning has trucks/equipment, pool service has vans). Ask Claude: "For the businesses that passed revenue screening, pre-score these 6 AQ criteria: location, broker, history, own property, staff, inventory. Use green/yellow/red. Return a table with business name and 6 ratings."

8. **Rank by composite succession likelihood and AQ pre-score.** The best targets have: no website (or dated), 15+ years in business, standalone building (property ownership signal), 5-15 employees (big enough to have revenue, small enough to be owner-dependent), and green ratings on location/history/staff. Ask Claude to rank the final list and export as markdown.

9. **Save the results.** Download the markdown file as `deal-finder-<vertical>-<city>-YYYY-MM-DD.md` and store it in a folder like `acquisitions/targets/<vertical>/`. This becomes your outreach list for email, LinkedIn, or cold calling.

## The Prompts

```
Prompt 1: Web search for businesses in vertical and city

You are a deal sourcing analyst. I need to find [my vertical, e.g. kitchen hood cleaning] companies in [my geography, e.g. Orange County California] that are potential acquisition targets. Web search for businesses in this vertical and geography. Return a list of 30+ businesses with: name, city, phone, website (if available), years in business (estimate from web results or reviews, and say which). Only list businesses you actually found in retrieved pages — never invent a business, phone number, or review count; if the search runs thin, say so and I will paste Google Maps results instead. Format as a markdown table with a source per row.
```

```
Prompt 2: Cross-reference Google Maps paste and flag succession signals

You are a deal analyst. I pasted a list of 40 businesses from Google Maps below. Cross-reference with your web search results. For each business, add these columns: has website (yes/no), website quality (modern/dated/none), Google review count, estimated years in business. Then flag businesses with these succession signals: no website OR dated website, 10+ years in business, 15+ reviews but no online booking. Return the flagged list ranked by succession likelihood (older + no website + high reviews = top rank).

[paste Google Maps list here]
```

```
Prompt 3: Pre-score 6 AQ criteria for top candidates

You are a deal qualification expert. From the ranked succession list above, take the top 10 businesses that likely fall in my revenue range (estimate from review count + years in business + employee signals — label these as proxies, not verified revenue). Pre-score these 6 AQ criteria using green/yellow/red: (1) location - inside [my geography] = green, outside = red; (2) broker - off-market = green; (3) history - 10+ years = green, 5-10 = yellow, under 5 = red; (4) own property - I will check Google Street View / the county assessor myself and tell you: standalone building = green, strip mall = yellow, unknown = yellow (you cannot view Street View — ask me for anything you need eyes on); (5) staff - 5+ employees on LinkedIn or website = green, under 5 = yellow; (6) inventory - service business with trucks/vans = green, no equipment = yellow. Return a table: business name, 6 AQ ratings, composite likelihood score. Rank by score descending.
```

## The Loop

Run this skill once per vertical per geography to build an initial pipeline of 30-50 leads. After you make first contact with the top 10, return to the list and work down to candidates 11-20. Every 2-3 months, re-run the search in the same vertical and city. New businesses age into the succession window, and owner circumstances change. A business that was not ready to sell 6 months ago may be ready now. Update your target files and track which businesses moved from contacted to conversation to qualified.

## Pitfalls

- **Searching too many verticals at once.** If you ask Claude to find "service businesses in Orange County," you will get a mess of carpet cleaners, HVAC, plumbers, and locksmiths with no depth in any vertical. Pick one vertical per run.
- **Trusting web search alone without Google Maps paste.** Older businesses often have no website or bad SEO, so they do not show in web search results. Google Maps finds them because they have a physical location and reviews. Always cross-reference both sources.
- **Assuming no website means the business is failing.** No website usually means older owner, not failing business. These are often profitable, long-tenured operations that never needed digital marketing because they run on referrals and word-of-mouth. This is exactly the acquisition sweet spot.
- **Not saving the results outside Claude.** If you run this search and do not download the markdown file, you will lose the list when the chat scrolls out of view. Always save as a file and store it in your acquisitions folder.
- **Skipping the AQ pre-score step.** If you go straight from deal-finder to cold outreach without pre-scoring, you will waste calls on businesses that fail obvious criteria like location or broker-listed. The 6 pre-scoreable criteria cut your outreach list by 30-50% and focus your time on real targets.

## Output

A ranked markdown file with 10-15 off-market businesses, each pre-scored on 6 of 13 AQ criteria, sorted by succession likelihood. The file includes: business name, address, phone, website status, years in business, estimated revenue range, 6 AQ ratings (green/yellow/red), and composite likelihood score. Save as `deal-finder-<vertical>-<city>-YYYY-MM-DD.md` in your acquisitions folder. This list feeds your outreach campaigns and discovery calls.
