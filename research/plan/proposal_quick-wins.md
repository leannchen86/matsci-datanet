# Proposal: quick wins (things one person can ship in two weeks or less, at a desk)

Lens: QUICK WINS. I looked only for work that (a) one person can finish in two weeks or less, (b) uses only data the reports say is already on disk, and (c) rests on evidence that was already checked a second time. I preferred work that is "80% done as analysis but never shipped".

Every number below is copied from the synthesis files and digests, with its denominator and the file it came from. Nothing here is new analysis. Where I could not find something, I say so.

Two short-hands used throughout:
- TE = thermoelectrics (materials that turn heat into electricity; the data are curves of electrical and thermal properties against temperature, read off plots in papers).
- XRD = powder X-ray diffraction (you shine X-rays on a powder and get a 1-D pattern of peaks; "phase identification" means naming which crystalline substances are in the powder, like multi-label classification of a spectrum).


## The one-paragraph answer

You have run four rounds of experiments and shipped nothing outward yet. At least five pieces are finished as analysis and need only packaging. The best one to start this week is the "real or simulated?" list of open XRD files with a tiny checker. It has been verified twice, its data sit in your own permanent project folders, its working manifest sits in a temporary folder that can vanish, and its first user is your own dara-conform project. In week 2, do the TE "exam is too easy" report. Both can be built without anyone's approval. Publishing or sending anything needs your explicit yes; I mark that on every item.


## Day 0 (half a day, before anything else): rescue the working files

Problem. Several finished pieces live in temporary folders that the computer can delete: the XRD usable-files manifest, the XRD session's 21-pair "tricky pairs" script and its five-item corrections note, the TE data and scripts (in a session folder from 14 September), the unsent corrections draft, and the 633-row TE review list. The offer to move them to a permanent folder was made before and never answered (source: storyline.md Part 5; builds.md section E).

Artifact. One permanent folder that you name, with a copy of each file and a text file of content hashes (a hash is a fingerprint that proves a file has not changed).

Approval needed. You must name the folder. Nothing leaves your machine.

Why it matters for quick wins. If those files vanish, three of the five items below stop being quick. The TE items would then need a fresh download, which needs your yes.


## Candidate 1. "Real or simulated?" list of open XRD files, plus a check-your-file-list tool (track: XRD)

What is broken, for whom. People train and test XRD models on files they believe are real measurements. A large share of those files are computer-calculated patterns (drawn from a crystal structure by software, with no instrument noise), or exact copies of each other. Anyone who reports accuracy on "experimental" data from these sources may be reporting accuracy on simulations.

Evidence (all [OWN-EXPERIMENT], reproduced by a second independent checker in the XRD session).
- 1,702 of 3,019 files (56.4%) that the RRUFF mineral archive calls "RAW" say in their own header that the profile is calculated. A separate noise test agrees with the header on 2,928 of 3,006 files (97.4%). (builds.md; round-4 verdicts)
- 499 of 499 patterns in one folder (HKUST-B) of the pooled archive opXRD have intensity values identical to RRUFF RAW files. 414 of those 499 are calculated but were deposited as "not simulated". The second checker re-hashed this independently. (C16)
- 124 of 2,680 opXRD files on disk are exact duplicates, in 61 groups. (C16)
- Usable pool: 1,683 of 7,183 files, falling to 1,600 after removing duplicates. Only 353 of those state the X-ray wavelength (a setting you need to interpret the pattern), and 352 of the 353 come from one lab. (C16)
- Eight published papers use between 148 and 3,002 RRUFF "experimental" files and give no list of file IDs, so nobody can check which were calculated. The same group that deposited HKUST-B re-published 261 of those files elsewhere as "experimental". (C16)

Honest limits the checker found. The RRUFF calculated status is written in RRUFF's own headers, so that part is "not news", only unnoticed. The HKUST-B match is new and undisclosed. "15 conflicting labels" was overstated: 9 of 20 hand-checked groups were just different phases of one multi-phase sample. The effect on dara-conform itself is small: 0 HKUST-B rows, 8 of 200 RRUFF rows suspect (2 in the pilot), and 8 duplicate pairs. A smoothness-only test for "calculated" is unsafe: of 29 disputed files only 3 look calculated. (C16)

