# Format: neon poetic micro-story

A second template alongside the atmospheric-shortform family. Where that one is
photoreal footage with a slow camera, this is **graphic, illustrated and
transformation-driven** — and it asks a generator for a far easier problem.

> **Evidence tier 3 — MEASURED.** Observed from one reference clip via
> `analyze_video.py`. Source was **576x576 square**, 24.87fps, 15.07s container with
> ~13.0s of content before the platform end card. Figures below are observations.
> Note the source aspect: these compositions were built for a square frame, so a 9:16
> version must be **recomposed, not cropped** — cropping a square destroys the lateral
> negative space the typography sits in.

## Measured values

| | Observed | Note |
|---|---|---|
| Mean exposure | **4.9%** | darkest clip measured in this project by a wide margin |
| Black point | 0.0% | true black background, not dark grey |
| White ceiling | 51.3% | glow never approaches clipping |
| Saturation | 0.43 | moderate — the colour is concentrated in small emissive areas |
| Highlight RGB | 131, 70, 158 | violet/magenta |
| First-second energy | **0.00** | nothing moves at 0s |
| Dead seconds | **7 of 13** | sec 0,2,3,4,7,9,11 |
| Strict cuts | 3, at 8.92 / 9.12 / 9.32 | all inside one 0.4s burst |
| Loose cut events | 18 | most are morphs, not cuts |
| Loop | does NOT loop | |

## The correction that matters

**This is not a continuously-moving edit.** Over half its seconds have no measurable
change at all. The real structure is **long held images punctuated by short bursts** —
motion concentrates at sec 8 (zoom +21.6%/s, roll -17.2 deg/s) and sec 10 (+30.7%/s),
with near-total stillness between.

Two consequences:

1. **The described "cut every 0.7-1.8s" is wrong.** Do not build to that rhythm. Build
   long holds, then one flurry of 3 cuts inside half a second.
2. **Most shots do not need video generation.** A held image with a glow pulse is a
   still plus a slow zoom. Generate video only for the burst and the morphs; that is a
   large cost saving over generating every shot as a clip.

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
| Cuts | long holds (1.4–1.8s) punctuated by ONE burst of ~3 cuts inside 0.5s. Never a steady rhythm — see Measured values. |
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
