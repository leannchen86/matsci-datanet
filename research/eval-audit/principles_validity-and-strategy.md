# principles validity-and-strategy

- P1 Name the decision and the decider: A score is never valid in general. It is valid for one stated use. Before building an eval, write who will decide what from its number.
  CHECK: For each planned eval item, can you fill in this line with a role outside this chat: 'ROLE will choose between A and B using this number'? Yes or no per item.
  SRC: Michael T. Kane 2013 Validating the Interpretations and Uses of Test Scores (J. Educational Measurement 50(1)) [opened] https://eric.ed.gov/?id=EJ996447; George Heilmeier / DARPA 1970s (DARPA page, current) The Heilmeier Catechism [opened] https://www.darpa.mil/about/heilmeier-catechism
- P2 Exam task must stand for real skill: Construct validity: the test task must exercise the skill the real job needs. Naming known powders in a weighed mixture (ground truth by recipe) is not the same skill as analysing a real reaction product with shifted, disordered, poorly crystalline or unlisted phases.
  CHECK: Is there measured evidence that tool rankings on weighed mixtures match tool rankings on real reaction products, for the same tools? If no, does every claim say 'on weighed mixtures' and nothing wider? Fail if neither.
  SRC: Abigail Z. Jacobs, Hanna Wallach 2021 Measurement and Fairness [opened] https://arxiv.org/abs/1912.05511; Raji, Bender, Paullada, Denton, Hanna 2021 AI and the Everything in the Whole Wide World Benchmark [opened] https://arxiv.org/abs/2111.15366; Fei, McDermott, Rom, Wang, Ceder 2025 Dara: Automated multiple-hypothesis phase identification and refinement from powder X-ray diffraction [opened] https://arxiv.org/html/2510.19667; Leeman, Liu, Stiles, Schoop and co-authors 2024 Challenges in High-Throughput Inorganic Materials Prediction and Autonomous Synthesis (PRX Energy 3, 011002) [opened] https://collaborate.princeton.edu/en/publications/challenges-in-high-throughput-inorganic-materials-prediction-and-/
- P3 Cover the failure modes that matter: Content validity: list the real-world ways phase identification fails first. Then count test items per failure mode. Empty rows are named gaps, not silence.
  CHECK: Does a written coverage table exist with rows such as: phase not in database; solid solution or shifted lattice; amorphous (non-crystalline) content; minor phase under about 5 wt%; preferred orientation; 4 or more phases; and a count of test items in each row? Yes or no.
  SRC: The Clay Minerals Society current page, contest since 2002 The Reynolds Cup (contest page) [opened] https://www.clays.org/reynolds/; Raven, Self 2017 Outcomes of 12 Years of the Reynolds Cup Quantitative Mineral Analysis Round Robin (Clays and Clay Minerals 65(2)) [memory] https://link.springer.com/article/10.1346/CCMN.2017.064054; Samuel R. Bowman, George E. Dahl 2021 What Will it Take to Fix Benchmarking in Natural Language Understanding? [opened] https://arxiv.org/abs/2104.02145
- P4 External validity before internal polish: First show the result transfers to the real setting, a second test set, or a second instrument. Only then tighten marking rules, intervals and splits.
  CHECK: Count planned desk-days by type. Are more days spent on internal validity (marking, ties, splits, noise) than on external validity (second measured set, second instrument or lab, real reaction products)? If yes, fail. Also: is every comparative claim backed by at least two independent test sets, or labelled 'one set, one instrument'?
  SRC: Liao, Taori, Raji, Schmidt 2021 Are We Learning Yet? A Meta Review of Evaluation Failures Across Machine Learning (NeurIPS Datasets and Benchmarks) [opened] https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/757b505cfd34c64c85ca5b5690ee5293-Abstract-round2.html; Dehghani, Tay, Gritsenko and co-authors 2021 The Benchmark Lottery [opened] https://arxiv.org/abs/2107.07002
- P5 Answer key independent of graded tools: If the ground truth was produced with help from a tool being graded, the score partly measures the tool agreeing with itself. Psychometrics calls this criterion contamination.
  CHECK: For each test set: was the answer key made by someone who had not seen any graded tool's output? Yes or no. For any planned specialist review: does the specialist mark blind first, before seeing the AI-drafted verdicts?
  SRC: Fei, McDermott, Rom, Wang, Ceder 2025 Dara: Automated multiple-hypothesis phase identification and refinement from powder X-ray diffraction [opened] https://arxiv.org/html/2510.19667; Michael T. Kane 2013 Validating the Interpretations and Uses of Test Scores [opened] https://eric.ed.gov/?id=EJ996447
