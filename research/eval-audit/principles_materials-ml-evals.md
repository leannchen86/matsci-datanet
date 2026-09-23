# principles materials-ml-evals

- P1 Split by the unit that leaks: Rows that share a hidden cause must sit on the same side of the split. In TE data the hidden causes are the paper (same lab, same sample batch), the formula (one compound measured at many temperatures) and the chemical family. Always print a nearest-neighbour baseline beside the model.
  CHECK: Does the results table show random, by-formula, by-paper and by-chemical-system scores side by side, each with a 1-nearest-neighbour row? Yes or no.
  SRC: Meredig, Antono, Church, Hutchinson, Ling, Paradiso, Blaiszik, Foster, Gibbons, Hattrick-Simpers, Mehta, Ward 2018 Can machine learning identify the next high-temperature superconductor? Examining extrapolation performance for materials discovery (Mol. Syst. Des. Eng.) [opened] https://citrine.io/can-machine-learning-identify-the-next-high-temperature-superconductor-examining-extrapolation-performance-for-materials-discovery/; Li, Fu, Omee, Hu 2024 MD-HIT: Machine learning for material property prediction with dataset redundancy control (npj Comput. Mater. 10, 245) [opened] https://arxiv.org/abs/2307.04351; Kapoor, Narayanan 2022 Leakage and the Reproducibility Crisis in ML-based Science [opened] https://arxiv.org/abs/2207.07048; Barua, Salla, Kleinke 2026 A Machine Learning Web Application for Real-Time Thermoelectric Property Predictions (ACS Omega, doi 10.1021/acsomega.6c01225) [opened] https://pmc.ncbi.nlm.nih.gov/articles/PMC13470758/; Na, Chang 2022 A public database of thermoelectric materials and system-identified material representation (npj Comput. Mater., doi 10.1038/s41524-022-00897-2); read via the SIMD code README [opened] https://github.com/KRICT-DATA/SIMD
- P2 Add a split by publication year: A forward-in-time split is the closest thing to real use. Train on what was known at a date. Test on what was published later.
  CHECK: Does D3 include one split where every test paper is published after every training paper? Yes or no.
  SRC: Riebesell, Goodall, Benner, Chiang, Deng, Ceder, Asta, Lee, Jain, Persson 2025 Matbench Discovery: a framework to evaluate machine learning crystal stability predictions (Nat. Mach. Intell. 7, 836) [opened] https://arxiv.org/abs/2308.14920; Li, DeCost, Choudhary, Greenwood, Hattrick-Simpers 2023 A critical examination of robustness and generalizability of machine learning prediction of materials properties [opened] https://arxiv.org/abs/2210.13597
- P3 Do not call grouped splits out-of-distribution: Holding out a group does not prove the test rows are far from training. Most 'out-of-distribution' splits in materials turn out to be interpolation. Measure the overlap and print it.
  CHECK: For each held-out split, is there a number for how many test rows still have a near twin in training (same formula, same paper, or a stated distance cut-off)? Yes or no.
  SRC: Li, K., Rubungo, Lei, Persaud, Choudhary, DeCost, Dieng, Hattrick-Simpers 2025 Probing out-of-distribution generalization in machine learning for materials (Commun. Mater. 6, 9) [opened] https://arxiv.org/abs/2406.06489; Omee, Fu, Dong, Hu, Hu 2024 Structure-based out-of-distribution materials property prediction: a benchmark study (npj Comput. Mater.) [memory] https://www.nature.com/articles/s41524-024-01316-4
- P4 Freeze, clean and fence the test list: Publish three things: the exact test list, the rule that removes test items duplicating training items (with counts), and the rule for what training data is allowed. Without all three, two people's scores cannot be compared.
  CHECK: Is there (a) a versioned file of test IDs, (b) a written de-duplication rule with the number removed, (c) a one-line allowed-training-data rule? Yes or no on each.
  SRC: Riebesell et al. 2025 Matbench Discovery (full text, v3) [opened] https://arxiv.org/html/2308.14920v3; Barroso-Luque et al. (Meta FAIR) 2024 Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models [memory] https://arxiv.org/abs/2410.12771
