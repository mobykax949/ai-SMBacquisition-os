---
name: deal-stacker
description: Use when you need to design creative financing structures for a business acquisition, stacking multiple strategies from the 216-technique taxonomy to reach zero cash at closing.
version: 1.0.0
---

# Deal Stacker

## Overview

The flagship financing design tool. Given a target's basic facts (asking price, SDE, asset value, seller motivation), this skill proposes three complete financing stacks that combine multiple strategies from Roland Frasier's 216-technique taxonomy. Each stack draws from the 13 families (earn-in, owner-carry, consulting offsets, asset carveouts, stock/merger, co-investor, debt assumption, SBA/institutional, cashflow-assignment, pre-sale funding, credit bridges, vendor financing, arbitrage) to minimize or eliminate your cash at closing. The chosen stack feeds directly into the LOI drafter.

## When to Use

Run deal-stacker after you have completed valuation and settled on a realistic price range. You need four inputs: the target price (or price range), trailing-twelve-month SDE, a rough asset inventory (real estate, FF&E, inventory), and the seller's stated motivation (retirement, burnout, distressed, health, other opportunity). If you lack any of these, return to discovery-interviewer or valuation first. The output is three ranked stacks (conservative, balanced, aggressive) with cash-at-closing computed for each.

## Steps

1. **Gather the four required inputs.** Target price (or walk-away/realistic/dream range from negotiation), TTM SDE, asset breakdown (real estate owned or leased, FF&E value, inventory value, intangibles), seller motivation category (retiring owner, distressed/capital-starved, strategic exit, health/personal).

2. **Describe the situation to Claude.** Paste the first prompt below and fill in the bracketed placeholders with your target's facts. Claude will analyze the situation and identify which of the 13 financing families apply.

3. **Review the three proposed stacks.** Claude returns a conservative stack (lowest risk, moderate seller-financing ask), a balanced stack (blends multiple families), and an aggressive stack (maximum creativity, targets zero cash). Each stack names every component strategy, shows the math, and computes your cash requirement at closing.

4. **Select one stack and refine.** Tell Claude which stack you prefer, then ask follow-up questions to refine terms (interest rates, balloon dates, earnout triggers, consulting fee structures). Claude will adjust the math and re-compute cash at closing.

5. **Export the chosen stack to LOI.** Once you settle on a structure, tell Claude to feed it into the LOI drafter. The financing terms become Section 3 of your Letter of Intent.

## The Prompts

**Prompt 1: Generate Three Financing Stacks**

```
I need three creative financing structures for this acquisition target:

- Asking price: [insert dollar amount or walk-away/realistic/dream range]
- TTM SDE: [insert SDE from valuation]
- Assets: Real estate [owned/leased, value if owned], FF&E [value], Inventory [value]
- Seller motivation: [retiring/distressed/strategic/health/other - describe briefly]

Design three stacks (conservative, balanced, aggressive) using Roland Frasier's 216 deal-funding strategies across the 13 families:

A. Earn-in / sweat equity (instant, milestone-based, train-in, toll-gate)
B. Seller-financed / owner-carry (unsecured/secured, balloon, earnout, deferred down payment, holdback)
C. Seller consulting / IP offsets (fee-based, performance-based, royalty, IP license)
D. Asset carveouts & consignment (sell non-essential assets, consign inventory, trash-to-cash, real estate split/sale-leaseback)
E. Stock buy-back & merger (sell-and-stock-back, SPV merger, roll-in, partial acquisition, option to acquire)
F. 3rd-party equity & co-investors (co-investors, non-competing equity split, integrator investor, employee/supplier/angel, crowdfunding, pipe wrench)
G. Debt assumption & restructuring (subject-to, debt wrap, assume target/seller debt, tax assumption, debt-to-equity swap)
H. Lender / institutional (SBA 7a/504, LBO, mezzanine, RBF, HELOC, margin loan, life insurance loan, IRA/ROBS, hard money, self-liquidating payment)
I. Cashflow-assignment down payments (assign gross/net sales/margin receipts to seller for DP or seller financing paydown)
J. Pre-sale / promotion funding (rev-share pre-sale tests to the target's list, 4-day cash machine, 100% promos, defer close + sale, pre-sell inventory/ad space)
K. Credit / round-robin / short-term bridges (credit card advance/round-robin, CC for seller's desired asset, short-term note, post-date check, CC reserve release)
L. Supplier / vendor / AR / inventory financing (supplier invests/loan/terms/consignment, PO finance, AR factoring, vendor prepayments, landlord rent deferral, vendor co-sign)
M. Arbitrage / flip / advanced (double escrow, reverse wholesale, barter arbitrage, 3rd-party hypothecation/guaranty/co-signer, asset/stock swaps, seller co-signs, W/C adjustment, non-compete abatement, pull recurring revenue forward)

For each stack, name every component strategy, show the dollar amount contributed by each, and compute my cash at closing. Explain the logic and timing of each piece. Apply Frasier's principle: stack multiple strategies to drive cash-at-closing to zero or negative.
```