- P6 Scoring rule must match the decision: Pick the metric from the decision it feeds, not from what is easy to compute or from a classification scheme.
  CHECK: Is each marking tier (strict formula, lenient formula, structure-level) tied in writing to a named downstream use, for example 'did the synthesis make the target compound' versus 'which structure family formed'? If tiers are justified only by a crystallography naming scheme, fail.
  SRC: Riebesell, Goodall, Benner and co-authors 2023 (rev. 2024) Matbench Discovery -- A framework to evaluate machine learning crystal stability predictions [opened] https://arxiv.org/abs/2308.14920; Matt Post 2018 A Call for Clarity in Reporting BLEU Scores [opened] https://arxiv.org/abs/1804.08771
- P7 Effect must beat noise and tool gap: A marking or split effect justifies a tool only if it is larger than sampling noise and changes which tool wins, on the data that matters.
  CHECK: On the target data (reaction products, not only the 40 weighed scans): does changing the marking rule flip any tool ranking, or move a score by more than the interval half-width? Yes or no. If no, stop N1.
  SRC: Card, Henderson, Khandelwal, Jia, Mahowald, Jurafsky 2020 With Little Power Comes Great Responsibility [opened] https://arxiv.org/abs/2010.06595; Evan Miller 2024 Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations [opened] https://arxiv.org/abs/2411.00640; Recht, Roelofs, Schmidt, Shankar 2019 Do ImageNet Classifiers Generalize to ImageNet? [opened] https://arxiv.org/abs/1902.10811; David J. Hand 2006 Classifier Technology and the Illusion of Progress [opened] https://arxiv.org/abs/math/0606441
- P8 Ask what gaming the exam breaks: Goodhart's law and consequential validity: before publishing a score, write how a tool could raise it without getting better at the real job, and what that tool would then get worse at.
  CHECK: Is there one written paragraph per eval that names the cheapest way to game it? If that way is easy (restrict the candidate list to the known chemical system; always pick the most common polymorph; always or never abstain), is there a guard or a narrower claim? Yes or no.
  SRC: David Manheim, Scott Garrabrant 2018 Categorizing Variants of Goodhart's Law [opened] https://arxiv.org/abs/1803.04585; Samuel Messick 1995 Validity of psychological assessment (American Psychologist 50(9), 741-749) [memory] https://doi.org/10.1037/0003-066X.50.9.741
- P9 One outside adopter before any build: An eval with no user outside its author is a private unit test. Get one named outside role to say 'I would use this' before building past the test stage.
  CHECK: Has one role outside this chat (a maintainer of the open phase-ID tool, one diffraction specialist, or one benchmark maintainer) been shown the 40-row result and replied? Yes or no. Today: no.
  SRC: Kiri L. Wagstaff 2012 Machine Learning that Matters [opened] https://arxiv.org/abs/1206.4656; Koch, Denton, Hanna, Foster 2021 Reduced, Reused and Recycled: The Life of a Dataset in Machine Learning Research [opened] https://arxiv.org/abs/2112.01716; George Heilmeier / DARPA 1970s (DARPA page, current) The Heilmeier Catechism [opened] https://www.darpa.mil/about/heilmeier-catechism
- P10 Evaluation data over evaluation commentary: The scarce thing is trusted measured test items, not more opinions about benchmarks. Prefer work that adds or repairs records someone else can load.
  CHECK: For each item: does it end with new or corrected measured records (rows, labels, provenance) that a stranger can load? Or only with a function or a note about evals? Count each kind. If functions and notes outnumber record-producing items in the first month, fail.
  SRC: Alampara, Schilling-Wilhelmi, Jablonka 2025 Lessons from the trenches on evaluating machine-learning systems in materials science [opened] https://arxiv.org/abs/2503.10837; Kapoor, Cantrell, Peng and co-authors 2023 REFORMS: Reporting Standards for Machine Learning Based Science [opened] https://arxiv.org/abs/2308.07832; Sambasivan, Kapania, Highfill, Akrong, Paritosh, Aroyo 2021 Everyone wants to do the model work, not the data work: Data Cascades in High-Stakes AI (CHI 2021) [memory] https://dl.acm.org/doi/10.1145/3411764.3445518
