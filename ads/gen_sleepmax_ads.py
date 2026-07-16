#!/usr/bin/env python3
# SLEEP MAXING launch ads — 5 creatives, 1080x1350. Neon vapor gen-z, real product renders.
import os
OUT = os.path.dirname(os.path.abspath(__file__))
F = ('<link href="https://fonts.googleapis.com/css2?family=Anton&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">')

BASE = """*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}
body{width:1080px;height:1350px;overflow:hidden;font-family:'Space Grotesk',sans-serif;position:relative;color:#fff}
.anton{font-family:Anton,sans-serif;font-weight:400;text-transform:uppercase}
.offer{position:absolute;bottom:44px;left:50%;transform:translateX(-50%);width:960px;background:rgba(14,16,51,.92);border:2.5px solid #7de8ff;border-radius:22px;padding:22px 34px;display:flex;align-items:center;justify-content:space-between;gap:20px;box-shadow:8px 8px 0 rgba(14,16,51,.6)}
.offer .left{display:flex;flex-direction:column;gap:5px}
.offer .tag{font-weight:700;font-size:16px;letter-spacing:2px;color:#ffd76e}
.offer .big{font-family:Anton;font-size:52px;line-height:1;color:#fff}
.offer .big small{font-size:24px;color:#8f89b8;text-decoration:line-through;font-family:'Space Grotesk';font-weight:600;margin-left:10px}
.offer .sub{font-size:15px;color:#cfc7ee;font-weight:600}
.cta{background:#c8ff3e;color:#0e1033;font-weight:700;font-size:22px;padding:18px 32px;border-radius:14px;white-space:nowrap;box-shadow:4px 4px 0 rgba(14,16,51,.8)}
.grad{background:linear-gradient(165deg,#1b1147 0%,#3a1d8a 45%,#6427c9 78%,#8f3bff 100%)}"""

def offer_card(cta="MAX MY SLEEP"):
    return f'''<div class="offer">
  <div class="left">
    <div class="tag">😴 FOUNDING DROP — 92% CLAIMED · 37 LEFT</div>
    <div class="big">$41.30 <small>$59</small></div>
    <div class="sub">0 melatonin · 0 caffeine · 0 groggy mornings · free US shipping</div>
  </div>
  <div class="cta">{cta} →</div>
</div>'''

A = {}

