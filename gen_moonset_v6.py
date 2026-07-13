#!/usr/bin/env python3
# v6: G3 = FINAL blue Moonset (M^moon monogram, ultra-readable, instantly clear product) + SLEEPMAXING gen-z fun brand.
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,500'
     '&family=Jost:wght@300;400;500;600;700&family=Anton&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">')

# M-in-ring with crescent "exponent" at top-right — the brand icon
def mmark(w, gold="#cbb37e", ink="none"):
    return f'''<svg viewBox="0 0 220 200" style="width:{w}px">
  <circle cx="100" cy="110" r="82" fill="{ink}" stroke="{gold}" stroke-width="2"/>
  <circle cx="100" cy="110" r="74" fill="none" stroke="{gold}" stroke-width="0.9" opacity=".65"/>
  <path d="M68 144 V80 L100 122 L132 80 V144" fill="none" stroke="{gold}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M186 22 a26 26 0 1 0 8 20 a20 20 0 1 1 -8 -20Z" fill="{gold}"/>
</svg>'''

L = {}

# ===== G3 · MOONSET MINUIT FINAL — blue, M^moon, ultra-clear =====
L["moonset-g3"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#101726;color:#f0e9d8;font-family:Jost,sans-serif;position:relative;text-align:center;padding:70px 64px}}
.no{{font-weight:500;font-size:18px;letter-spacing:7px;color:#b3ab97}}
.brand{{font-family:'Cormorant Garamond';font-weight:600;font-size:102px;letter-spacing:9px;padding-left:9px;line-height:1;color:#f6efdf;margin-top:28px}}
.what{{margin-top:20px;font-weight:700;font-size:31px;letter-spacing:6px;color:#e0c88f}}
.ritual{{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:29px;color:#cfc5ac;margin-top:16px}}
.band{{position:absolute;left:0;right:0;top:788px;background:linear-gradient(180deg,#d9c084,#bb9d5a);color:#1c1608;padding:30px 60px}}
.band .t{{font-weight:700;font-size:21px;letter-spacing:4px;margin-bottom:12px}}
.band .r{{display:flex;justify-content:space-between;font-size:21px;font-weight:600;letter-spacing:.5px;padding:7px 4px;border-top:1.2px solid rgba(28,22,8,.22)}}
.band .r:first-of-type{{border-top:none}}
.how{{position:absolute;top:1104px;left:64px;right:64px;font-weight:500;font-size:23px;color:#f0e9d8;line-height:1.6}}
.how b{{color:#e0c88f;font-weight:700}}
.free{{position:absolute;bottom:128px;left:64px;right:64px;font-weight:600;font-size:17px;letter-spacing:3.5px;color:#cfc5ac}}
.nw{{position:absolute;bottom:62px;left:64px;right:64px;font-weight:500;font-size:18px;letter-spacing:3px;color:#e0c88f;display:flex;justify-content:space-between;border-top:1px solid rgba(203,179,126,.4);padding-top:19px}}
</style></head><body><div class="p">
<div style="display:flex;justify-content:center;margin-bottom:6px">{mmark(150)}</div>
<div class="no">N&deg; 30 &mdash; NUIT</div>
<div class="brand">MOONSET</div>
<div class="what">CHOCOLATE SLEEP DRINK</div>
<div class="ritual">The night ritual &mdash; deep, natural sleep.</div>
<div class="band">
  <div class="t">CLINICALLY DOSED &middot; FIVE ACTIVES</div>
  <div class="r"><span>Saffron (affron&reg;)</span><b>28 mg</b></div>
  <div class="r"><span>Magnesium Glycinate</span><b>300 mg</b></div>
  <div class="r"><span>L-Theanine</span><b>200 mg</b></div>
  <div class="r"><span>Glycine &middot; Ashwagandha KSM-66</span><b>3 g &middot; 300 mg</b></div>
</div>
<div class="how">Mix one scoop into <b>warm milk</b>,<br><b>30 minutes before bed.</b></div>
<div class="free">MELATONIN-FREE &middot; CAFFEINE-FREE &middot; VEGAN</div>
<div class="nw"><span>240 G &mdash; 30 SERVINGS</span><span>THIRTY NIGHTS</span></div>
</div></body></html>'''

# ===== SLEEPMAXING · gen-z night stack =====
L["sleepmaxing"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:linear-gradient(165deg,#1b1147 0%,#3a1d8a 45%,#6427c9 78%,#8f3bff 100%);color:#fff;font-family:'Space Grotesk',sans-serif;position:relative;text-align:center;padding:64px 56px;overflow:hidden}}
.zz{{position:absolute;top:40px;right:44px;font-family:Anton;font-size:54px;color:#c8ff3e;transform:rotate(12deg);text-shadow:4px 4px 0 #1b1147}}
.moon{{width:120px;height:120px;margin:0 auto}}
.brand{{font-family:Anton;font-size:128px;line-height:.95;letter-spacing:2px;color:#fff;margin-top:14px;text-shadow:6px 6px 0 #1b1147}}
.brand .lime{{color:#c8ff3e}}
.what{{margin-top:16px;font-weight:700;font-size:30px;letter-spacing:3px;color:#fff;background:#1b1147;display:inline-block;padding:10px 22px;border-radius:14px;transform:rotate(-1.5deg)}}
.tag{{margin-top:22px;font-weight:600;font-size:25px;color:#e9e2ff}}
.stick{{position:relative;margin:34px auto 0;max-width:640px;display:flex;flex-wrap:wrap;gap:12px;justify-content:center}}
.s{{background:#c8ff3e;color:#1b1147;font-weight:700;font-size:19px;padding:11px 18px;border-radius:100px;transform:rotate(-2deg);box-shadow:3px 3px 0 #1b1147}}
.s.alt{{background:#fff;transform:rotate(1.5deg)}}
.stack{{margin:36px auto 0;max-width:620px;background:rgba(15,9,45,.72);border:2.5px solid #c8ff3e;border-radius:22px;padding:24px 28px;text-align:left}}
.stack .t{{font-family:Anton;font-size:26px;letter-spacing:1px;color:#c8ff3e;text-align:center;margin-bottom:12px}}
.stack .r{{display:flex;justify-content:space-between;font-size:21px;font-weight:600;padding:7px 2px;border-top:1px solid rgba(200,255,62,.25)}}
.stack .r:first-of-type{{border-top:none}}
.stack .r b{{color:#c8ff3e}}
.how{{margin-top:30px;font-weight:700;font-size:23px;color:#fff}}
.how .lime{{color:#c8ff3e}}
.nw{{position:absolute;bottom:56px;left:56px;right:56px;display:flex;justify-content:space-between;font-weight:700;font-size:18px;letter-spacing:2px;color:#e9e2ff;border-top:2px solid rgba(233,226,255,.35);padding-top:16px}}
</style></head><body><div class="p">
<div class="zz">ZZZ</div>
<svg class="moon" viewBox="0 0 120 120"><path d="M92 26 a44 44 0 1 0 14 34 a34 34 0 1 1 -14 -34Z" fill="#c8ff3e" stroke="#1b1147" stroke-width="5"/><circle cx="88" cy="30" r="5" fill="#fff"/></svg>
<div class="brand">SLEEP<br><span class="lime">MAXING</span></div>
<div class="what">CHOCOLATE SLEEP DRINK</div>
<div class="tag">max your sleep. wake up different.</div>
<div class="stick">
  <span class="s">0 MELATONIN</span>
  <span class="s alt">0 CAFFEINE</span>
  <span class="s">0 GROGGY MORNINGS</span>
</div>
<div class="stack">
  <div class="t">THE NIGHT STACK — FULL CLINICAL DOSES</div>
  <div class="r"><span>Saffron (affron&reg;)</span><b>28 mg</b></div>
  <div class="r"><span>Magnesium Glycinate</span><b>300 mg</b></div>
  <div class="r"><span>L-Theanine</span><b>200 mg</b></div>
  <div class="r"><span>Glycine</span><b>3 g</b></div>
  <div class="r"><span>Ashwagandha KSM-66</span><b>300 mg</b></div>
</div>
<div class="how">scoop + warm milk + 30 min = <span class="lime">elite sleep, on repeat</span></div>
<div class="nw"><span>240 G &middot; 30 SERVINGS</span><span>CHOC FLAVOR &middot; VEGAN</span></div>
</div></body></html>'''

for n,h in L.items():
    open(os.path.join(OUT,n+".html"),"w").write(h); print("wrote",n)
