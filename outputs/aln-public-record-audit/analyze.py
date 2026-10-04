"""Validate this bounded evidence audit and regenerate its counts and reading table.

Uses only the Python standard library. This checks package consistency, not science.
It does not extract answers, judge source support, or score a model.
"""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read_json(name):
    return json.loads((ROOT / name).read_text())


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def location(item):
    pages = ", ".join(map(str, item["pages"]))
    return f"{item['status']} — PDF p. {pages}; {item['anchor']}"


def main():
    questions = read_json("questions.json")
    evidence = read_json("evidence.json")
    manifest = read_json("manifest.json")
    qhash = digest(ROOT / "questions.json")
    require(qhash == manifest["question_sha256"] == evidence["question_sha256"],
            "Frozen questions changed; preserve v0.1 and record an amendment.")
    require(digest(ROOT / manifest["pdf_path"]) == manifest["pdf_sha256"],
            "Source PDF no longer matches the fixed packet.")
    require(digest(ROOT / "sources/stanford-aln.txt") == manifest["text_extraction"]["sha256"],
            "Text extraction changed; document it before rerunning.")
    rows = evidence["rows"]
    qids = [q["id"] for q in questions["questions"]]
    require(len(qids) == len(set(qids)) == 16, "Expected 16 unique fixed questions.")
    require([r["id"] for r in rows] == qids, "Question and evidence rows differ.")
    allowed = {"explicit", "partial", "inferred", "not_found", "ambiguous"}
    for row in rows:
        require(row["combined_status"] in allowed, "Invalid combined status.")
        for region, page_range in [("main", range(1, 9)), ("supplement", range(9, 19))]:
            require(row[region]["status"] in allowed, "Invalid source status.")
            require(bool(row[region]["anchor"]), "Missing evidence anchor.")
            require(all(p in page_range for p in row[region]["pages"]), "Page outside its source region.")
        if row["combined_status"] == "explicit":
            require(row["answer"] is not None, "Explicit row lacks an answer.")
            require(any(row[s]["status"] == "explicit" for s in ("main", "supplement")),
                    "Combined explicit classification lacks an explicit source.")
        if row["kind"] == "unresolved":
            require(row["answer"] is None, "An unresolved value must be null, not zero or an invented value.")

    already = [r["id"] for r in rows if r["main"]["status"] == "explicit"]
    additional = [r["id"] for r in rows if r["main"]["status"] != "explicit"
                  and r["combined_status"] == "explicit"]
    unresolved = [r["id"] for r in rows if r["combined_status"] != "explicit"]
    require(len(already) + len(additional) + len(unresolved) == 16, "Buckets must partition the questions.")
    result = {
        "status": evidence["status"],
        "question_sha256": qhash,
        "evidence_sha256": digest(ROOT / "evidence.json"),
        "main_explicit": {"count": len(already), "ids": already},
        "newly_explicit_with_supplement": {"count": len(additional), "ids": additional},
        "combined_explicit_count": len(already) + len(additional),
        "still_unresolved": {"count": len(unresolved), "ids": unresolved},
        "combined_classifications": dict(Counter(r["combined_status"] for r in rows)),
        "human_reviewed_count": sum(r["human_review"] == "verified" for r in rows),
        "model_comparison": evidence["model_comparison"]["status"],
        "interpretation": "Counts of information recoverable for 16 selected questions, not accuracy, experimental reproducibility, information value, or equal-weight scientific importance."
    }
    (ROOT / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")

    lines = [
        "# Stanford AlN evidence table",
        "",
        "AI checked; human review pending. All page numbers are physical PDF pages.",
        "",
        f"**{len(already)} main-supported; {len(additional)} newly resolved by the supplement; {len(unresolved)} unresolved.** These counts concern the fixed questions, not model performance or laboratory reproducibility.",
        "",
        f"Read [the original article and supplement]({manifest['source_url']}). The pinned local copy can be restored with fetch_source.py. `not_found` means the requested detail at the requested level was not located in this packet. Related information is preserved below.",
    ]
    for q, row in zip(questions["questions"], rows):
        lines += [
            "", f"## {q['id']} {q['question']}", "",
            f"**Object:** {q['object']}. **Required:** {q['required']}", "",
            f"**Candidate answer:** {row['answer'] or 'Not found at the requested level in this source packet.'}", "",
            f"- Main: {location(row['main'])}",
            f"- Supplement: {location(row['supplement'])}",
            f"- Human review: {row['human_review']}",
        ]
        for source in ("main", "supplement"):
            if "related_context" in row[source]:
                lines += ["", f"Related {source} context: {row[source]['related_context']}."]
        if "interpretation_guard" in row:
            lines += ["", f"Interpretation limit: {row['interpretation_guard']}"]
    (ROOT / "audit-table.md").write_text("\n".join(lines) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
