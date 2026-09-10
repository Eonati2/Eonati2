---
name: cleaning-os-voice
description: MANDATORY voice layer for every customer-facing word in the Commercial Cleaning Client Acquisition OS — Gumroad copy, sales pages, emails, outbound sequences, follow-ups, ads, proposals, product documentation, and anything a prospect or buyer will read. Use BEFORE drafting and AGAIN before sending. Routes the copy chain and overrides generic copywriting guidance. Also use when the user mentions brand voice, de-slop, "sounds like AI", "make this human", or asks for copy review.
---

# Voice — Commercial Cleaning OS

**Mandatory for anything a prospect or customer reads.** Internal notes, CRM fields and research
docs are exempt.

---

## 1. The goal, stated correctly

**The goal is not to sound human. The goal is to have something worth saying and to say it plainly.**

An anti-AI word list is the weakest possible version of this. Strip every banned word from an empty
sentence and it is still an empty sentence. What actually separates real writing from generated
writing is **specificity, evidence, a point of view, and the customer's own language** — and this
project has an unusual advantage there, because the evidence rules are already enforced upstream.

**The strongest anti-slop mechanism here is not a style rule. It is `Trigger_Event.evidence`.**
Copy that must trace every claim to a dated, sourced observation cannot drift into generic
marketing language, because generic language has nothing to trace.

---

## 2. The reader

A cleaning company owner with 3–25 staff, reading on a phone, between job sites, who gets twenty
agency emails a week and deletes nineteen. Or a practice manager who runs everything non-clinical
at a dental office and has four minutes.

Neither is impressed by writing. Both are looking for a reason to stop reading.

---

## 3. Do not

- Try to sound impressive
- Announce what you are about to say — *"Let's dive in", "Here's the thing", "In this guide we'll"*
- Use corporate filler
- Turn every thought into a three-part list
- Use fake conversational openers — *"Let's dive in", "Buckle up"*
- Write *"In today's fast-paced world"* or any variant
- Use **unlock · elevate · transform · revolutionize · game-changing · seamless · leverage ·
  robust · streamline · empower · supercharge · effortless · cutting-edge · best-in-class ·
  delve · tapestry · testament · landscape** — unless the specific context genuinely requires
  the literal word
- Polish away personality
- Make every paragraph the same length
- Manufacture enthusiasm
- Manufacture urgency
- **Manufacture proof**

## 4. Do

- Prefer specific observations to adjectives
- Prefer short sentences
- Vary sentence length naturally
- Use contractions
- Allow the occasional fragment
- Say the concrete thing: *"$600 a month"*, not *"significant recurring revenue"*
- Use the customer's words — *walkthrough, bid, accounts, recurring, getting in the door* — never
  *pipeline, ICP, sequence, cadence, TAM* in customer-facing copy

**The test:** if a sentence sounds like something a marketing department would write, rewrite it
like something a sharp business owner would actually say.

---

## 5. The three-question gate — from `copywriting-concrete`

Every line carrying weight must pass:

1. **Can I visualize it?** — *"23 businesses in Tampa that moved last quarter"*, not *"targeted
   prospect intelligence"*
2. **Can I falsify it?** — a claim that cannot be checked is decoration
3. **Could nobody else sign it?** — if a competitor could put their logo on the sentence, delete it

Three nos, rewrite. **Question 2 is the same discipline as the project's evidence rule**, arriving
from a different direction: *"they don't have a cleaner"* fails because it cannot be checked;
*"they opened on MacArthur on 14 August"* passes because it can.

---

## 6. The chain

Do not ask five skills to rewrite each other. Run it in order, once.

```
1. copywriting            structure and argument        (Corey Haines)
2. copywriting-concrete   make it concrete and ownable  (Harry Dry method)
3. cleaning-os-voice      this file — our reader, our vocabulary, our rules
4. anti-ai-writing-slop   evidence-aware de-slop, smallest useful edit
5. copy-editing           final tighten
```

**Who governs what**

| Question | Decided by |
|---|---|
| What is the argument? | `copywriting` |
| Is the line concrete, falsifiable, ownable? | `copywriting-concrete` |
| Does it sound like us, to our reader? | **this file — final say** |
| Is any claim unsupported? Any generic phrasing? | `anti-ai-writing-slop` |
| Is it tight? | `copy-editing` |
| Cold email specifically | `cold-email-copywriting` replaces steps 2 and 4 — it is scoped to that format |
| Personal-brand voice profile | `tone-of-voice` — **only if a named human byline is needed.** Do not let it invent a persona for the product |

**Steps 3 and 4 are not optional for customer-facing copy.** Everything else can be skipped when
the piece is short.

---

## 7. What we deliberately did not install

| Skill | Why not |
|---|---|
| `jalaalrd/anti-ai-slop-writing` | Aggressive banned-word list aimed at defeating AI detectors. Our goal is truth and specificity, not evasion — and a 50-word blocklist flattens voice while checking nothing about whether a claim is supported. `anti-ai-writing-slop` checks claims and preserves voice, which is the job. |
| `robpalmer99/*` direct-response pack | Excellent craft in a register we have banned. VSLs, urgency mechanics and ClickBank compliance are the toolkit of a business that manufactures scarcity; ours forbids it. It would fight this file on every draft. `copychief` alone is a reasonable later add for a line-by-line sales-page review. |

---

## 8. Hard limits — these outrank style

**No fabricated proof.** No invented testimonials, case studies, client names, statistics, reply
rates, or ROI figures. If there is no customer yet, write *"you'd be one of the first five"* — it
converts better than a fake reference and it survives being checked.

**No claim about a prospect that is not traceable** to something they said or a dated, sourced
observation. The pre-send claim check (`commercial-cleaning-os/crm/routing.md` §6, check 6) tests
merged copy against `Trigger_Event.evidence`.

**No guaranteed outcomes.** Not leads, meetings, walkthroughs, contracts, revenue, or reply rates.
State what will be built and run.

**No manufactured scarcity.** The five-pilot cap is real delivery capacity — say that. Never a fake
deadline or an expiring discount.

**No misleading subject lines.** The one area state law reaches past CAN-SPAM preemption;
California attaches $1,000 per email.

**Internal never goes public.** Revenue plans, model assumptions, funnel math and implementation
doubts stay out of the Gumroad page and every customer-facing document.

---

## 9. Two rewrites

**Sales page**
> ✗ *Unlock a seamless, game-changing system that transforms how your cleaning business generates
> leads and elevates your revenue to the next level.*
>
> ✓ *Most cleaning companies email every business in town. They already have a cleaner, and they're
> not switching because your email was nicer. This finds the ones with a reason to change this
> quarter.*

The second is shorter, names a real objection, and makes a claim you could argue with.

**Outbound**
> ✗ *I hope this email finds you well! I wanted to reach out because I noticed your business and
> thought there might be a great opportunity for us to partner together.*
>
> ✓ *I saw you opened the MacArthur location in August. We do nightly janitorial around Irving —
> if cleaning there is still being arranged, I'd be glad to walk it.*

Note what the second does *not* say: that they have no cleaner. It states the event and offers.

---

## 10. Before it ships

- [ ] Every claim about the reader traces to evidence
- [ ] No fabricated proof anywhere
- [ ] No banned words unless literally required
- [ ] No guaranteed outcomes
- [ ] Sentence lengths vary; not every paragraph is symmetrical
- [ ] Customer's vocabulary, not ours
- [ ] Passes the three-question gate
- [ ] Nothing internal leaked
- [ ] Read it aloud. If you would not say it to an owner standing in front of you, rewrite it
