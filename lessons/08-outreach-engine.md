# Lesson 08 — The Outreach Engine

*Personalized first contact across six channels and three seller archetypes — drafted by AI, sent only after you approve.*

Reading time: ~8 min · Track: Acquire · Prerequisite: a target list (`deal-finder`, Lesson 05)

---

## What this does

The Frasier 6-channel outreach machine. Give it a target seller and it generates first-contact drafts for warm intro, phone script, mailed letter, LinkedIn request, social DM, or cold email — each built on the verbatim EPIC scripts and matched to one of three seller archetypes: cold investor, strategic/related-business (the lowest-threat, highest-response angle), or distressed-capital-provider. The email channel uses the EPIC "puppy method" — a cute puppy/kitten image at the top, which the playbook reports tested at ~75% higher open rate (Frasier's stated result, not an independently verified benchmark), plus a curiosity subject line and "exploring opportunities" framing. Every draft is staged for your review; nothing sends automatically. The engine runs Step 1 of the EPIC 3-step sequence (personalized bulk outreach → rapport conversation → data-gathering conversation) against the benchmark funnel: 100 outreaches → 60 responses → 10 conversations → 5 offers → 1–3 deals.

**You'll walk away with:** ready-to-send outreach drafts per channel, and a logged funnel you can troubleshoot with real numbers.

---

## Step 1 — Install the plugin (one time, gets you every skill)

All skills ship in the SMB Wealth Builder plugin. *(Already installed? Skip to Step 2.)*

1. In Claude Desktop: **Customize** → **Plugins** tab.
2. **+** → **Add marketplace** → paste `mobykax949/ai-SMBacquisition-os`
3. Install **smb-wealth-builder**, **User** scope.
4. New Cowork chat, type `/` — the skills appear.

**Done when:** `/outreach-engine` shows in a fresh Cowork chat.

---

## Step 2 — Give Claude what it needs

- A real target: seller name, business name, industry, location, rough size. This skill writes copy for leads you already have — deal-finder builds the list.
- Any intel on motivation (retiring, distressed, strategic exit) to pick the archetype. Unsure? Default to strategic/related-business.
- Your own positioning facts: your name, your business (for the strategic angle), your buy box in one line.
- A spreadsheet or CRM to log every send.

---

## Step 3 — Run it (copy this)

```
/outreach-engine
```

Or specify the job:

```
Run the outreach-engine skill. Seller: [name], [business], [industry], [city, state], size [revenue/employees if known]. My intel: [motivation signals]. Me: [name], positioning [private investor / owner of a related [industry] business / capital provider]. Archetype: [strategic-related-business]. Generate drafts for [phone script + LinkedIn request + mailed letter], personalized, each ending with a clear call-to-action. Stage for my approval — do not send anything.
```

---

## What Claude creates

| File / output | What it is |
|---|---|
| Channel drafts | Opener, pitch, ask, next-step logistics per channel — under 150 words for letter/DM, under 90 seconds for phone |
| Archetype framing | Cold-investor, strategic/related (reads as partnership, not acquisition), or distressed-capital positioning applied consistently |
| Follow-up draft | The polite no-response follow-up — often the message that converts, because it shows persistence |
| Outreach log format | Channel, date sent, response, outcome — the funnel data you review every 20 sends |

**How it works:** the EPIC scripts are templates, not copy-paste — the engine personalizes each with the seller's name, business, niche, and one specific observation, because generic bulk messages get reported as spam. The goal of every message is the same: move up-channel to a live call fast. When a seller replies, you respond once with enthusiasm, propose a 15-minute call, and send a calendar link.

---

## Step 4 — Test it, refine it, stack it

**Test** (multi-channel one seller):
```
Same seller, three channels: phone script, LinkedIn request, mailed letter. Strategic angle, consistent positioning, tailored to each channel's norms. Stage all three.
```

**Refine** (the funnel tells you what's broken):
```
My last 20 outreaches: [N] responses. Benchmark is 60%. Diagnose: target list too cold, positioning not credible, or wrong archetype? Rewrite my worst-performing draft.
```

**Try the puppy method** (the tested email variant):
```
Draft a cold email to [seller] using the EPIC puppy method: mark where a cute puppy/kitten image goes at the top, a curiosity subject line, "exploring opportunities" framing (not "I want to buy"), one line on what I do, and a 15-minute-call ask. Under 150 words, staged for my approval.
```

**Stack it:** a positive reply goes straight to the seller deep dive.
```
[Seller] replied positively. Draft my one enthusiastic reply proposing a 15-minute call with my calendar link, then prep me: run the discovery-interviewer skill so I'm ready for the first call.
```

---

## Tips & troubleshooting

- **Personalize or perish.** Fifty identical LinkedIn messages get you reported for spam. Name, business, industry, and one specific observation — every time.
- **Match the archetype to reality.** The distressed-capital pitch offends a healthy, profitable seller. Use it only with visible distress signals; otherwise default to strategic/related-business.
- **Move to a live call fast.** Don't spend three days trading DMs. One warm reply, then propose the call. LinkedIn and email are stepping stones, not the destination.
- **Prepare for the responses before you send.** 100 outreaches can mean 60 inbound replies in days. Block response time, have your calendar link ready, and have the discovery script prepped before the batch goes out.
- **Follow up once, maybe twice — then stop.** Wait 5–7 days, send the polite follow-up. Three unanswered messages means not interested; move down the list.

---

## Where this fits

Branch B, step 3 — the bridge between sourcing (Lessons 05–07) and qualification. A responder who wants to sell moves to the first call, and post-contact you score them: **Lesson 09 — The AQ Analyzer**; the deep-dive call itself is **Lesson 10 — Discovery Interviewer**. But no outreach is wasted: an owner who's *not ready to sell* forks to **Lesson 08b — The CFE Converter** (pitch consulting-for-equity instead of walking away), and a non-fit gets asked for a referral.
