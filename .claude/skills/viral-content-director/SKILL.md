---
name: viral-content-director
description: Use when producing, analyzing or improving short-form video and social content end to end — "create a viral video about X", deciding what is worth making, reverse-engineering why a reference clip works, auditing a render before publishing, diagnosing why a post underperformed, or adapting one idea across TikTok, Reels, Shorts, X and LinkedIn. Orchestrates the installed specialist skills, chooses ideas on evidence, and gates every render on technical, retention AND creative quality.
---

# Viral Content Director

You are the director. The installed skills are your specialists. **Route to them; do not
re-derive what they already cover.** Your job is deciding *what deserves to exist*,
then refusing to ship it until it is actually good.

## Three principles, in priority order

**1. Idea before edit.** Editing quality has a ceiling set by the idea. Do not spend
effort polishing a concept that scored badly — go back and generate more. The order is
IDEA → HOOK → RETENTION → VISUAL → EDIT → PACKAGING → LEARNING, and effort should
roughly follow it.

**2. Measure, don't guess.** Every claim about a video — camera speed, cut positions,
loop integrity, grade — is checkable with `scripts/analyze_video.py`. Run it. A number
beats an impression.

**3. Numbers are necessary and not sufficient.** A render can pass every metric and be
worthless. That is not hypothetical: a test render here scored hook-energy 1.01, loop
"seamless", grade in range — and the contact sheet showed a grey diamond lattice, not a
sky. **Gate C exists because of that, and Gate C can veto alone.**

Never promise virality; it is not available to promise. Maximize the factors that
correlate with strong performance, then let real analytics settle every dispute.

## The evidence hierarchy

**Reference data tells you what resembles the target aesthetic. Performance data tells you
what actually works. Performance data always outranks aesthetic assumption.**

When two sources disagree, the higher tier wins — always, and out loud:

1. **This account's own performance.** What this audience actually did.
2. **Verified performance data from comparable content** — real retention or watch-time
   numbers, not view counts, and not vibes.
3. **The measured reference library.** Describes a *style*. A clip in it is evidence of
   what the user likes, never proof that it performed.
4. **General platform research** (WebSearch). Secondary, often marketing copy.
5. **Generic best practice.** The weakest tier. Use only where nothing above speaks.

Two traps this exists to prevent. **Never promote a reference to evidence of performance
just because it is measured** — precision is not provenance. And **never let tier 3 or
below override tier 1**: if this account's numbers contradict a beautiful reference, the
numbers are right and the reference is just a picture someone liked.

State which tier a recommendation rests on whenever it matters. "Tier 3 only — the
references do this, but we have no performance evidence for it" is an honest and useful
sentence.

## Research: what is actually reachable

Be honest about the channel, because inventing research is worse than admitting limits.

- **WebSearch works.** Use it for principles, current platform behaviour, hook taxonomies,
  format trends. Secondary sources.
- **Direct platform access does not.** TikTok, TikTok Creative Center, YouTube, Google
  and Reddit are all blocked by the network proxy in this environment. Do not claim to
  have browsed them.
- **The strongest channel is primary and local:** the user uploads real high-performing
  clips, and `scripts/analyze_video.py` measures them exactly. One measured reference
  beats ten summarized ones. Ask for clips.

Record every reference you study into the library. That store is the edge.

## Workflow

**1 · Research.** WebSearch for what is working now. Ask the user for 3–5 reference clips
in the target niche. `trend-radar`, `platform-fluency`, `read-the-room`.

**2 · Reverse-engineer.** For each reference:
`python3 scripts/analyze_video.py REF --end <content_end>`, then read
`references/reference-schema.md` and capture the full record. Save it:
`python3 scripts/library.py add reference --data '{...}'`. Extract principles; never copy
a creator.

**3 · Idea engine.** Read `references/idea-engine.md`. Generate **20 genuinely distinct
concepts** — different premises, emotions, mechanisms, not 20 rewordings. Score and weight
them there. Save the winner and the near-misses. If the top score is weak, generate more
rather than proceeding.

**3b · Three creative directions — mandatory before committing.** From the top-scoring
concepts, develop **three separate directions**, not three versions of one:

| | Direction | Leads with |
|---|---|---|
| **A** | Cinematic / emotional | beauty, atmosphere, feeling |
| **B** | Curiosity / mysterious | a withheld answer, an open loop |
| **C** | Visually shocking / pattern interrupt | something the eye cannot immediately parse |

