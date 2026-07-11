# Lesson 03 — The Buy-Box Builder

*Define exactly what you buy and what you pass — anchored on the income you need, stress-tested against real listings.*

Reading time: ~9 min · Track: Acquire · Prerequisite: `journey-navigator` (Lesson 00)

---

## What this does

A vague filter ("I want to buy a small business") wastes months. This skill builds a disciplined one. It starts from the number that matters — the annual SDE you need the business to pay you — and reverse-engineers the revenue range that produces it (the EPIC move: the box is built backward from your required number, not forward from a listing you liked). Then it defines criteria across three lanes (conservative / target / aggressive), scores 8–10 verticals on five factors, and stress-tests the finished box against ten real listings so you know it is tight enough to kill bad deals and wide enough to feed the funnel.

**You'll walk away with:** a ranked vertical list with composite scores, a 1-page `buy-box.md`, and a stress-test table showing how many of 10 real listings pass.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/buy-box-builder` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- In Project knowledge: `my-profile.md` (it pre-fills your capital, geography, hours) and the draft `buy-box.md` from Lesson 01.
- Have ready: the SDE you need per year, your 5-year net-worth goal, 8–10 candidate verticals (or let Claude propose them), and any hard passes (businesses you would never touch).
- If you have 1031 exchange equity, know the amount — it forces a separate real-estate track with a hard clock.

---

## Step 3 — Run it (copy this)

```
/buy-box-builder
```

Or steer it with your specifics:

```
Build my acquisition buy box. Income I need it to pay me: $[X] SDE/year, 5-year net-worth goal $[Y]. Capital: $[Z] plus SBA 7(a). Geography: [area]. Industries I'm drawn to: [list]; would never buy: [list]. Anchor the size on my income number, build the three lanes, then score these verticals against the box: [8-10 verticals].
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Three-lane criteria table | Conservative (take today) / target (ideal) / aggressive (stretch), across 8 rows: geography, revenue, SDE, employees, age, owner profile, financing, vertical focus |
| Vertical scorecard | 8–10 verticals scored 1–5 on recurring revenue, fragmentation, boomer ownership, AI-modernization upside, and entry multiple — times your personal interest multiplier |
| `buy-box.md` | The 1-pager: geography, revenue range, SDE floor, age, owner profile, financing, top 3 verticals, 3 auto-pass criteria |
| Stress-test table | 10 real listings run through the box, pass/fail with reasons |

**How it works:** the income anchor sets the floor (need $300K SDE where owners earn ~$150K per $1M revenue? You are hunting $3M+ businesses, not $1M — or a higher-margin vertical). The five-factor scoring finds verticals where the odds stack in your favor: contracted revenue, hundreds of small operators, retirement-age owners, automatable back offices, and entry multiples near the 2.4x owner-op anchor rather than 4x+. The stress-test then proves the box exists in the real market: 3–5 of 10 listings passing is the healthy zone.

---

## Step 4 — Test it, refine it, stack it

**Test** (stress the box against live listings):
```
Web search [BizBuySell] for "[top vertical] [geography] for sale". Pull 10 active listings with revenue, asking price, and SDE where disclosed. Run each through my buy box and return a pass/fail table with reasons. If under 3 pass, tell me which criterion to loosen.
```

**Refine** (every 2–3 weeks as you learn real pricing):
```
Market data update: I keep seeing [vertical] deals at [X]x SDE, not the [Y]x my box assumes. Re-score my verticals with the new multiple data and update buy-box.md.
```

**Stack it:** deep-grade the winner, then hunt.
```
Run the vertical-research skill on my #1 vertical: [vertical] in [geography]. I want the full investor-ready workup before I commit outreach hours.
```

---

## Tips & troubleshooting

- **Don't build the box around one cool deal you saw.** Score verticals objectively first, then filter deals. A box reverse-engineered from a single listing is a rationalization, not a filter.
- **Never skip the stress-test.** It catches impossible boxes — criteria no real listing can satisfy — before you burn weeks of outreach on deals that don't exist.
- **Set the SDE floor from the market, not just your needs.** If you need $300K but your vertical pays owners $150K, the answer is bigger revenue or a different vertical — not wishful screening.
- **Remember the 70% Rule.** Frasier's discipline: you should be able to kill 70% of bad deals in the first conversation. If everything sounds interesting, your box is too loose — tighten until 7 of 10 listings are obvious passes.
- **Keep 1031 money on its own track.** Like-kind rules force 1031 equity into real-estate-based businesses (car wash, laundromat, storage) on a hard 45-day identification / 180-day close clock. Mix the tracks and you'll miss the window chasing operating businesses it can't buy.

---

## Where this fits

First step of the acquisition funnel (Branch B, step 1). The navigator told you *which* play; this defines *what* you hunt. `buy-box.md` feeds every downstream skill — deal-finder, market-monitor, aq-analyzer. Next: **Lesson 04 — Vertical Research** for the deep workup, or straight to **Lesson 05 — Deal Finder** to source targets.