- P5 Pick the metric that matches the decision: Low average error does not mean good decisions. Report the number that matches the use: false-positive rate for screening, sign and size for a signed quantity, hit rate for discovery.
  CHECK: Does each headline number come with one sentence naming the decision it supports, and is at least one decision-level metric reported (false-positive rate, sign accuracy, top-k hit rate)? Yes or no.
  SRC: Riebesell et al. 2025 Matbench Discovery [opened] https://arxiv.org/abs/2308.14920; Borg, Muckley, Saal, Meredig and co-authors 2023 Quantifying the performance of machine learning models in materials discovery [opened] https://arxiv.org/abs/2210.13587
- P6 Reproduce the published marks before re-marking: Before proposing a new marking rule, reproduce the original authors' marks pattern by pattern under their own rule. Otherwise the gap may come from your harness, not from the field.
  CHECK: Is there a table lining up the Dara paper's per-pattern verdicts (its published benchmark spreadsheets) against the local run, with every mismatch tagged as library, settings or marking? Yes or no.
  SRC: Fei, McDermott, Rom, Wang, Ceder 2025 Dara: Automated multiple-hypothesis phase identification and refinement from powder X-ray diffraction [opened] https://arxiv.org/html/2510.19667v2; Dara repository 2025 idocx/dara (MIT licence) [opened] https://github.com/idocx/dara
- P7 Score phases, not only whole patterns: Per-pattern exact match hides whether errors are misses or false alarms. Also report per-phase precision, recall and F1. When the recipe weights are known, report weight error too.
  CHECK: Does the marker output per-phase true positives, false positives and false negatives (micro-F1) beside the per-pattern score, and a weight-error score for weighed mixtures? Yes or no.
  SRC: Tong, Jin, Xu, Rao, Jiang, Szymanski 2026 Scalable machine learning framework for multiphase identification from powder X-ray diffraction (GALAXI) [opened] https://arxiv.org/abs/2609.06908; Raven, Self 2017 Outcomes of 12 Years of the Reynolds Cup Quantitative Mineral Analysis Round Robin (Clays and Clay Minerals 65) [opened] https://www.cambridge.org/core/product/identifier/S0009860400039410/type/journal_article; Madsen, Scarlett, Cranswick, Lwin 2001 Outcomes of the IUCr Commission on Powder Diffraction round robin on quantitative phase analysis: samples 1a to 1h (J. Appl. Cryst. 34, 409) [memory] https://journals.iucr.org/j/issues/2001/04/00/hw0085/
- P8 Make the same-phase rule deterministic and versioned: Whether two database entries count as 'the same phase' must be a written rule that a script applies identically every time. An LLM judge or a human eye is not reproducible.
  CHECK: Can a stranger re-run the marker on the same results file and get identical marks, and is there a test file of tricky pairs with expected verdicts? Yes or no.
  SRC: RADAR-PD authors 2026 Automated multiphase identification and refinement in powder diffraction using mismatch-tolerant machine learning (APL Mach. Learn. 4, 036114) [opened] https://arxiv.org/html/2605.12478; Leeman, Hoelzel, Gibbons, Ferrenti, Shevlin, Schoop and co-authors 2024 Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis (PRX Energy 3, 011002) [opened] https://journals.aps.org/prxenergy/abstract/10.1103/PRXEnergy.3.011002
