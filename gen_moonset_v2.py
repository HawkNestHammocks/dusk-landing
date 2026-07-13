#!/usr/bin/env python3
# MOONSET packaging round 2 — four store-shelf-professional directions.
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700'
     '&family=Inter:wght@400;500;600;700;800;900&family=Oswald:wght@400;500;600;700'
     '&family=Poppins:wght@500;600;700;800&family=DM+Serif+Display&display=swap" rel="stylesheet">')

def mark(w, gold="#c99b3f", ink="#f2eddd", stars=True):
    st = f'''<path d="M56 44 l1.7 4.6 4.9.3 -3.9 3 1.4 4.7 -4.1-2.8 -4.1 2.8 1.4-4.7 -3.9-3 4.9-.3Z" fill="{ink}" opacity=".9"/>
    <circle cx="146" cy="58" r="3" fill="{ink}" opacity=".75"/>''' if stars else ""
    return f'''<svg viewBox="0 0 200 176" style="width:{w}px">
  <defs><clipPath id="ab{w}"><rect x="0" y="0" width="200" height="104"/></clipPath></defs>
  <g clip-path="url(#ab{w})"><circle cx="100" cy="104" r="46" fill="{gold}"/></g>
  <line x1="22" y1="104" x2="178" y2="104" stroke="{gold}" stroke-width="4" stroke-linecap="round"/>
  <line x1="64" y1="124" x2="136" y2="124" stroke="{gold}" stroke-width="3.4" stroke-linecap="round" opacity=".55"/>
  <line x1="78" y1="142" x2="122" y2="142" stroke="{gold}" stroke-width="3" stroke-linecap="round" opacity=".32"/>
  <line x1="90" y1="158" x2="110" y2="158" stroke="{gold}" stroke-width="2.6" stroke-linecap="round" opacity=".18"/>
  {st}</svg>'''

ACT = [("Magnesium Glycinate","300mg"),("L-Theanine","200mg"),("Glycine","3g"),
       ("Ashwagandha KSM-66","300mg"),("Saffron (affron)","28mg")]

LABELS = {}

