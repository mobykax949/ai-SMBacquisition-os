# Lesson 00 — The Journey Navigator

*Run this before any other skill. It tells you which play you're actually running.*

Reading time: ~8 min · Track: Both · Prerequisite: Cowork set up (Guide 01b)

---

## What this does

Not every buyer should run the same play. An owner modernizing their existing business hunts differently than a first-time searcher, and a searcher chasing a platform company runs a different strategy than one collecting bolt-ons or marketing assets. The Journey Navigator interviews you, writes your acquirer profile, places you in one of five journey stages, and hands you the exact strategy and skill path that fits. Run it once and every other skill reads the profile it produces, so you stop getting generic answers and start getting answers built around your capital, your geography, and where you actually are.

**You'll walk away with:** `my-profile.md` — a saved file with your acquirer profile, your journey stage, your chosen strategy (and the strongest alternative), and the ordered list of skills to run next.

---

## Step 1 — Install the skill (one click)

1. Download the skill: **[journey-navigator.zip](../downloads/journey-navigator.zip)**
2. Unzip it. You get a folder named `journey-navigator` containing `SKILL.md`.
3. In Finder press `Cmd+Shift+G`, type `~/.claude/skills/`, press Enter (create the `skills` folder if it isn't there), and drop the `journey-navigator` folder inside.
4. In Claude Desktop, click the **Cowork** tab and type `/` — you should see `journey-navigator` in the list.

**Done when:** typing `/journey-navigator` shows the skill.

---

## Step 2 — Give Claude what it needs

- Cowork mode selected, **"Ask before acting"** on, and a work folder authorized (e.g. `~/Acquisitions`).
- Nothing to pre-load — this is the first skill you run, so it has no prerequisites. It creates the profile everything else depends on.
- Have a few honest facts about yourself ready: your available capital, whether you own a business now, your geography, and how many hours a week you can give this.

---

## Step 3 — Run it (copy this)

```
Run the journey-navigator skill. Interview me one question at a time, wait for my answer, then ask the next. Cover: whether I own a business now, capital available and SBA/financing readiness, my background and operating skills, my geography, hours per week, risk tolerance, and my 5-year goal. Then write my acquirer profile to my-profile.md, place me in a journey stage, and recommend my strategy with the strongest alternative and the trade-off between them.
```

Answer each question honestly — state the capital you *have*, not what you hope to raise. The recommendation is only as good as the inputs.

---

## What Claude creates

| File / output | What it is |
|---|---|
| `my-profile.md` | Your acquirer profile: ownership status, capital, financing readiness, skills, geography, hours, risk, goal |
| A stage placement | One of five: Owner-Operator · Owner-Acquirer · First-Time Searcher · Platform Searcher · Roll-Up Operator |
| A strategy + alternative | Your recommended play (modernize first / bolt-ons / $0-traffic assets / platform search / roll-up) and the road not taken |
| A skill path | The ordered list of which skills to run next, for your stage |

**How it works:** The interview places you on a map of five stages, each with a different best move. An owner whose business still depends on them is told to *modernize first* (the Scalable-with-AI track) before buying anything, because lifting your own business from a 2.4x to a 4.0x multiple is the cheapest deal you'll ever do. A first-time searcher with thin capital is pointed at $0-traffic marketing assets before a platform buy. The profile it writes becomes the shared context every other skill reads, so the buy-box builder pre-fills from it and the deal-stacker already knows your capital.

---

## Step 4 — Test it, refine it, stack it

**Stress-test the recommendation** (make Claude argue the other side):
```
Here is my profile: [paste my-profile.md]. You recommended [strategy]. Argue against it: what does this path assume about me that might be wrong, and what would have to be true for the alternative to be the better play? Then give me your final call.
```

**Re-navigate after anything changes** (a close, a sale, new capital):
```
My situation changed: [what happened]. Here is my current profile: [paste]. Re-run the stage diagnosis, update my-profile.md, and tell me what skill to open next.
```

**Stack it into your next skill:** for most stages the next move is the buy box.
```
Using my-profile.md, run the buy-box-builder skill. Pre-fill my criteria from the profile and score these verticals against it: [your verticals].
```

---

## Tips & troubleshooting

- **Don't skip to the buy box.** A buy box built without a stage diagnosis aims at the wrong target class. The most common expensive mistake is a first-time searcher screening platform companies they can't finance or run.
- **Owner-operators: fix before you buy.** If your business still needs you daily, a second business doubles the dependency, not the income. The navigator will route you to modernize first — follow it.
- **Bolt-on and platform are different screens.** A bolt-on can fail the standalone tests (thin management, one big customer) and still be a great buy for you, because your existing operation supplies what it lacks. Score it as a bolt-on, not a broken platform.
- **Answer with real numbers.** Aspirational capital produces a strategy that doesn't fit. State what you have.
- **Re-run it.** Stages change. After every close, sale, or capital event, run the re-navigate prompt — yesterday's strategy may now be wrong.

---

## Where this fits

This is Skill Zero — it comes before everything. It decides whether you start on the **AI Acquisition track** (buy the next business) or the **Scalable-with-AI track** (modernize the one you own), and in what order. Next stop for most stages: **Lesson 02 — The Buy-Box Builder.**
