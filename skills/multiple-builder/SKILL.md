---
name: multiple-builder
description: Use when tracking your journey from 2.4x owner-operated SDE toward 4.0x professionally-managed EBITDA. Claude re-scores owner-dependency, management depth, documented processes, recurring revenue, and clean financials quarterly, then shows you the dollar value of each improvement.
version: 1.0.0
---

# Multiple Builder

## Overview

The cheapest acquisition deal you will ever do is the one you do on the business you already own. Moving a business from owner-operated (2.4x SDE) to professionally managed (4.0x EBITDA) often creates more value than buying a competitor. This skill tracks that transformation. Every quarter, you re-score five dimensions: owner-dependency (how many critical tasks still require you), management depth (can the business run for 2 weeks without you), documented processes (how many SOPs exist and are followed), recurring revenue percentage (predictable monthly cash flow), and clean financials (accurate books, separated personal and business expenses, auditable). Claude shows you how the business scores today, how it scored last quarter, and the dollar value of each improvement. Example: documenting 15 SOPs and hiring a manager who runs operations on Tuesdays moves you from 2.4x to 3.2x. On a business with $400K SDE, that is a $320K increase in enterprise value. This skill quantifies the return on modernization.

## When to Use

Run multiple-builder after you complete your first owner-dependency-audit and have implemented at least one improvement (documented SOPs, hired help, automated a process, or lifted margin). You need a baseline score to track progress against. Do not run this skill in your first week of ownership or before you have taken any modernization action. The value is in the quarterly comparison, not the initial snapshot. Re-run this skill every 90 days (tie it to quarterly financial close). If you plan to sell the business in 2 to 3 years, this skill shows you which improvements have the highest ROI in terms of multiple expansion.

## Steps

1. **Run the baseline assessment with Prompt 1.** Claude scores you on the five dimensions using a 1 to 10 scale: (1) Owner-dependency: How many critical tasks require you daily? 10 = business runs without you, 1 = nothing happens without you. (2) Management depth: Can the business operate for 2+ weeks if you are unavailable? 10 = fully managed team, 1 = solo owner. (3) Documented processes: How many SOPs exist and are actively used? 10 = all core processes documented, 1 = everything in your head. (4) Recurring revenue: What percentage of monthly revenue is predictable (subscriptions, retainers, contracts)? 10 = 80%+ recurring, 1 = all one-off transactional. (5) Clean financials: Are books accurate, separated from personal expenses, and audit-ready? 10 = CPA-reviewed, 1 = shoebox of receipts. Done when you have a score for each dimension and a composite score out of 50.

2. **Map your scores to the multiple ladder.** Claude translates your composite score into an estimated valuation multiple. The ladder: 0 to 15 points = 2.0x to 2.5x SDE (owner-operated, high dependency, no transferability), 16 to 30 points = 2.5x to 3.5x SDE (some documentation, part-time help, messy but improving), 31 to 40 points = 3.5x to 4.5x EBITDA (managed team, documented processes, recurring revenue starting), 41 to 50 points = 4.5x to 5.5x EBITDA (professionally managed, owner optional, clean financials, recurring revenue base). The point bands are this system's own calibration rubric built around Frasier's 2.4x owner-op and 4.0x managed anchors — a tracking tool, not a Frasier table. Done when you see your estimated multiple range.

3. **Calculate enterprise value at current and target multiples.** Paste your trailing 12-month SDE or EBITDA. Claude calculates: current enterprise value (your score today), target enterprise value (if you hit 40+ points), and the gap in dollars. Example: $400K SDE at 2.4x = $960K. Same business at 4.0x on $400K EBITDA = $1.6M. The gap is $640K of enterprise value you can create without acquiring anything. **One honesty rule in that math:** the upper bands price EBITDA, not SDE — and EBITDA is what remains *after* paying the manager who replaced you. When you project the target value, subtract a market-rate manager salary from your SDE first (e.g., $400K SDE − $80K manager = $320K EBITDA × 4.0 = $1.28M). The lift is still large; just never apply an EBITDA multiple to an SDE number. Done when you see the dollar opportunity.

