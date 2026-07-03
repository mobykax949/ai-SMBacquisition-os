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

## Step 1 — Install the skill (one click)
1. Download the skill folder: **[skill-name.zip](../downloads/skill-name.zip)**
2. Unzip it. You get a folder named `skill-name` containing `SKILL.md`.
3. In Finder press `Cmd+Shift+G`, go to `~/.claude/skills/`, and drop the folder in.
4. In Claude Desktop (Cowork mode), type `/` — you should see `skill-name` listed.

**Done when:** typing `/skill-name` shows the skill.

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
