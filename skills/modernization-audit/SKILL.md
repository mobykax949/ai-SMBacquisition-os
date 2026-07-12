---
name: modernization-audit
description: Use when you need a post-close 30-day AI modernization roadmap that inventories owner dependencies, ranks quick wins by margin impact vs disruption risk, and avoids touching customer relationships in week one.
version: 1.0.0
---

# Modernization Audit

## Overview

The post-acquisition AI modernization planner. This skill generates a 30-day roadmap for modernizing a newly-acquired business using AI tools, automation, and process improvements. It starts by inventorying every owner-dependent task (what only the owner knew how to do, what dies if the owner leaves), then ranks quick-win opportunities by margin impact versus disruption risk. The cardinal rule: nothing touches customer-facing relationships in week one. You stabilize first, modernize second. This skill is for after the deal closes, not before.

## When to Use

Run modernization-audit within the first week of ownership, after you have taken control of the business, met the team, and completed the seller transition handoff. You need a list of the business's current processes (sales, operations, customer service, accounting, marketing), the tools and software in use, and the owner's daily task list (shadowed during transition). If you run this before closing, the recommendations will be speculative. Real modernization planning requires operational access.

**Long-time owners (Stage 1 — you did not just buy this business):** this skill works for you too, with two adjustments. The "task list shadowed during transition" is simply your own week log (run `owner-dependency-audit` to build it — that is the natural first step for an existing owner), and the week-one "stabilize, earn credibility" mandate relaxes because you already have the team's trust. The four-bucket triage, the customer-facing cardinal rule, and the 5-changes-per-month limit all still apply.

## Steps

1. **Inventory the owner dependencies.** During the transition period, shadow the owner and document every task they perform. Note which tasks are (a) critical and customer-facing, (b) critical but internal, (c) administrative overhead, (d) strategic/growth work. Ask the team: "What will break if the owner is unavailable for a week?" Those are your dependencies. Paste this list into Prompt 1.

