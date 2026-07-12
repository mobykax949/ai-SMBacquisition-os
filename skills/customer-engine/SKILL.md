---
name: customer-engine
description: Use when modernizing revenue without touching active customer relationships in week one. Claude builds review generation cadence, reactivation campaigns for dormant customers, referral systems, and AI-drafted follow-up sequences you approve before sending.
version: 1.0.0
---

# Customer Engine

## Overview

Most small businesses have revenue sitting dormant in their customer list. Past customers who have not bought in 6 months, happy customers who would refer if asked, completed jobs with no review request, and follow-up sequences that live in the owner's head but never happen consistently. This skill modernizes your revenue engine using AI tools to automate the tasks that drive repeat business and referrals, without changing how you serve active customers. Claude helps you build four systems: (1) a review generation cadence (request reviews 3 to 7 days after job completion), (2) a reactivation campaign for dormant customers (win-back emails for customers who have not purchased in 6+ months), (3) a referral system (ask happy customers to refer, make it easy with a template), and (4) AI-drafted follow-up sequences (nurture leads and past customers with helpful content). The rule: nothing touches active customer relationships in week one. You build and test the systems on past and future customers first.

## When to Use

Run customer-engine after you have stabilized operations and documented a few core processes (you have completed the owner-dependency-audit and have at least 5 SOPs). You need access to your customer list (names, emails, last purchase date, and ideally a tag for happy versus problem customers). If your customer data is scattered across spreadsheets, QuickBooks, and email, consolidate it into one CRM or spreadsheet first. Customer-engine works best on businesses with at least 100 past customers and a repeat purchase cycle (customers buy again within 6 to 24 months).

## Steps

1. **Export your customer list and segment it.** Pull names, emails, phone numbers, last purchase date, and total lifetime spend. Segment into four groups: (1) Active customers (purchased in the last 90 days), (2) Recent customers (last purchase 3 to 6 months ago), (3) Dormant customers (last purchase 6+ months ago), (4) One-time customers who never returned. Done when you have the list and can count how many customers are in each segment.

2. **Build the review generation system with Prompt 1.** Reviews drive new customer acquisition (most buyers check Google or Yelp before calling). Claude drafts a review request sequence: (1) thank-you email sent 3 days after job completion with a review link, (2) follow-up reminder sent 7 days later if no review posted. You approve the drafts, then set up automation (using your email tool, CRM, or a service like Mailchimp or ActiveCampaign). Done when the system is live and every completed job triggers the review request automatically.

3. **Launch the dormant customer reactivation campaign with Prompt 2.** These are customers who bought from you once or multiple times, then went silent. They know you, they trust you (or they did), and they are much cheaper to reactivate than acquiring new customers. Claude drafts a 3-email win-back sequence: (1) "We miss you" email with a special offer or reminder of services, (2) value-add email (helpful tip, seasonal reminder, or case study), (3) last-chance email ("If you do not need us anymore, no problem, but here is one last offer"). Done when the sequence is drafted, you approve it, and you send it to the dormant segment (not the active customers).

4. **Set up the referral system with Prompt 3.** Most customers will refer if asked, but you have to ask. Claude drafts a referral request email and a referral landing page (simple Google Form or Typeform where referred customers can request a quote). You send the referral request to happy customers (those who left a 5-star review, or customers with 3+ repeat purchases). Include an incentive if appropriate (discount on next service, gift card, etc.). Done when you have sent the referral ask to at least 20 happy customers and the form is live.

5. **Create AI-drafted nurture sequences for leads and past customers with Prompt 4.** These are the follow-ups that should happen but never do consistently (the quote you sent that got no response, the customer who bought once and you never followed up, the lead who asked a question and you answered but never checked back). Claude drafts 5-email nurture templates you can customize and reuse: (1) quote follow-up, (2) post-purchase check-in, (3) seasonal reminder, (4) educational value-add, (5) upsell or cross-sell. You review and approve each template. Done when you have 5 reusable email templates saved in your email tool or CRM.

6. **Measure results after 30 days.** Track: reviews posted (goal: 10+ new reviews in 30 days), dormant customers reactivated (goal: 5 to 10 percent response rate on the win-back campaign), referrals received (goal: 3+ referrals from the ask), and nurture responses (goal: 10 to 20 percent reply rate on follow-up emails). Done when you have the baseline data and know which systems are working.

7. **Iterate and expand.** After 30 days, refine the messaging based on what got responses and what did not. Expand the review request system to include SMS if email is not getting opens. Add a second referral ask 90 days after the first for customers who did not respond. Build out the nurture sequences for other segments (new leads, high-value customers, seasonal buyers). The customer engine is not a one-time project. It is an operating system that runs in the background and compounds over time.

## The Prompts

**Prompt 1: Build the Review Generation System**

```
I want to build an automated review request system for my business. I need two emails:

1. **Thank-you + review request email** (sent 3 days after job completion):
   - Thank the customer for their business
   - Mention the specific service we completed (I will customize this per customer)
   - Ask them to leave a review on Google (or Yelp, depending on my industry)
   - Include a direct link to the review platform (I will insert the link)
   - Keep it short, friendly, and not pushy

2. **Reminder email** (sent 7 days later if no review posted):
   - Gentle reminder that their feedback helps us serve future customers
   - Same review link
   - Option to give private feedback if they had a problem (send to my email instead)

Draft both emails. Use a conversational tone appropriate for a small business owner. I will review and customize before sending.
```

**Prompt 2: Draft the Dormant Customer Win-Back Campaign**

