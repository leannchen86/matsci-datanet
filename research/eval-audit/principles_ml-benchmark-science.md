# principles ml-benchmark-science

- P1 Split by the unit that leaks: Rows that share a source (same paper, same formula, same duplicate file) must sit on one side of a split. A script must print a leak report that proves it.
  CHECK: For each train/test or calibration/test split in the plan: is the group unit named, does a script print 'share of test rows with a sibling in train' for that unit, and is that share 0? Yes/no.
  SRC: Kapoor and Narayanan 2022 (arXiv), 2023 (Patterns) Leakage and the Reproducibility Crisis in ML-based Science [opened] https://arxiv.org/abs/2207.07048; Meredig et al. 2018 Can machine learning identify the next high-temperature superconductor? Examining extrapolation performance for materials discovery [opened] https://citrine.io/can-machine-learning-identify-the-next-high-temperature-superconductor-examining-extrapolation-performance-for-materials-discovery/; Li, Fu, Omee, Hu 2023 (arXiv), 2024 (npj Comput. Mater.) MD-HIT: Machine learning for materials property prediction with dataset redundancy control [opened] https://arxiv.org/abs/2307.04351
- P2 Freeze test list and decision rule first: Fix the test items, a separate tuning set, and the pass/fail rule before looking at results. Log any later change with old and new numbers side by side.
  CHECK: (a) Before the run, does a dated, hashed file hold the test list, a separate dev list, and the decision threshold? (b) Were all baseline settings chosen on dev only? Yes/no to each.
  SRC: Hofman, Chatzimparmpas, Sharma, Watts, Hullman 2023 Pre-registration for Predictive Modeling [opened] https://arxiv.org/abs/2311.18807; Blum and Hardt 2015 The Ladder: A Reliable Leaderboard for Machine Learning Competitions [opened] https://arxiv.org/abs/1502.04585; Recht, Roelofs, Schmidt, Shankar 2019 Do ImageNet Classifiers Generalize to ImageNet? [opened] https://arxiv.org/abs/1902.10811
- P3 Intervals that respect clusters; compare paired: Every score gets an interval. Count independent units, not rows. Compare two tools on the same items with a paired test.
  CHECK: Does the D4 function take a cluster ID and a paired flag, and does 38 vs 35 of 40 still return 'tie' when the 40 scans are clustered into 20 mixtures? Yes/no.
  SRC: Miller 2024 Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations [opened] https://arxiv.org/abs/2411.00640; Dror, Baumer, Shlomov, Reichart 2018 The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing [opened] https://aclanthology.org/P18-1128/; Dietterich 1998 Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms [memory] https://doi.org/10.1162/089976698300017197
- P4 Size the test before building it: Decide the smallest difference you care about, then compute how many items you need. If you cannot get that many, say plainly that the test cannot rank tools.
  CHECK: For each planned comparison: is a minimum detectable difference, and the n it needs, written down before data are run or collected? Yes/no.
  SRC: Card, Henderson, Khandelwal, Jia, Mahowald, Jurafsky 2020 With Little Power Comes Great Responsibility [opened] https://arxiv.org/abs/2010.06595; Miller 2024 Adding Error Bars to Evals [opened] https://arxiv.org/abs/2411.00640
- P5 Give the metric a signature and version: A score is comparable only if the scoring settings are printed with it. Ship the metric as code that emits a settings string, and store that string with every score.
  CHECK: Does every stored score row carry a string naming: rule and version, tolerance, reference library and snapshot date, tool version, candidate cap, and whether 'correct' means the exact set of phases or per-phase credit? Can the 12/17/32/38 spread be fully explained by differing fields of that string? Yes/no.
  SRC: Post 2018 A Call for Clarity in Reporting BLEU Scores [opened] https://arxiv.org/abs/1804.08771; RADAR-PD authors 2026 Automated multiphase identification and refinement in powder diffraction using mismatch-tolerant machine learning [opened] https://arxiv.org/html/2605.12478; Tong et al. 2026 Scalable machine learning framework for multiphase identification from powder X-ray diffraction [opened] https://arxiv.org/abs/2609.06908
