# Audit — playbook vs. the Roland Frasier / EPIC knowledgebase

Scope: `setup/*.md`, `skills/*/SKILL.md`, `JOURNEY.md`, `prompts/vault.md`, plus
`advisor/*` and `index.html` where they make method claims. Compared against the
distilled KB at `personal-brain/references/` and the full playbook
(`references/epic-kb/acquisition-playbook-full.md`, ~2,520 lines).

Verdict up front: the repo is broadly faithful. The 13-criterion AQ Score, the
13 funding families (A–M) and the 216 count, the 100→60→10→5→1–3 funnel, the
50-question / 6-section deep dive, the 3-phase seller call structure, TTM +
replace-the-owner add-back discipline, the tax-return test, "price OR terms not
both", and the Acquisition Wheel are all stated correctly and consistently. No
file invents AQ point values (the KB flags those as an open item), and nobody
uses the discredited homemade "EPIC = Earnings/People/Industry/Culture" acronym.
The findings below are the exceptions, ranked. Items marked **FIXED** were
corrected in the first pass; items marked **RESOLVED** were actioned in the
second pass (the earlier FLAGGED recommendations — including the CFE surface and
the puppy-email channel — now implemented). Only the deliberate NO CHANGE items
(#12 Acquisition Wheel, #13 minors) remain untouched, by design.

---

## 1. valuation — walk-away/dream prices were inverted — **FIXED**

- **File:** `skills/valuation/SKILL.md`, Step 5.
- **What was off:** Step 5 said walk-away (the *maximum* you will pay) sits "at
  the low end of the multiple range" and dream at "low end of range or below" —
  internally contradictory, and contradicted by the skill's own Prompt 1
  ("walk-away (high multiple)... dream (low multiple)").
- **KB source:** playbook-full §Negotiation (line ~658): dream is the *best*
  case (lowest price / richest terms), "Negotiate for DREAM, land at
  REALISTIC"; walk-away is the ceiling.
- **Fix applied:** walk-away = high end of the range (above it you walk), dream
  = low end or below; added the negotiate-to-dream/land-at-realistic line.

## 2. discovery-interviewer — inverted the 70% Rule — **FIXED**

- **File:** `skills/discovery-interviewer/SKILL.md`, The Loop.
- **What was off:** it told users that walking away from *more than 70%* of
  deals after the first call means "your sourcing is bad." Frasier's rule is
  the opposite: the first conversation is *supposed* to kill ~70% of deals.
- **KB source:** playbook-full line 45–48 ("THE 70% RULE — Cut out 70% of bad
  deals in first conversation"); `epic-acquisition-playbook.md` P0.
- **Fix applied:** killing ~70% on the first call is the filter working;
  recalibrated the failure bands (too few kills = weak filtering, >90% = bad
  sourcing).

## 3. loi-drafter — 24-hour rule was only half the rule — **FIXED**

- **File:** `skills/loi-drafter/SKILL.md`, Step 1 (+ Pitfall 1 context).
- **What was off:** the skill framed the 24-hour rule purely as "sleep on it
  before sending the LOI." The canonical rule is *stated to the seller
  upfront* ("I never make decisions on the spot... I always take 24 hours") as
  protection against pressure tactics — and includes the counter-move when a
  seller demands a same-day decision.
- **KB source:** playbook-full lines 667–689 ("The 24-Hour Rule").
- **Fix applied:** added the upfront-declaration form and the walk response.
  (`prompts/vault.md` already had the correct form.)

## 4. outreach-engine — fabricated statistic — **FIXED**

- **File:** `skills/outreach-engine/SKILL.md`, The Loop.
- **What was off:** claimed the strategic/related-business angle "beats cold
  investor by 30 percent." No such number exists anywhere in the KB; the
  scripts file says only "lower threat, higher response."
- **KB source:** `epic-outreach-scripts.md`, Key operating insights.
- **Fix applied:** removed the number, kept the directional (and true) claim.

## 5. dd-engine — missing Frasier's DD philosophy — **RESOLVED**

- **File:** `skills/dd-engine/SKILL.md`.
- **What was off:** the skill presented a strictly sequential, pre-close,
  5-phase DD with no mention of Frasier's signature operating principles:
  move fast; use an SPV; include a break-up/out-clause; complete much of DD
  *shortly post-acquisition*. It also lacked the "70% of deals die in DD —
  this is normal" expectation-setting.
- **KB source:** `epic-due-diligence-roadmap.md` ("Frasier's Thoughts on DD");
  playbook-full §Phase 6 (3-stage DD: initial screen pre-LOI → detailed DD
  post-LOI → final verification week-before-close) and closing "Remember"
  list (line ~2494).
- **Fix applied:** added the speed/SPV/out-clause principles and the 70%-die
  norm to the Overview.
- **Resolution (2nd pass):** added a sentence to the Overview labeling the
  conservative, mostly pre-close five-phase sequence as a *deliberate
  softening* of Frasier's move-fast / post-close-DD stance — a first-time-buyer
  safety choice, with a note that an experienced operator on a clean SPV
  structure may legitimately push more DD past closing. The divergence from
  the playbook's 3-stage DD is now honest on the page rather than silent.

## 6. Red-flag thresholds — internally inconsistent, stricter than KB — **RESOLVED**

- **Files:** `skills/dd-engine/SKILL.md`, `prompts/vault.md`,
  `skills/discovery-interviewer/SKILL.md` (all use >30% single-customer
  concentration, >10% YoY decline); `advisor/advisor-instructions.md` (used
  >40%).
- **What was off:** two problems. (a) Internal: the advisor said 40% where
  everything else says 30% — **fixed** by aligning the advisor to 30%.
  (b) Attribution: the playbook's own "Red Flags to Exit Early" list uses
  *>50%* single-customer concentration and *>20%* YoY revenue decline
  (playbook-full §Phase 3). The repo's 30%/10% thresholds are stricter house
  rules — reasonable, but nothing in the repo says so.
- **Resolution (2nd pass):** added an attribution note to dd-engine Prompt 2
  stating that the 30% single-customer / 10% YoY-decline thresholds are
  deliberately tighter *house rules* than Frasier's own exit-early triggers
  (>50% concentration, >20% decline), and that users should not attribute the
  tighter numbers to Frasier. The dd-engine lesson (Lesson 14) already carried
  the same caveat.

## 7. Multiple landscape — house ranges presented as the method — **FIXED (labeling)**

- **Files:** `skills/valuation/SKILL.md` (2.4–3.5x / 4.0–6.0x ranges),
  `skills/multiple-builder/SKILL.md` (50-point ladder mapping to 2.0–5.5x).
- **What was off:** the KB gives point anchors — owner-op **2.4x SDE** (blue
  box), professionally managed <$2M profit **4.0x EBITDA** (green box), PE
  **10.8x** (down from 15x+ in 2021), NASDAQ **18.7x** (down from 27x), "buy
  blue/green, sell PE" — not ranges, and no scoring ladder. The repo's bands
  and the multiple-builder's 0–50-point rubric are useful house constructs
  but read as if they were Frasier's.
- **KB source:** playbook-full lines 458–463; `epic-acquisition-playbook.md` P4.
- **Fix applied:** valuation now anchors on the four KB values (adding the
  previously missing 18.7x public tier and buy-low/sell-PE framing) and
  labels the bands "working bands this system uses, not Frasier's table";
  multiple-builder's ladder now carries the same disclaimer.

## 8. Tax-return variance threshold drift — **FIXED**

- **Files:** `prompts/vault.md` said >10%; `skills/valuation/SKILL.md` and
  `skills/dd-engine/SKILL.md` say >5%.
- **KB source:** the KB states the tax-return test ("P&L must match Schedule
  C") but gives no numeric tolerance — so this is a house rule that must at
  least be consistent. Aligned vault to 5%.

## 9. Discovery — napkin offer / "better terms, better offer" missing — **FIXED**

- **File:** `skills/discovery-interviewer/SKILL.md`, Step 5.
- **What was off:** the seller questionnaire's Step 4 close includes telling
  the seller the initial offer comes back as a "napkin offer" and explicitly
  planting "the better the terms, the better the offer" — the lever that
  steers sellers toward seller financing. The skill had the 6% scarcity hook
  and the financials ask but dropped this.
- **KB source:** `epic-seller-questionnaire.md`, Step 4 + Key operating insights.
- **Fix applied:** added one sentence to Step 5.

## 10. CFE (consulting-for-equity) absent from the system — **RESOLVED**

- **Files:** whole plugin / `JOURNEY.md`. CFE appears only as a teaser in
  `advisor/README.md` ("paid community edition") and one passing word in the
  deal-evaluation context.
- **What's off:** CFE is a full Frasier pillar — the 10/10/10 model (greater
  of 10% of profits or $10k/mo, plus 10% of exit), a 7-module bonus course,
  equity-vesting rules, tax workarounds, five case studies — and in Max's own
  Koby playbook it is one of the three outcomes of every outreach
  ("acquire / agency client / referral — no outreach is wasted"). The skill
  pack has no CFE surface at all, so the outreach skills treat "not ready to
  sell" as a dead end when the method treats it as a second monetization path.
- **KB source:** `cfe-blueprint.md`; `koby-ventures-playbooks.md` (Magic
  Intersection); `epic-kb-inventory.md` (CFE 7-module course).
- **Resolution (2nd pass):** built a full CFE surface (now a 22-skill pack).
  - New skill `skills/cfe-converter/SKILL.md`: spots CFE candidates, runs the
    "other eye" upside hunt, and structures the deal on the 10/10/10 model
    (greater of 10% of profits or $10k/month, plus 10% of exit), permanent
    holdco-level equity, performance-vested off a baseline, with the
    tax-on-receipt workarounds (profits-only interest / new-co) flagged for a
    CPA. Grounded strictly in `cfe-blueprint.md` and `koby-ventures-playbooks.md`.
  - New lesson `lessons/08b-cfe-converter.md` (per `_TEMPLATE.md`), wired into
    `scripts/build-lessons.py` between outreach (08) and aq-analyzer (09).
  - `JOURNEY.md`: added the fork off `outreach-engine` (step 3b) and off
    `discovery-interviewer`, plus the Magic Intersection framing (acquire /
    CFE / referral — no outreach wasted) in the Branch B table and the mermaid
    diagram.
  - CFE fallback pointer added to the Loop of `outreach-engine` and
    `discovery-interviewer` SKILL.md and both lessons.
  - Plugin manifests (`plugin.json`, `marketplace.json`) updated 20 → 22 skills.
  - **One open item flagged in the skill itself:** the KB inventory references a
    higher "20/20/20" CFE variant but the downloaded materials give no terms;
    the skill notes 10/10/10 as the documented default and says NOT to invent
    20/20/20 numbers — confirm against source before use.

## 11. Outreach — puppy-email technique missing — **RESOLVED**

- **File:** `skills/outreach-engine/SKILL.md`.
- **What's off:** the playbook's cold-email chapter includes the tested
  "puppy/kitten image" email (75% higher open rate) and email wasn't one of
  the skill's five channels (the skill mirrored the outreach-scripts PDF's
  five channels, so this was a completeness gap vs. the wider playbook, not
  an error).
- **KB source:** playbook-full lines 134, 259–263; `epic-acquisition-playbook.md` P2.
- **Resolution (2nd pass):** added **cold email as the sixth channel** across
  the description, overview, Step 1, and Prompt 1 channel lists, plus a new
  dedicated **Prompt 3 (the puppy method)**: curiosity subject line, a
  puppy/kitten image placeholder, and "exploring opportunities" framing. The
  75% figure is explicitly labeled as Frasier's stated test result, not an
  independently verified benchmark (do not present it as a guarantee). The
  outreach-engine lesson (Lesson 08) now reflects the sixth channel, the
  puppy method, and a "try the puppy method" prompt.

## 12. Acquisition Wheel — two spoke lists exist in the KB itself — **NO CHANGE**

- **Files:** `skills/journey-navigator/SKILL.md`, `JOURNEY.md`, `index.html`
  use Competitors / Media / Teams / Products / Supply / IP / MRR.
- **Note:** the KB inventory (course structure) gives that 7-spoke list; the
  playbook's $100M path text gives "leads, products, services, verticals,
  recurring revenue." The repo consistently uses the course version, which is
  the more canonical artifact. Documented here so nobody "fixes" it into the
  other list.

## 13. Minor observations — **NO CHANGE**

- `advisor/advisor-instructions.md` says "unrealistic price (>4x SDE for
  owner-op business)" as a dealbreaker — not a KB number, but a sane
  derivative of the 2.4x anchor; acceptable as a labeled house rule.
- `prompts/vault.md` "REALISTIC (typically 10-20% below asking)" — house
  heuristic, KB-silent; harmless.
- Koby's own playbook describes the AQ scorecard as "12-criteria weighted";
  the canonical Frasier artifact is 13 criteria. The repo correctly uses 13
  everywhere. (The discrepancy lives in the KB, not the repo.)
- `epic-glossary.md`'s WWYDWTM ("what would you do with the money") question
  is represented in discovery/deal-stacker via seller-motivation capture. OK.
- The buy-box income anchor (reverse-engineer size from required SDE) was a
  previously found-and-fixed gap; verified present in `setup-my-workspace`,
  `buy-box-builder` Step 0, and `index.html`.

---

*Audit run 2026-07-10 on branch `fable5/lessons-audit`; second pass same day
resolved the flagged items (#5, #6, #10, #11). KB paths are absolute under
`/Users/veloxp/dev/personal-brain/references/`.*
