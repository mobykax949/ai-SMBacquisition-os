---
name: broker-finder
description: Use when building relationships with business brokers to access pocket listings before they go public. Finds and profiles brokers in a geography and vertical, then drafts a credible buyer introduction (financing ready, buy box attached).
version: 1.0.0
---

# Broker Finder

## Overview

Find and profile business brokers and M&A advisors who specialize in your target geography and verticals, then draft a credible buyer introduction to get on their list for pocket listings before deals go public. Brokers want serious, financed buyers. If you can prove you are ready to close (SBA pre-qualified or 1031 equity locked), they will send you opportunities before they hit BizBuySell. This is Roland Frasier's broker-relationship channel applied to off-market pre-market sourcing. It is the gold lane in the three-lane sourcing architecture.

## When to Use

- You are tired of competing with 10 other buyers on public BizBuySell listings at full asking price
- You want access to deals before they are marketed to the public
- You have financing lined up (SBA pre-qualification letter, 1031 equity parked with a QI, or cash ready) and need deal flow to deploy it
- You want to build long-term broker relationships that feed you opportunities for years

## Steps

1. **Define your target geography and top 2 verticals.** Example: Orange County California, focusing on service businesses (hood cleaning, pool service, laundromats). Brokers specialize. A broker who sells $10M manufacturing businesses in Ohio will not help you find a $2M pool service company in Orange County. Narrow your search.

2. **Ask Claude to web search for business brokers in your geography.** Prompt: "Web search for business brokers and M&A advisors in Orange County California who specialize in service businesses or small businesses under $5M. Return a list: broker name, firm name, website, phone, specialization (if disclosed), recent deals (if visible)." Claude will pull results from Google and broker association directories.

3. **Profile the top 10 brokers.** For each broker, check their website for: deal size focus ($1-5M is your range), verticals they cover, whether they mention seller financing or SBA deals, and recent closed transactions. Ask Claude: "From the broker list above, which 5 brokers are the best fit for my buy box: $1-5M revenue, service businesses, Orange County, SBA 7(a) or seller financing preferred. Rank them and explain why each is a good fit."

4. **Draft a credible buyer introduction.** Brokers get 50 emails a week from tire-kickers. Your intro needs to prove you are serious and financed. Use this structure: (1) who you are (experienced operator or first-time buyer with financing ready), (2) what you are looking for (attach your buy box: geography, revenue, SDE, verticals), (3) proof of financing (SBA pre-qualification letter, 1031 equity amount, or cash available), (4) why you are reaching out (looking for pocket listings before they go public), (5) call to action (15-minute intro call). Keep it under 200 words.

5. **Ask Claude to generate the email.** Prompt: "You are a business acquisition professional. Draft an email to a business broker introducing me as a serious buyer. Include: I am looking to acquire a service business in Orange County, $1-5M revenue, $200K+ SDE, my top verticals are [list], I have SBA 7(a) pre-qualification [or 1031 equity of $X], I prefer off-market or pocket listings before they are publicly listed, and I would like a 15-minute call to introduce myself and share my buy box. Tone: professional, confident, concise. Under 200 words."

6. **Attach your buy box to the email.** Save your buy box as a 1-page PDF (geography, revenue, SDE, verticals, financing, 3 auto-pass criteria) and attach it to the email. This proves you are organized and makes it easy for the broker to know what to send you. Brokers will forward your buy box to sellers who match.

7. **Send the email to the top 5 brokers.** Do not blast 50 brokers at once. Start with 5. If you get no responses in 1 week, refine the email or pick different brokers. If you get 2-3 intro calls booked, you are on the right track. After the intro call, ask: "What deals are you working on right now that match my criteria, even if they are not listed yet?" This is the pocket listing question.

8. **Track broker responses and relationships.** Create a simple spreadsheet: broker name, firm, contact info, intro call date, deals shared, follow-up cadence. Touch base with each broker every 2-4 weeks, even if you are not ready to make an offer on their current deals. The goal is to be top-of-mind when a good deal comes in.

## The Prompts

