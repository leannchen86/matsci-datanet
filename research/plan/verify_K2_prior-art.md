# Verify K2 ("Real or simulated?" check list for open XRD files) - lens: PRIOR ART

Date: 2026-09-18. Checker: prior-art skeptic. Web pages were read as data only. Nothing was downloaded, nobody was contacted, no file outside the scratchpad was opened.

Words used once: XRD = X-ray diffraction, a scan of a powder that shows which crystals are in it. RRUFF = a public mineral archive with XRD scans. opXRD = a pooled open collection of XRD scans from six institutions; HKUST-B is one folder in it. "Calculated" = the pattern was computed from a crystal structure on a computer, not measured on an instrument.

## Verdict: HOLDS WITH CHANGES

I tried to show that somebody has already published (a) the match between the HKUST-B folder and RRUFF, (b) a per-file "measured or calculated" list for these archives, or (c) a tool that checks a list of file IDs. I found none of the three. I did find that the general problem is known, and that one leading group measured it on its own test set and kept the calculated files anyway. So the novelty is real but narrow, and the wording of two claims has to be softened.

## What I checked, claim by claim

1. "The HKUST-B to RRUFF match is undisclosed." PARTLY.
   - The opXRD paper (arXiv 2503.05577, v1 HTML) says HKUST contributed 520 patterns: 21 in HKUST-A and 499 in HKUST-B. It describes HKUST-B as covering "ionic, atomic, and metallic crystals" taken from open-access publications and collaborating institutions. It does not name RRUFF, does not mention minerals, and does not say any pattern is calculated.
   - So the honest wording is: "the paper does not name the source archive and does not say any of these patterns are calculated". "Undisclosed" is too strong, because the paper does say the folder was gathered from outside open sources, and RRUFF is an open source.
   - Web searches for the HKUST-B / RRUFF identity returned nothing. The opXRD GitHub issue list shows one open issue (#3, "Add COD indices to the CNRS data", 23 March 2026, by an outside user); it does not mention RRUFF, duplicates or simulated data. This matches the C16 statement about the only outside issue.
   - Useful side fact: the paper says HKUST-B has 499 patterns, and the on-disk folder has 499. So for this one folder the on-disk copy is complete, even though the whole slice is only 2,680 of 92,552 files.

2. "The same group re-published 261 of them elsewhere as experimental." CONFIRMED (with one limit).
   - Hugging Face dataset card "caobin/opxrd_hkust_expdata": 1,277 "experimental" patterns, "including 261 selected, labeled experimental opXRD samples (from 499 HKUST-B dataset from opXRD)"; licence shown as Apache 2.0; the card recommends RRUFF and opXRD for benchmarking and says ground-truth accuracy "cannot be strictly guaranteed".
   - Limit: from the web I cannot tell whether any of the 261 are among the 414 calculated ones or all among the 85 measured ones (499 minus 414). Checking that needs the Hugging Face files, which is a download and needs the user's yes. Until then, say only what the card says.

3. "Eight papers use 148 to 3,002 RRUFF 'experimental' files with no ID lists." PARTLY.
   - I saw five papers with five different RRUFF subset sizes: SimXRD-4M 3,002; XQueryer 1,003; AlphaDiffract 734 (after filtering from 2,572 valid files); XDecomposer 662; RADAR-PD 291. A sixth (908 RRUFF patterns) appeared in a search snippet only; I did not open it. I did not see the "148" paper.
   - "No ID list" was judged from the paper text by a small reading model. It did not look inside each paper's code repository or supplement. The XQueryer repository has a folder of RRUFF-to-Materials-Project matching tools, which may in effect be an ID list. So do not say "no ID lists" in public until each repository has been opened by hand.
   - A safer and stronger public sentence: "five recent papers test on RRUFF subsets of 291, 662, 734, 1,003 and 3,002 files, so their scores cannot be compared".

4. "The RRUFF half is not news." CONFIRMED, and stronger than the candidate says.
   - AlphaDiffract (arXiv 2603.23367, March 2026) counts calculated entries in its own RRUFF test sets: 59 of 734 patterns used for classification (8.0%) and 55 of 240 used for regression (22.9%), and states that it keeps them and treats them as real-world data.
   - Meaning: a leading group knows, measured it, and did not remove them. Good for K2 (the share differs by subset, so people need a way to compute it for their own list). Bad for K2 (at least one group does not think it matters much).
   - SimXRD-4M calls all 3,002 RRUFF patterns experimental and does not mention calculated entries.

5. "No existing tool or list does this." CONFIRMED as far as I could search.
   - RADAR-PD built a "trusted" RRUFF subset of 291 samples, but its filter is about whether the label can be trusted (structure match within 5% on cell size, a GPT-4 comparison step, then fit-quality cut-offs). It is not a measured-versus-calculated list and I found no published ID list.
   - A Hugging Face copy of RRUFF powder data exists (AI4Spectro/rruff, 8,565 rows, Apache 2.0). Its card says it contains both computed and measured data and gives no de-duplication or flag list.
   - The opXRD Python wrapper and the xrdpattern library describe import, export and post-processing; nothing about duplicate or simulated checks in their README.
   - Generic ML tools for train/test overlap exist (for example deepchecks). They need the files themselves and know nothing about RRUFF headers or the cross-archive match, so they overlap only in spirit.

6. "Claimed users exist." PARTLY.
   - People who test on RRUFF as "experimental" clearly exist: at least five papers from 2024 to 2026.
   - Whether they will use a checker is unproven. AlphaDiffract kept its calculated files knowingly. The opXRD tracker has one open outside issue since 23 March 2026. The only certain user is the user's own project.

## Prior art table

| Item | URL | Overlap with K2 | What is left for K2 |
|---|---|---|---|
| opXRD paper | https://arxiv.org/abs/2503.05577 (HTML: https://arxiv.org/html/2503.05577v1) | Describes HKUST-B (499) as gathered from open-access publications and partner institutions | It never names RRUFF or says any are calculated; the hash match table is new |
| opXRD GitHub | https://github.com/aimat-lab/opxrd | The place a notice would go; one open outside issue (#3, 23 March 2026) | No issue about RRUFF, copies or simulated flags |
| Hugging Face re-release | https://huggingface.co/datasets/caobin/opxrd_hkust_expdata | Confirms the 261-of-499 "experimental" re-release | Does not name RRUFF; whether the 261 include calculated files is unchecked |
| AlphaDiffract | https://arxiv.org/abs/2603.23367 (HTML: https://arxiv.org/html/2603.23367v1) | Already counts calculated RRUFF entries in its own test sets (59 of 734; 55 of 240) and keeps them | No per-file list for others; no cross-archive check |
| RADAR-PD | https://arxiv.org/abs/2605.12478 (HTML: https://arxiv.org/html/2605.12478) | A curated "trusted" 291-sample RRUFF subset | Different purpose (label trust), no ID list found |
| SimXRD-4M | https://arxiv.org/html/2406.15469v2 | Uses 3,002 RRUFF patterns as "experimental", no ID list in the paper | Shows the need; not a solution |
| XQueryer | https://github.com/Bin-Cao/XQueryer | 1,003 RRUFF patterns; has a RRUFF-to-Materials-Project matching folder | May already contain an ID list; open it by hand before claiming "no list" |
| XDecomposer | https://arxiv.org/abs/2605.05866 | 662 RRUFF patterns, five-fold cross-validation, no ID list in the paper | Shows the need; not a solution |
| AI4Spectro/rruff | https://huggingface.co/datasets/AI4Spectro/rruff | A RRUFF powder copy that mixes computed and measured data | No flags, no de-duplication |
| awesome-xrd2crystal | https://github.com/Bin-Cao/awesome-xrd2crystal | A survey list that calls RRUFF "the most widely used experimental benchmark" | No file lists; shows where a pointer to K2 could live later |
| deepchecks (generic) | https://docs.deepchecks.com/stable/tabular/auto_checks/train_test_validation/plot_date_train_test_leakage_overlap.html | Generic train/test overlap checks | Not aware of these archives |

Pages I could not open: the Wiley published version of the opXRD paper (HTTP 403) and the opXRD Zenodo record (HTTP 504). So I do not know whether the journal version changed the HKUST-B description. Check that before any public note.

## Changes needed

1. Replace "undisclosed" with: "the opXRD paper does not name RRUFF and does not say any of these patterns are calculated; it says the folder was gathered from open-access publications and partner institutions".
2. Do not imply the 261 re-released files include calculated ones. State only the dataset card's words. Checking needs a download: user's yes.
3. Do not say "eight papers, no ID lists" in public yet. Either open each paper's repository by hand, or use the verified sentence about five different subset sizes (291, 662, 734, 1,003, 3,002).
4. Cite AlphaDiffract's own counts (59 of 734; 55 of 240) in the half-page note as prior art, and present the checker as "compute this share for your own list".
5. Say how K2 differs from RADAR-PD's 291-sample subset: theirs asks "is the label trustworthy", K2 asks "was this file measured at all, and is it a copy".
6. Keep K2 as a days-long side deliverable (CSV + checker + half-page note). The new part is one cross-archive table; it is not a paper and not the main contribution.
7. Add the coverage fact that HKUST-B is complete on disk (499 of the 499 the paper reports), while all other counts are lower bounds (2,680 of 92,552).
8. Licence care: the re-release shows Apache 2.0 while RRUFF shows no licence text. Publish IDs and hashes only; make no comment about licences in any notice.
9. Before any public step, read the journal version of the opXRD paper to see whether the HKUST-B wording changed.
10. Every outward step (publish CSV/tool/note, send a notice, download the Hugging Face set) stays behind the user's explicit yes.

## Smallest useful first step

Private, no approval needed: rebuild the CSV with the six requested changes and run the checker on the user's own 1,554-row list (expect 8 of 200 RRUFF rows, 0 HKUST-B rows, 8 duplicate pairs). In the same sitting, spend about an hour opening the code repositories of the five papers above by hand and write one table: paper, RRUFF subset size, ID list published yes/no, where. That table turns the weakest claim into a checked one without any download.
