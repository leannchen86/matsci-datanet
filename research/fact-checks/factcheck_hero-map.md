# factcheck:hero-map checked=24 findings=12

## 1 [overstated] L202
TEXT: a test nobody could game
PROBLEM: Overstated and not what the source says. Source describes ImageNet as a dataset plus a hidden-label contest plus a stable protocol. 'Nobody could game' is an absolute claim with no support in the files. Line 209 'cannot be passed by memorising' has the same absolute tone.
SOURCE: ImageNet was a dataset plus a hidden-label contest plus a stable protocol (synth/storyline.md:30)
FIX: a hidden-label test with fixed rules

## 2 [overstated] L220
TEXT: Random splits put the same paper on both sides, like splitting by scan instead of by patient.
PROBLEM: Presents same-paper leakage as the whole cause. Plan correction 17 says most of the 25.5-to-42.2 jump is unseen formulas, not memorised papers; correction 19 says holding out by chemical system still leaves the test paper in training 52.4% of the time; correction 21 says 'TE papers split at random' was never checked against a named paper. Also the synthesis source names this reason as 'exams are too easy', not purely paper leakage.
SOURCE: 17. Most of the 25.5-to-42.2 jump is unseen formulas, not memorised papers. (P2) exams are too easy. (plan/plan.md:184-188; synth/storyline.md:133)
FIX: Exams are too easy: random splits test on formulas and papers the model has already seen (mostly the same formulas, partly the same paper).

## 3 [unclear] L243
TEXT: 332 of 671</span> published “failed” superconductors were never actually made
PROBLEM: Count-of-what is loose and placement misleads. 671 is the number of entries extracted from one review paper's table of about 700 screened materials, not all published failed superconductors; and it sits under 'what do two companies reveal' though it is a separate experiment on a paper, not company data.
SOURCE: A well-known paper lists about 700 materials screened with 'no superconductivity'. In the 671 entries extracted, 332 (49.5%) are marked 'impossible to obtain the target phase' (synth/storyline.md:77; digests/C06-2of2.md:22)
FIX: Separately, in one well-known paper's list of failed superconductors, 332 of the 671 entries we extracted were never actually made.

## 4 [unclear] L243
TEXT: One headline score of 55.3% is best-of-7 on <span class="num">134</span> items; a single attempt scores about 36%.
PROBLEM: Presented as fact; sources tag the company figures as unverifiable company claims, and the more decision-relevant point (the lead over the best outside model is about 2 of 134 items, a statistical tie at plus or minus 4.3 points) is dropped. Company is unnamed so 'one headline score' is vague.
SOURCE: Periodic Labs [SOURCE, none of it verifiable] ... lead over the best outside model (about 53%) is about 2 of 134 problems with a standard error of about 4.3 points: a statistical tie (synth/storyline.md:74; digests/C07-12-13-14.md:38)
FIX: One company's self-reported 55.3% is best-of-7 on a private 134-item test (single attempt about 36%), and its lead over the best outside model is about 2 items: a tie.

## 5 [unsupported] L245
TEXT: You said “experimental first”, so this stopped.
PROBLEM: Quoted words attributed to the user are not found in the sources; the sources only paraphrase ('the user pointed out that the focus is experimental data'). Also what was parked was the simulated-database-side builds, not the question itself.
SOURCE: when the user pointed out that the focus is experimental data, all Materials-Project-side builds were parked (synth/storyline.md:32,271)
FIX: You pointed out that the focus is measured data, so the simulated-database builds were parked.

## 6 [unclear] L245
TEXT: DFT vs Experiment Debrief
PROBLEM: 'DFT' appears as a link label with no plain gloss nearby (the side-trail text says 'simulated data' but never ties it to the acronym). Check that DFT is in the end glossary; if not, gloss it.
SOURCE: DFT (density functional theory): a quantum simulation of a perfect crystal at absolute zero (synth/storyline.md:12)
FIX: Simulation (DFT) vs Experiment Debrief

## 7 [unclear] L253
TEXT: It comes with a built-in checksum and a measured lab-to-lab noise floor.
PROBLEM: Two problems. (a) 'checksum' is not explained here (it is: the efficiency score zT can be recomputed from the three other curves) and its coverage is omitted: only 13,702 of 55,422 samples are checkable. (b) The noise floor does not 'come with' the pool; it is from separate published round-robin studies on specific materials (a literature source, not measured on these 55,422 samples).
SOURCE: covers 13,702 of 55,422 samples / Alleno 2015 skutterudite round robin: S 6%, rho 8%, kappa 11%, ZT 19% [SOURCE] (plan/plan.md:145; digests/R07.md:26; synth/storyline.md:102)
FIX: A physics checksum works on 13,702 of the 55,422 samples (one reported number can be recomputed from three others), and published multi-lab studies give a lab-to-lab noise floor (6 to 19%).

## 8 [wrong] L259
TEXT: about 1,400 scans with recipes
PROBLEM: Wrong unit. 1,035 + 352 are samples / synthesis attempts, not scans. One of the two sets alone has 1,351 scans for its 1,035 samples. The hero (line 224) says 'records', so the two lines disagree.
SOURCE: Open records that pair a synthesis with its raw XRD total about 10^3 (Precursor Genome 1,035 + A-Lab GPSS 352). PG: 1,035 samples, 1,351 scans. (synth/storyline.md:63,116; synth/glossary_usermodel.md:129)
FIX: about 1,400 samples that have both a recipe and a raw scan (1,035 + 352)

## 9 [overstated] L259
TEXT: has no independent answer key
PROBLEM: Overstated. The sources say a true answer key does exist in the open: 40 scans of weighed mixtures (known-answer samples), called 'the only true answer key for XRD'. What is missing is a large or hard one, and the human labels that exist come from one editor.
SOURCE: it is the only true answer key for XRD. Dara's 40 scans are the only ones on disk. / only 167 'hard' patterns exist; all 1,216 human verifications carry one editor id (synth/glossary_usermodel.md:141; synth/storyline.md:116-117)
FIX: and its only true answer key is 40 scans of powders mixed at known weights; everything else is one analyst's or one program's opinion.

## 10 [unclear] L259
TEXT: Your own dara-conform project sits here.
PROBLEM: 'dara-conform' and the underlying program are used with no gloss of what they are (an XRD phase-naming program and the user's trust-scoring project around it). A reader skimming the map gets a bare project codename.
SOURCE: Dara comes from one research group and the trust-score tool (AIF) from another. Your project's 'shrink to the evaluation harness' rule ... (plan/plan.md:169)
FIX: Your own project (dara-conform, which adds a trust score to an automatic phase-naming program) sits here.

## 11 [overstated] L266
TEXT: of <span class="num">188</span> action items in them
PROBLEM: Missing scope. 'The reports' reads as all 10 reports; the audit covered three reports only (63 + 68 + 57).
SOURCE: An audit of 188 action items across three reports ... 3 have all four (ImageNet 2/63, atlas 0/68, TE spec 1/57) (synth/storyline.md:130; digests/C03-2of3.md:46)
FIX: of 188 action items in the three reports audited, only 3 said what, how, first step and done test

## 12 [unclear] L271
TEXT: Error lists are ready but unsent.
PROBLEM: Minor omission: sources say they are drafted and unfiled because they need the user's yes; the page hides that the blocker is the user's approval. Not wrong, but less actionable.
SOURCE: ready error lists that are unfiled because they need the user's yes (synth/storyline.md:36; digests/R10.md:54)
FIX: Error lists are drafted but unsent; sending them needs your yes.
