# Final Asset Audit
**2026-09-11** · 14 files in `customer-product/` · restructured to the 00–13 package

Sources in `customer-product/src/`. Restructured 2026-09-11: the ICP and decision-maker material split into two documents, and the package renumbered 00–13. PDFs rendered from those sources; both workbooks built from
scripts. Regenerating any file is reproducible.

---

## 1. Asset table

| # | Filename | Exists | Customer-facing | Contamination-free | Reviewed | Status |
|---|---|---|---|---|---|---|
| 00 | `00-START-HERE.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 01 | `01-CLIENT-ACQUISITION-OS.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 02 | `02-ACCOUNT-TRIGGER-TRACKER.xlsx` | PASS | PASS | PASS | **PASS** | **Ready** — formulas verified |
| 03 | `03-TRIGGER-LIBRARY.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 04 | `04-ICP-AND-TARGETING.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 05 | `05-DECISION-MAKER-GUIDE.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 06 | `06-PROSPECTING-WORKFLOW.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 07 | `07-OUTREACH-SEQUENCES.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 08 | `08-REPLY-HANDLING.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 09 | `09-WALKTHROUGH-SYSTEM.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 10 | `10-PROPOSAL-SYSTEM.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 11 | `11-30-DAY-IMPLEMENTATION.pdf` | PASS | PASS | PASS | PASS | **Ready** |
| 12 | `12-METRICS-SCOREBOARD.xlsx` | PASS | PASS | PASS | **PASS** | **Ready** — formulas verified |
| 13 | `13-AUTOMATION-BLUEPRINT.pdf` | PASS | PASS | PASS | PASS | **Ready** |

**14 of 14 exist. No placeholders.**

---

## 2. Contamination audit

Scanned every source for: Instance A/B language · our pricing · our former service tiers
strategy · our own funnel · repo paths · internal filenames · agent instructions · our kill/continue
rules.

**Result: clean.** Two scanner hits reviewed and cleared:

| Hit | Verdict |
|---|---|
| "your pipeline" in `00-START-HERE` | Customer's pipeline, not ours. Correct usage. |
| "Kill switch" in `12-AUTOMATION-BLUEPRINT` | The customer's own stop-all-sending control, which they should have. Not our internal rules. |

Two words changed on voice grounds: "highest-leverage" → "most work per conversation" (twice).
"Leverage" is on the banned list and there was a plainer way to say it.

### What was kept out, and why it mattered
`icp.md`, `personas.md` and `reply-routing.md` in the internal repo each contained **both** our
targeting logic and the customer's. These were rewritten from scratch rather than extracted, which
is the only reliable way to avoid shipping the half aimed at the buyer. The internal files remain
internal; nothing was copy-pasted.

**Never shipped, verified absent:** our pilot sales motion · our own outbound sequences · the
internal copy review · the skill dependency map · anything under `research/`.

---

## 3. Formula verification — done

**Both workbooks were evaluated and every formula checked against an expected value.**

LibreOffice cannot load any `.xlsx` in this environment (a two-cell control file fails too), so an
earlier version of this audit listed recalculation as an outstanding manual check. It isn't now:
the `formulas` library evaluates the workbooks directly.

**Result: 25 of 25 logic checks pass. No `#REF!`, `#N/A`, `#VALUE!` or `#DIV/0!` anywhere.**

| Workbook | Checks | Result |
|---|---|---|
| `02-ACCOUNT-TRIGGER-TRACKER.xlsx` | 16 | All pass |
| `12-METRICS-SCOREBOARD.xlsx` | 3 | All pass |
| `ACCOUNT-TRACKER-LITE.xlsx` (free) | 6 | All pass |

Verified by value, not just by absence of errors: score totals sum correctly · band thresholds fire
at the right boundaries · empty rows stay blank rather than showing zero · trigger tier, score and
window all resolve from the lookup table · freshness compares age against the right window ·
pipeline counts match the example rows · all seven health checks return zero · scoreboard ratios
stay blank on no data and the week dates step by seven · free-tracker scoring and banding match.

### The bug this caught

**The Pipeline health check "active accounts with no next action" returned 396 instead of 0.**

