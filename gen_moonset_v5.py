#!/usr/bin/env python3
# MOONSET v5 — three MORE black-scheme rectangular-tin designs. Readable type, "clinically dosed" prominent.
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500;6..96,600'
     '&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,500'
     '&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">')

def phases(w, gold="#d2ba85"):
    return f'''<svg viewBox="0 0 300 44" style="width:{w}px">
  <defs>
    <mask id="wxA"><rect width="300" height="44" fill="black"/><circle cx="30" cy="22" r="13" fill="white"/><circle cx="21" cy="22" r="13" fill="black"/></mask>
    <mask id="wxB"><rect width="300" height="44" fill="black"/><circle cx="90" cy="22" r="13" fill="white"/><rect x="77" y="9" width="13" height="26" fill="black"/></mask>
    <mask id="wnB"><rect width="300" height="44" fill="black"/><circle cx="210" cy="22" r="13" fill="white"/><rect x="210" y="9" width="13" height="26" fill="black"/></mask>
    <mask id="wnA"><rect width="300" height="44" fill="black"/><circle cx="270" cy="22" r="13" fill="white"/><circle cx="279" cy="22" r="13" fill="black"/></mask>
  </defs>
  <circle cx="30" cy="22" r="13" fill="{gold}" mask="url(#wxA)"/>
  <circle cx="90" cy="22" r="13" fill="{gold}" mask="url(#wxB)"/>
  <circle cx="150" cy="22" r="14.5" fill="{gold}"/>
  <circle cx="210" cy="22" r="13" fill="{gold}" mask="url(#wnB)"/>
  <circle cx="270" cy="22" r="13" fill="{gold}" mask="url(#wnA)"/>
</svg>'''

ACT = [("Saffron (affron®)","28 mg"),("Magnesium Glycinate","300 mg"),("L-Theanine","200 mg"),
       ("Glycine","3 g"),("Ashwagandha KSM-66","300 mg")]

L = {}

