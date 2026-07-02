---
name: margin-finder
description: Use when you need AI applied to your P&L to identify margin lifts ranked by impact vs disruption. Claude analyzes your categories, finds pricing gaps, unbilled work, admin time AI can absorb, and vendor renegotiation targets, then produces a 90-day margin plan.
version: 1.0.0
---

# Margin Finder

## Overview

Most small business owners leave 10 to 20 percent margin on the table without knowing it. The margin is there, hidden in pricing that has not been updated in years, unbilled work performed as favors, admin time that could be automated, and vendor contracts that were never renegotiated. This skill applies AI analysis to your profit and loss statement to find those margin lifts. You paste your P&L categories (revenue line items and expense line items), Claude identifies improvement opportunities ranked by impact (dollars added to the bottom line) versus disruption risk (how much it will upset customers, staff, or operations), and produces a 90-day margin plan with specific actions. This is the fastest path to profitability improvement without acquiring new customers.

## When to Use

Run margin-finder when you have at least 12 months of P&L data (ideally 24 months) and you want to lift net margin by 5 to 15 percentage points without changing your core service offering. You need access to your P&L categories broken out in detail (not just total revenue and total expenses). If your bookkeeping is a mess, clean it up first. If you do not know your margins by service line or customer type, get that data before running this skill. Margin-finder works best on established businesses with stable revenue where the owner has not optimized pricing or expenses in over 2 years.

## Steps

1. **Export your P&L for the last 12 to 24 months.** Pull the report from QuickBooks, Xero, or wherever you track finances. You need revenue broken out by product or service line (not just one total revenue number) and expenses broken out by category (payroll, rent, materials, software, marketing, etc.). Save as a CSV or copy the text into a document. Done when you have the full P&L data ready to paste.

2. **Run the margin analysis interview with Prompt 1.** Paste your P&L categories. Claude will ask clarifying questions: What is your pricing model (hourly, flat-fee, subscription)? When did you last raise prices? Do you track cost per job or customer? Are there services you deliver for free that you could charge for? Do you discount, and how often? Answer each question. Done when Claude has a clear picture of your revenue model and cost structure.

3. **Identify margin lift opportunities.** Use Prompt 2. Claude analyzes your P&L and flags opportunities in six categories: (1) Pricing gaps versus market (you are 10 to 20 percent below competitors), (2) Unbilled work (services performed as add-ons or favors that should have a line item), (3) Admin time that AI or automation absorbs (bookkeeping, scheduling, email, quoting), (4) Vendor renegotiation candidates (contracts over 2 years old, or single-source vendors with no recent rebid), (5) Underutilized subscriptions or tools (software you pay for but barely use), (6) Customer or service line pruning (money-losing customers or products). Done when you have a ranked list of 10 to 15 opportunities.

4. **Score each opportunity by impact versus disruption.** Impact is measured in annualized margin dollars added (if you raise prices 10 percent on $500K revenue, that is $50K impact). Disruption is scored low/medium/high based on customer reaction risk, operational complexity, and team friction. A 10 percent price increase on new customers is low disruption. A 10 percent price increase on existing customers mid-contract is high disruption. Done when every opportunity has an impact number and a disruption rating.

5. **Generate the 90-day margin plan.** Use Prompt 3. Claude sorts the opportunities into three 30-day waves: Month 1 (low disruption, fast implementation), Month 2 (medium disruption, requires customer communication or vendor negotiation), Month 3 (higher disruption, requires process change or repricing). Each wave specifies: actions to take, owner deliverables, expected margin lift, and rollback plan if something breaks. Done when you have a phased plan you can execute without overwhelming the business.

6. **Execute the plan and measure results.** Implement month one opportunities. Track the margin lift in your P&L. If a change causes problems (customer complaints, team confusion), pause and revise. At day 30, measure actual margin improvement versus projected. If you hit your target, proceed to month two. If you missed, diagnose why before adding more changes. Done when you have real data showing margin movement.

7. **Review and iterate for months two and three.** After month one, revisit the plan. Some opportunities will have worked better than expected. Some will not be worth the disruption. Revise months two and three based on actual results. The goal is net margin improvement of 5 to 15 points over 90 days. If you achieve that, the business is worth significantly more (every point of margin lifts the valuation).

## The Prompts

**Prompt 1: The P&L Analysis Interview**

```
I need to analyze my business P&L to find margin improvement opportunities. I will paste my revenue and expense categories below. After you review it, ask me these questions ONE at a time:

1. What is my pricing model? (hourly, flat-fee, per-project, subscription, hybrid)
2. When did I last raise prices?
3. Do I track cost per job or per customer? Can I see which services or customers are most profitable?
4. Are there services I deliver for free (or as add-ons) that I could charge for separately?
5. Do I offer discounts? How often, and what percentage?
6. Which expense categories have not been reviewed or renegotiated in over 2 years?
7. What software or subscriptions do I pay for that the team barely uses?

Here is my P&L data for the last 12 months:

[Paste P&L with revenue line items and expense categories. Include dollar amounts and percentages if available.]
```

