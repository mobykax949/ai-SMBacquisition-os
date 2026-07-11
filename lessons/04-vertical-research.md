# Lesson 04 — Vertical Research

*Before you spend a hundred outreaches on a vertical, spend thirty minutes grading it.*

Reading time: ~8 min · Track: Acquire · Prerequisite: `buy-box-builder` (Lesson 03)

---

## What this does

An investor-ready industry workup, on demand. Claude web-searches the vertical and delivers a nine-section report: market structure, fragmentation, succession dynamics, unit economics, live asking-price comps, regulatory moat, a three-lane buy box with pro formas, a ten-item red-flag check, and a go / pass / dig-deeper verdict. Then it argues the bear case against its own report — because the first draft always leans optimistic. The output is written to hand to an SBA lender, a co-investor, or a partner without rewriting.

**You'll walk away with:** `research/<vertical>-workup.md` — the full report — plus a one-page investor summary you can share.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/vertical-research` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- A specific scope in one sentence: "commercial kitchen hood cleaning in Orange County, CA" — not "cleaning services."
- Web search enabled (the report cites sources for every number).
- Your buy box in Project knowledge, so the three-lane criteria section lands in your size range.
- Expect the full pass to take 10–15 minutes of agentic work.

---

## Step 3 — Run it (copy this)

```
/vertical-research
```

Or name the scope directly:

```
Run the vertical-research skill on [vertical] in [geography]. Build the full nine-section investor report — cite a source for every number, and write "could not verify" where you can't, never estimate silently.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| `research/<vertical>-workup.md` | Nine sections: industry overview, market structure, succession dynamics, unit economics, live comps, regulatory & moat, three-lane buy box with pro formas, ten-item red-flag check, verdict |
| The bear case | The strongest honest argument *against* the vertical — labor exposure, disruption risk, hidden capex — with the verdict revised if it changed |
| Investor one-pager | The thesis in three sentences, the five numbers that matter, the buy box, the verdict, top three risks with mitigations (clean HTML) |

**How it works:** the workup prompt forces evidence discipline — every number cited or marked "could not verify" — so the report earns trust with a lender who will stress your numbers anyway. The bear-case pass (Prompt 2 in the skill) is the step that separates research from cheerleading: at least three genuine risks named with evidence before the verdict stands.

---

## Step 4 — Test it, refine it, stack it

**Test** (make it argue against itself):
```
Now argue against this vertical. Make the strongest honest case that acquiring in [vertical] in [geography] is a mistake: labor exposure, customer concentration patterns, technology or regulatory disruption, hidden capex. Then revise the verdict if the bear case changed it.
```

**Refine** (comps go stale):
```
Re-run section 5 (live comps) for [vertical] in [geography] with current listings. Have asking multiples moved since [date of report]? Update the report and re-date it.
```

**Stack it:** feed the verdict back into your box.
```
Using the final [vertical] workup, update my buy-box.md: adjust the entry-multiple assumption and the SDE floor for this vertical, and tell me if it should still be my #1.
```

---

## Tips & troubleshooting

- **Never skip the bear case.** The first draft always leans yes — every market looks good when you want it to. A lender will do this to your numbers anyway; do it first.
- **Don't accept unsourced numbers.** If Claude states a market size without a citation, ask for the source. "Could not verify" in the report is a strength, not a weakness.
- **National numbers, local decision.** A great national market can be saturated or empty in your county. Weight local structure, succession, and local comps over the industry overview.
- **Grade verticals side by side.** The verdict sharpens when two verticals are run through the same rubric. Run this per vertical, then compare.
- **Date the report and re-check.** Comps and consolidation state move. Don't act on a workup older than a quarter without re-running the comps section.

---

## Where this fits

The deep-workup adjunct to the buy box (Branch B, step 1). Run it on your top 1–2 verticals before committing outreach hours or capital — and again whenever a lender or co-investor asks "why this industry?" Next: **Lesson 05 — Deal Finder** to build the target list in the vertical that graded "go."
