# Glossary, user model, and where the old reports lose a newcomer

Built from all 32 digest files (C01–C11, C15, N00, R01–R10). Nothing here is new research. Every number is copied from a digest, with its denominator.

Status tags used on claims:
- [OWN-EXPERIMENT] = the sessions measured it on real files.
- [SOURCE] = a paper, dataset page or company page says it.
- [OPINION] = a judgment or deduction made in the sessions (or, where marked "this file", by this synthesis).
- [REFUTED] = an earlier claim that a later check overturned. The corrected value is given.

Report ids used below:
- R01 Materials Record Wall. R02 Record Wall Debrief.
- R03 Toward a Materials ImageNet. R04 Materials ImageNet Debrief.
- R05 Discovered Materials Data Gaps. R06 Discovered Materials Debrief.
- R07 Thermoelectric Benchmark Spec (draft 0.2). R08 DFT vs Experiment Debrief.
- R09 Recursion in Materials AI. R10 XRD Curation Experiments.

---

## Part 1. The 40 terms a reader must know

Read top to bottom. Each group builds on the one before.

The 12 most essential are marked **[ESSENTIAL]**. They are: specimen vs composition, phase, DFT, Matbench, powder XRD pattern, Rietveld refinement, known-answer test, Seebeck coefficient, zT, Starrydata, leakage, paper-grouped split.
Next tier if the reader has five more minutes: round robin, RRUFF, blind test.

### A. What one "data point" is in materials science

**1. Composition vs specimen [ESSENTIAL]**
- Plain: Composition is the chemical formula (Bi2Te3). A specimen is one physical piece of material, with its own processing history.
- ML analogy: composition is the class name; the specimen is the individual image. Most open tables store only the class name.
- Why here: the same formula gives very different measured values. 647 compositions appear in 2+ papers; the median between-paper difference in Seebeck coefficient is 32.7%, and 3,881 of 21,856 paper pairs (17.8%) even disagree on the sign [OWN-EXPERIMENT]. Even an "oracle" that knows the answers and returns the same-composition median misses by 15.0% [OWN-EXPERIMENT]. So "composition -> property" has a hard ceiling. The missing information is the specimen description.

**2. Phase (and "target phase") [ESSENTIAL]**
- Plain: one distinct crystalline substance inside a sample. A real powder is often a mixture of several phases ("multiphase"). The target phase is the one the chemist was trying to make.
- ML analogy: the sources in a source-separation problem. "Did the target phase form?" is the success label of a synthesis.
- Why here: almost every XRD question in this project is "which phases are in this powder, and how much of each?" That label is often ambiguous.

**3. Polymorph and handedness**
- Plain: polymorphs share a formula but have different crystal structures (alpha vs beta quartz; cubic vs hexagonal diamond). "Handedness" (enantiomorphs) means two mirror-image versions of one structure, e.g. quartz filed as space group #152 in one database and #154 in another.
- ML analogy: polymorphs are different classes with the same text label. Mirror images are duplicates that a naive join treats as different.
- Why here: formula-only models cannot separate polymorphs [SOURCE]. Joins by space-group number silently drop mirror-image records [OWN-EXPERIMENT]. The standard matching tool (pymatgen StructureMatcher) merges mirror images in 36/36 tests. That is correct for powder XRD, but its defaults also merge alpha and beta quartz (RMS 0.169) [OWN-EXPERIMENT]. The first reading, "the matcher has a bug", is [REFUTED].

**4. Precursor**
- Plain: a starting powder that goes into the furnace. A recipe = precursors + temperature + time + atmosphere.
- ML analogy: an input feature that also defines the right grouping unit for splits.
- Why here: on the Precursor Genome synthesis ledger, holding out a whole precursor drops outcome macro-F1 from 0.53 to 0.42 (rerun 0.49 to 0.39). Grouping by chemical system barely changes anything [OWN-EXPERIMENT]. So for synthesis data the fair split unit is the precursor.

**5. CIF, space group, esd**
- Plain: a CIF is the standard text file that describes a crystal structure. The space group is the symmetry label (a number 1–230). An esd is the small error bar written as "4.9134(2)".
- ML analogy: CIF is the annotation file format; the space group is a categorical field used as a join key; esd is a per-value uncertainty.
- Why here: they are the keys used to join records across databases, and they break quietly (see term 3).

### B. Simulated data: what exists in bulk, and what this project is not mainly about

**6. DFT, and "functional" [ESSENTIAL]**
- Plain: density functional theory. A quantum simulation of an ideal, perfect crystal at 0 K. The "functional" (PBE/GGA, r2SCAN, HSE06) is the approximation used inside it.
- ML analogy: synthetic labels from a biased simulator. Different functionals are different annotators with different systematic bias. A database recompute is a relabel.
- Why here: almost all large materials datasets are DFT, not measurements. The user drew the line: "dft-computed data is quite different from experimental data". Worked example on quartz: PBE cell volume is +6.3% vs experiment, r2SCAN +0.37%; the computed band gap is 5.72 eV vs 8.9 eV measured optically [OWN-EXPERIMENT + SOURCE]. Materials Project energies include a correction of −0.687 eV per oxygen atom that was fitted to experiment [SOURCE]. So "DFT -> experiment" benchmarks can leak labels.

