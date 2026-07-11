# Lesson 11 — Valuation & Add-Backs

*SDE or EBITDA, the TTM method, the add-back audit that stops you overpaying, and your three prices before the room.*

Reading time: ~9 min · Track: Acquire · Prerequisite: seller financials in hand (`discovery-interviewer`, Lesson 10)

---

## What this does

The EPIC valuation method, end to end. It chooses the right profit metric (SDE for owner-operated, EBITDA for professionally managed), computes trailing-twelve-month profit from the actual statements, then runs the audit that matters most: for every add-back the seller claims, it subtracts the true cost to replace the owner's role — the discipline that prevents the classic 20–40% overpay. It anchors the multiple on Frasier's landscape — owner-operated 2.4x SDE, professionally managed 4.0x EBITDA, private equity 10.8x, public markets 18.7x (buy at the low boxes, sell toward PE) — and ends with your three prices: walk-away, realistic, dream. A tax-return sanity test confirms the P&L matches Schedule C or the corporate return before you trust any of it.

**You'll walk away with:** adjusted TTM profit, a recommended multiple with rationale, enterprise value, and your walk-away / realistic / dream prices documented before negotiation.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/valuation` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- The real documents: three years of P&L, balance sheet, cash flow statement, and ideally tax returns. Do not attempt valuation from a teaser or broker summary — if you lack these, go back to discovery and request them.
- TTM revenue, COGS, operating expenses, owner compensation, and the seller's claimed add-backs, itemized.
- The business profile: the owner's actual daily role, team, and whether processes are documented (this decides SDE vs EBITDA).

---

## Step 3 — Run it (copy this)

```
/valuation
```

Or feed it the numbers:

```
Value this business with the EPIC method. TTM: revenue $[X], COGS $[Y], opex $[Z], owner comp $[W]. Seller's claimed add-backs: [list each with amount]. Owner role: [daily CEO / absentee]. Team: [n employees, key roles]. Choose SDE or EBITDA, compute TTM profit, audit every add-back against true replacement cost, recommend a multiple from the landscape, and give me walk-away / realistic / dream prices.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Metric choice + TTM profit | SDE or EBITDA, computed from the last 12 months — never the seller's claimed number |
| Add-back audit | Each claimed add-back vs. the true cost to replace the function; the adjusted profit that survives |
| Multiple + enterprise value | The recommended multiple with rationale, anchored on 2.4x / 4.0x / 10.8x / 18.7x; equity value if net debt is known |
| Three prices | Walk-away (the maximum — high end of the range; above it you walk), realistic (mid — where you expect to land), dream (low end or below) |
| Tax-return sanity test | P&L vs. Schedule C / 1120 within 5% — or a flag that the books are unreliable |

**How it works:** the add-back audit is where the money is. A seller claims their $200K salary as an add-back; if replacing what they actually do costs $100K, only $100K of it is real profit lift — accept the claim at face value at a 3x multiple and you just overpaid by $300K. The three-price frame then locks discipline before emotion: negotiate toward dream, land at realistic, never cross walk-away.

---

## Step 4 — Test it, refine it, stack it

**Test** (sensitivity):
```
My realistic valuation is $[X] at [Y]x adjusted SDE. Show the valuation if: the multiple drops 0.5x, profit drops 10% in the transition year, and I find another $20K of owner expenses. Recompute my three prices for each scenario.
```

**Refine** (diligence changes the number):
```
DD uncovered: [new fact — hidden cost, extra add-back, customer concentration]. Re-run the valuation with this, and tell me if my walk-away price changes. If the valuation dropped more than 20% from the original, say so plainly.
```

**Stack it:** the number goes to financing design.
```
Valuation locked: realistic $[X], TTM SDE $[Y]. Run the deal-stacker skill: assets are [FF&E, inventory, real estate y/n], seller motivation is [retirement/...]. Propose three financing stacks.
```

---

## Tips & troubleshooting

- **Never accept add-backs without the audit.** The most expensive mistake in the whole funnel. Ask "what does it cost to replace this function?" for every single claim.
- **Match the metric to the business.** Valuing an owner-operated business on EBITDA ignores the cost of replacing the owner — you overpay. Valuing a managed business on SDE lowballs — the seller walks.
- **Don't apply a PE multiple to a single-location service business.** 10.8x is for institutionalized, recurring-revenue, multi-location businesses. The anchors exist to keep your fantasy in check.
- **Run the tax-return test before you close.** P&L says $500K, return says $300K? Either hidden income or an inflated P&L — both are your problem. No reconciliation, no deal.
- **Three prices, always.** One number in your head means the seller's anchor controls the room. Walk-away, realistic, dream — documented before the conversation.

---

## Where this fits

Branch B, step 6 — the number that everything downstream depends on. Feeds **Lesson 12 — Deal Stacker** (financing the price) and **Lesson 13 — LOI Drafter** (offering it). Re-run after every material discovery in diligence.
