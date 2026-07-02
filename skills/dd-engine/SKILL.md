---
name: dd-engine
description: Use when you need to run sequential due diligence after LOI signing, track document requests and findings, apply red-flag rules, and make go/renegotiate/walk decisions per phase.
version: 1.0.0
---

# DD Engine

## Overview

The sequential due diligence runner. This skill guides you through the post-LOI diligence process in phases (financial, operational, legal, customer, and final verification). For each phase, it generates document requests, tracks findings in a structured format, applies red-flag rules (customer concentration above 30 percent, declining revenue trend, unresolved liabilities), and recommends a decision (go to next phase, renegotiate terms, or walk away). Due diligence is where most bad deals die. Use this skill to avoid buying a lemon.

## When to Use

Run dd-engine immediately after the seller signs the LOI. You have a fixed diligence period (typically 30 to 60 days per the LOI). The clock starts on signing day. Do not wait. Launch the first phase (financial diligence) within 48 hours of LOI execution. If you delay, you compress the timeline and miss red flags. You need access to the seller's financials, contracts, customer data, and operational systems. If the seller refuses access to any category, that is itself a red flag.

## Steps

1. **Set up the diligence tracker.** Create a spreadsheet or document with five tabs (Financial, Operational, Legal, Customer, Final Verification). For each tab, list the document requests and findings. Use Prompt 1 to generate the initial request list for Phase 1 (Financial).

2. **Phase 1: Financial Diligence.** Request three years of P&L, balance sheets, cash flow statements, tax returns, bank statements, A/R and A/P aging reports, and loan documents. Verify that the financials match the seller's claims from discovery. Recompute TTM profit. Audit add-backs again. Check for declining trends, seasonality, or one-time windfalls that inflate the numbers. If financials are clean, proceed to Phase 2. If discrepancies exceed 10 percent, renegotiate or walk.

3. **Phase 2: Operational Diligence.** Request employee list (names, roles, tenure, comp), vendor and supplier contracts, lease agreements, equipment list and condition, insurance policies, and operational procedures documentation. Verify that the business can run without the owner. Identify key-person dependencies. Check for unrecorded liabilities (deferred maintenance, warranty claims, pending refunds). If operations are stable, proceed to Phase 3. If owner-dependent or undocumented, renegotiate terms (longer transition, earnout tied to retention).

4. **Phase 3: Legal and Compliance Diligence.** Request entity documents (articles of incorporation, operating agreement, bylaws), IP registrations (trademarks, patents, copyrights), contracts (customer, vendor, employee), litigation history, regulatory compliance records (licenses, permits, OSHA, ADA, tax filings). Verify clean title to assets. Check for liens, encumbrances, or unresolved legal claims. If legal is clean, proceed to Phase 4. If material legal issues exist, walk or renegotiate to exclude liabilities.

5. **Phase 4: Customer and Revenue Diligence.** Request customer list (top 20 customers by revenue, contract terms, payment history), sales data (monthly revenue by customer, churn rate, new customer acquisition), and marketing data (channels, CAC, LTV). Calculate customer concentration (percent of revenue from top customer, top 3, top 10). Apply the red-flag rule: if any single customer exceeds 30 percent of revenue, renegotiate or walk. If top 3 exceed 50 percent, it is high-risk. Verify recurring revenue claims. If customer base is stable and diversified, proceed to Phase 5.

6. **Phase 5: Final Verification.** Conduct site visit. Interview key employees (confirm they will stay). Speak to top 3 customers (if seller permits). Review the last 30 days of bank statements and sales data to confirm no sudden drop-off. Run final red-flag check across all phases. If everything is green, recommend proceeding to closing. If yellow flags exist, list them and propose term adjustments. If red flags exist, recommend walking.

7. **Make the go/renegotiate/walk decision.** After each phase, paste your findings into Prompt 2 (Phase Decision). Claude evaluates the findings, applies red-flag rules, and recommends the next step. If go, move to next phase. If renegotiate, draft the revised terms and present to seller. If walk, exit per LOI terms (you are within the DD period, so no penalty).

## The Prompts

**Prompt 1: Generate Document Request List for Phase [X]**

```
Generate the due diligence document request list for [Phase: Financial / Operational / Legal / Customer / Final Verification]:

Target business: [business name]
Industry: [industry]
Size: [revenue, employees]

For this phase, list:
1. Required documents (must-have to proceed)
2. Preferred documents (nice-to-have, add context)
3. Red-flag indicators (what findings would stop the deal)
4. Timeline (how long this phase should take)

Organize the list as a checklist I can send to the seller or their attorney.
```

