# measurement-science

## is eval work: mostly
EVAL: - D1 is a unit-test file for a scoring rule, with a draft answer key. That is metric validation.
- D4 is the statistics of comparisons (tie or not).
- D3 is split design: a leak report and a frozen test list.
- D6 is a survey of candidate test sets.
- N1 implements the metric.
- N3 is a practice exam with bands fixed in advance.
- N4 is the best-achievable-score ladder. Metrology calls this the repeatability to reproducibility ladder.
- N5 is a reader's checklist for leaderboards.
- L1 is an expert review of the answer key.
- L2 is a hidden test set.
- L5 is a thermoelectric lab comparison.
- The first step (the 40-row test) is eval work of the most basic kind. It checks the marker before trusting any mark.

In the older field's words, D1, N1 and L1 set the assessment criteria. D4 is proficiency-test scoring. N3, L2 and L5 design the proficiency test. N4 is a precision study.
NOT: - D0 (file rescue) is housekeeping.
- D2 (499 files that look simulated but are filed as measured) is a data provenance audit. It touches eval in one place only: whether a duplicate pair sits on both sides of the calibration/test split.
- D5, L3 and L4 (error notes and a neutral notice) are error reporting to dataset owners.
- N6 (thermoelectric suspect list) is data quality flagging.
- The critique of one company's 134-item result is secondary reading of someone else's eval. Only its arithmetic (one standard error of about 4.3 points) is eval method.
- The partner-lab part of L2 (weighing, mixing, scanning, checking purity) is reference-material production. In a real proficiency test most of the organiser's effort goes there, not into scoring code.
NAME: Checking the exam before trusting the scores: answer keys, marking rules, splits and error bars for ML on measured materials data. Metrology calls this method validation and proficiency-test design.

## scorecard
- [partly] [BEFORE-STEP-1] P1 Say exactly what is being measured
  EVID: - plan/plan.md:7 defines the task as naming phases: "Think multi-label classification".
- plan/plan.md:29 asks for "three formula-level marks per scan". It never says what one mark means: all true phases named, or are extras allowed?
- plan/plan.md:110 (N3) says "report accuracy by how small the minor ingredient is". There is no task card.
- plan/plan.md:97 (D6) lists the row fields (raw scans, weighed answers, licence, powders, format, size). "What task was this set built for" is not among them.
  GAP: No single place states the task, naming level, wt% range, sample type, instrument and inputs given. The IUCr quantification round robin told entrants which phases were present (stage-1 reading of the 1998 letter; the page returned 403 to me). Re-using those scans for naming is a new use of that key, and the card should say so. Without a written mark definition, 12, 17 and 32 of 40 cannot be interpreted.
  FIX: Put a 6-line task card at the top of the 40-row table:
- Task: name phases only.
- One mark: the stored code's rule, written in words.
- Naming level: formula only.
- The wt% range of the 40 mixes.
- Sample: weighed mixtures, 3 phases or fewer, one instrument, 2- and 8-minute scans.
- Inputs: element list given; local open library capped at 80 candidates; Dara version.

Also add a D6 column: "original task: were phases given to entrants? yes/no". (20-30 minutes)
- [violates] P2 The answer key needs its own check
  EVID: - plan/plan.md:9: "Its right answer is certain and needs no analyst's opinion."
- plan/plan.md:127: "certain answers, but a one-instrument exam". The one-page request lists only "how many powders, pilot size, file-naming rule ... who holds the answers".
- page/big-picture.html:618: "answer comes from a balance, not from an analyst". Line 623: "One lab gives certain answers".

The notes already saw this failure mode. synth/gaps.md:109 records hydrate formulas that differ between two fields. synth/builds.md:565 records a README saying "equal weight" while the file names encode 10-90 wt%.
  GAP: - No purity scan of each ingredient.
- No independent check of the mix.
- No uncertainty on any weight fraction.

The Reynolds Cup (page re-opened in this run) requires purity known within 1 wt% and checks its splits by XRD and XRF. A bought chemical with 3% of a second phase really shows that phase, so a correct tool gets marked as a false positive. NIST's alumina standard is about 99% crystalline (stage-1 source), so weighed fraction and crystalline fraction differ by up to a few percent.
  FIX: - Replace "certain" with "known to within ingredient purity and weighing error" in the glossary, in L2 and on the page.
- Add three asks to the L2 one-pager: a scan of each ingredient lot; one bulk-chemistry check (such as XRF) on a random subset; a stated uncertainty per wt%.
- For the 40 scans, use the 10 single-ingredient scans already on disk (synth/gaps.md:208) as the purity check, if the stored results include them. Flag any ingredient whose own scan shows a second phase. (Wording 10 min; purity look 1-2 hours inside the first step; L2 lines 15 min)
- [partly] P3 No ranking inside the key's error
  EVID: - plan/plan.md:91: the function "prints an interval and a 'tie / not a tie' verdict ... 38 of 40 vs 35 of 40 must return 'tie'".
- plan/plan.md:78 labels the key "AI-drafted, not yet reviewed by a specialist" and words the figures as "disagrees with the draft key". That is the right instinct.
- page/big-picture.html:499: "The 40 scans are really 20 powders, each scanned twice."
  GAP: The tie function handles sampling error only. It has no input for the key's own error rate. The notes do not say whether the interval resamples 20 powders or 40 scans. The Reynolds Cup does this by rule: entries inside the mixtures' uncertainty are not separated on the main score.
  FIX: Give D4 two optional inputs:
- key_error_rate. While it is unknown, print "key unreviewed, no ranking claim".
- cluster ids, so the interval resamples powders, not scans.

Any "rule A is off on k of 18" line keeps the "draft key" wording until L1. (1-2 hours on top of D4)
- [not_yet_relevant] P4 Prove the test items are uniform and stable
  EVID: plan/plan.md:127 (L2): a one-page request for "about 385 separate powders". It has no line on homogeneity (are splits of one powder alike) or stability (does the powder change before scanning). The first step uses existing scans, so this does not apply yet.
  GAP: - In small hand-mixed powders, a 1 wt% ingredient may be only a few grains in the beam, so its peaks are a lottery (particle statistics).
- Many oxides, hydroxides and carbonates take up water or CO2 from air, so the recipe drifts.
- The usual proficiency-test limit is a between-split spread of at most 0.3 of the scoring tolerance. This comes from a secondary explainer; the ISO 13528 text was not opened.
  FIX: Add two lines to the L2 draft:
- Re-split and re-scan a random 10% and compare against a limit set in advance.
- Record the date mixed and the date scanned, and flag air-sensitive ingredients.

Add the re-scan subset to the 385-powder sizing. (15 minutes of drafting)
- [partly] P5 Separate reading a scan from making one
  EVID: - plan/plan.md:55: "That is still a one-instrument exam".
- plan/plan.md:127: "State the limit honestly".
- plan/plan.md:198 (correction 29): "One lab is enough is reasoning, not a measured fact".

The plan states this caution and acts on it in its wording.
  GAP: No second-instrument subset is planned. N3 would draw on sets from different instruments and radiations: lab copper, lab molybdenum and synchrotron, per the stage-1 reading of the León-Reina record. Headline numbers on the 40 scans carry no "fixed scans, one instrument" label.
  FIX: - N3: report per source set and per radiation, never pooled.
- L2 one-pager: an optional 20-30 powder subset re-scanned on a second instrument.
- Add "fixed scans, one instrument" to every headline. (10 minutes of wording)
- [partly] P6 Put known physical traps in on purpose
  EVID: - plan/plan.md:110: N3's only difficulty axis is "how small the minor ingredient is".
