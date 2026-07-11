# Lesson 14 — The DD Engine

*Sequential due diligence after the LOI: document requests, red-flag rules, and a go/renegotiate/walk decision at every phase.*

Reading time: ~9 min · Track: Acquire · Prerequisite: signed LOI (`loi-drafter`, Lesson 13)

---

## What this does

Due diligence is where most bad deals die — in this method roughly 70% of deals die in DD, and that is normal, not failure. This skill runs the post-LOI process in five phases — financial, operational, legal, customer, final verification — generating the document request list for each, tracking findings, applying the red-flag rules (single customer over 30% of revenue, declining trend, unresolved liabilities, no team/no systems, financials that don't match tax returns), and recommending go / renegotiate / walk after every phase. Two Frasier principles frame the pace: move fast (a slow DD kills more good deals than it catches bad ones), and where the structure allows, use an SPV plus a break-up clause so parts of DD can complete shortly post-close instead of stalling the deal.

**You'll walk away with:** a phase-by-phase diligence tracker, request checklists you can send to the seller's attorney, and a final closing-readiness report.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/dd-engine` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- The signed LOI (the DD period and exclusivity clock start on signing day — launch Phase 1 within 48 hours).
- Your valuation file and AQ scorecard (DD verifies what discovery claimed).
- Professionals lined up: a CPA for the financials, an attorney for contracts and entity docs. Budget $5K–15K — cheap insurance against a $500K mistake.
- Access commitments from the seller: financials, contracts, customer data. Refusal of any category is itself a red flag.

---

## Step 3 — Run it (copy this)

```
/dd-engine
```

Or launch phase by phase:

```
Run the dd-engine skill for [business], [industry], [revenue/employees]. Start with Phase 1 (Financial): generate the document request list — required docs, nice-to-haves, red-flag indicators, and timeline — formatted as a checklist I can send to the seller's attorney today.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Phase request checklists | Per phase: required documents, preferred documents, red-flag indicators, timeline |
| Findings evaluations | Your findings run against the red-flag rules, with a go / renegotiate / walk recommendation per phase |
| Renegotiation drafts | When DD uncovers issues: a professional email to the seller with the issues, rationale, and revised terms |
| Final DD report | All findings across all five phases, final red-flag count, closing-readiness assessment |

**How it works:** the phases are sequential for a reason — financial comes first because if the numbers are wrong nothing else matters (recompute TTM, re-audit add-backs, check for windfalls; discrepancies over 10% mean renegotiate or walk). Operational verifies the business runs without the owner; legal verifies clean title and no landmines; customer diligence computes concentration and verifies recurring-revenue claims; final verification is the site visit, key-employee interviews, and a last 30-day bank-statement check for sudden drop-off. Because the LOI binds only exclusivity and confidentiality, every phase's findings are leverage: adjust terms or exit penalty-free inside the period.

---

## Step 4 — Test it, refine it, stack it

**Test** (run a phase decision):
```
Phase 1 findings for [business]: [documents received/missing, discrepancies vs. seller claims, flags]. Apply the red-flag rules and recommend: go to Phase 2, renegotiate (specify what), or walk (explain why).
```

**Refine** (issues found, deal still alive):
```
DD uncovered: [issues — e.g. top-3 customers are 45% of revenue, $30K undisclosed equipment lease]. Original terms: [price/structure]. Draft the renegotiation email: respectful, solution-focused, with revised terms and a reminder we're inside the DD period.
```

**Stack it:** a clean DD closes — and the loop restarts.
```
All five phases green. Build my closing checklist with my attorney's punch list — and queue the modernization-audit skill for week one of ownership.
```

---

## Tips & troubleshooting

- **Run all five phases, even when financial looks great.** A business with beautiful books and 60% customer concentration is a time bomb. Skipping phases is how buyers of lemons explain themselves later.
- **Apply the red-flag rules mechanically.** A single 40% customer is a red flag no matter how much you like the business. Reprice the risk or walk — don't rationalize. (This system's 30%/10% thresholds are deliberately tighter than the playbook's exit-early triggers.)
- **Verify, never accept explanations.** "Revenue dipped because of COVID," "that lawsuit is frivolous" — request third-party evidence: bank statements, court filings, appraisals. No evidence, assume the worst.
- **Bring professionals.** Solo DD misses red flags. CPA on the books, attorney on the contracts, an industry operator on the ops if you can get one.
- **Sunk cost is not a reason to close.** Forty hours in, attorney paid, emotionally attached — and DD finds reds. Walking away from a bad deal is the success case. There are other deals.

---

## Where this fits

Branch B, step 9 — the last gate before closing. A green final report goes to your attorney's closing checklist; then the loop turns: you're an owner now, and the system routes you into Branch A — **Lesson 15 — The Modernization Audit** — to raise the multiple on what you just bought.
