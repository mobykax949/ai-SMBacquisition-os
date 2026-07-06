# Lesson Template — [Skill Name]

*Use this structure for every skill lesson. Modeled on Anthropic's use-case
format: task-first, copy-blocks for every action, an output table so the value
is concrete before you run it. Reading time target: 6-10 min. Delete these
italic notes when filling in.*

---

## What this does
*One short paragraph: the job the skill does and the payoff. End with the "it
just works" line — what the user no longer has to do by hand.*

**You'll walk away with:** *the concrete artifact (a file, a scored list, a draft).*

---

## Step 1 — Install the plugin (one time — gets you every skill)
You do not install skills one at a time. They all ship in a single plugin. Install it once and every skill is available. *(Already installed the plugin? Skip to Step 2.)*

1. In Claude Desktop, click **Customize** in the left sidebar and open the **Plugins** tab.
2. Click the **+** (top-right) → **Add marketplace**, and paste: `mobykax949/ai-SMBacquisition-os`
3. Find **smb-wealth-builder** in the list, click **Install**, and choose **User** scope.
4. Start a **new** Cowork chat and type `/` — the skills appear (e.g. `/skill-name`).

**Done when:** typing `/skill-name` in a fresh Cowork chat shows the skill.

> Don't search for "marketplace" in the plugin search box — it's a source you *add* with the **+** button, not a plugin you search for.

---

## Step 2 — Give Claude what it needs
*The context the skill reads before it runs. Usually: your Project, your
my-profile.md, and any data to paste. List exactly what to have ready.*

- Load these into your Project knowledge: *[e.g. my-profile.md, buy-box.md]*
- Have ready to paste: *[e.g. the target's asking price, SDE, assets]*
- Settings: Cowork mode, "Ask before acting" on, a work folder authorized.

---

## Step 3 — Run it (copy this)
*The literal run-prompt in a copy block. Bracketed fill-ins. This is the whole
interaction — no prose telling them what to type.*

```
[The exact RCTF prompt the user pastes, with [bracketed] fill-ins]
```

---

## What Claude creates
*The output table — the Anthropic move that makes value concrete.*

| File / output | What it is |
|---|---|
| `[artifact.md]` | *[what it contains]* |
| `[second artifact]` | *[what it contains]* |

**How it works:** *2-3 sentences on the loop or the logic, plainly.*

---

## Step 4 — Test it, refine it, stack it
**Test:**
```
[a second prompt that exercises the skill on a real example]
```
**Refine:**
```
[a prompt that adjusts the output — the "update the skill" move]
```
**Stack it:** *name the next skill this feeds into.*
```
[a prompt that chains this skill's output into the next skill]
```

---

## Tips & troubleshooting
*3-5 real pitfalls, Cowork-specific where relevant. Pull from the skill's own
Pitfalls section.*

- *[pitfall → fix]*

---

## Where this fits
*One line: where this sits in the 12-part system and what comes before/after.*