```
Prompt 1: Web search for business brokers in target geography

You are a deal sourcing strategist. I need to find business brokers and M&A advisors in Orange County California who specialize in selling small service businesses ($1-5M revenue range). Web search for brokers in this geography. Return a table: broker name, firm name, phone, website, specialization (verticals or deal size if disclosed), recent deals closed (if visible on their site or press). Prioritize brokers who mention SBA financing, seller financing, or service industry expertise.
```

```
Prompt 2: Rank brokers by fit and explain why

You are a broker-matching analyst. From the list above, rank the top 5 brokers who are the best fit for my buy box: $1-5M revenue, $200K+ SDE, service businesses (hood cleaning, pool service, laundromats, landscape, car wash), Orange County geography, SBA 7(a) or seller financing preferred. For each broker, write 1-2 sentences explaining why they are a good fit based on their specialization, deal size, or recent transactions.
```

```
Prompt 3: Draft a credible buyer introduction email

You are a business acquisition professional. Draft an email to introduce me to a business broker as a serious buyer. Include these points:

- I am actively looking to acquire a service business in Orange County.
- My buy box: $1-5M revenue, $200K+ SDE, 10+ years in business, boomer owner ready to exit.
- Top verticals: kitchen hood cleaning, pool service, laundromats, car wash, landscape maintenance.
- I have SBA 7(a) pre-qualification [OR: I have $1M in 1031 exchange equity ready to deploy within 120 days].
- I prefer off-market or pocket listings before they are publicly listed, so I can move quickly and avoid bidding wars.
- I would like a 15-minute intro call to share my full buy box and learn about your current opportunities.
- Attach: my 1-page buy box PDF.

Tone: professional, confident, concise. Under 200 words. Subject line: Serious Buyer — Service Businesses, Orange County, Financed & Ready.
```

## The Loop

Send the intro email to 5 brokers every 2 weeks until you have 10-15 active broker relationships. After the intro call, follow up every 2-4 weeks with a short check-in: "Any new opportunities in my verticals since we last spoke?" Track responses in a spreadsheet. When a broker sends you a pocket listing, run the AQ Score (aq-analyzer skill) within 24 hours and respond with interest or pass. Brokers remember buyers who are responsive and decisive. If you ghost them or take 2 weeks to respond, they will stop sending you deals. Speed and professionalism win pocket listings.

## Pitfalls

- **Sending generic cold emails with no buy box attached.** Brokers get 50 "I want to buy a business" emails a week. If you do not include your specific criteria and proof of financing, you look like a tire-kicker. Attach the buy box PDF and mention your financing in the first 3 sentences.
- **Contacting brokers before you are actually ready to buy.** If you do not have financing lined up (SBA pre-qual, 1031 equity, or cash), do not waste broker time. They will ask "are you pre-qualified?" on the intro call. If the answer is no, they will not send you deals. Get your financing lined up first.
- **Blasting 50 brokers at once with a copy-paste email.** Brokers talk to each other. If 5 brokers in the same city get the exact same email from you on the same day, you look like a spam campaign. Start with 5, refine your approach, then expand.
- **Not following up after the intro call.** The intro call is not the close. It is the beginning of a relationship. If you do not check in every 2-4 weeks, the broker will forget about you and send deals to other buyers who stay in touch. Set a recurring reminder.
- **Ghosting a broker after they send you a deal.** If a broker sends you a pocket listing and you do not respond within 48 hours, they will assume you are not serious and stop sending you opportunities. Even if the deal is a pass, reply with "Thank you, this one does not fit my criteria because [reason]. Please keep me in mind for future opportunities in [vertical]."

## Output

A ranked list of 5 business brokers with firm name, contact info, specialization, and fit explanation. A drafted buyer introduction email under 200 words with your buy box attached. A broker relationship tracker (spreadsheet or markdown table) with columns: broker name, firm, contact, intro call date, deals shared, last follow-up, next follow-up due. Save the email draft and tracker in your acquisitions folder. After sending, track responses and book intro calls. The goal is 3-5 active broker relationships feeding you pocket listings every month.