- P9 The answer key must stand without the tool: Ground truth should come from something independent of the method under test: a weighed recipe, a second measurement technique, or specialist agreement. A key drafted by a fitting tool or an LLM inherits their blind spots.
  CHECK: Does every benchmark row record its truth source as one of {weighed recipe, independent measurement, specialist-agreed, tool- or AI-drafted}, and are tool- or AI-drafted rows kept out of headline numbers? Yes or no.
  SRC: Szymanski, Rendy, Fei, Ceder and co-authors 2026 Author Correction: An autonomous laboratory for the accelerated synthesis of inorganic materials (Nature 650, E1) [opened] https://pmc.ncbi.nlm.nih.gov/articles/PMC12872444/; Leeman et al. 2024 Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis [opened] https://journals.aps.org/prxenergy/abstract/10.1103/PRXEnergy.3.011002; RADAR-PD authors 2026 Automated multiphase identification and refinement in powder diffraction using mismatch-tolerant machine learning [opened] https://arxiv.org/html/2605.12478
- P10 State the candidate library and its coverage: A phase-ID tool can only name phases that are in its reference library. Scores from different libraries are not comparable. Say which library, which version, how candidates were shortlisted, and whether the true phases were in the pool.
  CHECK: Does every score row carry library name and version, the candidate-pool rule, and a per-scan flag 'all true phases were in the pool'? Yes or no.
  SRC: Fei et al. 2025 Dara [opened] https://arxiv.org/html/2510.19667v2; RADAR-PD authors 2026 RADAR-PD [opened] https://arxiv.org/html/2605.12478; Tong et al. 2026 GALAXI [opened] https://arxiv.org/abs/2609.06908
- P11 Count independent units and show intervals: n is the number of independent things, not the number of rows. Compare two tools on the same items with a paired method. Put an interval on every score.
  CHECK: Does D4 resample by cluster (mixture for XRD, paper for TE) and use a paired comparison when both tools ran on the same scans? Yes or no.
  SRC: RADAR-PD authors 2026 RADAR-PD [opened] https://arxiv.org/html/2605.12478; Fei et al. 2025 Dara [opened] https://arxiv.org/html/2510.19667v2; Miller 2024 Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations [memory] https://arxiv.org/abs/2411.00640
- P12 Test on measured data; label simulated data: Models trained on computed patterns lose accuracy on measured ones. A benchmark must say, per file, measured or computed, and report the two apart.
  CHECK: Does every test file carry a verified measured/computed flag, and are headline scores on measured files only? Yes or no.
  SRC: Hollarek, Schopmans, Friederich and co-authors 2025 opXRD: Open Experimental Powder X-ray Diffraction Database [opened] https://arxiv.org/abs/2503.05577; Szymanski, Bartel, Zeng, Tu, Ceder 2021 A probabilistic deep learning approach to automate the interpretation of multi-phase diffraction spectra (XRD-AutoAnalyzer) [opened] https://arxiv.org/abs/2103.16664
- P13 Report the noise ceiling: Labels carry measurement error. No model can beat the disagreement between repeat measurements. Print that floor beside the model error so nobody chases noise.
  CHECK: Is there a label-noise number (repeat-measurement or across-paper spread) beside each model error, and is every claimed gain larger than it? Yes or no.
  SRC: Crusius, Cipcigan, Biggin 2025 Are we fitting data or noise? Analysing the predictive power of commonly used datasets in drug-, materials-, and molecular-discovery (Faraday Discuss. 256, 304) [memory] https://pubs.rsc.org/en/content/articlelanding/2025/fd/d4fd00091a; Ryu and co-authors 2025 teMatDb: a high-quality thermoelectric material database with self-consistent ZT filtering [opened] https://arxiv.org/abs/2505.19150
- P14 Say what the score claims to measure: Write down the real-world ability the benchmark stands for and why the task is a fair proxy. Ship that as a short card with the benchmark.
  CHECK: Is there a one-page card per benchmark with: the claimed ability, data source, known label problems, split rule, metric, and what a high score does NOT mean? Yes or no.
  SRC: Alampara, Schilling-Wilhelmi, Jablonka 2025 Lessons from the trenches on evaluating machine-learning systems in materials science (Comput. Mater. Sci. 259, 114041) [opened] https://arxiv.org/abs/2503.10837; Kapoor, Narayanan 2022 Leakage and the Reproducibility Crisis in ML-based Science [opened] https://arxiv.org/abs/2207.07048; Choudhary and co-authors 2023 JARVIS-Leaderboard: a large scale benchmark of materials design methods [opened] https://arxiv.org/abs/2306.11688

