# Reference schema

What to capture from every clip worth studying. Summarizing is not reverse-engineering —
the point is the mechanism, in numbers where numbers exist.

Run first: `python3 scripts/analyze_video.py REF --end <content_end>`

## Record

**Identity** — platform · url or file · handle · topic · premise · duration_s
(content only, excluding any outro card)

**Opening** — opening_frame (what is literally visible at 0.0s) · opening_line ·
hook_type · first_change_s (when the first visual change lands) · what unanswered
question exists by 1s

**Structure** — story shape (setup/conflict/escalation/reveal/payoff) · beat timestamps ·
where curiosity is opened and where it is closed

**Craft, measured** — cuts (timestamps) · cut cadence · camera motion per second
(pan/tilt/zoom/roll from the analyzer) · pacing changes · pattern_interrupts (what and
when) · captions (style, timing, whether they carry meaning or decorate) · broll (does it
add information or fill space) · sound (music, SFX, silence, whether audio changes on
visual beats) · grade (black/white points, mean, saturation)

**Ending** — how it closes · loops (analyzer verdict) · CTA if any · what would make
someone rewatch or comment

**Judgement** — why_it_worked, in one sentence naming a *mechanism*, not a vibe.
"Opens pointed at the ground so the sky reveal at 1.5s is a payoff" — not "beautiful
cinematography".

## Save it

```
python3 scripts/library.py add reference --data '{"platform":"tiktok", ...}'
```

## Extract, don't copy

Turn each reference into a transferable principle and record it as a rule with evidence.
The goal is a growing set of mechanisms you can apply to unrelated subjects — not a folder
of clips to imitate.
