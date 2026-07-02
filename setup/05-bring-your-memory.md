# Bring Your Memory

*Reading time: ~7 min. Outcome: A save-as-you-go file discipline that prevents lost work.*

Claude is not a database. A long conversation eventually compacts and Claude forgets the middle. The fix is simple: save everything worth keeping as a file. Files survive. Chat memory does not.

## The one rule

**If you produced it and you want it later, save it to a file.**

That applies to:
- Target notes and scorecards.
- Valuation models and comp analyses.
- Discovery call transcripts and seller questionnaires.
- Financing structures and term sheets.
- Buy-box updates and criteria changes.

Treat the chat as a workbench. Treat files as the filing cabinet.

## Where to save deal files (the naming system)

Use a simple folder structure so you can find targets later:

```
targets/
  professional-services/
    orange-county-it-consulting.md
    riverside-accounting-firm.md
  home-services/
    san-diego-hvac-co.md
```

Naming pattern: `targets/<vertical>/<business-name>.md`

Each target file holds:
- The AQ scorecard (13 criteria, green/yellow/red).
- Key financials (revenue, SDE, asking price, multiple).
- Discovery notes (owner motivation, team, transition plan).
- Red flags and deal structure ideas.

## What to save in Project knowledge vs. local files

| Save in Project knowledge | Save as local files |
|---|---|
| Buy box, AQ criteria, financing playbook (things you reference across all deals) | Individual target notes, scorecards, deal memos (specific to one business) |
| Your background and experience | Discovery call transcripts |
| Standard templates (LOI outline, seller questionnaire) | Valuation models and comp lists |

The rule: if it applies to every deal, put it in the Project. If it applies to one deal, save it as a file outside the Project and reference it when needed.

## How to save during a conversation

When Claude generates something you want to keep:

1. Copy the output (or use the artifact download if it is a table or document).
2. Paste it into a markdown file and save locally.
3. Name it following the `targets/<vertical>/<business>.md` pattern.
4. If you are mid-task and want to keep working, tell Claude: "Save this target scorecard as `targets/professional-services/oc-it-consulting.md` and continue."

Claude can write files directly (if you give the path and content), or you can copy and save manually. Either way, the output is now durable.

## What happens if you do not save

- Long conversations compact. Claude forgets the middle.
- You lose detailed analysis and have to regenerate it (wasted time, wasted tokens).
- You cannot compare targets side by side because the notes are buried in different chats.
- When you come back a week later, the context is gone.

## What good looks like when you bring your memory

- Every target you evaluate has a saved file with the AQ scorecard and notes.
- You can open any target file later, upload it to a new chat, and pick up where you left off.
- Your Project holds the method. Your local files hold the deals.
- Nothing important lives only in chat.

Next: **The Three Modes** — quick Q&A vs. deep analysis vs. long agentic jobs, and when to use each.