## prior art
- Dara paper benchmark, correctness rule and published spreadsheets [opened] in_notes=False: The original 40 weighed-mixture scans plus 20 reaction products, marked per pattern: all weighed-in phases found and no spurious phase. Summaries released as two spreadsheets.
  OVERLAPS: D1, N1
  OPEN: The notes know the 38-of-40 figure and the ICSD/COD difference, but not the stated rule or the spreadsheets. Open: a rule for when two database entries are the same phase. The paper does not give one. It cites Leeman without engaging with the disorder point.
  https://arxiv.org/html/2510.19667v2
- RADAR-PD GPT-4 equivalence judge [opened] in_notes=True: A 2026 phase-ID paper that lets a GPT-4 prompt decide if a predicted phase equals the label, tolerating supercells, hydration and symmetry variants. Labels were also LLM-selected.
  OVERLAPS: D1 tricky-pairs CSV, N1 tiered marker
  OPEN: A deterministic, versioned rule with a test file. No intervals. Dara was run on a merged COD plus MP pool, so the head-to-head is not clean.
  https://arxiv.org/html/2605.12478
- GALAXI (arXiv 2609.06908) [opened] in_notes=False: Sept 2026 multi-phase identifier scored by micro-F1 on curated measured patterns; claims to beat search-match and earlier deep models.
  OVERLAPS: N1 (metric choice), N3 (practice exam)
  OPEN: I read the abstract only. Test-set size, phase-matching rule and whether the curated patterns are public are unknown. Worth a 30-minute read before N1.
  https://arxiv.org/abs/2609.06908
- Reynolds Cup [opened] in_notes=True: A recurring blind contest: organisers mix known minerals, entrants report weight percents, score is summed deviation from truth. 448 entrants over 12 years.
  OVERLAPS: D6, N3, L2 (it is a working model of a hidden exam)
  OPEN: Notes list it as a dataset. They miss that it is already a hidden exam with a scoring rule, run by humans with any tool. Open: nobody has run automated tools on it as entrants, as far as I found. Whether raw scans are obtainable is unknown.
  https://www.cambridge.org/core/product/identifier/S0009860400039410/type/journal_article
- IUCr powder-diffraction round robin on quantitative phase analysis (Madsen 2001, Scarlett 2002) [memory] in_notes=True: Known mixtures sent to many labs; entrants scored by a Kullback-Leibler-type distance on weight fractions.
  OVERLAPS: D6, N3
  OPEN: Page returned 403; scoring detail is from a snippet. Notes have the dataset, not the scoring rule.
  https://journals.iucr.org/j/issues/2001/04/00/hw0085/
- XRD-AutoAnalyzer (Szymanski et al. 2021) [opened] in_notes=False: Deep-learning phase identifier trained on simulated patterns, tested on simulated and measured ones separately.
  OVERLAPS: N3, D2
  OPEN: The name does not appear in plan or synth files, though the same group's 2023 240-mixture set does. Its measured test set is small and single-lab. No shared marking rule.
  https://arxiv.org/abs/2103.16664
- opXRD [opened] in_notes=True: Pooled open collection of 92,552 XRD patterns from several labs; 2,179 labelled. States the simulated-to-measured gap. No benchmark protocol.
  OVERLAPS: D2, L4, N3
  OPEN: No split, no metric, no measured/computed audit. D2 fills a real hole.
  https://arxiv.org/abs/2503.05577
- SimXRD-4M [memory] in_notes=False: Large simulated XRD set that uses 3,002 RRUFF patterns as its 'experimental' test.
  OVERLAPS: D2
  OPEN: Not opened this run; known only from plan/verify_K2_prior-art.md, not from plan.md or gaps.md. No ID list for the RRUFF subset, so computed entries cannot be excluded by readers.
  https://arxiv.org/html/2406.15469v2
