import json, os, glob, re, sys
P = os.path.expanduser("~/.claude/projects")
PREFIX = "-Users-leannchen-Library-Application-Support-Claude-scratch-workspaces-2037fc6c-747d-4cf1-a5f5-8a4697a4e390-5ef58abe-646a-4ac9-9fae-d0ea15914ce2-scratch-"
CUT = sys.argv[1]
def clean(t):
    t = re.sub(r"<system-reminder>.*?</system-reminder>", "", t, flags=re.S)
    return t.strip()
for d in sorted(glob.glob(os.path.join(P, PREFIX + "*"))):
    tag = d.split(PREFIX)[1]
    if tag == "2026-09-18-23b6df": continue
    for f in sorted(glob.glob(os.path.join(d, "*.jsonl"))):
        sid = os.path.basename(f)[:8]
        with open(f, errors="replace") as fh:
            for line in fh:
                try: o = json.loads(line)
                except Exception: continue
                if o.get("isSidechain"): continue
                typ = o.get("type")
                if typ not in ("user","assistant"): continue
                ts = o.get("timestamp","")
                if ts <= CUT: continue
                c = (o.get("message") or {}).get("content")
                texts = []
                if isinstance(c, str): texts=[c]
                elif isinstance(c, list):
                    texts=[b.get("text","") for b in c if isinstance(b, dict) and b.get("type")=="text"]
                txt = clean("\n".join(texts))
                if not txt: continue
                if typ=="user" and (o.get("isMeta") or txt.startswith("<task-notification") or txt.startswith("<command-name>")): continue
                print(f"\n===== [{sid}] {typ.upper()} [{ts}] =====\n{txt}")
