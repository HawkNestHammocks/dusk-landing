#!/usr/bin/env python3
# Generates 3 distinct DUSK label front-panel HTML files (portrait, retail-detailed).
import os
OUT = os.path.expanduser("~/projects/dusk-landing")

FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700'
         '&family=Inter:wght@400;500;600;700;800&family=Oswald:wght@400;500;600;700'
         '&family=Bebas+Neue&display=swap" rel="stylesheet">')

ACTIVES = [
    ("Magnesium Glycinate", "300mg"),
    ("L-Theanine", "200mg"),
    ("Glycine", "3g"),
    ("Ashwagandha KSM-66", "300mg"),
    ("Apigenin (chamomile)", "50mg"),
]

# ---------- STYLE A: HEARTH — warm kraft, centered artisanal seal ----------
def style_a():
    rows = "".join(f'<div class="ar"><b>{n}</b><i>{d}</i></div>' for n,d in ACTIVES)
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;box-sizing:border-box}} body{{margin:0}}
.p{{width:900px;height:1400px;background:linear-gradient(172deg,#f4ead0,#e7d9b6);color:#2a2018;
padding:66px 60px;font-family:Inter,sans-serif;position:relative;text-align:center}}
.p::before{{content:"";position:absolute;inset:26px;border:1.5px solid #bd7f34;opacity:.5;border-radius:8px}}
.seal{{width:250px;height:250px;margin:2px auto 20px}}
.rt{{font-family:Oswald;font-size:20px;letter-spacing:5px;fill:#2a2018}}
.brand{{font-family:Fraunces;font-weight:600;font-size:150px;letter-spacing:2px;line-height:.85;color:#241b13}}
.desc{{font-family:Oswald;font-weight:600;font-size:34px;letter-spacing:9px;color:#bd7f34;margin-top:12px}}
.sub{{font-size:20px;color:#6b5c46;margin-top:14px;font-weight:500}}
.rule{{height:2px;background:linear-gradient(90deg,transparent,#bd7f34,transparent);margin:28px 60px}}
.bens{{display:flex;justify-content:center;gap:12px;margin-bottom:26px}}
.b{{border:1.6px solid #241b13;border-radius:40px;padding:10px 20px;font-size:16px;font-weight:700;letter-spacing:.5px}}
.b.f{{background:#241b13;color:#f4ead0}}
.ah{{font-family:Oswald;letter-spacing:3px;font-size:15px;color:#8a7a5f;margin-bottom:10px}}
.ar{{display:flex;justify-content:space-between;padding:9px 40px;font-size:21px;border-bottom:1px dotted rgba(42,32,24,.3)}}
.ar b{{font-weight:600}} .ar i{{font-style:normal;font-family:Oswald;color:#bd7f34;font-weight:600}}
.dir{{font-size:18px;color:#4a3d2c;margin-top:24px;line-height:1.5}} .dir b{{color:#241b13}}
.nw{{position:absolute;bottom:52px;left:0;right:0;font-family:Oswald;font-size:23px;letter-spacing:3px;color:#241b13}}
.nw span{{color:#bd7f34}}
</style></head><body><div class="p">
<div class="seal"><svg viewBox="0 0 250 250"><defs><path id="r" d="M125,125 m-98,0 a98,98 0 1,1 196,0 a98,98 0 1,1 -196,0"/></defs>
<circle cx="125" cy="125" r="118" fill="none" stroke="#241b13" stroke-width="2"/>
<circle cx="125" cy="125" r="100" fill="none" stroke="#bd7f34" stroke-width="1.5"/>
<text class="rt"><textPath href="#r" startOffset="0%">· NIGHTLY WIND-DOWN RITUAL · EST. 2026 </textPath></text>
<g transform="translate(125,128)"><g stroke="#bd7f34" stroke-width="2.4" opacity=".85">
<line x1="0" y1="-70" x2="0" y2="-58"/><line x1="49" y1="-49" x2="41" y2="-41"/><line x1="70" y1="0" x2="58" y2="0"/>
<line x1="-49" y1="-49" x2="-41" y2="-41"/><line x1="-70" y1="0" x2="-58" y2="0"/></g>
<path d="M 24,-40 a 46,46 0 1,0 0,80 a 34,34 0 1,1 0,-80 Z" fill="#241b13"/>
<path d="M34 -7 l3 8.5 9 .4 -7.2 5.6 2.6 8.7 -7.4 -5.1 -7.4 5.1 2.6 -8.7 -7.2 -5.6 9 -.4 Z" fill="#bd7f34"/></g></svg></div>
<div class="brand">DUSK</div><div class="desc">WIND-DOWN COCOA</div>
<div class="sub">A warm nightly ritual for deeper sleep</div><div class="rule"></div>
<div class="bens"><span class="b f">MELATONIN-FREE</span><span class="b f">CAFFEINE-FREE</span><span class="b">VEGAN</span></div>
<div class="ah">— CLINICALLY-DOSED PER SERVING —</div>{rows}
<div class="dir">Stir one scoop into 8oz <b>warm or cold milk</b>,<br>30 minutes before bed.</div>
<div class="nw">NET WT 240g (8.5 OZ) · <span>30 SERVINGS</span></div>
</div></body></html>'''

# ---------- STYLE B: NOCTURNE — tall AG1-style, navy body, clinical rows ----------
def style_b():
    rows = "".join(f'<div class="ar"><b>{n}</b><i>{d}</i></div>' for n,d in ACTIVES)
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;box-sizing:border-box}}
.p{{width:840px;height:1500px;background:#0f1430;color:#f2eddd;padding:70px 64px;font-family:Inter,sans-serif;position:relative}}
.top{{display:flex;align-items:center;gap:18px;margin-bottom:40px}}
.ring{{width:74px;height:74px;flex:0 0 74px}}
.tt{{font-family:Oswald;font-size:16px;letter-spacing:4px;color:#d9b25f;line-height:1.4}}
.brand{{font-family:Fraunces;font-weight:600;font-size:170px;letter-spacing:1px;line-height:.82;color:#f6f1e2}}
.desc{{font-family:Oswald;font-weight:500;font-size:32px;letter-spacing:10px;color:#d9b25f;margin:16px 0 8px}}
.sub{{font-size:20px;color:#b9bcd4;font-weight:400;margin-bottom:34px}}
.bens{{display:flex;gap:10px;margin-bottom:36px}}
.b{{border:1.4px solid #d9b25f;color:#d9b25f;border-radius:6px;padding:11px 16px;font-size:14px;font-weight:700;letter-spacing:1px}}
.b.f{{background:#d9b25f;color:#0f1430}}
.ah{{font-family:Oswald;letter-spacing:3px;font-size:15px;color:#8f93b5;margin-bottom:6px;border-top:1px solid rgba(217,178,95,.3);padding-top:22px}}
.ar{{display:flex;justify-content:space-between;padding:13px 4px;font-size:22px;border-bottom:1px solid rgba(255,255,255,.09)}}
.ar b{{font-weight:500;color:#f2eddd}} .ar i{{font-style:normal;font-family:Oswald;color:#d9b25f;font-weight:600}}
.dir{{font-size:18px;color:#c9cbdf;margin-top:30px;line-height:1.55}} .dir b{{color:#f6f1e2}}
.nw{{position:absolute;bottom:60px;left:64px;right:64px;display:flex;justify-content:space-between;font-family:Oswald;
font-size:20px;letter-spacing:2px;color:#d9b25f;border-top:1px solid rgba(217,178,95,.3);padding-top:20px}}
</style></head><body><div class="p">
<div class="top"><svg class="ring" viewBox="0 0 74 74">
<circle cx="37" cy="37" r="35" fill="none" stroke="#d9b25f" stroke-width="1.5"/>
<path d="M46 22 a19 19 0 1 0 0 30 a14 14 0 1 1 0-30Z" fill="#d9b25f"/>
<path d="M25 20 l1.3 3.6 3.8.2 -3 2.4 1.1 3.7 -3.2-2.2 -3.2 2.2 1.1-3.7 -3-2.4 3.8-.2Z" fill="#d9b25f"/></svg>
<div class="tt">NIGHTLY<br>WIND-DOWN<br>RITUAL</div></div>
<div class="brand">DUSK</div><div class="desc">WIND-DOWN COCOA</div>
<div class="sub">Melatonin-free evening cocoa for deeper, natural sleep</div>
<div class="bens"><span class="b f">MELATONIN-FREE</span><span class="b f">CAFFEINE-FREE</span><span class="b">VEGAN</span></div>
<div class="ah">CLINICALLY-DOSED ACTIVES · PER SERVING</div>{rows}
<div class="dir">Stir one scoop into 8oz <b>warm or cold milk</b>, 30 min before bed.</div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span>30 SERVINGS</span></div>
</div></body></html>'''

# ---------- STYLE C: LULL — clean modern minimal, oat/white + charcoal + teal ----------
def style_c():
    rows = "".join(f'<div class="ar"><b>{n}</b><i>{d}</i></div>' for n,d in ACTIVES)
    return f'''<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>
*{{margin:0;box-sizing:border-box}}
.p{{width:840px;height:1500px;background:#f3f1ea;color:#22262a;padding:74px 66px;font-family:Inter,sans-serif;position:relative}}
.moon{{width:64px;height:64px;margin-bottom:30px}}
.brand{{font-family:Inter;font-weight:800;font-size:158px;letter-spacing:-4px;line-height:.85;color:#15181b}}
.desc{{font-size:26px;letter-spacing:2px;color:#0c6b63;margin:18px 0 6px;font-weight:700;text-transform:uppercase}}
.sub{{font-size:20px;color:#6a7075;font-weight:400;margin-bottom:34px;max-width:560px}}
.bens{{display:flex;gap:10px;margin-bottom:38px}}
.b{{background:#15181b;color:#f3f1ea;border-radius:40px;padding:11px 20px;font-size:14px;font-weight:600;letter-spacing:.5px}}
.b.t{{background:#0c6b63}}
.ah{{font-size:13px;font-weight:700;letter-spacing:2px;color:#0c6b63;margin-bottom:4px}}
.ar{{display:flex;justify-content:space-between;padding:14px 2px;font-size:22px;border-bottom:1px solid #dcd9cf}}
.ar b{{font-weight:600}} .ar i{{font-style:normal;font-weight:700;color:#0c6b63}}
.dir{{font-size:18px;color:#4c5257;margin-top:30px;line-height:1.55}} .dir b{{color:#15181b}}
.nw{{position:absolute;bottom:62px;left:66px;right:66px;display:flex;justify-content:space-between;
font-size:19px;font-weight:700;letter-spacing:1px;color:#15181b;border-top:2px solid #15181b;padding-top:18px}}
.nw span.t{{color:#0c6b63}}
</style></head><body><div class="p">
<svg class="moon" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="none" stroke="#15181b" stroke-width="3"/>
<path d="M42 12 a24 24 0 1 0 0 40 a30 30 0 1 1 0-40Z" fill="#15181b"/></svg>
<div class="brand">DUSK</div><div class="desc">Wind-Down Cocoa</div>
<div class="sub">A warm, caffeine-free evening cocoa built on clinically-dosed calming actives.</div>
<div class="bens"><span class="b">MELATONIN-FREE</span><span class="b t">CAFFEINE-FREE</span><span class="b">VEGAN</span></div>
<div class="ah">ACTIVES PER SERVING</div>{rows}
<div class="dir">Mix one scoop into 8oz <b>warm or cold milk</b>, 30 minutes before bed.</div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span class="t">30 SERVINGS</span></div>
</div></body></html>'''

for name, html, w, h in [("label_a",style_a(),900,1400),("label_b",style_b(),840,1500),("label_c",style_c(),840,1500)]:
    open(os.path.join(OUT,name+".html"),"w").write(html)
    print(name, w, h)
