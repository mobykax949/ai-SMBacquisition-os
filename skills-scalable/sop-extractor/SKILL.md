---
name: sop-extractor
description: Use when you need to turn the owner's knowledge into documented process. Claude interviews you step-by-step for one dependency from your audit, writes the SOP, and builds the employee checklist version. Loop until your top risks are documented.
version: 1.0.0
---

# SOP Extractor

## Overview

The dependency audit showed you what only you know how to do. The SOP extractor gets it out of your head and onto paper so someone else can do it. This is not academic documentation. This is operational transfer. Claude interviews you about one dependency at a time, asking the questions an employee would need answered: what do you do first, what tools do you use, what could go wrong, how do you know it is done right, what do you do when the exception happens. The output is a two-part deliverable: the full narrative SOP (for training and reference) and the checklist version (for daily execution by an employee). Run this skill on every high-risk dependency from your audit until the knowledge transfer is complete.

## When to Use

Run sop-extractor after you have completed the owner-dependency-audit and identified your top-10 risk-ranked dependencies. Pick one dependency to document at a time. Start with high-risk + low-transfer-difficulty dependencies (the ones scored 1 or 2 on transfer difficulty). Do not start with the hardest dependency (transfer score 5). You need to build documentation muscle on easier processes first. If you have never written an SOP before, your first one will take 2 hours. Your tenth one will take 30 minutes. Practice on the simple stuff.

## Steps

1. **Pick one dependency from your audit to document.** Look at your owner-dependency-map and choose a dependency that is high-risk (business breaks if you are gone) but low-to-medium transfer difficulty (scored 1 to 3). Example: daily job scheduling, weekly vendor order, monthly financial close, customer onboarding process. Done when you have named the specific dependency you will document in this session.

2. **Run the step-by-step interview with Prompt 1.** Claude asks: what is the first step, what happens next, what tools or information do you need at each step, what decisions do you make along the way, what are the common mistakes or edge cases, how do you know the process is complete and correct. Answer in detail. If the process has branches (if this happens, do that), describe every branch. Done when Claude has extracted the full process from start to finish including edge cases.

3. **Generate the narrative SOP.** Use Prompt 2. Claude writes the process as a training document: purpose (why this process matters), scope (when to use it and when not to), materials and tools needed, step-by-step instructions with decision points, quality checks (how to verify it was done right), troubleshooting (what to do when common problems occur), and escalation (when to ask for help). Done when you have a readable document that a new hire could follow.

4. **Build the checklist version.** The narrative SOP is for training. The checklist is for daily execution. Use Prompt 3. Claude condenses the SOP into a one-page checklist: a numbered list of steps with yes/no completion boxes, decision branch callouts (IF this THEN that), and a final quality check. The checklist lives on a clipboard, in a shared doc, or in your project management tool. Done when you have a printable one-page checklist.

5. **Test the SOP with a team member.** Hand the checklist to an employee (or a family member if you do not have staff yet) and ask them to execute the process while you observe. Do not coach them unless they ask. If they get stuck, note where they got stuck. After the test, revise the SOP to fix the gap. Done when someone other than you can complete the process correctly using only the checklist.

6. **Save and version the SOP.** Save both the narrative and checklist versions as `SOP-<dependency-name>-v1.0-YYYY-MM-DD.md` in a folder like `operations/SOPs/`. When you revise the SOP based on testing or new edge cases, increment the version number and keep the old version for reference. Done when the SOP is stored and the team knows where to find it.

7. **Loop to the next dependency.** Return to your owner-dependency-map, mark this dependency as documented, and pick the next one. Repeat the process. The goal is to document 3 to 5 high-risk dependencies per month. After 6 months, you will have 20 to 30 SOPs covering the majority of the business.

## The Prompts

**Prompt 1: The Step-by-Step Process Interview**

```
I need to document this process from my business: [name the dependency, e.g., "daily job scheduling for our HVAC service team"].

Interview me step-by-step to extract the full process. Ask ONE question at a time:

1. What triggers this process? (Is it daily at a set time, or event-driven when something happens?)
2. What is the very first step you take? What information or tools do you need?
3. What comes next? Walk me through every step in order.
4. At each step, what decisions do you make? (For example: "If the customer requested same-day service, I check tech availability. If no techs are free, I call the customer to reschedule.")
5. What are the common mistakes or problems that happen during this process?
6. How do you handle exceptions? (For example: "If the part is out of stock, I...")
7. How do you know the process is complete and done correctly?
8. What happens if you skip a step or do it wrong? What breaks?

After I answer, compile the full process with all steps, decision branches, and exception handling.
```