The shippable artifact.
1. One CSV, one row per file: RRUFF ID or opXRD path, content hash, snapshot date, one category from a non-overlapping set (measured / header says calculated / identical to RRUFF file X / exact duplicate of Y / unlabelled), and a "basis of evidence" column (header text, hash match, or noise test).
2. A tiny command-line checker: you give it a list of file IDs, it prints how many are calculated, duplicated or unlabelled.
3. A one-page note that states coverage plainly: the opXRD copy on disk is a sparse 88 MB slice (2,680 of 92,552 files), not the full 1.4 GB release.
4. Neutral wording throughout: "intensity values identical to RRUFF file X", never "copied".

First step this week. Day 0 rescue, then rebuild the CSV from the saved scripts with the six changes the checker asked for (the list above), and run the checker tool against dara-conform's own file list as the first test case.

Effort. Days, up to one week.

Data on disk. Yes. The RRUFF files and the opXRD slice are in your dara-conform and direction-probes project folders (build-list "no approval needed"). The manifest itself is in a temporary area.

Approval needed. None to build. Publishing the CSV and tool needs your yes. Changing dara-conform's own filter (it searches for the word "calculat" and misses "computed", per C16) is a change to your project, so that is yours to make or approve.

Who benefits. Anyone benchmarking XRD models on RRUFF or opXRD; the eight papers' readers; dara-conform first.

Why it is smart. It is the XRD version of "de-duplicating the test set". It costs days, needs no domain judgement (headers and hashes are facts, not opinions), and it is the natural polite first contact with the labs you will need later for a harder test set.

Biggest risk. Low novelty for the RRUFF half, and a touchy message for the HKUST-B half. The neutral wording and the evidence column are the mitigation. RRUFF has no licence text, so publish IDs and hashes only, never the files.

Done looks like. Re-running the build gives a byte-identical CSV; every row has exactly one category and one evidence basis; the checker run on dara-conform's list reports the same 8 suspect RRUFF rows and 8 duplicate pairs the XRD session found.


## Candidate 2. Tricky-pairs table: how the marking rule changes the XRD score (track: XRD)

What is broken, for whom. When an XRD tool names the substances in a powder, someone must decide whether its answer "matches" the true answer. There is no agreed marking rule, and the choice of rule moves the score more than the choice of tool does. Anyone comparing phase-identification tools is affected, including dara-conform, whose marker compares chemical formulas only.

Evidence.
- Same tool (Dara, an open phase-identification program), same 40 easy scans of hand-weighed mixtures (the only case where the true answer is known for certain): 12 of 40 correct under a strict rule, 17 of 40 under a lenient rule, 32 of 40 after the matching code was corrected, against 38 of 40 in the paper (the paper run also used a paid reference library, so part of that gap is the library). (C16)
- The gap between the two tools in the paper is 38 of 40 against 35 of 40: a paired difference of 7.5 points with an interval of 0.0 to 15.0. The marking-rule swing is larger than the tool gap. (builds.md)
- Of 63 answers credited as correct under the lenient rule (out of 210 rows), 18 (28.6%) are correct only because of the lenient rule. (C16)
- On 18 hand-built tricky cases the strict rule gets 8 wrong and the lenient rule gets 13 wrong. The lenient rule treats Nb2O5 and Nb12O29 as the same substance, and WO3 and W18O49, and TiO2 and Ti9O17. (C16)
- A popular structure-comparison function (pymatgen StructureMatcher) at default settings merges two different forms of quartz; a tighter setting (site tolerance 0.15 or less) separates them. A "same space group" rule (space group = the symmetry class of a crystal) is wrong in at least 3 cases. (C16)
- Spelling the same formula differently (BiVO4 or VBiO4) flips 3 of 20 verdicts. (builds.md)
- 15 of 56 rows in one stored results file carry out-of-date lenient marks (64 stored against 79 recomputed, out of 260). (C16)

