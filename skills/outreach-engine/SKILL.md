---
name: outreach-engine
description: Use when you need to generate personalized seller outreach across six channels (warm intro, phone, letter, LinkedIn, DM, email) and three seller archetypes, with AI drafts staged for human approval before sending.
version: 1.0.0
---

# Outreach Engine

## Overview

The Frasier 6-channel outreach machine. This skill generates personalized first-contact messages to business sellers across six channels (warm intro request, phone script, mailed letter, LinkedIn connection request, social DM, cold email) and three seller archetypes (cold investor approach, strategic/related-business angle, distressed business). Each message follows the proven EPIC 3-step sequence (personalized bulk outreach, rapport-building conversation, data-gathering conversation) and the EPIC funnel (100 outreaches, 60 responses, 10 conversations, 5 offers, 1 to 3 deals — the course's stated benchmark; treat it as the shape of the process, since pure cold channels typically respond at a small fraction of that 60%). All drafts are staged for your review and approval. Nothing is sent automatically.

## When to Use

Run outreach-engine when you have identified a target seller (from a broker listing, direct research, referral, or your own prospecting) and need to make first contact. You must know the seller's name, business name, industry, and rough size (revenue or employee count). Optionally, know their motivation category (retiring, distressed, strategic exit) to select the best archetype. If you have no leads yet, this skill does not generate the lead list. It generates the outreach copy for leads you already have.

## Steps

1. **Choose your channel.** Decide whether you want a warm intro (ask a mutual contact to connect you), a phone script (for a cold call), a mailed letter, a LinkedIn connection request, a direct message on another social platform, or a cold email. If you have multiple channels available, generate drafts for all of them and pick the best fit. **Cold email note — the puppy method:** the EPIC email template opens with a cute puppy/kitten image, which the playbook reports tested at a 75% higher open rate. Pair it with a curiosity-based subject line ("Quick question about [Company]") and frame the message as *exploring opportunities*, not "I want to buy." (The 75% figure is Frasier's stated test result, not an independently verified benchmark.)

2. **Select the seller archetype.** Three archetypes match three scripts: (a) Cold investor (seller is unrelated to your business, you are positioning as a private investor or acquirer), (b) Strategic/related-business (seller operates in your industry or adjacent, you are positioning as a potential partner or referral source to reduce threat), (c) Distressed business (seller shows signs of financial stress or capital needs, you are positioning as a capital provider or turnaround partner). If unsure, default to strategic/related-business. It gets the highest response rate.

3. **Gather target-specific facts.** For personalization, collect: seller's first name, business name, industry/niche, location (city/state), approximate revenue or profit range (if known), your own business name and location (for strategic angle), any mutual connection (for warm intro). The more specific, the better the draft.

4. **Paste the prompt and fill the brackets.** Use Prompt 1 below. Claude generates a complete outreach draft (or multiple drafts if you request multiple channels). Each draft includes the opener, the pitch, the ask, and next-step logistics.

5. **Review, edit, approve.** Read the draft. Add your own voice, adjust any claims, personalize further if you have intel on the seller. When satisfied, send the message through your chosen channel. Log the outreach in a spreadsheet or CRM to track responses.

6. **Move responders into the sequence.** If the seller replies, move to Step 2 of the sequence (rapport-building conversation). Use discovery-interviewer for the next call.

## The Prompts

**Prompt 1: Generate Personalized Outreach Draft**

```
Generate a [channel: warm intro request / phone script / mailed letter / LinkedIn connection request / social DM / cold email] outreach message for this seller:

Seller details:
- Name: [first name or full name]
- Business name: [company name]
- Industry: [specific niche, e.g. "HVAC services" or "e-commerce beauty brand"]
- Location: [city, state]
- Approximate size: [revenue range or employee count, if known]
- My intel on their situation: [any known motivation, e.g. "owner is 65 and posted on a broker site" or "business has declining reviews and may need capital"]

My details:
- My name: [your name]
- My positioning: [choose: "private investor looking to acquire" OR "owner of a [your industry] business looking for partnerships/referrals" OR "investor group providing capital to distressed businesses"]
- My business (if strategic angle): [your company name and city]
- My buy-box: [e.g. "$1-5M revenue, B2B services, profitable, owner-operated"]

Archetype: [cold investor / strategic-related-business / distressed-capital-provider]

Use the EPIC outreach scripts as the template. Personalize with the target's specific details. Keep it short (under 150 words for letter/DM, under 90 seconds for phone script). End with a clear call-to-action (schedule a call, reply to this message, or I will follow up on [specific date]). Stage the draft for my approval. Do not send anything.
```

**Prompt 2: Generate a Multi-Channel Campaign**

```
I want to reach this seller through multiple channels. Generate drafts for:
- Phone script (cold call)
- LinkedIn connection request
- Mailed letter (will send via USPS to their business address)

Use the strategic/related-business archetype. All three messages should be consistent in positioning but tailored to the channel norms. Stage all drafts for my review.

[Then provide the same seller + my details as Prompt 1]
```

**Prompt 3: Cold Email — the Puppy Method**

```
Draft a cold outreach email to this seller using the EPIC "puppy method":

Seller details: [name, business name, industry, city/state, a specific detail I noticed — reviews, longevity, reputation]
My positioning: [private investor / owner of a related [industry] business / capital provider]
My credibility: [companies helped, deals done, outcome I can reference]

Format:
- Curiosity-based subject line (e.g. "Quick question about [Company]").
- Note at the top: [PLACE A CUTE PUPPY/KITTEN IMAGE HERE] — the playbook reports this tested ~75% higher open rate (Frasier's stated result, not independently verified).
- Frame as "exploring opportunities" / "bringing on a partner or exploring an exit," NOT "I want to buy your business."
- Reference the specific detail I noticed, state what I do in one line, and ask for a 15-minute call this week or next.
- Optional P.S. with a case study link.

Keep it under 150 words. Stage it for my approval — do not send anything.
```

**Prompt 4: Follow-Up After No Response**

```
I sent the [channel] outreach [X days/weeks] ago and got no response. Draft a polite follow-up message that re-states the value proposition, acknowledges they are busy, and gives them an easy out if they are not interested. Keep it brief and non-pushy.

Original message sent: [paste your original outreach here]
```

## The Loop

The outreach engine is Step 1 of the 3-step sequence. Your goal is to get a response. The EPIC funnel's stated benchmark is 60 responses per 100 outreaches — expect real cold-channel numbers to run well below that, and judge your trend rather than the ceiling. If your response rate stalls or falls, troubleshoot: (1) Is your buy-box too narrow or your target list too cold? (2) Is your positioning believable (do you have a credible company or track record to reference)? (3) Are you using the strategic angle when available (it reliably out-responds the cold-investor angle because it reads as partnership, not acquisition)? Track every outreach in a spreadsheet. Note the channel, date sent, response received (yes/no), and outcome (moved to call / not interested / no response). After 20 outreaches, review your data and refine your approach. If a seller responds positively, move immediately to discovery-interviewer to book the first call.

**No outreach is wasted — the three outcomes.** Every owner you reach lands in one of three buckets: (1) **acquire** — wants to sell, move to discovery and the AQ Score; (2) **CFE / agency client** — not ready to sell but the business is real and needs help, so pivot to `cfe-converter` and pitch consulting-for-equity instead of walking away; (3) **referral** — not a fit, but ask who else they know in your vertical. A "no" to selling is a fork, not a dead end.

## Pitfalls

1. **Sending generic bulk messages without personalization.** The EPIC scripts are templates, not copy-paste. If you send 50 identical LinkedIn messages, you will get reported for spam and your response rate will tank. Always personalize with the seller's name, business name, industry, and one specific observation (size, location, longevity, or a detail from their website).

2. **Using the wrong archetype for the seller's situation.** The distressed-capital-provider angle only works if the business actually shows distress signals (declining reviews, missed payroll rumors, obvious cash crunch). If you approach a healthy, profitable seller with a distressed pitch, they will be offended. Default to strategic/related-business unless you have clear evidence of distress.

3. **Not moving the channel up fast enough.** The goal of every outreach is to get to a live phone call or Zoom. If a seller replies to your LinkedIn message, do not spend three days exchanging DMs. Reply once with enthusiasm, then immediately propose a 15-minute call and send a calendar link. LinkedIn/DM/email are stepping stones, not the destination.

4. **Sending outreach without preparing for the response.** If 100 outreaches yield 60 responses, you will need to handle 60 inbound messages within a few days. Before you hit send on a batch, make sure you have time blocked to respond quickly, a calendar link ready to share, and your discovery script prepared. Slow responses kill momentum.

5. **Giving up after one message.** The follow-up message (Prompt 4) often converts better than the initial outreach because it shows persistence and seriousness. If you get no response after the first message, wait 5 to 7 days, then send a polite follow-up. Do not follow up more than twice. Three messages with no response means they are not interested.

## Output

You receive a complete outreach draft (or multiple drafts for multiple channels) staged in the Claude conversation window. The draft includes the opening line, the pitch (framed for your chosen archetype), the ask (typically "can we schedule a brief call"), and next-step logistics (your phone number, calendar link placeholder, or follow-up commitment). Copy the draft into your email client, LinkedIn message box, letter template, or phone script document. Edit as needed. Send when ready. Log the outreach. Wait for the response. If the seller replies positively, thank them and immediately move to book a discovery call using the discovery-interviewer skill.
