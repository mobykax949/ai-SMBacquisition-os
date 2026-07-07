# Models and Plans

*Reading time: ~8 min. Outcome: Know which Claude model to use, when limits matter, and when to upgrade your plan.*

Claude offers multiple model tiers and subscription plans. For acquisition work, the right combination is: **build your prompts and skills in the model you will actually run**, and **upgrade when you hit limits that block real work**.

## The model tiers (what they mean)

| Model tier | What it is | When to use it for deal work |
|---|---|---|
| **Haiku** | Fastest, cheapest, lightweight reasoning. | Quick lookups, simple calculations, reformatting data. Not recommended for full deal analysis. |
| **Sonnet** | Balanced speed and reasoning. The default for most tasks. | Target scoring, valuation models, comp research, deal memos. This is the workhorse for acquisitions. |
| **Opus** | Deepest reasoning, slowest, most expensive. | Complex multi-business analysis, vertical research, large-dataset work. Use when Sonnet is not enough. |

**The rule for acquisition work:** Default to **Sonnet**. Upgrade to **Opus** only when a task is too complex for Sonnet (rare). Do not use Haiku for anything that requires real reasoning.

## The subscription plans (Pro vs. higher tiers)

| Plan | Cost | What you get | When it is enough | When to upgrade |
|---|---|---|---|---|
| **Claude Pro** | $20/month | Projects, larger context, priority access during high demand. Enough for most acquisition work. | You are evaluating 5-10 targets per month, running deal memos and valuations, not hitting message limits. | You hit message limits mid-task or need to process 50+ targets per week. |
| **Claude Team** | $30/user/month | Higher limits, shared Projects (team collaboration). | You are running deals with a partner or team and need shared workspaces. | (Same as Pro — higher limits are the main benefit.) |
| **Claude Enterprise** | Custom pricing | Unlimited usage (within reason), custom integrations, priority support. | You are running a fund, processing hundreds of targets, or need API access for automation. | You outgrow Team limits or need enterprise features. |

**For most solo buyers or small partnerships:** **Pro is enough**. Upgrade to Team if you need shared Projects. Upgrade to Enterprise only if you are running institutional volume.

## Build in the model you run

**The mistake most people make:** Prototype a skill or prompt in a fast, cheap model (Haiku), then try to run the real task in Sonnet and wonder why the output is different.

**The fix:** Build your prompts and skills in **Sonnet** from the start. Test them in Sonnet, iterate in Sonnet, save them in Sonnet. When you run a real deal analysis, it will behave the same way.

Exception: If a task genuinely needs Opus (complex multi-step reasoning, large dataset), build and test in Opus. Do not build in Sonnet and hope Opus works the same.

## When limits mean upgrade

You will know it is time to upgrade when:
- **You hit message limits mid-task.** You are running a long agentic job (sourcing 20 targets, building a deal memo) and Claude stops because you used your daily message quota. Pro has higher limits than Free, but heavy users will eventually hit them.
- **You are processing volume.** If you are evaluating 50+ targets per week, scoring every one through AQ criteria, pulling comps, and writing memos, you will run out of messages on Pro. Upgrade to Team or Enterprise.
- **You need shared Projects.** If you are working with a partner and you both need access to the same buy box, target notes, and deal pipeline, upgrade to Team for shared Projects.

If you are running 5-10 deals per month, Pro is fine. If you are running a pipeline of 50+ active targets, you need Team or Enterprise.

## What good looks like when you pick the right plan

- You build and test your prompts in Sonnet (the model you will run for real work).
- You are on Pro (or higher) so you have Projects, large context, and enough message capacity for deal volume.
- You upgrade only when you hit real limits (message caps, need for shared Projects), not preemptively.
- Your workflow is consistent: same model, same prompts, repeatable results.

You are now through the full setup sequence. You have Claude configured, your Project loaded, your vocabulary solid, your prompt discipline in place, and your plan matched to your volume. Go run deals.