- P11 Newcomer claims must be checkable: A newcomer's critique is believed only if a stranger can re-run it from public files, every headline is scoped to what was measured, and one domain person has checked the domain calls.
  CHECK: Three yes/no tests. (a) Can a stranger reproduce every headline number from public inputs with one command? (b) Does every headline sentence carry 'on these N scans in our set-up'? (c) Has one specialist checked the domain verdicts, marking blind first?
  SRC: Sayash Kapoor, Arvind Narayanan 2022 Leakage and the Reproducibility Crisis in ML-based Science [opened] https://arxiv.org/abs/2207.07048; Koch, Denton, Hanna, Foster 2021 Reduced, Reused and Recycled: The Life of a Dataset in Machine Learning Research [opened] https://arxiv.org/abs/2112.01716
- P12 Search prior art before each build: Spend one to two hours searching before each build. Then shrink the item to the gap that is left.
  CHECK: Does each build item name its closest existing tool or paper and give one sentence on what that tool does not do? Items failing today: N1, N2, N4, N5, D4.
  SRC: Hicks, Toher, Ford and co-authors 2021 AFLOW-XtalFinder: a reliable choice to identify crystalline prototypes (npj Comput. Mater. 7, 30) [opened] https://arxiv.org/abs/2010.04222; Sun, Li, Imamura, Ohishi, Wolverton, Kurosaki 2025 (rev. 2026) Lattice-to-Total Thermal Conductivity Ratio: A Phonon-Glass Electron-Crystal Descriptor for Data-Driven Thermoelectric Design [opened] https://arxiv.org/abs/2511.21213; Meredig, Antono, Church and co-authors 2018 Can machine learning identify the next high-temperature superconductor? Examining extrapolation performance for materials discovery [opened] https://citrine.io/can-machine-learning-identify-the-next-high-temperature-superconductor-examining-extrapolation-performance-for-materials-discovery/; Crusius, Cipcigan, Biggin 2025 Are we fitting data or noise? Analysing the predictive power of commonly used datasets in drug-, materials-, and molecular-discovery (Faraday Discussions) [memory] https://pubs.rsc.org/en/content/articlelanding/2025/fd/d4fd00091a
- P13 Do the fork-deciding step first: Order work by uncertainty removed per day. Run slow, decisive asks in parallel from day one. Give every item a written kill result.
  CHECK: Is the step that decides the fork (will one diffraction specialist engage) scheduled before, or in parallel with, the desk builds that depend on it? Yes or no. Does every item have one sentence: 'if we see X, we stop'? Yes or no.
  SRC: George Heilmeier / DARPA 1970s (DARPA page, current) The Heilmeier Catechism [opened] https://www.darpa.mil/about/heilmeier-catechism
- P14 Hidden exam needs a standing referee: A real benchmark needs three things: sequestered test data, a referee who scores submissions, and enrolled competitors. Without all three, call it a practice exam and promise nothing more.
  CHECK: Does the plan name who will hold the hidden answers, score entries, and keep doing so for years? If no, is every output labelled 'practice exam' or 'one-off blind check'? Fail if neither.
  SRC: David Donoho 2017 50 Years of Data Science (J. Computational and Graphical Statistics 26(4)) [memory] https://www.tandfonline.com/doi/full/10.1080/10618600.2017.1384734; The Clay Minerals Society current page, contest since 2002 The Reynolds Cup (contest page) [opened] https://www.clays.org/reynolds/

## prior art
- Dara paper's own benchmark (Fei et al. 2025, arXiv 2510.19667) [opened] in_notes=True: The open phase-ID tool's own test: 10 binary + 10 ternary weighed precursor mixtures at 2-minute and 8-minute scans (Dara 18/20 and 20/20; commercial tool 16/20 and 18/20), plus 20 reaction products scored as 'all peaks indexed' against one expert who used the tool's suggestions.
  OVERLAPS: D1 (40-row marking test), N1, N3, L1; also the '20 reaction products' numbers in plan correction 2
  OPEN: Notes know the tool and the 16/15/7 scores but NOT that the 8-minute set is at ceiling, that 'correct' on mixtures means all phases and no spurious ones, or that the reaction-product key was made with the tool's suggestions. No independent, blind answer key for reaction products exists. No scoring script was confirmed (not checked this run).
  https://arxiv.org/html/2510.19667
