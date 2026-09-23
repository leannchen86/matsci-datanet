# factcheck:found checked=46 findings=14

## 1 [overstated] L285
TEXT: thermoelectric records fail their own checksum by more than 50%.
PROBLEM: Denominator not explained: 13,702 is only the checkable subset of 55,422 samples. 'A free validator' also oversells: another database already publishes the same kind of filter, and automatic fixing is refuted (flag, never fix).
SOURCE: "of 13,702 checkable samples, 646 are off by more than 50%"; "covers 13,702 of 55,422 samples"; "The core check is partly published already". (plan/plan.md:119, 139, 145)
FIX: "of the 13,702 records where the check is possible (out of 55,422) are off by more than 50%." and "A free flag, not a fix; another database already ships a similar filter."

## 2 [unclear] L286
TEXT: The efficiency score zT is computed from three other measured curves
PROBLEM: Jargon check: 'checksum' and 'zT' are used on a newcomer page; zT is glossed here as 'efficiency score', acceptable only if zT is in the end glossary. 'Macro-F1' (line 357) is glossed. 'RAW'/'PROCESSED' (line 291-292) and 'opXRD'/'RRUFF' are used with only a partial gloss ('mineral database'; opXRD just 'collection'). Low priority.
SOURCE: "opXRD (an open pattern collection)"; RRUFF "(a mineral database)" (synth/storyline.md:119)
FIX: First use: "opXRD (an open pooled collection of X-ray patterns)"; "RAW = as deposited, PROCESSED = cleaned copy of the same scan".

## 3 [overstated] L298
TEXT: Usable after cleaning: 1,683 of 7,183 files.
PROBLEM: Missing denominator warning required by corrections 13 and 16: 7,183 = 3,019 RAW + 1,484 PROCESSED + 2,680 opXRD, so one RRUFF sample can count twice, and 2,680 is only the part of opXRD on disk (2,680 of 92,552), so it is a lower bound.
SOURCE: "The pool of 7,183 files adds RAW, PROCESSED and opXRD files, so one RRUFF sample can count twice." "All other opXRD counts are lower bounds (2,680 of 92,552 files)." (plan/plan.md:178, 181; plan/verify_K2_evidence.md:22)
FIX: "Usable after cleaning: 1,683 of 7,183 files on disk (that total counts some RRUFF samples twice and covers only 2,680 of 92,552 opXRD files)."

## 4 [unclear] L301
TEXT: ~0.5% vs 4.2%
PROBLEM: Headline compares two different units (a median size of disagreement vs a share of records), so it reads as nonsense to a newcomer. '~0.5%' is the best of four medians (0.48 / 0.83 / 0.57 / 0.91%); builds says 0.5-1%. Scope is missing: 361 comparisons on 102 sample pairs from one database's high-performing papers. 'Two teams' are two databases. Also 'Data-entry errors are' was judged without opening any source paper.
SOURCE: medians 0.48% / 0.83% / 0.57% / 0.91%; 15 of 361 (4.2%) differ by more than 10%; "No source paper was opened". (plan/merged.md:143, 170; synth/storyline.md:299; synth/builds.md:83, 139)
FIX: Big number "15 of 361"; text: "Two databases that read the same published plots agree to a median of 0.5-0.9%. But in 15 of 361 shared comparisons (4.2%) they differ by more than 10%, and those look like record errors (judged without opening the papers)."

## 5 [unsupported] L314
TEXT: Lab-to-lab noise on one shared sample is only 6%.
PROBLEM: This is a literature round-robin figure, not an own experiment, and the card names no source, which breaks the page's own footnote rule. It is also the figure for one property (Seebeck) only; other properties are 8%, 11%, 19%. The card never says which property the 32.7% refers to (Seebeck coefficient).
SOURCE: "[SOURCE] Between-lab spread is known: S 6%, rho 8%, kappa 11%, zT 19%" (published round robin). (synth/builds.md:139, 154; synth/storyline.md:102)
FIX: "A published multi-lab test on one shared sample found only about 6% spread for the same property (the Seebeck coefficient, voltage per degree)."

## 6 [overstated] L325
TEXT: Re-scans more than 180 days apart changed their answer in 105 of 136 cases.
PROBLEM: Baseline missing, so the number reads as pure ageing. Scans 30 days or less apart also changed in 12 of 25 (48%). Source tags the result exploratory and confounded; another cut of the same data gives 154 of 184.
SOURCE: "105 of 136 cases (77%) vs 12 of 25 (48%) at 30 days or less ... exploratory" (synth/builds.md:287, 756; synth/storyline.md:300)
FIX: "Re-scans more than 180 days apart changed their fitted answer in 105 of 136 cases (77%), against 12 of 25 (48%) for re-scans within 30 days. Exploratory."

## 7 [unclear] L331
TEXT: Of 353 usable files that do state it, 352 come from one institution.
PROBLEM: Mixed denominators. The card's big number is about RRUFF (71 of 3,019 files = 2.4%), but 353/352 are from the combined RRUFF + opXRD usable pool, and the 352 are opXRD files from one institution, not RRUFF files. A reader will think 353 RRUFF files state a wavelength. The 2.4% also lacks its count.
SOURCE: "Wavelength is stated in 71 of 3,019 files (2.4%)"; "Usable open pool ... 1,683 of 7,183 ... Only 353 state a wavelength; 352 come from one institution." (synth/builds.md:166, 190; digests/C16-xrd-session-verification.md:140)
FIX: Big number "71 of 3,019 (2.4%)"; small print "Across the whole usable pool (RRUFF plus opXRD, 1,683 files) only 353 state a wavelength, and 352 of those come from one institution."

