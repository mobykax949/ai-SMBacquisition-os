# Lesson 15 — The Modernization Audit

*Your first 30 days as an owner: inventory what only the old owner knew, rank the quick wins, touch nothing customer-facing in week one.*

Reading time: ~8 min · Track: Modernize · Prerequisite: you own the business (post-close), or you're a Stage 1 owner-operator starting Branch A

---

## What this does

The post-acquisition AI modernization planner. It starts by inventorying every owner-dependent task (what dies if the owner leaves), sorts them into four buckets — automate immediately, automate after stabilization, delegate to team, keep as-is for now — and ranks the immediate bucket by margin impact versus disruption risk. Then it generates a week-by-week 30-day roadmap under the cardinal rule: nothing touches customer-facing relationships in week one. You stabilize first, modernize second. This is the first move of the Scalable-with-AI track — the "professionalize it" step on the path from a 2.4x owner-operated multiple toward 4.0x.

**You'll walk away with:** a categorized owner-dependency inventory, a top-5 quick-win list, and a 30-day week-by-week implementation roadmap with success metrics.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/modernization-audit` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- Operational access: run this in the first week of ownership, after meeting the team and starting the seller handoff — not before closing (pre-close recommendations are speculation).
- The owner's documented task list from shadowing them during transition: task, frequency, time required, who else can do it, customer-facing yes/no, tool used.
- The team's answer to one question: "What breaks if the owner is unavailable for a week?"
- The current tool inventory: what software the business actually runs on.

---

## Step 3 — Run it (copy this)

```
/modernization-audit
```

Or start with the inventory:

```
I just acquired this business. Here is the owner's task list from the transition: [paste — task, frequency, time, backup, customer-facing y/n, tool]. Inventory the owner dependencies, categorize into the four buckets (automate now / automate after stabilization / delegate / keep as-is), rank Bucket A by margin impact vs. disruption risk, and give me the top 5 quick wins.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Dependency inventory | Every owner task rated: critical y/n, customer-facing y/n, automatable y/n, disruption risk, time saved per week |
| Four buckets | A: automate immediately (low risk, high ROI, no customer contact) · B: automate after stabilization · C: delegate · D: keep as-is for month one |
| Top-5 quick wins | Bucket A ranked by margin impact vs. disruption risk |
| 30-day roadmap | Week 1 stabilize and observe · Week 2 top 2 quick wins · Week 3 next 3 + team training · Week 4 measure and plan month two — with actions, deliverables, tools, and success metrics per week |

**How it works:** week one exists because customers don't know you and the team doesn't trust you yet — change how orders or support work on day three and you burn both at once. The quick-win ranking keeps month one honest: five changes maximum, each measured (time saved, cost, net benefit), each with a rollback if it breaks. Month two graduates to Bucket B and revenue-lifting experiments, once stability has bought you credibility.

---

## Step 4 — Test it, refine it, stack it

**Test** (pressure-test the bucket sort):
```
Challenge your own categorization: which Bucket A item is most likely to blow up in my face, and why? Which Bucket D item could actually move to B sooner? Re-rank if needed.
```

**Refine** (day 30 review):
```
30-day results: [what worked, what failed, time saved, team and customer feedback]. Generate the month-two roadmap: refinements, Bucket B rollout, permanent delegations, and one growth experiment. Month two should lift revenue or margin, not just cut costs.
```

**Stack it:** the inventory feeds the deeper audits.
```
Run the owner-dependency-audit skill next — a full week-in-the-life interview to catch the dependencies the task list missed, especially tribal knowledge.
```

---

## Tips & troubleshooting

- **Nothing customer-facing in week one.** The most expensive mistake a new owner makes. Week one is observation and documentation; week four is the earliest customer-touching change.
- **Every automation ships with training.** A new tool without a 30-minute session and a written SOP gets ignored — or used wrong. Ask the team "what part of your job is repetitive and annoying?" and automate that first; they'll champion it.
- **Five quick wins, not twenty.** Three simultaneous broken automations can't be diagnosed. Test, measure, stabilize, then add.
- **Balance cost cuts with revenue lifts.** Automating the owner's admin saves hours; automating lead follow-up and win-back lifts the top line. Month one can be cost-focused; month two shouldn't be.
- **Measure or you're guessing.** Track every change: tool, time saved, cost, net benefit. A negative sum at day 30 means you over-automated — the data tells you which one to roll back.

---

## Where this fits

The entry point to Branch A — for Stage 1 owner-operators and every buyer post-close. The full Branch A chain: modernization-audit → **Lesson 16 — Owner Dependency Audit** → sop-extractor → margin-finder → customer-engine → multiple-builder. This is the loop that turns a 2.4x business into a 4.0x one.
