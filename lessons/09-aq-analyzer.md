# Lesson 09 — The AQ Analyzer

*The 13-criterion go/no-go screen — Roland Frasier's canonical filter, run in minutes instead of an afternoon.*

Reading time: ~8 min · Track: Acquire · Prerequisite: first contact made (`outreach-engine`, Lesson 08) or a listing in hand

---

## What this does

The Acquisition Qualification Score is the fast filter that decides whether a deal deserves more of your time — run *before* deep valuation, not after. This skill scores a business on the 13 AQ criteria — location, seller finance, broker, long listing, margin, history, FF&E, multiple, leased space, own property, staff, inventory, training — rating each green (confirmed favorable), yellow (unknown — an information gap to close, not a no), or red (confirmed unfavorable). It returns a go / pass / dig-deeper verdict plus the two highest-leverage questions for the next seller call. Note the honest limit: the source material teaches the scoreboard by demonstration, not with a numeric point table — green-heavy means pursue; red on a dealbreaker criterion (margin, owner-dependence, books) means pass.

**You'll walk away with:** `aq-score-<business>-YYYY-MM-DD.md` — the 13-row scorecard, verdict, and your two next-call questions.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/aq-analyzer` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- `aq-score.md` in Project knowledge (from Lesson 02) so the criteria definitions are loaded.
- Everything you know about the business: location, revenue or asking price, years operating, broker-listed or not, days on market, profitability estimate, property ownership, employee count, seller training offered. Gaps are fine — they score yellow and become your follow-up questions.
- If deal-finder pre-scored 6 criteria, bring that file; this run completes the other 7.

---

## Step 3 — Run it (copy this)

```
/aq-analyzer
```

Or paste the facts:

```
AQ-score this target: [business name / everything you know — location, revenue, asking price, years in business, broker y/n, days listed, SDE estimate, property owned, employees, training offered]. Score all 13 criteria green/yellow/red with evidence, give me the go / pass / dig-deeper verdict, and the two highest-leverage questions for the next seller call.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| 13-row AQ table | Criterion, rating, evidence, note — the full traffic-light scoreboard |
| Verdict | Go (pursue), pass (walk now), or dig deeper (close the yellows first) — with the biggest risk and biggest opportunity named |
| Two next-call questions | The questions most likely to turn yellows green or red, or to confirm dealbreakers early |
| `aq-score-<business>-YYYY-MM-DD.md` | The dated scorecard — your growing deal library |

**How it works:** the scoreboard front-loads the kill decision. Red on margin (unprofitable), history (young or declining), multiple (asking 5x+ SDE), or staff (100% owner-dependent) are the serious flags; one red is a risk to price, three reds is usually a pass. Yellow is the workhorse rating — "they didn't tell us the EBITDA yet" is a yellow, and the two follow-up questions exist to resolve exactly those. Re-run after each call: deals migrate from yellow-heavy to green-heavy (pursue) or to red (exit), and the date-stamped versions show you how the deal evolved.

---

## Step 4 — Test it, refine it, stack it

**Test** (rank a batch):
```
I have 5 warm leads: [paste one-line summaries]. Run a quick AQ pass on each and rank them by deal quality so I know where my next 5 hours go.
```

**Refine** (after the next call):
```
Update the AQ score for [business]: the seller answered our two questions — [answers]. Re-rate the affected criteria, update the verdict, and save a new dated version.
```

**Stack it:** a "go" moves to the deep dive.
```
[Business] scored go. Run the discovery-interviewer skill: build my prioritized 50-question guide for the deep-dive call, flagging the 3 dealbreaker questions.
```

---

## Tips & troubleshooting

- **Don't rate everything yellow to avoid deciding.** Yellow means you genuinely don't know. "We're barely breaking even" is a red, not a yellow. Honest ratings or the filter is theater.
- **One red is not an automatic pass.** A short lease (red on leased space) with greens elsewhere is a negotiating point — make the extension a condition. Three reds, or a red on a non-negotiable (margin, history, multiple), is when you walk.
- **Don't guess the seller-side criteria before the first call.** Six criteria are pre-scoreable from public data; the other seven need a conversation. Mark them yellow and ask.
- **Save every score outside Claude.** Ten scores in one chat with no files means ten scores lost. The dated files also stop you re-evaluating the same deal three months later.
- **Use the follow-up questions.** A "dig deeper" verdict without asking the two priority questions on the next call wastes the whole analysis.

---

## Where this fits

Branch B, step 4 — the flagship qualification gate, run post-contact (or on any listing worth a look). It embodies the 70% Rule: most deals should die here, fast, so your hours go to the green few. A "go" feeds **Lesson 10 — Discovery Interviewer**; the completed scorecard later feeds **Lesson 11 — Valuation**.