## 8 [unclear] L351
TEXT: of test samples under a random split come from a paper that is also in the training set.
PROBLEM: Unit asserted more firmly than the source allows. The checker notes the 93.5% unit is ambiguous (papers vs rows) and asks the re-run to print both. The same checker adds that only 40.4% of test formulas are in training, which matters for the 'new formulas' story on the adjacent card.
SOURCE: "the 93.5% unit is papers/rows of the S set; the re-run should print it both per paper and per sample"; "only 40.4% of test compositions are in training, but 93.5% of test papers are". (plan/verify_K3_evidence.md:13, 34)
FIX: "Under a random split, the test item's paper is already in training 93.5% of the time (whether counted per sample or per paper is to be confirmed on re-run). Only 40.4% of test formulas are."

## 9 [overstated] L355
TEXT: X-ray side, same effect: the score drops when whole starting ingredients are held out.
PROBLEM: Correction 24 dropped: up to half of this drop is shared by a temperature-only model, so it is not all ingredient leakage. Also omits the rerun (0.49 to 0.39) and the denominator (1,035 samples). 'Same effect' is loose given the neighbouring card now says the TE jump is mostly unseen formulas, not leakage.
SOURCE: "Up to half of the synthesis-ledger score drop is shared by a temperature-only model." 0.526 -> 0.415; rerun 0.488 -> 0.394; 1,035 samples. (plan/plan.md:191 (correction 24); plan/verify_K3_evidence.md:17)
FIX: "X-ray side, similar pattern on 1,035 samples: 0.53 -> 0.42 when whole starting ingredients are held out (rerun 0.49 -> 0.39). Up to half of the drop also appears in a model that sees only temperature."

## 10 [overstated] L370
TEXT: lenient match, recomputed ... 32
PROBLEM: Correction 1 not fully respected: the page labels 32 as 'recomputed' and says 'measured by the X-ray session', but the 32 was quoted from a stored result file, not recounted (only 12 and 17 were recounted). 17 + 15 stale rows = 32 is a checker's arithmetic.
SOURCE: "The 32 was quoted, not recounted." (plan/plan.md:164; plan/verify_K1_evidence.md:15)
FIX: Label the bar "lenient match, fresh marks (quoted from a result file, not recounted)" and add "12 and 17 were recounted; 32 was not" to the small print.

## 11 [overstated] L379
TEXT: And all 1,216 human checks carry a single editor ID.
PROBLEM: Minor: source adds that the 'manual' tag sits on all 1,216 blocks although 810 of them sit on automated fits, so 'human checks' overstates how human they are. Card also drops the key reason this set is useless as a test (no headroom: random 20.1% vs perfect 21.8%).
SOURCE: "verification method 'manual' on all 1,216 blocks though 810 sit on automated fits"; "No headroom (random 20.1% vs perfect 21.8%)". (synth/builds.md:564; plan/plan.md:146)
FIX: "All 1,216 checks marked 'manual' carry one editor ID, and 810 of them sit on automated fits. One annotator versus a machine, not a gold standard."

## 12 [wrong] L383
TEXT: is the entire open set where the true answer is known by weighing the ingredients.
PROBLEM: Wrong/overstated. The plan itself lists three harder public weighed sets (a round robin with 4 and 7 ingredients, 240 two-ingredient mixtures, a spiked series); for the round robin the files back 'raw scans and answers public'. The 40 scans are the only weighed set already on disk / used, not the only one in the open.
SOURCE: Three harder weighed sets are public ... 'raw scans and answers public' ONLY for the round robin; supported for one of three, from one checker. None downloaded. (plan/plan.md:96-97, 195 (correction 26); plan/verify_K4_evidence.md:23)
FIX: "is the only weighed-answer set we have on disk. At least one harder public set (a contest round robin) seems to exist; two more are unconfirmed and none has been fetched."

## 13 [unclear] L387
TEXT: is the noise on a 134-item company benchmark whose claimed lead is about 2 points.
PROBLEM: +/-4.3 is one standard error, not a 95% band (which would be about +/-8.4); the 40-scan card next to it uses 95% intervals, so the two are not comparable. Card is company-reported and unverifiable plus arithmetic, but names no source despite the footnote rule. 8,800 is per model, unpaired.
SOURCE: "[SOURCE, none of it verifiable] ... standard error of about 4.3 points ... [OPINION, arithmetic]. Resolving a 2.1-point gap needs about 8,800 items per model unpaired." (synth/storyline.md:74; synth/builds.md:521)
FIX: "is one standard error on a 134-item private company benchmark (their own reported scores, our arithmetic); the claimed lead is about 2 points. Separating that gap would need roughly 8,800 items per model."

## 14 [overstated] L393
TEXT: Every number here came from running code on public files and was re-derived by an independent checker, except where a card names another source.
PROBLEM: Overstated on three counts. (a) The split table 25.5/42.2/46.6 was run once with no independent re-run. (b) The 32 of 40 was quoted from a result file, not recounted, and all XRD marking numbers come second-hand from one session's notes on the user's local project set-up (not public files). (c) The 6% lab-to-lab figure and the +/-4.3 / 134 / 8,800 card are literature/company figures plus arithmetic, and neither card names its source.
SOURCE: "Run once ... I found no independent re-run of this table"; "The 32 was NOT recounted ... C16 is the only source"; round robin 6% is [SOURCE]; Periodic figures are "[SOURCE, none of it verifiable]" + "[OPINION, arithmetic]". (plan/verify_K3_evidence.md:13; plan/verify_K1_evidence.md:15; plan/plan.md:164, 209; synth/builds.md:139; synth/storyline.md:74)
FIX: "Most numbers came from running code on public files; many were re-checked by a second pass. Exceptions: the split table was run once, the 32 of 40 is quoted not recounted, and the 6% and the 134-item figures come from published sources."
