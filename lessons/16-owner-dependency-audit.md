# Lesson 16 — The Owner Dependency Audit

*A week-in-the-life interview that maps every decision, task, and relationship running through you — the foundation of the whole modernize track.*

Reading time: ~8 min · Track: Modernize · Prerequisite: `modernization-audit` (Lesson 15), or run directly if you own an owner-dependent business

---

## What this does

You cannot remove yourself from daily operations until you know exactly where you're embedded. Claude shadows you through a normal operating week — one question at a time, Monday through Friday — logging every decision only you could make, every question the team brought you, every relationship that depends on you personally. It categorizes the dependencies into six buckets (sales, pricing, scheduling, quality, vendor relations, tribal knowledge), scores each 1–5 on transfer difficulty, and ranks them by business risk: what breaks first if you're unavailable for a week. The output map drives the SOP extractor, the margin finder, and the multiple builder.

**You'll walk away with:** `owner-dependency-map-YYYY-MM-DD.md` — the full categorized list with transfer scores, the top-10 risk ranking, and a recommended delegation sequence.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/owner-dependency-audit` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- A representative week to audit: normal volume, normal problems. Not a trade-show week, not year-end close, not a crisis.
- Honest recall of your days: first task each morning, every "only I could decide this" moment, every team question, what you took home.
- 45–60 minutes for the interview — it documents at least 30 distinct owner tasks before it stops.
- (If your business already runs without you for weeks: skip this and go to margin-finder or customer-engine.)

---

## Step 3 — Run it (copy this)

```
/owner-dependency-audit
```

Or start the interview directly:

```
Act as a business analyst shadowing me for one week. Ask ONE question at a time, Monday through Friday: my first task each day, the first customer or team interaction, the problems only I could solve, the decisions only I could make, what the team asked me, and what I deferred. Then compile at least 30 owner-dependent tasks and categorize them into: sales, pricing, scheduling, quality, vendor relations, tribal knowledge.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Categorized dependency list | Every task in one of six buckets, with frequency, criticality, and whether anyone else can do it |
| Transfer-difficulty scores | 1 (checklist-delegable) to 5 (owner-unique relationship or judgment that may never transfer cleanly) |
| Top-10 risk ranking | What breaks the business fastest if you disappear: frequency × criticality × no-backup |
| Delegation sequence | The order of attack: high-risk + low-difficulty first (fast risk reduction), high-risk + high-difficulty last |

**How it works:** the interview format matters — asked to list your dependencies cold, you'd name eight; walked through the actual week, you surface thirty, because the invisible ones live inside routine moments. The scoring separates "needs a checklist" from "needs a cultural change," and the risk ranking keeps you from spending a month documenting low-stakes processes while the thing that actually breaks the business stays in your head. A business where the owner works 60 hours and everything routes through them is a 2.4x business; the map shows the gap to 4.0x in concrete tasks.

---

## Step 4 — Test it, refine it, stack it

**Test** (hunt the invisible dependencies):
```
Probe specifically for tribal knowledge: undocumented workarounds I do automatically, vendors who only deal with me, customers who only trust me, and anything not on my calendar that would surprise a new manager. Add at least 5 items to the map.
```

**Refine** (quarterly re-run):
```
Here is my dependency map from last quarter: [paste]. Since then I've: [SOPs written, hires made, automations shipped]. Re-score everything, show me what moved, and update the top-10 risk list.
```

**Stack it:** the map feeds documentation.
```
Take the top 3 high-risk, low-difficulty dependencies from my map and queue them for the sop-extractor skill — one per session, starting with [dependency].
```

---

## Tips & troubleshooting

- **Audit a boring week.** A crisis week overweights firefighting and underweights the normal operations that actually define your dependency.
- **Capture decisions, not just tasks.** "I answered the phone" is a task. "Only I knew whether to discount the quote" is the dependency. Decisions are the hard part to transfer.
- **Low-skill does not mean zero work.** A transfer-score-1 task still needs its checklist written. Verbal handoffs get forgotten or done wrong.
- **Hunt tribal knowledge explicitly.** It never appears on a calendar: the workaround, the relationship, the judgment call. If the interview surfaced fewer than 5 tribal items, it missed them — probe again.
- **The map is diagnostic, not the deliverable.** Filing it and doing nothing reduces zero dependencies. The next step is always: top 3 into the SOP extractor.

---

## Where this fits

Branch A, step 2 — the map everything else in the modernize track executes against. Feeds **Lesson 17 — The SOP Extractor** (document one dependency at a time) and **Lesson 20 — The Multiple Builder** (track dependencies eliminated per quarter).