4. **Identify the highest-ROI improvements with Prompt 2.** Claude ranks which dimension improvements give you the most multiple lift per unit of effort. Example: moving from 3 SOPs to 15 SOPs (documented processes score 3 to 7) is easier than building 50 percent recurring revenue from zero (recurring revenue score 1 to 5). The ranking shows you where to focus next quarter. Done when you have a prioritized improvement list.

5. **Set 90-day improvement goals.** Pick 2 to 3 dimensions to improve in the next quarter. Example goals: increase documented processes from 5 to 15 SOPs (score 4 to 6), reduce owner-dependency from daily involvement to 3 days per week (score 3 to 5), hire a part-time manager to handle scheduling and customer service (management depth score 2 to 4). Done when you have specific, measurable goals tied to the five dimensions.

6. **Execute the improvements and track progress.** Work the goals for 90 days using the other Scalable with AI skills (sop-extractor for documentation, margin-finder for financials, customer-engine for recurring revenue systems). At day 90, re-run the assessment with Prompt 1. Compare your new scores to baseline. Done when you have quarter-over-quarter data showing improvement.

7. **Repeat quarterly and track the value creation.** After 4 quarters (1 year), you should see measurable multiple expansion. A business that started at 2.4x and reached 3.5x in 12 months created hundreds of thousands of dollars in enterprise value. After 8 quarters (2 years), a business that hits 4.0x to 4.5x is ready to sell at a premium or operate as a cash-flowing asset while you acquire the next one.

## The Prompts

**Prompt 1: The Quarterly Multiple Assessment**

```
I want to assess my business on the five dimensions that drive valuation multiples. Score me on a 1 to 10 scale for each dimension based on my answers. Ask ONE question at a time:

**Dimension 1: Owner-Dependency**
- How many hours per week do you work in the business (not on strategy, just operations)?
- How many critical tasks require you personally (pricing, sales, quality control, vendor relations, scheduling)?
- What happens if you are unavailable for a week? (Does revenue stop, quality drop, team unable to function, or business runs fine?)

**Dimension 2: Management Depth**
- Do you have a manager, lead tech, or supervisor who can run daily operations without you?
- Can the business operate for 2+ weeks if you are on vacation or sick?
- How often does the team call you with questions they cannot answer themselves?

**Dimension 3: Documented Processes**
- How many written SOPs or process documents do you have?
- Are they actively used by the team (on clipboards, in shared docs, referenced daily), or are they filed and forgotten?
- What percentage of your core operations are documented (sales, service delivery, customer onboarding, financials)?

**Dimension 4: Recurring Revenue**
- What percentage of your monthly revenue is predictable (subscriptions, retainers, service contracts, repeat customers on auto-renew)?
- How much of your revenue is one-off transactional (you have to sell it fresh every month)?
- Do you have a backlog of committed work (jobs booked 30+ days out)?

**Dimension 5: Clean Financials**
- Are your books accurate and up-to-date (reconciled monthly, categorized expenses, no personal expenses mixed in)?
- Do you have a CPA or bookkeeper reviewing your financials, or do you do it yourself in QuickBooks?
- If a buyer asked to see your P&L and balance sheet tomorrow, could you hand it over with confidence?

After I answer all questions, give me a score (1-10) for each dimension, a composite score out of 50, and map me to the multiple ladder:
- 0-15 points = 2.0-2.5x SDE (owner-operated, high risk)
- 16-30 points = 2.5-3.5x SDE (improving, but still owner-dependent)
- 31-40 points = 3.5-4.5x EBITDA (managed, documented, some recurring revenue)
- 41-50 points = 4.5-5.5x EBITDA (professionally managed, transferable, low owner dependency)
```

**Prompt 2: Identify Highest-ROI Improvements**

