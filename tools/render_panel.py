from pathlib import Path


OUTPUT = Path("sysinfo.svg")

ROWS = [
    ("user", "TUshARKatpara"),
    ("role", "Data Science Student"),
    ("focus", "Machine Learning, EDA, Model Deployment"),
    ("stack", "Python, Pandas, NumPy, scikit-learn, SQL"),
    ("github", "6 visible repos, 392 tracked contributions"),
    ("projects", "Movie Rating Analysis, HR Analytics, Jarvis AI"),
    ("learning", "Deep Learning, MLOps, Power BI, GitHub"),
    ("status", "Building portfolio projects for real interviews"),
]

LINKS = [
    ("movie-rating-analysis", "rating prediction + EDA"),
    ("dA-HR-ANALYTICS-PROJECT", "HR analytics dashboard story"),
    ("ds-lab", "Python Jarvis assistant"),
    ("projects", "portfolio experiments"),
]


def esc(text):
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def row_markup():
    parts = []
    for i, (key, value) in enumerate(ROWS):
        y = 92 + i * 34
        delay = 0.18 + i * 0.12
        parts.append(
            f"""
  <g opacity="0">
    <text x="38" y="{y}" class="key">{esc(key)}</text>
    <text x="152" y="{y}" class="value">{esc(value)}</text>
    <animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.35s" fill="freeze"/>
  </g>"""
        )
    return "".join(parts)


def link_markup():
    parts = []
    for i, (name, desc) in enumerate(LINKS):
        y = 366 + i * 24
        delay = 1.15 + i * 0.12
        parts.append(
            f"""
  <g opacity="0">
    <text x="48" y="{y}" class="project">./{esc(name)}</text>
    <text x="266" y="{y}" class="muted">{esc(desc)}</text>
    <animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.35s" fill="freeze"/>
  </g>"""
        )
    return "".join(parts)


def render():
    return f"""<svg width="520" height="500" viewBox="0 0 520 500" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Terminal style profile panel for Tushar Katpara">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#090f1f"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <filter id="softGlow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <style>
      .mono {{ font-family: Consolas, 'Courier New', monospace; }}
      .key {{ font: 700 15px Consolas, monospace; fill: #67e8f9; }}
      .value {{ font: 14px Consolas, monospace; fill: #e5e7eb; }}
      .muted {{ font: 12px Consolas, monospace; fill: #94a3b8; }}
      .project {{ font: 13px Consolas, monospace; fill: #c4b5fd; }}
    </style>
  </defs>
  <rect width="520" height="500" rx="22" fill="#050816"/>
  <rect x="12" y="12" width="496" height="476" rx="18" fill="url(#bg)" stroke="#26354f"/>
  <line x1="12" y1="58" x2="508" y2="58" stroke="#26354f"/>
  <circle cx="34" cy="35" r="5" fill="#ff5f57"/>
  <circle cx="52" cy="35" r="5" fill="#ffbd2e"/>
  <circle cx="70" cy="35" r="5" fill="#28c840"/>
  <text x="94" y="40" class="muted">whoami --verbose</text>
  <text x="34" y="84" class="mono" fill="#a78bfa" font-size="15" filter="url(#softGlow)">$ profile.scan()</text>
  {row_markup()}
  <rect x="34" y="326" width="452" height="132" rx="12" fill="#07101f" stroke="#1e3a5f"/>
  <text x="48" y="350" class="key">featured repositories</text>
  {link_markup()}
  <text x="38" y="472" class="muted">signal: practical projects, clean docs, repeatable analysis</text>
</svg>
"""


if __name__ == "__main__":
    OUTPUT.write_text(render(), encoding="utf-8")