- P6 Check the metric against expert judgment: A marking rule is itself a model. Test it against labels from at least two specialists working apart, and report agreement with an interval. An AI-drafted key is a draft, not ground truth.
  CHECK: Is there a set of pairs labelled by 2 or more specialists independently, with their agreement reported, and is each marking rule's agreement with them given with an interval? Until then, is every figure against the AI key worded 'disagrees with the draft key'? Yes/no.
  SRC: Mathur, Baldwin, Cohn 2020 Tangled up in BLEU: Reevaluating the Evaluation of Automatic Machine Translation Evaluation Metrics [opened] https://arxiv.org/abs/2006.06264; Zheng et al. 2023 Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena [opened] https://arxiv.org/abs/2306.05685; RADAR-PD authors 2026 Automated multiphase identification and refinement in powder diffraction using mismatch-tolerant machine learning [opened] https://arxiv.org/html/2605.12478
- P7 Say what decision the score supports: A benchmark measures a construct: the real-world ability you care about. Name the user and the decision, then check that the items and the scoring match it.
  CHECK: Does each marking preset and each exam name one user and one decision (for example 'did my synthesis make the target compound?') and say which tiers count as correct for that use? Does the sample type match that use? Yes/no.
  SRC: Raji, Bender, Paullada, Denton, Hanna 2021 AI and the Everything in the Whole Wide World Benchmark [opened] https://arxiv.org/abs/2111.15366; Bean et al. 2025 Measuring what Matters: Construct Validity in Large Language Model Benchmarks [opened] https://arxiv.org/abs/2511.04703; Bowman and Dahl 2021 What Will it Take to Fix Benchmarking in Natural Language Understanding? [opened] https://arxiv.org/abs/2104.02145; Riebesell et al. 2023 Matbench Discovery: A framework to evaluate machine learning crystal stability predictions [opened] https://arxiv.org/abs/2308.14920
- P8 Show floor, ceiling and headroom: Put a trivial baseline and a best-achievable score beside every result. Build a test only where the gap between them is wider than the test's own error bar.
  CHECK: Does each results table show (a) a trivial baseline, (b) a ceiling from label noise or human agreement, each with an includes/excludes line, and (c) is ceiling minus best current tool larger than the interval half-width at the planned n? Yes/no.
  SRC: Crusius, Cipcigan, Biggin 2025 Are we fitting data or noise? Analysing the predictive power of commonly used datasets in drug-, materials-, and molecular-discovery [memory] https://pubs.rsc.org/en/content/articlehtml/2025/fd/d4fd00091a; Northcutt, Athalye, Mueller 2021 Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks [opened] https://arxiv.org/abs/2103.14749; Ott, Barbosa-Silva, Blagec, Brauner, Samwald 2022 Mapping global dynamics of benchmark creation and saturation in artificial intelligence [opened] https://arxiv.org/abs/2203.04592; Kiela et al. 2021 Dynabench: Rethinking Benchmarking in NLP [opened] https://arxiv.org/abs/2104.14337
- P9 A hidden test needs rules, not just secrecy: Blind tests work because of governance: fresh items each round, a custodian who is not a contestant, limits on scored submissions, and published independent assessment.
  CHECK: Does the L2 one-page request name each of: a custodian who does not enter; a hash of the answer key lodged before release; a cap on scored submissions; file names and headers with no recipe clues; a plan for new powders each round; what is published afterwards? Yes/no per item.
  SRC: Protein Structure Prediction Center (CASP organisers) 1994 to 2026 CASP home page [opened] https://predictioncenter.org/; Blum and Hardt 2015 The Ladder: A Reliable Leaderboard for Machine Learning Competitions [opened] https://arxiv.org/abs/1502.04585; Jacovi, Caciularu, Goldman, Goldberg 2023 Stop Uploading Test Data in Plain Text [opened] https://arxiv.org/abs/2305.10160
- P10 Ship a datasheet with every artefact: Each list, key or table ships with a short sheet: source snapshot and hash, how rows were chosen, who or what made the labels, licence, known errors, and what it must not be used for.
  CHECK: For each file the plan ships (tricky-pairs CSV, 499-row match table, frozen paper-ID list, number card): is there a one-page sheet with those fields, and does it say 'not a hidden test' where answers are public? Yes/no.
  SRC: Gebru et al. 2018 (arXiv), 2021 (CACM) Datasheets for Datasets [opened] https://arxiv.org/abs/1803.09010; Mitchell et al. 2018 Model Cards for Model Reporting [opened] https://arxiv.org/abs/1810.03993; Reuel, Hardy, Smith, Lamparth, Hardy, Kochenderfer 2024 BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices [opened] https://arxiv.org/abs/2411.12990; Kapoor, Cantrell, Peng et al. 2023 REFORMS: Reporting Standards for Machine Learning Based Science [opened] https://arxiv.org/abs/2308.07832
