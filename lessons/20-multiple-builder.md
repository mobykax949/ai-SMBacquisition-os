# Lesson 20 — The Multiple Builder

*Quarterly proof that modernization pays: track the climb from 2.4x owner-operated SDE toward 4.0x professionally-managed EBITDA — in dollars.*

Reading time: ~8 min · Track: Modernize · Prerequisite: first improvements shipped (Lessons 15–19)

---

## What this does

The cheapest acquisition you'll ever do is the one on the business you already own — Frasier's landscape prices owner-operated businesses at 2.4x SDE and professionally managed ones at 4.0x EBITDA, and this skill tracks your climb between them. Every quarter it re-scores five dimensions: owner-dependency, management depth, documented processes, recurring revenue, and clean financials. It maps your composite score to an estimated multiple, computes enterprise value at current and target multiples, and shows the gap in dollars — $400K SDE at 2.4x is $960K; the same business run at 4.0x on $400K EBITDA is $1.6M. The scoring ladder is this system's own calibration rubric built around Frasier's anchors (a tracking tool, not a Frasier table), but the anchors — and the dollars — are the method.

**You'll walk away with:** a quarterly scorecard (five dimensions, composite out of 50, estimated multiple range), the enterprise-value gap in dollars, and 2–3 prioritized 90-day improvement goals.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/multiple-builder` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- At least one completed improvement to measure (SOPs documented, help hired, an automation shipped, margin lifted). Don't run this in week one — the value is in the quarterly comparison, not the first snapshot.
- Your trailing 12-month SDE or EBITDA.
- Honest answers about hours worked in the business, who can run it for two weeks, how many SOPs are actually *used*, what percent of revenue is predictable, and whether your books would survive a buyer's glance tomorrow.
- Last quarter's scorecard, if this isn't your first run.

---

## Step 3 — Run it (copy this)

```
/multiple-builder
```

Or start the assessment:

```
Run the multiple-builder quarterly assessment. Ask me the questions one at a time across the five dimensions (owner-dependency, management depth, documented processes, recurring revenue, clean financials), score each 1-10, give me the composite out of 50, map me to the multiple ladder, and compute my enterprise value at the current multiple vs. the 4.0x target. My TTM SDE/EBITDA: $[X].
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Five-dimension scorecard | 1–10 per dimension with the evidence behind each score |
| Multiple estimate | Composite score mapped to an estimated range between the 2.4x and 4.0x+ anchors |
| The dollar gap | Enterprise value today vs. at target — the value you can create without buying anything |
| ROI-ranked improvements | Which dimension lifts the multiple most per unit of effort, with one concrete 90-day goal each |
| Quarterly progress report | Old vs. new scores, points gained, multiple change, dollars created, next quarter's focus |

**How it works:** the five dimensions are what a buyer (or lender, or PE fund) actually prices: can it run without you, is there a team, are processes on paper, is revenue predictable, are the books clean. Improvements interlock — documenting processes enables the manager hire, which cuts owner-dependency, which unlocks the managed-business multiple. The quarterly cadence turns modernization from a vibe into a trend line: four quarters of composite scores rising is proof the business is professionalizing, in the same language you'd use to evaluate any acquisition.

---

## Step 4 — Test it, refine it, stack it

**Test** (find the binding constraint):
```
Here are my five scores: [paste]. Which dimension is capping my multiple right now? Rank the five by ROI (multiple lift per unit of effort) and give me one 90-day goal for each of the top two.
```

**Refine** (the quarterly re-run):
```
Last quarter's scores: [paste]. Since then: [SOPs written, hires, automations, margin moves]. Re-score me, show old vs. new per dimension, the multiple change, and the enterprise value created in dollars. Format as a quarterly progress report I can file.
```

**Stack it:** a business that runs without you re-opens the hunt.
```
My composite crossed [35+] and the business runs without me. Re-run the journey-navigator skill: has my stage changed to Owner-Acquirer — and is it time to hunt bolt-ons?
```

---

## Tips & troubleshooting

- **Score honestly.** Twenty SOPs of which fifteen are filed and never used is a 5, not a 20. The skill only works if the trend line is real.
- **Fix the lowest score, not the favorite one.** Clean books at 9 with processes at 2 means the quarter belongs to documentation. The multiple is capped by the weakest dimension.
- **Never skip quarters.** One snapshot proves nothing; four quarters of 18 → 24 → 31 → 38 proves everything — to you, to a lender, to a buyer.
- **Always convert points to dollars.** "Documented 10 SOPs" feels like a chore; "created $150K of enterprise value" is an investment. Run the math every quarter.
- **Modernize years before you sell, not months.** Buyers discount last-minute cleanups. A business run at 4.0x-quality for 18 months holds the valuation; month-23 cosmetics don't.

---

## Where this fits

The final step of Branch A — and the hinge of the whole loop. When the multiple is rebuilt and the business runs without you, you've completed *buy → modernize*; the system sends you back to **Lesson 00 — Journey Navigator** and **Lesson 03 — Buy-Box Builder** to hunt the next one. Buy, modernize, buy again.
