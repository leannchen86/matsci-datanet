# Merged plan: five proposals reconciled into one list

Status: a merge of five proposer files (quick wins, leverage, user fit, contrarian, integrator). Nothing here is new analysis. Every number was re-checked against the synthesis files and the two late digests and carries its denominator. Nothing was sent, published, downloaded or changed.

Short names for sources: **builds** = synth/builds.md, **gaps** = synth/gaps.md, **story** = synth/storyline.md, **C15 / C16** = the two late digests, **build-list** = corpus/notes/FILE_build-list.md, **late2** = late2.txt (the XRD session's running notes). synth/critic.md did not exist when this was written.

Two words used throughout:
- **TE** = thermoelectrics [materials that turn heat into electricity; the data are property-versus-temperature curves read off plots in papers].
- **XRD** = powder X-ray diffraction [a 1-D curve of peaks from a powder; "phase identification" = naming which crystalline compounds ("phases") are in the powder, like multi-label classification of a spectrum].

---

## 1. The answer in one paragraph

All five lenses, working separately, picked the same first build: a **table of about 25 tricky answer pairs plus a small marking function for XRD answers**. Four of five put the long-run effort on the XRD side; none recommended the 1-2 month TE tooling plan as it stands. But every lens also kept the TE "exam is too easy" result as a 1-2 week deliverable, because it is already measured and only needs writing up. So the two lines are not rivals for the next two to three weeks. They only fork at the 1-2 month commitment, and that fork turns on one question only you can answer (section 4).

**Before anything else (half a day):** you name one permanent folder, and the finished pieces that sit in temporary folders are copied there with a text file of content fingerprints (hashes). At risk: the XRD usable-files list, the 21-pair script, the five-item corrections draft, and all TE data and scripts from the 14 September session (story Part 5; builds section E item 10; C16). Moving files to a folder you choose is listed as needing your go-ahead (builds section D; late2). Nothing leaves the machine.

---

## 2. The candidates (8, ranked)

### K1. Tricky-pairs table and a small marking function for XRD answers
- **Track:** XRD. **Proposed by:** all five lenses (it is the single recommendation of four of them; the quick-wins lens put it second).
- **Problem.** When a program names the compounds in a powder, someone must decide whether its answer "matches" the true answer. That rule is unwritten and home-made, and it moves the score more than the difference between programs. Your own project (dara-conform: a confidence score and a "not sure" option on top of the open phase-naming program Dara) is hit first: its marker compares chemical formulas only.
- **Evidence.**
  - Same program, same 40 scans of hand-weighed mixtures [powders mixed from known weighed ingredients, so the answer is certain]: 12 of 40 under the strict rule, 17 of 40 under the lenient rule, 32 of 40 after the matching code was corrected; the paper reports 38 of 40, but that run used a paid reference library, so part of 32-vs-38 is the library, not the rule (C16).
  - The published gap between the two programs is 38 of 40 vs 35 of 40: 7.5 points, interval 0.0 to 15.0, i.e. a tie (builds).
  - 18 of 63 lenient-correct answers (28.6%), among 210 rows, are correct only because of the lenient rule (C16).
  - On 18 hand-built tricky cases the strict rule is wrong on 8 and the lenient rule on 13; the lenient rule merges different compounds: Nb2O5 with Nb12O29 (distance 0.0139), WO3 with W18O49 (0.0373), TiO2 with Ti9O17 (0.0256) (C16).
  - Most real misses are spelling artifacts: "LaO3" for La(OH)3, "Ni1.875O2" for NiO, "V4O9.93316" for V2O5 (C16).
  - Second, independent result set: writing the formula in another order (BiVO4 vs VBiO4) flips 3 of 20 verdicts; exact-text marking gives tool A 17 and tool B 4 right, composition marking gives 18 and 7; an ingredient listed twice is still marked right in 4 of 4 and 2 of 3 cases (gaps G14; builds).
  - A popular structure-comparison function (pymatgen StructureMatcher) at default settings merges two different forms of quartz; a tighter setting (site tolerance 0.15 or less) separates them. A "same symmetry group" rule is wrong in at least 3 cases (builds; C16).
  - 15 of 56 rows in one stored results file carry out-of-date lenient marks (64 stored vs 79 recomputed, out of 260) (C16).
  - Your project's headline accuracy is 0.309 strict vs 0.745 lenient at n=55 (C16).
  - Prior-art check (one checker, NOT re-verified): "No installable grader or rule card exists"; the ideas date to a 1990 crystallography-union classification; one 2026 benchmark gives an AI judge 30% of the mark and another uses GPT-4 as judge (C16).
  - Honest limits: part of the 12-to-32 swing is a fault in one project's marker and a set-up that is not the published one (open library capped at 80 candidates); about 250 of 590 checkable scans offered two or more crystal forms yet 0 proven wrong marks came from crystal form, so the crystal-form machinery should stay small (C16).
- **What to build.** (1) One CSV of about 25 (program's answer, true answer) pairs, each with the expected verdict and a one-line plain reason. (2) One marking function that returns a tier, not yes/no: same / same compound spelled differently / same family but different crystal form / different / cannot tell. People then report a strict score and a family-level score side by side, like top-1 and top-5. (3) A runner that re-marks any results file under every rule and prints the table with a version string. Optional later: point the same runner at an AI judge to count how often it is wrong (any paid AI calls are your call). Present it as "the first runnable, tested rule card", not a new theory.
- **First step this week.** Rescue the existing 21-pair script. Add about 4 pairs (the two quartz forms, a listed-twice answer, the BiVO4 spelling case, one symmetry-group trap). Run five rules over every pair (strict formula, lenient formula, StructureMatcher default, StructureMatcher at 0.15, proposed tier). Re-mark the 40 weighed scans under each rule into one table. Count the Dara files first: the corpus gives 40, 41, 60, 61 and 70 (builds section E item 4). Read-only use of your project; no change to it.
- **Effort.** Days for the table; 1-2 weeks for the function and runner with tests. A specialist's sign-off adds calendar time outside your control.
- **Data on disk?** Yes per C16: all 40 mixture scans, 10 single-ingredient scans, the stored results and an installed Dara are on your machine. The 21-pair script is in a temporary area. No download.
- **Needs your yes.** None to build privately. CHANGE to dara-conform itself: yes. CONTACT one practising diffraction specialist to check the verdict column: yes (you send it). PUBLISH the table or function: yes. Sign-off is needed for publishing, not for using it inside your own project.
- **Who benefits.** Your project first. Then anyone comparing phase-naming programs, including the 2026 benchmarks now using AI judges.
- **Why it is smart.** It sits upstream of every XRD exam, yours or anyone's: a hidden test set is worth little if the marker alone moves the score by 20 of 40. It needs no lab, no data and no model. It is your project's own pre-written fallback ("shrink to the evaluation harness" if confidence scoring ships inside Dara; the group that makes Dara has since published a trust score on top of it, per one checker in C16). And "please look at these 25 rows and tell me where I am wrong" is the smallest credible request a newcomer can make of a specialist.
- **Biggest risk.** Modest novelty and credibility: old ideas in runnable form, and without one specialist's name the tiers are one ML person's opinion. A rule tuned on 25 hand-picked pairs can overfit them: tune on half, hold out half, ask the specialist for about 10 unseen pairs.
- **Done looks like.** One command rebuilds the pair table (25 or more pairs by 5 rules) and the 40-scan table, reproducing 12, 17 and 32 of 40 from stored files; on held-out pairs the tier rule is wrong less often than the two current rules (8 of 18 and 13 of 18 today); the 15-of-56 stale marks are listed, not silently fixed; one specialist's agreements and disagreements are recorded (after your yes).
- **Claims a skeptic should check.**
  1. The 12 / 17 / 32 of 40 figures come from stored files in your own project that THIS session did not open; C16 is the only source here.
  2. 18 of 63 (of 210 rows) depend on the lenient rule (C16).
  3. Strict wrong on 8 of 18, lenient wrong on 13 of 18, with the three named merges (C16).
  4. "No installable grader exists" rests on one unverified checker; check pymatgen, the Dara repository, the two 2026 benchmarks and the trust-score code on the web.
  5. StructureMatcher defaults merge the two quartz forms and 0.15 separates them (builds; re-runnable).
  6. Your project's frozen plan really contains the "shrink to the evaluation harness" rule, and the Dara group's trust score really exists (C16; second half web-checkable).

### K2. "Real or simulated?" check list for open XRD files, with a check-your-file-list tool
- **Track:** XRD. **Proposed by:** quick wins (its top pick), leverage, user fit, contrarian (as the one new item inside its courtesy batch).
- **Problem.** People test XRD models on files they believe are instrument measurements. Some are computer-calculated patterns and some are exact copies, and papers do not list which files they used, so nobody can check.
- **Evidence.**
  - New and undisclosed: 499 of 499 patterns in one folder (HKUST-B) of the pooled open collection opXRD have intensity values identical to files in the mineral archive RRUFF; 414 of the 499 are calculated but were deposited as "not simulated"; re-hashed by a second checker. The same group re-published 261 of them elsewhere as "experimental" (C16).
  - Eight papers use between 148 and 3,002 RRUFF "experimental" files with no list of file IDs (C16, one checker).
  - 124 of 2,680 opXRD files on disk are exact copies, in 61 groups. Usable pool: 1,683 of 7,183 files, 1,600 after removing copies; only 353 state the X-ray wavelength and 352 of those come from one institution (C16; builds).
  - NOT news, do not lead with it: 1,702 of 3,019 RRUFF "RAW" files are calculated, but their own headers say so and a March 2026 paper already notes it; a separate noise test agrees with the header on 2,928 of 3,006 files (97.4%) (C16; builds).
  - Effect on your own project is small: 0 HKUST-B rows; 8 of 200 RRUFF rows suspect (2 in the pilot); 8 duplicate pairs; its filter searches "calculat" and misses "computed"; its file list has 1,554 rows, 1,396 active. Whether a copy sits on both the training and test side is unchecked (C16; builds).
  - Other corrections from the checker: "15 conflicting labels" was overstated (9 of 20 hand-checked groups were different phases of one multi-phase sample); the "501 unlabelled files" are almost all the same 499 files, so do not count the problem twice; flagging by smoothness alone is unsafe (of 29 disputed files only 3 look calculated) (C16).
- **What to build.** (1) One CSV, one row per file: archive ID, content hash, snapshot date, exactly one category from a non-overlapping set (measured / header says calculated / identical to RRUFF file X / exact copy of Y / unlabelled), and a "what this rests on" column (header text, hash match, noise test). (2) A tiny command-line checker: give it a list of file IDs, it prints how many are calculated, copied or unlabelled. (3) A half-page note stating coverage plainly: the opXRD copy on disk is 2,680 of 92,552 files (an 88 MB slice of a roughly 1.4 GB release). Neutral wording throughout: "intensity values identical to RRUFF file X", never "copied from". Private part first: run it on your own file list and write down what changed.
- **First step this week.** After the rescue, rebuild the CSV from the saved scripts with the six changes the checker asked for, and run the tool read-only on your project's 1,554-row list. It should reproduce "8 of 200" and "0 HKUST-B rows".
- **Effort.** Days (up to one week).
- **Data on disk?** Yes per build-list ("no approval needed": RRUFF and the opXRD slice are in your own project folders). The working list itself is in a temporary area "that can vanish" (C15).
- **Needs your yes.** None to build. PUBLISH the CSV, tool or note: yes. SEND a neutral notice to the collection's maintainers: yes. CHANGE your project's filter: yours to make. Do NOT download the full 1.4 GB release (not approved, late2).
- **Who benefits.** Anyone benchmarking XRD models on these archives; authors and reviewers of the eight papers; your project as first user.
- **Why it is smart.** It is test-set de-duplication and de-contamination, an ML person's home turf; headers and hashes are facts, not domain opinions. Nobody did it because the two archives have different owners and nobody cross-hashed them. Turning a one-off finding into a checker others run on their own lists is what makes it reusable.
- **Biggest risk.** Low novelty for the RRUFF half; a touchy message for the HKUST-B half (it concerns a named group's files); the owners may not answer (the collection's only outside issue has been unanswered since March 2026, C16). RRUFF has no licence text: publish IDs and hashes only, never the files.
- **Done looks like.** Re-running gives a byte-identical CSV; every row has exactly one category and one evidence basis; the checker on your list reports 8 suspect RRUFF rows of 200, 0 HKUST-B rows and 8 duplicate pairs; the note states the 2,680-of-92,552 coverage; the public part exists only after your yes.
- **Claims a skeptic should check.**
  1. 499 of 499 identical, 414 calculated yet flagged "not simulated" (C16, re-hashed twice).
  2. "261 re-published as experimental" and "eight papers, 148 to 3,002 files, no ID lists" are single-checker findings; verify on the web before repeating them in public.
  3. The RRUFF half is already declared and already noted by others (C16), so the new part is only the cross-archive match.
  4. 124 of 2,680 copies in 61 groups; pool 1,683 of 7,183, then 1,600 (C16; builds).
  5. The on-disk slice is 2,680 of 92,552 files, so every count is a lower bound on the full release.
  6. Impact on your project: 0 / 8 of 200 / 8 pairs, read by the XRD session, not by this one.

### K3. TE "the exam is too easy": short note, one frozen test list, a leak report
- **Track:** TE (the leak report is reusable on any table). **Proposed by:** all five lenses (quick wins, leverage, user fit, contrarian; the integrator uses it as the leak half of its kit and note).
- **Problem.** TE prediction papers split data at random. Many samples come from the same paper, so the model has usually seen the test sample's paper in training, and reported errors are too optimistic. No shared fixed test list exists for this data.
- **Evidence.**
  - 12,222 samples from 3,015 papers. With a random split the test sample's own paper is in training 93.5% of the time. Median error on the Seebeck coefficient [voltage per degree of temperature difference]: 25.5% random, 42.2% with whole papers held out, 46.6% with whole chemical families held out (builds; build-list).
  - On the 3,593 held-out samples whose composition also appears in training papers, a plain same-composition lookup (22.9%) beats the nearest-neighbour model (29.4%); a lookup allowed to see the answers still misses by 15.0% (builds; the 3,593 count is in the 14 September session transcript).
  - The same formula in different papers differs by a median 32.7% across 21,856 paper pairs (647 compositions); opposite sign in 3,881 of those pairs (17.8%) (gaps G12).
  - Matching paper identifiers (DOIs) as raw text finds 183 / 26 / 4 shared papers across the three open TE databases; after cleaning the spelling, 193 / 75 / 7. Naive matching finds 26 of 75 in one pair (builds).
  - The right hold-out unit differs by dataset: in a 1,035-sample synthesis ledger, holding out a starting chemical drops the score (macro-F1) from 0.53 to 0.42 (rerun 0.49 to 0.39); in a well-known steels benchmark 66 of 312 groups have a near-copy in another group (builds).
  - Weak spots: the only model is a 5-nearest-neighbour baseline, and earlier forests were hand-written because scikit-learn was missing (builds; build-list). Test answers are published literature values, so this is a fair practice exam, never a hidden one (builds T5).
- **What to build.** Only what existing tools (scikit-learn's grouped split, the open MatFold split tool) lack: (1) the DOI cleaner and a CSV of shared DOIs (DOIs only; they are facts, not database content); (2) ONE FROZEN list of which DOIs are in the test set, with a checksum (ImageNet shipped a fixed list, not a split-making program); (3) a small leak report: for any table with a group column, print "X% of test items have a sibling in training"; (4) a note of about 4 pages with the 25.5 / 42.2 / 46.6 table, the lookup-beats-model result and the 15.0% floor; (5) an offer of a "hold out whole papers" split type to MatFold. One strong standard baseline is added BEFORE anything is frozen.
- **First step this week.** Confirm the TE data and the saved scripts survived in the 14 September session folder and copy them to the permanent folder. If they did: re-run the three-way table with one command, then add one strong standard baseline under the same split and see whether the jump survives. If scikit-learn is still missing, confirm the local install with you first.
- **Effort.** 1-2 weeks (about one week if the files survived).
- **Data on disk?** The corpus says yes (three TE databases; 55,422 samples in the largest), but in a temporary session folder (builds B1). If it has vanished, a re-download needs your yes; the download size is not stated anywhere in the files.
- **Needs your yes.** None to build if the files survived. PUBLISH the note, the DOI index or the frozen list: yes. A pull request or issue on MatFold: yes. One database (ESTM) has no licence: publish DOIs only, none of its rows.
- **Who benefits.** Authors and reviewers of TE property-prediction papers; MatFold's maintainers; anyone splitting a literature-mined table.
- **Why it is smart.** It is the classic leakage audit applied where nobody has published one, it carries the most quotable number in the files, and adoption runs through a tool people already use. The non-obvious part is the 15.0% floor: it says a better model cannot fix this, only a better description of the specimen can. It also cashes in four rounds of finished experiments instead of extending them.
- **Biggest risk.** "Random splits leak" is a familiar message, so the value is the numbers and the ready list. The jump may shrink under a strong baseline. No named outside user has asked for it, and the files do not say how many groups train on this data. No one checked whether a TE leakage audit has already been published.
- **Done looks like.** One command regenerates 25.5 / 42.2 / 46.6; the frozen list has an identical checksum on re-run; the strong-baseline row sits beside the nearest-neighbour row under all three splits; 100% of planted duplicate papers are caught with a measured false-alarm rate on shuffled data; the leak report run on the steels benchmark reproduces 66 of 312; MatFold has answered yes or no (after your yes to ask).
- **Claims a skeptic should check.**
  1. 93.5% and 25.5 / 42.2 / 46.6 on 12,222 samples / 3,015 papers rest on a 5-nearest-neighbour model only (builds).
  2. Lookup 22.9% vs model 29.4% on 3,593 samples; answers-known floor 15.0% (builds; 14 September transcript).
  3. 183 / 26 / 4 vs 193 / 75 / 7 shared papers (builds; a regression test is saved).
  4. MatFold exists, is open, and has no by-paper split type (web-checkable).
  5. The TE files are still in the temporary folder (nobody has looked since).
  6. Nobody has already published a paper-grouped leakage result for TE data (NOT checked anywhere in the corpus).

### K4. Known-answer XRD exam: desk stage now, practice exam after a download yes, hidden exam with one partner lab
- **Track:** XRD. **Proposed by:** leverage, user fit, contrarian (two of its five), integrator. (Quick wins listed the public harder sets as a trap only in the sense "not a quick win".)
- **Problem.** Almost every "right answer" for an XRD scan is one analyst's or one program's opinion. The only opinion-free answers on disk are 40 easy weighed scans, which programs nearly ace. This is the only candidate that creates trusted labels, the other half of the ImageNet goal.
- **Evidence.**
  - 38 of 40 vs 35 of 40 cannot separate two tools (interval 0.0 to 15.0); the errors sit in the 2-minute scans, the 8-minute scans are at ceiling: "needs harder items, not more items" (builds).
  - Human and program fits differ on 316 of 343 scans in the largest open ledger, all 1,216 human checks carry a single editor ID, and that set has no headroom anyway (random guessing scores 20.1%, a perfect method 21.8%); in a sister set 137 of 352 "human" files are the program's fit left unchanged (C16; builds).
  - Only 167 hard analyst-labelled patterns exist in the open (157 of 1,035 plus 10 of 352) against a bar of 270 (builds). That count did not include any weighed public set.
  - Harder weighed sets appear to be public already (each found by ONE checker, not re-verified; none on disk; all three listed "NOT approved" for download): an international round robin with 4- and 7-ingredient mixtures and minor ingredients at 1-5% by weight; 240 two-ingredient mixtures with the minor one at 2-20% (open licence, 1.87 GB); a spiked series at 0.12-4.0% by weight (open licence) (C16; late2).
  - Adding up single-ingredient scans cannot replace real mixtures: the recipe read back is off by about 15 points with a naive sum (worst 49) and about 5 with an absorption correction, and the sums differ from real scans by about 4 times counting noise. Fine as a plumbing test only (C16).
  - Sizing: 270 items give plus or minus 5 points only if accuracy is about 78% or higher; near 50% about 385 separate powders are needed; separating two tools 5 points apart needs about 470-780 paired powders (C16). An older note gives about 770 to 1,570 under other assumptions (builds).
  - Your set-up differs from the published one (open library capped at 80 candidates); 745 of 755 labels in one dataset exist only in the paid library, so some misses will be library gaps (C16; builds).
- **What to build.** Stage 1 (desk, no approval): a one-page dated protocol (which sets, which marker version from K1, which breakdowns, what "still too easy" means), then the "replay check" (rebuild the 40 mixtures by adding up single-ingredient scans, corrected for how strongly each compound absorbs X-rays, only to prove the scoring pipeline runs end to end; about 25 minutes of compute plus about a day of coding), and recipe-blind file names (today the names spell out the recipe). Stage 2 (after a download yes): run Dara on the public harder weighed sets and report accuracy by how small the minor ingredient is and by ingredient count, with counts and intervals. Call it a practice exam: the answers are public. Stage 3 (after a contact yes): a one-page request to ONE lab with a diffractometer and a balance, carrying the sizing table, a pilot size, the file-naming rule and who holds the answers; entries scored with the K1 marker on a free contest host that keeps answers private (entrants upload answers, not code, because of a 20-minute compute cap; one checker).
- **First step this week.** Write and date the one-page protocol. Do not run the replay until the K1 marker is frozen. In parallel draft (do not send) the one-page lab request.
- **Effort.** Desk stage: days to 1-2 weeks. Practice exam: 1-2 weeks after a download yes. Hidden exam: needs a partner; the files give no duration for the lab work (comparable TE lab comparisons took 4 months to about 2 years, builds), so plan in many months.
- **Data on disk?** Desk stage yes (40 mixture scans, 10 single-ingredient scans, Dara installed; 8 of the 10 singles sit on a shifted grid with longer counting, C16). Harder public sets: NOT on disk.
- **Needs your yes.** DOWNLOAD, asked one archive at a time: the 240-mixture archive (1.87 GB), the round-robin files and the spiked-series files (sizes not stated in the files). CONTACT any lab or person: yes, and you send it. PURCHASE of past contest powders (listed at $250 per unit, one checker, unverified): your decision. PUBLISH any result: yes.
- **Who benefits.** Every group building phase-naming programs; your project most of all, because a confidence score can only be checked against answers that do not depend on an analyst.
- **Why it is smart.** It turns part of "needs a lab" into "needs a download yes", along the axes that matter (small minor ingredient, more ingredients), so it is not the refuted "more easy mixtures" idea. Trusted XRD answers need ONE lab with a balance; a hidden TE exam needs at least 3 measuring labs. K1 and K2 shipped first are what make a small, exact ask from a newcomer credible. It is the one place where your lab relationships decide the outcome (an earlier session named a Taiwanese powder-diffraction beamline as a possible later route; nobody has been contacted).
- **Biggest risk.** No lab says yes. The public sets are unverified: they may be missing, in awkward instrument formats, or still too easy. A long-running human contest with weighed mineral powders already exists, so the new part is narrow: a standing, machine-marked test with hidden recipes. The honest outcome may be "this bottleneck is out of our reach", which you asked us to be willing to say.
- **Done looks like.** Desk: protocol dated before any run; replay table for the 40 mixtures with a written go / no-go. After a download yes: one table of accuracy by minor-ingredient band with counts and intervals, and a one-line verdict on whether the pooled sets can separate two tools. Lab ask: a materials person you trust can read the page in 5 minutes and name the cost and time; your send / do-not-send decision is recorded.
- **Claims a skeptic should check.**
  1. The three public harder weighed sets exist, include raw scans and answers, and carry the stated licences (one checker each; web-checkable without downloading the data).
  2. 38 of 40 vs 35 of 40 has an interval of 0.0 to 15.0 (builds).
  3. Sizing: about 385 powders near 50% accuracy; about 470-780 paired to separate tools 5 points apart (C16) vs the older 770-1,570 (builds); same arithmetic, different assumptions.
  4. Summed scans are off by about 5 points and about 4 times counting noise even with the absorption correction (C16).
  5. A hidden TE exam needs at least 3 labs while the XRD one needs one (builds; the XRD half is the proposers' reasoning, not a measured fact).
  6. Round 5 experiment 1 (the known-answer test on the 40 mixtures) has no results yet and was meant to decide go / no-go (builds section A).

### K5. "Is this difference real?" printed by every scorer, plus a noise ladder
- **Track:** cross-cutting. **Proposed by:** leverage (the is-it-real check) and integrator (the noise ladder). Merged because both answer "how much of this score is luck or noisy answers".
- **Problem.** Scores are reported with no error bar and no ceiling, so nobody can tell a real win from luck, or bad modelling from noisy answers. "How much does label noise matter" is one of the questions the ten reports never settled (story Part 4).
- **Evidence.**
  - 38 of 40 vs 35 of 40: interval 0.0 to 15.0, a tie (builds).
  - A company's private 134-item XRD test has a standard error of about 4.3 points, so 55.3% vs about 53% is about 2 of 134 items, a tie (story; gaps G22).
  - Two independent readings of the same printed TE figure differ by medians of 0.48% / 0.83% / 0.57% / 0.91% across four properties (361 comparisons, 102 specimen pairs; scope: one database's high-performing papers only); 15 of 361 (4.2%) differ by more than 10% and those were record errors, not reading noise (builds T6).
  - Same formula within one paper: median difference 12.9% (5,161 pairs); across papers 32.7% (21,856 pairs); an answers-known lookup still misses by 15.0%; the model under a fair split sits at 42.2% (gaps G12; builds).
  - Published lab-to-lab spread on one specimen: 6% / 8% / 11% / 19% for the four properties (from the literature, not our experiment) (builds B5).
  - Steels benchmark: 842 records averaged into 312 rows; median spread 82.7 MPa across 160 multi-record compositions vs model error 91.1 MPa on the averages and 116.9 MPa on raw records (gap interval 11.5-43.8; a linear model shows no gap) (gaps G3).
- **What to build.** Not a standalone note. (1) A small function that the K1 marker and the K3 leak report call by default, so every score prints with its interval and a "tie / not a tie" verdict. (2) One script that takes a table and its grouping columns (same figure, same paper, same formula) and prints a ladder: each noise level, the answers-known ceiling, the model score, and a list of repeat readings more than 10% apart to be re-read, never averaged. (3) A one-page card with the numbers above, each with denominator, source, and an "includes / excludes" line.
- **First step this week.** Half a day: write the function and test it on 38-vs-35 (must return "tie"). Draw the Seebeck ladder from saved numbers (0.48% / 12.9% / 32.7% / ceiling 15.0% / model 42.2%). No new experiments.
- **Effort.** Days to one week.
- **Data on disk?** Nothing new for the function and card. The ladder script needs the TE files and the steels member table (corpus says on disk; TE files in a temporary folder).
- **Needs your yes.** None to build. PUBLISH: yes, as part of K1 and K3 rather than on its own.
- **Who benefits.** Anyone comparing two models on these tasks; reviewers; you, as a plain yardstick for every claim in the ten reports.
- **Why it is smart.** Duplicates are normally deleted as a nuisance; here they are free repeat measurements, and a second independent reading of the same figure is a free label-noise estimate. The ladder's reading is actionable: cleaner figure-reading buys almost nothing; what is missing is a description of the specimen. It also yields the sizing table that makes a later lab request exact.
- **Biggest risk.** Misreading the rungs. The across-paper spread is not pure noise (it includes real differences between specimens); the reading-noise figure is a lower bound from a narrow slice and must not be used as a marking tolerance; the steels effect depends on the model (builds B5 notes).
- **Done looks like.** Running either scorer on two result files prints interval plus verdict; 38-vs-35 and the 134-item example both return "tie"; one command prints the ladder for at least two properties and two datasets and matches the saved numbers; every rung has its includes / excludes line.
- **Claims a skeptic should check.**
  1. The four reading-noise medians come from 361 comparisons on 102 pairs in one database's high-performing papers only (builds T6).
  2. 12.9% within a paper (5,161 pairs) vs 32.7% across papers (21,856 pairs, 647 compositions) (gaps G12).
  3. The 6 / 8 / 11 / 19% lab-to-lab figures are from a published comparison (builds cites Alleno 2015), not re-measured; web-checkable.
  4. 134 items give a standard error of about 4.3 points (own arithmetic on a company's self-reported, unverifiable numbers).
  5. Steels: 82.7 MPa median spread over 160 compositions; 91.1 vs 116.9 MPa; a linear model shows no gap (gaps G3).

### K6. Two short corrections notes holding only the certain items (drafts only)
- **Track:** cross-cutting. **Proposed by:** quick wins, user fit, contrarian. Leverage and integrator list "error reports as the strategy" as a trap, so this is capped at days and treated as a courtesy and a door-opener, not as the contribution.
- **Problem.** You hold verified lists of specific wrong values in other people's open datasets, and an unsent draft that still contains four claims your own checkers later withdrew. Sent as it stands it would cost credibility with exactly the people needed later.
- **Evidence.**
  - Synthesis ledger (1,035 robot-lab samples, open licence CC BY 4.0, 29.7 MB, paper still under review): all 8 drafted counts reproduce but only 5 items are certain: a stale copy of the target in 9 samples; negative XRD specimen masses in 19 of 991; 2 negative "recovered" masses; a weight-percent field that holds fractions (994 of 994); a formula field that drops the water from hydrates (132 samples). About 30 of 1,035 samples (about 3%) hold a truly wrong value (C16; builds O1; build-list).
  - Withdraw first: "method reads manual" (it is the default value), the 20 orphan files (18 are harmless leftovers), one quartz item whose count does not reproduce, and "not a furnace effect" (C16; builds section C).
  - The older "28% carry an error" is refuted; the strict figure is 93 of 1,035 (9.0%) (builds section C).
  - Largest TE database: 8 specific wrong curves among the 15 of 361 cross-database comparisons (4.2%) that disagree by more than 10%. No source paper was opened (builds).
  - Owners ranked by likely response: ledger authors first, the TE database second (it has a working fixes channel), opXRD third (its only outside issue unanswered since March 2026); RRUFF dropped as a target (C16).
- **What to build.** Two notes of at most one page. Every item has sample IDs, a few lines of script that reproduce it, and a tag: A = the file contradicts itself, B = the file contradicts the paper, C = a question. For the ledger, optionally a small corrections side file of your own, which its open licence allows. The ledger note goes privately to the authors, not as a public issue. You send both personally, or not at all.
- **First step this week.** Apply the four withdrawals; read the ledger's paper once so each item can be tagged A, B or C; cut the ledger note to the 5 certain items. Do not send anything.
- **Effort.** Days (time-boxed: two days).
- **Data on disk?** Ledger: yes (in your own project folder, build-list). A five-item draft with sample IDs exists in the XRD session's temporary area (C16). TE items share the temporary-folder caveat. Source-paper PDFs are not on disk.
- **Needs your yes.** SEND: an explicit yes per message, and you send it. DOWNLOAD the 8 TE source papers (listed "NOT approved", late2) would strengthen that note: yes. PUBLISH a corrections side file: yes.
- **Who benefits.** The dataset owners and their users; you, because a careful five-item note is the best introduction to a lab that will later be asked for harder test data.
- **Why it is smart.** Cutting from about thirty items to five is the lever: credibility, not volume. It is the step both sibling sessions share, so it costs nothing to the TE-versus-XRD decision.
- **Biggest risk.** Being wrong in front of the authors or their reviewers (the paper is mid-review). Hence five items, tagged, with reproduce lines, and nothing sent without a yes.
- **Done looks like.** Each note has 8 or fewer items, each with a tag, sample IDs and a reproduce line that runs; the four withdrawn claims appear nowhere; your yes or no to each note is recorded.
- **Claims a skeptic should check.**
  1. Only 5 of 8 ledger items are certain; about 30 of 1,035 samples truly wrong (C16).
  2. The four withdrawals are correct (C16; builds section C).
  3. The ledger's paper is still under review (C16; web-checkable).
  4. 8 wrong TE curves out of 15 of 361 disagreements, judged without opening any source paper (builds).
  5. The TE database has a working fixes channel (one checker, C16; web-checkable).

### K7. TE suspect list: a checker that flags and never fixes (narrow version only)
- **Track:** TE. **Proposed by:** quick wins only. Contrarian, leverage and integrator argue against it AS A PRODUCT; it is kept here in narrow form because it is the core of the main session's recommendation and its scripts already exist.
- **Problem.** TE records contain mistakes that nothing catches: wrong units, empty curves, spreadsheet formulas stored as if they were measurements. There is a free check: the headline TE score (zT) is defined by an equation from three other stored quantities, so it can be recomputed and compared, like a checksum.
- **Evidence.**
  - Of 13,702 samples where the recomputation is possible, 11,587 agree within 10% and 646 are off by more than 50%; 266 of those 646 are off by a clean power of ten (builds; gaps G1).
  - 2,622 curves contain no usable points (787 samples entirely empty); 240 Seebeck curves and 770 temperature axes are out of range (builds).
  - In a second database (ESTM) 3,853 power-factor cells and 3,310 zT cells are spreadsheet formulas, not measurements; the detector is not written yet (1-2 days) (builds; story Part 5).
  - Errors come paper by paper: 59 of 60 paper groups get one verdict. A review list exists: 633 specimens from 230 papers, 2 rows known to be mislabelled (builds).
  - Against it: a third database already publishes the same kind of filter (it kept 10,840 of 15,532 samples); the check covers 13,702 of 55,422 samples; the two curves it needs exist for 52.4% and 47.9% of experimental samples; the extra curve it would referee with is itself the single suspect in 133 of 245 cases (builds; build-list).
  - Automatic fixing is REFUTED: 85 of 266 fixable, at least 6 of those fixes wrong, measured wrong-fix rate 7.2% (interval 0-19%), 0 of 12 proven two-curve errors fixed (builds section C).
- **What to build.** Only the parts nobody else ships: a flag-only command that prints ok / flagged / cannot be checked with a reason and the rule's tolerance; the spreadsheet-formula detector; the corrected 633-row review list grouped by paper. It never edits a value. Reuse the other database's published filter rather than rewriting it.
- **First step this week.** Not this week. When its turn comes: correct the 2 mislabelled rows, write the formula detector (1-2 days), wrap the four existing scripts behind one command.
- **Effort.** 1-2 weeks for this narrow form (the build list's 1-3 months is for a fuller version; builds section E item 8).
- **Data on disk?** Same caveat as K3: the corpus says yes, in a temporary folder from 14 September.
- **Needs your yes.** None to build. SEND the list to a database owner: yes. PUBLISH: yes. DOWNLOAD source papers to confirm which number is wrong: yes.
- **Who benefits.** The three TE database maintainers and people training on their data. It improves one owner's records rather than how everyone tests.
- **Why it is smart.** The equation check needs no source paper and no domain judgement; few fields have a label checksum this cheap.
- **Biggest risk.** Low leverage and partial duplication of an existing filter. No source paper was opened, so "which number is wrong" rests on stored values. Round 5 experiment 2 (which decides the fix rule) has no results.
- **Done looks like.** On the frozen snapshot the tool reproduces 646 of 13,702 and the 266 power-of-ten cases; the formula detector reproduces 3,853 and 3,310; the review CSV has 633 rows with the 2 corrected; identical output hash on re-run.
- **Claims a skeptic should check.**
  1. 646 of 13,702 off by more than 50%; 266 a clean power of ten (builds).
  2. The other database's published filter kept 10,840 of 15,532 (builds cites arXiv 2505.19150; web-checkable) and how much of K7 it already covers.
  3. 3,853 and 3,310 formula cells in ESTM, and ESTM has no licence (gaps G8; build-list).
  4. Auto-fix refutation numbers (builds section C).
  5. The 633-row review list and its scripts still exist in the temporary folder.

### K8. One short note that tells the whole story: "the exam matters more than the contestants"
- **Track:** cross-cutting. **Proposed by:** integrator (its note plus its "one-page exam card" idea). It is packaging for K1, K3 and K5, not a separate build.
- **Problem.** Ten long reports tell no single story. The strongest verified findings exist only in chat notes and temporary folders, so nobody outside can cite or rerun them, and you cannot say in one sentence what was found.
- **Evidence.**
  - XRD: the same program on the same 40 scans scores 12, 17 or 32 of 40 under three marking rules, while the two tools being compared are 38 vs 35 of 40 apart (C16; builds). Caution: the 32 and the 38 come from different set-ups.
  - TE: 25.5% vs 42.2% median error depending on how the test set is picked (12,222 samples, 3,015 papers), while the two contestants (lookup 22.9%, model 29.4%) are closer than that (builds).
  - A company's private test: 134 items, standard error about 4.3 points, claimed lead about 2 items (story).
  - Labels that are not what they say: 414 of 499 copied patterns calculated but deposited as "not simulated" (C16); 332 of 671 entries in a published "not superconducting" table were never made (builds P4). The RRUFF 1,702 of 3,019 must be presented as "declared in the headers but ignored", not as a discovery.
  - Measured shortage of shipped things: of 188 action items in the reports, 3 had all of how / owner / first step / done test (builds W11).
- **What to build.** A note of at most six pages with one headline and four questions to ask before trusting a materials leaderboard: Is the exam leaky? Is the marking rule stable? What is the best achievable score? Is the data what its label says? One number from each line per question, one script per number. Appendix: the K3 frozen list, the K1 pair table. Optionally a one-page plain-text "exam card" per dataset printed by the K1, K3 and K5 scripts. It stays three scripts and a README: no framework, no dashboard.
- **First step this week.** Nothing separate. At the end of week 1, put the K1 five-rule table on one page beside the TE numbers already measured; that page is page one of the note.
- **Effort.** 1-2 weeks to a full draft, after K1 and K3 exist.
- **Data on disk?** Same as K1, K2, K3 and K5.
- **Needs your yes.** None to write. PUBLISH: yes. CONTACT one TE reader and one XRD reader before posting: yes, and you send it.
- **Who benefits.** People who build or review materials benchmarks; you, as the one document to attach to any later request to a lab.
- **Why it is smart.** Each finding alone is folklore inside its own community. What does not exist is one measured, side-by-side demonstration across two very different data types. Each community sees only its half; you hold both, already measured.
- **Biggest risk.** It reads as a grab-bag of complaints from a newcomer; the TE headline rests on a weak baseline; several prior-art items are single-checker. It can also swell into a "general benchmark platform", which you ruled out: a check is not called general until it has run on two real datasets from different lines.
- **Done looks like.** One command per question reproduces its number; six pages or fewer; every number has a denominator and a scope line; the stronger TE baseline is in; your publish / do-not-publish decision is recorded.
- **Claims a skeptic should check.**
  1. The XRD half compares a marking-rule swing measured on your local set-up with a tool gap from the published set-up (C16); the comparison must be worded carefully.
  2. The TE half survives a strong baseline (not yet run).
  3. The 134-item figures are the company's own and unverifiable (story).
  4. 332 of 671 "never made" (builds P4).
  5. No similar cross-domain note exists (not checked anywhere in the corpus).

---

## 3. Suggested order (desk work only until you say yes)

| When | What | Approval needed |
|---|---|---|
| Day 0 (half day) | You name a permanent folder; copy at-risk files there with hashes | your folder name / go-ahead |
| Week 1 | K1 pair table and five-rule re-marking of the 40 scans; K2 list and checker run on your own file list; K5 tie-check function | none |
| Week 2 | K3: confirm TE files, re-run the table, add one strong baseline, freeze the list; K6 drafts trimmed to certain items; K4 one-page protocol (dated) | none (a local package install may need confirming) |
| End of week 2 | One sitting where you say yes or no, item by item: publish K1/K2/K3? send K6 notes? ask one specialist about the 25 rows? download the public harder weighed sets (one archive at a time)? | all yours |
| Weeks 3-4 | K1 function and runner with tests; K4 replay check; K8 draft | none |
| After yeses | K4 practice exam; K4 lab request; K7 only if a TE database owner responds | download / contact |

This is two to three weeks of honest desk work for one person, not two.

---

## 4. Reconciling the TE recommendation and the XRD recommendation

**Statement.** For the next two to three weeks there is nothing to choose: do the shared desk steps from both lines (K1, K2, K3, plus the trimmed drafts). For the 1-2 month commitment the evidence favours the XRD line, in shrunken form: a days-long marker used inside your own project first, then a practice exam on harder weighed scans that may already be public, then a one-page request to one lab. The TE line should be cashed in as a 1-2 week note plus one frozen test list (K3), not extended into 1-2 months of tooling and a benchmark. This XRD lean is conditional on one thing only you know (the deciding question below).

**What the evidence supports.**
1. The ingredient actually missing for an "ImageNet moment" is fresh test items whose right answer is known without trusting an analyst. For XRD, one lab with a balance can make them by weighing powders, and harder weighed sets may already be public (unverified; needs a download yes). For TE, a hidden exam needs at least 3 measuring labs, the draft rulebook lacks 17 rules with 22 major and 15 minor review issues open, no pilot lab or cost estimate exists, and comparable lab comparisons took 4 months to about 2 years (builds T1, T2).
2. TE on today's data has an information ceiling that tooling cannot lift: an answers-known lookup still misses by 15.0%, the same formula differs across papers by a median 32.7%, and 7 of 28 proposed specimen-description fields exist in no source (builds B6, B7). The files themselves call the packaged TE benchmark "a fair DEV benchmark, not a blind test" because every label is a published figure (builds T5).
3. The main session's strongest argument for TE, the physics checksum, is real but partly already shipped by others and narrower than it sounds: another database publishes the same kind of filter (kept 10,840 of 15,532), the check covers 13,702 of 55,422 samples, and automatic fixing is refuted (builds B1, section C).
4. XRD has a first user today: your own project, whose headline moves from 0.309 to 0.745 (n=55) with the marking rule, and whose frozen plan names "shrink to the evaluation harness" as its fallback (C16). TE has no user, contact or project of yours.
5. What the main session gets right: TE has the most data (55,422 samples), the cleanest self-check, three overlapping databases, and its experiments are finished. That is exactly why its result should ship now as K3. "We have run enough experiments" (C15) applies to both lines.
6. Honest points against the XRD lean: part of the 12-to-32 swing is a fault in one project's marker and a non-published set-up; the 40 scans are easy; "no marker exists" rests on one unverified checker; the clean file list changes your own project very little (8 of 200 rows); no lab is secured; the public harder sets are unverified; Round 5's known-answer experiment has no result yet.
7. An asymmetry to keep in mind: the XRD shortlist went through nine adversarial checkers that evening (C16); the TE recommendation was a chat answer built on earlier verified rounds but was not itself attacked the same way. All five proposers also read the same digests, so their agreement is less independent than "five of five" sounds.

**What the two lines share.** The same first step (trim and hold the corrections drafts; rescue files), the same shape afterwards (a small verified list plus a tiny checker, then a fair exam), the same guardrails (flag, never fix; practice exam, never "hidden", when answers are public), and the same packaging (K8). The XRD marker, the TE leak report and the tie-check are the three checks any later lab exam would need, so none of the shared work is wasted whichever way the fork goes.

**The one deciding question for you.** Are you willing and able to approach ONE practising diffraction person or lab in the next few weeks: first with "please check these 25 rows", later with a one-page "weigh and scan N powders" request?
- If yes: XRD is the main line (K1, then K2, then K4), with K3 as the one-off TE deliverable.
- If no, or if nobody will look at 25 rows after about two weeks, or if a proper prior-art check finds a working marker already exists: keep K1 and K2 as internal fixes to your own project, and move the main effort to the desk-only, ML-native pieces (K3, K5, then K7), accepting that these give a fair practice exam but never a hidden one.

A second, smaller decision that does not change the first two weeks: whether the published trust score on top of Dara has triggered your project's written rule to shrink to the evaluation harness. K1 is useful either way.

---

## 5. Dropped or folded in, and why

| Item | Why |
|---|---|
| Split GENERATOR as a product | It is a standard grouped split plus an existing open tool; K3 ships a frozen list, the DOI cleaner and a leak report instead |
| Full TE "spell-checker" (1-3 months) | Core check already published by another database; covers 13,702 of 55,422; auto-fix refuted; kept only in narrow flag-only form as K7 |
| Small TE benchmark on public labels (1-2 months) | Labels are published figures, so not hidden; 15.0% floor and 32.7% spread; the files call it a development set |
| TE blind round / lab kit now | Needs at least 3 labs; 17 missing rules; no pilot lab, cost or organiser |
| "Fair-exam kit" as a 1-2 month three-check framework | Folded into K1 (marking), K3 (leak) and K5 (ceiling) with K8 as packaging; as one framework it risks becoming the platform you ruled out |
| Separate "known-answer unit tests for any judge" | Same first step and same table as K1; kept inside K1 as an optional runner for AI judges |
| Separate "practice exam" and "lab ask" candidates | Merged into K4 as stages 2 and 3 |
| Separate "contamination notice" | The 499-row table and checker live in K2; the courtesy messages live in K6 |
| Human-relabelled XRD check set / "human overruled the program" set | No headroom (20.1% random vs 21.8% perfect); one editor ID on all 1,216 checks; about 1,000 expert-hours; overlaps a published trust-score project and your own milestone |
| Summed "synthetic mixtures" as an exam | Off by about 5 points and about 4 times counting noise; kept only as a plumbing test in K4 |
| Handling-history standard, file-header proposals, table linter | Schema pitches with no lab behind them (your guardrail); the linter's main test table was archived and cannot take fixes; blank-cell meaning recoverable for 25.6% |
| Reporting RRUFF's calculated files to RRUFF | Their own headers already say so |
| Buying past contest powders | Unverified single-checker price; mentioned in K4 only as your decision |
| Anything on the computed-data side | Parked at your request |

---

## 6. Traps (combined)

1. Automatic unit fixing. REFUTED: 85 of 266 fixable, at least 6 of those wrong, wrong-fix rate 7.2% (interval 0-19%), 0 of 12 proven two-curve errors fixed. Flag, never fix.
2. Training a fast neural copy of the XRD simulator. REFUTED: simulating a pattern already takes about 0.3 ms.
3. Using datasets whose answers are public (the synthesis ledger, the 352-sample robot-lab set, the 40 weighed mixtures, the public 134-case 2026 benchmark whose answers sit in a public file with no licence and no scoring server) as a hidden test. REFUTED. Practice exam only.
4. "More" weighed mixtures of the same easy kind. REFUTED: the need is harder ones (4 or more ingredients, minor ones at a few percent by weight, short scans).
5. A fifth or sixth round of experiments before shipping anything. Only 3 of 188 action items had all the basics; the shortage is shipped things, not findings.
6. Starting the full TE benchmark or blind round now (see section 5).
7. Launching your own leaderboard, platform, dashboard, schema, ontology or lab notebook. Attach to tools people already use instead.
8. Sending the existing corrections draft as it stands (four withdrawn claims), or opening a public issue on the synthesis ledger while its paper is under review.
9. Treating error reports as the strategy. About 30 of 1,035 samples and 8 curves; a courtesy worth days.
10. Announcing "1,702 of 3,019 RRUFF RAW files are calculated" as a discovery, or quoting "28% of ledger samples have an error" (strict figure 93 of 1,035, 9.0%; truly wrong about 30 of 1,035).
11. Presenting the 12-to-32 of 40 swing as a field-wide finding. Part of it is one project's marker and a non-published set-up. Lead with that honestly.
12. Using StructureMatcher defaults or a same-symmetry-group rule as the marker; over-building crystal-form machinery that addresses 0 proven wrong marks.
13. Publishing marking rules without a specialist's sign-off, OR waiting for sign-off before using them inside your own project.
14. Flagging calculated patterns by smoothness alone (3 of 29 disputed files look calculated).
15. Downloading the full 1.4 GB opXRD release "to be complete", or any of the harder public sets without asking first, one archive at a time.
16. Re-hosting RRUFF files (no licence text), the robot-lab set's structure files (derived from a paid database), or any ESTM rows (no licence). IDs, hashes and DOIs only.
17. Using the figure-reading noise (about 0.5-1%) as a marking tolerance. It is a lower bound from a narrow slice.
18. Letting K8 become a grab-bag or a "general benchmark platform".
19. Skipping the Day 0 rescue. If the temporary folders vanish, K2's list, K1's script and all TE work stop being quick, and the TE ones need a download approval.
20. Changing files in your own project, downloading, contacting or publishing without your explicit yes; reviving the computed-data side because it holds the only documented outside request.
