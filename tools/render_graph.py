import json
from datetime import date, timedelta
from pathlib import Path


INPUT = Path("assets/contributions.json")
OUTPUT = Path("graph.svg")
LEVELS = ["#0b1020", "#12345a", "#145da0", "#38bdf8", "#c4b5fd"]


def fallback_payload():
    today = date.today()
    days = []
    for i in range(371):
        current = today - timedelta(days=370 - i)
        count = 0
        if current.weekday() in (0, 2, 4):
            count = (i * 5) % 6
        days.append({"date": current.isoformat(), "count": count})
    return {
        "username": "TUshARKatpara",
        "total": sum(day["count"] for day in days),
        "current_streak": 0,
        "longest_streak": 0,
        "days": days,
    }


def load_payload():
    if INPUT.exists():
        return json.loads(INPUT.read_text(encoding="utf-8"))
    return fallback_payload()


def level(count, max_count):
    if count <= 0:
        return 0
    if max_count <= 1:
        return 1
    ratio = count / max_count
    if ratio < 0.25:
        return 1
    if ratio < 0.5:
        return 2
    if ratio < 0.75:
        return 3
    return 4


def render_cells(days):
    max_count = max([day["count"] for day in days] or [1])
    cells = []
    size = 10
    gap = 4
    x0 = 44
    y0 = 82

    for index, day in enumerate(days[-371:]):
        week = index // 7
        weekday = index % 7
        x = x0 + week * (size + gap)
        y = y0 + weekday * (size + gap)
        color = LEVELS[level(day["count"], max_count)]
        delay = 0.018 * week
        cells.append(
            f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="3" fill="{color}" opacity="0">'
            f'<title>{day["date"]}: {day["count"]} contributions</title>'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.28s" fill="freeze"/>'
            "</rect>"
        )
    return "\n    ".join(cells)


def render_legend():
    parts = ['<text x="672" y="204" class="muted">less</text>']
    for i, color in enumerate(LEVELS):
        parts.append(f'<rect x="{716 + i * 18}" y="195" width="11" height="11" rx="3" fill="{color}"/>')
    parts.append('<text x="812" y="204" class="muted">more</text>')
    return "\n    ".join(parts)


def render():
    payload = load_payload()
    days = payload["days"][-371:]
    total = payload.get("total", sum(day["count"] for day in days))
    current = payload.get("current_streak", 0)
    longest = payload.get("longest_streak", 0)

    return f"""<svg width="880" height="250" viewBox="0 0 880 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Animated GitHub contribution graph for Tushar Katpara">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#050816"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      .title {{ font: 700 18px Consolas, monospace; fill: #e5e7eb; }}
      .muted {{ font: 12px Consolas, monospace; fill: #94a3b8; }}
      .stat {{ font: 700 15px Consolas, monospace; fill: #67e8f9; }}
    </style>
  </defs>
  <rect width="880" height="250" rx="22" fill="#030712"/>
  <rect x="12" y="12" width="856" height="226" rx="18" fill="url(#bg)" stroke="#26354f"/>
  <circle cx="34" cy="35" r="5" fill="#ff5f57"/>
  <circle cx="52" cy="35" r="5" fill="#ffbd2e"/>
  <circle cx="70" cy="35" r="5" fill="#28c840"/>
  <text x="94" y="40" class="muted">contributions.log</text>
  <text x="34" y="64" class="title" filter="url(#glow)">$ git activity --last-year</text>
  <g>
    {render_cells(days)}
  </g>
  <g>
    {render_legend()}
  </g>
  <text x="44" y="222" class="stat">{total:,} contributions tracked</text>
  <text x="292" y="222" class="stat">current streak: {current} days</text>
  <text x="536" y="222" class="stat">longest streak: {longest} days</text>
</svg>
"""


if __name__ == "__main__":
    OUTPUT.write_text(render(), encoding="utf-8")
