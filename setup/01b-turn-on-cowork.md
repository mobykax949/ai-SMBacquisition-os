# Setup Guide 01b — Turn On Cowork

*Reading time: ~8 min. Outcome: Cowork mode active, one skill installed, a test task run.*

Cowork is the mode that turns Claude from a chat window into something that does the work on your own machine. It reads your files, runs the skills, and hands you finished documents (a deal dashboard, an investor report, a valuation) instead of text you copy out. This is where you run the acquisition system.

## What you need
- **Claude Pro ($20/mo) or higher.** Cowork is included in Pro.
- **An Apple Silicon Mac (M1/M2/M3/M4) on macOS Sonoma 14 or later, OR Windows.** Intel Macs are not supported. If you are on an Intel Mac, use plain Chat + Projects instead (the skills still work, you just paste more).
- The latest **Claude Desktop app** from claude.com/download.

## Turn it on (10 minutes, once)
1. Open the Claude Desktop app and sign in.
2. Find the mode tabs at the top: **Chat · Cowork · Code**. Click **Cowork**.
3. Set the permission mode to **"Ask before acting"** while you learn. Claude will pause and show you its plan before it touches anything. (Settings → Cowork.)
4. Create a folder for this work, for example `~/Acquisitions`. When you run your first task, Claude asks permission to access a folder — point it here. It can only touch folders you authorize.

**What good looks like:** the Cowork tab is selected, permission mode is "Ask before acting," and you have a dedicated folder Claude is allowed to use.

## Install your first skill
Skills live in a folder Claude reads automatically.
1. In Finder, press `Cmd+Shift+G` and go to `~/.claude/skills/` (create the `skills` folder if it is not there).
2. Copy the skill folder you want to run (for example the whole `journey-navigator` folder, the one containing `SKILL.md`) into `~/.claude/skills/`.
3. Back in Cowork, type `/` and you should see the skill listed. It is now installed.

**What good looks like:** typing `/journey-navigator` in Cowork shows the skill.

## Run a test task
In Cowork, say:

> Run the journey-navigator interview on me. Ask one question at a time.

Answer honestly. When it finishes, it writes `my-profile.md` into your folder — a real file you can open. That is the difference: Cowork produced a document, not just a reply.

## Safety while you learn (read once)
- Keep **"Ask before acting"** on until you trust the flow. Review each plan before you approve it.
- Start in a **test folder**, not your real financial files.
- Cowork is sandboxed and asks before deleting anything, but treat any file it can reach as fair game — do not point it at sensitive data during practice.
- The Claude Desktop app must stay open while a task runs.

Next: **02 — Projects Setup**, where your buy box and profile become permanent context every skill reads.