# S1 · HERO
A["sm-ad1"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:linear-gradient(165deg,#1b1147 0%,#3a1d8a 45%,#6427c9 78%,#8f3bff 100%)}}
.zz{{position:absolute;top:44px;right:56px;font-family:Anton;font-size:64px;color:#7de8ff;transform:rotate(12deg);text-shadow:5px 5px 0 #1b1147}}
.top{{position:absolute;top:70px;left:0;right:0;text-align:center}}
h1{{font-family:Anton;font-size:118px;line-height:.98;text-shadow:6px 6px 0 rgba(14,16,51,.85)}}
h1 .c{{color:#7de8ff}}
.sub{{margin-top:18px;font-size:29px;font-weight:600;color:#f2e9ff}}
.sub b{{color:#ffd76e}}
.tin{{position:absolute;top:390px;left:50%;transform:translateX(-50%);width:660px;border-radius:24px;box-shadow:0 50px 100px rgba(0,0,0,.55);border:3px solid rgba(255,255,255,.2)}}
</style></head><body>
<div class="zz">ZZZ</div>
<div class="top">
  <h1>MAX YOUR SLEEP.<br><span class="c">WAKE UP DIFFERENT.</span></h1>
  <div class="sub">The nightly sleep drink that <b>tastes like chocolate</b> and works like science.</div>
</div>
<img class="tin" src="../images/sleepmaxing-c-hero2.png">
{offer_card()}
</body></html>'''

# S2 · SLEEP SCORE
A["sm-ad2"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:#0e1033}}
.top{{position:absolute;top:66px;left:0;right:0;text-align:center;padding:0 70px}}
h1{{font-family:Anton;font-size:88px;line-height:1.02;text-shadow:5px 5px 0 rgba(125,232,255,.25)}}
h1 .c{{color:#7de8ff}}
.ringwrap{{position:absolute;top:360px;left:120px;width:420px}}
.ring{{width:100%;filter:drop-shadow(0 0 40px rgba(125,232,255,.45))}}
.ringnum{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}}
.ringnum span{{font-family:Anton;font-size:130px;color:#fff;line-height:1;text-shadow:0 0 40px rgba(125,232,255,.6)}}
.ringnum small{{font-size:22px;letter-spacing:5px;color:#7de8ff;font-weight:700;margin-top:6px}}
.right{{position:absolute;top:400px;right:90px;width:400px}}
.was{{font-size:26px;color:#8f89b8;font-weight:600}}
.was b{{font-size:56px;color:#8f89b8;font-family:Anton;text-decoration:line-through}}
.arrow{{font-family:Anton;font-size:60px;color:#ffd76e;margin:10px 0}}
.now{{font-size:26px;color:#f2e9ff;font-weight:600}}
.now b{{font-size:100px;color:#c8ff3e;font-family:Anton;text-shadow:0 0 30px rgba(200,255,62,.5)}}
.cap{{position:absolute;top:880px;left:0;right:0;text-align:center;font-size:24px;color:#cfc7ee;font-weight:600}}
.cap b{{color:#ffd76e}}
.chips{{position:absolute;top:955px;left:70px;right:70px;display:flex;gap:18px}}
.chip{{flex:1;background:rgba(255,255,255,.06);border:2px solid rgba(255,158,207,.4);border-radius:18px;padding:18px 10px;text-align:center}}
.chip b{{display:block;font-family:Anton;font-size:44px;color:#ffd76e;line-height:1.05}}
.chip span{{font-size:16.5px;color:#cfc7ee;font-weight:600}}
</style></head><body>
<div class="top"><h1>YOUR SLEEP SCORE<br><span class="c">CALLED. IT WANTS GAINS.</span></h1></div>
<div class="ringwrap">
  <svg class="ring" viewBox="0 0 200 200">
    <circle cx="100" cy="100" r="86" fill="none" stroke="rgba(125,232,255,.15)" stroke-width="15"/>
    <circle cx="100" cy="100" r="86" fill="none" stroke="url(#g)" stroke-width="15" stroke-linecap="round" stroke-dasharray="540" stroke-dashoffset="70" transform="rotate(-90 100 100)"/>
    <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#7de8ff"/><stop offset="100%" stop-color="#ff9ecf"/></linearGradient></defs>
  </svg>
  <div class="ringnum"><span>87</span><small>SLEEP SCORE</small></div>
</div>
<div class="right">
  <div class="was">before: <b>68</b></div>
  <div class="arrow">↓ 2 WEEKS ↓</div>
  <div class="now">on the stack: <b>87</b></div>
</div>
<div class="cap">Avg tester gain: <b>+19 points</b> — full clinical doses, zero melatonin*</div>
<div class="chips">
  <div class="chip"><b>2×</b><span>more deep sleep*</span></div>
  <div class="chip"><b>87%</b><span>fell asleep faster*</span></div>
  <div class="chip"><b>0 mg</b><span>melatonin, ever</span></div>
</div>
{offer_card("GET THE STACK")}
</body></html>'''

# S3 · GUMMIES ARE MID
A["sm-ad3"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:linear-gradient(180deg,#0e1033,#241263)}}
.top{{position:absolute;top:64px;left:0;right:0;text-align:center}}
h1{{font-family:Anton;font-size:120px;line-height:1;text-shadow:6px 6px 0 rgba(14,16,51,.8)}}
h1 .c{{color:#7de8ff}}
.cols{{position:absolute;top:280px;left:56px;right:56px;display:flex;gap:22px}}
.col{{flex:1;border-radius:20px;padding:28px}}
.col h3{{font-family:Anton;font-size:32px;margin-bottom:16px;letter-spacing:1px}}
.col.bad{{background:rgba(255,255,255,.05);border:2px solid rgba(255,255,255,.18)}}
.col.good{{background:rgba(125,232,255,.09);border:2.5px solid #7de8ff}}
.col.good h3{{color:#7de8ff}}
.col li{{list-style:none;font-size:23.5px;padding:15px 0 15px 44px;position:relative;color:#cfc7ee;border-bottom:1px solid rgba(255,255,255,.08);font-weight:600;line-height:1.3}}
.col.bad li::before{{content:"💀";position:absolute;left:0;font-size:20px}}
.col.good li::before{{content:"⚡";position:absolute;left:0;font-size:20px}}
.col.good li{{color:#fff}}
.tin{{position:absolute;bottom:125px;left:50%;transform:translateX(-50%);width:340px;border-radius:18px;box-shadow:0 30px 60px rgba(0,0,0,.6);border:3px solid rgba(255,255,255,.2)}}
.mid{{position:absolute;top:728px;left:0;right:0;text-align:center;font-family:Anton;font-size:44px;color:#ffd76e;text-shadow:4px 4px 0 rgba(14,16,51,.8)}}
</style></head><body>
<div class="top"><h1>GUMMIES ARE <span class="c">MID.</span></h1></div>
<div class="mid">UPGRADE YOUR MAIN STAT.</div>
<div class="cols">
  <div class="col bad"><h3>MELATONIN GUMMIES</h3>
    <li>A literal hormone, dosed like candy</li><li>The groggy-morning hangover</li><li>Body makes less of its own</li><li>Kinda embarrassing tbh</li></div>
  <div class="col good"><h3>SLEEP MAXING</h3>
    <li>Full clinical doses, zero hormones</li><li>Wake up actually clear</li><li>Tastes like chocolate</li><li>Looks fire on your counter</li></div>
</div>
<img class="tin" src="../images/sleepmaxing-c-tin.png">
{offer_card()}
</body></html>'''

# S4 · REVENGE BEDTIME SCROLLING
A["sm-ad4"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:#0a0a1e}}
.phoneglow{{position:absolute;top:0;left:0;right:0;height:60%;background:radial-gradient(90% 60% at 50% 0%,rgba(125,232,255,.13),transparent 70%)}}
.time{{position:absolute;top:100px;left:0;right:0;text-align:center;font-family:Anton;font-size:190px;color:#7de8ff;text-shadow:0 0 60px rgba(125,232,255,.5);letter-spacing:4px}}
.line1{{position:absolute;top:340px;left:0;right:0;text-align:center;font-size:38px;font-weight:600;color:#cfc7ee}}
.line1 b{{color:#fff}}
h1{{position:absolute;top:430px;left:70px;right:70px;text-align:center;font-family:Anton;font-size:92px;line-height:1.04;text-shadow:5px 5px 0 rgba(14,16,51,.9)}}
h1 .y{{color:#ffd76e}}
.tin{{position:absolute;bottom:190px;left:50%;transform:translateX(-50%);width:430px;border-radius:20px;box-shadow:0 40px 80px rgba(0,0,0,.65);border:3px solid rgba(255,255,255,.18)}}
</style></head><body>
<div class="phoneglow"></div>
<div class="time">1:47 AM</div>
<div class="line1"><b>400 videos deep.</b> Again.</div>
<h1>YOUR SLEEP DESERVES<br><span class="y">BETTER THAN THIS.</span></h1>
<img class="tin" src="../images/sleepmaxing-c-hero2.png">
{offer_card("FIX MY NIGHTS")}
</body></html>'''

# S5 · THE NIGHT STACK receipts
A["sm-ad5"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{BASE}
body{{background:linear-gradient(165deg,#1b1147 0%,#3a1d8a 50%,#c2438f 100%)}}
.top{{position:absolute;top:62px;left:0;right:0;text-align:center}}
h1{{font-family:Anton;font-size:96px;line-height:1;text-shadow:6px 6px 0 rgba(14,16,51,.85)}}
h1 .c{{color:#c8ff3e}}
.sub{{margin-top:14px;font-size:26px;font-weight:600;color:#f2e9ff}}
.stack{{position:absolute;top:300px;left:110px;width:540px;background:rgba(14,16,51,.9);border:2.5px solid #ff9ecf;border-radius:22px;padding:26px 32px}}
.stack .t{{font-family:Anton;font-size:28px;color:#ff9ecf;text-align:center;margin-bottom:12px;letter-spacing:1px}}
.r{{display:flex;justify-content:space-between;font-size:24px;font-weight:600;padding:11px 2px;border-top:1px solid rgba(255,158,207,.3)}}
.r:first-of-type{{border-top:none}}
.r b{{color:#7de8ff}}
.tin{{position:absolute;top:380px;right:55px;width:380px;border-radius:18px;box-shadow:0 40px 80px rgba(0,0,0,.55);border:3px solid rgba(255,255,255,.2)}}
.stick{{position:absolute;top:960px;left:0;right:0;display:flex;gap:16px;justify-content:center}}
.s{{background:#ffd76e;color:#0e1033;font-weight:700;font-size:22px;padding:14px 26px;border-radius:100px;transform:rotate(-2deg);box-shadow:4px 4px 0 rgba(14,16,51,.8)}}
.s.b{{background:#7de8ff;transform:rotate(1.5deg)}}
.s.w{{background:#fff;transform:rotate(-1deg)}}
.eq{{position:absolute;top:1065px;left:0;right:0;text-align:center;font-family:Anton;font-size:34px;color:#c8ff3e;text-shadow:3px 3px 0 rgba(14,16,51,.8)}}
</style></head><body>
<div class="top">
  <h1>THE NIGHT STACK.<br><span class="c">NOTHING FAKE.</span></h1>
  <div class="sub">The doses sleep nerds buy in five bottles — in one chocolate scoop.</div>
</div>
<div class="stack">
  <div class="t">WHAT'S IN EVERY SCOOP</div>
  <div class="r"><span>Saffron (affron®)</span><b>28 mg</b></div>
  <div class="r"><span>Magnesium Glycinate</span><b>300 mg</b></div>
  <div class="r"><span>L-Theanine</span><b>200 mg</b></div>
  <div class="r"><span>Glycine</span><b>3 g</b></div>
  <div class="r"><span>Ashwagandha KSM-66</span><b>300 mg</b></div>
</div>
<img class="tin" src="../images/sleepmaxing-c-tin.png">
<div class="stick"><span class="s">0 MELATONIN</span><span class="s b">0 CAFFEINE</span><span class="s w">0 GROGGY MORNINGS</span></div>
<div class="eq">SCOOP + WARM MILK + 30 MIN = ELITE SLEEP</div>
{offer_card("GET THE STACK")}
</body></html>'''

for n, h in A.items():
    open(os.path.join(OUT, n + ".html"), "w").write(h)
    print("wrote", n)