- AFLOW-XtalFinder (Hicks et al. 2021) [opened] in_notes=False: Open-source Python and command-line tool that decides whether two crystal structures are the same at several similarity levels (same symmetry skeleton; same skeleton and similar geometry), with a numeric misfit.
  OVERLAPS: N1 tiered marking function; D1 tricky-pairs verdicts
  OPEN: It compares structures, not phase-ID answers. It does not clean formula text, has no 'cannot tell' verdict, and does not map a tool's answer list to a per-scan mark. Whether its levels equal the 1990 classification tiers was not confirmed. N1 could shrink to a thin wrapper plus the verdict table.
  https://arxiv.org/abs/2010.04222
- pymatgen StructureMatcher [memory] in_notes=True: Widely used open Python routine that tests whether two crystal structures match within tolerances.
  OVERLAPS: N1, D1
  OPEN: From memory, docs not opened this run. Gives match or no-match, not graded tiers tied to a decision. Same gap as above.
  https://pymatgen.org
- Alampara, Schilling-Wilhelmi, Jablonka 2025, 'Lessons from the trenches on evaluating machine-learning systems in materials science' [opened] in_notes=False: A review of materials-ML evaluation through measurement theory (construct validity, data quality, metrics, benchmark upkeep). Proposes 'evaluation cards'.
  OVERLAPS: N5 'four questions' note; the whole framing of this review
  OPEN: General to materials ML. Abstract shows no worked powder-XRD phase-ID example with numbers. The 40-row table could serve as one worked example of their point, which is a smaller and more credible contribution than a new note.
  https://arxiv.org/abs/2503.10837
- REFORMS (Kapoor et al. 2023) [opened] in_notes=False: A 32-question reporting checklist for ML-based science, built by 19 researchers for authors, reviewers and editors.
  OVERLAPS: N5
  OPEN: Not materials-specific and says nothing about answer-key marking rules. N5 should cite it and add at most the one or two questions it lacks.
  https://arxiv.org/abs/2308.07832
- BetterBench (Reuel et al. 2024) [opened] in_notes=False: 46 best practices for benchmarks, applied to 24 AI benchmarks; finds most do not report statistical significance or allow easy replication. Ships a checklist and a living site.
  OVERLAPS: N5, D4
  OPEN: No materials benchmarks assessed, as far as the abstract shows. Applying its checklist to one or two XRD benchmarks is a possible small item, but it is still commentary.
  https://arxiv.org/abs/2411.12990
- Kapoor and Narayanan 2022, 'Leakage and the Reproducibility Crisis in ML-based Science' [opened] in_notes=False: A survey of train-test leakage across 17 fields and 329 papers, with a taxonomy and model info sheets.
  OVERLAPS: D3, N2 (TE split audit)
  OPEN: Unknown whether thermoelectrics or Starrydata appears in their list; I did not check. It is the template for how an outsider audit earns trust: named papers, reproducible code.
  https://arxiv.org/abs/2207.07048
- Meredig et al. 2018, leave-one-cluster-out cross-validation (LOCO-CV) [opened] in_notes=False: Shows random cross-validation overstates materials-ML performance; proposes holding out whole chemical clusters and a nearest-neighbour baseline.
  OVERLAPS: D3, N2
  OPEN: Clusters by chemistry, not by source paper. Paper-level (DOI-grouped) leakage on TE data is still open, but plan correction 17 says it is the smaller effect (24.8% to 29.4%).
  https://citrine.io/can-machine-learning-identify-the-next-high-temperature-superconductor-examining-extrapolation-performance-for-materials-discovery/
- Sun et al. 2025, Starrydata thermoelectric model with formula-grouped split (arXiv 2511.21213) [opened] in_notes=False: A TE machine-learning paper on Starrydata (about 72 thousand entries) that keeps all entries of one reduced formula on the same side of the split.
  OVERLAPS: D3, N2
  OPEN: Groups by formula, not by paper. Reports no random-vs-grouped comparison. No frozen DOI list. It weakens N2's premise that TE papers split at random; what is left is the paper-level residual and a reusable frozen split.
  https://arxiv.org/abs/2511.21213
