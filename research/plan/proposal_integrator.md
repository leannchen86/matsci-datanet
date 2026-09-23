# Proposal through one lens: connect the threads

Lens: cross-thread integrator. I looked for contributions that join the separate lines of work and that were never on the ranked build list.

Status of everything below: a proposal. Nothing has been sent, published, downloaded or changed. Every outward-facing step is marked **NEEDS YOUR YES**.

Source tags in square brackets name the file a number came from: [storyline] = synth/storyline.md, [gaps] = synth/gaps.md, [builds] = synth/builds.md, [xrd-check] = digests/C16-xrd-session-verification.md, [late] = digests/C15-late-updates.md, [build-list] = corpus/notes/FILE_build-list.md, [late2] = late2.txt.

---

## 0. The answer in seven lines

1. The two sessions did not find two different problems. They found the same problem twice, in two kinds of data.
2. The shared problem: **how the exam is set and marked moves the score more than the contestants differ from each other.**
3. That sentence is backed by measured numbers in every thread (table in section 1). No report says it, because each report sees only its own half.
4. So do not pick "thermoelectric line" or "XRD line". Pick one product: a **fair-exam package** = one short note (the story) + one small kit of three checks (the reusable part).
5. The strongest thermoelectric results are already measured. Cash them in as the note's evidence now. Do not spend one to two months on more thermoelectric tooling first.
6. Build the XRD marking check first, because it lives inside your own project and needs no one's permission.
7. This week: make the "tricky pairs" marking table, and put it on one page next to the thermoelectric numbers you already have.

Words used above, once:
- Thermoelectric (TE): a material that turns a temperature difference into electricity. The main measured number used here is the Seebeck coefficient (volts produced per degree of temperature difference).
- XRD (X-ray diffraction): a scan of a powder. The peaks in the scan act like a fingerprint of the crystals inside. "Phase identification" means naming the crystalline ingredients (each ingredient is called a phase) from the scan. In ML terms it is multi-label classification where the label list is open-ended.
- Marking rule: the rule that decides whether a program's answer counts as right. For example, is "NiO" the same answer as "Ni1.875O2"?

---

## 1. The one story every thread tells

"The exam effect is bigger than the gap between contestants."

| Thread | How much the exam design moves the score | How far apart the contestants are | Source |
|---|---|---|---|
| XRD phase naming | The same program on the same 40 scans scores 12 of 40, 17 of 40 or 32 of 40 under three marking rules. The published figure is 38 of 40 (that run also used a different, paid reference library). | The two tools being compared score 38 of 40 and 35 of 40: three scans apart. | [xrd-check], [storyline] |
| TE property prediction | Median Seebeck error is 25.5% when test items are picked at random and 42.2% when whole papers are held out (12,222 samples from 3,015 papers). With a random pick, the test sample's paper is already in the training data 93.5% of the time. | A plain look-up of the same formula (22.9% error) beats the nearest-neighbour model (29.4%), on 3,593 samples. Even a look-up that is allowed to see the answers misses by 15.0%. | [gaps], [storyline] |
| Private AI-lab tests | The test has 134 items, so the standard error is about 4.3 points. | The claimed lead over the best outside model is about 2 of 134 items. | [storyline], [gaps] |

Why this matters for the "ImageNet moment" goal: ImageNet worked because the exam was fair and fixed, not because its labels were perfect. The table says the materials field does not yet have that, and it says so with numbers from your own experiments.

---

## 2. Four questions that work on any experimental-materials exam

Both lines already hold a measured answer to each question. This is the spine of the package.

