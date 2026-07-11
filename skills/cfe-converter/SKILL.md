---
name: cfe-converter
description: Use when a business owner you contacted is not ready to sell. Converts a dead "no" into a consulting-for-equity (CFE) engagement — pitching advisory work in exchange for permanent equity using Roland Frasier's 10/10/10 model, so no outreach is wasted.
version: 1.0.0
---

# CFE Converter

## Overview

Most buyers treat "I'm not ready to sell" as the end of the conversation. In the EPIC method it is a fork, not a dead end. Every owner you reach lands in one of three outcomes — **acquire** (they want to sell, run the AQ Score), **agency client / CFE** (not ready to sell but needs help, so you take equity for advisory work), or **referral** (not a fit, but they know someone who is). No outreach is wasted. This skill runs the middle path: it helps you spot when an owner is a consulting-for-equity candidate, frame the pitch around the value they cannot see in their own business ("the other eye"), and structure the deal on Roland Frasier's default **10/10/10** terms — the greater of 10% of profits or $10k per month, plus 10% of the exit price. The result is permanent equity in a business you never had to buy.

## When to Use

- An owner from your outreach or a discovery call says they are not ready to sell, but the business is real, profitable, and has obvious untapped upside
- You have a skill, network, or system the owner lacks (marketing, AI operations, acquisitions know-how, an exit playbook) and could apply for equity instead of a fee
- You want a second monetization path for the ~60% of responders who will never sell, so your outreach funnel keeps paying off
- You already do consulting or agency work for a flat fee and want to add equity on top

Do NOT use this when the owner genuinely wants to sell (go to `aq-analyzer` and the acquisition funnel) or when there is no real business value to unlock (route to `referral` and move on).

## Steps

1. **Confirm the fork.** From the outreach or discovery conversation, decide which of the three outcomes this owner is: acquire, CFE/agency, or referral. This skill runs only when the answer is CFE/agency — the owner is not selling, but the business is worth helping and you have something to contribute. Done when you can name why this is a CFE candidate and not an acquisition.

2. **Find the money already in front of them ("be the other eye").** Most owners are caught up in the thing they sell and cannot see the transformation ladder worth far more — a backend offer, a monetization layer, an acquisition they could make, an exit they could run. List the specific upside you can unlock that they are not capturing. Done when you have 1–3 concrete, believable value levers named.

3. **Decide what you contribute and what you take.** You bring skills, systems, network, or capital-adjacent know-how; you take equity, not (only) a fee. Prefer permanent equity in the company over a one-time joint venture. Use Prompt 1 to draft the contribution-for-equity scope. Done when the deliverables and the equity ask are both written down.

4. **Structure the equity on 10/10/10.** The default Frasier structure is the **greater of 10% of profits OR $10k/month, plus 10% of the exit price**, applied at the holding-company level (preferred) or a single business, as permanent equity. Prefer **performance-vested** equity tied to a measured baseline ("as long as we hit X, our equity vests") so you only get paid when you outperform — and so you do not inflate the valuation against yourself. Use Prompt 2. Done when you have a written structure with the vesting trigger named.

5. **Handle the tax and structure notes.** Receiving equity in an *existing valuable* company can trigger tax on receipt. The two KB workarounds: (a) take a **profits-only interest**, or (b) start a **new company** both parties contribute into (they contribute assets, you contribute skills/services). Flag these for the owner's CPA — this skill does not give tax advice. Done when the tax path is chosen and flagged for professionals.

6. **Pitch it and close.** Deliver the offer as a partnership, not a sale: you keep them in control, you unlock value they were leaving on the table, and you only win when they win. Where they still resist equity, offer a JV as a bridge to prove credibility first. Use Prompt 3. Done when you have a staged pitch ready to send and, ideally, a signed letter of engagement routed through their attorney.

## The Prompts

**Prompt 1: Find the Upside and Draft the Contribution**

```
I contacted a business owner who is not ready to sell but has a real, profitable business. Help me build a consulting-for-equity (CFE) case.

Owner / business: [name, industry, size, what they do]
What they are NOT capturing (my read): [untapped backend, no marketing system, manual ops, no acquisition strategy, no exit plan, etc.]
What I bring: [my skills, systems, network, AI-operations capability, acquisitions know-how]

Be "the other eye": name the 1-3 highest-value levers I could unlock in this business that the owner probably cannot see because they are caught up in the thing they sell. For each, state the transformation and a rough sense of the value at stake (label anything you cannot ground as an estimate). Then draft a consulting deliverables scope: what I would advise on (business model, value ladder, marketing, growth, acquisitions, exit) and how I would contribute.
```