2. **Categorize tasks by modernization potential.** Claude will sort tasks into four buckets: (A) Automate immediately (low risk, high ROI, no customer interaction), (B) Automate after stabilization (high ROI, moderate risk, requires testing), (C) Delegate to team (not automatable, but should not be owner's job), (D) Keep as-is for now (too risky or too complex to change in month one). Focus on bucket A for the first 30 days.

3. **Rank quick wins by margin impact vs. disruption risk.** For each Bucket A task, estimate the time saved per week, the cost of the AI tool or automation (if any), and the risk of disruption (customer complaints, team friction, errors). Claude will compute a priority score and rank the opportunities. Tackle the top 5 in weeks 2 through 4.

4. **Generate the 30-day implementation plan.** Use Prompt 2. Claude creates a week-by-week roadmap: Week 1 (stabilize, do nothing customer-facing, observe and document), Week 2 (implement top 2 quick wins from Bucket A), Week 3 (implement next 3 quick wins, start training team), Week 4 (measure results, iterate, plan month 2). Each week includes specific actions, owner deliverables, and success metrics.

5. **Execute the plan and track results.** Implement the quick wins. Measure time saved, cost reduced, or revenue lifted. If a change causes problems (team confusion, customer complaints), roll it back immediately. Modernization is iterative. You will get some wrong. The goal is net improvement, not perfection.

6. **Review and iterate for month two.** At day 30, review results with the team. What worked? What failed? What new opportunities appeared? Use Prompt 3 to generate the month-two roadmap. Month two can tackle Bucket B tasks (higher risk, but the business is now stable and you have credibility with the team).

## The Prompts

**Prompt 1: Inventory Owner Dependencies and Categorize for Modernization**

```
I just acquired this business. Here is the owner's task list (documented during transition):

[Paste the task list here. Include: task name, frequency (daily/weekly/monthly), time required, who else knows how to do it (if anyone), customer-facing yes/no, current tool/method used.]

Inventory the owner dependencies. For each task, identify:
1. Is it critical to operations (yes/no)?
2. Is it customer-facing (yes/no)?
3. Can it be automated with AI or software (yes/no)?
4. If automated, what is the risk of disruption (low/medium/high)?
5. Estimated time saved per week if automated or delegated.

Categorize into four buckets:
A. Automate immediately (low risk, high ROI, no customer interaction)
B. Automate after stabilization (high ROI, moderate risk, requires testing)
C. Delegate to team (not automatable, but not owner's job)
D. Keep as-is for now (too risky or complex to change in month one)

For Bucket A, rank by priority (margin impact vs. disruption risk). Return the top 5 quick wins.
```

**Prompt 2: Generate 30-Day Modernization Roadmap**

```
Using the Bucket A quick wins from the inventory, generate a 30-day week-by-week modernization plan:

Week 1: Stabilize (observe, document, meet team, no changes to customer-facing processes)
Week 2: Implement top 2 quick wins from Bucket A
Week 3: Implement next 3 quick wins, train team on new tools
Week 4: Measure results, iterate, plan month two

For each week, specify:
- Actions (what to do)
- Owner deliverables (what I personally must complete)
- Tools or resources needed (software subscriptions, AI tools, training materials)
- Success metrics (how to measure if it worked)

Include the cardinal rule: nothing customer-facing changes in week one. We stabilize first, modernize second.
```

**Prompt 3: Month-Two Planning (Iterate and Tackle Bucket B)**

```
I completed the 30-day plan. Here are the results:

[Paste results: what worked, what failed, time saved, cost reduced, team feedback, customer feedback, new opportunities discovered.]

Generate the month-two roadmap. Include:
1. Refinements to the month-one changes (what needs tweaking)
2. Rollout of Bucket B tasks (higher risk, but business is now stable)
3. Team training and delegation (which tasks can I hand off permanently)
4. Growth experiments (can we use the freed-up time for acquisition marketing, upsells, or new products)

Prioritize by impact. Month two should lift revenue or margin, not just cut costs.
```

## The Loop

Modernization is not a one-time project. It is a continuous process. Month one stabilizes and captures the low-hanging fruit. Month two tackles higher-risk improvements and starts delegating. Month three begins growth experiments (using the owner's freed-up time for customer acquisition, product expansion, or pricing optimization). By month six, the business should be running with minimal owner involvement, documented processes, and a trained team. At that point, it is professionalizing (moving from owner-operated 2.4x SDE to managed 4.0x EBITDA). If you plan to sell in 2 to 3 years, this multiple lift is where you make your money.

## Pitfalls

1. **Changing customer-facing processes in week one.** This is the most common and most expensive mistake. You just bought the business. Customers do not know you. The team does not trust you yet. If you immediately change how orders are taken, how support tickets are handled, or how invoices are sent, customers will complain and the team will resist. Stabilize first. Week one is for observation and documentation only. Week two is when you can start internal changes. Week four is the earliest you touch anything customer-facing.

2. **Automating without training the team.** If you install a new CRM or AI tool without training the team, they will not use it. Or worse, they will use it wrong and create errors. Every automation must include a 30-minute training session and a written SOP. Involve the team in the decision. Ask: "What part of your job is repetitive and annoying?" Then automate that. They will champion the change instead of resisting it.

3. **Over-automating too fast.** Modernization is seductive. You see 20 opportunities and want to tackle them all in month one. This overwhelms the team and introduces too many points of failure. If three automations break simultaneously, you cannot diagnose which one caused the problem. Limit month one to 5 quick wins. Test, measure, stabilize. Then add more in month two.

4. **Ignoring margin impact and focusing only on cost cuts.** Automating the owner's admin tasks (bookkeeping, email, scheduling) saves time but does not grow the business. The real wins are margin-impacting changes: automating lead follow-up (lifts conversion), automating upsell emails (lifts AOV), automating customer retention (reduces churn). Balance cost cuts with revenue lifts. Month one can be cost-focused. Month two should include revenue experiments.

5. **Not measuring results.** If you implement 5 quick wins and do not measure time saved or cost reduced, you have no idea if they worked. Track everything. Use a simple spreadsheet: Task automated, Tool used, Time saved per week, Cost of tool, Net benefit. At day 30, sum the net benefit. If it is positive, you succeeded. If negative, you over-automated or picked the wrong tasks. Measure, iterate, improve.

## Output

You receive a complete owner-dependency inventory categorized into four buckets (automate immediately, automate later, delegate, keep as-is), a prioritized list of the top 5 quick wins ranked by margin impact vs. disruption risk, and a 30-day week-by-week implementation roadmap. The roadmap includes specific actions, owner deliverables, tools needed, and success metrics. At day 30, you receive a month-two planning document that builds on month-one results and tackles higher-risk improvements. By the end of month two, you should have freed up 10 to 20 hours per week of the owner's time (your time), documented the core processes, and lifted margin or revenue by at least 5 percent. If you achieve this, the business is on the path to professionalization and multiple expansion.
