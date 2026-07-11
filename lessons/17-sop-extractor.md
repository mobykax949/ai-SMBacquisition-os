# Lesson 17 — The SOP Extractor

*Get the process out of your head and onto paper — one dependency at a time, until someone else can run it.*

Reading time: ~8 min · Track: Modernize · Prerequisite: `owner-dependency-audit` (Lesson 16)

---

## What this does

The dependency audit showed you what only you know how to do; this skill performs the operational transfer. Claude interviews you about one dependency at a time, asking the questions a new employee would need answered: what triggers the process, what's the first step, what tools, what decisions along the way, what goes wrong, how do you know it's done right. The output is a two-part deliverable per dependency: the full narrative SOP (for training and reference) and a one-page checklist version (for daily execution). Loop it weekly until your top-10 risks are documented — that stack of SOPs is what lets you hire a manager, take a vacation, and eventually sell at a managed-business multiple.

**You'll walk away with:** `SOP-<dependency>-v1.0-YYYY-MM-DD.md` — narrative SOP plus one-page checklist — tested on a real person.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/sop-extractor` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- One dependency from your map — high-risk but transfer difficulty 1–3. Don't start with the hardest one; build documentation muscle on easier processes first (your first SOP takes 2 hours, your tenth takes 30 minutes).
- Real recall of the process including the exceptions: the out-of-stock case, the angry-customer branch, the thing you do automatically without noticing.
- A person to test the checklist on — an employee, or a family member if you have no staff yet.

---

## Step 3 — Run it (copy this)

```
/sop-extractor
```

Or name the process:

```
I need to document this process: [e.g. daily job scheduling for the service team]. Interview me step-by-step, ONE question at a time: what triggers it, the first step, every step in order, the decisions at each step, common mistakes, how I handle exceptions, and how I know it's done correctly. Then compile the full process with all branches.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Narrative SOP (2–3 pages) | Purpose, scope (when to use and when NOT), materials and tools, numbered steps with decision branches, quality checks, troubleshooting, escalation rules |
| One-page checklist | Checkbox steps with IF/THEN branch callouts and a final quality check — lives on a clipboard or shared doc |
| Version trail | `SOP-<name>-v1.0-YYYY-MM-DD.md`; revisions increment the version so improvements are traceable |

**How it works:** the interview is the trick. Written from memory, your SOP skips steps and assumes knowledge, because you know too much. Interviewed as if teaching someone who knows nothing, the branches and exceptions surface. Then the test closes the loop: hand the checklist to someone who has never done the process, watch without coaching, note where they stall, revise. Done when they complete it correctly using only the page.

---

## Step 4 — Test it, refine it, stack it

**Test** (the human trial):
```
[Name] just ran the checklist while I observed. They got stuck at: [where and why]. Revise both the narrative SOP and the checklist to close those gaps, and bump the version.
```

**Refine** (keep them current):
```
This process changed: [what's different — new tool, new step, new exception]. Update SOP-[name] to v[next], keep the old version for reference, and flag anything else in my SOP library that this change touches.
```

**Stack it:** loop until the top risks are covered.
```
Mark [dependency] documented on my owner-dependency-map. What's the next highest-risk, lowest-difficulty dependency to extract? Start the interview.
```

---

## Tips & troubleshooting

- **Never write the SOP from memory.** You'll skip steps and assume context. The interview forces the explain-it-to-a-stranger discipline. Every time.
- **Keep it short.** Narrative over 3 pages doesn't get read; checklist over 1 page doesn't get used. A genuinely complex process becomes two SOPs, not one long one.
- **Always test with a real person.** The SOP makes perfect sense to you because you already know it. A first-timer finds five gaps you can't see.
- **Document by risk, not by ease.** Three hours on the office-supplies ordering process is three hours wasted. High-risk, high-frequency first — those are the ones that bite when you're unavailable.
- **Store SOPs where the team lives.** A folder on your desktop helps no one. Shared drive, Notion, printed and laminated on the wall — visible and findable without asking you.

---

## Where this fits

Branch A, step 3 — the execution loop of the modernize track. One dependency per week: 12 SOPs in three months, 25 in six, at which point the business can run without you for a week and a GM hire becomes realistic. Each documented process raises your score in **Lesson 20 — The Multiple Builder**. Next up in parallel: **Lesson 18 — The Margin Finder**.
