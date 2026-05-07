#!/usr/bin/env python3
from __future__ import annotations

from html import escape
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = REPO_ROOT / "assets" / "franknft-ascii.svg"
TERMINAL_GREEN = "#39FF14"
TERMINAL_BACKGROUND = "#0D1117"

ASCII_ART = [
    " ________  _______    ______   __    __  __    __  __    __  "
    "________  ________",
    "|        \\|       \\  /      \\ |  \\  |  \\|  \\  /  \\|  \\  "
    "|  \\|        \\|        \\",
    "| $$$$$$$$| $$$$$$$\\|  $$$$$$\\| $$\\ | $$| $$ /  $$| $$\\ "
    "| $$| $$$$$$$$ \\$$$$$$$$",
    "| $$__    | $$__| $$| $$__| $$| $$$\\| $$| $$/  $$ | $$$\\| "
    "$$| $$__       | $$",
    "| $$  \\   | $$    $$| $$    $$| $$$$\\ $$| $$  $$  | $$$$\\ "
    "$$| $$  \\      | $$",
    "| $$$$$   | $$$$$$$\\| $$$$$$$$| $$\\$$ $$| $$$$$\\  | $$\\$$ "
    "$$| $$$$$      | $$",
    "| $$      | $$  | $$| $$  | $$| $$ \\$$$$| $$ \\$$\\ | $$ "
    "\\$$$$| $$         | $$",
    "| $$      | $$  | $$| $$  | $$| $$  \\$$$| $$  \\$$\\| $$  "
    "\\$$$| $$         | $$",
    " \\$$       \\$$   \\$$ \\$$   \\$$ \\$$   \\$$ \\$$   \\$$ "
    "\\$$   \\$$ \\$$          \\$$",
]


def _build_svg() -> str:
    tspan_lines = [
        f'    <tspan x="36" dy="{0 if index == 0 else 18}">'
        f"{escape(line, quote=False)}</tspan>"
        for index, line in enumerate(ASCII_ART)
    ]

    return "\n".join(
        [
            '<svg width="940" height="210" viewBox="0 0 940 210" role="img" '
            'aria-labelledby="title desc" xmlns="http://www.w3.org/2000/svg">',
            '  <title id="title">FrankNFT terminal ASCII banner</title>',
            "  <desc id=\"desc\">"
            "Green old-terminal ASCII art spelling FrankNFT."
            "</desc>",
            "  <defs>",
            '    <filter id="terminal-glow" x="-20%" y="-20%" width="140%" '
            'height="140%">',
            '      <feGaussianBlur stdDeviation="1.4" result="blur"/>',
            "      <feMerge>",
            '        <feMergeNode in="blur"/>',
            '        <feMergeNode in="SourceGraphic"/>',
            "      </feMerge>",
            "    </filter>",
            "  </defs>",
            f'  <rect width="940" height="210" rx="16" fill="{TERMINAL_BACKGROUND}"/>',
            f'  <text x="36" y="38" fill="{TERMINAL_GREEN}" '
            'filter="url(#terminal-glow)" font-size="15" '
            'font-family="SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace" '
            'xml:space="preserve">',
            *tspan_lines,
            "  </text>",
            "</svg>",
            "",
        ]
    )


def _main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(_build_svg(), encoding="utf-8")


if __name__ == "__main__":
    _main()
