from pathlib import Path


OUTPUT = Path("portrait.svg")
ACCENT = "#6ee7f9"
ACCENT_2 = "#a78bfa"
BG = "#060914"


ASCII_ROWS = [
    "                 .::::::.                 ",
    "            .:-=+*######*+=-:.            ",
    "          .-+################+-.          ",
    "        .-*#######******#######*-.        ",
    "       :+#####*+=--::::--=+*#####+:       ",
    "      -#####*=:.          .:=*#####-      ",
    "     -#####+:     .----.     :+#####-     ",
    "    .#####+.    .+######+.    .+#####.    ",
    "    +####*.    :##########:    .*####+    ",
    "   .#####:     *###*++*###*     :#####.   ",
    "   -####*      ###-    -###      *####-   ",
    "   =####+      ##+  TK  +##      +####=   ",
    "   -####*      ###-    -###      *####-   ",
    "   .#####:     *###*++*###*     :#####.   ",
    "    +####*.    :##########:    .*####+    ",
    "    .#####+.    .+######+.    .+#####.    ",
    "     -#####+:     .----.     :+#####-     ",
    "      -#####*=:.          .:=*#####-      ",
    "       :+#####*+=--::::--=+*#####+:       ",
    "        .-*#######******#######*-.        ",
    "          .-+################+-.          ",
    "            .:-=+*######*+=-:.            ",
    "                 .::::::.                 ",
    "      DATA SCIENCE  |  ML  |  AI          ",
    "     PYTHON  PANDAS  SKLEARN  SQL         ",
]


def esc(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render():
    row_height = 15
    y_start = 56
    svg_rows = []
    for index, row in enumerate(ASCII_ROWS):
        y = y_start + index * row_height
        delay = 0.035 * index
        color = ACCENT if index < 23 else ACCENT_2
        svg_rows.append(
            f"""
  <text x="38" y="{y}" fill="{color}" font-size="13" opacity="0">
    {esc(row)}
    <animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.24s" fill="freeze"/>
  </text>"""
        )

    return f"""<svg width="380" height="500" viewBox="0 0 380 500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Animated ASCII portrait of Tushar Katpara">
  <defs>
    <linearGradient id="shell" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b1224"/>
      <stop offset="55%" stop-color="#090b18"/>
      <stop offset="100%" stop-color="#10172f"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="380" height="500" rx="22" fill="{BG}"/>
  <rect x="12" y="12" width="356" height="476" rx="18" fill="url(#shell)" stroke="#23304f"/>
  <circle cx="34" cy="32" r="5" fill="#ff5f57"/>
  <circle cx="52" cy="32" r="5" fill="#ffbd2e"/>
  <circle cx="70" cy="32" r="5" fill="#28c840"/>
  <text x="94" y="37" fill="#94a3b8" font-family="Consolas, monospace" font-size="13">portrait.ai</text>
  <g font-family="Consolas, 'Courier New', monospace" filter="url(#glow)">
    {''.join(svg_rows)}
  </g>
  <path d="M46 438 C118 410, 245 462, 334 426" fill="none" stroke="#6ee7f9" stroke-width="2" opacity="0.7">
    <animate attributeName="stroke-dasharray" values="0 500;260 500" dur="2.8s" fill="freeze"/>
  </path>
  <text x="42" y="470" fill="#c4b5fd" font-family="Consolas, monospace" font-size="16">TUSHAR KATPARA</text>
  <text x="42" y="490" fill="#7dd3fc" font-family="Consolas, monospace" font-size="12">aspiring machine learning engineer</text>
</svg>
"""


if __name__ == "__main__":
    OUTPUT.write_text(render(), encoding="utf-8")