# ===== A · CLINICAL CLEAN — white body, navy band, gold mark (Ritual/Vital-Proteins shelf energy) =====
rows = "".join(f'<div class="ar"><b>{n}</b><i>{d}</i></div>' for n,d in ACT)
LABELS["moonset-a"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#f7f5f0;color:#152244;font-family:Inter,sans-serif;position:relative;text-align:center}}
.band{{background:#152244;color:#f7f5f0;padding:46px 60px 38px}}
.brand{{font-family:Inter;font-weight:900;font-size:96px;letter-spacing:4px;line-height:1;color:#fff;margin-top:16px}}
.desc{{font-family:Oswald;font-weight:500;font-size:26px;letter-spacing:9px;color:#d9b25f;margin-top:12px}}
.mid{{padding:34px 60px 0}}
.tagline{{font-size:21px;color:#4a5677;font-weight:500;margin-bottom:24px}}
.bens{{display:flex;gap:10px;justify-content:center;margin-bottom:28px}}
.b{{background:#152244;color:#fff;border-radius:100px;padding:11px 18px;font-size:14px;font-weight:700;letter-spacing:.5px}}
.b.g{{background:#d9b25f;color:#152244}}
.ah{{font-family:Oswald;letter-spacing:3px;font-size:14px;color:#8d97b5;margin-bottom:2px}}
.ar{{display:flex;justify-content:space-between;padding:13px 8px;font-size:22px;border-bottom:1.5px solid #e2ddd2;text-align:left}}
.ar b{{font-weight:700;color:#152244}} .ar i{{font-style:normal;font-weight:800;color:#b8860b}}
.flav{{margin-top:26px;display:inline-block;border:2px solid #152244;border-radius:12px;padding:10px 26px;font-weight:800;font-size:20px;letter-spacing:1px}}
.nw{{position:absolute;bottom:52px;left:60px;right:60px;display:flex;justify-content:space-between;font-family:Oswald;font-size:20px;letter-spacing:2px;color:#152244;border-top:2px solid #152244;padding-top:18px}}
</style></head><body><div class="p">
<div class="band"><div style="display:flex;justify-content:center">{mark(120,"#d9b25f","#fff")}</div>
<div class="brand">MOONSET</div><div class="desc">WIND-DOWN COCOA</div></div>
<div class="mid">
<div class="tagline">Clinically-dosed evening cocoa for deep, natural sleep</div>
<div class="bens"><span class="b">MELATONIN-FREE</span><span class="b g">CAFFEINE-FREE</span><span class="b">VEGAN</span></div>
<div class="ah">ACTIVES PER SERVING</div>{rows}
<div class="flav">RICH CHOCOLATE · MIX WITH MILK</div>
</div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span>30 SERVINGS</span></div>
</div></body></html>'''

# ===== B · TWILIGHT DREAM — lavender/indigo gradient, stars, friendly rounded (Olly/sleep-aisle energy) =====
LABELS["moonset-b"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:linear-gradient(180deg,#2b2a5e 0%,#4b3f8f 45%,#7a6ac0 80%,#a99ad8 100%);color:#fff;font-family:Poppins,sans-serif;position:relative;text-align:center;padding:60px 58px}}
.stars svg{{position:absolute;top:0;left:0;width:100%}}
.slp{{font-weight:800;font-size:30px;letter-spacing:8px;color:#ffd98a;margin-top:26px}}
.brand{{font-family:Poppins;font-weight:800;font-size:92px;letter-spacing:2px;line-height:1;color:#fff;margin-top:6px;text-shadow:0 4px 14px rgba(0,0,0,.25)}}
.desc{{font-weight:600;font-size:24px;letter-spacing:3px;color:#e4dcff;margin-top:10px}}
.pill{{display:inline-block;margin-top:24px;background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.55);border-radius:100px;padding:12px 26px;font-weight:700;font-size:19px}}
.bl{{margin-top:34px;text-align:left;background:rgba(20,18,50,.35);border-radius:22px;padding:26px 30px;backdrop-filter:blur(2px)}}
.bl .h{{font-weight:800;letter-spacing:3px;font-size:15px;color:#ffd98a;margin-bottom:10px;text-align:center}}
.br{{display:flex;justify-content:space-between;padding:11px 4px;font-size:21px;border-bottom:1px solid rgba(255,255,255,.18)}}
.br b{{font-weight:600}} .br i{{font-style:normal;font-weight:800;color:#ffd98a}}
.badges{{display:flex;gap:10px;justify-content:center;margin-top:26px}}
.bd{{background:#fff;color:#4b3f8f;border-radius:100px;padding:10px 18px;font-weight:800;font-size:14px}}
.nw{{position:absolute;bottom:50px;left:58px;right:58px;display:flex;justify-content:space-between;font-weight:700;font-size:19px;letter-spacing:1px;color:#fff;border-top:1.5px solid rgba(255,255,255,.4);padding-top:18px}}
</style></head><body><div class="p">
<div class="stars"><svg viewBox="0 0 840 300"><g fill="#fff" opacity=".8">
<circle cx="90" cy="60" r="3"/><circle cx="230" cy="120" r="2"/><circle cx="420" cy="40" r="2.6"/>
<circle cx="600" cy="100" r="2"/><circle cx="750" cy="60" r="3"/><circle cx="330" cy="180" r="1.8"/><circle cx="680" cy="190" r="1.8"/></g></svg></div>
<div style="display:flex;justify-content:center">{mark(130,"#ffd98a","#fff")}</div>
<div class="slp">SLEEP</div>
<div class="brand">moonset</div>
<div class="desc">wind-down cocoa</div>
<div class="pill">☾ &nbsp;Fall asleep naturally &mdash; wake up clear</div>
<div class="bl"><div class="h">CLINICALLY-DOSED ACTIVES</div>
{"".join(f'<div class="br"><b>{n}</b><i>{d}</i></div>' for n,d in ACT)}</div>
<div class="badges"><span class="bd">MELATONIN-FREE</span><span class="bd">CAFFEINE-FREE</span><span class="bd">VEGAN</span></div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span>30 SERVINGS</span></div>
</div></body></html>'''

# ===== C · COCOA CRAFT — chocolate brown + cream, cozy premium hot-cocoa tin (Williams-Sonoma energy) =====
LABELS["moonset-c"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#2e1d12;color:#f4e9d8;font-family:Inter,sans-serif;position:relative;text-align:center;padding:56px 58px}}
.p::before{{content:"";position:absolute;inset:22px;border:2px solid #c99b3f;border-radius:10px;opacity:.6}}
.est{{font-family:Oswald;font-size:15px;letter-spacing:6px;color:#c99b3f}}
.brand{{font-family:'DM Serif Display';font-size:104px;letter-spacing:3px;line-height:1;color:#f4e9d8;margin-top:14px}}
.desc{{font-family:Oswald;font-weight:500;font-size:25px;letter-spacing:10px;color:#c99b3f;margin-top:12px}}
.script{{font-family:'DM Serif Display';font-style:italic;font-size:30px;color:#d8b98a;margin-top:20px}}
.div{{width:200px;height:1px;background:linear-gradient(90deg,transparent,#c99b3f,transparent);margin:26px auto}}
.ar{{display:flex;justify-content:space-between;padding:12px 30px;font-size:21px;border-bottom:1px dotted rgba(201,155,63,.4);text-align:left}}
.ar b{{font-weight:600;color:#f4e9d8}} .ar i{{font-style:normal;font-family:Oswald;font-weight:600;color:#e2b45c}}
.badges{{display:flex;gap:10px;justify-content:center;margin-top:28px}}
.bd{{border:1.5px solid #c99b3f;color:#e8ce96;border-radius:6px;padding:10px 16px;font-weight:700;font-size:13.5px;letter-spacing:1px}}
.nw{{position:absolute;bottom:54px;left:58px;right:58px;display:flex;justify-content:space-between;font-family:Oswald;font-size:19px;letter-spacing:2px;color:#c99b3f;border-top:1px solid rgba(201,155,63,.5);padding-top:18px}}
</style></head><body><div class="p">
<div class="est">SMALL-BATCH · EST. 2026</div>
<div style="display:flex;justify-content:center;margin-top:18px">{mark(140,"#c99b3f","#f4e9d8")}</div>
<div class="brand">MOONSET</div>
<div class="desc">WIND-DOWN COCOA</div>
<div class="script">a rich, drinking-chocolate nightcap &mdash; without the caffeine</div>
<div class="div"></div>
{"".join(f'<div class="ar"><b>{n}</b><i>{d}</i></div>' for n,d in ACT)}
<div class="badges"><span class="bd">MELATONIN-FREE</span><span class="bd">CAFFEINE-FREE</span><span class="bd">VEGAN</span><span class="bd">NO ADDED SUGAR</span></div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span>30 SERVINGS</span></div>
</div></body></html>'''

# ===== D · SPORT MINIMAL — white + huge navy type + gold moon, benefit-forward (Momentous/Thorne energy) =====
LABELS["moonset-d"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#fdfcfa;color:#10182e;font-family:Inter,sans-serif;position:relative;padding:64px 60px;text-align:left}}
.topline{{display:flex;align-items:center;justify-content:space-between}}
.wd{{font-family:Oswald;font-size:17px;letter-spacing:4px;color:#8a8f9e}}
.brand{{font-family:Inter;font-weight:900;font-size:112px;letter-spacing:-3px;line-height:.92;margin-top:34px}}
.benefit{{font-family:Inter;font-weight:900;font-size:44px;color:#b8860b;margin-top:10px;letter-spacing:-1px}}
.sub{{font-size:20px;color:#5a6274;margin-top:18px;max-width:560px;line-height:1.5}}
.rule{{height:3px;background:#10182e;margin:34px 0 0}}
.ar{{display:flex;justify-content:space-between;padding:14px 2px;font-size:22px;border-bottom:1.5px solid #e8e4dc}}
.ar b{{font-weight:700}} .ar i{{font-style:normal;font-weight:800;color:#b8860b}}
.badges{{display:flex;gap:9px;margin-top:28px;flex-wrap:wrap}}
.bd{{background:#10182e;color:#fff;border-radius:6px;padding:10px 16px;font-weight:800;font-size:13.5px;letter-spacing:.5px}}
.nw{{position:absolute;bottom:54px;left:60px;right:60px;display:flex;justify-content:space-between;font-weight:800;font-size:19px;letter-spacing:1px;border-top:3px solid #10182e;padding-top:16px}}
</style></head><body><div class="p">
<div class="topline">{mark(96,"#b8860b","#10182e",stars=False)}<span class="wd">WIND-DOWN COCOA</span></div>
<div class="brand">MOON<br>SET</div>
<div class="benefit">DEEP SLEEP, ON REPEAT.</div>
<div class="sub">Five clinically-dosed actives in a rich chocolate mix. Stir into warm or cold milk, 30 minutes before bed.</div>
<div class="rule"></div>
{"".join(f'<div class="ar"><b>{n}</b><i>{d}</i></div>' for n,d in ACT)}
<div class="badges"><span class="bd">MELATONIN-FREE</span><span class="bd">CAFFEINE-FREE</span><span class="bd">VEGAN</span><span class="bd">3RD-PARTY TESTED</span></div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span>30 SERVINGS</span></div>
</div></body></html>'''

for n,h in LABELS.items():
    open(os.path.join(OUT,n+".html"),"w").write(h); print("wrote",n)