**Prompt 2: Phase Decision (Go / Renegotiate / Walk)**

```
I completed [Phase X: Financial / Operational / Legal / Customer / Final] due diligence. Here are my findings:

[Paste findings here. Include: documents received, documents missing, discrepancies vs. seller claims, red flags discovered, yellow flags, green signals.]

Apply the red-flag rules:
- Customer concentration >30% (single customer) or >50% (top 3) = red flag
- Declining revenue or profit trend (>10% YoY drop) = red flag
- Unresolved legal liabilities (pending lawsuits, tax liens, regulatory violations) = red flag
- Owner is the entire business (no team, no systems, no documentation) = red flag
- Financials do not match tax returns (>5% discrepancy) = red flag

Recommend: Go to next phase / Renegotiate terms (specify what to change) / Walk away (explain why).
```

**Prompt 3: Draft Renegotiation Email to Seller**

```
Due diligence uncovered these issues:
- [List the issues, e.g. "Customer concentration is 45% from top 3 customers", "Revenue declined 12% YoY", "Undisclosed equipment lease liability of $30K"]

My original offer was [price and terms]. Given these findings, I want to renegotiate to:
- [State the new terms, e.g. "Reduce price by $100K", "Add earnout contingent on customer retention", "Seller absorbs the lease liability before closing"]

Draft a professional email to the seller explaining the issues, the rationale for the adjustment, and the revised terms. Keep the tone respectful and solution-focused. Remind them that we are still within the DD period per the LOI.
```

## The Loop

Due diligence is sequential. Do not skip phases. Financial diligence must come first because if the numbers are wrong, nothing else matters. Operational and legal can run in parallel after financial is clean. Customer diligence follows operational (you need the employee and contract data to understand customer relationships). Final verification is the last gate before closing. Track everything in the diligence tracker. Update the tracker daily. Share it with your attorney, CPA, and any advisors. If the seller is slow to provide documents, send a reminder every 3 days. If they miss deadlines or refuse to provide key documents, that is a red flag. Consider walking.

## Pitfalls

1. **Skipping phases or rushing to closing.** Buyers who fall in love with a business sometimes skip operational or customer diligence because financial looks good. This is a mistake. A business with great financials but 60 percent customer concentration is a ticking time bomb. If the top customer leaves post-acquisition, revenue collapses. Run all five phases.

2. **Not applying the red-flag rules consistently.** The rules (customer concentration above 30 percent, declining trend, unresolved liabilities) are objective. Do not rationalize them away. If a single customer is 40 percent of revenue, that is a red flag regardless of how much you like the business. Either renegotiate to account for the risk (lower price, earnout tied to retention) or walk.

3. **Accepting the seller's explanations without verification.** Sellers will explain away every discrepancy. "Revenue is down because of COVID but it will bounce back." "That lawsuit is frivolous and will be dismissed." "The equipment works fine, it just looks old." Do not accept explanations. Verify. Request third-party evidence (bank statements, court filings, equipment appraisals). If the seller cannot provide evidence, assume the worst.

4. **Not involving professionals.** Due diligence is not a solo job. You need a CPA to audit the financials, an attorney to review contracts and legal docs, and possibly an industry expert to assess operational risks. Trying to do it all yourself leads to missed red flags. Budget $5K to $15K for professional DD help. It is cheap insurance against a $500K mistake.

5. **Staying in a bad deal because of sunk cost.** You spent 40 hours on discovery, drafted an LOI, paid your attorney $2K, and you are emotionally attached. Then DD uncovers red flags. Walking away feels like failure. It is not. Walking away from a bad deal is success. The LOI is non-binding except for exclusivity. If the deal is bad, walk. There are other deals.

## Output

For each phase, you receive a document request checklist, a findings summary, a red-flag evaluation, and a go/renegotiate/walk recommendation. At the end of the final verification phase, you receive a comprehensive DD report summarizing all findings across all phases, a final red-flag count, and a closing-readiness assessment. If the recommendation is go, you proceed to closing (use your attorney for the closing checklist). If renegotiate, you receive a draft email to the seller with revised terms. If walk, you receive an exit script to deliver the news professionally and preserve the relationship (you may meet this seller again in a future deal).