```
Here are my scores from the quarterly assessment:
- Owner-dependency: [score/10]
- Management depth: [score/10]
- Documented processes: [score/10]
- Recurring revenue: [score/10]
- Clean financials: [score/10]
- Composite: [score/50]

My trailing 12-month SDE or EBITDA is: $[amount].

Analyze which dimension improvements will give me the most multiple lift per unit of effort. Consider:
1. Which scores are lowest (biggest gaps)?
2. Which improvements are fastest to implement (documented processes and clean financials are easier than building recurring revenue from zero)?
3. Which improvements unlock others (e.g., documenting processes enables hiring a manager, which reduces owner-dependency)?

Rank the five dimensions by ROI (return on effort). For each, suggest one concrete 90-day improvement goal that would lift the score by 2-3 points. Also calculate: if I improve my composite score from [current] to [current + 10 points], what is the estimated increase in enterprise value at the higher multiple?
```

**Prompt 3: Track the Journey (Run After Each Quarter)**

```
I last ran the multiple-builder assessment on [date]. Here were my scores:
[paste previous quarter scores]

I have completed these improvements in the last 90 days:
[list what you did: SOPs documented, help hired, processes automated, margin lifted, financials cleaned up, recurring revenue systems launched]

Re-score me on the five dimensions using the same questions from Prompt 1. After scoring, show me:
1. Score comparison: old vs new for each dimension
2. Composite score change (points gained)
3. Estimated multiple change (old range vs new range)
4. Enterprise value increase in dollars (at my current SDE/EBITDA)
5. What I should focus on next quarter (the dimension with the biggest remaining gap and highest ROI)

Format as a quarterly progress report I can save and track over time.
```

## The Loop

Assess quarterly (every 90 days). After each assessment, pick 2 to 3 improvement goals tied to the five dimensions. Execute the goals using the other Scalable with AI skills. Re-assess at the end of the quarter and track progress. Over 4 to 8 quarters, you should see the composite score rise from the teens or twenties into the thirties or forties. Each 10-point increase in composite score typically lifts the multiple by 0.5x to 1.0x. On a $400K EBITDA business, moving from 2.5x to 4.0x creates $600K in enterprise value. That value is real. It shows up when you sell, when you raise capital, or when you borrow against the business. The multiple-builder skill quantifies the return on modernization so you know where to invest time and effort.

## Pitfalls

1. **Scoring yourself too generously.** If you say you have 20 SOPs but 15 of them are filed and never used, your real score is 5, not 20. Be honest. The value of this skill is in tracking real improvement, not inflating the score to feel good.

2. **Improving the wrong dimensions.** If your business has clean financials (score 9) but zero documented processes (score 2) and total owner-dependency (score 2), do not spend the quarter optimizing your bookkeeping further. Focus on the low scores. The multiple is limited by the weakest dimension, not the strongest.

3. **Skipping quarters.** If you assess once and never re-run it, you have no idea if your efforts are working. The power is in the trend line. Four quarters of steady improvement (composite score 18, then 24, then 31, then 38) proves you are on track. One snapshot proves nothing.

4. **Not tying improvements to dollar value.** If you document 10 SOPs and never calculate the enterprise value lift, the work feels like a chore instead of an investment. Always run the math: X improvement = Y point increase = Z multiple lift = $ABC,000 more enterprise value. When you see the dollars, the motivation is clear.

5. **Waiting to sell before modernizing.** The best time to professionalize the business is 2 to 3 years before you plan to sell, not 2 months before. Buyers can tell when you cleaned up the books last minute. They discount for it. If you modernize early and run the business at 4.0x for 18 months, the valuation holds. If you modernize in month 23 of a 24-month sales process, buyers will assume the improvements are cosmetic.

## Output

You receive a quarterly scorecard showing your scores (1-10) on the five dimensions (owner-dependency, management depth, documented processes, recurring revenue, clean financials), a composite score out of 50, an estimated valuation multiple range (2.0x to 5.5x), and calculated enterprise value at current and target multiples. After each quarter, you also receive a progress report comparing this quarter to last quarter, showing points gained, multiple lift, and dollar value created. Over time, you build a trend line that proves the business is professionalizing. When your composite score reaches 35 to 40 points, the business is worth 3.5x to 4.5x EBITDA and can sell to a strategic buyer or private equity. At that point, you have created hundreds of thousands of dollars in enterprise value without acquiring anything. The multiple-builder skill shows you the ROI of modernization in the same language you use to evaluate acquisition deals: cash-on-cash return, multiple expansion, and enterprise value lift.
