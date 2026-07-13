#!/usr/bin/env python3
# MOONSET round 3 — ULTRA-PREMIUM directions. New marks, new type, luxury restraint.
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500;6..96,600'
     '&family=Cormorant+Garamond:wght@400;500;600&family=Tenor+Sans&family=Questrial'
     '&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">')

# MARK 1 — moonphase strip (watch-complication cue): waxing → full → waning
def phases(w, gold="#cbb37e"):
    return f'''<svg viewBox="0 0 300 44" style="width:{w}px">
  <defs>
    <mask id="wax1"><rect width="300" height="44" fill="black"/><circle cx="30" cy="22" r="13" fill="white"/><circle cx="21" cy="22" r="13" fill="black"/></mask>
    <mask id="wax2"><rect width="300" height="44" fill="black"/><circle cx="90" cy="22" r="13" fill="white"/><rect x="77" y="9" width="13" height="26" fill="black"/></mask>
    <mask id="wan2"><rect width="300" height="44" fill="black"/><circle cx="210" cy="22" r="13" fill="white"/><rect x="210" y="9" width="13" height="26" fill="black"/></mask>
    <mask id="wan1"><rect width="300" height="44" fill="black"/><circle cx="270" cy="22" r="13" fill="white"/><circle cx="279" cy="22" r="13" fill="black"/></mask>
  </defs>
  <rect width="300" height="44" fill="none"/>
  <circle cx="30" cy="22" r="13" fill="{gold}" mask="url(#wax1)"/>
  <circle cx="90" cy="22" r="13" fill="{gold}" mask="url(#wax2)"/>
  <circle cx="150" cy="22" r="14.5" fill="{gold}"/>
  <circle cx="210" cy="22" r="13" fill="{gold}" mask="url(#wan2)"/>
  <circle cx="270" cy="22" r="13" fill="{gold}" mask="url(#wan1)"/>
</svg>'''

# MARK 2 — minimal eclipse: gold disc with offset dark bite
def eclipse(w, gold="#b9a06a", bg="#f4f1e9"):
    return f'''<svg viewBox="0 0 120 120" style="width:{w}px">
  <circle cx="60" cy="60" r="40" fill="{gold}"/>
  <circle cx="74" cy="48" r="36" fill="{bg}"/>
</svg>'''

# MARK 3 — M-crescent monogram in fine double ring
def monogram(w, gold="#cbb37e", ink="#101726"):
    return f'''<svg viewBox="0 0 200 200" style="width:{w}px">
  <circle cx="100" cy="100" r="92" fill="none" stroke="{gold}" stroke-width="1.4"/>
  <circle cx="100" cy="100" r="84" fill="none" stroke="{gold}" stroke-width="0.8" opacity=".7"/>
  <path d="M62 138 V72 L100 118 L138 72 V138" fill="none" stroke="{gold}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M148 60 a20 20 0 1 0 6 14 a15 15 0 1 1 -6 -14Z" fill="{gold}" transform="scale(.62) translate(118,8)"/>
</svg>'''

LABELS = {}

