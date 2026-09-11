# Customer Product

What a buyer receives. Thirteen files: eleven PDF guides and two Excel workbooks.

`src/` holds the markdown sources for the PDFs. Both workbooks are built from scripts, so every
file here is reproducible.

| File | Source |
|---|---|
| `00-START-HERE.pdf` … `12-AUTOMATION-BLUEPRINT.pdf` | `src/*.md` |
| `02-ACCOUNT-TRIGGER-TRACKER.xlsx` | build script |
| `11-METRICS-SCOREBOARD.xlsx` | build script |

## Rules for anything added here

**Nothing internal ships.** No Instance A/B language, no our-pricing, no pilot strategy, no repo
paths, no internal filenames. The shared internal files contain both our targeting logic and the
customer's — rewrite from scratch rather than extracting, which is how these were produced.

**Nothing unevidenced ships.** No testimonials, case studies, results, reply rates, ROI figures or
published benchmarks. There are no customers yet, so there is nothing to cite.

**Voice:** an experienced operator talking to a busy owner. Run new material through
`cleaning-os-voice` → `anti-ai-writing-slop` before it goes in.

Status and outstanding checks: `../gumroad/FINAL-ASSET-AUDIT.md`.