**Prompt 2: Write the Narrative SOP**

```
Using the step-by-step process interview above, write a narrative SOP document with these sections:

**Process Name:** [name of dependency]

**Purpose:** Why this process matters to the business (what happens if we do not do it or do it wrong).

**Scope:** When to use this process and when NOT to use it (e.g., "Use this for standard jobs under $5K. Jobs over $5K require owner approval.").

**Materials and Tools:** What you need before starting (software, access, forms, contact lists, etc.).

**Step-by-Step Instructions:** Numbered steps with decision branches clearly marked (IF this THEN that). Include screenshots or examples where helpful.

**Quality Checks:** How to verify the process was completed correctly (e.g., "All jobs assigned should appear in the dispatch board by 9 AM.").

**Troubleshooting:** Common problems and how to fix them (e.g., "If no techs are available, check the on-call list.").

**Escalation:** When to ask for help (e.g., "If a customer requests a discount over 15%, escalate to the owner.").

Format as a markdown document that I can save as an SOP file.
```

**Prompt 3: Build the Checklist Version**

```
Using the narrative SOP from Prompt 2, create a one-page execution checklist for daily use by an employee. Format:

**[Process Name] – Daily Checklist**

[ ] Step 1: [action] (expected result or quality check)
[ ] Step 2: [action]
    - IF [condition], THEN [alternative action]
[ ] Step 3: [action]
...
[ ] Final Check: [how to verify completion, e.g., "All jobs in system, no unassigned slots"]

**Escalate to owner if:** [list the exception cases that require owner involvement]

Keep it to one page. Use checkboxes. No narrative, just actions and decision branches.
```

## The Loop

Document one dependency per week. Start with the top-ranked high-risk dependencies from your audit. After 3 months, you will have 12 SOPs. After 6 months, 25 SOPs. At that point, most of your core operations are documented. The business can run without you for a week. When you hit 30 documented SOPs covering all top-10 dependencies, you are ready to hire a general manager or operations lead who can execute the playbook without asking you 50 questions per day. The SOPs are also the foundation for selling the business. A buyer will pay more for a business with documented processes than one where everything lives in the owner's head.

## Pitfalls

1. **Writing the SOP yourself without the interview.** If you sit down and write the SOP from memory, you will skip steps, forget edge cases, and assume knowledge the employee does not have. The interview forces you to explain it as if teaching someone who knows nothing. Use the interview every time.

2. **Making the SOP too long.** If the narrative SOP is over 3 pages, the employee will not read it. If the checklist is over 1 page, they will not use it. Keep it tight. If the process is genuinely complex, break it into multiple SOPs (e.g., "Daily Scheduling Part 1: Assigning Jobs" and "Daily Scheduling Part 2: Handling Reschedules").

3. **Not testing the SOP with a real person.** The SOP you wrote makes perfect sense to you because you already know how to do it. An employee will find 5 gaps you did not see. Always test the checklist with someone who has never done the process before. Revise based on their questions.

4. **Documenting low-value processes first.** If you spend 3 hours documenting how to order office supplies (a low-risk, low-frequency task), you wasted the time. Start with the dependencies that are high-risk and high-frequency. Those are the ones that will bite you when you are unavailable.

5. **Storing SOPs where no one can find them.** If the SOPs live in a folder on your desktop, they are useless. Store them in a shared location (Google Drive, Notion, Dropbox, or your project management tool) where the team can access them without asking you. Better yet, print the checklists and laminate them. Tape them to the wall or keep them on clipboards. Make them physical and visible.

## Output

You receive two files for each documented dependency: (1) the narrative SOP (2 to 3 pages) with purpose, scope, materials, step-by-step instructions, quality checks, troubleshooting, and escalation rules; (2) the one-page execution checklist with numbered steps, decision branches, and a final quality check. Both are saved as `SOP-<dependency-name>-v1.0-YYYY-MM-DD.md` in your operations folder. After completing 10 to 15 SOPs, you will have documented the majority of your high-risk owner dependencies. At that point, you can hand off entire functions (scheduling, vendor ordering, customer onboarding) to employees or a manager without being the bottleneck. Your dependency count drops, your transferability score improves, and your business multiple rises from 2.4x to 4.0x.
