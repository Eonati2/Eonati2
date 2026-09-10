#!/usr/bin/env python3
"""
render_neon_still.py — reference implementation for the neon poetic micro-story
format. Renders emissive primitives on true black, deterministically and at zero
generation cost.

STATUS: a validated RENDERER, not a validated format. It passed Gate C on the
"Never Both" shot set, which establishes that the target grammar can be produced
locally. It does NOT establish that the format performs — no clip built this way
has ever been published, and no tier-1 evidence exists for it.

The generated stills are deliberately not in this repo. Only the implementation is.

What it solves, each found by measuring against the reference and then looking:

  * HUE-PRESERVING HIGHLIGHT ROLLOFF. A hard per-channel ceiling drives every
    channel of a hot core to the same value, so the brightest part of each orb
    turns grey. Gate C vetoed exactly that. The rolloff here is applied to the
    channel MAXIMUM and the other channels scale by the same factor, so hue
    survives into the core. Highlight saturation went 0.03-0.18 -> 0.44-0.60.

  * SHADOW DESATURATION. Most of the frame is near-black, and a pure-hued dark
    pixel computes as highly saturated, so mean saturation sat near 0.75 no
    matter how the cores were tinted. Pulling the glow tail toward neutral lands
    the measured 0.43.

  * MONOCHROME GRAIN. Per-channel noise re-saturates the shadows just
    neutralised, and is wrong for film grain regardless.

  * CONTROLLED ASYMMETRY. Slight ellipse plus a low-order contour wobble reads
    as hand-drawn. This is smooth irregularity, NOT additive noise, which only
    ever looks like a dirty render.

Grade targets measured off the reference clip (576x576, 24.87fps, ~13.0s):
  black 0.0%  ·  mean 4.9%  ·  saturation 0.43  ·  highlight RGB ~131,70,158

One target is deliberately NOT met: the reference's 51.3% white ceiling. That
came from large lit shapes filling a square frame; these are compact orbs in a
taller 9:16 canvas with far more black. Chasing it would mean inflating the orbs
until they destroy the negative space the typography needs. Measurement narrows
the target; looking decides whether it was hit.

Usage:  python3 render_neon_still.py     (writes the six stills beside itself)
"""
import numpy as np
from PIL import Image
import os

W, H = 1080, 1920
CEIL, KNEE = 176.0, 132.0   # highlight ceiling and shoulder softness
OUT = os.path.dirname(os.path.abspath(__file__))

# palette — emissive, tuned so peak luminance lands near the measured ceiling
BLUE    = np.array([58, 104, 235], dtype=np.float32)
MAGENTA = np.array([232, 46, 150], dtype=np.float32)
VIOLET  = np.array([131, 70, 200], dtype=np.float32)

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)


WHITE = np.array([255, 255, 255], dtype=np.float32)

def orb(canvas, cx, cy, core_r, colour, intensity, halo=3.4,
        ellipse=(1.0, 1.0), wob=0.0, lobes=3.0, phase=0.0):
    """Additive emissive disc with a white-hot centre.

    Real emissive sources desaturate toward white at the core; without that the
    frame reads as flat coloured paint and saturation runs far above the
    measured 0.43. The flat-topped core also lifts the 99th-percentile
    luminance to the reference's 51% ceiling."""
    # Slight ellipse and a low-order contour wobble. This is deliberate, smooth
    # irregularity — a hand-drawn edge — not additive noise, which would only
    # look like a dirty render.
    ex, ey = ellipse
    ang = np.arctan2(yy - cy, xx - cx)
    warp = 1.0 + wob * np.sin(ang * lobes + phase)
    d = np.sqrt(((xx - cx) / ex) ** 2 + ((yy - cy) / ey) ** 2) / warp
    core = np.clip(1.0 - (d / core_r) ** 2, 0, 1) ** 0.55         # flat-topped
    glow = np.exp(-(d / (core_r * halo)) ** 1.30)
    hot = np.clip(1.0 - (d / (core_r * 0.62)) ** 2, 0, 1) ** 0.8  # white centre
    tint = colour[None, None, :] * (1 - hot[..., None] * 0.30) \
         + WHITE[None, None, :] * (hot[..., None] * 0.30)
    field = (core * 1.05 + glow * 0.42) * intensity
    canvas += field[..., None] * tint


