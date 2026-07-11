# Lesson 07 — The Market Monitor

*A 30-minute Monday scan of on-market listings: your pricing-comps engine and deal safety net.*

Reading time: ~7 min · Track: Acquire · Prerequisite: `buy-box-builder` (Lesson 03)

---

## What this does

On-market is not your primary hunting ground — off-market and broker relationships are — but ignoring it costs you two things: valuation comps and the occasional good deal everyone else missed. This skill runs a weekly web-search scan of BizBuySell, BizQuest, and local broker sites filtered by your buy box, computes asking multiples where SDE is disclosed, flags outliers and motivated sellers (90+ days listed, price cuts, seller financing mentioned), and tells you which 2–3 listings deserve an AQ Score this week. After 4–8 weeks of saved scans, you own a pricing trend dataset to anchor negotiations.

**You'll walk away with:** `market-monitor-YYYY-MM-DD.md` — the weekly filtered table with asking multiples and 2–3 flagged listings — and, over time, a comps library.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/market-monitor` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- `buy-box.md` in Project knowledge (geography, revenue, SDE, top 3 verticals).
- A recurring Monday calendar block, 30 minutes, named "Weekly Market Monitor." The discipline is the product — skip three weeks and you lose the trend line.
- A folder for the scans: `acquisitions/market-scans/`.

---

## Step 3 — Run it (copy this)

```
/market-monitor
```

Or scope the scan:

```
Run the market-monitor skill. Web search BizBuySell, BizQuest, and [region] broker sites for listings in my top 3 verticals, my geography, posted or updated in the last 30 days. Screen against my buy box, compute asking multiples where SDE is disclosed, and flag the top 3 worth an AQ Score this week.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Listings table | Business/description, city, asking price, revenue, SDE, days listed, source — new in the last 30 days |
| Buy-box screen | Pass/fail per listing with the reason (revenue too low, wrong geography, franchise...) |
| Asking-multiple analysis | Asking ÷ SDE per listing, vertical averages, outliers flagged (20%+ below average = potential deal; 50%+ above = will sit) |
| Top-3 flags | The listings worth an AQ Score: under 3.0x asking, 90+ days listed, seller financing mentioned, or real estate included |
| `market-monitor-YYYY-MM-DD.md` | The dated scan — your growing comps dataset |

**How it works:** each scan is a snapshot; the stack of scans is intelligence. Rising asking multiples mean the market is heating; lengthening days-listed means sellers are getting realistic. A listing that appears in four consecutive scans with no price movement is an unmotivated seller; one that cuts 20% between week 2 and week 3 is a call-the-broker-today signal — price cuts attract offers within days.

---

## Step 4 — Test it, refine it, stack it

**Test** (mine the multiples):
```
From this week's scan, calculate the asking multiple for every listing with disclosed SDE. What's the average per vertical? Flag anything priced 20%+ below its vertical average.
```

**Refine** (after 4 weeks of scans):
```
Here are my last 4 weekly scans: [attach files]. What's trending — multiples, days listed, seller financing frequency? Should I adjust my buy box or shift verticals?
```

**Stack it:** flags go straight to qualification.
```
Run the aq-analyzer skill on this week's top flagged listing: [paste listing details]. Same-day — on-market deals move fast after a price cut.
```

---

## Tips & troubleshooting

- **Don't make on-market your primary channel.** Public listings are shopped to every buyer with a checkbook. This is the safety net and the comps engine; deal-finder and broker-finder are the hunt.
- **Stay inside the box.** The cool $8M restaurant two counties over is a two-hour distraction, not a deal. The buy box exists to keep you disciplined.
- **Save every scan.** Unsaved scans mean no trend data and re-evaluating deals you already passed on. Date-stamp and file every one.
- **Weekly, not monthly.** Motivated sellers who cut price and add financing get offers within days. A monthly check means you're always too late.
- **Follow through on the flags.** Flagging 3 listings a week and never AQ-scoring them is market research, not deal sourcing.

---

## Where this fits

Branch B, step 2 — the on-market lane of the three sourcing lanes, and the source of the comps you'll cite in every negotiation. Next: **Lesson 08 — Outreach Engine** turns your sourced lists into conversations.