- plan/plan.md:142: "the need is harder ones". It does not say harder in what way.
- synth/builds.md:320 defines harder as "4 or more phases, minor phases under 10 wt%, polymorph pairs, 2-minute scans".
- synth/gaps.md:210, own measurement: X-ray absorption runs from 8.4 to 261.0 cm2/g across the Dara ingredients, and summed scans are about 5 points off.

Correction to the compiled notes: they apply this principle to N4. plan/plan.md:112-113 shows N4 is a thermoelectric label-noise ladder, not an X-ray difficulty axis, so that criticism does not apply to N4.
  GAP: "Harder" means count, amount and scan time. It leaves out the systematic effects the 1998 round robin built one sample each for:
- Microabsorption: heavy grains shade themselves, so their peaks come out weak.
- Preferred orientation: flat or needle grains lie down, so some peaks are too strong.
- Non-crystalline content: glass gives no sharp peaks at all.

The user's own 40 scans already span a 30-fold absorption contrast.
  FIX: Add per-item tags to the N3 score sheet and the L2 recipe list: absorption contrast, plate- or needle-shaped ingredient, non-crystalline ingredient, poorly crystalline ingredient, scan time. Report results per tag. Optional for the first step: tag the 40 rows with absorption contrast and scan time, since those numbers already exist. (1 hour for tags; a design choice for L2)
- [partly] P7 Report detection by amount, with a floor
  EVID: - plan/plan.md:110: "Fix in advance which bands count as 'harder'" and "with counts and intervals". Both are right.
- synth/gaps.md:278 already says XRD misses minor phases below about 1 to 5 wt%. N3 does not act on it.
  GAP: No declared floor. The León-Reina series runs from 0.12 to 4.0 wt%. A careful lab study put the detection limit near 0.2 wt% on a copper source, with relative error under 20% only above 1 wt% (stage-1 reading of the 2016 abstract). Routine fast scans are worse. A low score in that band says little about the tool.
  FIX: - One line in N3: declare a floor band (below 1 wt% for routine scans, with its source). Report misses there, but do not count them against the tool.
- D6 row: add "wt% range" and "scan time". (10 minutes)
- [violates] [BEFORE-STEP-1] P8 Wrong extra phases cost as much as misses
  EVID: - plan/plan.md:29: "three formula-level marks per scan", which is one yes/no per scan.
- plan/plan.md:110: "report accuracy". No false-positive count appears anywhere in plan.md.

The notes know the risk:
- synth/gaps.md:232-234: the fit always improves when a phase is added.
- synth/gaps.md:154: "Duplicate phase entries were still marked correct in 4 of 4 and 2 of 3 cases".

Reynolds Cup page (re-opened in this run): naming absent phases is "THE biggest source of bias".
  GAP: A lenient rule can turn a long, over-reported phase list into a "correct" scan. The plan does not say whether the stored 12, 17 and 32 marks punish extras. If they do not, part of the rule effect is over-reporting, not naming.
  FIX: - Give the 40-row table four more columns per rule: true phases, named phases, missed, extra.
- Add one sentence saying whether the stored mark punishes extras.
- N3 and L2: report extras per scan separately. Include single-phase trap items; the 10 single-ingredient scans on disk are free ones. (1-2 hours, in the same pass over the data)
- [partly] [BEFORE-STEP-1] P9 Publish naming levels before the test
  EVID: Good:
- plan/plan.md:79: formula-only input "must be allowed to return 'cannot tell'".
- plan/plan.md:80: guard rows.
- page/big-picture.html:614: ask the specialist for about 10 unseen pairs as a held-out check.

Missing:
- plan/plan.md:104: tier names from the 1990 classification, with no numeric tolerances.
- plan/plan.md:30: "Hand-sort each into 'spelling artifact' or 'real chemistry disagreement'", with no written rule.
- plan/plan.md:36: the go/no-go line has no number set in advance.
  GAP: - The first step's own grading (the hand-sort) is decided after seeing the answers, by a non-specialist plus an AI, into only two bins. There is no bin for a library gap, a suspect key or "unsure".
- "Cannot tell" is treated as a property of the pair only. It also depends on scan quality: ordered vs disordered versions differ by weak extra peaks that only a long scan shows.
  FIX: Before opening the data, write:
- The sort rule in 5 lines, with bins: spelling / real chemistry / library or set-up gap / key may be wrong / unsure, needs a specialist.
- The decision number: "build the marker if at least K differing rows are real chemistry". The user picks K.

Mark the sort "draft until L1". In N1, add a numeric tolerance per tier; ICSD's rule-based structure-type procedure (Allmann and Hinek 2007, stage-1 source) is a worked model. Word the verdict as "cannot tell at this scan quality". (30 minutes)
- [partly] P10 Fix and log what the entrant was given
  EVID: - plan/plan.md:110: a per-scan flag, "were all true ingredients in the candidate list?". Right; keep it.
- plan/plan.md:164 names the reference library and local set-up as the cause of 32 vs 38.
- synth/gaps.md:213: the local install is version 1.1.12, with open pools capped at 80 candidates.

The plan has no line on whether the element list is given, and none on the database date.
  GAP: Dara searches inside a given chemical space, per its paper's abstract (search snippet seen in this run). So this exam is "elements given", which matches real synthesis work. Tools that get no elements do a harder task and cannot be compared on one number. In the 2002 naming round robin about 16% of entrants failed one sample on database age alone (stage-1 source).
  FIX: - Put it on the task card (see P1).
- Add N3 result columns: library name and date; elements given yes/no; truth in candidate list yes/no.
- Never pool across settings. (10 minutes)
- [partly] P11 Freeze settings; the operator is a variable
  EVID: - plan/plan.md:110: "Run Dara and report...". No frozen configuration is mentioned. The deliverable "is it still too easy for Dara, by band?" is true for one configuration only.
- synth/gaps.md:213: the local install "is not the published set-up".

The first step reads stored results with no per-scan human adjustment, so it is fine here.
  GAP: - No configuration hash is recorded with scores.
- No note that the public round-robin scans were used as development examples by at least one tool's authors (the 2019 full-profile search-match paper, stage-1 source). A good score there may be partly tuned-in.
  FIX: N3: one configuration file, its hash in every result row, no per-scan edits, and the line "scans public since 1999; tools may have been tuned on them". (15 minutes)
- [partly] P12 Reproduce a certified answer before building anything
  EVID: - plan/plan.md:33: the done test "reproduces 12, 17 and 32 of 40". That reproduces the project's own numbers.
- plan/plan.md:164: the published 38 of 40 is not reproduced locally (32). The gap is put down to library and set-up but is not itemised.
- D6 (plan/plan.md:97) is web-only.
  GAP: The pipeline has never been run on an externally verified item. The one external reference that exists (38 of 40 on the same scans) currently fails by 6 scans, with the cause assumed rather than shown.
  FIX: - Optional in the first step: add a column "paper's per-scan verdict" if the Dara paper or repository lists it (web look, no download). That itemises the 6-scan gap as library, set-up or marker.
- Before N3: run the pipeline once on the IUCr round-robin sample 1 supplied scans as a positive control. They are small text files with weighed values long public. The download needs the user's yes. (1 hour for the column; half a day for the control)
- [partly] P13 Weighed mixtures are the easy case
  EVID: - plan/plan.md:55: "What is truly missing ... is fresh test items whose right answer nobody has to trust an analyst for". That means weighed mixtures only.
- plan/plan.md:165 and plan/plan.md:91, the plan's own data: on 20 real reaction products the two tools differ by 11-13 of 20; on the weighed scans they tie. So the weighed set is the easy, less discriminating case.
- plan/plan.md:104: a "specialists disagree" tier, the seed of an appeal path.
- plan/plan.md:146 drops a human-relabelled set, for good reasons.
  GAP: - No "upper bound" wording.
