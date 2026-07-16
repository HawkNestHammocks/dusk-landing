#!/usr/bin/env python3
# MOONSET launch ads — 5 creatives, 1080x1350 (4:5 feed). Premium navy/gold, real product renders.
import os
OUT = os.path.dirname(os.path.abspath(__file__))
F = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500'
     '&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">')

BASE = """*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}
body{width:1080px;height:1350px;overflow:hidden;font-family:Jost,sans-serif;position:relative;color:#f2eddd}
.serif{font-family:'Fraunces',serif}
.offer{position:absolute;bottom:44px;left:50%;transform:translateX(-50%);width:960px;background:linear-gradient(180deg,#1b2350ee,#0d1230f5);border:1.5px solid #d9b25f;border-radius:24px;padding:24px 36px;display:flex;align-items:center;justify-content:space-between;gap:20px;box-shadow:0 30px 60px rgba(0,0,0,.5)}
.offer .left{display:flex;flex-direction:column;gap:6px}
.offer .tag{font-weight:700;font-size:17px;letter-spacing:2.5px;color:#d9b25f}
.offer .big{font-family:'Fraunces';font-weight:600;font-size:46px;line-height:1;color:#f2eddd}
.offer .big small{font-size:22px;color:#8f95bb;text-decoration:line-through;font-weight:400;margin-left:10px}
.offer .sub{font-size:15.5px;color:#b9bcd6}
.cta{background:linear-gradient(180deg,#e8c983,#c99a3f);color:#0d1230;font-weight:700;font-size:21px;padding:18px 34px;border-radius:60px;white-space:nowrap;box-shadow:0 10px 24px rgba(217,178,95,.4)}"""

def offer_card(cta="Claim 30% Off"):
    return f'''<div class="offer">
  <div class="left">
    <div class="tag">☾ FOUNDING BATCH №1 — 92% CLAIMED</div>
    <div class="big">$41.30 <small>$59</small></div>
    <div class="sub">Free US shipping · taxes included · 30-night guarantee</div>
  </div>
  <div class="cta">{cta} →</div>
</div>'''

A = {}

