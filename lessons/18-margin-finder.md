# Lesson 18 — The Margin Finder

*AI on your P&L: hunting the pricing gaps, unbilled work, and stale vendor contracts that can hide many points of margin.*

Reading time: ~8 min · Track: Modernize · Prerequisite: 12+ months of categorized P&L data

---

## What this does

Most small business owners leave margin on the table without knowing it — in prices not raised for years, work performed as unbilled favors, admin hours automation could absorb, and vendor contracts nobody ever rebid. This skill runs your P&L through a structured hunt across six categories: pricing gaps vs. market, unbilled work, admin time AI can absorb, vendor renegotiation candidates, underutilized subscriptions, and money-losing customers or service lines. Every opportunity gets an annualized dollar impact and a disruption rating, then everything rolls into a phased 90-day plan — low-disruption wins first, repricing existing customers last.

**You'll walk away with:** a ranked list of 10–15 margin opportunities and a three-wave 90-day plan with expected lift, owner deliverables, and rollback plans.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/margin-finder` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- Your P&L for the last 12–24 months, exported from QuickBooks/Xero, with revenue broken out by service line and expenses by category. One total-revenue number and a "miscellaneous" expense bucket won't work — clean up the books first if needed (2 hours recategorizing beats a useless analysis).
- Answers ready for the interview: your pricing model, when you last raised prices, whether you track cost per job, what you deliver free, how often you discount, which contracts haven't been rebid in 2+ years.

---

## Step 3 — Run it (copy this)

```
/margin-finder
```

Or start with the data:

```
Analyze my P&L for margin improvement. Here are my last 12 months of revenue line items and expense categories: [paste]. Interview me one question at a time about pricing model, last price raise, cost tracking, free work, discounting, stale vendor contracts, and unused subscriptions. Then find opportunities in the six categories and rank by impact vs. disruption.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Opportunity table | 10–15 opportunities across the six categories, each with annualized dollar impact and low/medium/high disruption |
| 90-day plan | Month 1: low-disruption quick wins · Month 2: customer communication and vendor negotiation · Month 3: process changes and repricing existing customers — with actions, deliverables, expected lift, and rollback plans per wave |
| Tracking instructions | Which P&L lines to watch weekly so the lift is measured, not assumed |

**How it works:** impact and disruption are scored separately because they don't correlate — a 10% price rise on *new* customers is low-disruption free money; the same rise mid-contract on existing customers is a churn event. The three waves sequence trust: quick wins fund credibility, then vendor rebids and communicated changes, then the structural moves. Every 5 points of net margin on a $2M business is roughly $100K of EBITDA — worth $400K at a 4x multiple. Margin work is multiple work.

---

## Step 4 — Test it, refine it, stack it

**Test** (validate the biggest claim):
```
Take the #1 opportunity: [opportunity]. Show your math on the $[X] annual impact, list what could go wrong, and give me the smallest safe pilot to prove it before full rollout.
```

**Refine** (day 30 checkpoint):
```
Month 1 results: [what was implemented, actual margin movement, any complaints or friction]. Compare actual vs. projected, diagnose gaps, and revise months 2 and 3 before we add more change.
```

**Stack it:** margin lift plugs into the valuation math.
```
Re-run my multiple-builder assessment with the new margins — show me the enterprise-value change from this quarter's margin work.
```

---

## Tips & troubleshooting

- **Don't run this on messy books.** Everything dumped in "miscellaneous" hides every opportunity. Recategorize first.
- **One wave at a time.** Raising prices, cutting vendors, automating scheduling, and firing customers in the same week creates chaos you can't diagnose. The phasing is the plan.
- **Communicate price rises to existing customers.** 30–60 days notice, a reason (costs, added value, market rates), and a softer increase for multi-year commitments. A conversation, not a policy announcement.
- **Don't cut expenses that protect quality.** Killing a $100/month tool the team relies on and losing 10% productivity is a $10K own-goal. Ask: does this expense support revenue or quality? Negotiate it, don't eliminate it.
- **Measure weekly.** Implemented changes without P&L tracking means you have opinions, not results. Opportunity, date, expected lift, actual at day 30.

---

## Where this fits

Branch A, step 4 — the fastest value creator in the modernize track (no new customers required). Runs alongside the SOP loop; feeds **Lesson 19 — The Customer Engine** (revenue side) and shows up directly in **Lesson 20 — The Multiple Builder**'s clean-financials and valuation math. Re-run quarterly — the business is never fully optimized.