**Q1. Is the exam leaky?** (Do near-copies of test items sit in the training data?)
- TE: 93.5% of test samples share a paper with training data; error goes 25.5% to 42.2% when papers are held out (12,222 samples, 3,015 papers) [gaps].
- Synthesis records (the Precursor Genome robot-lab ledger, 1,035 samples): holding out a starting chemical drops the score (macro-F1) from 0.53 to 0.42. Grouping by chemical system barely matters. So the right "group" differs by dataset [build-list].
- Steel strength table: 66 of 312 groups have a near-identical composition (within 0.1 wt%, i.e. percent by weight) in another group [build-list].
- XRD archives: 124 of 2,680 labelled patterns are exact copies (61 groups). All 499 patterns in one folder of the pooled opXRD collection are copies of files from the RRUFF mineral archive [build-list]. Whether copies sit on both sides of the split in your own project is still unchecked [builds].

**Q2. Is the marking rule stable?** (Does the score survive a change of marking rule?)
- XRD: 12 / 17 / 32 of 40 (above). Across 210 usable pilot rows, 63 answers are credited under the lenient rule and 18 of those 63 (28.6%) are credited only because of that rule [xrd-check].
- On 18 hand-built tricky cases the strict rule is wrong on 8 and the lenient rule is wrong on 13. The lenient rule treats Nb2O5 and Nb12O29 as the same answer [xrd-check].
- Writing the same formula in a different order (BiVO4 vs VBiO4) flips 3 of 20 verdicts. An ingredient listed twice is still marked correct in 4 of 4 and 2 of 3 cases [gaps].
- 15 of 56 rows in your pilot results carry out-of-date lenient marks [xrd-check].

**Q3. What is the best score anyone could get?** (How noisy are the answers themselves?)
- Two people reading the same published plot (digitising) agree to a median of 0.48% for Seebeck (361 comparisons over 102 specimen pairs; 15 of 361 are more than 10% apart, and those turned out to be record errors, not reading noise) [build-list], [builds].
- Same formula, same paper: median difference 12.9% (5,161 pairs). Same formula, different papers: 32.7% (21,856 pairs from 647 compositions), with opposite sign in 3,881 pairs (17.8%) [gaps].
- Published lab-to-lab comparison on one physical specimen: Seebeck 6%, resistivity 8%, thermal conductivity 11%, the combined figure of merit zT 19% [storyline; this one is from the literature, not our experiment].
- Steel table: 842 measured records were averaged into 312 rows. One row is the average of 53 records running from 1005.9 to 1605.4 MPa. Across the 160 compositions with several records the median spread is 82.7 MPa, while a standard model's error is 91.1 MPa on the averages and 116.9 MPa on the raw records. (A linear model shows no such gap, so the size of the effect depends on the model.) [gaps]

**Q4. Is the data what its label says?**
- 1,702 of 3,019 RRUFF files named "RAW" say in their own header that they were calculated, not measured (56.4%). RRUFF declares this itself; the news is that users ignore it [build-list], [xrd-check].
- 414 of the 499 copied opXRD patterns are calculated but deposited as "not simulated". This match is new and undisclosed [xrd-check].
- In a well-known table of about 700 "not superconducting" materials, 332 of the 671 extracted entries were never actually made [gaps].

---

## 3. Candidate contributions

### Candidate 1. One short research note: "Four questions to ask before trusting a materials leaderboard"
Track: cross-cutting.

- **Problem.** Ten long reports, no single story. The strongest verified findings exist only in chat notes and temporary folders [storyline]. Nobody outside can cite or rerun them.
- **What to build.** A note of at most six pages. One headline (section 1). Four short sections (the four questions), each with one number from each line and one script that reproduces it. Appendix: a frozen list of which paper IDs go in which test fold, the tricky-pairs table, and the scripts.
- **Hardening before anyone sees it.**
  - The 25.5% to 42.2% result uses a simple 5-nearest-neighbour model. Add one stronger standard model so the claim does not rest on a weak baseline.
  - State scope each time: Seebeck only; the two-reader comparison covers one database's high-performing papers only; the local XRD set-up (Dara 1.1.12 with the open reference library, candidate list capped at 80) is not the published set-up.
  - Present the RRUFF 56.4% as "declared but ignored", not as a discovery.