- Two 2026 TE machine-learning papers using GroupShuffleSplit by formula (ScienceDirect) [memory] in_notes=False: Search results indicate two further TE papers that group the split by chemical formula.
  OVERLAPS: N2
  OPEN: Seen in search snippets only; not opened, details unverified. If confirmed, formula-grouped splitting is becoming normal in TE and N2 shrinks further.
  https://www.sciencedirect.com/science/article/pii/S0264127526011068 ; https://www.sciencedirect.com/science/article/pii/S2667022426000952
- Crusius, Cipcigan, Biggin 2025, NoiseEstimator [memory] in_notes=False: A paper and Python package that derive the best achievable model score from experimental error, applied to nine drug, materials and molecular datasets.
  OVERLAPS: N4 noise ladder
  OPEN: Snippet only (page returned 403). Unknown whether any TE or Starrydata set is covered. The separate rungs in N4 (re-reading noise 0.48%, within-paper 12.9%, across-paper 32.7%) may still be new data; the method is not.
  https://pubs.rsc.org/en/content/articlelanding/2025/fd/d4fd00091a
- Miller 2024 'Adding Error Bars to Evals' and Card et al. 2020 'With Little Power Comes Great Responsibility' [opened] in_notes=False: Standard recipes for intervals, paired differences, clustered errors and power analysis in ML evals; evidence that small test sets mislead.
  OVERLAPS: D4 tie function; L2 sample-size sums
  OPEN: Nothing methodological. D4 is a convenience wrapper over textbook statistics. Its value is only in being switched on by default in the user's own scripts.
  https://arxiv.org/abs/2411.00640 ; https://arxiv.org/abs/2010.06595
- sacreBLEU (Post 2018) [opened] in_notes=False: A shared scorer that ended configuration-driven spread (up to 1.8 points) in a translation metric.
  OVERLAPS: D1, N1 (the 'standard marker' idea)
  OPEN: Mentioned on the big-picture page but not in plan.md or gaps.md. Caution on the analogy: sacreBLEU worked because many groups already reported the same metric. For XRD phase ID there is no shared metric community yet, so a scorer alone has no one to standardise.
  https://arxiv.org/abs/1804.08771
- Reynolds Cup (Clay Minerals Society) and its 12-year review (Raven and Self 2017) [opened] in_notes=True: Biennial blind contest on weighed realistic mineral mixtures, about 100 sample sets, human analysts, any method, scored by summed absolute weight error.
  OVERLAPS: D6, N3, L2
  OPEN: Contest is in gaps.md (G20); the 2017 review paper is not (snippet only, not opened). It is minerals, human-run, and scores amounts, not machine phase naming on synthesis products. The page did not confirm the price of past samples quoted in the notes. Left open: a machine-scored test on real reaction products.
  https://www.clays.org/reynolds/
- Matbench Discovery (Riebesell et al.) [opened] in_notes=True: A materials benchmark that aligns its metric with the discovery decision and argues for prospective testing.
  OVERLAPS: P6 precedent; N5; any future leaderboard idea
  OPEN: It is about computed stability, not measured data. It is the pattern to copy for 'metric follows decision', not a competitor.
  https://arxiv.org/abs/2308.14920
- Leeman et al. 2024 critique of an autonomous lab's phase analysis (PRX Energy) [opened] in_notes=True: Re-analysis arguing two thirds of claimed new compounds were likely known disordered phases, and that automated whole-pattern fitting is not yet reliable.
  OVERLAPS: P2 construct; L2; content coverage for D1/N3
  OPEN: In gaps.md but not connected to the plan's test content. It says the consequential failure mode is disorder and solid solutions. No planned test item contains that.
  https://collaborate.princeton.edu/en/publications/challenges-in-high-throughput-inorganic-materials-prediction-and-/
- Harder public measured mixture sets already listed in gaps.md G20 (IUCr quantitative round robins 2001/2002, a 2023 set of 240 two-phase mixtures, others) [memory] in_notes=True: Public weighed-mixture XRD sets with more phases or harder conditions than the 40 scans.
  OVERLAPS: D6, N3
  OPEN: Not re-verified this run. Under this lens they are the cheapest route to a second independent test set (P4) and should move ahead of N1, N4 and N5. They are still known powders, so they do not fix P2 or P3.
  see gaps.md G20 (not re-opened this run)