- AutoXRD / XRDBench (arXiv 2609.00070) [opened] in_notes=True: Aug 2026 agent benchmark: 100 question tasks plus 34 end-to-end XRD tasks.
  OVERLAPS: L2, N3
  OPEN: Abstract does not say how answers are scored or whether they are public. Notes say answers are public, so it cannot serve as a hidden exam.
  https://arxiv.org/abs/2609.00070
- Matbench Discovery design principles [opened] in_notes=True: The best-known materials benchmark redesign: prospective test set, relevant target, decision metrics, de-duplication, compliant-training rule.
  OVERLAPS: D3, L5, N5
  OPEN: gaps.md cites its scores only. Its design rules are the template a reviewer will hold the plan to. It is for computed stability, not measured properties. Nothing like it exists for TE or XRD.
  https://arxiv.org/abs/2308.14920
- Meredig 2018 leave-one-cluster-out validation [opened] in_notes=False: The paper that made grouped validation and a nearest-neighbour baseline standard advice in materials ML.
  OVERLAPS: D3, N2
  OPEN: Clusters are in feature space, not by paper. Must be cited in N2 or a reviewer will ask why not.
  https://citrine.io/can-machine-learning-identify-the-next-high-temperature-superconductor-examining-extrapolation-performance-for-materials-discovery/
- MD-HIT [opened] in_notes=False: Tool and paper on thinning near-duplicate materials before splitting.
  OVERLAPS: D3, D2
  OPEN: Works on computed-structure datasets by composition or structure similarity. Does not handle 'same paper' or 'same sample at many temperatures'.
  https://arxiv.org/abs/2307.04351
- MatFold [opened] in_notes=True: Open library of standard grouped splits for materials (by composition, chemical system, elements, symmetry and more), saved as JSON.
  OVERLAPS: N2
  OPEN: README lists no split by paper or arbitrary user group. That reading comes from a summary of the README, so treat as uncertain. The plan already dropped the pull-request idea.
  https://github.com/d2r2group/MatFold
- Li et al. 2025 on out-of-distribution tests [opened] in_notes=False: Shows most held-out-group tests in materials are interpolation.
  OVERLAPS: D3, N2 wording
  OPEN: On computed datasets. The plan's 52.4 percent paper-overlap number is the same idea on measured TE data and appears to be new.
  https://arxiv.org/abs/2406.06489
- Li et al. 2023 version-shift study [opened] in_notes=True: Models trained on an older database snapshot fail on newer entries.
  OVERLAPS: D3 (time split)
  OPEN: Computed data only. No one has done a publication-year split on Starrydata that I could find.
  https://arxiv.org/abs/2210.13597
- Borg et al. discovery metrics [opened] in_notes=False: Argues regression error does not predict discovery success; offers two discovery-level metrics.
  OVERLAPS: N2, N5
  OPEN: Simulated discovery campaigns on existing datasets. Not applied to TE.
  https://arxiv.org/abs/2210.13587
- Kapoor and Narayanan leakage taxonomy and model info sheets [opened] in_notes=False: Cross-field survey of leakage with a fill-in checklist.
  OVERLAPS: N5, D5
  OPEN: No materials examples. N5 can be the materials instance.
  https://arxiv.org/abs/2207.07048
- Alampara, Schilling-Wilhelmi, Jablonka evaluation cards [opened] in_notes=False: 2025 materials-specific paper on evaluation validity, with a documentation template.
  OVERLAPS: N5
  OPEN: General guidance. It has no worked XRD or TE case and no numbers like 12 / 17 / 32 of 40. N5 should cite it and fill one card.
  https://arxiv.org/abs/2503.10837
- Crusius et al. NoiseEstimator [memory] in_notes=False: Computes the best score a dataset's label noise allows; ships a package.
  OVERLAPS: N4, N2
  OPEN: Not opened (403). It assumes a stated error per dataset. The plan measures across-paper spread directly, which may be stronger. Check reuse before building N4.
  https://pubs.rsc.org/en/content/articlelanding/2025/fd/d4fd00091a
