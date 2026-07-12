---
name: claude-acquisition-setup
description: Use when setting up Claude Desktop + Pro for acquisition work. Creates a Project, loads the buy box as project knowledge, and configures the RCTF prompting frame.
version: 1.0.0
---

# Claude Acquisition Setup

## Overview

Configure Claude Desktop + Claude Pro for deal sourcing and analysis. You will create a dedicated Project, load your buy box criteria as project knowledge, and establish the RCTF prompting pattern (Role/Context/Task/Format) that makes every prompt clear and actionable. This setup runs once and turns Claude into your 24/7 deal analyst.

## When to Use

- You just subscribed to Claude Pro and installed Claude Desktop
- You are starting acquisition work for the first time
- You need to rebuild a Project after testing or switching accounts
- You want to ensure Claude remembers your criteria across all deal conversations

## Steps

1. **Open Claude Desktop and create a new Project.** Click the Projects menu (left sidebar), then New Project. Name it "Acquisition Engine" or similar. A Project holds persistent knowledge across all chats inside it.

2. **Write your buy box criteria as a markdown file.** Save it as `buy-box.md` on your desktop. Include: YOUR geography (e.g., Orange County CA), revenue (e.g., $1M-$5M), SDE (e.g., $200K+), employees (e.g., 5-25), age (e.g., 10+ years), owner profile (e.g., boomer 55+, exit-minded), financing (e.g., SBA 7(a) + seller note, or 1031 if real estate), and YOUR priority verticals (e.g., hood cleaning, laundromats, pool service). These examples are one buyer's box, not the method — use the numbers from your own `setup-my-workspace` / `buy-box-builder` output. Keep it under 2 pages.

3. **Upload the buy box to Project Knowledge.** Inside the Acquisition Engine Project, click the gear icon (Project settings), then Add Knowledge, and upload `buy-box.md`. Claude will now reference this file in every conversation inside this Project without you needing to paste it again.

4. **Add the 13-criterion AQ Score as Project Knowledge.** Ask Claude to create `aq-score.md` with the 13 criteria: location, seller finance, broker, long listing, margin, history, FF&E, multiple, leased space, own property, staff, inventory, training — using the rating legend from the aq-analyzer skill (green = confirmed favorable, yellow = unknown/info gap, red = confirmed unfavorable). Keep the three counterintuitive reads from that legend: long time-on-market = green (motivated seller), direct/off-market = green (broker = yellow-neutral), real estate owned = green. Upload it the same way.

5. **Test the Project setup.** Start a new chat inside the Project and ask: "What are my acquisition criteria?" Claude should reference the uploaded buy box. If it does not mention your verticals or geography, the upload failed. Try re-uploading with a smaller file.

6. **Establish the files-not-chat-memory rule.** Tell Claude in your first Project chat: "Always save deal analyses, target lists, and AQ scores as markdown files that I can download and version outside this chat. Never rely on chat memory alone for deal data." Pin this instruction in the Project description field if available.

7. **Learn the RCTF prompt structure.** Every prompt you write should have four parts: Role (who Claude is), Context (the situation), Task (what you want), Format (how to deliver it). Example: "You are a deal analyst. I am screening a BizBuySell listing for a pool service business in Orange County. Run the AQ Score green/yellow/red on the 13 criteria. Return a table with criterion, rating, evidence, and a go/pass/dig-deeper verdict at the bottom."

## The Prompts

```
Prompt 1: Test the Project setup

You are my acquisition analyst. I am setting up this Project to screen and analyze small business deals. Review the uploaded buy box and AQ Score files. Confirm: what geography am I targeting, what revenue range, and what are the 13 AQ criteria? If you cannot find these files, say so.
```

```
Prompt 2: Save a deal analysis example

You are a deal analyst. I need to establish the file format for all future deal analyses. Create a template markdown file called "deal-analysis-template.md" with these sections: Business Name, Listing Source, AQ Score Table (13 rows: criterion, rating, evidence), Financial Summary (revenue, SDE, asking price, multiple), Go/Pass/Dig Verdict, and Top 2 First-Call Questions. Show me the file content so I can download it.
```

```
Prompt 3: Establish the weekly workflow

You are my workflow designer. I need a weekly acquisition routine using this Project. Design a 5-step checklist that runs every Monday: (1) web search new BizBuySell/broker listings in my verticals + geography, (2) screen against buy box, (3) run AQ Score on 3 best matches, (4) rank by succession likelihood, (5) save the results as "weekly-scan-YYYY-MM-DD.md". Show me the checklist and the file format.
```

## The Loop

After initial setup, return to the Project weekly to run deal scans, score opportunities, and refine your buy box. When you discover a new vertical or adjust your criteria, update the `buy-box.md` file and re-upload it to Project Knowledge. Claude will immediately use the new version in all future chats. If a conversation gets messy or off-track, start a fresh chat inside the same Project. All uploaded knowledge carries over.

## Pitfalls

- **Uploading PDFs instead of markdown.** Claude reads markdown fastest. If your buy box is a PDF, copy the text into a plain markdown file first.
- **Forgetting which Project you are in.** If you start a chat outside the Acquisition Engine Project, Claude will not see your buy box or AQ criteria. Always check the Project name before running a deal analysis.
- **Overloading Project Knowledge with too many files.** Keep it focused: buy box, AQ Score, and deal templates only. Do not upload every listing you find. Claude slows down with 50+ files in Project Knowledge.
- **Not versioning your buy box outside Claude.** If you lose access to your Claude account or the Project gets corrupted, your buy box is gone. Save `buy-box.md` in Dropbox, Google Drive, or a local folder as backup.
- **Relying on chat memory for deal data.** Claude cannot recall details from a conversation 3 weeks ago. Always save deal analyses as downloadable markdown files and store them outside Claude in a folder like `acquisitions/targets/<vertical>/<business-name>.md`.

## Output

You will have a working Claude Desktop Project loaded with your buy box and AQ Score as persistent knowledge. Every conversation inside this Project will reference your criteria without you needing to paste them. You will also have a template file format for deal analyses and a weekly workflow checklist. Save the Project name and confirm it works by running the test prompt above.
