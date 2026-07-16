#!/usr/bin/env python3
# Ads v2 — FULL-BLEED product photos, minimal overlay, one message per ad. No lime green on SM.
import os
OUT = os.path.dirname(os.path.abspath(__file__))
F = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500'
     '&family=Anton&family=Space+Grotesk:wght@500;600;700&family=Jost:wght@500;600;700&display=swap" rel="stylesheet">')

BASE = """*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}
body{width:1080px;height:1350px;overflow:hidden;position:relative;color:#fff}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;inset:0}
"""

# ---------- MOONSET: full-bleed, serif, slim gold pill ----------
def ms(bg, headline, sub, shade_top=".55", shade_bot=".72", pos="top", extra=""):
    top_block = f'''<div class="txt {'txtb' if pos=='bottom' else ''}">
  <h1>{headline}</h1>
  {f'<div class="sub">{sub}</div>' if sub else ''}
</div>'''
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{font-family:Jost,sans-serif}}
.shade{{background:linear-gradient(180deg,rgba(8,10,26,{shade_top}) 0%,transparent 38%,transparent 58%,rgba(8,10,26,{shade_bot}) 100%)}}
.txt{{position:absolute;top:76px;left:60px;right:60px;text-align:center}}
.txt.txtb{{top:auto;bottom:250px}}
h1{{font-family:'Fraunces',serif;font-weight:600;font-size:88px;line-height:1.06;text-shadow:0 4px 34px rgba(0,0,0,.65)}}
h1 em{{font-style:italic;color:#e8c983}}
.sub{{margin-top:18px;font-size:28px;font-weight:600;color:#f0ebdc;letter-spacing:1px;text-shadow:0 2px 16px rgba(0,0,0,.75)}}
.pill{{position:absolute;bottom:64px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:22px;background:rgba(13,18,48,.88);border:1.5px solid #d9b25f;border-radius:100px;padding:16px 20px 16px 34px;box-shadow:0 20px 50px rgba(0,0,0,.5);white-space:nowrap}}
.pill .p{{font-family:'Fraunces';font-weight:600;font-size:36px}}
.pill .p small{{font-size:20px;color:#9aa0c0;text-decoration:line-through;font-family:Jost;font-weight:500;margin-left:8px}}
.pill .d{{font-size:17px;color:#d9b25f;font-weight:600;letter-spacing:1.5px}}
.pill .cta{{background:linear-gradient(180deg,#e8c983,#c99a3f);color:#0d1230;font-weight:700;font-size:20px;padding:14px 28px;border-radius:100px}}
{extra}
</style></head><body>
<img class="bg" src="{bg}">
<div class="shade"></div>
{top_block}
<div class="pill"><span class="p">$41.30 <small>$59</small></span><span class="d">FOUNDING BATCH · 92% CLAIMED</span><span class="cta">Claim 30% Off →</span></div>
</body></html>'''

A = {}
A["ms2-1"] = ms("../images/moonset-g5-night.png",
                "One warm cup.<br><em>Thirty minutes later, gone.</em>",
                "Melatonin-free · clinically dosed · dark chocolate")
A["ms2-2"] = ms("../images/moonset-morning.png",
                "Wake up clear.<br><em>Not groggy.</em>",
                "The melatonin-free night ritual", shade_top=".5")
A["ms2-3"] = ms("../images/moonset-g5-tin3.png",
                "Melatonin-free.<br><em>Clinically dosed.</em>",
                "Saffron · magnesium · L-theanine · glycine · ashwagandha", shade_top=".42", shade_bot=".6")
A["ms2-4"] = ms("../images/moonset-hands.png",
                "The night ritual<br><em>your evenings are missing.</em>",
                "One scoop. Warm milk. Deep, natural sleep.")
A["ms2-5"] = ms("../images/moonset-g5-night.png",
                "Founding Batch №1<br><em>is 92% claimed.</em>",
                "When it's gone, the price goes up.", shade_top=".6")

# ---------- SLEEP MAXING: full-bleed, Anton, cyan/pink/sun only ----------
def sm(bg, headline, sub, shade_top=".5", shade_bot=".72", extra_html=""):
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{font-family:'Space Grotesk',sans-serif}}
.shade{{background:linear-gradient(180deg,rgba(14,16,51,{shade_top}) 0%,transparent 38%,transparent 58%,rgba(14,16,51,{shade_bot}) 100%)}}
.txt{{position:absolute;top:70px;left:50px;right:50px;text-align:center}}
h1{{font-family:Anton;font-size:112px;line-height:1;text-transform:uppercase;text-shadow:6px 6px 0 rgba(14,16,51,.85)}}
h1 .c{{color:#7de8ff}}
.sub{{margin-top:16px;font-size:28px;font-weight:600;color:#f2e9ff;text-shadow:0 2px 14px rgba(0,0,0,.7)}}
.sub b{{color:#ffd76e}}
.pill{{position:absolute;bottom:64px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:20px;background:rgba(14,16,51,.92);border:2.5px solid #7de8ff;border-radius:18px;padding:14px 18px 14px 30px;box-shadow:6px 6px 0 rgba(14,16,51,.6);white-space:nowrap}}
.pill .p{{font-family:Anton;font-size:40px}}
.pill .p small{{font-size:20px;color:#8f89b8;text-decoration:line-through;font-family:'Space Grotesk';font-weight:600;margin-left:8px}}
.pill .d{{font-size:16.5px;color:#ffd76e;font-weight:700;letter-spacing:1px}}
.pill .cta{{background:#7de8ff;color:#0e1033;font-weight:700;font-size:20px;padding:14px 26px;border-radius:12px}}
{extra_html}
</style></head><body>
<img class="bg" src="{bg}">
<div class="shade"></div>
<div class="txt">
  <h1>{headline}</h1>
  {f'<div class="sub">{sub}</div>' if sub else ''}
</div>
<div class="pill"><span class="p">$41.30 <small>$59</small></span><span class="d">FOUNDING DROP · 37 LEFT</span><span class="cta">MAX MY SLEEP →</span></div>
</body></html>'''

A["sm2-1"] = sm("../images/sleepmaxing-c-hero2.png",
                "MAX YOUR SLEEP.<br><span class='c'>WAKE UP DIFFERENT.</span>",
                "Tastes like <b>chocolate</b>. Works like science.")
A["sm2-2"] = sm("../images/sleepmax-neon-bed.png",
                "PHONE DOWN.<br><span class='c'>SLEEP MAXED.</span>",
                "One scoop · warm milk · 30 minutes")
A["sm2-3"] = sm("../images/sleepmaxing-c-tin.png",
                "0 MELATONIN.<br><span class='c'>0 GROGGY MORNINGS.</span>",
                "Full clinical doses. Nothing fake.", shade_top=".42", shade_bot=".62")
A["sm2-4"] = sm("../images/sleepmax-choco.png",
                "BEDTIME JUST GOT<br><span class='c'>A GLOW-UP.</span>",
                "The nightly sleep drink that tastes like <b>chocolate</b>")
A["sm2-5"] = sm("../images/sleepmaxing-c-hero2.png",
                "SLEEP SCORE:<br><span class='c'>68 → 87.</span>",
                "Avg tester gain in two weeks* · 0 melatonin")

for n, h in A.items():
    open(os.path.join(OUT, n + ".html"), "w").write(h)
    print("wrote", n)
