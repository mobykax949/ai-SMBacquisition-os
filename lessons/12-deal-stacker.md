# Lesson 12 — The Deal Stacker

*Three complete financing structures from the 216-technique taxonomy — stacked to drive your cash at closing toward zero.*

Reading time: ~9 min · Track: Acquire · Prerequisite: `valuation` complete (Lesson 11)

---

## What this does

The single biggest myth in acquisitions is that you need the purchase price in cash. Frasier's method catalogs 216 distinct funding strategies in 13 families — earn-in, seller-financed/owner-carry, consulting/IP offsets, asset carveouts, stock/merger structures, third-party equity, debt assumption, SBA/institutional, cashflow-assignment, pre-sale/promotion funding, credit bridges, supplier/vendor financing, and arbitrage plays — and real deals stack several at once. Give this skill the target's facts and it proposes three complete stacks (conservative, balanced, aggressive), names every component, shows the math, and computes your cash at closing for each. The chosen stack becomes Section 3 of your LOI.

**You'll walk away with:** three ranked financing stacks with per-component dollar amounts, payment timelines, and computed cash-at-closing — one of them ready to export to the LOI drafter.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/deal-stacker` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

Four inputs, all from earlier skills:

- **Target price** — or your walk-away/realistic/dream range from valuation.
- **TTM SDE** — the audited number, not the seller's claim.
- **Asset inventory** — real estate owned or leased, FF&E value, inventory, intangibles.
- **Seller motivation** — retiring, distressed, strategic exit, health. This drives which families fit: a retiring seller optimizing for certainty rejects a high-earnout stack; a distressed seller needs liquidity now.

Missing any of these? Go back to discovery or valuation first.

---

## Step 3 — Run it (copy this)

```
/deal-stacker
```

Or feed the facts:

```
Stack this deal: [target], asking $[X] (my realistic: $[Y]), TTM SDE $[Z]. Assets: real estate [owned/leased, value], FF&E $[A], inventory $[B]. Seller motivation: [retiring, wants certainty and legacy]. Propose three stacks (conservative / balanced / aggressive) from the 13 funding families, name every component with its dollar contribution and timing, compute my cash at closing for each, and recommend one with reasoning.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Conservative stack | Lowest risk, moderate seller-financing ask — the fallback if the seller resists creative structure |
| Balanced stack | Multiple families blended — typically your realistic target |
| Aggressive stack | Maximum creativity, targets zero (or negative) cash at closing — the opening position with a motivated seller |
| Per-stack math | Every named strategy, its dollar amount, the payment timeline (at closing / deferred / earnout / consulting), and your computed cash-at-closing |
| LOI handoff | The chosen stack formatted as purchase-price-and-payment-terms line items |

**How it works:** the backbone of nearly every low-money-down deal is seller financing + owner-carry + earnout + deferred down payment + consulting offset; the other families layer on top (assume debt, carve out and sell non-essential assets, pre-sale promotions to the target's own list, third-party equity). The principle is Frasier's: cover the purchase price from sources other than your own cash. Zero cash at closing does not mean zero price — the seller still receives the agreed price, just from stacked sources instead of your bank account.

---

## Step 4 — Test it, refine it, stack it

**Test** (pressure-test against the seller's psychology):
```
The seller's stated priority is [certainty / immediate liquidity / legacy / top dollar]. Score each of the three stacks against that priority and flag any component they're likely to reject. Adjust the recommended stack.
```

**Refine** (tune the chosen structure):
```
I'm going with the [balanced] stack. Extend the seller note balloon to 7 years, add a $[X]/year consulting offset for 3 years, and re-compute my cash at closing and the full payment schedule.
```

**Stack it:** lock it into the offer.
```
Lock in this financing stack and feed it to the loi-drafter skill as Section 3 (Purchase Price and Payment Terms).
```

---

## Tips & troubleshooting

- **Get seller buy-in on the concept before the complexity.** If the seller is broker-advised toward conventional terms, open with the conservative stack and introduce one or two creative elements — not seven. Trust first, then structure.
- **Flag tax and legal implications early.** Consulting offsets, IP royalties, and stock consideration all have tax consequences for both sides. Attorney and CPA before the LOI — Claude's math does not account for tax treatment.
- **Don't confuse cash-at-closing with purchase price.** Present them separately to the seller, or the structure sounds like a discount and offends them.
- **Don't count pre-sale funding you haven't confirmed.** Rev-share pre-sales and 4-day-cash-machine plays require the seller to allow pre-close marketing to their list. Many refuse. Confirm before it goes in the stack.
- **Match the stack to the seller's motivation, not just the dollar target.** Certainty-and-legacy sellers reject earnout-heavy structures even at a higher total price. The motivation you captured in discovery is a structural input, not color.

---

## Where this fits

Branch B, step 7 — between the number (valuation) and the offer (LOI). The output is a financing design, not a legal document: your attorney drafts the notes and agreements that implement it. Next: **Lesson 13 — The LOI Drafter**.
