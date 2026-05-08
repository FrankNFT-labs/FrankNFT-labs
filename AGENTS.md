# PROJECT KNOWLEDGE BASE

**Generated:** 08-05-2026
**Commit:** 88a4532
**Branch:** main

## OVERVIEW

Personal portfolio profile repo. Contains ASCII banner generator script + GitHub Actions workflow for contribution graph snake animation.

## STRUCTURE

```
./
├── .github/workflows/snake.yml    # Daily cron: generates snake animation
├── assets/                      # Generated assets (franknft-ascii.svg)
├── scripts/generate_franknft_ascii_svg.py  # Banner generator
└── README.md                    # Profile readme
```

## WHERE TO LOOK

| Task              | Location                                      | Notes                      |
| ----------------- | --------------------------------------------- | -------------------------- |
| Edit ASCII banner | scripts/generate_franknft_ascii_svg.py        | Modify ASCII_ART list      |
| Regenerate banner | python scripts/generate_franknft_ascii_svg.py | Outputs to assets/         |
| Snake workflow    | .github/workflows/snake.yml                   | Runs daily at midnight UTC |

## CONVENTIONS

- Python: type hints, pathlib, f-strings
- SVG output: 940x210, terminal green #39FF14, dark bg #0D1117

## ANTI-PATTERNS (THIS PROJECT)

- No tests needed (trivial script)
- No CI beyond GitHub Actions

## COMMANDS

```bash
python scripts/generate_franknft_ascii_svg.py
```

## NOTES

- Single-purpose repo for profile assets
- Snake workflow commits to `output` branch