The shippable artifact. One CSV of about 25 tricky pairs, one row per pair, with the verdict each of five rules gives: strict formula, lenient formula, StructureMatcher default, StructureMatcher at the tighter setting, and a proposed three-level answer (same / same family / different) instead of yes/no. Plus a one-page note with the 12 / 17 / 32 / 38 of 40 table. 21 of the 25 pairs already exist as a script in the XRD session's work area.

First step this week. Rescue the 21-pair script, add about 4 pairs (the quartz forms, a duplicated-phase answer, a formula-spelling case), run the five rules, write the CSV.

Effort. Days for the CSV and note. One to two weeks if you also wrap the rules as a small installable marker with tests (this is the XRD session's recommended build, the "fair marking kit").

Data on disk. Yes: the 40 mixture scans, the stored results and the pair script. No download needed.

Approval needed. None to build. Two outward steps each need your yes: asking one practising diffraction specialist to sign off the proposed tiers (that is contacting someone), and publishing.

Who benefits. Every XRD phase-identification comparison; dara-conform directly. Its pre-registered fallback if Dara ships its own confidence feature is "shrink to the evaluation harness", and this is the first brick of that harness.

Why it is smart. It sits upstream of every XRD exam. A hidden test set built later is worth little if the marker can swing the score by 20 of 40. It needs no lab, no new data and no model.

Biggest risk. The ideas are old (a 1990 crystallography-union report already discusses them). Present it as "the first executable, tested rule card", not as a new theory. Without a specialist's sign-off the proposed tiers are one ML person's opinion.

Done looks like. CSV of 25 or more pairs by 5 rules committed with a test that re-derives every verdict; the note reproduces 12, 17 and 32 of 40 from stored files; the stale 15 of 56 marks are listed, not silently fixed.


## Candidate 3. TE "the exam is too easy" report, with a shared-paper index and a paper-grouped split tool (track: TE)

What is broken, for whom. TE machine-learning papers split their data at random. Many samples come from the same paper, so the model has usually seen the test sample's paper during training. Reported errors are therefore too optimistic. Anyone who builds or reviews a model that predicts TE properties from composition is affected.

Evidence (all [OWN-EXPERIMENT], on 12,222 samples from 3,015 papers and 2,419 chemical systems; sources: builds.md, C03, R07).
- Under a random split the test sample's own paper is in the training set 93.5% of the time.
- Median error on the Seebeck coefficient (the voltage a material gives per degree of temperature difference) goes from 25.5% with a random split, to 42.2% when whole papers are held out, to 46.6% when whole chemical families are held out.
- On the 3,593 held-out samples whose composition also appears in training papers, a plain lookup of the median for that composition (22.9% error) beats the nearest-neighbour model (29.4%). Even a lookup that is allowed to see the answers still misses by 15.0%, because the same formula made in different papers differs by a median 32.7% (21,856 paper pairs), and in 3,881 of those 21,856 pairs (17.8%) even the sign differs.
- To hold out papers across the three open TE databases you must first know which papers they share. Matching the paper identifier (DOI) as a raw string finds 183 / 26 / 4 shared papers (first database pair / second pair / all three); after cleaning up the DOI spelling it is 193 / 75 / 7. So naive matching finds 26 of 75 in one pair.

The shippable artifact.
1. A CSV of shared paper identifiers across the three databases (DOIs only, which are facts, not the databases' content).
2. A small command-line tool that takes a table with a DOI column and writes paper-grouped and chemical-family-grouped splits with a reproducible hash. Build it on the existing tools (scikit-learn GroupKFold and the MatFold split package) and offer the "group by paper" split back to MatFold.
3. A two-page note with the 25.5 / 42.2 / 46.6 table, the lookup-beats-model result and the 15.0% floor.

First step this week. Confirm the TE data and the saved baseline and DOI-cleaning scripts survived (they are in a session folder from 14 September). If yes, re-run the baseline to reproduce the table and freeze the hash.

Effort. About one week.

Data on disk. The reports say yes, but in a temporary session folder from 14 September. If it has vanished, re-downloading needs your yes. I could not find the download size in the files I read.

Approval needed. None to build. Publishing the note, the index or a MatFold contribution needs your yes. One of the three databases (ESTM) has no licence, so publish DOIs only and none of its rows.

Who benefits. Authors and reviewers of TE property-prediction papers; the MatFold maintainers; your own later TE benchmark if you ever build it.

Why it is smart. This is the classic ML leakage audit, which is your home turf, applied where nobody has done it. The 15.0% floor is the non-obvious part: it says a better model cannot help and only a better description of the specimen can. Your own TE report (digest R07) calls it "a clean, publishable demonstration".

Biggest risk. "Random splits leak" is a familiar message; the value is in the numbers and the ready-to-use tool, not the idea. Also, the baseline is a simple nearest-neighbour model; a critic will ask for one stronger model.

Done looks like. The tool reproduces the 25.5 / 42.2 / 46.6 table; the split manifest hash is identical on a re-run; 100% of planted duplicate papers are caught, with a stated false-alarm bound (build-list "done when").


## Candidate 4. TE suspect list: a checker that flags and never fixes (track: TE)

What is broken, for whom. TE records contain mistakes that nothing catches: wrong units, empty curves, spreadsheet formulas stored as if they were measurements. There is a free check nobody runs: the headline TE score (zT) is defined by an equation from three other stored quantities, so you can recompute it and compare, like a checksum.

Evidence ([OWN-EXPERIMENT]; builds.md, storyline.md, round-4 verdicts).
- Of 13,702 samples where the recomputation is possible, 11,587 agree within 10% and 646 are off by more than 50%. 266 of those 646 are off by a clean power of ten (a unit slip).
- 2,622 curves contain no usable points (787 samples are entirely empty). 240 Seebeck curves and 770 temperature axes are outside physically sensible ranges.
- In the ESTM database, 3,853 power-factor cells and 3,310 zT cells are spreadsheet formulas, not measurements, and are not marked as such. The detector for this is not written yet (1 to 2 days).
- Comparing the same sample across two databases: 15 of 361 comparisons (4.2%) disagree by more than 10%, and 8 of those are record errors in the largest database.
- Errors come paper by paper: in 59 of 60 paper groups every flagged sample gets the same verdict. So review effort is per paper, not per sample.
- A review list already exists: 633 specimens from 230 papers. Two of its rows are known to be mislabelled and must be corrected first.
- Do not add automatic fixing. That was tested and refuted: only 85 of 266 power-of-ten cases were fixable, at least 6 of those fixes were wrong, and 0 of 12 proven two-curve errors were fixed (builds.md section C).

The shippable artifact. A small command-line checker that reads a TE record and prints flags with a reason and the rule's tolerance (three states: ok / flagged / cannot be checked). Plus the corrected 633-row review CSV grouped by paper. It suggests; it never edits.

First step this week. Correct the 2 mislabelled rows in the review list, write the spreadsheet-formula detector (1 to 2 days), and wrap the four existing analysis scripts behind one command.

Effort. One to two weeks. (One report says 1 to 3 months for a fuller version; the two-week figure is for the flag-only tool on existing scripts. builds.md section E notes this inconsistency.)

Data on disk. Same caveat as Candidate 3: reports say yes, in a temporary folder from 14 September.

Approval needed. None to build. Sending the list to a database owner or publishing it needs your yes.

Who benefits. The three TE database maintainers and anyone training on their data. The largest one has a working channel for fixes (C16).

Why it is smart. The equation check needs no access to the source paper and no domain judgement, so an ML person can run it with confidence. Few fields have a label checksum this cheap.

Biggest risk. No source paper was opened, so "which number is wrong" rests on stored values only. A flag-only tool is honest about that; a fixing tool would not be. Round 5 (still running, no results in the files I read) is testing a fix rule; this candidate does not depend on it.

Done looks like. The tool reproduces 646 of 13,702 and 266 power-of-ten cases on the frozen snapshot; the formula detector reproduces 3,853 and 3,310; the review CSV has 633 rows with the 2 corrected.


## Candidate 5. Two short corrections notes, each with a script that reproduces the problem (track: cross-cutting)

What is broken, for whom. You hold verified lists of specific wrong values in other people's open datasets, and an unsent draft. The draft also contains four claims that your own checkers later withdrew. Sent as it stands, it would cost you credibility with exactly the labs you need later.

Evidence (C16 for the synthesis ledger; builds.md and round-4 verdicts for TE).
- Synthesis ledger (Precursor Genome: 1,035 samples, open licence CC BY 4.0, its paper still under review). The second checker found only 5 items are certain: a stale copy of the target in 9 samples; negative XRD specimen masses in 19 of 991; 2 negative "recovered" masses; a weight-percent field that holds fractions (sums to 1.0 in 994 of 994) where the documentation shows a percent; and a formula field that drops the water from hydrates in 132 samples. About 30 of 1,035 samples (about 3%) hold a truly wrong value.
- Withdraw four earlier claims before sending anything: "method reads manual" (it is a default value, not an error), the 20 orphan files (18 are harmless leftovers), one quartz item whose count does not reproduce, and "not a furnace effect".
- TE: 8 specific wrong curves in the largest TE database (Celsius stored as kelvin twice, a sign flip, a power of ten, conductivity filed as Seebeck, two curves swapped, a squeezed temperature axis). No source paper was opened for these.
- An older headline, "28% of ledger samples carry an error", is refuted. The strict figure is 93 of 1,035 (9.0%), and truly wrong values are about 3%.

The shippable artifact. Two short notes (one per dataset owner), each item tagged A (the file contradicts itself), B (the file contradicts the paper) or C (a question), each with sample IDs and a few lines of script that reproduce it. For the ledger, also a small "corrections" side file of your own, which the CC BY 4.0 licence allows.

First step this week. Apply the four withdrawals to the draft; read the ledger's paper once so that every item can be tagged A, B or C; cut the note to the 5 certain items.

Effort. Days.

Data on disk. Yes for the ledger (29.7 MB in your own project folder). TE items share the temporary-folder caveat.

Approval needed. Your explicit yes for every send, and you send it yourself. Note that the ledger's paper is under review, so a public issue would be visible to its reviewers; a private message to the authors is the gentler route. Opening the 8 TE source papers would strengthen that note; downloading them needs your yes.

Who benefits. The dataset owners and their users; you, because a careful five-item note is the best introduction to a lab you will later ask for harder test data.

Why it is smart. A short, reproducible, polite note is cheap to write, is rare, and is a door-opener. The order of owners by likely response: the ledger authors first, the TE database second (working fixes channel), opXRD third (its only outside issue has been unanswered since March 2026). RRUFF is dropped as a target because its headers already declare the calculated files.

Biggest risk. Tone and timing. Anything overstated will be remembered. Hence five items, not thirty.

Done looks like. Each note has 8 or fewer items, each with a tag, IDs and a reproduce line that runs; the four withdrawn claims appear nowhere; nothing is sent until you say yes.


## Also finished, but not on either main line

A cleaned table of "never made" negative examples for superconductors (332 of 671 entries never actually made) is done and validated two ways. I left it out because its file lives in another session's temporary area, its payoff test needs two downloads (358 KB and 9.46 MB) and your yes, and it is not TE or XRD.


## TE or XRD? My view

For the next two weeks the choice is a false one. Both lines' quick wins take two weeks or less and have the same shape: a small verified list plus a tiny checker. Doing Candidate 1 and 2 (XRD) and Candidate 3 (TE) is about three weeks of desk work in total. The real fork only appears at the one-to-two-month commitment.

At that fork I lean XRD, for three reasons, in order of weight:
1. A first user exists. Your dara-conform project already needs a clean file list and a fair marker, and its own written fallback is to become the evaluation harness. On the TE side there is no user yet.
2. In XRD the input contains the answer: the pattern really does determine which substances are present. In TE, a model that sees only the composition has a 15.0% floor even with the answers known, and 7 of 28 specimen-description fields that would lower the floor exist in no source (builds.md). So a TE benchmark on today's data mostly measures missing information.
3. The marking-rule swing (12 / 17 / 32 / 38 of 40) is bigger than the gap between tools (38 against 35 of 40). Fixing the marker is upstream of any XRD exam, and it is desk work.

What to do with TE: ship Candidate 3 (and 4 if there is time) as one-off contributions, because they are nearly done and useful on their own. Do not commit one to two months to the full TE benchmark until someone outside responds. By the reports' own account that benchmark would be a fair development set, not a blind test, and a blind round needs at least three labs.

One honest caveat against my own lean: the XRD checker found that the clean list changes dara-conform itself very little (8 suspect rows of 200, 8 duplicate pairs). Its value is mainly to other people and as a door-opener, not to your own results.

A practical tie-breaker: the XRD data sit in your permanent project folders. The TE data sit in a temporary folder from 14 September.


## Traps: tempting things not to do

- Automatic unit fixing. Refuted: 85 of 266 fixable, at least 6 wrong, 0 of 12 proven errors fixed.
- Training a fast neural copy of the XRD simulator. Refuted (builds.md section C).
- Using datasets whose answers are already public (the ledger, the 352-sample robot-lab set, the 40 mixtures, XRDBench) as a hidden test. Refuted: the answers are downloadable.
- Collecting "more" weighed mixtures of the same easy kind. Refuted: the need is harder ones (four or more substances, minor ones under 10% by weight, short scans), and that needs a lab.
- A fifth round of experiments before shipping anything. The main session's own words: "We have run enough experiments."
- Starting the TE benchmark or a blind round now. It has open design issues and needs at least three labs.
- A metadata standard, schema, dashboard or lab notebook with no lab behind it. This is your own guardrail.
- A human-relabelled XRD check set. The checker weakened it: on the ledger, random guessing scores 20.1% and a perfect method 21.8%, so there is no room to show anything.
- Downloading the full 1.4 GB opXRD release "to be complete". State the coverage of the slice instead.
- Sending the existing corrections draft as it stands. It contains four withdrawn claims.
- Reporting RRUFF's calculated files to RRUFF as an error. Their headers already say so.
- Flagging "calculated" patterns by smoothness alone. Of 29 disputed files only 3 look calculated.
- Using StructureMatcher defaults or "same space group" as the marker. Both are shown wrong on named cases.
- Re-hosting the robot-lab set's crystal-structure files or RRUFF files. The first derive from a paid database; the second has no licence.
- Anything on the computed-data (Materials Project) side. Parked at your request.
- Quoting "28% of ledger samples have an error". The strict figure is 9.0%, truly wrong about 3%.
- Treating the harder public weighed mixtures as a quick win. The XRD session's prior-art search found public sets with 4 and 7 ingredients and minor phases at 1 to 5% by weight (an international round robin from 2001-2002), and 240 two-phase mixtures (2023, CC BY 4.0). They are worth a look later as a harder practice set, but they are not on disk, so they need a download and your yes, and their answers are public, so they can never be a hidden test.


## Suggested two-week calendar

- Day 0: name a permanent folder; rescue files; write hashes.
- Days 1 to 4: Candidate 1 (XRD list and checker), tested on dara-conform's file list.
- Day 5: Candidate 5 paperwork only: apply the withdrawals, tag the 5 items. Do not send.
- Days 6 to 8: Candidate 2 (tricky-pairs CSV and the 12 / 17 / 32 / 38 note).
- Days 9 to 10: Candidate 3 first step: confirm the TE files survived; reproduce the table; freeze the hash.
- End of week 2: you decide, item by item, what to publish or send. Nothing goes out before that.