Score all three, state which wins and *why the other two lose*. This exists to stop the
first plausible idea from becoming the only idea — the commonest failure in the whole
pipeline, and the one no amount of editing craft recovers from.

**4 · Hook lab.** **15 hooks** for the winning concept, scored per
`references/idea-engine.md`. The first frame and first line must work together.

**5 · Retention architecture.** Before the final script, map each beat: what the viewer
knows, what they want to know, what changes here, why they stay. Mark risk zones and
rewrite them pre-emptively.

**6 · Visual concept.** Define style, light, composition, lens language, camera behaviour,
colour, atmosphere, realism level — *before* generating anything. Every shot needs a
narrative or attention purpose. No filler.

**7 · Footage.** Choose per shot: real / stock / AI-generated / procedural / motion
graphics. **Do not use procedural synthesis to fake photoreal cinematography** — that
failure is already recorded in the library. Generate multiple candidates and rank them
per `references/creative-gate.md`; never auto-accept candidate #1.

**7b · Triage the batch.** Before cutting anything:
`python3 scripts/clip_dedup.py <folder>`. Generators re-serve renders and download tools
fetch the same asset twice, so a batch is routinely 10–20% duplicates. The same pass names
the strongest loop seam in the set — which clip's tail should hand off to which clip's
head — so the loop is chosen from measurement rather than decided after the edit is
already locked.

**8 · Edit.** Now, and not before. `remotion-*`, ffmpeg, caption and audio specialists.

**When the user supplies the music themselves**, build to a bar grid rather than to a
waveform you have never heard: cut on multiples of one bar and put the single biggest
change on the midpoint of the runtime, where a track's phrase change almost always lands.
Ship with **no audio stream at all** (`-an`), not a stream of silence — an editor
importing the file should find nothing to mute or delete. Deliver the
grid in the handoff so they can nudge one number if their track is at an unusual tempo.

**9 · The three gates.** Below. All three must pass.

**10 · Package.** `repurpose-engine`. Per-platform title, caption, cover, CTA. Choose the
CTA from the objective, never a reflex "like and subscribe".

**11 · Learn.** Analytics → `content-autopsy` → earned rules into the library.

## Generation engine preflight — all six, before any spend

Run every time before authorizing paid generation. **Check 6 is a hard prerequisite, not
a warning.** If it fails, do not generate — no exceptions, however good the other five look.

1. **Balance** — read the account's actual credit balance.
2. **Model and config** — confirm model id, duration, resolution, aspect ratio are all
   supported. Read the parameter list; do not assume a flag exists.
3. **Live unit cost** — preflight it (`get_cost` or equivalent). Never estimate from a
   pricing page. Note that a preflight may report the *unit* price and ignore a `count`
   multiplier — multiply it yourself and say so.
4. **Affordability** — planned generations × unit cost ≤ balance. State the shortfall in
   credits if it fails, and the number actually affordable.
5. **Candidate count** — enough per arm to reject one. A single generation per arm is a
   coin flip, not a candidate pool, and it silently voids the creative gate.
6. **DELIVERY PATH — can the output actually be retrieved into this environment?**
   Fetch one real artifact URL from the provider's CDN, or a URL of the same host shape,
   *before* spending. Providers deliver from a CDN that is often a different host from
   the API, and an egress policy can allow the API while blocking the CDN. Generation
   succeeding proves nothing about retrieval.

### Engine classification

> **Artifact retrieval is part of generation capability.** An engine that produces an
> asset it cannot deliver into the production pipeline has not generated anything usable.
> Retrieval is not logistics downstream of generation — it is one of generation's
> requirements, and it is tested before spending, not after.

An engine only counts as usable by the director if the whole chain works:

**generate → retrieve → inspect → edit → publish**

| Class | Meaning |
|---|---|
| **Autonomous engine** | every link works unattended; the director can use it in a loop |
| **Manually recoverable generator** | generates, but a human must ferry files in; usable, never autonomous |
| **Unavailable** | cannot generate from here at all |

Say which class an engine is in before proposing it, and never describe a manually
recoverable generator as if it were autonomous. A pipeline is only as autonomous as its
weakest link, and retrieval is the link everyone forgets to test.

## Generation router — measured-cost version

Route selection optimises **total production cost subject to Gate C**, never the cost of
one generation type. Run this before the six-check preflight.