**Prompt 2: Structure the 10/10/10 Equity Deal**

```
Structure a consulting-for-equity deal on Roland Frasier's default 10/10/10 model:
- The greater of 10% of profits OR $10,000/month, PLUS 10% of the exit price.
- Permanent equity, at the holding-company level if there is one, otherwise this single business.
- Performance-vested against a measured baseline: define the baseline (their historical average over prior periods) and the trigger (equity vests as we beat it), so I am paid on outperformance, not on the valuation as-is.

Deal facts:
- Business: [name, current profit, rough valuation if known]
- Baseline to beat: [historical average revenue/profit, or "need to compute from their last N periods"]
- What I contribute: [from Prompt 1]

Produce: the equity terms in plain English, the vesting trigger, and whether I should also keep an upfront fee (equity is on top, not instead). Note where I should take equity in BOTH the core asset AND its monetization layer. Do NOT give tax or legal advice — flag the receipt-of-equity tax question for their CPA and note the two workarounds (profits-only interest, or a new co both parties contribute into).
```

**Prompt 3: Draft the Partnership Pitch**

```
Draft the CFE pitch to this owner as a partnership, not a sale. Tone: collaborative, low-pressure, "the other eye."

Include: (1) what I noticed they are leaving on the table, (2) what I would contribute, (3) the 10/10/10 structure framed as "I only win when you win" (performance-vested), (4) that they stay in control and keep their business, (5) a soft close to a working session. If they resist granting equity, offer a joint venture as a bridge to prove the value first, then convert to equity. Keep it under 200 words. Stage it for my review — do not send anything.
```

## The Loop

CFE is the second lane of the Magic Intersection: acquire · agency-client/CFE · referral. Run it whenever an outreach or discovery conversation produces a "not selling" that still has real business value behind it. The engagement compounds your funnel — a single outreach campaign that yields a handful of acquisitions can also yield CFE equity stakes and referrals, so no conversation is wasted. Over time, holding-company-level 10/10/10 stakes across several owners become their own portfolio, and a CFE client who later decides to sell is a warm acquisition lead you already understand from the inside.

## Pitfalls

1. **Taking a one-time JV when you could take permanent equity.** A JV is only a bridge for proof/credibility when the owner will not grant equity yet. The goal is permanent equity in the company. Do not settle for the JV if you can get the equity.

2. **Raising the valuation before you take equity.** If you inflate the valuation first, the owner learns they are worth more, needs you less, and offers you a smaller piece. Vest your equity off a measured baseline and take your stake before you drive the number up.

3. **Pitching a fee instead of equity — or equity instead of a fee.** The move is usually equity ON TOP of your normal fee, not instead of it. Stack them. Leaving the fee on the table is as much a mistake as leaving the equity.

4. **Ignoring the tax-on-receipt problem.** Equity in an existing valuable company can be a taxable event for you on day one. Use a profits-only interest or a new-co both parties contribute into, and flag it for a CPA. Do not hand-wave this.

5. **Selling the thing instead of the transformation.** The owner undervalues themselves because they are focused on the thing they sell (the product, the service, the event). Your job is to be the other eye and sell the transformation ladder worth far more. If your pitch is about the thing, you have missed the point.

6. **Forcing CFE on an owner who wants to sell.** If they actually want out, this is an acquisition, not a consulting engagement. Do not talk a seller out of selling — run the AQ Score and the funnel instead.

## Output

A consulting-for-equity case for one owner: the named upside levers ("the other eye"), a consulting deliverables scope, a 10/10/10 equity structure (greater of 10% of profits or $10k/month, plus 10% of exit) with a performance-vesting trigger tied to a baseline, the tax path flagged for a CPA, and a staged partnership pitch ready for your review. Save it as `cfe-<business-name>-YYYY-MM-DD.md` in your acquisitions folder. This turns a "not ready to sell" into permanent equity — and keeps the door open for a future acquisition.

*Note: the KB also references a higher "20/20/20" CFE variant, but the downloaded materials do not state its terms — do not invent them. 10/10/10 is the documented default; treat 20/20/20 as an open item to confirm against the source before using.*
