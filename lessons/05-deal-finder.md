# Lesson 05 — The Deal Finder

*Find off-market targets before they ever list with a broker — the volume engine that feeds your pipeline.*

Reading time: ~9 min · Track: Acquire · Prerequisite: `buy-box-builder` (Lesson 03)

---

## What this does

On-market listings mean competing with ten other buyers at full asking price. This skill hunts the businesses that haven't listed: Claude web-searches a vertical and city, you paste in Google Maps results to enrich the list, and it flags the succession signals — no website (or a dated one), 10+ years in business, plenty of reviews but no online booking. That combination usually means an older owner running a profitable, un-modernized operation on referrals: the acquisition sweet spot. It screens survivors against your buy box, ranks them by succession likelihood, and pre-scores 6 of the 13 AQ criteria before you make first contact.

**You'll walk away with:** a ranked markdown file of 10–15 off-market targets, each pre-scored on 6 AQ criteria — your outreach list.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/deal-finder` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- `buy-box.md` in Project knowledge (the screen the list runs against).
- One vertical + one city per run. Not "service businesses in Southern California" — "kitchen hood cleaning in Irvine."
- A Google Maps tab open: you'll search the same query there and paste 30–50 results (name, address, phone) into the chat. Maps surfaces the old, no-SEO operators web search misses.

---

## Step 3 — Run it (copy this)

```
/deal-finder
```

Or scope it explicitly:

```
Run the deal-finder skill: [vertical] in [city]. Web search for 30+ businesses, then I'll paste Google Maps results to cross-reference. Flag succession signals, screen against my buy box, pre-score the 6 pre-scoreable AQ criteria, and rank by succession likelihood.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Cross-referenced business table | Web search + your Maps paste merged: website status and quality, review count, estimated years in business |
| Succession-signal ranking | Businesses flagged on: no/dated website, 10+ years operating, high reviews but no online booking — ranked by likelihood |
| Revenue screen | Review count + employee signals used as a proxy to flag which targets likely sit in your revenue range |
| AQ pre-score table | 6 of 13 criteria scored green/yellow/red before first contact: location, broker (off-market = green), history, own property, staff, inventory |
| `deal-finder-<vertical>-<city>-YYYY-MM-DD.md` | The final ranked list — your outreach file |

**How it works:** the other 7 AQ criteria (seller finance, margin, multiple, and so on) require a seller conversation, so they stay open until the first call. Pre-scoring the public 6 typically trims a meaningful slice of the outreach list and points your limited call time at real targets. Property ownership is one *you* check — open Google Street View or the county assessor site yourself and tell Claude what you see (Claude can't view Street View) — a standalone building is both a financing asset and a succession signal.

---

## Step 4 — Test it, refine it, stack it

**Test** (enrich with your Maps paste):
```
Here are 40 businesses from Google Maps: [paste]. Cross-reference with your web search results. For each: has website (yes/no), website quality (modern/dated/none), review count, estimated years in business. Rank the flagged succession candidates.
```

**Refine** (when the list is thin):
```
Only [N] candidates passed. Expand the search to [adjacent cities / full county] and re-run the screen. Keep the same buy box.
```

**Stack it:** the list feeds first contact.
```
Take the top 5 from my deal-finder list and run the outreach-engine skill: draft a mailed letter and a LinkedIn request for each, strategic/related-business angle where it fits, staged for my approval.
```

---

## Tips & troubleshooting

- **One vertical per run.** Asking for "service businesses" returns a shallow mess of carpet cleaners, HVAC, and locksmiths with no depth in any of them.
- **Never trust web search alone.** Older businesses with no website or bad SEO are invisible to search — and they are exactly who you're hunting. Always cross-reference the Google Maps paste.
- **No website does not mean failing.** It usually means older owner, referral-driven, profitable, and never needed digital marketing. That is the sweet spot, not a warning.
- **Save the file or lose the list.** A list left in chat scrolls away. Download the markdown and file it under `acquisitions/targets/<vertical>/`.
- **Don't skip the AQ pre-score.** Going straight from list to cold calls wastes conversations on businesses that fail obvious criteria. Pre-score first, call second.

---

## Where this fits

Branch B, step 2 — the sourcing trio's off-market lane (alongside broker-finder and market-monitor). Re-run each vertical every 2–3 months: businesses age into the succession window and circumstances change. Next: **Lesson 06 — Broker Finder** for the pocket-listing lane and **Lesson 07 — Market Monitor** for the on-market comps lane, then **Lesson 08 — Outreach Engine** to make contact.
