# Automation Blueprint

Read this last, and build it later.

Automating a process you haven't run by hand produces a machine that does the wrong thing quickly.
Run twenty accounts manually first. You'll discover what actually takes time, and it usually isn't
what you expected.

When you're ready, this is the architecture.

---

## The pipeline

```
Account source → Enrichment → Verification → Trigger detection → Scoring
      → HUMAN REVIEW → Outreach → Replies → Records → Follow-up → Reporting
```

Nine of those ten steps can be automated. The one in capitals cannot, and the value of the whole
thing depends on that.

---

## What to automate, what to keep

| Step | Automate? | Why |
|---|---|---|
| Finding accounts | **Yes** | Mechanical. Search, pull, save. |
| Filtering out obvious misfits | **Yes** | Rules-based. No website, wrong area, too small. |
| Finding contact details | **Yes, partly** | Machines find addresses well. Deciding who signs is judgment. |
| Verifying an email is real | **Yes** | Purely mechanical, and it protects your domain. |
| Watching for triggers | **Yes** | The best use of automation here. Checking permits and listings weekly by hand is tedious and easy to skip. |
| Scoring | **Yes** | It's arithmetic. |
| **Deciding who to contact** | **No** | See below. |
| **Approving the send** | **No** | See below. |
| Sending an approved batch | Yes | Once a human approved that batch. |
| Sorting replies by type | **Yes, partly** | Sorting is fine. Answering is not. |
| **Replying to a person** | **No** | |
| Suppressing an opt-out | **Yes, always** | Should be instant and not depend on you noticing. |
| Logging activity | **Yes** | |
| Reminding you a follow-up is due | **Yes** | |
| Weekly reporting | **Yes** | |

### The three that must stay human

**Deciding who to contact.** A machine can score an account. It can't tell you that the building is
across the road from your worst customer, or that you met the owner and it went badly. Look at the
list before it becomes a send.

**Approving the send.** Every batch, every time. Not "approved for the week." The failure this
prevents is the expensive one: a merge field that didn't populate, a stale trigger, an account that
should have been suppressed. All three are obvious to a person glancing at the batch and invisible
to the system that produced it.

**Replying to a person.** Someone who replies to a cold email is the scarcest thing this system
produces. An automated answer squanders it, and they can tell.

### Never automate

- Sending without a human looking at that specific batch
- Any claim about a prospect the system inferred rather than observed
- Re-adding someone who opted out, for any reason, ever
- Automated calling, recorded messages, or synthetic voice — a separate area of law, and the wrong
  place to experiment
- Changing a price

---

## The gates

Build these as hard stops. A gate that warns and continues isn't a gate.

| Gate | Checks | Blocks when |
|---|---|---|
| **Suppression** | Every address and number against your opt-out list, **at the moment of sending** | Any match |
| **Verification** | Address confirmed deliverable, recently | Unverified, or checked over 90 days ago |
| **Score floor** | Total score | Below 8 |
| **Trigger validity** | Source and date present, still inside its window | Missing or expired |
| **Claim check** | The actual merged text, not the template | Any sentence asserts something not in the trigger record |
| **Compliance** | Business name, postal address, opt-out present | Any missing |
| **Volume** | Daily send count against what your domain can carry | Over the limit |
| **Human approval** | A person approved *this* batch | Always required |
| **Kill switch** | A single flag that stops all sending | When set |

Check suppression at send time, not when the list was built. A list built Monday and sent Thursday
can email someone who opted out on Tuesday.

The claim check is the one no tool does for you. Read the merged emails — five of them, not the
template — and confirm every statement about the recipient traces to something dated in your
records.

---

## Build it in this order

Stop at whatever level is genuinely helping. Most operators never need level 4.

**Level 0 — manual.** Spreadsheet and inbox. Do this for at least twenty accounts.

**Level 1 — save time on finding.** Automate account discovery and contact extraction into your
tracker. Everything downstream stays manual. Biggest time saving for the least risk, and it's where
most people should stop for the first month.

**Level 2 — add trigger watching.** Weekly automated checks against permit portals, listings and
job boards, writing into the Trigger Tracker. This is the highest-value automation in the system,
because trigger hunting is the step people skip when busy — and it's the step the whole method
depends on.

**Level 3 — sequencing with an approval gate.** Sending tool holds the sequences; you approve each
batch. Replies route back to your tracker.

**Level 4 — full orchestration.** One workflow end to end, with the human gate still in the middle.
Only worth it above a few hundred accounts a month.

---

## Tool options

None of these is required. The method works on a spreadsheet.

| Job | Options | Notes |
|---|---|---|
| Account discovery | Apify Google Maps scrapers, Outscraper, manual search | Apify charges per result, typically a few dollars per thousand. Pricing changes — check before committing. |
| Contact enrichment | Apollo, Hunter, Clearbit, or reading their website | For small local businesses, their own site is often better than a database. Databases tend to return generic inboxes. |
| Email verification | NeverBounce, ZeroBounce, Bouncer | Cheap. Do not skip it. |
| Trigger sources | County permit portals, Google Business listings, Indeed, state registries, CRE listing sites | Mostly free and public. |
| Orchestration | n8n, Make, Zapier, or a scheduled script | n8n self-hosts, which matters if you're storing contact data. |
| Storage | The provided tracker, Google Sheets, Airtable, or a CRM | Move off the spreadsheet when it starts hurting, not before. |
| Sending | Your normal email, or a sequencing tool | Sequencing tools help at volume and are unnecessary below about fifty a week. |

**One warning on sequencing tools:** merge-field syntax differs between them. Some use
`{{first_name}}`, others `{{firstName}}`. Get it wrong and your prospects receive the literal tag.
Send yourself a test before every new campaign.

---

## A worked example — the trigger watcher

The one automation worth building early, even if you build nothing else.

**Once a week, automatically:**
1. Read the list of accounts in your tracker that are still active.
2. For each, check: has the Google listing address changed? Is there a new permit at that address?
   Is there a new job posting mentioning facilities or operations?
3. Where something is found, write a row into the Trigger Tracker — the observation, the source,
   and the date.
4. Send yourself one summary email: *"4 new triggers this week."*

**Then you open the tracker and decide what to do.** The automation found the signals. It didn't
decide anything, didn't contact anyone, and didn't interpret what it saw.

That division is the whole design. Machines are good at watching things constantly and bad at
knowing what they mean. You are the other way round.

---

## Before you automate anything

- [ ] You've run at least twenty accounts by hand
- [ ] You know which step actually eats your time
- [ ] Your suppression list exists and is one list, not several
- [ ] You can stop all sending with one switch
- [ ] Every automated write is logged, so you can see what happened
- [ ] The human approval gate is built in from the start, not added later

The last one matters most. An approval gate added to a working automation is a gate people learn to
click through. Built in from the beginning, it's just how the system works.
