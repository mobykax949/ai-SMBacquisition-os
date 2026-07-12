# Lesson 02 — Claude Acquisition Setup

*Turn Claude into your 24/7 deal analyst: a dedicated Project, your buy box as permanent knowledge, and the RCTF prompting frame.*

Reading time: ~7 min · Track: Both · Prerequisite: `setup-my-workspace` (Lesson 01)

---

## What this does

This is the plumbing lesson. It configures Claude Desktop + Pro for deal work: a dedicated Project that holds your buy box and the 13-criterion AQ Score as persistent knowledge, a files-not-chat-memory rule so no analysis ever evaporates, and the RCTF pattern (Role / Context / Task / Format) that makes every ad-hoc prompt land. Run it once; from then on every conversation inside the Project already knows your criteria without you pasting anything.

**You'll walk away with:** a working "Acquisition Engine" Project with `buy-box.md` and `aq-score.md` loaded, a deal-analysis file template, and a weekly scan workflow.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin — install once and everything is available. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop, click **Customize** in the left sidebar and open the **Plugins** tab.
2. Click the **+** (top-right) → **Add marketplace**, and paste: `mobykax949/ai-SMBacquisition-os`
   > It's a source you *add* with the **+** button, not a plugin you search for.
3. Find **smb-wealth-builder**, click **Install**, choose **User** scope.
4. Start a NEW Cowork chat and type `/` — the skills appear.

**Done when:** typing `/claude-acquisition-setup` in a fresh Cowork chat shows the skill.

---

## Step 2 — Give Claude what it needs

- The files from Lesson 01: `my-profile.md` and `buy-box.md`. If you skipped Lesson 01, this skill will have you write a buy box from scratch — but the front door is the better path.
- A Claude Pro (or higher) subscription and Claude Desktop installed.
- Ten minutes to click through Projects once, guided.

---

## Step 3 — Run it (copy this)

```
/claude-acquisition-setup
```

It walks you through: create the Project, upload `buy-box.md` (from Lesson 01) and `aq-score.md` — a file Claude generates for you in this step using the 13 criteria (location, seller finance, broker, long listing, margin, history, FF&E, multiple, leased space, own property, staff, inventory, training), each defined green / yellow / red per the aq-analyzer skill's legend — then test that the upload took. Steer it if you want:

```
Walk me through setting up my Acquisition Engine Project step by step: create it, upload my buy box and the 13-criterion AQ Score as project knowledge, establish the rule that all deal analyses are saved as markdown files I can download, and teach me the RCTF prompt structure with one worked example from my verticals.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| The **Acquisition Engine** Project | Persistent knowledge across every chat inside it — no re-pasting criteria |
| `buy-box.md` (uploaded) | Your criteria: geography, revenue, SDE, verticals, financing — referenced automatically |
| `aq-score.md` (uploaded) | The 13 AQ criteria with green/yellow/red definitions, ready for every scoring run |
| `deal-analysis-template.md` | The standard file format: AQ table, financial summary, go/pass/dig verdict, first-call questions |
| A weekly workflow | The 5-step Monday checklist: search listings → screen against buy box → AQ-score the best 3 → rank → save as `weekly-scan-YYYY-MM-DD.md` |

**How it works:** Projects hold knowledge; chats inside them read it. The RCTF frame — Role ("you are a deal analyst"), Context (the listing, your buy box), Task ("run the AQ Score"), Format ("return a table with a verdict") — is how you talk to the setup when you go off-script. Every skill in the pack is a fully-formed RCTF prompt under the hood, so most days you just type `/skill-name`.

---

## Step 4 — Test it, refine it, stack it

**Test** (confirm the knowledge is live):
```
You are my acquisition analyst. Review the uploaded buy box and AQ Score files. Confirm: what geography am I targeting, what revenue range, and what are the 13 AQ criteria? If you cannot find these files, say so.
```

**Refine** (when criteria change):
```
I am updating my buy box: [what changed]. Rewrite buy-box.md with the change and remind me to re-upload it to Project Knowledge so every future chat uses the new version.
```

**Stack it:** confirm your stage before hunting.
```
Run the journey-navigator skill using my-profile.md in this Project. Confirm my stage and my next skill.
```

---

## Tips & troubleshooting

- **Upload markdown, not PDFs.** Claude reads markdown fastest. If your buy box is a PDF, copy the text into a plain `.md` file first.
- **Check which Project you're in.** A chat started outside the Acquisition Engine Project cannot see your buy box or AQ criteria. Glance at the Project name before any deal analysis.
- **Keep Project Knowledge lean.** Buy box, AQ Score, and templates only. Don't upload every listing you find — a crowded Project dilutes what Claude pays attention to.
- **Version your buy box outside Claude.** If you lose account access, an un-backed-up buy box is gone. Keep `buy-box.md` in Dropbox, Drive, or a local folder too.
- **Never trust chat memory with deal data.** Claude cannot recall a conversation from three weeks ago. Every analysis gets saved as a downloadable file, filed like `acquisitions/targets/<vertical>/<business>.md`.

---

## Where this fits

Phase 0, right after the front door. Lesson 01 wrote your files; this lesson makes them permanent infrastructure. Next: **Lesson 02b — Journey Navigator** confirms your stage, then the funnel starts at **Lesson 03 — Buy-Box Builder**.
