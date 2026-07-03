---
name: owner-dependency-audit
description: Use when you need to inventory every decision, task, and relationship that runs through you as the owner. Claude interviews you through a week-in-the-life, categorizes dependencies, and outputs the map that drives everything else in the Scalable with AI track.
version: 1.0.0
---

# Owner Dependency Audit

## Overview

You cannot remove yourself from daily operations until you know exactly where you are embedded. This skill turns your mental model of the business into a structured dependency map. Claude walks you through a week in the life of the business, asking about every decision you make, every task you handle, and every relationship that depends on you. The output categorizes dependencies into six buckets (sales, pricing, scheduling, quality, vendor relations, tribal knowledge), scores each by transfer difficulty (how hard to delegate or automate), and ranks them by business risk (what breaks fastest if you are unavailable). This dependency map is the foundation for the SOP extractor, margin finder, and multiple builder skills. Run this first.

## When to Use

Run owner-dependency-audit when you own a business that depends on you showing up every day, and you need to see exactly where you are stuck before you can unstick yourself. You need at least one normal operating week to shadow (not a holiday week, not a crisis week). If you are considering selling, acquiring, or hiring a general manager, this audit shows you what needs documentation and delegation before the business can run without you. If your business already runs without you for weeks at a time, skip this skill and go straight to margin-finder or customer-engine.

## Steps

1. **Pick a representative week to audit.** Choose a week that looks like most weeks: normal customer volume, normal problems, normal decisions. Not a trade show week, not year-end close, not summer shutdown. You need a week where the business behaves like itself. Done when you can name the week you will shadow.

2. **Run the interview with Prompt 1.** Claude asks one question at a time, building a log of your daily activities. Answer for each day of the week: Monday morning through Friday close (or Saturday if you work weekends). Claude will ask about customer interactions, team questions, vendor issues, financial decisions, and problem solving. Done when Claude has documented at least 30 distinct owner tasks across the week.

3. **Categorize dependencies into the six buckets.** Claude sorts your tasks into sales (closing deals, pricing quotes, customer acquisition), pricing (setting prices, approving discounts, margin decisions), scheduling (assigning jobs, managing capacity, prioritizing work), quality (inspecting output, handling complaints, defining standards), vendor relations (sourcing, negotiating, managing suppliers), and tribal knowledge (things only you know how to do, undocumented processes, relationships only you hold). Done when every task from the interview lands in a bucket.

4. **Score each dependency by transfer difficulty.** Use Prompt 2. Claude rates each task on a 1 to 5 scale: (1) easy to delegate with a checklist, (2) delegate with training and supervision, (3) requires skilled hire or substantial automation, (4) requires cultural change or customer trust transfer, (5) owner-unique relationship or judgment call that may never transfer cleanly. Done when every dependency has a score.

5. **Rank by business risk.** Claude answers: if you were unavailable for a week, which dependencies would break the business first? Revenue stops? Quality collapses? Customers leave? Vendors cut you off? The ranking combines frequency (how often the task happens), criticality (what breaks if it does not happen), and current backup (does anyone else know how to do this). Done when you have a top-10 highest-risk dependency list.

6. **Generate the dependency map.** Use Prompt 3. Claude produces a document with three views: (1) the full categorized list with transfer scores, (2) the top-10 risk-ranked dependencies, (3) the recommended sequence for documentation and delegation (start with high risk + low transfer difficulty, end with high risk + high transfer difficulty). Save this as `owner-dependency-map-YYYY-MM-DD.md`. Done when the file is in your project knowledge and you can see the path forward.

## The Prompts

**Prompt 1: The Week-in-the-Life Interview**

```
Act as a business analyst shadowing me for one week. Ask me ONE question at a time about my activities as the business owner. Cover each day Monday through Friday (or Saturday if I work weekends). For each day, ask:

1. What time did you start working and what was the first decision or task?
2. Walk me through the first customer or team interaction of the day. What did they need from you specifically?
3. What problems came up that only you could solve?
4. What decisions did you make that no one else could make (pricing, hiring, vendor choices, quality calls)?
5. What questions did the team ask you? What would have happened if you were not available?
6. How did the day end? What tasks did you take home or defer to tomorrow?

After I answer for the full week, compile a list of at least 30 distinct owner-dependent tasks. Categorize each into: sales, pricing, scheduling, quality, vendor relations, or tribal knowledge. Show me the categorized list.
```

