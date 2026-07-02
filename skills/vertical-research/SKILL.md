---
name: vertical-research
description: Use when you need a full industry workup on an acquisition vertical — the investor-ready report that grades the market, sets the buy box, and delivers a go/pass verdict. Run before committing outreach hours or capital to a vertical.
version: 1.0.0
---

# Vertical Research

## Overview

Before you spend a hundred outreaches on a vertical, spend thirty minutes grading it. This skill runs a full industry workup using Claude web search and delivers an investor-ready report: market structure, fragmentation, succession dynamics, unit economics, live comps, a three-lane buy box with pro formas, a ten-item red-flag check, and a go / pass / dig-deeper verdict. The output is written to hand to a lender, a co-investor, or a partner without rewriting.

## When to Use

- A new vertical is on your list and you need to know if it deserves outreach hours
- An SBA lender or co-investor asks "why this industry?"
- Two verticals compete for your attention and you need them graded the same way
- Before the buy-box builder locks criteria for a vertical you haven't studied

## Steps

1. **Name the vertical and geography.** Be specific: "commercial kitchen hood cleaning in Orange County, CA," not "cleaning services." Done when the scope fits one sentence.

2. **Run the workup prompt (Prompt 1).** Claude web-searches market size, consolidation activity, operator density, typical economics, and live asking-price comps. Expect 10-15 minutes for a thorough pass. Done when every report section below has real content or an honest "could not verify."

3. **Stress-test the draft (Prompt 2).** The report will lean optimistic on first pass — every market looks good when you want it to. The stress-test argues the bear case. Done when at least three genuine risks are named with evidence.

4. **Score the verdict.** Go / pass / dig-deeper, with the two facts that most drove it. Done when you can defend the verdict to a skeptic in under a minute.

5. **Save and reuse.** Save as `research/<vertical>-workup.md` (or HTML for sharing) in your Project. It feeds the buy-box builder, the lender package, and the partner deck. Done when the file is in project knowledge.

## The Prompts

**Prompt 1: The Industry Workup**

```
Act as a private-equity industry analyst preparing an acquisition research report for an investor audience. Use web search throughout and cite sources.

Vertical: [kitchen hood cleaning] · Geography: [Orange County, CA]

Build the report in these sections:
1. INDUSTRY OVERVIEW — what the service is, who buys it, market size and growth (national + this geography), demand drivers.
2. MARKET STRUCTURE — operator count in geography, franchise vs independent mix, fragmentation, consolidation state: who is rolling this up already and what multiples are platforms paying?
3. SUCCESSION DYNAMICS — typical owner profile and age, owner-dependency patterns, signs of a retirement wave.
4. UNIT ECONOMICS — typical revenue and SDE per operator, margin profile, recurring vs project revenue split, pricing norms.
5. LIVE COMPS — current asking prices and multiples from public listing pages for this vertical (this geography first, then comparable markets).
6. REGULATORY & MOAT — mandates that force demand (codes, licensing, compliance cycles), barriers to entry.
7. THREE-LANE BUY BOX — conservative / target / aggressive criteria for this vertical, with a simple pro forma for each lane (price, structure, year-one cash flow) at conservative, realistic, and optimistic scenarios.
8. TEN-ITEM RED-FLAG CHECK — the ten things most likely to make deals in this vertical fail, each rated present/absent/unknown for this market.
9. VERDICT — go / pass / dig-deeper, the two facts that drove it, and the specific questions to answer before committing capital.

Rules: cite a source for every number. Where you cannot verify, write "could not verify" — never estimate silently. Write for an investor reading cold.
```

**Prompt 2: The Bear Case**

```
Now argue against this vertical. Take the report you just wrote and make the strongest honest case that acquiring in [vertical] in [geography] is a mistake: labor exposure, customer concentration patterns, technology or regulatory disruption, hidden capex, why the smart money might be avoiding it. Then revise the verdict if the bear case changed it, and update the red-flag check.
```

**Prompt 3: The Investor One-Pager**

```
Condense the final report into a one-page investor summary: the thesis in three sentences, the five numbers that matter, the buy box, the verdict, and the top three risks with mitigations. Format as a clean HTML page I can share.
```

## The Loop

Workup → bear case → revised verdict → one-pager. Re-run the comps section quarterly if you stay in the vertical — asking multiples move.

## Pitfalls

1. **Skipping the bear case.** The first draft always leans yes. The stress-test is where the report earns trust — a lender will do this to your numbers anyway; do it first.
2. **Accepting unsourced numbers.** If Claude states a market size without a citation, ask for the source. "Could not verify" in the report is a strength, not a weakness.
3. **National numbers, local decision.** A great national market can be saturated or empty in your county. Weight sections 2, 3, and 5 (local structure, succession, local comps) over section 1.
4. **Grading one vertical in isolation.** The verdict sharpens when two verticals are graded side by side with the same rubric. Run this per vertical, then compare.
5. **Treating the report as permanent.** Comps and consolidation state move. Date the report; re-check before acting on one older than a quarter.

## Output

`research/<vertical>-workup.md` — the full nine-section report — plus the one-page investor summary (HTML). Feeds: buy-box-builder, lender/SBA package, co-investor conversations, and your build-in-public content ("what we learned about [vertical]").