**Prompt 2: Identify and Rank Margin Opportunities**

```
Using my P&L data and your answers to the interview questions, identify margin lift opportunities in these six categories:

1. **Pricing gaps versus market:** Am I priced below competitors? Should I raise prices for new customers, existing customers, or specific services?
2. **Unbilled work:** Services I perform as favors, add-ons, or scope creep that should have a billable line item.
3. **Admin time AI/automation can absorb:** Tasks I or my team spend time on (scheduling, quoting, invoicing, email, bookkeeping) that software could handle.
4. **Vendor renegotiation candidates:** Contracts over 2 years old, single-source vendors, or categories where I accepted the first quote without rebidding.
5. **Underutilized subscriptions or tools:** Software or services I pay for monthly but use less than once per week.
6. **Customer or service line pruning:** Money-losing customers (high cost to serve, low margin) or products that are not worth the complexity.

For each opportunity, estimate the annualized margin impact in dollars (e.g., "Raising prices 8% on new customers = $40K/year") and score disruption risk as low, medium, or high. Return a ranked table: opportunity, category, impact, disruption, priority.
```

**Prompt 3: Build the 90-Day Margin Plan**

```
Using the ranked opportunity list from Prompt 2, create a 90-day phased margin improvement plan:

**Month 1 (Days 1-30): Low-Disruption Quick Wins**
- Opportunities: [list the low-disruption, high-impact items]
- Actions: [specific steps to take]
- Owner deliverables: [what I personally must do]
- Expected margin lift: [dollar amount]
- Rollback plan: [what to do if it causes problems]

**Month 2 (Days 31-60): Medium-Disruption Improvements**
- Opportunities: [medium-disruption items, requires customer communication or vendor negotiation]
- Actions, deliverables, margin lift, rollback plan

**Month 3 (Days 61-90): Higher-Disruption Strategic Changes**
- Opportunities: [higher-disruption items, process changes or repricing existing customers]
- Actions, deliverables, margin lift, rollback plan

**Total Expected Margin Lift:** [sum of all three months in dollars and percentage points]

Include measurement instructions: which P&L line items to track weekly to confirm the lift is real.
```

## The Loop

Run margin-finder once to build the baseline 90-day plan. Execute the plan in monthly waves, measuring margin improvement after each wave. After 90 days, re-run the analysis. Some opportunities you skipped in round one will now be feasible (you built trust with customers, you have automation in place, you hired help). New opportunities will appear as the business grows or market conditions change. The business is never fully optimized. Margin-finder is a quarterly discipline, not a one-time project. Every 5 percentage points of margin improvement increases your business value by hundreds of thousands of dollars (moving from 15 percent margin to 20 percent margin on a $2M revenue business lifts EBITDA from $300K to $400K, worth $400K more at 4x EBITDA).

## Pitfalls

1. **Running margin-finder on messy books.** If your P&L is not categorized (everything dumped into "miscellaneous expenses"), Claude cannot find the opportunities. Clean up your bookkeeping first. Spend 2 hours recategorizing the last 12 months before running this skill.

2. **Implementing every opportunity at once.** If you raise prices, cut vendors, automate scheduling, and fire low-margin customers all in the same week, you will overwhelm the business and create chaos. The 90-day plan phases changes for a reason. One wave at a time.

3. **Raising prices on existing customers without communication.** A surprise 10 percent price increase will lose you customers. If you need to raise prices on existing contracts, give 30 to 60 days notice, explain the reason (costs went up, you added value, market rates shifted), and offer a smaller increase for multi-year commitments. Handle it like a conversation, not a policy change.

4. **Cutting costs that matter to quality.** Not all expenses should be cut. If you eliminate a tool the team relies on to save $100 per month, and productivity drops 10 percent, you just cost yourself $10K in lost revenue. Always ask: does this expense support revenue or quality? If yes, negotiate it down but do not eliminate it.

5. **Not measuring the results.** If you implement 5 margin improvements and do not track the P&L weekly, you have no idea if they worked. Create a simple tracking spreadsheet: opportunity implemented, date implemented, expected margin lift, actual margin lift at day 30. Measure, compare, adjust.

## Output

You receive a 90-day phased margin improvement plan with 10 to 15 ranked opportunities grouped into three monthly waves. Each opportunity includes: the category (pricing, unbilled work, automation, vendor renegotiation, subscription pruning, or customer pruning), the estimated annualized margin impact in dollars, the disruption risk rating (low/medium/high), and specific action steps with owner deliverables. The plan also includes weekly P&L tracking instructions so you can measure actual margin lift versus projected. After executing the 90-day plan, your net margin should improve by 5 to 15 percentage points. That margin lift translates directly to business value. A business with 20 percent margin is worth significantly more than the same business with 10 percent margin, even if revenue is identical. Margin-finder is the fastest way to increase your multiple without buying anything.
