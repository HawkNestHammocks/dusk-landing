#!/usr/bin/env python3
# v7: G4 = blue Moonset w/ "SLEEP DRINK" descriptor (no "chocolate") + dark-chocolate flavour tag.
#     + 3 NEW SLEEP MAXING square-tin variants: B=Blackout, C=Vapor, D=Cloud.
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,500'
     '&family=Jost:wght@300;400;500;600;700&family=Anton&family=Space+Grotesk:wght@400;500;600;700'
     '&family=Archivo+Black&display=swap" rel="stylesheet">')

def mmark(w, gold="#cbb37e", ink="none"):
    return f'''<svg viewBox="0 0 220 200" style="width:{w}px">
  <circle cx="100" cy="110" r="82" fill="{ink}" stroke="{gold}" stroke-width="2"/>
  <circle cx="100" cy="110" r="74" fill="none" stroke="{gold}" stroke-width="0.9" opacity=".65"/>
  <path d="M68 144 V80 L100 122 L132 80 V144" fill="none" stroke="{gold}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M186 22 a26 26 0 1 0 8 20 a20 20 0 1 1 -8 -20Z" fill="{gold}"/>
</svg>'''

L = {}

# ===== G4 · MOONSET FINAL — "SLEEP DRINK", flavour tag =====
L["moonset-g4"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:840px;height:1500px;background:#101726;color:#f0e9d8;font-family:Jost,sans-serif;position:relative;text-align:center;padding:70px 64px}}
.no{{font-weight:500;font-size:18px;letter-spacing:7px;color:#b3ab97}}
.brand{{font-family:'Cormorant Garamond';font-weight:600;font-size:102px;letter-spacing:9px;padding-left:9px;line-height:1;color:#f6efdf;margin-top:28px}}
.what{{margin-top:22px;font-weight:700;font-size:38px;letter-spacing:9px;padding-left:9px;color:#e0c88f}}
.ritual{{font-family:'Cormorant Garamond';font-style:italic;font-weight:500;font-size:29px;color:#cfc5ac;margin-top:18px}}
.band{{position:absolute;left:0;right:0;top:788px;background:linear-gradient(180deg,#d9c084,#bb9d5a);color:#1c1608;padding:30px 60px}}
.band .t{{font-weight:700;font-size:21px;letter-spacing:4px;margin-bottom:12px}}
.band .r{{display:flex;justify-content:space-between;font-size:21px;font-weight:600;letter-spacing:.5px;padding:7px 4px;border-top:1.2px solid rgba(28,22,8,.22)}}
.band .r:first-of-type{{border-top:none}}
.how{{position:absolute;top:1096px;left:64px;right:64px;font-weight:500;font-size:23px;color:#f0e9d8;line-height:1.6}}
.how b{{color:#e0c88f;font-weight:700}}
.flav{{position:absolute;top:1218px;left:0;right:0;display:flex;justify-content:center}}
.flav span{{border:1.4px solid #cbb37e;border-radius:100px;padding:12px 30px;font-weight:600;font-size:18px;letter-spacing:4px;color:#e0c88f}}
.free{{position:absolute;bottom:128px;left:64px;right:64px;font-weight:600;font-size:17px;letter-spacing:3.5px;color:#cfc5ac}}
.nw{{position:absolute;bottom:62px;left:64px;right:64px;font-weight:500;font-size:18px;letter-spacing:3px;color:#e0c88f;display:flex;justify-content:space-between;border-top:1px solid rgba(203,179,126,.4);padding-top:19px}}
</style></head><body><div class="p">
<div style="display:flex;justify-content:center;margin-bottom:6px">{mmark(150)}</div>
<div class="no">N&deg; 30 &mdash; NUIT</div>
<div class="brand">MOONSET</div>
<div class="what">SLEEP DRINK</div>
<div class="ritual">The night ritual &mdash; deep, natural sleep.</div>
<div class="band">
  <div class="t">CLINICALLY DOSED &middot; FIVE ACTIVES</div>
  <div class="r"><span>Saffron (affron&reg;)</span><b>28 mg</b></div>
  <div class="r"><span>Magnesium Glycinate</span><b>300 mg</b></div>
  <div class="r"><span>L-Theanine</span><b>200 mg</b></div>
  <div class="r"><span>Glycine &middot; Ashwagandha KSM-66</span><b>3 g &middot; 300 mg</b></div>
</div>
<div class="how">Mix one scoop into <b>warm milk</b>,<br><b>30 minutes before bed.</b></div>
<div class="flav"><span>DARK CHOCOLATE FLAVOUR</span></div>
<div class="free">MELATONIN-FREE &middot; CAFFEINE-FREE &middot; VEGAN</div>
<div class="nw"><span>240 G &mdash; 30 SERVINGS</span><span>THIRTY NIGHTS</span></div>
</div></body></html>'''

# shared bits for SLEEP MAXING square-tin faces (900x1100, squarer)
SM_ACTS = '''<div class="r"><span>Saffron (affron&reg;)</span><b>28 mg</b></div>
  <div class="r"><span>Magnesium Glycinate</span><b>300 mg</b></div>
  <div class="r"><span>L-Theanine</span><b>200 mg</b></div>
  <div class="r"><span>Glycine &middot; Ashwagandha</span><b>3 g &middot; 300 mg</b></div>'''

# ===== SM-B · BLACKOUT — matte black + acid lime, midnight-gamer glow =====
L["sleepmaxing-b"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:900px;height:1100px;background:#0a0a0c;color:#fff;font-family:'Space Grotesk',sans-serif;position:relative;text-align:center;padding:54px 52px;overflow:hidden}}
.p::before{{content:"";position:absolute;top:-160px;left:50%;transform:translateX(-50%);width:700px;height:700px;background:radial-gradient(circle,rgba(200,255,62,.16),transparent 62%)}}
.moon{{width:130px;height:130px;margin:24px auto 0;filter:drop-shadow(0 0 26px rgba(200,255,62,.8))}}
.brand{{font-family:Anton;font-size:118px;line-height:.95;letter-spacing:2px;color:#c8ff3e;margin-top:26px;text-shadow:0 0 34px rgba(200,255,62,.45)}}
.brand span{{color:#fff}}
.what{{margin-top:30px;font-weight:700;font-size:29px;letter-spacing:5px;color:#0a0a0c;background:#c8ff3e;display:inline-block;padding:11px 28px;border-radius:8px}}
.tag{{margin-top:24px;font-weight:600;font-size:24px;color:#9aa0a8}}
.tag b{{color:#c8ff3e}}
.stack{{margin:42px auto 0;max-width:680px;background:#121216;border:2px solid #c8ff3e;border-radius:18px;padding:26px 30px;text-align:left;box-shadow:0 0 30px rgba(200,255,62,.18)}}
.stack .t{{font-family:Anton;font-size:23px;letter-spacing:1.5px;color:#c8ff3e;text-align:center;margin-bottom:10px}}
.stack .r{{display:flex;justify-content:space-between;font-size:21px;font-weight:600;padding:8px 2px;border-top:1px solid rgba(200,255,62,.2)}}
.stack .r:first-of-type{{border-top:none}}
.stack .r b{{color:#c8ff3e}}
.flav{{margin-top:38px;font-weight:700;font-size:19px;letter-spacing:3px;color:#9aa0a8}}
.flav b{{color:#fff}}
.nw{{position:absolute;bottom:44px;left:52px;right:52px;display:flex;justify-content:space-between;font-weight:700;font-size:16px;letter-spacing:2px;color:#9aa0a8;border-top:1.5px solid #26262c;padding-top:14px}}
</style></head><body><div class="p">
<svg class="moon" viewBox="0 0 120 120"><path d="M92 26 a44 44 0 1 0 14 34 a34 34 0 1 1 -14 -34Z" fill="#c8ff3e"/></svg>
<div class="brand">SLEEP<span>MAXING</span></div>
<div class="what">NIGHTLY SLEEP DRINK</div>
<div class="tag">0 melatonin &middot; 0 caffeine &middot; <b>0 groggy mornings</b></div>
<div class="stack">
  <div class="t">THE NIGHT STACK &mdash; FULL CLINICAL DOSES</div>
  {SM_ACTS}
</div>
<div class="flav">TASTES LIKE <b>CHOCOLATE</b> &middot; MIXES INTO WARM MILK</div>
<div class="nw"><span>240 G &middot; 30 SERVINGS</span><span>VEGAN</span></div>
</div></body></html>'''

# ===== SM-C · VAPOR — sunset vaporwave gradient, chrome-adjacent =====
L["sleepmaxing-c"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:900px;height:1100px;background:linear-gradient(180deg,#0e1033 0%,#3b1a6e 42%,#c2438f 78%,#ff8e5a 100%);color:#fff;font-family:'Space Grotesk',sans-serif;position:relative;text-align:center;padding:54px 52px;overflow:hidden}}
.sun{{position:absolute;bottom:-190px;left:50%;transform:translateX(-50%);width:520px;height:520px;border-radius:50%;background:linear-gradient(180deg,#ffd76e,#ff7a4d);opacity:.55}}
.z{{position:absolute;top:44px;left:48px;font-family:Anton;font-size:44px;color:#7de8ff;transform:rotate(-10deg);text-shadow:3px 3px 0 #0e1033}}
.moon{{width:100px;height:100px;margin:0 auto}}
.brand{{font-family:Anton;font-size:104px;line-height:.95;letter-spacing:2px;margin-top:10px;background:linear-gradient(180deg,#fff 30%,#7de8ff 65%,#ff9ecf);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(4px 5px 0 #0e1033)}}
.what{{margin-top:16px;font-weight:700;font-size:26px;letter-spacing:5px;color:#0e1033;background:#7de8ff;display:inline-block;padding:9px 24px;border-radius:100px}}
.tag{{margin-top:16px;font-weight:600;font-size:22px;color:#ffe6f2}}
.stack{{position:relative;z-index:2;margin:26px auto 0;max-width:640px;background:rgba(14,16,51,.78);border:2px solid #ff9ecf;border-radius:18px;padding:18px 26px;text-align:left}}
.stack .t{{font-family:Anton;font-size:21px;letter-spacing:1.5px;color:#ff9ecf;text-align:center;margin-bottom:8px}}
.stack .r{{display:flex;justify-content:space-between;font-size:19px;font-weight:600;padding:6px 2px;border-top:1px solid rgba(255,158,207,.28)}}
.stack .r:first-of-type{{border-top:none}}
.stack .r b{{color:#7de8ff}}
.flav{{position:relative;z-index:2;margin-top:20px;font-weight:700;font-size:17px;letter-spacing:3px;color:#0e1033;background:#ffd76e;display:inline-block;padding:8px 20px;border-radius:100px;transform:rotate(-1.5deg)}}
.nw{{position:absolute;bottom:44px;left:52px;right:52px;display:flex;justify-content:space-between;font-weight:700;font-size:16px;letter-spacing:2px;color:#fff;border-top:1.5px solid rgba(255,255,255,.4);padding-top:14px;z-index:2}}
</style></head><body><div class="p">
<div class="sun"></div>
<div class="z">ZZZ</div>
<svg class="moon" viewBox="0 0 120 120"><path d="M92 26 a44 44 0 1 0 14 34 a34 34 0 1 1 -14 -34Z" fill="#ffd76e" stroke="#0e1033" stroke-width="5"/></svg>
<div class="brand">SLEEP<br>MAXING</div>
<div class="what">NIGHTLY SLEEP DRINK</div>
<div class="tag">clock out. power down. max out.</div>
<div class="stack">
  <div class="t">THE NIGHT STACK &mdash; FULL CLINICAL DOSES</div>
  {SM_ACTS}
</div>
<div class="flav">CHOCOLATE FLAVOR &middot; 0 MELATONIN &middot; 0 CAFFEINE</div>
<div class="nw"><span>240 G &middot; 30 SERVINGS</span><span>VEGAN</span></div>
</div></body></html>'''

# ===== SM-D · CLOUD — cream + sky blue + navy Anton, soft sticker vibe =====
L["sleepmaxing-d"] = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>
*{{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
.p{{width:900px;height:1100px;background:#f3efe6;color:#1d2a5e;font-family:'Space Grotesk',sans-serif;position:relative;text-align:center;padding:54px 52px;overflow:hidden}}
.cl{{position:absolute;border-radius:100px;background:#dfe9ff}}
.cl1{{width:300px;height:96px;top:70px;left:-70px}}
.cl2{{width:240px;height:80px;top:180px;right:-60px}}
.cl3{{width:280px;height:90px;bottom:150px;left:-80px;opacity:.7}}
.moon{{width:124px;height:124px;margin:20px auto 0;position:relative;z-index:2}}
.brand{{position:relative;z-index:2;font-family:Anton;font-size:116px;line-height:.95;letter-spacing:2px;color:#1d2a5e;margin-top:26px}}
.brand span{{color:#4f7bff}}
.what{{position:relative;z-index:2;margin-top:30px;font-weight:700;font-size:29px;letter-spacing:5px;color:#f3efe6;background:#1d2a5e;display:inline-block;padding:11px 28px;border-radius:10px;transform:rotate(-1deg)}}
.tag{{position:relative;z-index:2;margin-top:24px;font-weight:600;font-size:24px;color:#5a648c}}
.stick{{position:relative;z-index:2;margin:30px auto 0;display:flex;gap:12px;justify-content:center}}
.s{{background:#ffd54d;color:#1d2a5e;font-weight:700;font-size:18.5px;padding:11px 19px;border-radius:100px;transform:rotate(-2deg);box-shadow:2.5px 2.5px 0 #1d2a5e}}
.s.b{{background:#4f7bff;color:#fff;transform:rotate(1.5deg)}}
.s.w{{background:#fff;transform:rotate(-1deg)}}
.stack{{position:relative;z-index:2;margin:42px auto 0;max-width:680px;background:#fff;border:2.5px solid #1d2a5e;border-radius:18px;padding:26px 30px;text-align:left;box-shadow:5px 5px 0 #1d2a5e}}
.stack .t{{font-family:Anton;font-size:23px;letter-spacing:1.5px;color:#1d2a5e;text-align:center;margin-bottom:10px}}
.stack .r{{display:flex;justify-content:space-between;font-size:21px;font-weight:600;padding:8px 2px;border-top:1px solid #e3e6f2}}
.stack .r:first-of-type{{border-top:none}}
.stack .r b{{color:#4f7bff}}
.flav{{position:relative;z-index:2;margin-top:38px;font-weight:700;font-size:19px;letter-spacing:3px;color:#5a648c}}
.flav b{{color:#1d2a5e}}
.nw{{position:absolute;bottom:44px;left:52px;right:52px;display:flex;justify-content:space-between;font-weight:700;font-size:16px;letter-spacing:2px;color:#5a648c;border-top:2px solid #1d2a5e;padding-top:14px;z-index:2}}
</style></head><body><div class="p">
<div class="cl cl1"></div><div class="cl cl2"></div><div class="cl cl3"></div>
<svg class="moon" viewBox="0 0 120 120"><path d="M92 26 a44 44 0 1 0 14 34 a34 34 0 1 1 -14 -34Z" fill="#ffd54d" stroke="#1d2a5e" stroke-width="5"/><circle cx="88" cy="30" r="5" fill="#4f7bff"/></svg>
<div class="brand">SLEEP<span>MAXING</span></div>
<div class="what">NIGHTLY SLEEP DRINK</div>
<div class="tag">max your sleep. wake up different.</div>
<div class="stick">
  <span class="s">0 MELATONIN</span>
  <span class="s b">0 CAFFEINE</span>
  <span class="s w">0 GROGGY AMs</span>
</div>
<div class="stack">
  <div class="t">THE NIGHT STACK &mdash; FULL CLINICAL DOSES</div>
  {SM_ACTS}
</div>
<div class="flav">TASTES LIKE <b>CHOCOLATE</b> &middot; WARM MILK + 30 MIN</div>
<div class="nw"><span>240 G &middot; 30 SERVINGS</span><span>VEGAN</span></div>
</div></body></html>'''

for n,h in L.items():
    open(os.path.join(OUT,n+".html"),"w").write(h); print("wrote",n)