**Prompt 2: Refine the Chosen Stack**

```
I want to move forward with the [conservative/balanced/aggressive] stack. Let's refine these terms:

- [Ask specific questions: "Can we extend the seller note balloon to 7 years instead of 5?" or "What if we add a consulting offset of $50K/year for 3 years?" or "How would an earnout on year-2 SDE growth change the math?"]

Re-compute cash at closing with the adjusted terms and confirm the revised financing schedule.
```

**Prompt 3: Export to LOI Drafter**

```
Lock in this financing stack and feed it to the LOI drafter. I'm ready to draft the Letter of Intent with these terms as Section 3 (Purchase Price and Payment Terms).
```

## The Loop

After Claude generates the three stacks, review them against your own liquidity and risk tolerance. The conservative stack is the fallback if the seller resists creative structures. The aggressive stack is your opening negotiating position if the seller is highly motivated (retiring, distressed, or explicitly asked for creative terms). The balanced stack is typically your realistic target. Refine the chosen stack by asking Claude to adjust individual components (longer amortization, higher earnout threshold, larger consulting offset, different balloon date). Each refinement re-runs the math. When you settle on final terms, export to LOI drafter and proceed to negotiation.

## Pitfalls

1. **Stacking without seller buy-in on the concept.** Creative financing only works if the seller understands and accepts non-traditional structures. If the seller demands all-cash or is broker-advised toward conventional terms, start with the conservative stack and introduce one or two creative elements, not seven. Build trust before complexity.

2. **Ignoring the tax and legal implications of certain strategies.** Some structures (seller consulting offsets, IP royalties, stock-based consideration) have tax consequences for both parties. Flag these for your attorney and CPA before the LOI. Do not assume Claude's financing math accounts for tax treatment.

3. **Confusing cash-at-closing math with total purchase price.** A zero-cash-at-closing deal does not mean zero purchase price. The seller still receives the agreed price, but the payment sources come from seller financing, earnouts, asset sales, pre-close promotions, or third-party equity instead of your bank account. Clearly distinguish "price" from "your cash in" when presenting to the seller.

4. **Over-reliance on pre-sale/promo funding without testing demand first.** Strategies like rev-share pre-sale tests and the 4-day cash machine require access to the target's customer list and the ability to run a promotion before closing. If the seller refuses pre-close marketing (common), these strategies are unavailable. Confirm seller willingness before including them in your stack.

5. **Not pressure-testing the stack against the seller's stated priorities.** A retiring seller optimizing for certainty and legacy will reject a high-earnout, low-upfront stack even if the total price is higher. A distressed seller needing immediate liquidity will reject long-term consulting offsets. Match your stack's structure to the seller's motivation, not just the dollar target.

## Output

You receive three complete financing stacks, each with: (1) a list of named strategies from the 13 families, (2) the dollar contribution of each component, (3) a payment timeline (upfront, at closing, deferred, earnout, consulting, etc.), (4) computed cash-at-closing for you, and (5) a brief rationale explaining why this stack fits the target's profile. After refinement, you receive an updated stack ready to export into the LOI drafter. The output is a financing design, not a legal document. You still need an attorney to draft the actual promissory notes, security agreements, consulting contracts, and earnout schedules that implement the stack.
