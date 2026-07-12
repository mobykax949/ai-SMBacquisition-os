# Lesson 01 — Set Up My Workspace

*The front door. Run this first, right after installing the plugin — before any other skill.*

Reading time: ~7 min · Track: Both · Prerequisite: none (this is the beginning)

---

## What this does

You just installed the plugin and have the full skill pack, but Claude knows nothing about you. This skill fixes that in one sitting. It interviews you — who you are, what you have, what you need this business to pay you — then writes three files that make every other skill smarter: your acquirer profile, a first-draft buy box, and a set of Project instructions you paste once so Claude remembers you in every conversation. It ends by placing you in a journey stage and naming the next skill to run. You never again re-explain your situation at the start of a chat.

**You'll walk away with:** `my-profile.md`, `buy-box.md`, and `project-instructions.md` in your Acquisitions folder, a Claude Project loaded with all three, and your journey stage named.

---

## Step 1 — Install the plugin (one time, gets you every skill)

You do not install skills one at a time. They all ship in the SMB Wealth Builder plugin — install it once and every skill is available. No terminal; it is all point-and-click.

1. In Claude Desktop, click **Customize** in the left sidebar and open the **Plugins** tab.
2. Click the **+** (top-right) → **Add marketplace**, and paste: `mobykax949/ai-SMBacquisition-os`
   > Don't search "marketplace" in the search box — it's a source you *add* with the **+** button, not a plugin you search for.
3. Find **smb-wealth-builder** in the list, click **Install**, and choose **User** scope. (Not showing yet? Hit the **↻ refresh** icon.)
4. Start a NEW Cowork conversation and type `/` — the skills appear.

**Done when:** typing `/setup-my-workspace` in a fresh Cowork chat shows the skill.

---

## Step 2 — Give Claude what it needs

- Cowork mode selected, **"Ask before acting"** on, and a work folder authorized. If you don't have one, just ask Claude to create a folder called `Acquisitions` — that is where your files will live.
- Nothing to pre-load — this is the first skill in the system.
- Have honest numbers ready: cash you can actually invest, whether you can get an SBA loan, the annual income (owner cashflow / SDE) you need a business to pay you, your industries of interest, geography, and hours per week.

---

## Step 3 — Run it (copy this)

```
/setup-my-workspace
```

Claude interviews you one question at a time — ownership status, capital, financing readiness, required income, background, industries, geography, hours, risk, 5-year goal — then writes the three files and tells you your stage. Want to steer it? Add specifics:

```
Run the setup-my-workspace skill. Interview me one question at a time. When you have my answers, write my-profile.md, buy-box.md (anchor the size on the SDE I need — reverse-engineer the revenue range from that number), and project-instructions.md to my Acquisitions folder. Then tell me my journey stage and which skill to run next.
```

*Under the hood* the buy box is built **backward from your required income** — the EPIC move. Need $300K SDE in a vertical that pays owners ~$150K? You are hunting $3M+ revenue businesses, not $1M ones.

---

## What Claude creates

| File / output | What it is |
|---|---|
| `my-profile.md` | Your acquirer profile: ownership status, capital, financing readiness, skills, geography, hours, risk, goal — plus your journey stage |
| `buy-box.md` | First-draft buy box anchored on your required income/SDE: industries, size, geography, deal structure, red flags |
| `project-instructions.md` | A short set of custom instructions you paste once into a Claude Project so it remembers all of this in every future chat |
| A next step | Your journey stage and the name of the next skill to open |

**How it works:** the interview captures facts, not hopes, and turns them into files every other skill reads. The buy-box builder pre-fills from your profile, the deal-stacker already knows your capital, and the Deal Advisor knows your situation. The Project step is what makes it permanent — paste-once memory instead of re-explaining yourself every chat.

---

## Step 4 — Test it, refine it, stack it

**Test** (make sure the memory took):
```
What are my acquisition criteria, my required SDE, and my journey stage? Answer from my profile and buy box — if you cannot see those files, say so.
```

**Refine** (whenever your situation changes):
```
My situation changed: [what happened — new capital, a move, sold something]. Re-run the setup interview where needed, rewrite the three files, and tell me if my journey stage changed.
```

**Stack it:** the next skill confirms the stage this one assigned.
```
Run the journey-navigator skill using my-profile.md. Confirm my journey stage, argue the strongest alternative, and tell me the trade-off.
```

---

## Tips & troubleshooting

- **Don't skip this and jump to a skill.** Without your profile and buy box, every other skill starts by asking you the same questions. Ten minutes here saves an hour later.
- **Answer with facts, not hopes.** State the capital you have and the loan you can actually get. A buy box built on wishful numbers points you at businesses you cannot buy.
- **Actually paste the instructions into a Project.** If you skip the Project step, Claude forgets you the moment the chat ends. The whole point is paste-once memory.
- **Treat the buy box as a draft.** This first version is a starting point — the buy-box-builder skill refines it against real verticals and real listings later.

---

## Where this fits

This is the single front door of the whole system — Phase 0. It does setup *and* orientation in one sitting. From here: **Lesson 02 (claude-acquisition-setup)** wires the Project plumbing, then **Lesson 02b (journey-navigator)** pressure-tests the stage this skill assigned before you commit outreach hours or capital.