- **First step this week.** Day 1: copy working files out of temporary areas to a folder you choose (the corpus says the TE data and the XRD file list sit in temporary folders [builds]). Days 2-3: rerun the four headline numbers from saved files into one "reproduce table"; drop any that fail. Days 3-4: the tricky-pairs table (Candidate 3). Day 5: a one-page skeleton with the section-1 table and two figures.
- **Effort.** 1-2 weeks to a full draft.
- **Data.** All on disk according to [build-list] and [late2]: the three TE databases, your pilot results, the 40 weighed-mixture scans, RRUFF and the opXRD labelled slice. Risk: some of it is in temporary folders.
- **Needs your yes.** Nothing to write it. **NEEDS YOUR YES: posting it anywhere (publish).** **NEEDS YOUR YES: asking one TE reader and one XRD reader to check it (contact; you send it).**
- **Who benefits.** People who build or review materials benchmarks. You: it is the one document to attach to any later request to a lab.
- **Why it is smart.** Each finding alone is folklore in its own community. The missing piece is one measured, side-by-side demonstration, across two very different data types, that the exam effect beats the contestant gap. Nobody has written it because each community sees one half.
- **Biggest risk.** It reads as a grab-bag of complaints from a newcomer. Several prior-art items were found by a single checker and not re-verified [xrd-check]. Mitigation: one headline, four numbers, every one rerunnable; two domain readers before posting.
- **Done looks like.** One command per question reproduces its number from saved files; at most six pages; every number has a denominator and a scope line; the stronger TE baseline is in; your decision on posting is recorded.

### Candidate 2. The fair-exam kit: three small checks that print one "exam card"
Track: cross-cutting.

- **Problem.** Each line planned its own tool (a split generator for TE, a marking kit for XRD). They are the same product. Built apart, neither is reusable, and the later lab exam would need a third.
- **What to build.** Three scripts and a README. No framework, no configuration language, no dashboard.
  1. **Leak check.** Splits by a group column and reports how many test items have a relative in training. It must let the group differ by dataset: paper for TE, starting chemical plus furnace run for synthesis records, duplicate group plus cross-archive file hash for XRD [build-list].
  2. **Marking check.** Marks the same answers under several rules and reports the spread. For XRD it returns a tier (same / same family / different), not yes-or-no [xrd-check].
  3. **Ceiling check.** From repeated records already in the data, prints the noise levels and the best achievable score (Candidate 4).
  Output: a one-page text "exam card" per dataset with the three results.
