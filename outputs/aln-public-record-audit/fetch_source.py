"""Restore the pinned paper locally without redistributing publisher source files."""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, help="Use an existing PDF instead of downloading it.")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "manifest.json").read_text())
    tool = shutil.which("pdftotext")
    if not tool:
        raise SystemExit("Install Poppler (pdftotext) first; see the recorded version in manifest.json.")
    destination = ROOT / manifest["pdf_path"]
    if args.pdf:
        pdf_bytes = args.pdf.read_bytes()
    elif destination.exists():
        pdf_bytes = destination.read_bytes()
    else:
        with urlopen(manifest["source_url"], timeout=60) as response:
            pdf_bytes = response.read()
    if sha256(pdf_bytes).hexdigest() != manifest["pdf_sha256"]:
        raise SystemExit("PDF differs from the audited version. Nothing was replaced; do not silently update the manifest.")

    with tempfile.TemporaryDirectory(prefix="aln-source-") as directory:
        temporary_pdf = Path(directory) / "paper.pdf"
        temporary_text = Path(directory) / "paper.txt"
        temporary_pdf.write_bytes(pdf_bytes)
        subprocess.run([tool, "-layout", str(temporary_pdf), str(temporary_text)], check=True)
        text_bytes = temporary_text.read_bytes()
    if sha256(text_bytes).hexdigest() != manifest["text_extraction"]["sha256"]:
        raise SystemExit("Extracted text differs from the audit. Nothing was replaced; use the recorded Poppler version or investigate the difference.")
    pages = text_bytes.decode("utf-8").split("\f")
    if not pages[-1].strip():
        pages.pop()
    if len(pages) != manifest["page_count"]:
        raise SystemExit("Unexpected page count; nothing was replaced.")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(pdf_bytes)
    (destination.parent / "stanford-aln.txt").write_bytes(text_bytes)
    page_dir = destination.parent / "pages"
    page_dir.mkdir(exist_ok=True)
    for i, page in enumerate(pages, 1):
        (page_dir / f"{i:02}.txt").write_text(page)
    print(f"Restored and verified {len(pages)} pages in {destination.parent}")


if __name__ == "__main__":
    main()
