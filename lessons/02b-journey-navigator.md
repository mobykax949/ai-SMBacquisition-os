# Lesson 02b — The Journey Navigator

*Run this right after `setup-my-workspace` to confirm your stage — and re-run it whenever your situation changes.*

Reading time: ~8 min · Track: Both · Prerequisite: `setup-my-workspace` (Lesson 01)

---

## What this does

Not every buyer should run the same play. An owner modernizing their existing business hunts differently than a first-time searcher, and a searcher chasing a platform company runs a different strategy than one collecting bolt-ons or marketing assets. `setup-my-workspace` already interviewed you and placed you in a journey stage. The Journey Navigator confirms it: it stress-tests your placement against the strongest alternative, names the trade-off, and re-diagnoses whenever your situation changes — so the profile every other skill reads always fits where you actually are.

**You'll walk away with:** `my-profile.md` — a saved file with your acquirer profile, your journey stage, your chosen strategy (and the strongest alternative), and the ordered list of skills to run next.

---

## Step 1 — Install the plugin (one time, gets you every skill)

You do not download this skill by itself. It ships in the SMB Wealth Builder plugin with all the others. Install the plugin once and journey-navigator is there. No terminal — it is all point-and-click.

1. In Claude Desktop, click **Customize** in the left sidebar and open the **Plugins** tab.
2. Click the **+** (top-right) → **Add marketplace**, and paste: `mobykax949/ai-SMBacquisition-os`
   > Don't search "marketplace" in the search box — it's a source you *add* with the **+** button, not a plugin you search for.
3. Open **smb-wealth-builder** in the list, click **Install**, and choose **User** scope. (Not showing yet? Hit the **↻ refresh** icon.)
4. Start a NEW Cowork conversation and type `/` — you should see `journey-navigator` (and the rest) in the list.

Already installed the plugin? Skip straight to Step 3.

**Done when:** typing `/journey-navigator` in a fresh Cowork chat shows the skill.

---

## Step 2 — Give Claude what it needs

- Cowork mode selected, **"Ask before acting"** on, and a work folder authorized (e.g. `~/Acquisitions`).
- Your `my-profile.md` from `setup-my-workspace` (Lesson 01) — the front door you run first. If you skipped it, the navigator will interview you from scratch instead.
- Have a few honest facts about yourself ready: your available capital, whether you own a business now, your geography, and how many hours a week you can give this.

---

## Step 3 — Run it (copy this)

The skill is installed, so you just invoke it — it reads the profile `setup-my-workspace` already wrote:

```
/journey-navigator
```

Want to steer it? Add specifics in plain English:

```
Run the journey-navigator skill using my-profile.md. Confirm my journey stage, argue the strongest alternative and the trade-off, then give me your final call and the next skill to run.
```

*Under the hood* it reads your profile, pressure-tests your stage, and updates `my-profile.md` if anything changed — no re-interview from scratch. If your profile is missing (you skipped the front door), it will interview you first.

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

This runs right after `setup-my-workspace` (the front door) to confirm your stage — and again whenever your situation changes. It settles whether you're on the **AI Acquisition track** (buy the next business) or the **Scalable-with-AI track** (modernize the one you own), and in what order. Next stop for most stages: **Lesson 03 — The Buy-Box Builder** (Lesson 02 sets up your Claude Project first if you haven't).
