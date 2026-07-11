---
name: valuation
description: Use when you need to value a target business using SDE or EBITDA, apply the TTM method, audit add-backs, and determine the realistic multiple within the 2.4x to 10.8x landscape.
version: 1.0.0
---

# Valuation

## Overview

The EPIC valuation method for small and mid-size businesses. This skill walks you through the choice between SDE (Seller's Discretionary Earnings) and EBITDA, the trailing-twelve-month profit calculation, the add-back audit (where you subtract the true cost to replace the owner instead of blindly accepting their add-back claims), and the multiple landscape (owner-operated 2.4x SDE, professionalized 4.0x EBITDA, private equity 10.8x EBITDA). The output is a walk-away, realistic, and dream valuation range. You also run a tax-return sanity test to confirm the P&L matches Schedule C or corporate returns.

## When to Use

Run valuation after you have completed discovery and received the seller's financials (three years of profit and loss statements, balance sheet, cash flow statement, and ideally tax returns). You need trailing-twelve-month revenue, cost of goods sold, operating expenses, owner compensation, and the seller's claimed add-backs. If you lack these, return to discovery-interviewer and request the documents. Do not attempt valuation from a teaser or broker summary alone.

## Steps

1. **Choose the profit metric: SDE or EBITDA.** For owner-operated businesses (owner is CEO, works in the business daily, no professional management team), use SDE. For professionally managed businesses (owner is absent or part-time, has a GM or president running operations), use EBITDA. If unsure, default to SDE. Most small businesses are owner-operated.

2. **Compute trailing-twelve-month profit.** Add the most recent 12 months of revenue, subtract COGS, subtract operating expenses, add back owner compensation, add back one-time or non-recurring expenses (if legitimate). This gives you TTM SDE or EBITDA. Do not use the seller's claimed profit without auditing it.

3. **Audit the add-backs.** Sellers inflate profit by claiming excessive add-backs (owner salary, personal expenses, one-time costs). For each add-back, ask: "What is the true cost to replace this function?" If the owner claims a $200K salary as an add-back but you will need to hire a $100K manager to replace them, subtract $100K from the profit. The adjusted profit is your valuation base. This step is critical. Skipping it leads to overpaying by 20 to 40 percent.

4. **Determine the multiple.** Anchor on the EPIC multiple landscape: owner-operated 2.4x SDE, professionally managed 4.0x EBITDA, private equity 10.8x EBITDA, public markets (NASDAQ) 18.7x. The play is to buy at the owner-op/managed multiples and sell toward the PE box. In practice, quality moves small deals in a band around those anchors (owner-op roughly 2.4x-3.5x SDE; managed roughly 4.0x-6.0x EBITDA — working bands this system uses, not Frasier's table). Apply the multiple to your adjusted TTM profit to get enterprise value. Subtract net debt (liabilities minus cash) to get equity value.

5. **Set your three-price framework.** Walk-away price (the maximum you will pay — the high end of the multiple range; above it you walk), realistic price (your target, mid-range multiple), dream price (best-case scenario if the seller is highly motivated — the low end of the range or below). Document all three before entering negotiation. Negotiate toward dream, land at realistic, never cross walk-away.

6. **Run the tax-return sanity test.** If the seller provided tax returns, compare the P&L to Schedule C (sole prop) or Form 1120/1120S (corporation). Revenue and net income should match within 5 percent. If they do not, the P&L is unreliable. Request reconciliation or walk away.

## The Prompts

**Prompt 1: Compute Adjusted TTM Profit and Valuation Range**

```
Value this business using the EPIC method:

Financials (trailing 12 months):
- Revenue: [insert TTM revenue]
- COGS: [insert COGS]
- Operating expenses: [insert total opex]
- Owner compensation: [insert owner W2 or draws]

Seller's claimed add-backs:
- [List each add-back and amount, e.g. "Owner salary $150K", "Personal vehicle $12K", "One-time legal fees $8K"]

Business profile:
- Industry: [insert industry]
- Owner role: [insert owner's daily role: CEO, works in business daily, manages team, etc.]
- Team: [number of employees, key roles]
- Systems: [are procedures documented? Is there a management team?]

Steps:
1. Choose SDE or EBITDA based on owner involvement.
2. Compute TTM profit before add-backs.
3. Audit each add-back: what is the true replacement cost? Subtract replacement cost from profit to get adjusted profit.
4. Apply the multiple landscape: 2.4x-3.5x for owner-op, 4.0x-6.0x for managed, 10.8x+ for PE-grade. Recommend a multiple based on the business quality.
5. Compute enterprise value (adjusted profit × multiple).
6. If net debt is known, subtract it to get equity value.
7. Provide three prices: walk-away (high multiple), realistic (mid multiple), dream (low multiple).
```

**Prompt 2: Tax Return Sanity Test**

```
The seller provided a P&L showing [revenue] and [net profit]. Their Schedule C (or Form 1120) shows [revenue] and [net income]. Are these consistent? Flag any discrepancies larger than 5 percent. If inconsistent, what are the likely explanations (unreported cash income, personal expenses run through the business, timing differences)? Should I request reconciliation or walk away?
```

**Prompt 3: Valuation Sensitivity Analysis**

```
I computed a realistic valuation of [price] at [multiple]x adjusted SDE. Show me how the valuation changes if:
- The multiple drops by 0.5x (market softens or buyer finds new red flags)
- The profit drops by 10% (first-year revenue dip after transition)
- I increase add-backs by $20K (discover additional owner expenses)

For each scenario, recompute enterprise value and my walk-away / realistic / dream prices.
```

## The Loop

Valuation is not a one-time calculation. After the initial valuation, the number will change as you learn more in diligence (discover hidden costs, uncover additional add-backs, find customer concentration risk that depresses the multiple). Rerun the valuation after every major discovery. Track the changes in a spreadsheet. The final valuation (the one that goes into your LOI) should reflect all known facts and risks. If the valuation drops by more than 20 percent from your initial estimate, renegotiate or walk. Do not rationalize your way into overpaying because you fell in love with the business.

## Pitfalls

1. **Accepting the seller's add-backs without audit.** This is the most common and expensive mistake. Sellers routinely claim $150K to $200K in add-backs (owner salary, personal expenses, one-time costs) without justification. If you accept these at face value and apply a 3x multiple, you overpay by $300K to $600K. Always ask: "What does it cost to replace this function?" Subtract the replacement cost from the add-back. The difference is the true profit lift.

2. **Using the wrong profit metric.** If the business is owner-operated and you value it on EBITDA (which excludes owner comp), you will overpay because you are not accounting for the cost to replace the owner. Conversely, if the business is managed and you value it on SDE, you will underpay and the seller will reject your offer. Match the metric to the business structure.

3. **Applying a PE multiple to a small owner-operated business.** The 10.8x EBITDA multiple is for institutionalized, recurring-revenue, multi-location businesses that private equity wants. It does not apply to a single-location service business with no systems. Applying the wrong multiple leads to fantasy valuations. Use 2.4x to 3.5x for owner-op, 4.0x to 6.0x for managed, 10.8x+ only for true PE-grade businesses.

4. **Skipping the tax-return test.** If the P&L shows $500K profit but the tax return shows $300K, the seller is either hiding income (good for you, bad for IRS) or inflating the P&L (bad for you). Do not close without reconciling this gap. Request a written explanation. If the seller refuses, walk.

5. **Setting only one price instead of three.** If you enter negotiation with a single number in your head, you have no flexibility. The seller will anchor higher or lower and you will lose control. Always set walk-away (max you will pay), realistic (your target), and dream (best-case if seller is desperate). Negotiate toward dream, land at realistic, never exceed walk-away.

## Output

You receive an adjusted TTM profit figure (after auditing add-backs), a recommended multiple and rationale, an enterprise value calculation, and three prices (walk-away, realistic, dream). If net debt is provided, you also receive equity value. If tax returns are available, you receive a sanity-test pass/fail and any flags. This output feeds directly into the negotiation phase and the LOI drafter. Print the valuation summary and bring it to every negotiation conversation. Do not deviate from your walk-away price without new information.