- Barua, Salla, Kleinke 2026 (ACS Omega) GroupKFold on Starrydata [opened] in_notes=False: TE property predictor that switched to composition-grouped folds to stop one compound at many temperatures straddling the split; tests on three outside sets.
  OVERLAPS: D3, N2, correction 21
  OPEN: Groups by composition only. No by-paper grouping, no random-versus-grouped numbers side by side, no frozen list, no noise ceiling.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC13470758/
- Na and Chang 2022, ESTM dataset and unseen-group test [opened] in_notes=True: Curated TE table (5,205 rows) with a test on material groups absent from training.
  OVERLAPS: D3, N2
  OPEN: Notes know ESTM as a dataset (and its spreadsheet-formula problem), not its unseen-group evaluation. README only; paper not opened. No licence stated.
  https://github.com/KRICT-DATA/SIMD
- Parse et al. 2024, Predicting High-Performance Thermoelectric Materials With StarryData2 [memory] in_notes=False: Gradient-boosted model on 18,126 Starrydata rows, 5-fold validation, R2 about 0.8.
  OVERLAPS: N2, correction 21 (candidate named example of a random split)
  OPEN: Page returned 403. Split type NOT confirmed. Do not cite as a random-split example until the methods section is read.
  https://onlinelibrary.wiley.com/doi/full/10.1002/adts.202400308
- Composition-grouped TE classifier with SHAP (2026, ScienceDirect S2667022426000952) [memory] in_notes=False: Search snippet says it uses composition-grouped validation with the formula as the group key.
  OVERLAPS: N2, correction 21
  OPEN: Not opened (403). Second sign that formula grouping is already practised in TE.
  https://www.sciencedirect.com/science/article/pii/S2667022426000952
- Katsura et al. 2022, data bias in Starrydata-based discovery [memory] in_notes=False: Paper by Starrydata's own group on how biased coverage distorts ML screening; uses clustering and an applicability-domain check.
  OVERLAPS: N2, N6
  OPEN: Not opened (403). Closest thing found to an existing TE evaluation audit. Must be read before N2 claims novelty.
  https://www.tandfonline.com/doi/full/10.1080/27660400.2022.2109447
- IOP review of AI for thermoelectrics (J. Phys. Energy, 10.1088/2515-7655/adba87) [opened] in_notes=False: 2025 review of TE ML.
  OVERLAPS: N2
  OPEN: Warns about tuning on the test set and poor extrapolation. Says nothing about grouped splits or same-compound temperature points. Supports the view that a by-paper audit is open.
  https://iopscience.iop.org/article/10.1088/2515-7655/adba87
- teMatDb self-consistency filter [opened] in_notes=True: TE database that flags records whose figure of merit disagrees with the value recomputed from its parts.
  OVERLAPS: N6
  OPEN: Covers 262 papers, not all of Starrydata. N6's power-of-ten and spreadsheet-formula detectors are not in it.
  https://arxiv.org/abs/2505.19150
- JARVIS-Leaderboard experimental category [opened] in_notes=True: Large community leaderboard with an experimental track built on inter-laboratory comparison.
  OVERLAPS: L2, L5, N5
  OPEN: Notes record that it has no experimental TE task. They do not record that an inter-lab experimental track already exists as a host. A hidden XRD or TE exam could be proposed there instead of built alone.
  https://arxiv.org/abs/2306.11688
- Leeman 2024 and the 2026 Nature author correction [opened] in_notes=False: The public dispute over tool-generated XRD identifications in an autonomous lab, and the authors' correction after manual re-analysis.
  OVERLAPS: D5, L3, L1, N1
  OPEN: Leeman is in gaps.md. The correction's content is in storyline.md but not in plan.md or gaps.md. Left open by both sides: a shared, written marking rule for ordered versus disordered variants.
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12872444/