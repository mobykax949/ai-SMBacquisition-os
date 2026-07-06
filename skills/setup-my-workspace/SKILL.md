---
name: setup-my-workspace
description: Use this first, right after installing the plugin. It interviews you and sets up your entire Claude workspace for acquisitions — your profile, your buy box, and your Project instructions — so every other skill already knows who you are. Run it once before anything else.
version: 1.0.0
---

# Set Up My Workspace

## Overview

This is the front door. You just installed the plugin and you have the full skill pack, but Claude does not yet know anything about you. This skill fixes that in one sitting. It interviews you, then writes three files that make every other skill smarter: your acquirer profile, your buy box, and a set of Project instructions you paste once so Claude remembers you in every conversation. Run this before any other skill.

## When to Use

- The first thing you do after installing the SMB Wealth Builder plugin
- Any time your situation changes enough that your buy box or strategy should change
- When you want Claude to stop asking you the same background questions every conversation

## Steps

1. **Make a home for your work.** Create a folder on your computer called `Acquisitions` (in Cowork, you can just ask Claude to make it). This is where your files live. Done when the folder exists and Claude has permission to use it.

2. **Run the interview (Prompt 1).** Claude asks you one question at a time about who you are, what you have, and what you want. Answer honestly with real numbers. Done when Claude has your ownership status, capital, financing readiness, **required income/SDE target**, background, **industries of interest**, geography, hours, risk tolerance, and 5-year goal.

3. **Get your three files.** Claude writes `my-profile.md` (who you are), `buy-box.md` (what you are hunting), and `project-instructions.md` (the paste-once memory). Done when all three files are in your Acquisitions folder.

4. **Install your memory into a Project (Prompt 2 guides you).** Open Claude's Projects, create one called "My Acquisitions," paste the contents of `project-instructions.md` into the project's **Instructions** (the project brief), and add `my-profile.md` and `buy-box.md` to the project's **Context**. Done when your Instructions are set and both files are in Context.

5. **Get your next step.** Claude reads your profile and tells you which skill to run next and why. Done when you know your journey stage and the name of the next skill to open.

## The Prompts

**Prompt 1: The Setup Interview**

```
Run the setup-my-workspace skill. Interview me one question at a time, wait for each answer, then ask the next. Cover:

1. Do I already own a business? (What is it, rough revenue, does it run without me?)
2. Cash I can actually invest right now, and am I able to get an SBA loan?
3. How much annual income (owner cashflow / SDE) do I need this business to pay me — now, and what is my 5-year net-worth or income goal? (We size the buy box from this number.)
4. My work background and the skills I bring
5. Which industries or business types am I drawn to, already understand, or have an edge in — and any I would never buy?
6. Where I live and how far I am willing to operate
7. Hours per week I can give this
8. Do I want steady income or a bigger swing?
9. What I want in 5 years — income, a business to run, or something to sell?

When you have my answers, write three files to my Acquisitions folder:
- my-profile.md: my acquirer profile and my journey stage
- buy-box.md: a first-draft buy box anchored on my required income/SDE (reverse-engineer the revenue range from that number), plus my industries of interest, size, geography, deal structure, and red flags
- project-instructions.md: a short set of custom instructions I can paste into a Claude Project so you remember all of this in every future chat

Then tell me my journey stage and which skill to run next.
```

**Prompt 2: Turn It Into Permanent Memory**

```
Walk me through setting up my Cowork project step by step, as if I have never used projects before. Tell me exactly how to create it, what to name it, how to paste project-instructions.md into the project's Instructions (the project brief), and how to add my-profile.md and buy-box.md to the project's Context so you see them in every conversation. Keep it to plain numbered steps.
```

## The Loop

Interview → three files → Project set up → next skill. Re-run the interview (Prompt 1) whenever your situation changes; it rewrites the three files and your Project stays current.

## Pitfalls

1. **Skipping this and jumping to a skill.** Without your profile and buy box, every other skill starts by asking you the same questions. Ten minutes here saves you an hour later.
2. **Answering with hopes instead of facts.** State the capital you have and the loan you can actually get. A buy box built on wishful numbers points you at businesses you cannot buy.
3. **Not pasting the instructions into a Project.** If you skip the Project step, Claude forgets you the moment the chat ends. The whole point is paste-once memory.
4. **Treating the buy box as final.** This first draft is a starting point. The buy-box-builder skill refines it against real verticals later.

## Output

Three files in your Acquisitions folder — `my-profile.md`, `buy-box.md`, `project-instructions.md` — and a Claude Project set up with your instructions and knowledge loaded. From here, Claude knows who you are in every conversation. Next skill: usually `journey-navigator` to confirm your strategy, then `buy-box-builder`.