- **Order.** Marking check first. Leak check second; it is mostly built: the paper-ID cleaner is saved with a regression test (193 / 75 / 7 shared papers after cleaning vs 183 / 26 / 4 by raw text match) [build-list]. Ceiling check third.
- **First step this week.** Same as Candidate 3 (the marking table), plus run the leak check read-only on your own project's file list (1,554 rows, 1,396 active [late2]) to see whether the 8 known duplicate pairs fall on both sides of your split.
- **Effort.** 1-2 months for all three with tests. Each piece alone is days to two weeks.
- **Data.** On disk (same sets as Candidate 1).
- **Needs your yes.** Nothing to build. **NEEDS YOUR YES: publishing the kit; offering the paper-grouped split to the existing MatFold split tool; any change inside your dara-conform project** (reading it is fine).
- **Who benefits.** Anyone releasing an experimental-materials benchmark; your own project, whose written fallback is "shrink to the evaluation harness" [late2]; the future lab exam.
- **Why it is smart.** The generic parts exist (scikit-learn's grouped split, MatFold). The non-obvious parts are ours and measured: the right group differs per dataset; nobody reports marking-rule spread; nobody prints the ceiling next to the score. One card with all three is what makes TE and XRD work feed the same thing.
- **Biggest risk.** It swells into a general "benchmark platform" nobody adopts, which is exactly what you said not to default to. Rule: a check is not called general until it has run on two real datasets from different lines.
- **Done looks like.** Each check runs with one command on two datasets and reproduces saved numbers: leak check gives 93.5% and 193 / 75 / 7 on TE and 124 copies in 61 groups on the opXRD slice; marking check gives 12 / 17 / 32 of 40; ceiling check gives 15.0% on TE and 82.7 MPa on steels.

### Candidate 3. Known-answer unit tests for any judge (program, marking rule, or LLM)
Track: XRD first, then cross-cutting.

- **Problem.** Whatever decides "is this answer right" is checked against expert opinion, or not at all. It is never checked against a truth fixed by construction.
  - One AI lab reports its LLM judge agrees with experts 74.6% of the time, while experts agree with each other 77.2% [gaps; self-reported, unverifiable]. No judge-versus-measurement number exists.
  - Another project's LLM recipe judge passes 1 of 531 submissions, and rejected recipes are never tried [storyline].
  - Your own marking code is wrong on 8 (strict) or 13 (lenient) of 18 tricky cases [xrd-check].
- **What to build.** A small folder of test cases with known right verdicts, in two layers.
  - Layer A: about 25 tricky pairs of ingredient names, each with the right verdict tier and a one-line reason. Examples already found: La(OH)3 reported as "LaO3"; NiO as "Ni1.875O2"; Nb2O5 vs Nb12O29; two crystal forms of Y2O3 [xrd-check].
  - Layer B: the 40 weighed-mixture scans (powders mixed by weight on a balance, so the recipe is the answer key and no analyst's opinion is involved), used end to end: tool output + recipe in, verdict out.
  - A runner that takes any judge (a function, or a prompt sent to an LLM) and reports how often it is wrong and in which direction (too strict or too lenient).
- **First step this week.** A spreadsheet of about 25 pairs with the verdict from each of five markers: strict formula match, lenient formula match, the standard structure-comparison function (pymatgen StructureMatcher) at default settings, the same at a tighter setting (site tolerance 0.15), and the proposed tier. Then re-mark the 40 scans with all five.
- **Effort.** Days for the table; 1-2 weeks for the runner with tests; a few more days for an optional LLM-judge run.
- **Data.** On disk: the 40 mixture scans plus 10 single-ingredient scans, your pilot results, the open reference library [late2].
- **Needs your yes.** Nothing to build. **NEEDS YOUR YES: asking one practising diffraction specialist to sign off the verdict column (contact; you send it). Publishing. Any change inside dara-conform.** Your call, not outward-facing: paying for LLM calls on public data.
- **Who benefits.** You (the fallback for your project). Anyone scoring XRD tools. Anyone using an LLM as a judge in materials.
- **Why it is smart.** It turns "LLM judges are unvalidated" from an opinion into a count, with data already on disk. It is the unit-test idea: fix the truth by construction, then test the judge. It does not die if someone else ships confidence scores for the same XRD tool, because it judges the judges, not the tool.
- **Biggest risk.** The 40 scans are easy (38 vs 35 of 40 cannot be told apart), so this tests the marker, not the tool. Say so plainly. Without a specialist, the verdict column is only our opinion. With 25-40 cases, report counts, never percentages alone.
- **Done looks like.** At least 25 pairs by 5 markers, each pair with a cited reason; the runner reproduces 12 / 17 / 32 of 40; at least one judge from outside your code is scored; a specialist has signed the verdict column (after your yes).

### Candidate 4. The "noise ladder": best achievable score from repeats you already have
Track: cross-cutting (TE and steels now; others later).

- **Problem.** Scores are reported with no ceiling. Nobody can tell whether 42.2% error is bad modelling or noisy answers. "How much does label noise matter?" is one of the questions your ten reports never settled [storyline].
- **What to build.** One script. Input: a table and its grouping columns (same figure, same paper, same formula). Output: a ladder table and figure, the "allowed to see the answers" ceiling, and a list of repeat readings more than 10% apart for re-reading (never averaging).
- **The ladder for Seebeck, already measured.** Reading the same plot twice 0.48%; same formula within one paper 12.9%; same formula across papers 32.7%; answers-known ceiling 15.0%; model under a fair split 42.2% [build-list], [gaps]. Reading: cleaner digitising would buy almost nothing; what is missing is a description of the specimen. That matches another finding: 7 of 28 proposed specimen fields exist in no source [storyline].
- **First step this week.** Half a day: draw the Seebeck ladder from saved numbers. Then rerun for resistivity (saved: 0.35 powers of ten between papers vs 0.14 within [gaps]) and for the steel table.
- **Effort.** Days to one week.
- **Data.** On disk: the three TE databases and the steel member table (842 records behind 312 rows).
- **Needs your yes.** Nothing to compute. **NEEDS YOUR YES: publishing the figure or script.**
- **Who benefits.** Benchmark builders (they get a ceiling line for free). You (it settles an open question with one figure).
- **Why it is smart.** Duplicates are normally deleted as a nuisance. Here they are free repeat measurements, and a second independent digitisation is a free label-noise estimate that nobody budgets for. The ladder separates three kinds of "noise" that the reports kept mixing.
- **Biggest risk.** The across-paper spread is not pure noise: it includes real differences between specimens. The two-reader comparison covers only one database's high-performing papers. The steel effect depends on the model. Each rung needs a line saying what it does and does not include.
- **Done looks like.** One command prints the ladder for at least two properties and two datasets and matches the saved numbers; every bar shows its denominator; each rung has its "includes / excludes" line.

### Candidate 5. Bridge to fresh answers: desk rehearsal, then a one-page request to a lab with the kit attached
Track: XRD. Needs partners for the second half.

- **Problem.** Every public answer key is either someone's opinion or already public, so there is no blind exam. In one robot-lab dataset the human and the program disagree on 316 of 343 scans, and a single editor ID is on all 1,216 checks [storyline]. The only opinion-free key is a weighed mixture, and the 40 that exist are too easy. About 385 separate powders are needed if tools score near 50%, and about 470-780 paired powders to separate two tools that are 5 points apart [xrd-check].
- **What to build.** Desk half: rebuild the 40 mixtures by adding up the single-ingredient scans, corrected for how strongly each ingredient absorbs X-rays, to prove the scoring pipeline runs end to end (about 25 minutes of compute plus about a day of coding [xrd-check]); rename files so they stop spelling out the recipe; write a one-page request with the sizing table. Partner half: a lab weighs and scans harder mixtures (four or more ingredients, minor ingredients at 1-5% by weight).
- **First step this week.** Only after Candidate 3's marker exists: run the rehearsal with the scorer frozen beforehand.
- **Effort.** Desk half 1-2 weeks. Partner half: needs partners, months.
- **Data.** Desk half on disk. Harder public weighed sets exist but are not on disk.
- **Needs your yes.** **NEEDS YOUR YES, each separately: contacting any lab (you send it); downloading public harder weighed sets as a practice exam (one of them is 1.87 GB [late2]; the others' sizes are not stated in the files I read); any purchase.**
- **Who benefits.** The whole XRD tool community. It is the piece closest to a real "ImageNet moment".
- **Why it is smart.** It ties the package together: the note is the credibility, the kit is the scoring, so the request to a lab shrinks to "weigh and scan N powders". Added-up scans are used only as a plumbing test, never as the exam.
- **Biggest risk.** No lab says yes. Added-up scans differ from real ones by about 4 times the counting noise, and the recipe read back from them is off by about 5 points even with the absorption correction [xrd-check], so the desk half proves plumbing only.
- **Done looks like.** Rehearsal runs end to end with recipe-blind file names and a scorer frozen in advance; the one-page request exists with the sizing table; your send / do-not-send decision is recorded.

---

## 4. The one thing to start this week

Make the tricky-pairs marking table (about 25 pairs by 5 markers, then re-mark the 40 weighed scans), and put it on one page beside the TE numbers you already have (section 1 table).

Why this one: it needs no approval, no download and no lab. It is the first step that the XRD session and the other lenses all reach independently. It is what your own project shrinks to if its stop rule fires. And with the TE numbers beside it, five days of work yields the first page of the note, not just a spreadsheet.

---

## 5. TE line or XRD line?

Neither as a "line". Choose the product (note + kit) and let each line supply what it is strongest at.

- TE supplies the leak and ceiling evidence, already measured on large data. Cash it in now. Do not spend one to two months on TE tooling first: another database already publishes the zT consistency filter; the split generator is mostly an existing scikit-learn function plus MatFold; the test answers are public literature values, so it would be a fair practice benchmark, not a blind exam; and the curves the checksum needs exist for only 52.4% and 47.9% of experimental samples [build-list].
- XRD supplies the marking evidence, your own project, and the only path from a desk to fresh, opinion-free answers (weighed powders).

The deciding reason is reuse. The XRD marker, the TE leak check and the ceiling check are the same three checks the later lab exam will need. Every hour goes toward that exam, and no hour goes into a single-line tool that an upstream group can make obsolete.

One decision only you can make: a Berkeley group has published a trust score on top of the same XRD tool your project extends [late2]. Your project's frozen plan says that if such a feature ships in the tool itself, the project shrinks to its evaluation harness. Whether that rule has fired is your call. Candidates 2 and 3 are useful either way.

---

## 6. Tempting things not to do

- **Automatic fixing of unit errors.** Only 85 of 266 power-of-ten errors were fixable; the measured false-fix rate is 7.2%; the rule fixed 0 of 12 proven two-curve errors [build-list]. Flag, never fix.
- **A general "benchmark platform", schema or dashboard.** Your own guardrail. The kit stays three scripts and a one-page card.
- **Treating public answers as a hidden test.** The answers for the 40 scans, the robot-lab sets and XRDBench are public [late2]. Practice exam only.
- **More easy weighed mixtures.** 38 vs 35 of 40 already cannot be told apart. The need is harder mixtures.
- **Using added-up synthetic scans as the exam.** About 5 points off even when corrected, and about 4 times the counting noise [xrd-check]. Plumbing test only.
- **Training a fast copy of the XRD simulator.** Listed as refuted [builds].
- **Expert re-labelling of public scans.** About 1,000 expert-hours [build-list], and one paper reports chemists agree pairwise only 35-70% [xrd-check; unverified prior art].
- **The "human overrules the program" test set.** No headroom: random scores 20.1%, a perfect method 21.8% [xrd-check].
- **A one-to-two-month TE benchmark before anything ships.** Public answers, a 15.0% ceiling from formula alone, and the checksum covers about half the samples.
- **Treating error reports as the strategy.** About 30 of 1,035 robot-lab samples hold a truly wrong value; 8 TE record errors are confirmed [xrd-check], [build-list]. A courtesy worth doing with your yes, not a contribution that changes the field.
- **A new standard for recording sample handling.** No lab is behind it. Also, the "scans change over time" result (105 of 136 vs 12 of 25) is confounded [gaps].
- **A sixth round of experiments before shipping anything.** The audit found 188 action items, of which 3 had a first step, an owner, a method and a done test [build-list].
- **The computed-data side.** Parked by you.

---

## 7. Everything that needs your explicit yes

- Posting the note, the kit, any table or any figure (publish).
- Asking any specialist to review, and any request to a lab (contact; you send it yourself).
- Any download, each one separately (public harder weighed sets; one is 1.87 GB).
- Any change inside your dara-conform project (reading it is fine).
- Offering code to MatFold or any other upstream project.
- Sending any error note to any data owner.
- Any purchase.

## 8. Honest limits of this proposal

- I did not rerun any number. Every figure is copied from the files listed at the top.
- Several prior-art items (the 1990 similarity levels, XRDBench details, the Berkeley trust score figures, the public weighed sets) were found by one checker and not independently re-verified [xrd-check].
- "Who is 'we'?" was never settled in the corpus [storyline]. This plan assumes one person at a desk with AI tools.
- The file sizes of two of the three public weighed sets are not stated in anything I read.
