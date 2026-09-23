import re, os, glob, html, json, shutil, sys
SP = sys.argv[1]
AF = os.path.join(SP, "artifact-files")
names = {
 "d5a2dd11": "R03_toward-a-materials-imagenet",
 "1b55fc0e": "R10_xrd-curation-experiments",
 "230ca46d": "R08_dft-vs-experiment-debrief",
 "ed9b9c93": "R04_materials-imagenet-debrief",
 "c4ba2e10": "R06_discovered-materials-debrief",
 "8018ee71": "R02_record-wall-debrief",
 "23cb6c87": "R07_thermoelectric-benchmark-spec",
 "80f08ad9": "R09_recursion-in-materials-ai",
 "ab544b74": "R05_discovered-materials-data-gaps",
 "2c88ce50": "R01_materials-record-wall",
}
def to_text(h):
    h = re.sub(r"(?is)<(script|style|svg|noscript)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</(p|div|li|tr|h[1-6]|section|article|details|summary|table|ul|ol|header|footer|figure|figcaption|blockquote|dd|dt)>", "\n", h)
    h = re.sub(r"(?i)<(h[1-6])[^>]*>", "\n\n## ", h)
    h = re.sub(r"(?i)<li[^>]*>", "\n- ", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    h = re.sub(r"(?s)<[^>]+>", "", h)
    h = html.unescape(h)
    h = re.sub(r"[ \t\r\f\v]+", " ", h)
    h = re.sub(r"\n\s*\n\s*\n+", "\n\n", h)
    return h.strip()
rep = []
for d in glob.glob(os.path.join(AF, "*")):
    key = os.path.basename(d)[:8]
    if key not in names: continue
    raw = open(os.path.join(d, "index.html"), errors="replace").read()
    title = re.search(r"(?is)<title>(.*?)</title>", raw)
    txt = to_text(raw)
    # embedded JSON data in scripts (Record Wall keeps records in script) -> note size only
    out = os.path.join(SP, "corpus/reports", names[key] + ".txt")
    open(out, "w").write(f"# REPORT: {title.group(1).strip() if title else names[key]}\n\n" + txt)
    rep.append((names[key], len(raw), len(txt)))
for r in sorted(rep): print("report", r)

# conversations
CV = os.path.join(SP, "convos")
def parts(f):
    t = open(f).read()
    ps = re.split(r"\n\n(?====== USER|----- ASSISTANT)", t)
    return ps[0], ps[1:]
units = {}
hA, A = parts(os.path.join(CV, "2026-09-14-84cb7d__1abc87d2.md"))
hB, B = parts(os.path.join(CV, "2026-09-14-84cb7d__7c448781.md"))
hC, C = parts(os.path.join(CV, "2026-09-14-84cb7d__cc6ae63b.md"))
units["C01_data-landscape_TRUNK(shared-start-of-3-branches)"] = A[:25]
units["C02_data-landscape_branch-periodic-labs-report"] = A[25:]
units["C03_data-landscape_branch-main(build-list+curation-rounds)"] = B[25:]
units["C04_data-landscape_branch-data-curation(xrd)"] = C[25:]
other = {
 "2026-09-14-7df469__684bb26e.md": "C05_discovered-materials-experimental-data-bottlenecks",
 "2026-09-14-857a6c__6fecd6c5.md": "C06_periodic-labs-experimental-data-bottlenecks",
 "2026-09-14-a75db7__4719b81d.md": "C07_untitled-early-session-a75db7",
 "2026-09-15-387821__8f175840.md": "C08_rruff-data-and-dft-comparison",
 "2026-09-15-7c0b2b__a3da4b7e.md": "C09_data-absence-patterns-analysis",
 "2026-09-15-eea14f__0cb20509.md": "C10_recursive-intelligence-in-materials-ai",
 "2026-09-16-7feddc__41c43c5f.md": "C11_periodic-lab-xrd-research-analysis",
 "2026-09-17-bf2b0e__aba0a037.md": "C12_xrd-molecule-neural-net-distillation",
 "2026-09-18-dd3040__db35e15d.md": "C13_xrd-vs-complementary-characterization",
}
small = ["2026-09-15-384e41__e8e97633.md","2026-09-15-ec08f9__b85dcfe9.md","2026-09-16-751631__4f24a3c9.md","2026-09-17-0bcb14__53b5f1ff.md"]
for f, n in other.items():
    units[n] = parts(os.path.join(CV, f))[1]
sm = []
for f in small:
    sm.append("\n\n######## small session " + f + "\n" + open(os.path.join(CV, f)).read())
units["C14_four-tiny-sessions"] = sm
LIM = 230_000
man = []
for n, ps in units.items():
    chunks, cur, size = [], [], 0
    for p in ps:
        if size + len(p) > LIM and cur:
            chunks.append(cur); cur, size = [], 0
        cur.append(p); size += len(p)
    if cur: chunks.append(cur)
    for i, ch in enumerate(chunks, 1):
        fn = f"{n}__part{i}of{len(chunks)}.md"
        body = "\n\n".join(ch)
        open(os.path.join(SP, "corpus/convos", fn), "w").write(f"# CONVERSATION UNIT {n} — part {i} of {len(chunks)}\n# (USER = the human; ASSISTANT = Claude's visible replies. Tool output removed. 'compaction summary' = auto-summary of earlier context.)\n\n" + body)
        man.append((fn, len(body)))
for m in man: print("convo", m)
print("total convo chars", sum(m[1] for m in man), "files", len(man))