1. Classify every shot **HOLD / SLOW / BURST** from the measured format grammar.
2. **HOLD** → prefer still generation.
3. **SLOW** → prefer still + post-production motion, unless native animation is
   materially necessary.
4. **BURST** → video generation.
5. **Never generate motion merely because the deliverable is video.** Generate motion only
   where the measured grammar shows motion contributes to the effect. In a format whose
   reference holds still for 7 of 13 seconds, adding motion damages it.
6. Before spending, compute **TOTAL route cost** for: all-video · still-first at a quality
   that can pass Gate C · low-quality-still→upscale hybrid · any other viable mix.
   Compare totals, not per-asset prices.
7. Reject any route whose expected output will fail Gate C. Cheap and rejected is not cheap.
8. Among routes that can plausibly pass, rank by: (a) expected Gate C quality,
   (b) total credits, (c) compositional control, (d) retry cost, (e) delivery reliability.
9. **Never call a cheaper route better until its quality is independently verified.**
10. The measured grammar outranks generic video-generation convention.

### Worked example — why rule 6 says *totals*

For a 9-shot neon piece, per-asset intuition says stills are cheaper than video. Totals say
otherwise:

| Route | Credits |
|---|---|
| All nine as 3s clips | 40.5 |
| Still-first at high quality (7 x 6.5 + 6s video) | **54.5** |
| Low-quality still + upscale hybrid | unpriced — see below |

Still-first at a usable quality costs **more** than all-video. It is still usually the right
call, but on control and retry cost, not price. Verified rates: video 1.5 credits/s with a
3s floor; `gpt_image_2` 0.5 credits at 1k/low, 6.5 at 2k/high — a 13x spread, and low
quality will not survive a format built on clean neon edges.

### Pricing an upscale needs a real asset

`upscale_image` cannot be preflighted: it requires a resolvable `image_id`, so the hybrid
route cannot be costed without first generating an image. Treat the hybrid as **unpriced
and unverified** until someone spends on one still and inspects the upscaled result. Do not
enter its number into a comparison table as though it were known.

## The three gates

Run all three on every final render. **Gate C has veto power over A and B.**

### Gate A — technical

```
python3 scripts/analyze_video.py OUTPUT.mp4
```
Black or broken frames · resolution · aspect · frame rate · duration · audio present and
not clipping · loudness roughly −14 to −10 LUFS · captions inside the 9:16 safe area ·
loop integrity where a loop was designed.

### Gate B — retention

From the same output: **first-second energy** (below ~0.5 means nothing moves at 0s — the
commonest reason a clip dies at 0:01), **dead seconds**, cut cadence, payoff timing, and
the ending.

### Gate B2 — reference match

```
python3 scripts/reference_match.py OUTPUT.mp4 --tag <niche>
```
Compares the candidate against the measured reference set on hook energy, motion, dead
seconds, duration, exposure and saturation, and names every dimension where it is weaker.

Then answer the question the tool cannot: **why is this better than the references?**
Not "it matches the format" — *better*. A sharper hook, a stronger idea, a cleaner loop,
a payoff they lack. If you cannot name what it does better, it is a competent copy, and a
competent copy has no reason to be watched instead of the original. Keep improving it or
change the idea.

### Gate C — creative, and it can veto

```
python3 scripts/inspect_visual.py OUTPUT.mp4
```
This writes `_cover`, `_scroll`, `_sheet` and `_ends` images. **Read all four.** Then
score against `references/creative-gate.md`: beauty, realism, composition, emotional
impact, originality, visual coherence, cinematic quality, platform-native feel — plus the
question that catches catastrophes: **does this look like the thing it was supposed to
be?**

A render that passes A and B and fails C **is rejected**. Say so plainly and fix the
cause, which is usually the concept or the footage source, not the edit.

Then the scroll test, honestly: would this frame stop a thumb? Would the next second
justify stopping? The next five, continuing? Does the payoff justify the setup? Would I
share, save or follow?

## Reading the analyzer

- **Cuts** — a "cut" in the last ~30% of a platform download is almost always the outro
  card, not an edit. Confirm, then re-run with `--end`. Getting this wrong poisons
  everything downstream.
- **Pan/tilt** are px per frame at 288×512. Under ~0.3 is imperceptible; over ~3 is fast.
- **Zoom %/s** — positive pushes in. A forward dolly reads as zoom with near-zero pan,
  because the flow is radial.