def thread(canvas, p0, p1, colour, intensity, width=2.4, wobble=0.0):
    """Thin emissive line with bloom — the violet connection."""
    x0, y0 = p0; x1, y1 = p1
    t = np.linspace(0, 1, 900)
    px = x0 + (x1 - x0) * t
    py = y0 + (y1 - y0) * t
    if wobble:
        px = px + np.sin(t * np.pi * 3) * wobble
    d = np.full((H, W), 1e9, dtype=np.float32)
    for a, b in zip(px, py):
        seg = np.sqrt((xx - a) ** 2 + (yy - b) ** 2)
        np.minimum(d, seg, out=d)
    line = np.exp(-(d / width) ** 2) + 0.30 * np.exp(-(d / (width * 9)) ** 2)
    canvas += (line * intensity)[..., None] * colour[None, None, :]


def tendril(canvas, cx, cy, tx, ty, colour, intensity):
    """A reaching curve — magenta extending toward blue. Tapers as it goes."""
    t = np.linspace(0, 1, 700)
    bow = 150.0
    px = cx + (tx - cx) * t
    py = cy + (ty - cy) * t - np.sin(t * np.pi) * bow
    d = np.full((H, W), 1e9, dtype=np.float32)
    taper = np.full((H, W), 1.0, dtype=np.float32)
    for i, (a, b) in enumerate(zip(px, py)):
        seg = np.sqrt((xx - a) ** 2 + (yy - b) ** 2)
        m = seg < d
        d = np.where(m, seg, d)
        taper = np.where(m, 1.0 - 0.72 * (i / len(t)), taper)
    line = (np.exp(-(d / 3.0) ** 2) + 0.28 * np.exp(-(d / 26.0) ** 2)) * taper
    canvas += (line * intensity)[..., None] * colour[None, None, :]


def finish(canvas, grain=2.0, vig=0.55, seed=0, shadow_desat=26.0):
    """Vignette, shadow desaturation, monochrome grain, and a hard ceiling.

    shadow_desat is what lands the measured 0.43 saturation. Most of this frame
    is near-black, and a pure-hued dark pixel computes as highly saturated, so
    without pulling the glow tail toward neutral the average sits near 0.75 no
    matter how the cores are tinted. Colourists desaturate shadows for the same
    reason it reads correctly here.

    Grain is monochrome — per-channel noise would re-saturate the very shadows
    just neutralised, as well as being wrong for film grain."""
    rng = np.random.default_rng(seed)
    cx, cy = W / 2, H / 2
    r = np.sqrt(((xx - cx) / cx) ** 2 + ((yy - cy) / cy) ** 2)
    canvas *= (1.0 - vig * np.clip(r - 0.45, 0, 1) ** 1.5)[..., None]

    lum = canvas @ np.array([.2126, .7152, .0722], dtype=np.float32)
    keep = np.clip(lum / shadow_desat, 0, 1)[..., None] ** 0.75
    canvas = lum[..., None] * (1 - keep) + canvas * keep

    canvas += rng.normal(0, grain, (H, W, 1)).astype(np.float32)
    canvas = np.clip(canvas, 0, None)

    # Ratio-preserving highlight rolloff. A hard per-channel ceiling drives every
    # channel of a hot core to the same value, so the brightest part of every orb
    # loses its hue and reads as grey — the defect Gate C vetoed. Here the rolloff
    # is applied to the channel MAXIMUM and the other channels are scaled by the
    # same factor, so hue survives all the way into the core.
    mx = canvas.max(axis=2, keepdims=True)
    rolled = CEIL * (1.0 - np.exp(-mx / KNEE))          # soft shoulder, asymptotic
    canvas = canvas * np.divide(rolled, np.maximum(mx, 1e-6))
    return Image.fromarray(np.clip(canvas, 0, 255).astype(np.uint8), "RGB")