# ===== E · MAISON — near-black, Bodoni didone, moonphase strip, apothecary N° =====
LABELS["moonset-e"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#0b0d14;color:#e9e2d2;font-family:Jost,sans-serif;position:relative;text-align:center;padding:80px 70px}}
.no{{font-family:Jost;font-weight:300;font-size:19px;letter-spacing:7px;color:#8d8674}}
.brand{{font-family:'Bodoni Moda';font-weight:500;font-size:104px;letter-spacing:10px;padding-left:10px;line-height:1;color:#efe8d8;margin-top:40px}}
.desc{{font-family:Jost;font-weight:400;font-size:20px;letter-spacing:9px;color:#cbb37e;margin-top:24px}}
.strip{{margin-top:64px;display:flex;justify-content:center}}
.line{{width:1px;height:78px;background:linear-gradient(180deg,transparent,#cbb37e,transparent);margin:56px auto}}
.body{{font-family:Jost;font-weight:300;font-size:20px;color:#b6ae9b;line-height:1.85;max-width:520px;margin:0 auto}}
.body b{{font-weight:500;color:#e9e2d2}}
.free{{margin-top:56px;font-family:Jost;font-weight:400;font-size:15px;letter-spacing:4px;color:#8d8674}}
.nw{{position:absolute;bottom:64px;left:70px;right:70px;font-family:Jost;font-weight:300;font-size:16px;letter-spacing:4px;color:#8d8674;display:flex;justify-content:space-between}}
</style></head><body><div class="p">
<div class="no">N&deg; 30 &mdash; NUIT</div>
<div class="brand">MOONSET</div>
<div class="desc">WIND-DOWN COCOA</div>
<div class="strip">{phases(320)}</div>
<div class="line"></div>
<div class="body">A nightly drinking chocolate composed of <b>magnesium glycinate</b>, <b>saffron</b>, <b>L&#8209;theanine</b>, <b>glycine</b> &amp; <b>ashwagandha</b> &mdash; in clinical doses, without melatonin or caffeine.</div>
<div class="free">MELATONIN-FREE &nbsp;&middot;&nbsp; CAFFEINE-FREE &nbsp;&middot;&nbsp; VEGAN</div>
<div class="nw"><span>240 G &mdash; 8.5 OZ</span><span>TRENTE NUITS &middot; 30 SERVINGS</span></div>
</div></body></html>'''

# ===== F · ATELIER — bone/ivory, letterspaced caps, eclipse mark, skincare-minimal =====
LABELS["moonset-f"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#f4f1e9;color:#1c1a15;font-family:Questrial,sans-serif;position:relative;text-align:center;padding:90px 70px}}
.brand{{font-family:'Tenor Sans';font-size:74px;letter-spacing:26px;padding-left:26px;line-height:1.1;color:#1c1a15;margin-top:52px}}
.desc{{font-size:18px;letter-spacing:8px;color:#8c8371;margin-top:26px}}
.rule{{width:64px;height:1.5px;background:#b9a06a;margin:60px auto}}
.body{{font-size:20px;color:#4a463c;line-height:1.9;max-width:500px;margin:0 auto;letter-spacing:.4px}}
.acts{{margin-top:58px;font-size:15.5px;letter-spacing:2.5px;color:#8c8371;line-height:2.3}}
.acts b{{color:#1c1a15;font-weight:400}}
.nw{{position:absolute;bottom:66px;left:70px;right:70px;font-size:15px;letter-spacing:3.5px;color:#8c8371;display:flex;justify-content:space-between}}
</style></head><body><div class="p">
<div style="display:flex;justify-content:center">{eclipse(112)}</div>
<div class="brand">MOONSET</div>
<div class="desc">WIND-DOWN COCOA &middot; N&deg;01</div>
<div class="rule"></div>
<div class="body">Five actives at clinical dose, folded into single-origin cocoa. Taken warm, thirty minutes before sleep.</div>
<div class="acts">MAGNESIUM GLYCINATE 300MG &middot; L-THEANINE 200MG<br>GLYCINE 3G &middot; ASHWAGANDHA 300MG &middot; <b>SAFFRON 28MG</b><br>MELATONIN-FREE &middot; CAFFEINE-FREE</div>
<div class="nw"><span>240 G / 8.5 OZ</span><span>30 SERVINGS</span></div>
</div></body></html>'''

# ===== G · GRAND CRU — midnight + gold band, Cormorant, M monogram (Bader energy) =====
LABELS["moonset-g"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#101726;color:#ece5d3;font-family:'Cormorant Garamond',serif;position:relative;text-align:center;padding:74px 66px}}
.brand{{font-weight:500;font-size:100px;letter-spacing:8px;padding-left:8px;line-height:1;color:#f0e9d8;margin-top:34px}}
.desc{{font-family:Jost;font-weight:400;font-size:18px;letter-spacing:8px;color:#cbb37e;margin-top:20px}}
.band{{position:absolute;left:0;right:0;top:760px;background:linear-gradient(180deg,#d6bc82,#b89a58);color:#221c0e;padding:34px 66px}}
.band .t{{font-family:Jost;font-weight:500;font-size:17px;letter-spacing:4px;margin-bottom:8px}}
.band .acts{{font-family:Jost;font-weight:400;font-size:15.5px;letter-spacing:1.8px;line-height:1.9}}
.body{{font-size:26px;font-style:italic;color:#c8bfa8;line-height:1.7;max-width:520px;margin:36px auto 0}}
.free{{position:absolute;bottom:128px;left:66px;right:66px;font-family:Jost;font-weight:400;font-size:14.5px;letter-spacing:4px;color:#8f8871}}
.nw{{position:absolute;bottom:64px;left:66px;right:66px;font-family:Jost;font-weight:300;font-size:16px;letter-spacing:4px;color:#cbb37e;display:flex;justify-content:space-between;border-top:1px solid rgba(203,179,126,.35);padding-top:20px}}
</style></head><body><div class="p">
<div style="display:flex;justify-content:center">{monogram(148)}</div>
<div class="brand">MOONSET</div>
<div class="desc">WIND-DOWN COCOA</div>
<div class="body">The evening composed &mdash;<br>a rich cocoa for deep, natural sleep.</div>
<div class="band">
  <div class="t">CLINICALLY-DOSED ACTIVES</div>
  <div class="acts">MAGNESIUM GLYCINATE 300MG &middot; L-THEANINE 200MG &middot; GLYCINE 3G<br>ASHWAGANDHA KSM-66 300MG &middot; SAFFRON (AFFRON&reg;) 28MG</div>
</div>
<div class="free">MELATONIN-FREE &middot; CAFFEINE-FREE &middot; VEGAN &middot; THIRD-PARTY TESTED</div>
<div class="nw"><span>240 G &mdash; 8.5 OZ</span><span>30 SERVINGS</span></div>
</div></body></html>'''

for n,h in LABELS.items():
    open(os.path.join(OUT,n+".html"),"w").write(h); print("wrote",n)
