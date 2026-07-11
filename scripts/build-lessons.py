#!/usr/bin/env python3
import subprocess, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Flat, ordered walkthrough. dir/slug -> output at <dir>/<slug>.html
SETUP = [
    ("00",  "00-start-here-newbie", "Start Here"),
    ("01",  "01-getting-started",   "Getting Started"),
    ("01b", "01b-turn-on-cowork",   "Cowork & Install"),
    ("02",  "02-projects-setup",    "Projects Setup"),
    ("03",  "03-the-vocabulary",    "The Vocabulary"),
    ("04",  "04-why-claude",        "Why Claude"),
    ("05",  "05-bring-your-memory", "Bring Your Memory"),
    ("06",  "06-the-three-modes",   "The Three Modes"),
    ("07",  "07-prompt-like-a-buyer","Prompt Like a Buyer"),
    ("08",  "08-models-and-plans",  "Models & Plans"),
]
# Journey order (JOURNEY.md): Phase 0 -> Phase 1 -> Branch B -> Branch A.
# journey-navigator keeps its original "00" but sits third, after Phase 0.
LESSONS = [
    ("01", "01-setup-my-workspace",      "Setup My Workspace"),
    ("02", "02-claude-acquisition-setup","Acquisition Setup"),
    ("00", "00-journey-navigator",       "Journey Navigator"),
    ("03", "03-buy-box-builder",         "Buy-Box Builder"),
    ("04", "04-vertical-research",       "Vertical Research"),
    ("05", "05-deal-finder",             "Deal Finder"),
    ("06", "06-broker-finder",           "Broker Finder"),
    ("07", "07-market-monitor",          "Market Monitor"),
    ("08", "08-outreach-engine",         "Outreach Engine"),
    ("09", "09-aq-analyzer",             "AQ Analyzer"),
    ("10", "10-discovery-interviewer",   "Discovery Interviewer"),
    ("11", "11-valuation",               "Valuation & Add-Backs"),
    ("12", "12-deal-stacker",            "Deal Stacker"),
    ("13", "13-loi-drafter",             "LOI Drafter"),
    ("14", "14-dd-engine",               "DD Engine"),
    ("15", "15-modernization-audit",     "Modernization Audit"),
    ("16", "16-owner-dependency-audit",  "Owner Dependency Audit"),
    ("17", "17-sop-extractor",           "SOP Extractor"),
    ("18", "18-margin-finder",           "Margin Finder"),
    ("19", "19-customer-engine",         "Customer Engine"),
    ("20", "20-multiple-builder",        "Multiple Builder"),
]

pages = []
for num, slug, short in SETUP:
    pages.append(dict(num=num, slug=slug, short=short, d="setup"))
for num, slug, short in LESSONS:
    pages.append(dict(num=num, slug=slug, short=short, d="lessons"))
for p in pages:
    p["out"] = f'{p["d"]}/{p["slug"]}.html'

CSS = """
:root{--paper:#FAF8F5;--ink:#2D2926;--gold:#C4A35A;--copper:#B87333;--line:#E4DDD2;--muted:#6B6459;--card:#FFFFFF;--dark:#211E1B;--mono:'JetBrains Mono',ui-monospace,monospace;--sans:'Inter',-apple-system,sans-serif;}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.7;-webkit-font-smoothing:antialiased}
.layout{display:grid;grid-template-columns:250px 1fr;min-height:100vh}
.sidebar{border-right:1px solid var(--line);padding:28px 20px;position:sticky;top:0;height:100vh;overflow-y:auto;background:var(--paper)}
.brand{display:block;font-family:var(--mono);font-weight:700;font-size:13px;letter-spacing:.12em;text-transform:uppercase;text-decoration:none;color:var(--ink)}
.brand small{display:block;color:var(--copper);font-weight:400;margin-top:2px;font-size:10px;letter-spacing:.16em}
.group{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin:26px 0 8px}
a.nav{display:flex;gap:10px;align-items:baseline;padding:6px 8px;border-radius:3px;font-size:13px;text-decoration:none;color:#443f38}
a.nav:hover{background:rgba(196,163,90,.1)}
a.nav.active{background:rgba(196,163,90,.16);color:var(--ink);font-weight:600}
a.nav .n{font-family:var(--mono);font-size:10.5px;color:var(--copper);min-width:18px}
.content{padding:40px 52px 80px;max-width:900px;margin:0 auto}
.crumb{font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin-bottom:22px}
.crumb a{text-decoration:none;color:var(--muted)}
article h1{font-size:31px;line-height:1.2;margin:0 0 10px}
article h2{font-size:21px;margin:38px 0 10px}
article h3{font-size:16.5px;margin:26px 0 8px}
article h1 em,article h2 em{font-style:normal;color:var(--copper)}
article p,article li{font-size:15.5px;color:#3a352f}
article a{color:var(--copper)}
article strong{color:var(--ink)}
article code{font-family:var(--mono);font-size:13px;background:rgba(184,115,51,.09);border:1px solid var(--line);border-radius:3px;padding:1px 5px}
article pre{background:var(--dark);color:#f3ede2;border-radius:5px;padding:16px 18px;overflow-x:auto}
article pre code{background:none;border:none;color:inherit;padding:0;font-size:13px;line-height:1.6}
article blockquote{margin:16px 0;padding:8px 18px;border-left:3px solid var(--gold);background:rgba(196,163,90,.07);color:#4a443c}
article blockquote p{margin:6px 0}
.tablewrap{overflow-x:auto;margin:18px 0}
article table{border-collapse:collapse;width:100%;font-size:14px}
article th,article td{border:1px solid var(--line);padding:8px 12px;text-align:left;vertical-align:top}
article th{background:rgba(184,115,51,.06);font-family:var(--mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted)}
article hr{border:none;border-top:1px solid var(--line);margin:34px 0}
article ul,article ol{padding-left:22px}
article li{margin:5px 0}
.pager{display:flex;justify-content:space-between;gap:14px;margin-top:48px;border-top:1px solid var(--line);padding-top:22px}
.pager a{flex:1;max-width:48%;text-decoration:none;border:1px solid var(--line);border-radius:4px;padding:12px 16px;font-size:13px;color:var(--ink)}
.pager a:hover{border-color:var(--gold)}
.pager a.next{text-align:right;margin-left:auto}
.pager .lbl{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:3px}
@media(max-width:820px){.layout{grid-template-columns:1fr}.sidebar{position:static;height:auto;border-right:none;border-bottom:1px solid var(--line)}.content{padding:26px 20px 60px}}
"""

TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__ · SMB Wealth Builder</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>__CSS__</style>
</head>
<body>
<div class="layout">
<aside class="sidebar">
<a class="brand" href="../index.html">SMB Wealth Builder<small>ai.smbwealthbuilder.com</small></a>
__SIDEBAR__
</aside>
<main class="content">
<div class="crumb"><a href="../index.html">← Home</a></div>
<article>
__CONTENT__
</article>
<nav class="pager">__PAGER__</nav>
</main>
</div>
</body>
</html>
"""

# Mirrors the landing-page sidebar exactly so lessons feel like the same site.
# Setup items link to lesson pages; everything else back to index.html anchors.
NAV = [
    ("group", "Start Here", None),
    ("00",  "Start Here (Newbie)",   "setup/00-start-here-newbie.html"),
    ("01",  "Getting Started",       "setup/01-getting-started.html"),
    ("01b", "Cowork &amp; Install",  "setup/01b-turn-on-cowork.html"),
    ("02",  "Projects Setup",        "setup/02-projects-setup.html"),
    ("03",  "The Vocabulary",        "setup/03-the-vocabulary.html"),
    ("04",  "Why Claude",            "setup/04-why-claude.html"),
    ("05",  "Bring Your Memory",     "setup/05-bring-your-memory.html"),
    ("06",  "The Three Modes",       "setup/06-the-three-modes.html"),
    ("07",  "Prompt Like a Buyer",   "setup/07-prompt-like-a-buyer.html"),
    ("08",  "Models &amp; Plans",    "setup/08-models-and-plans.html"),
    ("→",   "Install the Plugin",    "index.html#install"),
    ("group", "Skill Lessons", None),
    # generated from LESSONS below (journey order)
    ("group", "The System", None),
    ("09", "Find Your Starting Point", "index.html#journey"),
    ("10", "The Numbers Game",         "index.html#numbers"),
    ("11", "12-Part Deal Engine",      "index.html#system"),
    ("12", "Three Sourcing Lanes",     "index.html#lanes"),
    ("13", "Skill Demos",              "index.html#demos"),
    ("group", "Execute", None),
    ("14", "Week-One Playbook",  "index.html#weekone"),
    ("15", "216 Ways to Fund It","index.html#financing"),
    ("16", "The Deal Advisor",   "index.html#advisor"),
    ("17", "The Prompt Vault",   "index.html#vault"),
    ("18", "The Video Series",   "index.html#videos"),
    ("group", "Go Deeper", None),
    ("19", "The Community", "index.html#community"),
    ("20", "Ways In",       "index.html#offers"),
    ("21", "Appendix",      "index.html#appendix"),
]

# splice the lesson entries (journey order) into NAV under "Skill Lessons"
_li = next(i for i, (n, l, h) in enumerate(NAV) if n == "group" and l == "Skill Lessons") + 1
NAV[_li:_li] = [(num, short, f"lessons/{slug}.html") for num, slug, short in LESSONS]

def sidebar_for(cur):
    out = []
    for num, label, href in NAV:
        if num == "group":
            out.append(f'<div class="group">{label}</div>')
            continue
        cls = "nav active" if href == cur else "nav"
        out.append(f'<a class="{cls}" href="../{href}"><span class="n">{num}</span>{label}</a>')
    return "\n".join(out)

def pager_for(i):
    parts = []
    if i > 0:
        prev = pages[i-1]
        parts.append(f'<a class="prev" href="../{prev["out"]}"><span class="lbl">← Previous</span>{prev["short"]}</a>')
    if i < len(pages)-1:
        nxt = pages[i+1]
        parts.append(f'<a class="next" href="../{nxt["out"]}"><span class="lbl">Next →</span>{nxt["short"]}</a>')
    return "".join(parts)

for i, p in enumerate(pages):
    src = ROOT / p["d"] / f'{p["slug"]}.md'
    if not src.exists():
        print("SKIP missing", src); continue
    body = subprocess.run(["pandoc","-f","gfm","-t","html5",str(src)],
                          capture_output=True, text=True, check=True).stdout
    # wrap tables for horizontal scroll on mobile
    body = body.replace("<table>", '<div class="tablewrap"><table>').replace("</table>", "</table></div>")
    title = p["short"]
    html = (TPL.replace("__CSS__", CSS)
               .replace("__TITLE__", title)
               .replace("__SIDEBAR__", sidebar_for(p["out"]))
               .replace("__PAGER__", pager_for(i))
               .replace("__CONTENT__", body))
    dest = ROOT / p["out"]
    dest.write_text(html)
    print("wrote", p["out"], f'({len(html)//1024}KB)')

print("DONE:", len(pages), "pages")
