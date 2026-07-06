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

## 2. Write your buy-box context document

Your buy box is the 1-page spec that tells Claude exactly what businesses you want. Write this as a markdown file (call it `buy-box.md`) and save it locally before uploading.

| Section | What to include |
|---|---|
| **Target profile** | Industry, revenue range, profit range (e.g. "B2B service businesses, $1-5M revenue, $300K-1M SDE"). |
| **Owner profile** | Demographics and motivation (e.g. "baby-boomer founders 55-70, owner-operated, looking to retire or exit"). |
| **Geography** | Where you want to buy (metro area, state, or national). |
| **Deal structure** | How you want to finance (e.g. "seller financing preferred, $0 out of pocket, equity rollover welcome"). |
| **Red flags** | What kills the deal fast (e.g. "single-customer concentration >40%, declining revenue, missing financials"). |
| **Evaluation method** | The AQ criteria or your own framework (green/yellow/red scoring on seller finance, margin, location, staff, etc.). |

Example snippet:
```
Target: B2B professional services, Orange County CA
Revenue: $1-5M top line, $300-1M SDE
Owner: 55-70, burned out, owner-operated
Structure: Seller financing, equity rollover, consultant transition
Red flags: <40% margin, single customer >40%, no books
```

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