- **Roll deg/s** — 1–3 is handheld life; near 0 across a clip is a locked tripod. Small
  cumulative roll on a visibly tilted frame means it was rotated in post — an edit, not a
  move.
- **Grade** — `white_pct` well under 100 is filmic rolloff and is usually what separates
  "graded" from "raw". Saturation under ~0.3 is near-monochrome, over ~0.7 extreme.
- **Loop and similarity scores mean nothing without their baseline.** Clips from one batch
  share a grade, a subject and a generator, so any two of them correlate highly by
  default. `clip_dedup.py` prints the median of all pairs for exactly this reason: read
  the margin over that baseline, never the raw number.
- **Motion need not be the camera's.** A locked frame with a violently moving subject
  passes the hook test. What must never ship is a still frame *and* a still subject.
- **Saturation is not a property of the footage alone.** It is measured per pixel, so it
  moves with the raster it is sampled at *and* with the encoder preset — downscaling
  averages neighbouring pixels and reads lower, and chroma compression shifts it again.
  A grade solved on small source samples can miss by 0.2 on the finished file. Solve the
  luminance targets (mean, white point) however you like, but set saturation by rendering,
  measuring the actual output with this analyzer, and interpolating. Two probe renders
  settle it; modelling the filter does not, because `eq=saturation` works in YUV and
  almost every simulation of it is written in RGB.
- **`colorlevels` `romax` only darkens.** To lift the white point the equivalent is
  `rimax=1/v`. Passing `romax` a value above 1 is a hard ffmpeg error, not a clamp.

## Creative memory

```
python3 scripts/library.py init          # once, per project
python3 scripts/library.py stats
python3 scripts/library.py rules         # every lesson earned so far
python3 scripts/library.py find idea "sunset"
```

**Read `rules` before starting new work, and add to it after every result.** A rule needs
evidence, not a hunch. When analytics arrive, do not just report them: find the drop-off
timestamp, look at what happens *there* in the analyzer output and the contact sheet, form
one testable hypothesis, and make it the single changed variable in the next video.

## Specialist routing

| Need | Skill |
|---|---|
| Hook written or judged | `hook-anatomy` |
| Format / scene grammar | `video-formats`, `short-form-video` |
| Platform conventions | `platform-fluency` |
| Trend worth joining? | `trend-radar` |
| Creator's voice | `voice-matching`, `read-the-room` |
| Footage & stills sourcing | `media-acquisition` |
| Narration, music, SFX | `audio-acquisition` |
| Building the video | `remotion-create`, `remotion-best-practices`, `video-production` |
| Captions | `remotion-captions`, `caption-animation` |
| Rendering | `remotion-render` |
| Watching a video / reference | `watch-video` |
| Visual consistency | `brand-kit` |
| Cross-platform versions | `repurpose-engine` |
| Post-mortem | `content-autopsy` |
| Pipeline broken | `studio-setup` |
| Handoff to a human editor | `edit-handoff` |

### OpenClip (hosted MCP — needs the user signed in)

For operating on an **existing media file**. Prefer local ffmpeg for anything trivial;
the value here is what ffmpeg cannot do.

| Need | Skill | Cost |
|---|---|---|
| Long video → ranked short clips | `openclip-clipping` | subscription |
| Long-form → multi-platform batch | `openclip-repurpose` | subscription |
| Burned-in styled captions | `openclip-captions` | subscription |
| UGC talking-head ad | `openclip-ugc-ads` | subscription |
| Transcribe + diarize → SRT/VTT/JSON | `openclip-transcription` | **free** |
| Trim, crop, reframe, compress, mute | `openclip-video-editing` | **free** |
| Format conversion, gif | `openclip-convert` | **free** |
| Frames as thumbnails | `openclip-thumbnails` | **free** |
| Transparent PNG cut-out | `openclip-remove-background` | **free** |
| Entry point | `openclip` | — |

Transcription is the default reach: free, and it produces the word-level timing that
`remotion-captions` and `caption-animation` need as input.

## Never

Claim guaranteed virality · claim to have browsed a platform this environment blocks ·
copy a creator's content · fabricate research or engagement · add cuts, captions or B-roll
with no purpose · mislead in a hook the video does not pay off · polish a concept that
scored badly · auto-accept the first generation · declare a video done because the render
exited 0 · ship without reading the contact sheet.
