# Setup Guide 01b — Turn On Cowork & Install the Plugin

*Reading time: ~8 min. Outcome: Cowork mode active, the SMB Wealth Builder plugin installed, the full skill pack available.*

Cowork is the mode that turns Claude from a chat window into something that does the work on your own machine. It reads your files, runs the skills, and hands you finished documents (a deal dashboard, an investor report, a valuation) instead of text you copy out. This is where you run the acquisition system.

You do **not** download skills one by one. Every skill ships as a single **plugin**. You install it once, and every skill becomes available in your next Cowork conversation. No per-skill downloads, no dragging files into folders.

## What you need
- **Claude Pro ($20/mo) or higher.** Cowork is included.
- **An Apple Silicon Mac (M1/M2/M3/M4) on macOS Sonoma 14+, OR Windows.** Intel Macs are not supported. On an Intel Mac, use Chat + Projects and paste the skill contents manually.
- The latest **Claude Desktop app** from claude.com/download.

## Step 1 — Turn on Cowork (10 minutes, once)
1. Open the Claude Desktop app and sign in.
2. Switch to **Cowork** (the mode selector in the app).
3. Set the permission mode to **"Ask before acting"** while you learn. Claude pauses and shows its plan before it touches anything.
4. Create a folder for this work, for example `~/Acquisitions`. When you run your first task, Claude asks permission to access a folder. Point it here. It can only touch folders you authorize.

**What good looks like:** Cowork is selected, permission mode is "Ask before acting," and you have a dedicated folder Claude can use.

## Step 2 — Install the SMB Wealth Builder plugin (one time)
The plugin bundles the whole skill pack. Install it once — no terminal, all point-and-click.

Two pieces: a **marketplace** (the store) and the **plugin** (the app inside it). You add the store, then install the app.

1. In Claude Desktop, open the **Directory** — the panel with **Skills · Connectors · Plugins** tabs — and click the **Plugins** tab.
2. Click the **+** in the **top-right corner**, choose **Add marketplace**, and paste the repository:
   ```
   mobykax949/ai-SMBacquisition-os
   ```
   > ⚠️ Don't type "marketplace" into the search box — it searches plugin *names* and finds nothing. The marketplace is a source you *add* with the **+** button.
3. Open **smb-wealth-builder** in the list and click **Install**. Choose **User** scope so the skills work in every chat. (Not showing yet? Click the **↻ refresh** icon, top-right.)
4. Start a new Cowork conversation. Type `/` and you will see the skills (`/journey-navigator`, `/setup-my-workspace`, and the rest).

**What good looks like:** typing `/` in a fresh Cowork chat lists the acquisition skills.

> Prefer the command line? The same install, in Terminal:
> ```
> claude plugin marketplace add mobykax949/ai-SMBacquisition-os
> claude plugin install smb-wealth-builder@smb-wealth-builder
> ```

## Step 3 — Run your first skill
Start with Skill Zero. In Cowork, paste:

> Run the journey-navigator skill. Interview me one question at a time, then write my acquirer profile to my-profile.md and recommend my strategy.

Answer honestly. When it finishes, it writes `my-profile.md` into your folder — a real file you can open. That is the difference: Cowork produced a document, not just a reply.

## Safety while you learn (read once)
- Keep **"Ask before acting"** on until you trust the flow. Review each plan before you approve it.
- Start in a **test folder**, not your real financial files.
- Cowork is sandboxed and asks before deleting anything, but treat any file it can reach as fair game. Do not point it at sensitive data during practice.
- The Claude Desktop app must stay open while a task runs.

## Troubleshooting
- **Skills do not appear after installing:** start a NEW Cowork conversation. The skill list loads when a conversation begins.
- **Cannot add the marketplace:** the plugin installs from a public GitHub repo. If the repo is private, you will not see it until it is published.
- **"Command not found" in Terminal:** the CLI path is for people who have Claude Code installed; use the **Directory → Plugins → +** path instead.

Next: **02 — Projects Setup**, where your buy box and profile become permanent context every skill reads.
