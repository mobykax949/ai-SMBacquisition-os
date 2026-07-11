# Lesson 10 — The Discovery Interviewer

*The 50-question seller deep dive — with a simulator that role-plays a retiring owner and scores your performance before the real call.*

Reading time: ~9 min · Track: Acquire · Prerequisite: a seller who said yes to a call (`aq-analyzer` go, Lesson 09)

---

## What this does

The discovery call is where deals are won or lost, and most buyers wing it. This skill runs the EPIC 50-question deep dive across six sections — story and motivation, operations, revenue and customers, profitability, marketing and sales, systems and documentation — behind the proven call frame: position yourself as an investor, not a broker (no fees), explain the three-phase process (discovery → valuation → offer), and close with the financials ask and the scarcity lever ("our team vets only about six percent of deals to the next phase"). Nervous? The built-in simulator role-plays a realistic retiring owner, lets you rehearse the whole call, then scores you on rapport, information extraction, and next-step clarity.

**You'll walk away with:** a prioritized question guide for the live call (or a scored rehearsal), and a post-call debrief with red flags and a proceed/renegotiate/walk recommendation.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/discovery-interviewer` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- The seller's name, business name, industry, and approximate size.
- Your AQ scorecard for this target (the yellows become priority questions).
- A decision: rehearse first (simulator) or go straight to the live-call guide. First seller call ever, or high-stakes target? Rehearse.
- For the debrief afterward: your raw call notes.

---

## Step 3 — Run it (copy this)

```
/discovery-interviewer
```

To rehearse, ask for the simulator; to prep the real call:

```
Run the discovery-interviewer skill in live-call mode. Seller: [name], [business], [industry], [size], motivation [if known]. Build my prioritized question guide across the six EPIC sections, top-15 must-ask first, and flag the 3 dealbreaker questions — if those answers are bad, I walk.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Simulator session + scorecard | Claude plays a realistic retiring owner (62–68, values legacy, cautious); after "end simulation," you're scored on rapport, extraction, and next-step clarity |
| Live-call question guide | 15–20 prioritized questions across the six sections, dealbreakers flagged, tailored to the seller's industry |
| The call frame | The opening script: investor-not-broker positioning, the three-phase explanation, agenda setting |
| Post-call debrief | Key facts summarized, rough valuation range (2.4x–4.0x by quality), red flags scanned, proceed / renegotiate / walk |

**How it works:** the six sections map to what valuation will need — you leave the call with revenue, profit, owner role, customer concentration, and financials availability, or you know exactly what's missing. The close is scripted for momentum: three years of financials plus balance sheet and cash flow, sent all at once, with a 5–7 day deadline; the "napkin offer" framing plants the key idea early — the better the terms, the better the offer — which steers sellers toward seller financing before you ever negotiate.

---

## Step 4 — Test it, refine it, stack it

**Test** (rehearse against a hard seller):
```
Run the seller simulator, but make this owner difficult: evasive about financials, anchored on an inflated valuation, emotionally attached. I'll conduct the call. When I say "end simulation," score me on the three dimensions with specific feedback.
```

**Refine** (debrief the real call):
```
I completed the discovery call with [seller]. Notes: [paste]. Summarize key facts, compute a rough valuation range, scan for red flags (concentration >30%, declining trend, unwilling to transition, legal liabilities, no financials, owner-is-the-business), and recommend: proceed to valuation / renegotiate / walk.
```

**Stack it:** greens go to the numbers.
```
The financials arrived. Run the valuation skill on [business]: TTM profit, add-back audit, multiple, and my three prices.
```

---

## Tips & troubleshooting

- **Never skip the frame script.** Interrogating a seller cold makes them defensive. The first 3–5 minutes of framing — who you are, the three phases, investor-not-broker — is what opens them up.
- **Don't demand financials in minute one.** Story and motivation first; after 20–30 minutes of trust, the financials request lands as process, not interrogation.
- **Listen for motivation above all.** "Why are you selling, and why now?" separates serious sellers (retiring, burned out, health) from market-testers. No clear motivation = a deal that drags and dies.
- **Don't rationalize red flags because you like the business.** Concentration over 30%, declining revenue, unresolved liabilities — you can price risk, you cannot erase it. Multiple flags: walk.
- **Never end without a commitment.** Financials by a date, a follow-up call booked, an NDA signed. "I'll think about it" is how deals die; the six-percent scarcity line and a deadline keep momentum.

---

## Where this fits

Branch B, step 5 — the seller deep dive, late-funnel. (Don't confuse the two interviews: `setup-my-workspace` interviews *you*; this interviews *the seller*.) The debrief's facts flow directly into **Lesson 11 — Valuation**; a red-flagged call ends the deal politely and sends you back to the pipeline.