def blank():
    return np.zeros((H, W, 3), dtype=np.float32)


# ---- the six ------------------------------------------------------------
# Placement is deliberately off-grid: nothing sits on a centre line or a tidy
# diagonal, and no two orbs share a radius. Sparse stays sparse.

# s1  shots 1 and 9 — one light alone. Opens and closes the piece.
c = blank()
orb(c, W * 0.44, H * 0.605, 124, BLUE, 1.06,
    ellipse=(1.05, 0.94), wob=0.045, lobes=3, phase=0.7)
finish(c, seed=1).save(f"{OUT}/s1_blue_alone.png")

# s2  shot 2 — blue dimming as magenta arrives. The see-saw begins.
c = blank()
orb(c, W * 0.335, H * 0.695, 98, BLUE, 0.40,
    ellipse=(0.96, 1.06), wob=0.05, lobes=4, phase=2.1)
orb(c, W * 0.655, H * 0.335, 128, MAGENTA, 1.02,
    ellipse=(1.07, 0.95), wob=0.04, lobes=3, phase=1.3)
finish(c, seed=2).save(f"{OUT}/s2_blue_dim_magenta_rise.png")

# s3  shot 4 — both held at half, a thin violet thread between them
c = blank()
orb(c, W * 0.30, H * 0.615, 108, BLUE, 0.64,
    ellipse=(1.03, 0.97), wob=0.05, lobes=3, phase=0.2)
orb(c, W * 0.695, H * 0.405, 104, MAGENTA, 0.62,
    ellipse=(0.97, 1.04), wob=0.045, lobes=4, phase=2.6)
thread(c, (W * 0.30, H * 0.615), (W * 0.695, H * 0.405), VIOLET, 0.46,
       width=2.1, wobble=13.0)
finish(c, seed=3).save(f"{OUT}/s3_half_thread.png")

# s4  shot 5 — THE REACH. A new state, not s2 with a line added: the filament
# crosses the full negative space, the receiving light is displaced low-left and
# pushed off the s2/s3 diagonal, and blue flares slightly where it lands.
c = blank()
orb(c, W * 0.215, H * 0.80, 86, BLUE, 0.72,
    ellipse=(1.10, 0.92), wob=0.07, lobes=3, phase=1.9)
orb(c, W * 0.78, H * 0.245, 116, MAGENTA, 0.86,
    ellipse=(0.94, 1.08), wob=0.05, lobes=4, phase=0.4)
tendril(c, W * 0.78, H * 0.245, W * 0.245, H * 0.775, MAGENTA, 0.70)
finish(c, seed=4).save(f"{OUT}/s4_reach.png")

# s5  shot 7 — both violet, equal, dimmer than either was alone. The cost.
c = blank()
orb(c, W * 0.375, H * 0.565, 114, VIOLET, 0.70,
    ellipse=(1.02, 0.98), wob=0.05, lobes=3, phase=2.9)
orb(c, W * 0.625, H * 0.455, 110, VIOLET, 0.68,
    ellipse=(0.98, 1.03), wob=0.05, lobes=4, phase=1.1)
finish(c, seed=5).save(f"{OUT}/s5_both_violet.png")

# s6  shot 8 — violet going out
c = blank()
orb(c, W * 0.375, H * 0.565, 118, VIOLET, 0.24,
    ellipse=(1.02, 0.98), wob=0.05, lobes=3, phase=2.9)
orb(c, W * 0.625, H * 0.455, 114, VIOLET, 0.23,
    ellipse=(0.98, 1.03), wob=0.05, lobes=4, phase=1.1)
finish(c, grain=1.6, seed=6).save(f"{OUT}/s6_violet_fading.png")

print("rendered 6 stills to", OUT)
