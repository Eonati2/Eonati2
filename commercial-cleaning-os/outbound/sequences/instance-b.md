# Instance B Sequences — product content

Templates the customer runs against facilities in their own metro. **This ships inside the Core
OS**, so it is written for a cleaning company owner, not for us.

## Rules — carried into the product
1. **Observation → relevance → service connection → low-friction CTA.** Four beats, nothing more.
2. **State the event. Never state what it implies.** You saw a permit; you did not see their
   contract.
3. **Under 90 words.**
4. **Reply-based CTA.** Not a link, not a calendar, not a brochure.
5. **Plain text**, real signature, real postal address, working opt-out.
6. **Never mention a review you found.** It reads as surveillance and asserts something you cannot
   support.

**The four-beat pattern:**
```
"I noticed [dated, factual observation]."
"We provide recurring commercial cleaning in [area]."
"If you're reviewing coverage for [site], I'd be glad to understand the scope."
"Would a short call or walkthrough next week be useful?"
```

---

## B-PM-NEW · Property management, new building
*Trigger T4. Persona: Property Manager. Highest leverage — one relationship, several buildings.*

**E1 · day 0 — subject: `the Elm Street building`**
```
Hi {{first_name}} — I noticed {{management_co}} recently added the Elm Street
property to your portfolio.

We handle recurring janitorial for commercial buildings around {{area}}.

If you're reviewing cleaning coverage there — or inherited an arrangement
you're still evaluating — I'd be glad to walk it and give you a scoped
number.

Would a short call this week be useful?

— {{name}}, {{company}}
```

**E2 · day 4 — subject: `re: the Elm Street building`**
```
{{first_name}} — following up briefly.

Most managers I work with want two things from a cleaning vendor: someone who
answers the phone, and no tenant complaints reaching the owner.

Happy to walk the building and put a scoped proposal together, whether or not
anything changes today.

Worth fifteen minutes?
```

**E3 · day 11 — subject: `closing the loop`**
```
{{first_name}} — I'll leave it there.

If it's useful, tell me roughly when the current arrangement comes up for
review and I'll check back then rather than filling your inbox.

Either way, good luck with the new property.
```

---

## B-MED-MOVE · Medical or dental, new location or move
*Triggers T1/T2/T3. Persona: **Practice Manager — not the physician**.*

**E1 · day 0 — subject: `the new {{street}} office`**
```
Hi {{first_name}} — I saw {{practice}} opened at {{street}} last month.
Congratulations.

We do recurring cleaning for medical and dental offices around {{area}} —
nightly and after-hours, with documented restroom and treatment-room
protocols.

If cleaning for the new space is still being arranged, I'd be glad to walk it
and put a scope and price together.

Would Tuesday or Thursday suit for fifteen minutes?
```

Note the phrasing: *"if cleaning is still being arranged"* — a conditional, not an assertion. It
does not claim they have no cleaner.

**E2 · day 4 — subject: `re: the new {{street}} office`**
```
{{first_name}} — one thing worth asking whoever you use: whether they document
what was cleaned, room by room.

For medical spaces it matters when someone asks, and most janitorial
companies don't do it.

Happy to show you what our reporting looks like, no obligation.
```

**E3 · day 11 — the close-out.** Same shape as B-PM-NEW E3.

---

## B-OFF-MOVE · Office or professional, move or new location
*Triggers T1/T2/T3. Persona: Office Manager.*

**E1 · day 0 — subject: `your move to {{street}}`**
```
Hi {{first_name}} — noticed {{company}} moved into {{street}} recently.

We handle nightly and weekly cleaning for offices around {{area}}.

Moves usually mean sorting out a dozen vendors at once. If cleaning is still
on that list, I can walk the space and have a scoped proposal to you in two
days.

Would a quick call this week help?
```

*"Moves usually mean sorting out a dozen vendors at once"* is an observation about moves in
general, not a claim about them. That distinction is the whole rule.

**E2 · day 4 — subject: `re: your move to {{street}}`**
```
{{first_name}} — briefly.

The thing offices most often want fixed is consistency — the same crew, the
same standard, and someone who picks up the phone.

If you're comparing providers, worth asking each one what their response time
is in writing.

Happy to walk the space either way.
```

**E3 · day 11 — the close-out.**

---

## B-OFF-HIRE · Office, facilities hiring
*Trigger T5. Persona: Office or Facilities Manager.*

**E1 · day 0 — subject: `saw the facilities role`**
```
Hi {{first_name}} — saw {{company}} is hiring a facilities manager.

We provide recurring commercial cleaning around {{area}}. When facilities
becomes someone's actual job, vendor arrangements usually get reviewed at
some point.

No rush on my side — if it'd be useful to have a scoped quote on file for
when that happens, I'm glad to walk the space.

Worth a short call?
```

*"usually get reviewed at some point"* and *"no rush"* — this trigger is real but slow, and copy
that pretends it is urgent will read as false.

---

## B-IND-NEW · Industrial, new facility or renovation
*Triggers T2/T6. Persona: Operations Manager.*

**E1 · day 0 — subject: `the {{street}} facility`**
```
Hi {{first_name}} — I saw the {{street}} facility recently cleared occupancy.

We handle recurring cleaning for industrial and warehouse space around
{{area}} — floors, restrooms, break areas, and post-construction cleanup
where it's needed.

If cleaning for the new space isn't settled, I'd be glad to walk it.

Would next week work?
```

Post-construction is a **separate, usually larger, one-off scope**. Price it separately and say so
on site (`../../sales/02-walkthrough.md`).

---

## B-EDU-TERM · Schools and daycares
*Triggers T2/T6 plus term timing. Persona: Director or Business Manager.*

**E1 · day 0 — subject: `cleaning coverage for {{school}}`**
```
Hi {{first_name}} — I work with schools and childcare centres around
{{area}} on recurring cleaning.

I noticed {{school}} {{observation}}.

Most centres I work with care about two things: consistency, and staff who've
been background-checked. Happy to walk the site and put a scope together.

Would a short call before term suits?
```

Timing matters more than the trigger here — before term start and before the summer break.

---

## Follow-up rules — same across all templates

| Touch | Day | Content |
|---|---|---|
| E1 | 0 | Observation + offer to walk |
| E2 | 4 | One genuinely useful point, not a nudge |
| E3 | 11 | Close-out. Ask for the renewal date |
| — | — | **Stop.** → nurture with a review date |

**Three emails, then stop.** A fourth does not win the contract and costs the chance to come back
when something actually changes.

**The close-out is the highest-response message in the sequence**, because it is genuinely final
and asks for one small fact rather than a decision.

---

## Compliance footer — required on every send
```
—
{{name}}, {{company}}
{{street_address}}, {{city}}, {{state}} {{zip}}

You're receiving this because {{account}} appears as a commercial business in
{{area}}. Reply "no thanks" and I'll remove you right away.
```

Plain and human. It satisfies the identification, physical-address and opt-out requirements, and
reads like a person — which draws fewer complaints than an unsubscribe-link block.

**Opt-outs are honored immediately and permanently, across email and phone.** At realistic volumes
a very small number of complaints breaches the 0.3% threshold, and the give-first framing in these
templates is a large part of why complaints stay low.