# M1 · HERO — premium product + offer
A["ms-ad1"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:radial-gradient(130% 90% at 50% 0%,#1c2454 0%,#0d1230 62%)}}
.top{{position:absolute;top:64px;left:0;right:0;text-align:center}}
.kick{{font-weight:600;font-size:19px;letter-spacing:6px;color:#d9b25f}}
h1{{font-family:'Fraunces';font-weight:600;font-size:78px;line-height:1.08;margin-top:16px}}
h1 em{{font-style:italic;color:#d9b25f}}
.tin{{position:absolute;top:320px;left:50%;transform:translateX(-50%);width:640px;border-radius:24px;box-shadow:0 50px 100px rgba(0,0,0,.6)}}
.glow{{position:absolute;top:300px;left:50%;transform:translateX(-50%);width:820px;height:820px;background:radial-gradient(circle,rgba(217,178,95,.22),transparent 65%)}}
</style></head><body>
<div class="glow"></div>
<div class="top">
  <div class="kick">MELATONIN-FREE · CLINICALLY DOSED</div>
  <h1>Your mornings have coffee.<br>Your nights deserve <em>Moonset.</em></h1>
</div>
<img class="tin" src="../images/moonset-g5-tin3.png">
{offer_card()}
</body></html>'''

# M2 · VS — melatonin gummies comparison
A["ms-ad2"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:linear-gradient(180deg,#0d1230,#141a3c)}}
.top{{position:absolute;top:58px;left:0;right:0;text-align:center}}
h1{{font-family:'Fraunces';font-weight:600;font-size:66px;line-height:1.1}}
h1 em{{font-style:italic;color:#d9b25f}}
.cols{{position:absolute;top:245px;left:60px;right:60px;display:flex;gap:24px}}
.col{{flex:1;border-radius:22px;padding:32px 32px}}
.col h3{{font-family:'Fraunces';font-size:33px;margin-bottom:18px}}
.col.bad{{background:rgba(201,139,122,.08);border:1.5px solid rgba(201,139,122,.4)}}
.col.good{{background:rgba(217,178,95,.1);border:1.5px solid #d9b25f}}
.col li{{list-style:none;font-size:23.5px;padding:15px 0 15px 42px;position:relative;color:#cfd0e0;border-bottom:1px solid rgba(255,255,255,.07);line-height:1.3}}
.col.bad li::before{{content:"✕";position:absolute;left:4px;color:#c98b7a;font-weight:700}}
.col.good li::before{{content:"✓";position:absolute;left:4px;color:#d9b25f;font-weight:700}}
.col.good li{{color:#f2eddd}}
.tin{{position:absolute;bottom:135px;left:50%;transform:translateX(-50%);width:360px;filter:drop-shadow(0 30px 60px rgba(0,0,0,.6));border-radius:18px}}
.mid{{position:absolute;top:648px;left:0;right:0;text-align:center;font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:40px;color:#e8c983}}
</style></head><body>
<div class="top"><h1>Melatonin knocks you out.<br><em>Moonset lets you drift.</em></h1></div>
<div class="mid">Fall asleep naturally. Wake up clear.</div>
<div class="cols">
  <div class="col bad"><h3>Melatonin gummies</h3>
    <li>A hormone, dosed like candy</li><li>Groggy "hungover" mornings</li><li>Body builds tolerance</li><li>Forces sleep</li></div>
  <div class="col good"><h3>The Moonset ritual</h3>
    <li>Nutrients your body already uses</li><li>Wake up clear</li><li>Nothing to depend on</li><li>Builds real wind-down habit</li></div>
</div>
<img class="tin" src="../images/moonset-g5-tin3.png">
{offer_card("Try It Tonight")}
</body></html>'''

# M3 · LIFESTYLE — nightstand full-bleed
A["ms-ad3"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,26,.62) 0%,transparent 40%,rgba(8,10,26,.8) 100%)}}
.top{{position:absolute;top:70px;left:70px;right:70px;text-align:center}}
h1{{font-family:'Fraunces';font-weight:600;font-size:74px;line-height:1.1;text-shadow:0 4px 30px rgba(0,0,0,.6)}}
h1 em{{font-style:italic;color:#e8c983}}
.sub{{margin-top:18px;font-size:26px;color:#e6e2d2;font-weight:500;text-shadow:0 2px 14px rgba(0,0,0,.7)}}
</style></head><body>
<img class="bg" src="../images/moonset-g5-night.png">
<div class="shade"></div>
<div class="top">
  <h1>One warm cup.<br><em>Thirty minutes later, gone.</em></h1>
  <div class="sub">Saffron · magnesium · L-theanine · glycine · ashwagandha</div>
</div>
{offer_card("Begin the Ritual")}
</body></html>'''

# M4 · TRANSPARENCY — doses disclosed
A["ms-ad4"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:radial-gradient(130% 90% at 50% 0%,#171f4a 0%,#0d1230 60%)}}
.top{{position:absolute;top:60px;left:0;right:0;text-align:center}}
h1{{font-family:'Fraunces';font-weight:600;font-size:70px;line-height:1.08}}
h1 em{{font-style:italic;color:#d9b25f}}
.panel{{position:absolute;top:290px;left:90px;width:580px;background:#fdfcf8;border-radius:14px;padding:34px 36px;color:#111;box-shadow:0 40px 80px rgba(0,0,0,.5)}}
.panel .t{{font-weight:700;font-size:30px;border-bottom:8px solid #000;padding-bottom:8px;margin-bottom:10px;font-family:Jost}}
.r{{display:flex;justify-content:space-between;font-size:24px;padding:14px 0;border-bottom:1px solid #000;font-weight:500}}
.r b{{font-weight:700}}
.foot{{font-size:15px;color:#444;padding-top:10px}}
.tin{{position:absolute;top:400px;right:48px;width:390px;filter:drop-shadow(0 40px 70px rgba(0,0,0,.6));border-radius:18px}}
.badges{{position:absolute;top:1010px;left:0;right:0;display:flex;justify-content:center;gap:16px}}
.bdg{{border:1.4px solid #d9b25f;border-radius:100px;padding:12px 26px;font-weight:600;font-size:18px;letter-spacing:2.5px;color:#e8c983}}
</style></head><body>
<div class="top"><h1>No proprietary blends.<br><em>Every dose disclosed.</em></h1></div>
<div class="badges"><span class="bdg">MELATONIN-FREE</span><span class="bdg">VEGAN · NON-GMO</span><span class="bdg">🇺🇸 MADE IN USA</span></div>
<div class="panel">
  <div class="t">In every scoop</div>
  <div class="r"><span>Saffron (affron®)</span><b>28 mg</b></div>
  <div class="r"><span>Magnesium Glycinate</span><b>300 mg</b></div>
  <div class="r"><span>L-Theanine</span><b>200 mg</b></div>
  <div class="r"><span>Glycine</span><b>3 g</b></div>
  <div class="r"><span>Ashwagandha KSM-66®</span><b>300 mg</b></div>
  <div class="foot">The exact doses from the clinical studies. Zero melatonin.</div>
</div>
<img class="tin" src="../images/moonset-g5-tin3.png">
{offer_card("See the Science")}
</body></html>'''

# M5 · TESTIMONIAL
A["ms-ad5"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:linear-gradient(165deg,#101726,#1b2350 70%,#101726)}}
.q{{position:absolute;top:120px;left:90px;right:90px;text-align:center}}
.stars{{color:#d9b25f;font-size:38px;letter-spacing:8px;margin-bottom:30px}}
blockquote{{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:62px;line-height:1.25;color:#f2eddd}}
.who{{margin-top:26px;font-size:23px;color:#b9bcd6;font-weight:500;letter-spacing:1px}}
.tin{{position:absolute;bottom:200px;left:50%;transform:translateX(-50%);width:420px;filter:drop-shadow(0 40px 80px rgba(0,0,0,.6));border-radius:20px}}
.glow{{position:absolute;bottom:100px;left:50%;transform:translateX(-50%);width:700px;height:500px;background:radial-gradient(circle,rgba(217,178,95,.18),transparent 65%)}}
</style></head><body>
<div class="q">
  <div class="stars">★★★★★</div>
  <blockquote>"I quit melatonin cold turkey. This is the first thing that actually made my brain go quiet at night."</blockquote>
  <div class="who">— MARCUS T. · EARLY TESTER</div>
</div>
<div class="glow"></div>
<img class="tin" src="../images/moonset-g5-tin3.png">
{offer_card()}
</body></html>'''

for n, h in A.items():
    open(os.path.join(OUT, n + ".html"), "w").write(h)
    print("wrote", n)
