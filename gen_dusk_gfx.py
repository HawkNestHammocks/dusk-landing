#!/usr/bin/env python3
import os
OUT = os.path.expanduser("~/projects/dusk-landing")
F = ('<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700'
     '&family=Inter:wght@400;500;600;700;800&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">')
CSS = '''*{margin:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}
:root{--navy:#0f1430;--navy2:#161c40;--cream:#f2eddd;--gold:#d9b25f;--muted:#9096ba;--line:rgba(217,178,95,.28)}
body{font-family:Inter,sans-serif}
.moon{fill:var(--gold)}
'''

# ============ BACK PANEL (navy, tall) ============
BACK = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{CSS}
.p{{width:840px;height:1500px;background:var(--navy);color:var(--cream);padding:60px 58px;position:relative}}
.top{{display:flex;align-items:center;gap:12px;border-bottom:1px solid var(--line);padding-bottom:22px;margin-bottom:26px}}
.top svg{{width:44px;height:44px}} .top .bn{{font-family:Fraunces;font-size:34px;font-weight:600;letter-spacing:3px}}
.top .tag{{margin-left:auto;font-family:Oswald;font-size:13px;letter-spacing:3px;color:var(--gold)}}
.facts{{background:var(--cream);color:#111;border:3px solid #111;border-radius:5px;padding:16px 18px;font-family:Inter;margin-bottom:24px}}
.facts .h{{font-family:Fraunces;font-weight:700;font-size:32px;border-bottom:9px solid #111;padding-bottom:2px;line-height:1}}
.facts .s{{font-size:13px;border-bottom:1px solid #111;padding:3px 0;display:flex;justify-content:space-between}}
.facts .s b{{font-weight:700}}
.facts .hdr{{display:flex;justify-content:flex-end;font-size:11px;font-weight:700;border-bottom:5px solid #111;padding:3px 0}}
.facts .r{{display:flex;justify-content:space-between;font-size:14px;border-bottom:1px solid #111;padding:6px 1px}}
.facts .r .n b{{font-weight:600}} .facts .r .n span{{font-weight:400;color:#444}}
.facts .foot{{font-size:10.5px;color:#333;margin-top:7px;line-height:1.35}}
.blk{{margin-bottom:20px}} .blk .lbl{{font-family:Oswald;font-size:13px;letter-spacing:2.5px;color:var(--gold);margin-bottom:6px}}
.blk p{{font-size:15px;color:#d5d7e6;line-height:1.5}}
.badges{{display:flex;gap:8px;margin:22px 0}}
.badge{{border:1px solid var(--gold);color:var(--gold);border-radius:5px;padding:8px 12px;font-size:12px;font-weight:600;letter-spacing:.5px}}
.foot2{{position:absolute;bottom:52px;left:58px;right:58px;display:flex;justify-content:space-between;align-items:flex-end;border-top:1px solid var(--line);padding-top:20px}}
.bar{{display:flex;align-items:flex-end;gap:2px;height:46px}} .bar i{{width:3px;background:var(--cream)}}
.brandinfo{{text-align:right;font-size:12px;color:var(--muted);line-height:1.5}} .brandinfo b{{color:var(--cream);font-family:Oswald;letter-spacing:1px}}
</style></head><body><div class="p">
<div class="top"><svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="20" fill="none" stroke="#d9b25f" stroke-width="1.5"/><path d="M28 12 a12 12 0 1 0 0 20 a9 9 0 1 1 0-20Z" class="moon"/></svg>
<span class="bn">DUSK</span><span class="tag">WIND-DOWN COCOA</span></div>
<div class="facts">
<div class="h">Supplement Facts</div>
<div class="s"><span>Serving Size: 1 Scoop (8 g)</span></div>
<div class="s"><b>Servings Per Container: 30</b></div>
<div class="hdr">Amount Per Serving</div>
<div class="r"><span class="n"><b>Magnesium</b> <span>(as glycinate)</span></span><b>300 mg</b></div>
<div class="r"><span class="n"><b>Glycine</b></span><b>3 g</b></div>
<div class="r"><span class="n"><b>L-Theanine</b></span><b>200 mg</b></div>
<div class="r"><span class="n"><b>Ashwagandha</b> <span>(KSM-66®, root)</span></span><b>300 mg</b></div>
<div class="r"><span class="n"><b>Saffron extract</b> <span>(affron®)</span></span><b>28 mg</b></div>
<div class="r"><span class="n"><b>Lemon Balm</b> <span>(aerial)</span></span><b>300 mg</b></div>
<div class="r"><span class="n"><b>Apigenin</b> <span>(from chamomile)</span></span><b>50 mg</b></div>
<div class="foot">Other ingredients: Carob powder, coconut milk powder, natural cocoa flavor, Ceylon cinnamon, monk fruit extract, Himalayan pink salt, vanilla.</div>
</div>
<div class="blk"><div class="lbl">DIRECTIONS</div><p>Stir one scoop into 8 oz of warm or cold milk (dairy or plant). Enjoy 30 minutes before bed as part of your wind-down.</p></div>
<div class="blk"><div class="lbl">WARNINGS</div><p>Consult your physician before use if pregnant, nursing, taking medication, or have a medical condition. Do not exceed one serving daily. Keep out of reach of children. Store in a cool, dry place.</p></div>
<div class="badges"><span class="badge">MELATONIN-FREE</span><span class="badge">CAFFEINE-FREE</span><span class="badge">VEGAN</span><span class="badge">3RD-PARTY TESTED</span></div>
<div class="foot2">
<div class="bar"><i style="height:100%"></i><i style="height:60%"></i><i style="height:100%"></i><i style="height:45%"></i><i style="height:85%"></i><i style="height:100%"></i><i style="height:55%"></i><i style="height:95%"></i><i style="height:100%"></i><i style="height:70%"></i><i style="height:100%"></i><i style="height:50%"></i><i style="height:90%"></i><i style="height:100%"></i><i style="height:65%"></i><i style="height:100%"></i></div>
<div class="brandinfo"><b>DUSK SUPPLY CO.</b><br>Distributed in the USA<br>hello@dusk.co · dusk.co<br>LOT/EXP: see bottom</div>
</div>
</div></body></html>'''

# ============ HOW-TO-USE (landscape) ============
HOWTO = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{CSS}
.p{{width:1200px;height:700px;background:var(--navy);color:var(--cream);padding:56px 60px;position:relative}}
.hd{{text-align:center;margin-bottom:44px}}
.hd .k{{font-family:Oswald;letter-spacing:4px;font-size:15px;color:var(--gold);margin-bottom:8px}}
.hd h2{{font-family:Fraunces;font-size:48px;font-weight:600}}
.steps{{display:flex;gap:26px}}
.st{{flex:1;background:var(--navy2);border:1px solid var(--line);border-radius:18px;padding:34px 26px;text-align:center}}
.st .ic{{width:78px;height:78px;margin:0 auto 20px;border:1.5px solid var(--gold);border-radius:50%;display:flex;align-items:center;justify-content:center}}
.st .ic svg{{width:40px;height:40px;stroke:var(--gold);fill:none;stroke-width:1.6}}
.st .num{{font-family:Oswald;color:var(--gold);letter-spacing:2px;font-size:14px;margin-bottom:6px}}
.st h3{{font-family:Fraunces;font-size:26px;margin-bottom:8px}}
.st p{{font-size:16px;color:#c4c7dc;line-height:1.5}}
</style></head><body><div class="p">
<div class="hd"><div class="k">THE NIGHTLY RITUAL</div><h2>Three minutes to a slower night</h2></div>
<div class="steps">
<div class="st"><div class="ic"><svg viewBox="0 0 40 40"><path d="M8 14 h24 l-3 18 a2 2 0 0 1-2 2 H13 a2 2 0 0 1-2-2 Z"/><path d="M14 14 c0-6 12-6 12 0"/></svg></div><div class="num">STEP 01</div><h3>Scoop</h3><p>One level scoop of DUSK wind-down cocoa.</p></div>
<div class="st"><div class="ic"><svg viewBox="0 0 40 40"><rect x="11" y="6" width="18" height="28" rx="3"/><path d="M11 14 h18"/><path d="M16 2 v4 M24 2 v4"/></svg></div><div class="num">STEP 02</div><h3>Warm or cold milk</h3><p>Stir into 8 oz of milk, dairy or plant. Your call.</p></div>
<div class="st"><div class="ic"><svg viewBox="0 0 40 40"><path d="M9 18 h20 v6 a10 10 0 0 1-20 0 Z"/><path d="M29 19 h4 a3 3 0 0 1 0 8 h-3"/><path d="M15 10 c0-3 3-3 3-6 M22 10 c0-3 3-3 3-6"/></svg></div><div class="num">STEP 03</div><h3>Sip 30 min before bed</h3><p>Phone down. Let the day dissolve. Drift off naturally.</p></div>
</div>
</div></body></html>'''

# ============ SCIENCE (portrait-ish) ============
ING = [
 ("Magnesium Glycinate","300&nbsp;mg","Calms the nervous system &amp; relaxes muscles","The single most evidence-backed sleep mineral — multiple RCTs."),
 ("L-Theanine","200&nbsp;mg","Quiets mental chatter, no sedation","RCTs show faster sleep onset &amp; less nighttime anxiety."),
 ("Glycine","3&nbsp;g","Lowers core temp for deeper sleep","Trials: improved sleep quality &amp; less next-day fatigue."),
 ("Ashwagandha KSM-66®","300&nbsp;mg","Drops cortisol, eases a busy mind","Human trials: reduced stress &amp; improved sleep."),
 ("Saffron (affron®)","28&nbsp;mg","Improves sleep quality &amp; morning mood","30+ clinical trials; 28&nbsp;mg measurably improved sleep."),
 ("Apigenin (chamomile)","50&nbsp;mg","Gently eases you into sleep","Binds the same calming GABA-A receptors as chamomile."),
]
rows = "".join(f'''<div class="ir"><div class="il"><div class="inm">{n}</div><div class="idose">{d}</div></div>
<div class="iben">{b}</div><div class="iev">{e}</div></div>''' for n,d,b,e in ING)
SCI = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{CSS}
.p{{width:1200px;height:660px;background:var(--navy);color:var(--cream);padding:52px 62px}}
.hd{{text-align:center;margin-bottom:34px}} .hd .k{{font-family:Oswald;letter-spacing:4px;font-size:15px;color:var(--gold);margin-bottom:8px}}
.hd h2{{font-family:Fraunces;font-size:46px;font-weight:600}} .hd p{{color:var(--muted);font-size:17px;margin-top:8px}}
.colhead{{display:grid;grid-template-columns:1.15fr 1.15fr 1.3fr;gap:18px;font-family:Oswald;font-size:13px;letter-spacing:2px;color:var(--gold);padding:0 8px 10px;border-bottom:1px solid var(--line)}}
.ir{{display:grid;grid-template-columns:1.15fr 1.15fr 1.3fr;gap:18px;align-items:center;padding:18px 8px;border-bottom:1px solid rgba(255,255,255,.08)}}
.inm{{font-family:Fraunces;font-size:22px;font-weight:600}} .idose{{font-family:Oswald;color:var(--gold);font-size:15px;margin-top:2px}}
.iben{{font-size:16px;color:#dcdeec}} .iev{{font-size:14.5px;color:#a7abc9;line-height:1.45}}
.ft{{text-align:center;margin-top:22px;font-size:14px;color:var(--muted)}}
</style></head><body><div class="p">
<div class="hd"><div class="k">BACKED BY SCIENCE</div><h2>Real ingredients. Real doses. Real evidence.</h2>
<p>No proprietary blends. Every active is disclosed at a dose studies actually used.</p></div>
<div class="colhead"><div>INGREDIENT</div><div>WHAT IT DOES</div><div>THE EVIDENCE</div></div>
{rows}
<div class="ft">Statements not evaluated by the FDA. Not intended to diagnose, treat, cure, or prevent any disease.</div>
</div></body></html>'''

# ============ BENEFITS (landscape) ============
BEN = [
 ("Fall asleep faster","Calming actives quiet the mind so you drift off instead of ruminating."),
 ("Sleep deeper","Magnesium + glycine support the deep, restorative stages of sleep."),
 ("Wake up clear","No hangover, no fog — you wake refreshed, not knocked-out."),
 ("Calm a racing mind","L-theanine &amp; ashwagandha take the edge off the day's stress."),
 ("No dependency","Zero melatonin. Nothing your body learns to rely on."),
 ("A ritual you crave","A warm, cozy cup replaces the doomscroll as your off-switch."),
]
bcards = "".join(f'''<div class="bc"><div class="bi"><svg viewBox="0 0 24 24"><path d="M12 3 a9 9 0 1 0 9 9 A7 7 0 0 1 12 3Z"/></svg></div>
<h3>{t}</h3><p>{d}</p></div>''' for t,d in BEN)
BENH = f'''<!DOCTYPE html><html><head><meta charset="utf-8">{F}<style>{CSS}
.p{{width:1200px;height:820px;background:var(--navy);color:var(--cream);padding:52px 60px}}
.hd{{text-align:center;margin-bottom:36px}} .hd .k{{font-family:Oswald;letter-spacing:4px;font-size:15px;color:var(--gold);margin-bottom:8px}}
.hd h2{{font-family:Fraunces;font-size:46px;font-weight:600}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
.bc{{background:var(--navy2);border:1px solid var(--line);border-radius:16px;padding:28px}}
.bi{{width:52px;height:52px;border-radius:12px;background:rgba(217,178,95,.14);display:flex;align-items:center;justify-content:center;margin-bottom:16px}}
.bi svg{{width:26px;height:26px;fill:var(--gold)}}
.bc h3{{font-family:Fraunces;font-size:23px;margin-bottom:7px}} .bc p{{font-size:15.5px;color:#c4c7dc;line-height:1.5}}
</style></head><body><div class="p">
<div class="hd"><div class="k">WHAT A NIGHTLY CUP DOES</div><h2>Better nights, clearer mornings</h2></div>
<div class="grid">{bcards}</div>
</div></body></html>'''

for n,h in [("back_panel",BACK),("gfx_howto",HOWTO),("gfx_science",SCI),("gfx_benefits",BENH)]:
    open(os.path.join(OUT,n+".html"),"w").write(h); print(n)
