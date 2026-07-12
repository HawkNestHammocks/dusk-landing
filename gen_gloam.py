#!/usr/bin/env python3
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700'
     '&family=Inter:wght@400;500;600;700&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">')

# refined premium crescent+star seal (gold on navy)
def seal(size, ring=True):
    r = size/2 - 4
    return f'''<svg viewBox="0 0 {size} {size}">
      {'<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#d9b25f" stroke-width="1.4"/>'%(size/2,size/2,r) if ring else ''}
      {'<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#d9b25f" stroke-width="0.9" opacity=".55"/>'%(size/2,size/2,r-7) if ring else ''}
      <g transform="translate({size/2},{size/2+2})">
        <path d="M {size*0.10},{-size*0.16} a {size*0.19},{size*0.19} 0 1 0 0,{size*0.32} a {size*0.14},{size*0.14} 0 1 1 0,{-size*0.32} Z" fill="#d9b25f"/>
        <path d="M {size*0.16} {-size*0.03} l {size*0.014} {size*0.038} {size*0.04} .003 -{size*0.032} {size*0.026} {size*0.012} {size*0.04} -{size*0.034} -{size*0.024} -{size*0.034} {size*0.024} {size*0.012} -{size*0.04} -{size*0.032} -{size*0.026} {size*0.04} -.003 Z" fill="#f2eddd"/>
      </g></svg>'''

# ---------- FRONT LABEL (for tin wrap) ----------
LABEL = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#0f1430;color:#f2eddd;padding:70px 62px;font-family:Inter,sans-serif;position:relative}}
.top{{display:flex;align-items:center;gap:20px;margin-bottom:44px}}
.top svg{{width:82px;height:82px;flex:0 0 82px}}
.tt{{font-family:Oswald;font-size:15px;letter-spacing:4px;color:#d9b25f;line-height:1.45}}
.brand{{font-family:Fraunces;font-weight:600;font-size:150px;letter-spacing:4px;line-height:.82;color:#f6f1e2}}
.desc{{font-family:Oswald;font-weight:500;font-size:30px;letter-spacing:11px;color:#d9b25f;margin:18px 0 8px}}
.sub{{font-size:20px;color:#b9bcd4;font-weight:400;margin-bottom:34px}}
.bens{{display:flex;gap:10px;margin-bottom:34px}}
.b{{border:1.4px solid #d9b25f;color:#d9b25f;border-radius:6px;padding:11px 15px;font-size:14px;font-weight:700;letter-spacing:1px}}
.b.f{{background:#d9b25f;color:#0f1430}}
.ah{{font-family:Oswald;letter-spacing:3px;font-size:15px;color:#8f93b5;margin-bottom:4px;border-top:1px solid rgba(217,178,95,.3);padding-top:22px}}
.ar{{display:flex;justify-content:space-between;padding:13px 4px;font-size:22px;border-bottom:1px solid rgba(255,255,255,.09)}}
.ar b{{font-weight:500;color:#f2eddd}} .ar i{{font-style:normal;font-family:Oswald;color:#d9b25f;font-weight:600}}
.dir{{font-size:18px;color:#c9cbdf;margin-top:30px;line-height:1.55}} .dir b{{color:#f6f1e2}}
.nw{{position:absolute;bottom:60px;left:62px;right:62px;display:flex;justify-content:space-between;font-family:Oswald;
font-size:20px;letter-spacing:2px;color:#d9b25f;border-top:1px solid rgba(217,178,95,.3);padding-top:20px}}
</style></head><body><div class="p">
<div class="top">{seal(82)}<div class="tt">NIGHTLY<br>WIND-DOWN<br>RITUAL</div></div>
<div class="brand">GLOAM</div><div class="desc">WIND-DOWN COCOA</div>
<div class="sub">Melatonin-free evening cocoa for deeper, natural sleep</div>
<div class="bens"><span class="b f">MELATONIN-FREE</span><span class="b f">CAFFEINE-FREE</span><span class="b">VEGAN</span></div>
<div class="ah">CLINICALLY-DOSED ACTIVES · PER SERVING</div>
<div class="ar"><b>Magnesium Glycinate</b><i>300mg</i></div>
<div class="ar"><b>L-Theanine</b><i>200mg</i></div>
<div class="ar"><b>Glycine</b><i>3g</i></div>
<div class="ar"><b>Ashwagandha KSM-66</b><i>300mg</i></div>
<div class="ar"><b>Saffron (affron)</b><i>28mg</i></div>
<div class="dir">Stir one scoop into 8oz <b>warm or cold milk</b>, 30 min before bed.</div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span>30 SERVINGS</span></div>
</div></body></html>'''

# ---------- LOGO LOCKUP (brand presentation) ----------
LOGO = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:1200px;height:800px;background:radial-gradient(120% 100% at 50% 0%,#1a2150,#0d1230 65%);color:#f2eddd;
font-family:Inter,sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.seal{{width:150px;height:150px;margin-bottom:30px}}
.brand{{font-family:Fraunces;font-weight:600;font-size:130px;letter-spacing:14px;padding-left:14px;color:#f6f1e2;line-height:1}}
.rule{{width:220px;height:1px;background:linear-gradient(90deg,transparent,#d9b25f,transparent);margin:26px 0 20px}}
.tag{{font-family:Oswald;font-weight:500;font-size:24px;letter-spacing:11px;color:#d9b25f}}
.foot{{position:absolute;bottom:44px;font-size:14px;letter-spacing:3px;color:#8f93b5;font-family:Oswald}}
</style></head><body><div class="p">
<div class="seal">{seal(150)}</div>
<div class="brand">GLOAM</div>
<div class="rule"></div>
<div class="tag">WIND-DOWN COCOA</div>
<div class="foot">MELATONIN-FREE · THE NIGHTLY RITUAL</div>
</div></body></html>'''

open(os.path.join(OUT,"gloam_label.html"),"w").write(LABEL)
open(os.path.join(OUT,"gloam_logo.html"),"w").write(LOGO)
print("wrote gloam_label.html, gloam_logo.html")