- P11 Read the rows; keep hand-picked sets apart: Totals hide causes. Publish row-level tables and slice by known factors. Never quote a pass rate on hand-picked hard cases as an error rate in the wild.
  CHECK: Does each headline number come with a row-level file and at least one slice named in advance? Is every figure from the tricky-pairs file worded as 'unit tests failed', not 'percent wrong'? Yes/no.
  SRC: Ribeiro, Wu, Guestrin, Singh 2020 Beyond Accuracy: Behavioral Testing of NLP Models with CheckList [opened] https://arxiv.org/abs/2005.04118; Northcutt, Athalye, Mueller 2021 Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks [opened] https://arxiv.org/abs/2103.14749
- P12 Replicate before you generalise: A finding about a benchmark on one dataset and one tool is local. Show it on a second independent dataset and tool, or word it as local.
  CHECK: Is each headline claim in N5 shown on 2 or more independent datasets and 2 or more tools? If not, does the text say 'in our set-up'? Yes/no.
  SRC: Dehghani et al. 2021 The Benchmark Lottery [opened] https://arxiv.org/abs/2107.07002; Gorman and Bedrick 2019 We Need to Talk about Standard Splits [opened] https://aclanthology.org/P19-1267/; Recht, Roelofs, Schmidt, Shankar 2019 Do ImageNet Classifiers Generalize to ImageNet? [opened] https://arxiv.org/abs/1902.10811
- P13 Assume the score will be gamed: Once a number is a target, tools drift toward what it rewards. Design the score so that vague or padded answers lose.
  CHECK: Does the marker charge for extra wrong phases as well as missed ones? Does 'cannot tell' score below 'same'? Would a tool that lists more phases, or a vaguer formula, gain under any preset? Run it as a unit test. Yes/no.
  SRC: Thomas and Uminsky 2020 (arXiv), 2022 (Patterns) The Problem with Metrics is a Fundamental Problem for AI [opened] https://arxiv.org/abs/2002.08512
- P14 No user, no benchmark: Most benchmarks are never adopted. Secure one outside user or host before building for outsiders, and make the tool trivial to run.
  CHECK: Before N1 or N5 is built for others: is there one named outside tool author, benchmark host or specialist who has said they would run or host it? Yes/no.
  SRC: Ott, Barbosa-Silva, Blagec, Brauner, Samwald 2022 Mapping global dynamics of benchmark creation and saturation in artificial intelligence [opened] https://arxiv.org/abs/2203.04592; Koch, Denton, Hanna, Foster 2021 Reduced, Reused and Recycled: The Life of a Dataset in Machine Learning Research [opened] https://arxiv.org/abs/2112.01716; Post 2018 A Call for Clarity in Reporting BLEU Scores [opened] https://arxiv.org/abs/1804.08771

## prior art
- sacreBLEU (Post 2018) [opened] in_notes=False: A scoring tool for machine translation that fixes the settings and prints a version-and-settings string with every score.
  OVERLAPS: D1 40-row marking test, N1 tiered marking function
  OPEN: Nothing like it exists for X-ray phase answers as far as this run found. The idea transfers directly: signature string plus one agreed default.
  https://arxiv.org/abs/1804.08771
- RADAR-PD's GPT-4 phase-equivalence judge [opened] in_notes=True: A 2026 X-ray/neutron phase-ID paper that lets a GPT-4 prompt decide if a predicted structure is the same phase as the reference (accepts alternate settings, supercells, hydration and defect variants). 291 mineral-archive samples.
  OVERLAPS: D1 tricky-pairs key, N1 marker tiers
  OPEN: The page shows no validation of the judge against specialists and no runnable rule card. Its accepted-variant list is a ready comparison for the plan's tier names.
  https://arxiv.org/html/2605.12478
- Martirossyan et al. 2025, 'All that structure matches does not glitter' [opened] in_notes=False: Audit of crystal-structure-prediction benchmarks: one common set is only about 40% unique structures; random splits put crystal forms of one formula on both sides; the match-rate metric misleads. Proposes two new metrics (METRe, cRMSE) and cleaned splits, including variants with mirror-image pairs.
  OVERLAPS: N1 structure-level marking; D1 mirror-image guard row; P1 splits
  OPEN: It covers generated structures on computed data, not marking formula-only answers from measured scans. Abstract only was read.
  https://arxiv.org/abs/2509.12178