**Prompt 2: Score Transfer Difficulty**

```
Here is the categorized dependency list from my week-in-the-life interview: [paste the list from Prompt 1].

For each dependency, score the transfer difficulty on a 1 to 5 scale:
1 = Easy to delegate with a written checklist (employee can do it after reading the SOP)
2 = Delegate with training and supervision (requires a few weeks of coaching)
3 = Requires skilled hire or substantial automation (need a specialist or software tool)
4 = Requires cultural change or customer trust transfer (customers expect to deal with the owner)
5 = Owner-unique relationship or judgment that may never transfer cleanly

For each dependency, also estimate: frequency (daily/weekly/monthly), criticality (what breaks if this does not happen: revenue stops / quality fails / customers leave / vendors cut us off / nothing immediate), and current backup (does anyone else know how to do this yes/no).

Return a table with: dependency name, category, frequency, criticality, backup, transfer score.
```

**Prompt 3: Generate the Dependency Map and Delegation Sequence**

```
Using the scored dependency table from Prompt 2, produce the owner dependency map with three sections:

1. Full List: All dependencies grouped by category (sales, pricing, scheduling, quality, vendor relations, tribal knowledge), showing transfer score, frequency, and criticality.

2. Top 10 Risk-Ranked: The dependencies that would break the business fastest if I were unavailable, ranked by composite risk (high frequency + high criticality + no backup = highest risk).

3. Recommended Delegation Sequence: The order to tackle documentation and delegation. Start with high-risk + low-transfer-difficulty (the quick wins that reduce risk fast). End with high-risk + high-transfer-difficulty (the hard ones that take months). For each dependency, suggest: document as SOP, automate with software, delegate to existing team, hire a specialist, or keep as owner role for now.

Format as a markdown document I can save as owner-dependency-map.md.
```

## The Loop

Run the audit once to build the baseline dependency map. Then re-run it quarterly after you have documented SOPs, hired help, or automated processes. Each audit shows you what moved: dependencies that dropped from score 5 to score 2 (you documented the process and trained someone), or dependencies that disappeared entirely (you automated them with software). The map is a living document. As you reduce dependencies, your business becomes more valuable. A business where the owner works 20 hours per week and nothing breaks is worth 4.0x EBITDA. A business where the owner works 60 hours per week and everything depends on them is worth 2.4x SDE. This audit shows you the gap in dollar terms.

## Pitfalls

1. **Auditing an unusual week.** If you shadow yourself during a crisis week (server down, major customer angry, employee quit), the dependency list will overweight firefighting and underweight normal operations. Pick a boring week.

2. **Only listing tasks, not decisions.** The audit must capture decision-making dependencies, not just tasks. A task is "I answered the phone." A decision dependency is "I answered the phone and only I knew whether to discount the quote to close the deal." Decisions are harder to delegate than tasks.

3. **Assuming low-skill tasks are easy to delegate.** A task scored 1 (easy checklist) still requires you to write the checklist. If you skip that step and just tell someone verbally how to do it, they will forget or do it wrong. Every delegation requires documentation.

4. **Not tracking tribal knowledge.** Tribal knowledge is the invisible dependency. It is not a task on your calendar. It is the vendor who only deals with you, the customer who only trusts you, the workaround you do automatically that no one else knows exists. If the interview does not surface at least 5 tribal knowledge items, you missed them. Ask Claude to probe for undocumented processes and unique relationships.

5. **Stopping at the map without acting on it.** The dependency map is diagnostic, not prescriptive. After you generate it, the next step is to pick the top 3 high-risk dependencies and run them through the SOP extractor skill. If you file the map and do nothing, the dependencies do not reduce. The map is only useful if you use it to drive documentation and delegation.

## Output

You receive `owner-dependency-map-YYYY-MM-DD.md` saved to project knowledge. The file contains: (1) the full categorized dependency list with transfer scores, frequency, criticality, and backup status for every owner-dependent task in a normal week; (2) the top-10 risk-ranked dependencies that would break the business fastest if you disappeared; (3) the recommended delegation sequence showing which dependencies to tackle first (high risk, low difficulty) and which to save for later (high risk, high difficulty). This map feeds directly into the SOP extractor (pick a dependency and document it) and the multiple builder (track how many dependencies you have eliminated over time). When your dependency count drops below 10 and your transfer difficulty average drops below 3, your business is ready to run without you.