**7. Formation energy, convex hull, energy above hull (E_hull)**
- Plain: formation energy is the energy released when a compound forms from its elements. The convex hull is DFT's ranking of which compounds are stable. E_hull is the distance from that ranking; near 0 means "predicted stable".
- ML analogy: a stability score. It is not a "can be made" label.
- Why here: 50.5% of observed phases are metastable, median 15 meV/atom above the hull (Sun 2016) [SOURCE]. Of GNoME's 2.2 million below-hull predictions, 736 had been independently made [SOURCE]. Reading hull position as existence is a recurring trap.

**8. Materials Project (MP)**
- Plain: the largest open database of DFT-computed crystal properties.
- ML analogy: a huge pretraining corpus of simulator outputs.
- Why here: many benchmarks are cut from it. The user: "the materials project is all dft - computed data, no?" All MP-side builds are now parked. One finding stands: MP serves a misspelled field, `energy_uncertainy_per_atom`, which is empty on 342,144 documents [OWN-EXPERIMENT].

**9. GNoME**
- Plain: Google DeepMind's release of DFT-predicted "stable" crystals.
- ML analogy: a very large generated candidate set, scored by the simulator, mostly unverified in the lab.
- Why here: it is the usual example of "discovery" being counted in simulation. Switching the functional from PBE to r2SCAN flips the stable/unstable call for 22.1% of 117,043 entries (4.8% with a 25 meV/atom buffer) [OWN-EXPERIMENT]. Licence is CC BY-NC.

**10. MLIP (machine-learned interatomic potential)**
- Plain: a neural network trained to imitate DFT energies and forces, much faster.
- ML analogy: a learned surrogate simulator. The big ones (MACE-MP, CHGNet, MatterSim, UMA) play the role of a pretrained backbone.
- Why here: values "computed" by an MLIP are two steps from a measurement. At Discovered Materials, agents are asked for "measured" thermal conductivity that is in fact MLIP-computed; the export shows 504 mlip / 22 mlip-verified / 0 dft provenance [OWN-EXPERIMENT on company files].

**11. Matbench [ESSENTIAL]**
- Plain: the standard suite of 13 property-prediction tasks (312 to 132,752 samples) with a public leaderboard.
- ML analogy: the GLUE/UCI-style leaderboard for materials property prediction.
- Why here: it shows what the field's "exam" looks like today. Most tasks use DFT labels. It has no thermoelectric task and no XRD task [SOURCE]. Its rows drop the source id and version. Its one steel task averages 842 records into 312 rows; one group of 53 records spanning 1005.9–1605.4 MPa became the single value 1338.0 [OWN-EXPERIMENT].

### C. X-ray diffraction (XRD): the measurement every synthesis lab uses

**12. Powder XRD pattern [ESSENTIAL]**
- Plain: shine X-rays on a powder and record intensity vs angle. The result is a 1-D curve of peaks. Peak positions come from the crystal lattice spacing; peak heights come from which atoms sit where.
- ML analogy: a spectrogram that you must decompose into known sources.
- Why here: it is the first check after every synthesis, so it is the natural "image" of a materials ImageNet. Limits [SOURCE]: X-rays scatter off electrons, so lithium is nearly invisible and Mn/Fe/Co/Ni look alike; it is blind to non-crystalline material and to phases below roughly 1–5%.

**13. Phase identification**
- Plain: deciding which phases are in the pattern.
- ML analogy: open-set, multi-label classification with no cheap verifier.
- Why here: it is the task behind Periodic Labs' benchmark, behind Dara, and behind the user's own local project (dara-conform: calibrated confidence and abstention on top of Dara). Historic anchor: in the 2002 Search-Match Round Robin, 1 of 25 participants found all 10 phases at the first step [SOURCE].

**14. Rietveld refinement and Rwp [ESSENTIAL]**
- Plain: fit a simulated pattern, built from candidate phases, to the measured one. Rwp is the misfit number. The fit also gives the weight fraction of each phase.
- ML analogy: analysis-by-synthesis. Rwp behaves like a training loss: you can lower it by adding phases. It can rule answers out, but it cannot prove one right. As a reward it is hackable.
- Why here: the "label" in XRD datasets is a refinement result, not ground truth. Four different three-phase answers gave a near-identical fit on one Dara pattern [OWN-EXPERIMENT]. On Precursor Genome, the human fit and the software fit list different phases in 316 of 343 scans [OWN-EXPERIMENT]. That is machine-vs-human, not rater-vs-rater: all 1,216 of 1,216 verifications carry one editor id.

**15. Calculated vs measured pattern**
- Plain: a calculated pattern is simulated from a known structure. A measured one comes from a real sample on a real instrument.
- ML analogy: synthetic vs real data; the sim-to-real gap.
- Why here: open archives mix the two without saying so (see RRUFF, opXRD). Simulating forward is cheap: 0.3–13 ms per pattern on the user's machine, about 2 core-hours for 1 million [OWN-EXPERIMENT]. So the user's idea "distill the simulator" is partly [REFUTED]: simulate-then-train has been standard since about 2017 [SOURCE]. The scarce thing is trusted real patterns with known answers.