- No plan to make recipes look like real products.
- No rule for challenging and revising a key.

Published keys have been revised before: one 2002 key was contradicted by a 2019 automatic run plus a manual check (stage-1 source).
  FIX: - One sentence in L2 and N5: "accuracy on weighed mixtures is an upper bound on accuracy on real products".
- Draw L2 recipes from real reaction-product phase lists (left-over starting chemicals plus known by-products).
- Give the D1 CSV three columns as the appeal log: disputed by / date / resolution. (20 minutes)
- [partly] P14 Fresh items each round, key holder stays out
  EVID: - plan/plan.md:127: "file-naming rule (today's file names spell out the recipe), who holds the answers". Both are right.
- plan/plan.md:141: public-answer sets are practice exams only. Right.

Missing: item retirement, entries per entrant, entrant codes, the cost of new powders each round. plan/plan.md:8: the user's own project sits on Dara, so the organiser is also a likely entrant.
  GAP: A machine exam that re-uses hidden items and takes repeated submissions leaks its key through the scores. The human contest allows one entry per organisation, makes fresh mixtures each round and keeps the organiser out of the contest (Reynolds Cup page, re-opened in this run). "Standing" therefore means new physical powders every round, and that cost is not in the 385-powder sizing.
  FIX: Add four lines to the L2 one-pager:
- The partner lab holds the key.
- The organiser's own tool is scored but reported outside the ranking.
- N submissions per entrant per round.
- Items retire when their truth is released.

Add a per-round powder cost to the sizing. (15 minutes)

## direction findings
- [low] The first step is the right kind of step, and the plan is fine here. Checking the marker before trusting any mark is what a proficiency-test organiser does before round one.
  EVID: - plan/plan.md:19-43: a 40-row table on data already on disk, a done test, two approvals, and no download or contact.
- The plan already matches older practice in five places: a tie rule (plan.md:91); a "cannot tell" verdict with guard rows (plan.md:79-80); bands fixed in advance and a truth-in-candidate-list flag (plan.md:110); public-answer sets called a practice exam (plan.md:110, 141); L2 labelled a one-instrument exam (plan.md:127).
  REC: Keep the step. Add three things before building the table, under an hour of writing in all:
- A task card that defines one mark (P1).
- Per-scan missed and extra counts (P8).
- A pre-written sort rule with five bins and a preset go/no-go number (P9).

Treat the hand-sort as a draft until a specialist sees it.
- [high] The plan puts its effort into scoring code and one line into the answer key. The older field does the opposite: the key and the physical items are the product.
  EVID: - N1 is 2-3 weeks on a marking function (plan.md:103-104). L2's key quality gets the word "certain" (plan.md:127; page/big-picture.html:618, 623).
- Reynolds Cup organiser rules (re-opened in this run): purity known within 1 wt%, a repeatable splitting procedure, and splits verified by XRD and XRF before shipping.
- The IUCr round robin cross-checked weighed values by XRF on three portions (stage-1 reading; the page returned 403 to me).
- The user's own notes already found hydrated chemicals filed under dry formulas (synth/gaps.md:109).
  REC: Reword "certain" everywhere. When L2 is drafted, make key verification its main section: ingredient scans, one independent chemistry check, an uncertainty per wt%, a homogeneity re-scan subset and a stability rule. Price all of that in. If no lab will do it, the plan's own sentence applies: "this bottleneck is out of our reach".
- [high] The long-term aim is narrower than the plan thinks. A machine scored against blind-contest weighed mixtures already exists. A standing, hidden, third-party, naming-first exam on synthesis chemistry with a published marking rule still appears open.
  EVID: - Butler and Hillier 2021, Clays and Clay Minerals 69, 38-51: an automatic algorithm run on 27 samples from nine Reynolds Cup contests, claimed accurate enough for the top three. I saw a search snippet only this run; Springer redirected to an authorisation flow, not followed. URL: https://link.springer.com/article/10.1007/s42860-020-00105-6