`COUNTIFS(range,"<>")` is ambiguous across engines: it can mean "not blank" or "not equal to an
empty string", and the second reading matches every empty row in the sheet. The check that exists
to catch a data-quality problem was itself producing a false alarm on 396 rows — which would have
trained the user to ignore it, making every other health check worthless too.

Rewritten as `SUMPRODUCT` with explicit conditions, which is unambiguous in any engine. Now returns 0.

**Still worth opening once in Excel** before publishing — evaluation libraries and Excel are not
identical, and a visual check costs two minutes. But it is a confirmation now, not the verification.

## 4. Customer quality test

Read as someone who just paid $197 and has no access to the repo.

| Question | Answer |
|---|---|
| Do I understand what this is? | Yes — `00` and `01` |
| Do I know what to do first? | Yes — `00` gives an hour-one list |
| Can I use the tracker? | Yes — Quick Start and Instructions tabs, four worked example rows |
| Can I find target accounts? | Yes — `04` names search terms and sources |
| Can I score them? | Yes — dropdowns, automatic total and band |
| Can I identify a trigger? | Yes — `03`, sixteen with sources and windows |
| Can I contact the right person? | Yes — `05` maps role to building type |
| Can I run the outreach? | Yes — `06`, six sequences, fill the brackets |
| Can I handle a reply? | Yes — `07`, ten reply types |
| Can I run a walkthrough? | Yes — `08`, checklist and two pricing methods |
| Can I build a proposal? | Yes — `09`, seven sections and a three-tier table |
| Can I measure results? | Yes — `11`, plus definitions so the counting stays consistent |
| Can I understand the automation? | Yes — `12`, platform-agnostic first, tools optional |
| Can I implement without asking what you meant? | Yes |

### Three weaknesses worth naming

**No screenshots.** The tracker instructions are text. A buyer who is not comfortable with
spreadsheets would be helped by images or a short walkthrough video. Not a blocker; a real
improvement.

**Pricing guidance is deliberately thin.** `08` gives the method and refuses to publish rate
ranges, because a buyer who prices from someone else's numbers will win jobs that lose money. An
operator new to commercial will find this less satisfying than a table of rates. That is the right
trade, and the document says so.

**Permit portals vary by county.** `03` says where to look; it cannot tell every buyer their
county's URL. A future addition could be a lookup list for the largest metros.

---

## 5. Voice and evidence

Chain applied: `cleaning-os-voice` → `copywriting-concrete` → `anti-ai-writing-slop` → evidence
validation.

| Check | Result |
|---|---|
| Banned words / AI filler | Clean after two edits |
| Fabricated proof — testimonials, case studies, results | **None.** No customer has used this yet, so there is nothing to cite and nothing is cited |
| Invented statistics | **None.** No reply rates, no ROI figures, no "X% more leads" |
| Guaranteed outcomes | **None.** `00`, `01` and `10` each state plainly that contracts are not guaranteed |
| Unsupported market claims | **None.** Where a market claim was tempting it became a recommendation or a question |
| Manufactured scarcity | **None** |
| Benchmarks | **None published.** `11` tells the buyer their own baseline is the only benchmark worth using, and says why |

**The evidence rule was applied to our own product, not only to outreach.** The page originally
listed four assets that did not exist. Rather than describe them, they were built.

---

## 6. Remaining before publish

| # | Item | Owner |
|---|---|---|
| 1 | Open both workbooks once, confirm no formula errors | You |
| 2 | Decide and state the refund policy | You |
| 3 | Package as a ZIP and upload | You |
| 4 | Test-purchase and confirm the download | You |
| 5 | Reconcile against the live Gumroad page — unreachable from this environment | You |
| 6 | Optional: cover image | You |

**Item 4 is the one that matters now.** Everything else is recoverable after launch; a broken
download is not.

---

## 7. Status

**Product complete and verified.** 14 of 14 assets exist, are customer-facing, are free of internal
material, have been reviewed, and both workbooks evaluate correctly.

Outstanding: the Gumroad purchase test, the refund policy, and reconciling against the live page
(unreachable from this environment).