```
I have a list of customers who purchased from me 6+ months ago and have gone silent. I want to reactivate them with a 3-email win-back sequence. My business is [describe your service, e.g., "residential HVAC repair and maintenance"].

Draft these three emails:

1. **"We miss you" email:**
   - Acknowledge we have not heard from them in a while
   - Remind them of the services we offer (especially seasonal ones if applicable)
   - Include a special offer (I will decide: discount, free inspection, etc.)
   - Low-pressure, friendly tone

2. **Value-add email** (sent 7 days after email 1 if no response):
   - Helpful tip related to my service (e.g., "5 signs your HVAC system needs maintenance")
   - Case study or success story from a recent customer
   - Soft call-to-action (book a service or call with a question)

3. **Last-chance email** (sent 14 days after email 2 if no response):
   - "If you do not need us anymore, no problem, but here is one last offer"
   - Time-limited discount or incentive
   - Clear unsubscribe option (respect their choice if they are done)

Keep each email under 150 words. Conversational, not salesy.
```

**Prompt 3: Create the Referral Request System**

```
I want to ask my happiest customers to refer new business. Draft:

1. **Referral request email:**
   - Thank them for being a great customer
   - Ask if they know anyone who could use my services (be specific about the ideal referral: homeowners, businesses, specific industry, etc.)
   - Make it easy: include a link to a referral form (I will create the form) or tell them to reply with the contact info
   - Offer an incentive if appropriate (I will decide: $50 off next service, $25 Amazon gift card, etc.)

2. **Referral form questions** (for a Google Form or Typeform):
   - Referred customer name
   - Referred customer email or phone
   - What service do they need?
   - Any notes (optional)
   - Your name (the person making the referral)

Keep the email warm and personal, not transactional.
```

**Prompt 4: Draft 5 Reusable Nurture Email Templates**

```
I need 5 email templates I can reuse for following up with leads and past customers. My business is [describe service]. Draft:

1. **Quote follow-up** (sent 3 days after sending a quote that got no response):
   - Check in, ask if they have questions
   - Offer to adjust the quote or schedule a call
   - No pressure, just helpful

2. **Post-purchase check-in** (sent 7 days after completing a job):
   - How is everything working?
   - Anything we can help with?
   - Reminder of related services (upsell, but soft)

3. **Seasonal reminder** (sent before a peak season, e.g., HVAC before summer):
   - Reminder to book before the busy season
   - Why booking early saves them time and money
   - Clear call-to-action (book now)

4. **Educational value-add** (evergreen content for nurturing leads):
   - Helpful tip or how-to (e.g., "How to extend the life of your equipment")
   - No sales pitch, just value
   - Builds trust for future purchase

5. **Upsell or cross-sell** (sent to existing customers who bought service A, pitch service B):
   - You already trust us for [service A], did you know we also do [service B]?
   - Brief benefit statement
   - Easy next step (call, book online, or reply for a quote)

Keep each template under 100 words. Friendly, helpful, not pushy.
```

## The Loop

Build the four systems (review generation, dormant reactivation, referral ask, nurture templates) in month one. Measure results at day 30. Refine the messaging based on open rates, response rates, and conversions. Expand to new customer segments in month two (add win-back for 3 to 6 month dormant customers, add a second referral ask for customers who did not respond the first time, add nurture sequences for high-value customers). By month three, the systems should be running automatically with minimal owner involvement. The compounding effect is significant: 10 new reviews lift your Google ranking, 5 reactivated customers add $10K to $50K in revenue, 3 referrals per month add 30+ new customers per year. The customer engine does not replace sales. It multiplies the value of the customers you already have.

## Pitfalls

1. **Sending reactivation emails to active customers.** If you blast the win-back campaign to your entire list including customers who just bought last week, you look disorganized and hurt trust. Segment carefully. Active customers get different messaging than dormant ones.

2. **Asking for reviews too soon after the job.** If you send the review request the same day you completed the job, the customer has not had time to experience the result. Wait 3 to 7 days. For services with longer outcome cycles (e.g., pest control, landscaping), wait 2 weeks.

3. **Over-automating without review.** If you set up the email sequences and never look at responses, you will miss opportunities. Check your inbox daily for replies to nurture emails. If a customer responds with a question or concern, reply personally, do not send another automated email.

4. **Not offering an incentive for referrals.** Some customers will refer without an incentive, but most need a nudge. A $25 gift card or discount costs you $25 and can bring a customer worth $500 to $5,000 lifetime value. The ROI is obvious.

5. **Giving up after one campaign.** If you send the dormant win-back sequence and only 3 percent respond, that is normal. Do not abandon the system. Refine the messaging, test a different offer, and run it again in 90 days. The customers who did not respond this time may respond next time when their situation changes.

## Output

You receive four complete revenue systems ready to deploy: (1) a 2-email review generation sequence (thank-you + reminder) with automation instructions, (2) a 3-email dormant customer win-back campaign targeted at customers who have not purchased in 6+ months, (3) a referral request email with referral form questions, and (4) 5 reusable nurture email templates for quote follow-up, post-purchase check-in, seasonal reminders, educational value-add, and upsell/cross-sell. After 30 days of operation, measure against the working goals: 10+ new reviews, 5 to 10 reactivated customers, 3+ referrals, and 10 to 20 percent response rates on nurture emails — these are targets to calibrate against, not promised results; falling short means iterate the messaging, not that the system failed. These systems do not require you to change how you serve active customers. They monetize the customer base you already have. Over time, the compounding effect adds tens of thousands of dollars in revenue per year without additional marketing spend.