- Lutterotti et al. 2019 tested an automatic tool on IUCr round-robin scans and on the four 2002 naming samples (stage-1 source).
- synth/gaps.md:209 still words the novelty as "standing, machine-scored, hidden-recipe".
- Two searches in this run for a standing machine-facing blind phase-naming exam found none. That is absence of evidence.
- The GALAXI abstract (re-opened; https://arxiv.org/abs/2609.06908) reports micro-F1 0.935 on "a curated set of experimental patterns". It states no source, no count and no definition of a correct phase.
  REC: - Drop "machine-scored" from the novelty sentence.
- State the open part as: standing + hidden + third-party + naming-first + inorganic synthesis chemistry + written marking rule + a multi-label score.
- When drafting L2, weigh one alternative: offer the scoring rule, the statistics and a machine submission format to an existing round-robin body, instead of founding a scheme alone. This fits an ML person's assets better than organising powders. It means contacting people, so it waits for the user's yes.
- [medium] Weighed mixtures are the easy, less discriminating case, and the plan's own numbers show it. A weighed-only exam can end up accurate but uninformative.
  EVID: - plan/plan.md:165: on 20 real reaction products the tool gap is 11-13 of 20 and the rule effect 1-3 of 20.
- plan/plan.md:91: on the weighed scans the two tools tie.
- The Reynolds Cup page says its mixtures are built to represent realistic rock assemblages, not arbitrary recipes.
- The round robin's natural rock had no known answer at all (stage-1 source).
  REC: - Call weighed-mixture accuracy an upper bound in L2 and N5.
- Build L2 recipes to mimic reaction products: left-over starting chemicals plus known by-products, tagged for the physical traps in P6.
- Keep a small real-product arm as a later, clearly separate item. It would use a consensus key and a written way to challenge that key.
- [medium] A diffraction person will not be surprised that formula-string marking is unstable. The contribution that survives is a runnable, tested rule with numbers, not the discovery.
  EVID: - In search-match practice an answer is a database entry (structure plus cell), not a formula string. Strings such as "Ni1.875O2" and "LaO3" are the formulas of database entries (refined site occupancies; hydrogen atoms not located), per synth/gaps.md:153.
- The plan already says the ideas are old (plan.md:171, correction 8). It also says the stored results threw away the chosen reference file (plan.md:81).
- Precedents exist: the Reynolds Cup grouping spreadsheet, the 2002 lenient hand grading, and ICSD's rule-based structure types.
- From memory, not opened: ISO 13528 has only a short clause on qualitative results. I know of no standard score for a multi-label phase list.
  REC: - Keep presenting N1 as "first runnable, tested rule card".
- Borrow numeric tolerances from the ICSD 2007 procedure, not only tier names from 1990.
- The multi-label score (misses, extras, tiers, a tie rule that knows the key's error) is where an ML-minded person adds something the older field lacks. Say so in N5.
- [low] The thermoelectric noise ladder (N4) is sound by metrology standards, but it omits the one rung that is a true between-lab measurement. The compiled notes misread N4 as an X-ray noise axis.
  EVID: - plan/plan.md:113 lists five rungs: reading noise 0.48%, within-paper 12.9%, across-paper 32.7%, answers-known 15.0%, model 42.2%. It already warns that the across-paper spread "is not pure noise".
- synth/gaps.md:137 and :190 hold a round-robin figure on one specimen measured by several labs: about 6% for the Seebeck coefficient. It is cited there from the literature and was not opened in this run.
- That rung is what shows most of the 32.7% is specimen difference, not instrument noise.
  REC: Add one rung to N4: "same specimen, different labs: about 6% (published round robin)". Tag it as a literature value and give it an includes/excludes line like the others. No other change to the thermoelectric side from this lens. D3's frozen paper-ID list and leak report are fine.

## top changes
- Before building the 40-row table, write a 6-line task card: the task, what one mark means, the naming level, the wt% range, the sample type and instrument, and the inputs given (elements, library and its cap, Dara version). Also write the hand-sort rule down first, with five bins (spelling / real chemistry / library or set-up gap / key may be wrong / unsure) and a go/no-go number set in advance. About 1 hour.
- In the same table, log per scan and per rule: true phases, named phases, missed, extra. State whether the stored 12, 17 and 32 marks punish extra phases. The older field found wrongly named extra phases to be the largest error source, and a lenient rule can hide them. 1-2 hours, same pass over the data.
- Stop calling weighed answers "certain" (plan.md:9 and :127; page lines 618 and 623). Say "known to within ingredient purity and weighing error". Use the 10 single-ingredient scans already on disk as the purity check for the 40. Add to the L2 one-pager: an ingredient-lot scan, one independent chemistry check on a random subset, an uncertainty per wt%, a re-scan subset for uniformity, a storage and date rule, and the organiser's own tool reported outside the ranking.
- Narrow the novelty claim and reshape L2. A machine scored on contest weighed mixtures already exists (2019 and 2021 papers). The open part is standing + hidden + third-party + naming-first + synthesis chemistry + a published marking rule and multi-label score. Build recipes that mimic real reaction products, tag the physical traps (grain shading, flat grains, glass, poor crystallinity), and call the result an upper bound. "Standing" means new powders every round, so price that in.
- Small edits to D4, D6 and N3, all of which can wait for the week-2 sitting:
- D4: add a key-error input, and resample 20 powders rather than 40 scans.
- D6: add columns for "phases given to original entrants?", wt% range and scan time.
- N3: declare a detection floor (misses below about 1 wt% are not counted against the tool); freeze one configuration and record its hash; log the library date and whether elements were given; report per source set, never pooled; note that tool authors have already used the round-robin scans as development examples.
- Before N3: run one positive control on the IUCr sample 1 supplied scans. The download needs the user's yes.
- N4: add the published between-lab rung (about 6%).

## verdict: Proceed with changes. The first step is sound, cheap and the right kind of eval work. Make three small additions before the table is built, under an hour of writing in all: the task card, the missed/extra columns, and the pre-written sort rule with a preset decision number. Two direction-level corrections can wait for the week-2 sitting and do not block the start: the answer key is a claim with an error bar, not \"certain\"; and the long-term exam is narrower than the plan thinks.

# CHALLENGE
- [holds] (is_eval_work) is_eval_work: "mostly" ... "Checking the exam before trusting the scores"
  WHY: The split is right. D1, D4, D3, D6, N1, N3, N4, N5, L1, L2 check an exam (metric, key, split, error bars). D0, D2, D5, L3, L4, N6 are housekeeping, provenance and error reporting. Two small notes. (1) D4 is closer to a paired comparison of two methods than to proficiency-test z-scoring; the analogy is loose but harmless. (2) The precise ML name is meta-evaluation: validating the metric and the key, not running the benchmark. The audit's most useful sentence is that the partner-lab half of L2 is reference-material production, not desk eval work. That is correct and it is why L2 is further away than it reads.
  CORRECTED: 
- [holds_with_changes] (scorecard) P1 partly: "It never says what one mark means" ... 6-line task card, must fix before first step
  WHY: True for plan.md: no line defines a mark. But the definition already exists in two places the audit did not open. (a) The user's frozen pre-registration, as recorded in digests/C16-xrd-session-verification.md:29-31: strict = equal reduced formula; lenient = ignore unlocated hydrogen, same elements within distance 0.04 (two-element compounds) or 0.10, phases matched one-to-one. Stored columns are gt_phases and rank1_phases (C16:243). (b) The Dara paper (arXiv 2510.19667, HTML opened this run): only the top-ranked answer is judged; a scan is correct if it includes all weighed phases and excludes any spurious phase. So the card is a 20-minute copy job plus one look at the marker code, not a design task. The audit also missed one card line: top-ranked answer only.
  CORRECTED: Task card (copy, do not invent): Task = name phases. One mark = per scan, top-ranked answer only (column rank1_phases); strict and lenient rules quoted from the project's frozen pre-registration; confirm in code that one-to-one matching means extras make the scan wrong. Published rule for the 38 of 40 = all weighed phases present and no spurious phase, top answer only. Naming level = formula. Sample = 20 mixtures from 10 ingredients, 3 phases or fewer, 2- and 8-minute scans, one instrument. Inputs = element list given; local open library capped at 80 candidates; Dara 1.1.12.
- [holds_with_changes] (scorecard) P2 violates: "Its right answer is certain" ... use the 10 single-ingredient scans as the purity check, 1-2 hours
  WHY: The verdict holds and is stronger than the audit knew. The Dara paper itself reports a real extra phase in one of the 20 mixtures (the 30 NiO / 30 Bi2O3 / 40 Li2CO3 mix shows a bismuth carbonate, put down to reaction with Li2CO3 or air during mixing). The authors chose to leave that phase out of their evaluation. That is an analyst's judgement on the key, on the very 40 scans the first step uses. So "needs no analyst's opinion" (plan.md:9) is already false for this set. The proposed first-step fix is not proportionate, though. An earlier checker (plan/verify_K1_newcomer-skeptic.md:20) already said reading the single-ingredient scans "is not a five-minute job for a newcomer", and gaps.md:208 says 8 of the 10 singles sit on a different measurement grid. The first step reads stored results only; it does not run Dara on singles.
  CORRECTED: Reword "certain" to "known to within ingredient purity, weighing error and any reaction during mixing" (plan.md:9, :127; page lines 618, 623). In the 40-row table add one flag column: "recipe has a documented off-recipe phase" and mark the rows that hold both Bi2O3 and Li2CO3, citing the Dara paper. Leave the purity look at the 10 single scans for L1 (the specialist) or for N1. Keep the three L2 asks (ingredient-lot scan, one chemistry check, stated uncertainty) but write them only when L2 is drafted.
- [holds_with_changes] (scorecard) P3 partly: tie function has no key-error input; "The notes do not say whether the interval resamples 20 powders or 40 scans"
  WHY: One sub-claim is refuted. The notes do say it: plan/verify_K4_evidence.md:17 and verify_K1_evidence.md:17 record "10,000 resamples of the 20 mixtures (so the real unit is 20 powders)". The audit searched the verify files and missed this. What is left: plan.md:91 does not make cluster ids part of the D4 spec, and it should. The key_error_rate parameter is over-built for a half-day function; a fixed caveat line does the same job. Also the Reynolds Cup paraphrase is slightly off: the page says entries inside the uncertainty are separated by stricter tie-break criteria (total clay bias, relative errors, number of missed or wrongly named phases), not left unranked.
  CORRECTED: D4 spec: takes optional cluster ids and resamples clusters (powders, papers), never rows. When the key is flagged as draft or has known exceptions, print one line: "key not verified; no ranking claim". For the 40 scans a floor on key error now exists: at least 1 of 20 recipes has a documented off-recipe phase.
- [holds] (scorecard) P4 not_yet_relevant: homogeneity and stability lines for L2
  WHY: Correctly parked. The 0.3-of-tolerance homogeneity rule is confirmed by secondary sources in a search this run (the ISO text was not opened by me either). Nothing to do this month.
  CORRECTED: 
- [holds] (scorecard) P5 partly: no second-instrument subset; add "fixed scans, one instrument" to every headline
  WHY: The plan already states the limit three times (plan.md:55, :127, :198). The fix is three wording lines. It changes nothing the user does this month. Cheap and harmless; not a reason to pause.
  CORRECTED: 
- [holds_with_changes] (scorecard) P6 partly: "harder" omits microabsorption, preferred orientation, non-crystalline content; add per-item tags
  WHY: Evidence checks out (plan.md:110, :142; builds.md:320; gaps.md:210). Scarlett 2002 did build samples for preferred orientation (brucite), non-crystalline content and microabsorption (search snippet; IUCr page 403). But those traps were chosen for a quantification test (how much of each phase). For a naming test the order of importance differs. A newcomer also cannot tag grain shape or crystallinity alone; those tags would be AI-drafted and need the specialist.
  CORRECTED: For a naming exam tag, in this order: minor amount; weakly scattering phase next to a strongly scattering one (Li2CO3 beside La(OH)3 is the user's own 30-fold example); overlapping or same-structure pairs; poorly crystalline or non-crystalline ingredient; flat or needle grains; scan time. Only scan time and the heavy/light pairing are free for the 40 rows. The rest is an N3/L2 checklist, drafted by AI and checked at L1.
- [holds_with_changes] (scorecard) P7 partly: declare a floor band below 1 wt%; misses there not counted against the tool
  WHY: The Leon-Reina numbers are confirmed (Zenodo record opened: detection limit about 0.2 wt% copper source, 0.3 wt% molybdenum; relative error under 20% only above 1 wt%). But that study used careful long scans. Its floor does not transfer to 2-minute scans, and "do not count" hides data.
  CORRECTED: N3: report every band, including the lowest, with counts. Do not headline the lowest band. State the scan conditions beside each band. If a floor is declared, take it from that set's own paper, not from a different instrument.
- [holds_with_changes] (scorecard) P8 violates: "No false-positive count appears anywhere" ... a lenient rule can turn an over-reported list into a correct scan; 1-2 hours; must fix
  WHY: Downgrade from "violates" to "partly". The published mark already punishes extras: the Dara paper counts a scan correct only if it "excludes any spurious phases", top answer only. The local lenient rule matches phases one-to-one (C16:31), which very likely also fails a scan with an extra phase. So the feared loophole probably does not exist in this marker. What is truly missing is one sentence confirming that from the code, and explicit missed/extra counts. The table already holds "true formulas" and "the program's formulas" per scan (plan.md:29), so the counts are a 15-30 minute addition, not 1-2 hours. The Reynolds Cup quote is confirmed verbatim: misidentified absent phases are "THE biggest source of bias".
  CORRECTED: Add two integer columns (missed, extra) per rule, derived from the two formula columns already planned. Add one sentence after reading the marker code: "an extra phase makes the scan wrong: yes/no". For N3 report misses and extras per scan beside the all-or-nothing mark.
- [holds_with_changes] (scorecard) P9 partly: hand-sort has no written rule; go/no-go has no preset number; five bins; ICSD numeric tolerances
  WHY: Pre-writing the sort rule and the threshold is proportionate: the decision gates 2-3 weeks of N1, and the user already pre-registers (builds.md:55; frozen PREREG). Two corrections. (1) Count in distinct formula pairs, not scans. The 40 scans come from 20 mixtures of only 10 ingredients, so one spelling such as "LaO3" for La(OH)3 repeats in every mixture that holds it. gaps.md:153 names three such spellings. Twenty differing rows may be 3-5 distinct cases. K must be in distinct pairs. (2) Five bins is one too many: a library gap mostly shows as "wrong under every rule", which is outside the differing-rows list. The ICSD numeric tolerances need crystal structures, which the stored results do not keep (plan.md:81), so that part belongs to N1 only.
  CORRECTED: Before opening the data write: bins = spelling / real chemistry / key or recipe suspect / unsure (needs specialist). Decision = "build the reusable marker if at least K DISTINCT (true, named) formula pairs are real chemistry"; user picks K. Report both counts: differing rows and distinct pairs. Mark the sort "draft until L1".
- [holds] (scorecard) P10 partly: element list given or not; database date; 16% failed on database age
  WHY: Dara's abstract confirms it searches "within a given chemical space", so this is an elements-given exam. The 2002 search-match abstract (opened) confirms a two-stage design, first without chemistry and then with it, and says up-to-date databases are a condition of success. The specific 16% figure is not in the abstract and I could not verify it. The fix is one line on the task card.
  CORRECTED: 
- [holds_with_changes] (scorecard) P11 partly: freeze one configuration, record its hash; "tools may have been tuned on" the round-robin scans
  WHY: The config-hash advice is fine but belongs to N3, which may never run. The audit missed the closer case of the same problem: the user's own lenient rule was tuned on these 40 scans. The hydrogen rule was added after seeing the misses and moved accuracy from 0.545 to 0.745 (gaps.md:153; C16:245). So 32 of 40 is an in-sample number for the marker. Also, Lutterotti 2019 (full text opened) says "Testing was done initially using the data set 1_h"; that supports "used as published test examples", not clearly "development examples".
  CORRECTED: First-step table: add one line, "the lenient rule was adjusted after seeing these scans; its score here is in-sample". Any marker built from this table needs a check on compounds outside the 10 ingredients (the 20 reaction products, or the specialist's unseen pairs). N3 note: "scans public since about 1999 and used as test examples in tool papers".
- [holds_with_changes] (scorecard) P12 partly: pipeline never run on an externally verified item; optional "paper's per-scan verdict" column; IUCr sample 1 positive control
  WHY: Right principle. Promote the optional column to a required one: the notes say the 38 and 35 are "the marks printed in the paper's own spreadsheet" (verify_K4_evidence.md:17), so per-scan published verdicts exist, and the paper states its marking rule. That column itemises the 6-scan gap at almost no cost. One number to re-check while doing it: the arXiv text as I read it says the commercial tool fails 2 of 20 at 8 minutes (18/20, so 34 of 40), while the notes record 19/20 (35 of 40). The off-recipe carbonate case may explain the one-scan difference. The IUCr positive control is a fair smoke test but only before N3.
  CORRECTED: Required column in the 40-row table: the paper's own per-scan verdict, with the paper's rule quoted once. Reconcile 34 vs 35 for the second tool before quoting either.
- [holds_with_changes] (scorecard) P13 partly: no "upper bound" wording; draw L2 recipes from real reaction-product phase lists; appeal-log columns
  WHY: The plan already says weighed sets are easy in three places (plan.md:142; gap G20; N3's deliverable "is it still too easy"). Only the "upper bound" sentence is new, and it is cheap. The recipe idea has a cost the audit skipped: many by-products of real reactions are not sold as pure powders. A lab would have to make and verify each one, which is the P2 problem again at larger scale. The Lutterotti 2019 case of a published key being contradicted (one lead oxide listed by the organisers, not found by the automatic run, confirmed absent by manual refinement) is verified and is a good reason for the three appeal-log columns.
  CORRECTED: L2 and N5: "accuracy on weighed mixtures is an upper bound on accuracy on real products". L2 recipes: left-over starting chemicals plus by-products that can be bought as checked single-phase powders; say plainly that other by-products are out of scope. D1 CSV: add disputed-by / date / resolution.
- [holds_with_changes] (scorecard) P14 partly: fresh items each round, key holder stays out (Reynolds Cup page)
  WHY: The four L2 lines are sensible and cost 15 minutes when L2 is drafted. "Standing means new powders every round" is the important point and it holds: it makes a standing exam much dearer than the 385-powder sizing. But two claims are credited to the Reynolds Cup page that the page does not state. It says one entry per organisation (confirmed) and that the previous winner has so far volunteered to organise the next round. It does not say the organiser may not enter, and it does not say mixtures must be fresh each round. Both are reasonable inferences, not quotes.
  CORRECTED: Cite the page only for: one entry per organisation; winner organises next round; purity within 1 wt%; splits verified by XRD and XRF. Present "organiser's own tool reported outside the ranking" and "items retire once truth is released" as the plan's own rules.
- [holds] (direction) Direction 1: "The first step is the right kind of step" (low)
  WHY: Quoted lines are real (plan.md:19-43, :79-80, :91, :110, :127, :141). Checking the marker before trusting marks is the right order. The additions fit in about an hour if the task card is copied from the pre-registration and the Dara paper instead of being designed from scratch.
  CORRECTED: 
- [holds] (direction) Direction 2: "The plan puts its effort into scoring code and one line into the answer key" (high)
  WHY: Confirmed and strengthened. Reynolds Cup organiser rules are verified on the page. The Dara paper shows the weighed key already needed a judgement call on 1 of 20 recipes. The user's notes already hold two more key slips in this family of data (hydrate formulas, gaps.md:109; README says equal weight while file names encode 10-90 wt%, builds.md:565). For this month the cost is a wording change and one flag column. For L2 it changes what is asked of the lab, and makes "out of our reach" more likely.
  CORRECTED: 
- [holds_with_changes] (direction) Direction 3: "The long-term aim is narrower than the plan thinks" ... open part = standing + hidden + third-party + naming-first + synthesis chemistry + written marking rule + multi-label score (high)
  WHY: Both papers are real and say what is claimed. Butler and Hillier 2021 (abstract opened): an automated algorithm picked phases from a 201-pattern library on 27 samples from nine contests and would have placed top three in all nine. Lutterotti 2019 (full text opened): automatic tool run on round-robin sample 1_h and on three of the four 2002 naming samples. Three corrections. (1) Both are after-the-fact runs by tool authors on public keys, for quantification in one case; they remove "machine-scored" from the novelty, not "hidden". (2) A novelty sentence with seven qualifiers is itself a warning. The honest open part is short: hidden and recurring, for software, on synthesis-type chemistry. The likely reason nobody runs one is the cost of fresh verified powders, not oversight. (3) Drop "multi-label score" from the open list: GALAXI already reports micro-F1 on phase lists, and the Dara paper already uses an all-present, no-spurious mark. The suggested alternative (offer scoring and a machine submission format to an existing body) is good advice for an ML person, but the fit is limited: the standing contest is clay minerals and quantification, and the IUCr round robins are over 20 years old. Another standing scheme the audit missed: ASTM C1365 qualifies cement X-ray analysis against certified reference clinkers (search result only, not opened).
  CORRECTED: Novelty sentence: "Software has already been scored on contest weighed mixtures after the fact (2019, 2021). What still appears open is a recurring exam with hidden recipes for phase-naming software on synthesis-type chemistry. The main barrier is the cost of fresh, verified powders each round."
- [holds_with_changes] (direction) Direction 4: "Weighed mixtures are the easy, less discriminating case" ... keep a small real-product arm with a consensus key (medium)
  WHY: The numbers are real (plan.md:165, :91) but the plan already knows this (plan.md:142; gap G20), so severity is low-to-medium, not a new finding. The "real-product arm with a consensus key" conflicts with the plan's own section 6 (no headroom: random 20.1% vs perfect 21.8%; single-rater labels) and with the user's core idea that the key should not rest on an analyst. The notes already hold the better version: a real-product set whose key is checked by a second kind of measurement (gap G21: about 12 weeks, about 200 hours, one outside lab). The audit did not link to it.
  CORRECTED: Add the "upper bound" sentence. If a real-product arm is ever added, its key must come from a second measurement (chemistry or microscopy), not from analyst consensus. That is the existing G21 idea and is a later, lab-dependent item.
- [holds_with_changes] (direction) Direction 5: "A diffraction person will not be surprised that formula-string marking is unstable" ... the multi-label score is where an ML-minded person adds something the older field lacks (medium)
  WHY: First half holds and the plan already says it (plan.md:151, :171). Dara itself clusters same-structure phases and groups similar compositions for display, so the tool's authors already handle this inside the tool. Second half is overstated: micro-F1 on phase lists is already in use (GALAXI 2026), the Dara paper has an explicit correct-scan rule, and the Reynolds Cup tie-break already counts missed and wrongly named phases.
  CORRECTED: What an ML person can still add: a tested tiered matcher with a "cannot tell" outcome, intervals that resample powders, and a no-ranking rule when the key is unverified. Present N1 as "first runnable, tested rule card", nothing more.
- [holds_with_changes] (direction) Direction 6: N4 omits the between-lab rung (about 6%, published round robin); compiled notes misread N4 (low)
  WHY: The rung is real: Alleno et al. 2015, one skutterudite specimen, 8 labs for the Seebeck coefficient, 6% (search snippet; PubMed page was a cookie wall). gaps.md:137 and :190 hold it. But it is a different statistic from the other rungs. It is a relative standard uncertainty at the 68% level, averaged over 300-700 K. The other rungs are median differences between pairs. For a bell-shaped spread a 6% standard deviation equals a median pairwise difference of about 5.7% (0.954 times the standard deviation; my arithmetic). I cannot check the side claim that earlier compiled notes misread N4; those notes are not in my files.
  CORRECTED: N4 extra rung: "same specimen, different labs: 6% standard deviation, about 5.7% as a median pairwise difference; one material, 300-700 K; literature value". Give it an includes/excludes line like the others.
- [holds_with_changes] (top_change) Top change 1: 6-line task card plus pre-written five-bin sort rule and preset go/no-go number, about 1 hour
  WHY: Keep it. Fill the card from the frozen pre-registration and the Dara paper's stated rule. Add "top-ranked answer only". Use four bins. Set K in distinct formula pairs, not scans, because the 40 scans come from 10 ingredients.
  CORRECTED: About 1 hour: copy the mark definitions onto a task card; write a four-bin sort rule; pick K as a number of distinct formula pairs; add the line that the lenient rule was tuned on these scans.
- [holds_with_changes] (top_change) Top change 2: log true, named, missed, extra per scan and rule; state whether marks punish extras; 1-2 hours
  WHY: Useful, but smaller and less alarming than stated. The published mark already fails a scan with any spurious phase, and one-to-one matching suggests the local mark does too. Two derived integer columns and one sentence from the code. 15-30 minutes.
  CORRECTED: Add missed and extra counts and one sentence from the marker code. Also add the paper's per-scan verdict as a required column.
- [holds_with_changes] (top_change) Top change 3: stop calling weighed answers "certain"; use the 10 single-ingredient scans as the purity check; six L2 additions
  WHY: The wording change is plainly right and now has direct evidence from the same dataset. The single-scan purity check is too much for a newcomer in a stored-results-only step (an earlier checker said so). Replace it with a flag on the recipes the paper itself reports as off-recipe. The six L2 lines are correct but should be written only when L2 is drafted, not now.
  CORRECTED: Now: reword in four places; flag the Bi2O3 + Li2CO3 rows. Later, in the L2 draft: ingredient-lot scans, one chemistry check on a subset, stated uncertainty per weight fraction, re-scan subset, dates and storage, organiser's tool outside the ranking.
- [holds_with_changes] (top_change) Top change 4: narrow the novelty claim and reshape L2 (mimic reaction products, tag traps, upper bound, price new powders per round)
  WHY: Narrowing is correct and verified. Shorten the novelty sentence instead of stacking seven qualifiers. Drop "multi-label score" as novel. Limit reaction-product recipes to ingredients that can be bought as checked single-phase powders. "New powders every round" is the point that matters most for feasibility.
  CORRECTED: See corrected novelty sentence under Direction 3. Add to L2 sizing: powders per round times rounds, not a one-off 385.
- [holds_with_changes] (top_change) Top change 5: twelve small edits to D4, D6, N3, N4 plus a positive control
  WHY: Each edit is sound. Together they risk becoming the "fifth or sixth round before shipping" that plan.md:143 forbids. Only D4 and D6 are DO-NOW items. N3 depends on D6 and on downloads the user has not approved, so its edits should not be written into anything yet.
  CORRECTED: Do now: D4 resamples clusters; D6 gains three columns (phases given to original entrants, wt% range, scan time). Park the N3, N4 and positive-control items as a short checklist attached to those items, to be applied only if they go ahead.
- [holds] (direction) verdict_on_proceeding: "Proceed with changes ... under an hour of writing"
  WHY: Agreed. Nothing found here justifies pausing the first step. The honest answer to the user's question is: yes, it is mostly eval work; yes, a principles check was worth doing once; it costs about an hour of additions, and it should not grow into another round of auditing.
  CORRECTED: 

## citation checks
- [real_and_says_this] Clay Minerals Society, Reynolds Cup competition rules and guidelines page (undated web page) https://www.clays.org/reynolds/ :: Opened this run. Confirms: mineral purity known within 1 wt%; repeatable splitting; splits verified by XRD and XRF before shipping; only one entry per organisation; mixtures should represent natural sedimentary rocks or soils; "Misidentification of phases that are not present in the mixtures is THE biggest source of bias"; winner = smallest sum of absolute errors, with stricter tie-break criteria when entries fall within the uncertainties.
- [real_but_misdescribed] Same Reynolds Cup page, as cited for "keeps the organiser out of the contest" and "makes fresh mixtures each round" https://www.clays.org/reynolds/ :: Opened this run. The page says the winner of the previous contest has so far volunteered to organise the next. It does not state that the organiser may not enter, and it states no rule that mixtures must be new each round. Both are inferences. Also the page says ties within uncertainty are broken by stricter criteria, not left unranked as the audit's P3 implies.
- [real_and_says_this] Butler B.M. and Hillier S., 2021, "Automated full-pattern summation of X-ray powder diffraction data for high-throughput quantification of clay-bearing mixtures", Clays and Clay Minerals 69, 38-51 https://www.cambridge.org/core/journals/clays-and-clay-minerals/article/abs/automated-fullpattern-summation-of-xray-powder-diffraction-data-for-highthroughput-quantification-of-claybearing-mixtures/08FBFB456A95213FFB6F0B0D2B65DF5E :: Abstract opened on Cambridge Core (Springer URL redirects to a login flow; not followed). 27 samples from nine Reynolds Cup contests; automated; phases selected automatically from a 201-pattern library; accuracy "would be sufficient for top-3 placings in all nine" contests. It is quantification (weight percent) on already-published keys, run by the tool's authors.
- [real_and_says_this] Lutterotti L., Pilliere H., Fontugne C., Boullay P., Chateigner D., 2019, "Full-profile search-match by the Rietveld method", J. Appl. Cryst. 52, 587-598 https://pmc.ncbi.nlm.nih.gov/articles/PMC6557175/ :: Full text opened. Tested on quantification round-robin data set 1_h (three phases found, within about 2% absolute) and on 2002 search-match samples 1, 3 and 4 (sample 2 skipped: unknown structure). For sample 4 it reports that a lead oxide (massicot) listed by the organisers "is indeed not present", checked by manual refinement. So a published key was contradicted. Element list can be supplied to restrict the search. The audit's phrase "development examples" is a stretch; the paper says "testing was done initially" on 1_h.
- [real_and_says_this] Dara paper: "Dara: Automated multiple-hypothesis phase identification and refinement from powder X-ray diffraction", arXiv 2510.19667 (2025; also Chemistry of Materials) https://arxiv.org/abs/2510.19667 :: Abstract and arXiv HTML (https://arxiv.org/html/2510.19667) opened. Confirms "within a given chemical space". The audit did not open the body, which holds the most relevant facts: only the top solution is judged; a scan is correct if it includes all weighed phases and excludes any spurious phase; 2-minute scans 18/20 for Dara; 8-minute 20/20; one mixture shows a real off-recipe bismuth carbonate that the authors chose to exclude from evaluation; no systematic purity check of the ten starting powders is described. As I read it the commercial tool scores 16/20 and 18/20 (34), while the user's notes record 35 from the paper's spreadsheet; this needs reconciling. Read through a summarising fetch; re-check quotes before repeating.
- [real_and_says_this] GALAXI: Tong X. et al., 2026, "Scalable machine learning framework for multiphase identification from powder X-ray diffraction", arXiv 2609.06908 https://arxiv.org/abs/2609.06908 :: Abstract opened. Reports micro-F1 0.935 on "a curated set of experimental patterns"; gives no source, count or definition of a correct phase. Side effect: this shows a multi-label score is already in use in this subfield, which weakens the audit's claim that such a score is what the older field lacks.
- [real_and_says_this] Leon-Reina L. et al., 2016, "Accuracy in Rietveld quantitative phase analysis: a comparative study of strictly monochromatic Mo and Cu radiations", J. Appl. Cryst. 49; data record on Zenodo https://zenodo.org/records/1291900 :: Zenodo landing page opened (no download). CC BY 4.0; raw patterns listed; detection limits about 0.2 wt% (copper) and 0.3 wt% (molybdenum); relative errors under 20% need more than 1.0 wt%; lab copper, lab molybdenum and synchrotron data. Matches the audit. These are careful long scans, so the floor does not transfer to fast routine scans.
- [real_and_says_this] Alleno E. et al., 2015, "Invited Article: A round robin test of the uncertainty on the measurement of the thermoelectric dimensionless figure of merit of Co0.97Ni0.03Sb3", Rev. Sci. Instrum. 86, 011301 https://pubmed.ncbi.nlm.nih.gov/25638064/ :: Not opened: PubMed returned a cookie wall. Confirmed from a search-result abstract only: 8 labs for Seebeck; relative standard uncertainties at 68% confidence, averaged 300-700 K, of 6%, 8%, 11%, 19%. Note the statistic differs from the plan's median pairwise differences.
- [real_and_says_this] Madsen I.C. et al., 2001, J. Appl. Cryst. 34, 409-426 and Scarlett N.V.Y. et al., 2002, J. Appl. Cryst. 35, 383-400, "Outcomes of the IUCr Commission on Powder Diffraction Round Robin on Quantitative Phase Analysis" https://journals.iucr.org/j/issues/2002/04/00/hw0096/ :: Not opened: IUCr and Wiley pages returned HTTP 403. Search snippets confirm titles, authors, that sample 1 is corundum, fluorite and zincite at eight compositions, that sample 2 adds brucite to bring in preferred orientation, and that samples 3 and 4 target non-crystalline content and microabsorption. NOT checked by me or by the audit in this run: that entrants were told which phases were present, and that weighed values were cross-checked by XRF on three portions.
- [could_not_find] Le Meins J.-M., Cranswick L.M.D., Le Bail A., 2003, "Results and conclusions of the internet based 'Search/match round robin 2002'", Powder Diffraction 18 (authors and year from memory) https://www.cambridge.org/core/journals/powder-diffraction/article/abs/results-and-conclusions-of-the-internet-based-searchmatch-round-robin-2002/9BD4F592660EF4E09E2A8FC7F789D2B2 :: Abstract opened. The paper is real. It confirms a two-stage design (first without chemistry, then with chemistry and sample history) and that up-to-date databases are a condition of success. The abstract does not contain the two numbers the notes lean on: "about 16% failed one sample on database age" and "1 of 25 found all 10 phases". Those remain unverified.
- [real_and_says_this] Cline J.P. et al., 2011, "Addressing the amorphous content issue in quantitative phase analysis: the certification of NIST SRM 676a", J. Appl. Cryst. (journal per the NIST page; volume not checked) https://www.nist.gov/publications/addressing-amorphous-content-issue-quantitative-phase-analysis-certification-nist-srm :: NIST page opened. Certified phase purity 99.02% +/- 1.11% (95% interval). Supports "weighed fraction is not crystalline fraction" to within about a percent.
- [real_and_says_this] Allmann R. and Hinek R., 2007, "The introduction of structure types into the Inorganic Crystal Structure Database ICSD", Acta Cryst. A63, 412-417 https://journals.iucr.org/a/issues/2007/05/00/sh0188/ :: Not opened (IUCr site blocks this tool). Search snippet confirms rule-based criteria: space group, Wyckoff sequence, Pearson symbol, axial ratio and angle ranges, formula type. These need crystal structures, which the stored results on the 40 scans do not keep, so it is relevant to N1 only.
- [not_checked] ISO 13528 homogeneity criterion (between-item spread at most 0.3 of the scoring standard deviation) https://shapypro.com/iso-13528-homogeneity-stability/ :: Standard text not opened (paywalled). Several secondary pages in a search this run state the 0.3 rule. The audit's remark that ISO 13528 has only a short clause on qualitative results is from its memory and mine; not checked.

## missed
- The Dara paper already defines the mark and already shows the key is not clean. Top-ranked answer only; all weighed phases present; any spurious phase makes the scan wrong. One of the 20 recipes shows a real off-recipe carbonate, and the authors chose to exclude that phase from their evaluation. This answers the audit's P1 and P8 questions for the published 38 of 40 and gives direct evidence for P2. The audit leaned on the abstract only. Reading that one section (web page, no download) should be part of the first step.
- The sample is smaller than 40 and smaller than 20. The 20 mixtures are built from 10 ingredients, so one formula spelling repeats across many scans. The first step should count distinct (true, named) formula pairs as well as rows, and the go/no-go number should be in distinct pairs. The notes name only three such spellings so far (gaps.md:153). A conclusion from three to five compounds cannot be generalised, which supports plan.md:151 (do not sell the swing as field-wide).
- The marker was tuned on the test scans. The hydrogen rule was added after looking at these scans and moved accuracy from 0.545 to 0.745. So 32 of 40 is in-sample for the rule. The page's idea of about 10 unseen pairs from the specialist is the held-out check; until then, the 20 reaction products are the only out-of-sample look, and there the rule effect is 1-3 of 20.
- Top-1 versus ranked answers, and how to score "not sure". Dara is built to return several candidate answers when the scan is ambiguous, and search-match software in general returns a ranked list with a figure of merit for an analyst to choose from. The stored marks judge rank 1 only. The user's own project adds confidence and abstention, yet neither the plan nor the audit says how an exam should score an abstention (for example accuracy against the share of scans answered). For this user that is the most natural ML contribution, and it is absent from N1, N3 and L2.
- A possible one-scan discrepancy: the arXiv text as I read it gives the commercial tool 18 of 20 on 8-minute scans (34 of 40 overall); the notes record 19 of 20 (35 of 40) from the paper's spreadsheet. The excluded carbonate case may be the cause. Reconcile before quoting "38 vs 35" again; the tie verdict does not change.
- The key is a bottle label, not a crystal structure. An earlier checker said this (plan/verify_K1_newcomer-skeptic.md:20); the audit's P2 covers purity but not which crystal form was in each bottle. It does not matter for formula-level marks. It matters as soon as N1 adds a "same formula, different crystal form" tier.
- More standing schemes exist than the audit lists. ASTM C1365 qualifies cement X-ray phase analysis against certified reference clinkers, and proficiency programmes exist for cement and for crystalline silica (search results only; not opened). All are quantification in one industry, none is phase naming for synthesis, so the narrowed novelty sentence survives. They are further proof that the older field's effort goes into the reference material.
- Process risk. The audit adds 14 rows of fixes to a plan that already lists 31 corrections and warns against "a fifth or sixth round of experiments before shipping anything" (plan.md:143). The useful output of this whole check is about one hour of additions to the first step, four wording changes, and a parked checklist for N3 and L2. It should stop there.
- Several older-field details used by the audit were never opened in either stage because the IUCr site blocks automated reading: whether round-robin entrants were told the phases, the XRF cross-check on three portions, and the two 2002 numbers (16%, 1 of 25). None is needed for this month's work. They should not appear in anything public until a person has read the papers.

## overall
The audit mostly survives. No scorecard row is fully refuted. Its file and line quotes are real; I checked plan.md:9, :29-36, :55, :78-81, :91, :97, :104, :110, :113, :127, :141-146, :164-165, gaps.md:109, :153-154, :207-213, builds.md:320 and :565, and page lines 499, 614, 618, 623. Its main web sources are real and say what it claims: the Reynolds Cup organiser rules, Butler and Hillier 2021, Lutterotti 2019, GALAXI, Leon-Reina 2016, SRM 676a.

What I changed. (1) P8 drops from "violates" to "partly": the published mark already fails a scan that names a spurious phase, and the local rule matches phases one-to-one, so the feared loophole probably does not exist; the fix is 15-30 minutes, not 1-2 hours. (2) One P3 sub-claim is refuted: the notes do record that the 38-vs-35 interval resamples the 20 mixtures (verify_K4_evidence.md:17). (3) Two statements are credited to the Reynolds Cup page that the page does not make (organiser may not enter; fresh mixtures each round). (4) The P2 purity check on the 10 single scans is too much for a newcomer in a stored-results-only step; an earlier checker already said so. (5) The claim that a multi-label score is what ML adds is overstated; micro-F1 is already in use. (6) The seven-qualifier novelty sentence should be shortened; the real barrier is the cost of fresh verified powders. (7) The 6% between-lab rung is a different statistic from the other rungs and needs a conversion note.

Biggest miss. The audit never opened the body of the Dara paper. It defines the mark (top answer only, all weighed phases, no spurious phase) and documents a real off-recipe phase in one of the 20 recipes that the authors chose to leave out of scoring. That is direct evidence, on the user's own 40 scans, that a weighed key is not "certain" and does need a judgement. Two further misses matter for the first step: the 40 scans come from only 10 ingredients, so count distinct formula pairs; and the lenient rule was tuned on these same scans, so its score is in-sample. One direction-level miss: nobody has said how an exam should score "not sure", which is the user's own speciality.

Bottom line for the user. Yes, this is mostly eval work, of the kind ML calls meta-evaluation and metrology calls method validation. Yes, the one-off principles check was worth it. It does not justify a pause. Proceed with the 40-row test after about an hour of additions: a task card copied from the frozen pre-registration and the Dara paper; missed, extra and paper-verdict columns; a four-bin sort rule with a threshold counted in distinct formula pairs; a flag on the recipe with the documented off-recipe phase; and the word "certain" replaced in four places. Everything else in the audit is a parked checklist for N3 and L2, to be used only if those items go ahead.

Relevant files (absolute paths): <session-scratchpad> ; .../scratchpad/plan/verify_K4_evidence.md (line 17) ; .../scratchpad/plan/verify_K1_newcomer-skeptic.md (lines 18-22) ; .../scratchpad/digests/C16-xrd-session-verification.md (lines 25-31, 243-254) ; .../scratchpad/synth/gaps.md (lines 153, 207-213) ; .../scratchpad/page/big-picture.html (lines 499, 614-623).