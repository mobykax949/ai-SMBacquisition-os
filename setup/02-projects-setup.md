# Projects Setup

*Reading time: ~8 min. Outcome: Your acquisition Project created and loaded with context.*

Your deal work depends on Claude remembering what you are looking for and how you evaluate businesses. Without that context, every conversation starts from scratch. A Project is where you load the method once and have it available every time.

## The project brief — fill this out first

When you open your project in Cowork, the right-hand panel has **four parts**. This is your project's permanent brain: fill it once and every conversation in the project starts already knowing your situation.

| Part | What it is | What an acquirer puts here |
|---|---|---|
| **Instructions** | Your project brief — how Claude should behave in this project | Who you are, your buy box in one line, your income/SDE target, and the method to use (template below) |
| **Memory** | Facts Claude remembers as you work | Your target verticals, capital on hand, deal preferences |
| **Context** | Files loaded into every chat in the project | `my-profile.md`, `buy-box.md`, and your deal notes |
| **Scheduled** | Recurring tasks | e.g. a weekly `market-monitor` scan of new listings |

### Fill in the Instructions (your brief)

This is the field the app asks you to complete when you create the project. Click the **Instructions** pencil (top-right of the panel) and paste the text below, filled in with your details. The `setup-my-workspace` skill writes this for you as `project-instructions.md` — just paste that in.

```
I am [name]. I am acquiring [buy box in one line: industry, size, geography].
I need this business to pay me about [target SDE] per year; my 5-year goal is [net-worth or income goal].

How to help me in this project:
- Use the EPIC / Frasier method. Score deals against the 13 AQ criteria, value on SDE/EBITDA multiples, structure creative financing (seller notes, earnouts, $0-down stacks), and enforce the 70% Rule — kill weak deals fast.
- Always read my-profile.md and buy-box.md in Context before advising.
- Ask me for the deal facts before giving advice — no guessing.
- You are my method coach and analyst, not a lawyer or CPA. Flag when I need to hire one.
```

Then load your files into **Context** (below) and you are set. Memory and Scheduled are optional — add to them as you go.

## 1. Create your acquisition Project

1. In the Claude desktop app, click **Projects** in the left sidebar.
2. Click **New Project**.
3. Name it something clear: "OC Acquisitions", "Deal Pipeline", or "Portfolio Expansion".
4. Click **Create**.

You now have a persistent workspace where uploaded files and custom instructions stay loaded across every conversation in that Project.

## 2. Your buy box — the skills write it for you

You do **not** hand-write your buy box. Two skills produce and refine it:

- **`setup-my-workspace`** writes a first-draft `buy-box.md` from your interview (you already have this if you ran it).
- **`buy-box-builder`** turns that draft into the real thing: three lanes (conservative / target / aggressive), verticals scored on five factors, sized from the income you need, and stress-tested against live listings.

So your only job here is to make sure `buy-box.md` exists, then add it to Context in the next step.

> Haven't run them yet? Open a Cowork chat and run `setup-my-workspace` (writes the first draft), then `buy-box-builder` (refines and scores it). Come back here to load the result into Context.

For reference, this is what the buy box the skills produce contains:

| Section | What it holds |
|---|---|
| **Income anchor** | The SDE you need the business to pay you → the revenue range that produces it |
| **Target profile** | Industry, revenue range, SDE range |
| **Owner profile** | e.g. baby-boomer founders 55-70, owner-operated, exiting |
| **Geography** | Metro, state, or national |
| **Deal structure** | Financing preference (seller notes, $0-down, equity rollover) |
| **Red flags** | Auto-pass criteria (customer concentration, declining revenue, no books) |
| **Top verticals** | The 3 highest-scoring verticals from `buy-box-builder` |

## 3. Upload the buy-box file to your Project

1. Open your acquisition Project.
2. In the right-hand panel, click the **+** next to **Context**.
3. Upload `buy-box.md` (and `my-profile.md`).

Claude now sees this context in every conversation inside this Project. You do not need to re-explain your criteria.

## 4. What belongs in Project knowledge vs. chat

| Put in Project knowledge | Keep in chat |
|---|---|
| Buy box, evaluation criteria, financing playbook | Individual target notes, discovery call transcripts, specific deals |
| Your background (experience, network, capital available) | Weekly sourcing lists, broker leads |
| Standard templates (LOI outline, seller questionnaire) | One-off analysis ("run comps for this business") |

The rule: if you will reference it in 10+ conversations, upload it to the Project. If it is deal-specific, keep it in chat or save as a separate file.

## 5. What good looks like when setup is done

- A Project created and named.
- Your buy box uploaded so Claude knows your criteria.
- You open that Project every time you work on deals, and Claude starts every conversation already knowing what you want.

Next: **The Vocabulary** — 10 terms you need to know to operate Claude like a professional.
