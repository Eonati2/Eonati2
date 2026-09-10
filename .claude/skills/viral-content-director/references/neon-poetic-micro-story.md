# Format: neon poetic micro-story

A second template alongside the atmospheric-shortform family. Where that one is
photoreal footage with a slow camera, this is **graphic, illustrated and
transformation-driven** — and it asks a generator for a far easier problem.

> **Evidence tier 4 — described, not measured.** This spec was written from a
> description of a reference clip, not from `analyze_video.py` output. Every number
> below is a *design target*, not an observed value. Do not treat it as a measured
> reference, do not add it to the library with a `measured` block, and do not let
> `reference_match.py` compare against it until a real example has been analyzed.
> If the user uploads one, measure it and replace these targets with observations.

## The system

Black canvas. One isolated symbolic object per shot, drawn as emissive neon line art.
Tiny editorial typography sitting *inside* the composition. Cuts driven by metaphor
change rather than by elapsed time. A visual motif returns at the end.

That system is the transferable thing. The specific symbols, wording and shot order of
any reference clip are **not** to be reproduced — invent new ones every time.

## Visual grammar

| | |
|---|---|
| Canvas | 9:16, near-black background, heavy negative space |
| Palette | black · deep violet · electric blue · hot magenta · soft white. Nothing else. |
| Colour as meaning | blue = distance, cool, thinking · magenta = warmth, intensity · violet = the turn between them · white = the voice |
| Subject | ONE isolated object per shot. No environment, no ground plane, no horizon. |
| Rendering | illustrated, hand-drawn, slightly imperfect. Emissive, lit from within, controlled bloom. Never photographic. |
| Motion | appear → morph → pulse → transform → replace. **Not** dolly, pan, crane or track. |
| Cuts | every 0.7–1.8s, on a metaphor change, never on a timer |
| Ending | return to the opening motif — a callback, not a resolution |

## Typography

The single strongest fingerprint, and the easiest thing to get wrong.

- Thin editorial serif. Small relative to the canvas.
- Positioned in the composition, near centre — **never** parked at the bottom like a
  subtitle.
- Two-level hierarchy: a primary line, then a smaller, lower-contrast second line.
- The text sets the pacing. A line holds until it has been read once, unhurried.

**Explicitly not:** bold TikTok captions, word-by-word karaoke, giant hook text, heavy
sans-serif. Those belong to `caption-animation` and would destroy this format.

## Writing

A four-beat emotional shape carries it: **a question · an answer · a hesitation · the
thing underneath.** Short lines, plain words, no rhyme scheme, no ornament.

Write something original every time. Do not adapt, paraphrase or word-swap lines from an
existing clip — that produces a derivative of someone's work and it reads as one. Take the
*shape*, then write your own.

## Generation strategy — micro-shots

Do not ask for the whole story in one generation. Ask for one object doing one thing:

> isolated neon line-art hand, black void, slowly rotating, soft blue inner glow

not

> cinematic flight through a night landscape as a figure reaches toward the moon

The first is a problem a generator can solve. The second is three problems and it will
fail at all of them. **This is why the format suits generation better than photoreal
camera work** — simple graphic primitives on a black field are close to the easiest thing
a video model can do, and black backgrounds hide the artifacts that usually fail Gate C.

Hold one shared style string across every shot so nine generations look like one artist:

> black infinite background, minimal neon line-art illustration, emissive blue and magenta
> strokes, soft bloom, hand-drawn surreal aesthetic, sparse composition, strong negative
> space, no realistic environment, no photographic texture

Then vary only the subject line.

## The cost arithmetic — read before proposing this

Generation is billed by **duration**, not by clip. On Kling 3.0 Turbo 720p it is
**1.5 credits/second** (verified: 3s = 4.5, 9s = 13.5).

| Approach | Generated footage | Credits |
|---|---|---|
| One 9s take | 9s | 13.5 |
| 9 micro-shots at the 3s minimum | 27s | **40.5** |

Micro-shots cost **3× more** for the same finished runtime, because the minimum
generation is 3s and most of each shot is trimmed away. That is the price of edit control
— it is often worth paying, but say so out loud rather than presenting micro-shots as a
saving.

Cheaper routes worth pricing first: fewer, longer shots reused with different text; or
generating stills and animating them, since much of this format is a static object with a
glow pulse.

## Audio

Sparse, dreamy, restrained. Subtle whoosh or pulse on each transformation so the cuts feel
intentional. **Never transcribe or reconstruct speech from a reference clip you cannot
actually hear** — if there is no transcription model available, say so and leave it blank.