# ===== H · NOIR BAND — black + gold CLINICALLY DOSED band (the E×G combo) =====
L["moonset-h"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#0b0d14;color:#ede6d6;font-family:Jost,sans-serif;position:relative;text-align:center;padding:76px 66px}}
.no{{font-weight:400;font-size:19px;letter-spacing:7px;color:#9a9280}}
.brand{{font-family:'Bodoni Moda';font-weight:500;font-size:102px;letter-spacing:9px;padding-left:9px;line-height:1;color:#f2ebdb;margin-top:36px}}
.desc{{font-weight:500;font-size:22px;letter-spacing:10px;color:#d2ba85;margin-top:24px}}
.strip{{margin-top:48px;display:flex;justify-content:center}}
.vow{{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:34px;color:#ddd4bd;line-height:1.55;margin-top:46px}}
.band{{position:absolute;left:0;right:0;top:868px;background:linear-gradient(180deg,#d6bc82,#b89a58);color:#1c1608;padding:34px 64px}}
.band .t{{font-weight:600;font-size:19px;letter-spacing:4px;margin-bottom:12px}}
.band .r{{display:flex;justify-content:space-between;font-size:19px;font-weight:500;letter-spacing:.8px;padding:6px 0;border-top:1px solid rgba(28,22,8,.18)}}
.band .r:first-of-type{{border-top:none}}
.free{{position:absolute;bottom:132px;left:66px;right:66px;font-weight:500;font-size:16px;letter-spacing:4px;color:#9a9280}}
.nw{{position:absolute;bottom:66px;left:66px;right:66px;font-weight:400;font-size:17px;letter-spacing:4px;color:#d2ba85;display:flex;justify-content:space-between;border-top:1px solid rgba(210,186,133,.35);padding-top:20px}}
</style></head><body><div class="p">
<div class="no">N&deg; 30 &mdash; NUIT</div>
<div class="brand">MOONSET</div>
<div class="desc">THE NIGHT RITUAL</div>
<div class="strip">{phases(300)}</div>
<div class="vow">One cup, as the day ends.<br>Sleep, as it should be.</div>
<div class="band">
  <div class="t">CLINICALLY DOSED &middot; FIVE ACTIVES</div>
  <div class="r"><span>Saffron (affron&reg;)</span><b>28 mg</b></div>
  <div class="r"><span>Magnesium Glycinate</span><b>300 mg</b></div>
  <div class="r"><span>L-Theanine &middot; Glycine &middot; Ashwagandha</span><b>200 mg &middot; 3 g &middot; 300 mg</b></div>
</div>
<div class="free">MELATONIN-FREE &middot; CAFFEINE-FREE &middot; VEGAN</div>
<div class="nw"><span>240 G &mdash; 8.5 OZ</span><span>THIRTY NIGHTS</span></div>
</div></body></html>'''

# ===== I · NOIR FRAME — double gold frame, apothecary list, large readable rows =====
L["moonset-i"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#0c0e15;color:#ede6d6;font-family:Jost,sans-serif;position:relative;text-align:center;padding:96px 84px}}
.p::before{{content:"";position:absolute;inset:30px;border:1.6px solid #cbb37e;border-radius:4px}}
.p::after{{content:"";position:absolute;inset:42px;border:.8px solid rgba(203,179,126,.55);border-radius:2px}}
.no{{font-weight:400;font-size:18px;letter-spacing:7px;color:#9a9280}}
.brand{{font-family:'Cormorant Garamond';font-weight:600;font-size:104px;letter-spacing:8px;padding-left:8px;line-height:1;color:#f2ebdb;margin-top:30px}}
.desc{{font-weight:500;font-size:21px;letter-spacing:10px;color:#d2ba85;margin-top:20px}}
.rule{{width:70px;height:1.5px;background:#cbb37e;margin:42px auto}}
.ct{{font-weight:600;font-size:20px;letter-spacing:5px;color:#d2ba85;margin-bottom:20px}}
.row{{display:flex;justify-content:space-between;align-items:baseline;padding:15px 8px;border-bottom:1px solid rgba(210,186,133,.25);font-size:23px}}
.row span{{color:#ede6d6;font-weight:400;letter-spacing:.5px}}
.row b{{color:#d2ba85;font-weight:600;font-family:'Cormorant Garamond';font-size:26px}}
.vow{{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:30px;color:#c9c0a9;margin-top:44px;line-height:1.55}}
.strip{{position:absolute;bottom:170px;left:0;right:0;display:flex;justify-content:center}}
.nw{{position:absolute;bottom:78px;left:84px;right:84px;font-weight:400;font-size:16.5px;letter-spacing:4px;color:#9a9280;display:flex;justify-content:space-between}}
</style></head><body><div class="p">
<div class="no">N&deg; 30 &mdash; NUIT</div>
<div class="brand">MOONSET</div>
<div class="desc">THE NIGHT RITUAL</div>
<div class="rule"></div>
<div class="ct">CLINICALLY DOSED &middot; FIVE ACTIVES</div>
<div class="row"><span>Saffron (affron&reg;)</span><b>28 mg</b></div>
<div class="row"><span>Magnesium Glycinate</span><b>300 mg</b></div>
<div class="row"><span>L-Theanine</span><b>200 mg</b></div>
<div class="row"><span>Glycine</span><b>3 g</b></div>
<div class="row"><span>Ashwagandha KSM-66</span><b>300 mg</b></div>
<div class="vow">Nothing to depend on.<br>Everything to return to.</div>
<div class="strip">{phases(260)}</div>
<div class="nw"><span>240 G &mdash; 8.5 OZ</span><span>MELATONIN-FREE &middot; THIRTY NIGHTS</span></div>
</div></body></html>'''

# ===== J · NOIR ECLIPSE — huge gold full moon behind wordmark, bold minimal, plaque =====
L["moonset-j"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#0a0c12;color:#ede6d6;font-family:Jost,sans-serif;position:relative;text-align:center;padding:70px 64px;overflow:hidden}}
.moonbg{{position:absolute;top:150px;left:50%;transform:translateX(-50%);width:520px;height:520px;border-radius:50%;
background:radial-gradient(circle at 38% 32%,#e8cf96,#c2a25c 60%,#9c7d3e);opacity:.92}}
.hor{{position:absolute;top:670px;left:0;right:0;height:210px;background:#0a0c12}}
.content{{position:relative;z-index:2}}
.no{{font-weight:400;font-size:18px;letter-spacing:7px;color:#9a9280}}
.brand{{font-family:'Bodoni Moda';font-weight:500;font-size:112px;letter-spacing:8px;padding-left:8px;line-height:1;color:#0d0f16;margin-top:210px}}
.desc{{font-weight:600;font-size:22px;letter-spacing:11px;color:#0d0f16;margin-top:10px}}
.vow{{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:33px;color:#ddd4bd;line-height:1.55;margin-top:170px}}
.plaque{{margin:52px auto 0;max-width:600px;border:1.4px solid #cbb37e;border-radius:6px;padding:26px 30px}}
.plaque .t{{font-weight:600;font-size:18px;letter-spacing:4px;color:#d2ba85;margin-bottom:14px}}
.plaque .a{{font-weight:400;font-size:19.5px;letter-spacing:1.2px;color:#ede6d6;line-height:2}}
.plaque .a b{{color:#d2ba85;font-weight:600}}
.nw{{position:absolute;bottom:64px;left:64px;right:64px;font-weight:400;font-size:16.5px;letter-spacing:4px;color:#9a9280;display:flex;justify-content:space-between;border-top:1px solid rgba(210,186,133,.3);padding-top:18px}}
</style></head><body><div class="p">
<div class="moonbg"></div><div class="hor"></div>
<div class="content">
<div class="no">N&deg; 30 &mdash; NUIT</div>
<div class="brand">MOONSET</div>
<div class="desc">THE NIGHT RITUAL</div>
<div class="vow">The moon goes down.<br>So do you.</div>
<div class="plaque">
  <div class="t">CLINICALLY DOSED &middot; FIVE ACTIVES</div>
  <div class="a">Saffron <b>28mg</b> &middot; Magnesium Glycinate <b>300mg</b> &middot; L-Theanine <b>200mg</b><br>Glycine <b>3g</b> &middot; Ashwagandha KSM-66 <b>300mg</b></div>
</div>
</div>
<div class="nw"><span>240 G &mdash; 8.5 OZ</span><span>MELATONIN-FREE &middot; THIRTY NIGHTS</span></div>
</div></body></html>'''

for n,h in L.items():
    open(os.path.join(OUT,n+".html"),"w").write(h); print("wrote",n)
