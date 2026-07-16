#!/usr/bin/env python3
# Generic Seedream v4 edit: feed a product render, swap the scene. Usage: edit_scene.py <in.png> <out.png> <prompt> [WxH]
import base64, json, os, subprocess, sys, time, urllib.request

src, out, prompt = sys.argv[1], sys.argv[2], sys.argv[3]
w, h = (sys.argv[4].split("x") if len(sys.argv) > 4 else ("1080", "1920"))
key = json.load(open(os.path.expanduser("~/.openclaw/secrets/fal.json")))["fal_key"]

small = f"/tmp/edit_sm_{os.getpid()}.png"
subprocess.run(["sips", "--resampleWidth", "820", src, "--out", small], check=True, capture_output=True)
uri = "data:image/png;base64," + base64.b64encode(open(small, "rb").read()).decode()

req = urllib.request.Request(
    "https://queue.fal.run/fal-ai/bytedance/seedream/v4/edit",
    data=json.dumps({"prompt": prompt, "image_urls": [uri],
                     "image_size": {"width": int(w), "height": int(h)}}).encode(),
    headers={"Authorization": f"Key {key}", "Content-Type": "application/json"})
rid = json.load(urllib.request.urlopen(req))["request_id"]
print("submitted", rid, flush=True)

base = f"https://queue.fal.run/fal-ai/bytedance/requests/{rid}"
for _ in range(60):
    time.sleep(5)
    st = json.load(urllib.request.urlopen(urllib.request.Request(
        base + "/status", headers={"Authorization": f"Key {key}"})))
    if st["status"] == "COMPLETED":
        res = json.load(urllib.request.urlopen(urllib.request.Request(
            base, headers={"Authorization": f"Key {key}"})))
        urllib.request.urlretrieve(res["images"][0]["url"], out)
        print("DONE", out)
        sys.exit(0)
    if st["status"] not in ("IN_QUEUE", "IN_PROGRESS"):
        print("FAILED", st); sys.exit(1)
print("TIMEOUT"); sys.exit(1)