- Wei, Li, Omee, Hu 2023, 'Towards Quantitative Evaluation of Crystal Structure Prediction Performance' (and CSPBench 2024) [opened] in_notes=False: A set of automatic structure-similarity metrics to replace case-by-case manual comparison, plus a 180-structure benchmark of 13 algorithms.
  OVERLAPS: N1 marking function (structure tier)
  OPEN: Aimed at structure prediction, not phase identification. CSPBench itself was seen in search results only (https://arxiv.org/abs/2407.00733), not opened.
  https://arxiv.org/abs/2307.05886
- CheckList (Ribeiro et al. 2020) [opened] in_notes=False: Unit-test style behavioural tests for models: minimum functionality, invariance and directional tests.
  OVERLAPS: D1 tricky-pairs table
  OPEN: A method template only. The mirror-image pair is an invariance test; the Nb2O5 vs Nb12O29 pair is a minimum functionality test. Use its vocabulary instead of inventing one.
  https://arxiv.org/abs/2005.04118
- Reynolds Cup (Raven and Self 2017 review) [opened] in_notes=True: Blind contest on weighed mineral mixtures, any method allowed, ranked by a 'bias' score (summed deviation from the true amounts). About 448 participants and 21 samples over 2002 to 2014. Notes that phases reported by automatic search-match programs were often implausible.
  OVERLAPS: L2 hidden exam, N3 practice exam, P13 over-answering
  OPEN: Notes know the contest but not its scoring rule. It is for human analysts, about 3 samples a round, clay-heavy, scored on amounts not on naming. No standing machine-scored version.
  https://www.cambridge.org/core/product/identifier/S0009860400039410/type/journal_article
- CASP [opened] in_notes=True: Blind protein-structure test every two years since 1994 with independent assessors.
  OVERLAPS: L2 hidden exam (governance template)
  OPEN: Template only. Needs a steady stream of unpublished answers, which one partner lab does not give.
  https://predictioncenter.org/
- Blum and Hardt 2015 (the Ladder) and Jacovi et al. 2023 [opened] in_notes=False: Leaderboard mechanism against overfitting by repeated submission; practical rules against test-set contamination (encrypt, bar derivatives, avoid items with answers online).
  OVERLAPS: L2 hidden exam; N3 (public answers, recipe in file names); D3 frozen paper-ID list
  OPEN: General ML. Second URL: https://arxiv.org/abs/2305.10160. The plan's L2 one-pager lacks a submission cap and a refresh rule.
  https://arxiv.org/abs/1502.04585
- Codabench [memory] in_notes=True: Free challenge host that keeps answers hidden.
  OVERLAPS: L2 hidden exam
  OPEN: Not opened in this run; taken from the notes (G17, single-agent finding).
  https://www.codabench.org/
- Meredig et al. 2018, leave-one-cluster-out cross-validation [opened] in_notes=False: The standard materials citation for 'random splits overstate performance', with a nearest-neighbour baseline.
  OVERLAPS: D3 private TE re-run, N2 TE note
  OPEN: Not TE, not grouped by paper, no frozen list. It means the general claim is 8 years old; N2 must not present it as new.
  https://citrine.io/can-machine-learning-identify-the-next-high-temperature-superconductor-examining-extrapolation-performance-for-materials-discovery/
- MD-HIT (Li, Fu, Omee, Hu 2023/2024) [opened] in_notes=False: Tool that removes near-duplicate materials so random splits stop flattering models.
  OVERLAPS: D3, N2; the dropped 'fair-split generator'
  OPEN: Shown on computed-property datasets. Says nothing about paper-level grouping of measured TE curves. Supports the plan's choice not to build a split tool.
  https://arxiv.org/abs/2307.04351
- MatFold [memory] in_notes=True: Existing materials split tool (grouped and out-of-distribution folds).
  OVERLAPS: D3, N2
  OPEN: Not opened in this run; URL from memory. Plan already drops the pull request.
  https://github.com/d2r2group/MatFold
- 2026 Materials and Design TE paper with a composition-wise split [memory] in_notes=False: 'Physics-inspired feature engineering and interpretable machine learning for thermoelectric properties of multicomponent materials'. Search snippet: R-squared about 0.96 on a random split falls to 0.82 to 0.88 when whole compositions are held out (3,879 compositions).
  OVERLAPS: N2 TE note (the '1-2 hour search for an existing TE leakage audit')
  OPEN: NOT opened (403); search snippet only. It holds out compositions, not papers, on one dataset, and ships no frozen list as far as the snippet shows. So correction 21 stands, but 'TE papers split at random' now has a counter-example to cite.
  https://www.sciencedirect.com/science/article/pii/S0264127526011068
- Ma and Poon 2025, 'Reexamining Machine Learning Models on Predicting Thermoelectric Properties' [opened] in_notes=False: Looks like an audit by its title. The abstract is about adding physics features and dopant properties.
  OVERLAPS: N2 TE note
  OPEN: The abstract has nothing on leakage, splits or baselines. Not the audit N2 worries about. Whether any paper-level TE leakage audit exists is still unknown after two searches.
  https://arxiv.org/abs/2509.00299
- Crusius, Cipcigan, Biggin 2025, 'Are we fitting data or noise?' [memory] in_notes=False: Best-achievable-score bounds from experimental error for nine chemistry and materials datasets, with a Python package and web app. Four datasets had models at or past the bound.
  OVERLAPS: N4 noise ladder and number card
  OPEN: NOT opened (403 on publisher and preprint); search results only. Unknown whether any TE set is included. The plan's ladder adds rungs this work does not seem to have (reading noise, within-paper, across-paper), but N4 should cite it and check its package before writing new code.
  https://pubs.rsc.org/en/content/articlehtml/2025/fd/d4fd00091a
- Miller 2024, 'Adding Error Bars to Evals' [opened] in_notes=False: Formulas for standard errors, paired differences, clustering and power for evals.
  OVERLAPS: D4 'tie or not?' function
  OPEN: Nothing. D4 is an implementation of known statistics; cite it, add the cluster argument, claim no novelty.
  https://arxiv.org/abs/2411.00640
- BetterBench (46 criteria), REFORMS (32 questions), Kapoor-Narayanan model info sheets, Bean et al. 2025 (8 recommendations) [opened] in_notes=False: General checklists for judging a benchmark or an ML-based scientific claim.
  OVERLAPS: N5 'four questions before trusting a materials leaderboard'
  OPEN: None is materials-specific, and none covers 'is the data what its label says' for measured vs simulated scans or a label-noise ladder from lab round robins. N5 should map its four questions onto these and keep only what is new. Other URLs: https://arxiv.org/abs/2308.07832, https://arxiv.org/abs/2207.07048, https://arxiv.org/abs/2511.04703.
  https://arxiv.org/abs/2411.12990
- GALAXI (arXiv 2609.06908, 7 Sept 2026) [opened] in_notes=False: New X-ray phase-ID tool with classifiers for 64,594 structures and a public web interface. Reports micro-F1 0.935 on a curated experimental set, above search-match and earlier deep-learning tools.
  OVERLAPS: N3 practice exam (a second tool to run); P5 (yet another scoring unit)
  OPEN: Abstract only. No item count, matching rule or intervals in the abstract; the HTML full text returned 404. Shows the field is moving this month and that scores are still reported in non-comparable units.
  https://arxiv.org/abs/2609.06908
- Northcutt et al. 2021 and Recht et al. 2019 [opened] in_notes=True: Test-set label-error audit (6% in ImageNet validation) and fresh-test-set replication (11 to 14% drop, rankings held).
  OVERLAPS: D5/L3 error notes, N6 TE suspect list, D2 match table
  OPEN: gaps.md quotes both facts (G17, G34) without naming the sources. Second URL: https://arxiv.org/abs/1902.10811. Lesson for D5: report how much the errors change a score or a ranking, not only how many there are.
  https://arxiv.org/abs/2103.14749
- Matbench Discovery (Riebesell et al. 2023) [opened] in_notes=True: Computed-data materials leaderboard whose paper argues the metric must match the discovery task.
  OVERLAPS: N5 short note; P7
  OPEN: Notes know it as a leaderboard (G41), not for its metric-validity argument. It is computed data only, so the measured-data side stays open.
  https://arxiv.org/abs/2308.14920
- IUCr powder-diffraction round robins (quantitative analysis 2001/2002; search-match 2002) and the 1990 structure-similarity classification [memory] in_notes=True: Older community tests with weighed 4- and 7-ingredient mixtures and lenient human marking; a formal vocabulary for 'how alike are two structures'.
  OVERLAPS: N1 tier names, N3 practice exam, D6 web check
  OPEN: Not opened in this run; URL from memory and may have moved. Notes flag these as single-agent findings. D6 should verify them on the web as planned.
  https://www.iucr.org/resources/commissions/powder-diffraction/projects
- XRDBench [memory] in_notes=True: LLM-oriented X-ray benchmark (100 question tasks, 34 end-to-end tasks); answers are in public JSON per the latest notes.
  OVERLAPS: N3 practice exam, L2, P14 (possible host for the marker)
  OPEN: Not opened in this run. Notes flip-flopped on whether its answers are public; latest word is public. 30% of its score comes from an LLM judge, so P6 applies to it too.
  