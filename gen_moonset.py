#!/usr/bin/env python3
# MOONSET brand assets — logo lockup + tin front label (Nocturne navy/gold, Fraunces).
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700'
     '&family=Inter:wght@400;500;600;700&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">')

# ---- THE MARK: gold moon half-set behind a horizon line, shimmering reflection below ----
def mark(w):
    return f'''<svg viewBox="0 0 200 200" style="width:{w}px;height:{w}px">
  <defs>
    <clipPath id="above"><rect x="0" y="0" width="200" height="104"/></clipPath>
    <linearGradient id="gld" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#eccb7f"/><stop offset="1" stop-color="#c99b3f"/>
    </linearGradient>
  </defs>
  <!-- setting moon (top half only) -->
  <g clip-path="url(#above)">
    <circle cx="100" cy="104" r="46" fill="url(#gld)"/>
  </g>
  <!-- horizon -->
  <line x1="22" y1="104" x2="178" y2="104" stroke="#d9b25f" stroke-width="4" stroke-linecap="round"/>
  <!-- reflection ripples, fading -->
  <line x1="64" y1="124" x2="136" y2="124" stroke="#d9b25f" stroke-width="3.4" stroke-linecap="round" opacity=".55"/>
  <line x1="78" y1="142" x2="122" y2="142" stroke="#d9b25f" stroke-width="3" stroke-linecap="round" opacity=".32"/>
  <line x1="90" y1="158" x2="110" y2="158" stroke="#d9b25f" stroke-width="2.6" stroke-linecap="round" opacity=".18"/>
  <!-- two tiny stars above -->
  <path d="M56 44 l1.7 4.6 4.9.3 -3.9 3 1.4 4.7 -4.1-2.8 -4.1 2.8 1.4-4.7 -3.9-3 4.9-.3Z" fill="#f2eddd" opacity=".9"/>
  <circle cx="146" cy="58" r="3" fill="#f2eddd" opacity=".75"/>
</svg>'''

LOGO = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:1200px;height:800px;background:radial-gradient(120% 100% at 50% 0%,#1a2150,#0d1230 65%);color:#f2eddd;
font-family:Inter,sans-serif;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;position:relative}}
.brand{{font-family:Fraunces;font-weight:600;font-size:118px;letter-spacing:16px;padding-left:16px;color:#f6f1e2;line-height:1;margin-top:10px}}
.rule{{width:230px;height:1px;background:linear-gradient(90deg,transparent,#d9b25f,transparent);margin:26px 0 20px}}
.tag{{font-family:Oswald;font-weight:500;font-size:23px;letter-spacing:11px;color:#d9b25f}}
.foot{{position:absolute;bottom:42px;font-size:14px;letter-spacing:3px;color:#8f93b5;font-family:Oswald}}
</style></head><body><div class="p">
{mark(190)}
<div class="brand">MOONSET</div>
<div class="rule"></div>
<div class="tag">WIND-DOWN COCOA</div>
<div class="foot">MELATONIN-FREE · THE NIGHTLY RITUAL</div>
</div></body></html>'''

LABEL = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#0f1430;color:#f2eddd;padding:64px 62px;font-family:Inter,sans-serif;position:relative;text-align:center}}
.brand{{font-family:Fraunces;font-weight:600;font-size:108px;letter-spacing:7px;line-height:.9;color:#f6f1e2;margin-top:18px}}
.desc{{font-family:Oswald;font-weight:500;font-size:29px;letter-spacing:11px;color:#d9b25f;margin:18px 0 8px}}
.sub{{font-size:20px;color:#b9bcd4;font-weight:400;margin-bottom:30px}}
.bens{{display:flex;gap:10px;margin-bottom:30px;justify-content:center}}
.b{{border:1.4px solid #d9b25f;color:#d9b25f;border-radius:6px;padding:11px 15px;font-size:14px;font-weight:700;letter-spacing:1px}}
.b.f{{background:#d9b25f;color:#0f1430}}
.ah{{font-family:Oswald;letter-spacing:3px;font-size:15px;color:#8f93b5;margin-bottom:4px;border-top:1px solid rgba(217,178,95,.3);padding-top:22px}}
.ar{{display:flex;justify-content:space-between;padding:13px 6px;font-size:22px;border-bottom:1px solid rgba(255,255,255,.09);text-align:left}}
.ar b{{font-weight:500;color:#f2eddd}} .ar i{{font-style:normal;font-family:Oswald;color:#d9b25f;font-weight:600}}
.dir{{font-size:18px;color:#c9cbdf;margin-top:28px;line-height:1.55}} .dir b{{color:#f6f1e2}}
.nw{{position:absolute;bottom:58px;left:62px;right:62px;display:flex;justify-content:space-between;font-family:Oswald;
font-size:20px;letter-spacing:2px;color:#d9b25f;border-top:1px solid rgba(217,178,95,.3);padding-top:20px}}
</style></head><body><div class="p">
<div style="display:flex;justify-content:center">{mark(150)}</div>
<div class="brand">MOONSET</div><div class="desc">WIND-DOWN COCOA</div>
<div class="sub">Melatonin-free evening cocoa for deeper, natural sleep</div>
<div class="bens"><span class="b f">MELATONIN-FREE</span><span class="b f">CAFFEINE-FREE</span><span class="b">VEGAN</span></div>
<div class="ah">CLINICALLY-DOSED ACTIVES · PER SERVING</div>
<div class="ar"><b>Magnesium Glycinate</b><i>300mg</i></div>
<div class="ar"><b>L-Theanine</b><i>200mg</i></div>
<div class="ar"><b>Glycine</b><i>3g</i></div>
<div class="ar"><b>Ashwagandha KSM-66</b><i>300mg</i></div>
<div class="ar"><b>Saffron (affron)</b><i>28mg</i></div>
<div class="dir">Stir one scoop into 8oz <b>warm or cold milk</b>,<br>30 minutes before bed.</div>
<div class="nw"><span>NET WT 240g (8.5 OZ)</span><span>30 SERVINGS</span></div>
</div></body></html>'''

open(os.path.join(OUT,"moonset_logo.html"),"w").write(LOGO)
open(os.path.join(OUT,"moonset_label.html"),"w").write(LABEL)
print("wrote moonset_logo.html, moonset_label.html")