**16. COD vs ICSD / ICDD, and "crosswalk"**
- Plain: databases of reference crystal structures. COD is open (CC0, 534,931 entries). ICSD (335,032 entries) is paid and restricted. ICDD's terms bar ML/AI use. A crosswalk is a table that maps ids from one database to another.
- ML analogy: the label vocabulary. Here the vocabulary is paywalled.
- Why here: in Precursor Genome, 745 of 755 phase labels carry ICSD ids and 0 carry COD or Materials Project ids [OWN-EXPERIMENT]. Any redistributable benchmark needs a crosswalk to open ids first.

**17. RRUFF**
- Plain: a University of Arizona database of mineral samples with Raman spectra, XRD patterns and chemistry. 9,858 samples, 4,349 public. No licence stated. The user asked "what's rruff?".
- ML analogy: a small, hand-collected reference set that everyone reuses without reading the datasheet.
- Why here: 1,702 of 3,019 "RAW" powder files (56.4%) declare a calculated profile. A noise-signature test separates calculated from measured at AUC 0.998. Only 2.4% of RAW files state the X-ray wavelength. 11 file pairs hold identical data under two mineral names [OWN-EXPERIMENT].

**18. opXRD**
- Plain: an open collection of 92,552 experimental powder patterns from several institutions; 2,179 are labelled.
- ML analogy: a large, mostly unlabelled pool.
- Why here: in a checked slice of 2,680 patterns, 501 are unlabelled; 485 (18.1%) are multi-phase (an earlier count of 41.4% is [REFUTED]); 124 are exact duplicates in 61 groups, 15 groups with conflicting labels; all 499 patterns from one contributor copy RRUFF files, and 414 of those are calculated but deposited as "not simulated" [OWN-EXPERIMENT]. Usable pool across archives: 1,683 of 7,183 files. Only 353 have a real wavelength, and 352 of those come from one institution [OWN-EXPERIMENT].

**19. A-Lab**
- Plain: the autonomous (robotic) synthesis lab at Berkeley. It mixes powders, fires them, runs XRD, and decides the next try.
- ML analogy: a closed-loop agent whose reward comes from automated XRD analysis.
- Why here: its headline was corrected in January 2026 from 41 of 58 targets made to 36 of 57 (63%) [SOURCE]; the old number is [REFUTED]. Leeman et al. argue the phase analysis neglected disorder [SOURCE]. It is the public example of "the XRD label was the weak link".

**20. Precursor Genome (PG) and A-Lab GPSS**
- Plain: two open synthesis ledgers with XRD scans. PG: 1,035 samples, 1,351 scans, CC BY. GPSS: 352 samples.
- ML analogy: the closest thing to (recipe -> outcome) training data, with failures included.
- Why here: PG logs failures as richly as successes (369 unreacted, 113 partially reacted, 26 physical failures) [OWN-EXPERIMENT]. Problems found: furnace logs fall short of the programmed hold in 118 of 981 runs; an undocumented 100 mg pass/fail threshold; strict wrong values on 93 samples (9.0%). An earlier "28% carry an error" is [REFUTED].

**21. Dara (and Jade)**
- Plain: Dara is an open automated phase-identification tool with a small benchmark of 20 reactions and 40 scans of hand-weighed mixtures. Jade is the commercial software it is compared with.
- ML analogy: two baselines on a tiny gold test set.
- Why here: Dara scores 38/40 and Jade 35/40; the intervals overlap, so 40 scans cannot rank methods [OWN-EXPERIMENT]. Nearly all errors are on 2-minute scans; 8-minute scans are near ceiling. The spelling of a formula alone (BiVO4 vs VBiO4) flips 3 of 20 of Jade's verdicts [OWN-EXPERIMENT].

**22. Known-answer test (weighed mixture) [ESSENTIAL]**
- Plain: mix powders at known weights, then measure. The right answer is known by construction.
- ML analogy: ground truth by construction, like a synthetic test with real sensors.
- Why here: it is the only true answer key for XRD. Dara's 40 scans are the only ones on disk. The main session's fourth problem is "for some tasks there is no answer key" [OPINION]. The XRD session calls a harder hidden version, made with a partner lab, "the actual ImageNet-style seed" [OPINION].

**23. Hard pattern**
- Plain: a term made up inside R10, not a field standard. It means a pattern whose fitted answer has 4 or more phases at 1 wt% or more each.
- ML analogy: the hard subset of a test set.
- Why here: only 167 exist in the open data checked (PG 157 of 1,035 + GPSS 10 of 352). About 270 are needed for a usable agreement estimate [OWN-EXPERIMENT]. The user had to ask "what do 'hard patterns' mean?"

**24. Handling history**
- Plain: what happened to a sample between the furnace and the instrument: air, humidity, grinding, storage time.
- ML analogy: an unrecorded covariate that causes distribution shift.
- Why here: none of PG's 115 fields records it, and 13 handling words get 0 hits in PG free text. Samples re-scanned more than 180 days later changed their fitted phase set in 105 of 136 cases (77%), vs 12 of 25 (48%) for gaps of 30 days or less [OWN-EXPERIMENT, exploratory]. Without handling history, sample aging and fitting drift cannot be told apart.

