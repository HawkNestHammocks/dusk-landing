#!/usr/bin/env python3
# Wrap a flat label PNG onto a tin via fal Seedream v4 edit. Usage: wrap_tin.py <label.png> <out.png> <tin_desc>
import base64, json, os, subprocess, sys, time, urllib.request

label, out, desc = sys.argv[1], sys.argv[2], sys.argv[3]
key = json.load(open(os.path.expanduser("~/.openclaw/secrets/fal.json")))["fal_key"]

small = f"/tmp/wrap_sm_{os.getpid()}.png"
subprocess.run(["sips", "--resampleWidth", "840" if "moonset" in label else "900", label, "--out", small],
               check=True, capture_output=True)
subprocess.run(["sips", "--resampleWidth", "700", small, "--out", small], check=True, capture_output=True)
uri = "data:image/png;base64," + base64.b64encode(open(small, "rb").read()).decode()

prompt = (f"Take this flat label design and apply it as the printed front face of {desc} "
          "The tin sits on a surface in a professional studio product photograph, soft lighting, subtle shadow. "
          "PERFECTLY STRAIGHT-SIDED tin with crisp vertical edges — no taper, no pinch, no hourglass shape. "
          "TEXT FIDELITY IS CRITICAL: copy every word of the label EXACTLY, letter-for-letter, "
          "preserving all colors, layout proportions and the logo precisely as designed.")

req = urllib.request.Request(
    "https://queue.fal.run/fal-ai/bytedance/seedream/v4/edit",
    data=json.dumps({"prompt": prompt, "image_urls": [uri],
                     "image_size": {"width": 1080, "height": 1350}}).encode(),
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
        url = res["images"][0]["url"]
        urllib.request.urlretrieve(url, out)
        print("DONE", out)
        sys.exit(0)
    if st["status"] not in ("IN_QUEUE", "IN_PROGRESS"):
        print("FAILED", st); sys.exit(1)
print("TIMEOUT"); sys.exit(1)
