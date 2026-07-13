#!/usr/bin/env python3
# MOONSET v4 — rectangular tin LOCKED. Elevated ritual wording. E2 = black MAISON, G2 = midnight GRAND CRU.
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500;6..96,600'
     '&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,500'
     '&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">')

def phases(w, gold="#cbb37e"):
    return f'''<svg viewBox="0 0 300 44" style="width:{w}px">
  <defs>
    <mask id="wx1"><rect width="300" height="44" fill="black"/><circle cx="30" cy="22" r="13" fill="white"/><circle cx="21" cy="22" r="13" fill="black"/></mask>
    <mask id="wx2"><rect width="300" height="44" fill="black"/><circle cx="90" cy="22" r="13" fill="white"/><rect x="77" y="9" width="13" height="26" fill="black"/></mask>
    <mask id="wn2"><rect width="300" height="44" fill="black"/><circle cx="210" cy="22" r="13" fill="white"/><rect x="210" y="9" width="13" height="26" fill="black"/></mask>
    <mask id="wn1"><rect width="300" height="44" fill="black"/><circle cx="270" cy="22" r="13" fill="white"/><circle cx="279" cy="22" r="13" fill="black"/></mask>
  </defs>
  <circle cx="30" cy="22" r="13" fill="{gold}" mask="url(#wx1)"/>
  <circle cx="90" cy="22" r="13" fill="{gold}" mask="url(#wx2)"/>
  <circle cx="150" cy="22" r="14.5" fill="{gold}"/>
  <circle cx="210" cy="22" r="13" fill="{gold}" mask="url(#wn2)"/>
  <circle cx="270" cy="22" r="13" fill="{gold}" mask="url(#wn1)"/>
</svg>'''

def monogram(w, gold="#cbb37e"):
    return f'''<svg viewBox="0 0 200 200" style="width:{w}px">
  <circle cx="100" cy="100" r="92" fill="none" stroke="{gold}" stroke-width="1.4"/>
  <circle cx="100" cy="100" r="84" fill="none" stroke="{gold}" stroke-width="0.8" opacity=".7"/>
  <path d="M62 138 V72 L100 118 L138 72 V138" fill="none" stroke="{gold}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

LABELS = {}

# ===== E2 · MAISON NOIR — elevated ritual wording =====
LABELS["moonset-e2"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#0b0d14;color:#e9e2d2;font-family:Jost,sans-serif;position:relative;text-align:center;padding:84px 72px}}
.no{{font-weight:300;font-size:18px;letter-spacing:7px;color:#8d8674}}
.brand{{font-family:'Bodoni Moda';font-weight:500;font-size:100px;letter-spacing:10px;padding-left:10px;line-height:1;color:#efe8d8;margin-top:42px}}
.desc{{font-weight:400;font-size:21px;letter-spacing:10px;color:#cbb37e;margin-top:26px}}
.strip{{margin-top:60px;display:flex;justify-content:center}}
.line{{width:1px;height:70px;background:linear-gradient(180deg,transparent,#cbb37e,transparent);margin:52px auto}}
.ritual{{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:34px;color:#d9d0ba;line-height:1.5}}
.body{{margin-top:40px;font-weight:300;font-size:19px;color:#b6ae9b;line-height:1.9;max-width:520px;margin-left:auto;margin-right:auto}}
.body b{{font-weight:500;color:#e9e2d2}}
.free{{margin-top:52px;font-weight:400;font-size:14.5px;letter-spacing:4px;color:#8d8674}}
.nw{{position:absolute;bottom:66px;left:72px;right:72px;font-weight:300;font-size:16px;letter-spacing:4px;color:#8d8674;display:flex;justify-content:space-between}}
</style></head><body><div class="p">
<div class="no">N&deg; 30 &mdash; NUIT</div>
<div class="brand">MOONSET</div>
<div class="desc">THE NIGHT RITUAL</div>
<div class="strip">{phases(310)}</div>
<div class="line"></div>
<div class="ritual">One cup, as the day ends.<br>Sleep, as it should be.</div>
<div class="body">A velvet evening elixir &mdash; <b>saffron</b>, <b>magnesium glycinate</b>, <b>L&#8209;theanine</b>, <b>glycine</b> &amp; <b>ashwagandha</b> at clinical dose. Nothing to depend on. Everything to return to.</div>
<div class="free">SANS M&Eacute;LATONINE &nbsp;&middot;&nbsp; MELATONIN-FREE &nbsp;&middot;&nbsp; CAFFEINE-FREE</div>
<div class="nw"><span>240 G &mdash; 8.5 OZ</span><span>THIRTY NIGHTS</span></div>
</div></body></html>'''

# ===== G2 · GRAND CRU MINUIT — elevated ritual wording =====
LABELS["moonset-g2"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#101726;color:#ece5d3;font-family:'Cormorant Garamond',serif;position:relative;text-align:center;padding:78px 68px}}
.brand{{font-weight:500;font-size:98px;letter-spacing:9px;padding-left:9px;line-height:1;color:#f0e9d8;margin-top:36px}}
.desc{{font-family:Jost;font-weight:400;font-size:19px;letter-spacing:9px;color:#cbb37e;margin-top:22px}}
.ritual{{font-size:33px;font-style:italic;font-weight:500;color:#c8bfa8;line-height:1.6;margin-top:44px}}
.band{{position:absolute;left:0;right:0;top:812px;background:linear-gradient(180deg,#d6bc82,#b89a58);color:#221c0e;padding:30px 68px}}
.band .t{{font-family:Jost;font-weight:500;font-size:16px;letter-spacing:4px;margin-bottom:8px}}
.band .acts{{font-family:Jost;font-weight:400;font-size:15px;letter-spacing:1.6px;line-height:1.9}}
.vow{{position:absolute;top:1050px;left:68px;right:68px;font-size:24px;font-style:italic;color:#b5ac93}}
.free{{position:absolute;bottom:130px;left:68px;right:68px;font-family:Jost;font-weight:400;font-size:14px;letter-spacing:4px;color:#8f8871}}
.nw{{position:absolute;bottom:64px;left:68px;right:68px;font-family:Jost;font-weight:300;font-size:16px;letter-spacing:4px;color:#cbb37e;display:flex;justify-content:space-between;border-top:1px solid rgba(203,179,126,.35);padding-top:20px}}
</style></head><body><div class="p">
<div style="display:flex;justify-content:center">{monogram(140)}</div>
<div class="brand">MOONSET</div>
<div class="desc">THE NIGHT RITUAL</div>
<div class="ritual">The evening, composed &mdash;<br>a velvet elixir for deep, natural sleep.</div>
<div class="band">
  <div class="t">CLINICALLY-DOSED &middot; FIVE ACTIVES</div>
  <div class="acts">SAFFRON (AFFRON&reg;) 28MG &middot; MAGNESIUM GLYCINATE 300MG<br>L-THEANINE 200MG &middot; GLYCINE 3G &middot; ASHWAGANDHA KSM-66 300MG</div>
</div>
<div class="vow">Taken nightly, thirty minutes before sleep.</div>
<div class="free">MELATONIN-FREE &middot; CAFFEINE-FREE &middot; VEGAN &middot; THIRD-PARTY TESTED</div>
<div class="nw"><span>240 G &mdash; 8.5 OZ</span><span>THIRTY NIGHTS</span></div>
</div></body></html>'''

for n,h in LABELS.items():
    open(os.path.join(OUT,n+".html"),"w").write(h); print("wrote",n)