### D. Thermoelectrics (TE): the property family with the best open data

**25. Thermoelectric material; Seebeck coefficient S [ESSENTIAL]**
- Plain: a thermoelectric material turns a temperature difference into voltage. S is volts per degree. Its sign says whether the material conducts by electrons (n-type) or holes (p-type).
- ML analogy: a regression target whose sign is also a class label. A sign error is a wrong class, not noise.
- Why here: S is the main target of the proposed TE benchmark. Reported values for Bi2Te3 across 111 papers range from −241 to +280 µV/K [OWN-EXPERIMENT].

**26. Resistivity ρ and thermal conductivity κ**
- Plain: how hard it is to push current through (ρ), and how well heat flows (κ). κ is slow to measure: it needs three separate quantities.
- ML analogy: two more regression targets with different noise levels.
- Why here: labs agree on S to about 6%, ρ 8%, κ 11% (Alleno 2015 round robin) [SOURCE]. That is why the spec starts with S and ρ only. Trap: "kappa" also means Cohen's kappa (rater agreement) in R05/R06.

**27. zT [ESSENTIAL]**
- Plain: the figure of merit, zT = S² · T / (ρ · κ). It is computed from the other three curves.
- ML analogy: a derived label that works as a checksum. Recompute it and compare with what the paper reported.
- Why here: of 13,702 checked Starrydata samples, 646 are off by more than 50%, and 266 of those are clean powers of ten (unit errors) [OWN-EXPERIMENT]. This free check is why TE was picked. Two early hopes are [REFUTED]: "most unit errors are fixable" (only 85 of 266), and "an automatic fix is safe" (measured false-fix rate 7.2%, low confidence). Fixes stay as suggestions in a review queue (633 specimens, 230 papers).

**28. Starrydata (with teMatDb and ESTM) [ESSENTIAL]**
- Plain: an open (CC BY) database of curves read off figures in published thermoelectric papers: 55,422 samples, 156,721 curves, 9,512 papers (snapshot 2026-09-14). teMatDb (272 samples) and ESTM (5,205 rows) are smaller, overlapping sets.
- ML analogy: the largest open training pool of experimental labels in this project. The three sets are partly independent annotations of the same papers.
- Why here: it is the data behind the TE line. Most descriptors are missing: relative density on 4.4% of samples, grain size 1.7%, measurement direction on 12 of 55,422; 7 of 28 proposed specimen fields exist in no source [OWN-EXPERIMENT]. The sets share papers (193 / 75 / 7 shared DOIs), but plain string matching finds only 183 / 26 / 4 [OWN-EXPERIMENT]. That is a cross-dataset leak.

**29. Digitisation**
- Plain: reading numbers off a plot image in a paper.
- ML analogy: the annotation step.
- Why here: it is not the bottleneck. Two independent digitisations of the same figure agree within 2% in 98 of 100 pairs (median 0.45%) [OWN-EXPERIMENT]; a later round found medians of 0.48–0.91% across 361 comparisons, with 15 of 361 more than 10% apart [OWN-EXPERIMENT]. The big gaps turned out to be record errors (Celsius stored as kelvin, sign flips, swapped curves), not reading scatter. A second reading therefore doubles as an error detector.

