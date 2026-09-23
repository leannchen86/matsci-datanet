import json, os, glob, re, sys
P = os.path.expanduser("~/.claude/projects")
PREFIX = "-Users-leannchen-Library-Application-Support-Claude-scratch-workspaces-2037fc6c-747d-4cf1-a5f5-8a4697a4e390-5ef58abe-646a-4ac9-9fae-d0ea15914ce2-scratch-"
OUT = sys.argv[1]
SKIP = {"2026-09-18-23b6df", "2026-09-16-5cd38c"}
def clean(t):
    t = re.sub(r"<system-reminder>.*?</system-reminder>", "", t, flags=re.S)
    t = re.sub(r"<local-command-stdout>.*?</local-command-stdout>", "", t, flags=re.S)
    return t.strip()
rows = []
for d in sorted(glob.glob(os.path.join(P, PREFIX + "*"))):
    tag = d.split(PREFIX)[1]
    if tag in SKIP: continue
    for f in sorted(glob.glob(os.path.join(d, "*.jsonl"))):
        sid = os.path.basename(f)[:8]
        out = []; nu = na = 0; first = last = None; title = None
        with open(f, errors="replace") as fh:
            for line in fh:
                try: o = json.loads(line)
                except Exception: continue
                if o.get("type") == "summary" and o.get("summary"): title = o["summary"]
                if o.get("isSidechain"): continue
                typ = o.get("type")
                if typ not in ("user", "assistant"): continue
                msg = o.get("message") or {}
                c = msg.get("content")
                texts = []
                if isinstance(c, str): texts = [c]
                elif isinstance(c, list):
                    for b in c:
                        if isinstance(b, dict) and b.get("type") == "text": texts.append(b.get("text", ""))
                txt = clean("\n".join(texts))
                if not txt: continue
                ts = o.get("timestamp", "")
                first = first or ts; last = ts or last
                if typ == "user":
                    if o.get("isMeta"): continue
                    if txt.startswith("<task-notification") or txt.startswith("<command-name>") or "tool_use_id" in txt[:40]: 
                        continue
                    nu += 1
                    tagname = "USER (compaction summary)" if o.get("isCompactSummary") else "USER"
                    out.append(f"\n\n===== {tagname} [{ts[:16]}] =====\n{txt}")
                else:
                    na += 1
                    out.append(f"\n\n----- ASSISTANT [{ts[:16]}] -----\n{txt}")
        body = "".join(out)
        name = f"{tag}__{sid}.md"
        with open(os.path.join(OUT, name), "w") as w:
            w.write(f"# Transcript digest: workspace {tag}, session {sid}\n# span {first} -> {last}; user msgs {nu}; assistant text msgs {na}\n" + body)
        rows.append((name, len(body), nu, na, (first or "")[:10], (last or "")[:10]))
for r in rows: print(r)
