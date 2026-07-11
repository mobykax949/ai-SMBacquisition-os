# Lesson 13 — The LOI Drafter

*The written offer — built on your financing stack, disciplined by the 24-hour rule and "price OR terms, not both."*

Reading time: ~8 min · Track: Acquire · Prerequisite: `deal-stacker` stack chosen (Lesson 12)

---

## What this does

Generates a complete, properly structured Letter of Intent once price and terms are settled: parties, purchase price, payment terms (your financing stack, line by line), earnout provisions, seller transition and training, due diligence period, exclusivity, closing conditions — with the binding sections (only exclusivity and confidentiality) clearly marked. Two Frasier disciplines govern the draft. The 24-hour rule: you never commit on the spot — you state upfront that you always take 24 hours, which defuses pressure tactics before they start. And the trade: "You can have your price OR your terms, not both" — the seller gets their asking price only in exchange for favorable terms (long seller note, earnout, consulting offset), or accepts your lower price with seller-friendlier terms.

**You'll walk away with:** a ready-for-attorney-review LOI with your stack integrated as Section 3, plus a counteroffer evaluation framework.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/loi-drafter` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- Your documented walk-away / realistic / dream prices (Lesson 11).
- The chosen financing stack (Lesson 12) — every component with amounts, timing, interest, and security.
- The seller's priorities from discovery: certainty vs. speed vs. maximum dollars vs. legacy.
- A decision on the price-vs-terms path: their price with your terms, or your price with their terms. Not both.

---

## Step 3 — Run it (copy this)

```
/loi-drafter
```

Or specify the deal:

```
Draft a Letter of Intent. Buyer: [me/entity]. Seller: [name]. Target: [business, entity type, state]. Price: $[X]. Payment structure: [paste the stack line by line — e.g. $X cash at closing, $Y seller note at Z% over N years with balloon, $A earnout tied to year-2 SDE > $B, $C/year consulting for 3 years]. Transition: [training weeks, consulting period, non-compete radius/duration]. DD period: [30/45/60] days. Exclusivity matching. Mark binding vs non-binding sections clearly.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| The LOI document | Ten standard sections with signature blocks: parties, price, payment terms, earnout, transition, DD period, exclusivity, closing conditions, confidentiality, non-binding clause |
| Binding/non-binding markings | Only exclusivity and confidentiality bind; everything else stays negotiable through DD |
| Counteroffer evaluator | When the seller counters, it checks the counter against your walk-away and recommends accept / counter back / walk |
| Contingency clauses on request | E.g. an SBA financing contingency with a good-faith requirement and a defined out |

**How it works:** the stack becomes Section 3 line items, each with amount, timing, rate, security, and default remedies — vague terms ("$500K seller financing") are what create closing-table disputes. The LOI is morally (sometimes legally) weighty: only sign for deals you intend to close, because walking after signature costs reputation, even though the document itself leaves you free to renegotiate on DD findings.

---

## Step 4 — Test it, refine it, stack it

**Test** (evaluate a counter):
```
The seller countered: [changes — more cash at closing, lower earnout threshold, shorter non-compete]. My walk-away is $[X] and [terms]. Does the counter cross it? Recommend accept, counter back (with what), or walk.
```

**Refine** (add protection):
```
Add an SBA 7(a) financing contingency: if I cannot secure financing on acceptable terms within [X] days, I can terminate without penalty and recover earnest money. Keep the effort good-faith — no indefinite out.
```

**Stack it:** signature starts the clock.
```
The seller signed the LOI today. Run the dd-engine skill: set up the diligence tracker and generate the Phase 1 (financial) document request list — I want it sent within 48 hours.
```

---

## Tips & troubleshooting

- **Honor the 24-hour rule even under pressure.** Deal fever after a long negotiation is real. If a seller demands a same-day decision — "decide today or the deal is off" — that is itself a red flag; hold the line (they usually backtrack).
- **Never give both price and terms.** Their $2M asking price with $1.5M cash at closing and a short note means you overpaid and surrendered all leverage. The trade is the discipline.
- **Specify every payment term.** Interest rate, amortization shape, security, default remedies, prepayment. "Seller financing of $500K" is a dispute waiting for a closing table.
- **Size the DD period to the deal.** 30 days suits clean single-location books; complex businesses need 45–60. Compressing diligence to please a seller is how red flags get missed.
- **Attorney before the seller sees it.** State law varies on LOI enforceability and earnout language. The $500–$1,500 review is the cheapest insurance in the whole process.

---

## Where this fits

Branch B, step 8 — the offer. Acceptance starts the diligence clock: **Lesson 14 — The DD Engine**. A counter loops you back through your three prices; a rejection is information — ask why, then revise or walk.