**30. Round robin, reference material (SRM), z′ score**
- Plain: a round robin sends the same sample to many labs to see how much they disagree. A reference material (NIST SRM 3451, BCR-724) is a certified sample with a known value. A z′ score expresses a prediction error in units of that between-lab spread.
- ML analogy: inter-annotator agreement for instruments; a calibration example; error normalised by label noise.
- Why here: it gives the noise floor: S 6%, ρ 8%, κ 11%, zT 19% (Alleno 2015) [SOURCE]. Model error under a fair split is 42.2%. So there is a large gap between label noise and model error, and the benchmark can say which model differences are real. Two earlier claims are [REFUTED]: "no certified κ reference exists" (BCR-724 does) and "reproducibility SD >= 20%" (R07 reports this only as the round-robin authors' expectation, not a measurement).

### E. Evaluation terms, as used in this project

**31. Leakage [ESSENTIAL]**
- Plain: test items that are not truly new to the model.
- ML analogy: the usual meaning. Here the leak runs through the paper: samples from one paper share a lab, a batch and a method.
- Why here: under a random split of Starrydata, the test sample's own paper is already in training 93.5% of the time [OWN-EXPERIMENT]. Other leak routes found: the same paper in two databases; near-duplicate steel compositions in 66 of 312 Matbench groups; DFT corrections fitted to the experimental values later used as test labels.

**32. Paper-grouped split [ESSENTIAL]**
- Plain: keep all samples from one paper (one DOI) on the same side of the split.
- ML analogy: GroupKFold by DOI; like splitting by patient instead of by scan.
- Why here: it is the project's clearest single result. Median Seebeck error goes from 25.5% (random split) to 42.2% (papers held out), on 12,222 samples from 3,015 papers [OWN-EXPERIMENT]. The right grouping unit differs by dataset: paper for TE, precursor plus furnace run for synthesis, duplicate group plus cross-archive hash for XRD [OWN-EXPERIMENT]. Holding out a "chemical system" is weaker than it sounds.

**33. Blind test (hidden labels; CASP, ILSVRC)**
- Plain: the organisers keep the answers secret until predictions are in. Best case: the answers are measured fresh, so they exist nowhere online.
- ML analogy: a held-out test server. ImageNet was a sequence: the 2009 dataset, then the ILSVRC contest with hidden labels, then AlexNet at 15.3% vs 26.2% top-5 error [SOURCE].
- Why here: the sessions judged protein structure's PDB + CASP a closer analogy than ImageNet [OPINION]. No blind TE test with new measurements was found (a negative search, not proof) [SOURCE]. PG, GPSS and Dara publish their answers, so none of them can be the hidden split [OPINION].

**34. Pre-registration**
- Plain: write down the hypothesis and the pass/fail rule before looking at the data.
- ML analogy: fixing the eval protocol before training.
- Why here: R10's seven XRD hypotheses (H1–H7) and the later curation rounds work this way. The sessions also admit a weakness: some registered checks passed by construction [OWN-EXPERIMENT].

**35. Noise floor and minimum detectable difference**
- Plain: the smallest gap between two models that a test set of a given size and label noise can show.
- ML analogy: confidence intervals on benchmark scores.
- Why here: a 134-item test gives about ±4.3 points standard error. About 270 items give ±5 points on an agreement rate. About 770–1,570 items are needed to resolve a 5-point gap between models [OWN-EXPERIMENT arithmetic]. This sizes every proposed benchmark. It is also why Periodic Labs' 55.3% vs a rival's ~53% is a statistical tie.

**36. Censored values, selective labels, negative results**
- Plain: a value recorded as ">300" is censored: you know a bound, not the number. Selective labels means you only see outcomes for the cases someone chose to run. Negative results are failed attempts, which are rarely published.
- ML analogy: survival-analysis censoring; selection bias; missing negatives in the training set.
- Why here: one alloy table turned ">300" into 300.0 and "150-200" into 175.0, so 382 cells now look exact; "±" was deleted from 264 cells; a polymer table stores std "0.0" on 7,088 of 7,367 rows where it means n=1 [OWN-EXPERIMENT]. A superconductor review marks 332 of 671 compounds (49.5%) as "impossible to obtain the target phase", but only by cell background colour; the mark survives text extraction in 0 of 671 cells [OWN-EXPERIMENT]. At Discovered Materials, refused recipes are never run, so a refusal can never be proved wrong [OPINION].

**37. LLM-as-judge, recipe grader, reward hacking**
- Plain: using a language model to score answers or recipes against a rubric.
- ML analogy: a reward model checked against annotator preference, not against ground truth.
- Why here: Discovered Materials' grader passes 1 of 531 recipes (52 unlikely, 478 refuse), while its physics filter passes 527 of 531; no record links a verdict to a real deposition outcome [OWN-EXPERIMENT on company files + OPINION]. One agent submitted the same material 58 times as larger and larger supercells to beat a novelty check [SOURCE]. On Periodic Labs' benchmark, the judge agrees with an expert 74.6% of the time, against 77.2% for expert vs expert [SOURCE]. Judge verdicts are ratings, not ground truth.

**38. Record Wall vocabulary: information layers, present / partial / absent, provenance**
- Plain: R01 checks each example record on 8 layers: composition, processing, structure, method, signal, uncertainty, provenance (where it came from, under what licence), supported tasks. Each cell is labelled present, partial, absent or not applicable.
- ML analogy: a datasheet-for-datasets audit, done per record.
- Why here: it is the frame of R01, R02 and R08. The labels are soft. Of 72 cells, 50 are "partial" (12 present, 8 absent, 2 n/a), and neither "present" nor "partial" is defined anywhere [OWN-EXPERIMENT audit]. "Partial" was assistant judgment, not a benchmark. One headline, "uncertainty absent in 6 of 9 cases", becomes 4 of 9 if the legend's own rule is applied consistently.

### F. The two companies that were studied

**39. Periodic Labs**
- Plain: a startup that trains its own large model and runs its own lab (about 100 experiments per day, company claim). The user: "i know their long term goal is ai scientist that can make superconductor materials".
- ML analogy: reinforcement learning where the lab is the environment. They describe a "ladder of rewards"; XRD phase identification is the first rung.
- Why here: on their FrontierXRD benchmark (n=134) their model scores 55.3% vs 2.7% for its base model. That figure is best-of-7 with a learned selector; a single attempt is about 36% [SOURCE + OWN-EXPERIMENT arithmetic]. Nothing is released. The claim "thousands of patterns / PhD annotators" is unverified. The user caught an overclaim about this model in the assistant's first write-up.

**40. Discovered Materials (DM)**
- Plain: a two-person YC startup ($9M seed, company claim) using LLM agents to propose thin films that spread heat on chips. Films must be made at 400 °C or below.
- ML analogy: a generate-then-filter pipeline where the final filter is an LLM judge.
- Why here: it is the case study of R05/R06. Every quoted number needs its denominator: 531 graded, 526 exported, "500+" on the web page [OWN-EXPERIMENT]. Conclusion so far: "no compelling contribution established" until DM answers one question: have grader verdicts ever been compared with real deposition outcomes? [OPINION]

---

## Part 2. The user model

### Background
- An ML/data person. New to materials science, and says so often: "I'm new to materials science and want to understand its data landscape deeply enough to identify meaningful gaps in data reusability." "i'm new to this and need to better educate myself". "I'm very unfamiliar with this domain". "what's rruff?"
- Thinks in ML terms without prompting: learning curves, scaling, "comparing oranges and apples?", looped transformers, DFT pretraining as "obvious because experiment is scarce".
- Follows autonomous-lab companies closely, above all Periodic Labs.
- Has local projects named in the notes: dara-conform (calibrated confidence and abstention on Dara's XRD phase identification, pre-registered 2026-07-09), direction-probes/P1-dara-miscalibration, materials-event-modeling/lab-sim, alabos, "explore materials". These lean toward XRD and lab workflow [OPINION, this file].
- Works "alone or with a small team". Assets they named: AI tooling, lab relationships, "Taiwanese/Mandarin-speaking connections".
- Runs many parallel sessions and loses track: "i can't find the chat related to matterlab work".
- The sessions assumed "we" = a small software team working with public data, with no lab of its own. The user never confirmed or denied this.

### Goals, in their words
- "the imagenet moment for materials science has not happened yet, and i'm working towards making that happen - even thought it's much more complicated and challenging that the imagenet data tiself"
- "find gaps or opportunities of what kind of data is needed for this type of workflow and we can think of helping to curate and open-source it to help the community"
- "the practical work of collecting, curating, recovering, connecting, and making experimental evidence usable for AI learning"
- "take responsibility for difficult data work that model researchers may recognize but lack the time, access, or incentive to undertake"
- "identify a specific, consequential bottleneck that a small external team could remove"
- Also asked "whether there is a credible product opportunity for us". The outcome may be software, "a useful dataset, collection process, or data partnership".
- Anchors they cite: Anubhav Jain (experimental datasets are "scattered or unavailable, lacking metadata, and lacking clearly defined problems and evaluation metrics"); Ghiringhelli et al. 2023 on shared metadata.
- The original picture in their head: "standing in a room where a large wall displays rich materials records together". And: "I do not want to memorize a separate vocabulary for every material."

### Complaints about how results were delivered
- Too long: "well the report still is a lot, just want to make sure if the reports contain actionable items - especially what and how we can build to bridge to gap/helping the workflow".
- Too much jargon, no big picture, no next step: "i read the report, but still don't get what's going on, maybe there's too many jargons ... i'm still confused and not clear what the next actionable meaningful (and ideally thoughtfully smart) contribution we can do here? like what problems, gaps we identify and what solutions (maybe some of them are low-hanging fruit)". They asked this three times, in three sessions, within about 30 minutes. The need is unmet.
- "after reading these essays, even though i learned things, i'm still confused".
- Had to ask for the plan again: "can you recap what's the plan here to do data curation?"
- Asked for the same kind of summary in at least four sessions: "can you yield me a readable report of the convo so far - the takeaways, the action-taking direcitons/goals, conclusions, etc."
- Runs took too long: "please wrap up in 10 mins" (after waits of about 1.5 h and 3 h).
- Beginner questions left on published pages: "what do 'hard patterns' mean?", "what influences the big peaks and small peaks?", "why?".
- The sessions measured the complaint. Of 188 action items across the reports, all say what, 120 say how, 59 name an owner, 11 give a first step, 8 give a done test, and 3 have all four. Only 8 of 188 are software builds [OWN-EXPERIMENT]. The assistant admitted one debrief's actions are "mostly for data owners and funders".

### Stated preferences
Format:
- "Keep explanations concise and let the tables and diagrams carry most of the information."
- "keep your explanation brief and to the point plz."
- "Avoid toy records, fabricated values, unsupported completeness claims, and long introductory explanations."
- "Favor a reliable deliverable over unnecessary interface complexity."
- From the memory notes: gloss domain jargon once; do not over-explain ML; give the direct answer first, then numbers and caveats; lead with short build lists and verdicts.

Tone and rigor:
- "i rather you not make up anything just to fill in some text and want you instead to objectively tell me the truth"
- "wait are you sure this is true?" / "stand at a 'critique' perspective" / "please double check for me"
- "after carefully researching and critiquing, tell me what you think" / "use your logic and deduction"
- "Separate documented facts, company claims, deductions, and proposals". "Use primary sources and cite them".
- "Keep the language concrete: files, measurements, decisions, operator actions, and deliverables."
- Wants to know how a judgment was made: "is it bc there's some reference/benchmark or you rely on some reasoning?"
- "Avoid unsupported percentages or speedup estimates".

Focus:
- Experimental data, not simulated: "i just noticed that we're also bulk downloading dft data? i thought our focus is more around curating experimental data, even though it's not perfect yet".
- Learn by doing: "you can even start experimenting some data curation just to validate/invalidate your hypotheses, which would help iterate/improve our understanding".
- Problem first: "Prioritize discovering the real data problem over pitching a product". "Let the diagnosed problem determine the intervention".
- Not another generic fix: "Do not automatically recommend a connector, dashboard, lab notebook, universal schema, ontology, or new laboratory". "Don't restart with another generic metadata or ontology proposal."
- No easy assumptions: "Do not assume raw or more detailed data are automatically better". "Do not assume richer data improves decisions".
- Honest about limits: "Be willing to conclude that the dominant bottleneck is inaccessible to us".
- "Stay at investigation and design until we select a build direction."

Working style and constraints:
- "Make reasonable scope decisions and proceed without repeatedly asking for confirmation." Replies are terse go signals: "ok go ahead", "yeah go ahead".
- "Verify record identity, important joins, source values, and dataset scope."
- Downloads need an explicit yes. Only "Core datasets, 142 MB (Recommended)" was approved. "i think i already have related existing downloads on my laptop".
- Anything public needs a yes: filing upstream error reports, contacting labs or companies, recruiting raters, republishing a shared page. None has been approved yet. Several approval requests were never answered.
- The user sends any outreach personally.
- "the memory should be limited to only this folder". Nothing under their code folders was modified.
- The assistant must not handle credentials. The user once pasted an API key; the assistant refused it.

### What kind of contribution they seem to want [OPINION, this file]
- Open, community-facing work on experimental data. In practice a bundle: a small tool, plus a cleaned dataset or error list, plus a fair benchmark. Not a paper for its own sake, and not a product pitch. A "credible product opportunity" or a data partnership is welcome if the diagnosis leads there.
- It must be doable by one person or a small team without a lab, at least for the first steps.
- It must be concrete and checkable: a first step, a done test, real files.
- It should be "thoughtfully smart": a lever others have missed, not more metadata advice. Candidates that fit, all found in the corpus: the zT checksum, paper-grouped splits, a second digitisation used as a noise floor, a file-only test for calculated patterns, a fair XRD scoring tool, a known-answer XRD set.
- They want low-hanging fruit named as such, separate from the long projects.
- Open decision the user has not made: the main session recommends the thermoelectric line (error reports -> "spell-checker" -> fair exam -> small benchmark). The XRD session leans to XRD error reports + a usable-files index + a scoring tool, as door-openers to a known-answer set with a partner lab. Nobody has reconciled the two. The user's own local project is on the XRD side.

---

## Part 3. The 10 places where the existing reports are hardest for a newcomer

**1. R01 Materials Record Wall: huge, and its main label is undefined.**
- 5,573 lines as text; 9 cases x 8 layers; 72 gap rows; a 60-term field guide; six material families, each with its own vocabulary.
- The headline grid is 50 of 72 "partial" with no written definition and no roll-up rule. The user had to ask how "partial" was decided. The answer: assistant judgment.
- One record per case, so it cannot say how common any problem is. It defines no task, split or metric.
- Avoid by: one running example, defined labels, and a "so what" per row.

**2. R02 Record Wall Debrief: the actions are for someone else.**
- 72 gap rows mapped to third-party owners (database maintainers, funders), mostly without milestones.
- Tag jargon: gap types obs/def/join/unc/var/model; fix types; "co-occurrence lift".
- User verdict: "still is a lot".
- Avoid by: listing only actions the user can take, each with a first step and a done test.

**3. R03 Toward a Materials ImageNet: three research rounds folded into one page.**
- Its own code families (Track A with A1–A7, Track B) and its own claim tags (Fact / Inference / Forecast / Synthesis).
- A1–A7 mostly describe datasets that should exist, not things to build now. Track A vs Track B is left undecided.
- Sample-size arithmetic (270 / 770 / 1,570 items) and Periodic Labs statistics arrive with no primer.
- Avoid by: stating the ImageNet analogy in two lines (trusted labels + a fair exam), then the gaps.

**4. R04 Materials ImageNet Debrief: a correction log presented as a summary.**
- A second tag scheme (Stated / Arithmetic / Inference / Mixed), z-scores, a table of 14 corrected sentences, about 20 unknowns about Periodic Labs, and about 30 action rows that mostly say what, not how. Many are "watch" items.
- It still carries one uncorrected statement (the composites example names the wrong confound).
- Avoid by: showing corrected facts only. Keep the correction history in an appendix.

**5. R07 Thermoelectric Benchmark Spec: written like a standards document.**
- No primer for S, ρ, κ, zT or power factor.
- Proficiency-testing statistics (z′, σpt, u(xpt), ISO 13528), a 28-field schema, rules R1–R12, 17 missing rules, 22 major + 15 minor open review issues.
- Its newcomer-friendly results (the zT checksum; 25.5% -> 42.2%; reading error about 0.5%) sit in section 3 behind the framework.
- The full plan needs at least 3 measuring labs, and no pilot lab, cost or organiser is named. The buildable parts (validator, split generator) are not separated from the parts that need labs.
- Avoid by: leading with the three results, then splitting "can do now on disk" from "needs partner labs".

**6. R10 XRD Curation Experiments: verdict codes without XRD basics.**
- H1–H7 with "held / failed / inconclusive" wording. "Hard pattern" is a term invented by the plan. Peak basics are assumed. The user's comments on the page were "what do 'hard patterns' mean?" and "what influences the big peaks and small peaks?"
- It has its own build list B1–B7, which collides with the project-wide list B1–B12.
- The handedness finding needs three domain ideas at once (space group, enantiomorph, powder vs single crystal), and its reading flipped mid-report.
- Avoid by: a five-line XRD primer first, then each finding as "what we checked, what we found, so what".

**7. R05 and R06 Discovered Materials reports: a third jargon stack, shifting denominators, no verdict.**
- Thin-film and chip terms: BEOL, PVD/CVD, TDTR, 3-omega, thermal boundary resistance, lonsdaleite.
- "kappa" means thermal conductivity in one paragraph and Cohen's kappa (rater agreement) in another.
- Denominators shift: 531 graded / 526 exported / "500+" on the page / an earlier 756.
- A third tag scheme (Documented / Company claim / Deduction / Proposal / Illustrative), a 10-stage trace, and stop conditions stated in AUROC.
- It ends with no direction chosen. R06 lists 8 corrections that the published R05 still owes. Neither page was visually checked before publishing.
- Avoid by: one paragraph on what the company does, the one key finding (a judge never checked against outcomes), and the one question to ask them.

**8. R08 DFT vs Experiment Debrief: three questions, heavy physics, and it concerns the parked side.**
- Functional names (PBE, r2SCAN, PBE0), the MP2020 correction, hull ordering, scaling-law fits (C + D·N^−α), "exchange rates" between DFT and experimental points, detection limits.
- 12 proofreading corrections and two decisions still "awaiting your yes".
- The takeaways are simple: label the source of every value; measuring the curve is fine, extrapolating it is not. The route to them is not.
- Avoid by: stating the two takeaways and the quartz example. Mark the rest "computed side, parked".

**9. R09 Recursion in Materials AI: a literature dump beside the main thread.**
- 110 papers in six threads and 56 long dataset cards. No experiments by the sessions.
- Two jargon stacks at once: ML trend terms (TRM, HRM, DEQ, S.U.N., GRPO) and materials terms.
- It never connects to experimental data, XRD or thermoelectrics. By a reader's count, only about 10 of the 56 datasets carry experimental labels, and none is XRD or TE [OPINION]. In the session behind it, seven directions were listed and the user never picked one.
- Avoid by: one box, "side topic: what it found, why it is not on the main path".

**10. Across all reports: colliding codes, four tag schemes, stale numbers, two competing recommendations.**
- Code collisions. "B1/B2/B3" means Periodic Labs bottlenecks in one session, DM bottlenecks in R05/R06, build-list items B1–B12 in the notes, and R10's revised builds B1–B7. One note even calls the XRD scoring library "B3", while B3 on the ranked list is a different tool. Other families: H1–H7; E1–E6 vs E1–E7; P1–P7 (R02 patterns) vs P1–P4 (the main session's four problems); A1–A7 (R03) vs A–E (XRD ideas); rules R1–R12 vs curation rounds R1–R4; gap ids like `case#n`. The memory notes flag this clash themselves.
- Four tagging schemes for the same idea ("how sure are we"), one per report family.
- Stale numbers still live on published pages. Examples: A-Lab 41/58 (now 36/57); opXRD multi-phase 41.4% (now 18.1%); "28% of PG samples carry an error" (strict rate 9.0%); Jha "0.06 vs 0.13–0.15" (now 0.0715 vs 0.1325 eV/atom); Starrydata Experiment count 32,497 (now 32,435); "83 of 279" (now 80/278); "uncertainty absent in 6 of 9" (4 of 9 under a consistent rule); "no certified κ reference" (BCR-724 exists).
- The two live sessions recommend different first lines (thermoelectric vs XRD), and no document reconciles them.
- Avoid by: no private codes in the overview (use names); one tag scheme; corrected numbers only, each with its denominator; one reconciled recommendation, or an explicit either/or with the deciding question.

### Short rules for the new overview [OPINION, this file], drawn from the ten points above
1. Start with the two-line picture: ImageNet = trusted labels + a fair exam. Open experimental materials data has neither, for four fixable reasons: uncaught record errors; exams that are too easy; records that do not say how the measurement was made; tasks with no answer key.
2. Gloss each term once, with an ML analogy, at first use. Use no more than the 12 essential terms on page one.
3. One number per claim, with its denominator and a status tag.
4. Every action gets: who does it (the user, or a partner), first step, done test, what approval it needs, and whether the data is already on disk.
5. Separate "days" items (send error lists already in hand; all need the user's yes) from "weeks" items (TE checker, fair-split generator, XRD scoring tool) from "needs a lab" items (known-answer XRD set, blind TE round).
6. Say plainly what is parked (computed/DFT side, recursion survey, DM until they reply) and why.
