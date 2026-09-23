# Build + idea inventory

Everything that was PROPOSED anywhere in the corpus: tools, datasets, benchmarks, experiments, reports, outreach, research ideas.
Compiled 2026-09-18 from all 32 digest files (12 chat-slice groups, 10 reports, memory notes + build list, late updates).
Nothing here is new. Every number is copied from the digests, with its denominator.

---

## 0. How to read this file

**Status words**
- idea = mentioned, no plan yet.
- specified = a written plan exists (steps, or pass/fail rules).
- started = some code, draft or data work exists.
- done = finished.
- parked = paused by a decision (can be resumed).
- dropped / refuted = tried or checked, and it failed. Do not revive without new evidence.

**Claim tags (kept from the corpus)**
- [OWN-EXPERIMENT] = measured by the sessions on real files.
- [SOURCE] = a paper, website or dataset README says so. Not re-measured.
- [OPINION] = reasoning or judgment. Not measured.
- [REFUTED] = was claimed at some point, then shown wrong.

**"On disk?"** means: does the corpus SAY the data already sits on the user's machine. I did not open any folder outside the scratchpad, so none of these locations were checked.

**Numbering clash (important).** Four different lists in the corpus use "B1, B2, B3...". They are not the same things.

| Label in the corpus | What it means there | Label used in this file |
|---|---|---|
| B1-B12 in the ranked build list (memory notes) | the main ranked builds | **B1-B12** (unchanged) |
| "revised builds B1-B7" in the XRD Curation Experiments report | XRD-side builds | **X1-X7** |
| B1-B8 in the TE Benchmark Spec digest | parts of the TE benchmark | **T-items** |
| B1-B3 in the Discovered Materials reports; B2/B3 in the Periodic session | "bottleneck 1, 2, 3" (problems, not builds) | **DM-bottleneck / Periodic-bottleneck** |

Experiment names also repeat with different meanings: "E1-E6", "E1-E7", "H1-H7", "Round 5 E1-E5". Each is tied to its session below.

**Mini glossary (each term once)**
- Thermoelectric (TE) material: turns a temperature difference into voltage.
- Seebeck coefficient S: volts per degree. Resistivity rho: how much the material resists current. Thermal conductivity kappa: how well it carries heat. Power factor (PF) = S^2/rho. zT = S^2*T/(rho*kappa): the overall quality score. Because zT is computed from the other curves, you can recompute it and catch wrong records. It works like a checksum.
- Starrydata / teMatDb / ESTM: three open TE databases. Their numbers were read off plots in published papers ("digitised").
- DOI: the unique id of a paper. Paper-grouped split: train/test split where a whole paper is on one side only (GroupKFold by DOI).
- Powder XRD (X-ray diffraction): a 1-D fingerprint signal of a powder. Phase: one distinct crystalline compound in the sample. Phase identification: say which phases are in the pattern (multi-label classification, plus weight fractions).
- Rietveld refinement / "fit": the curve-fitting step that turns a pattern into phases and fractions. Its residual is a loss value, not proof of correctness.
- Weighed mixture: powders mixed at known weights. The only true "known-answer" label for phase ID.
- Multi-rater set: several experts label the same item and every label is kept (inter-annotator agreement).
- Calculated vs measured profile: a pattern simulated from a crystal structure vs one recorded on an instrument (synthetic vs real image).
- Enantiomorph / "hands": mirror-image crystal structures (for quartz, space groups #152 and #154). Powder XRD cannot tell them apart.
- CIF: crystal-structure file. COD (open, CC0) and Materials Project, MP (open, CC BY) vs ICSD / ICDD / CSD (paywalled): structure databases. Their ids are the join keys for phase labels.
- DFT: quantum simulation of an ideal crystal at 0 K. Think "synthetic labels from a biased simulator". MP, OQMD, JARVIS, GNoME are big DFT databases. Matbench: a standard ML benchmark suite, mostly DFT labels.
- MLIP: machine-learned interatomic potential. A fast learned stand-in for DFT.
- Round robin: many labs measure the same sample. Gives the between-lab spread (the label-noise floor).
- z' score (ISO 13528): model error divided by expected between-lab spread. Tells you when two models are indistinguishable.
- SRM / BCR-724: certified reference samples with known values (NIST SRM 3451/3452 for Seebeck; BCR-724 for thermal conductivity; SRM 2686a for a multi-phase XRD mixture).
- Pre-registration: fix the hypothesis and the pass/fail bar before looking. Matched null: compare every flag rate to the rate on shuffled or known-clean data.
- Errata / upstream issue: an error report sent to a database owner.

---

## 1. The short version

1. Almost everything in the corpus is still an idea or a spec. The actionability audit measured this: of 188 action items in the reports, 3 had all four of how / owner / first step / done-criterion [OWN-EXPERIMENT].
2. Four builds are small, extend existing tools, need no approval, and have their data on disk: **B1** TE record checker, **B2** fair-split generator, **B3** table linter, **B8** release-file lint.
3. One contribution is ready today but blocked on a yes: **send the error lists already found** to database owners.
4. Two sessions gave different first lines on the same evening. The main session says "commit to the TE line". The XRD session leans to "error reports + usable-files index now, scoring tool as the bridge, hard known-answer set with a lab later". Nobody has reconciled them.
5. Round 5 experiments were started. No results are in. Two of them decide B1 and B11.
6. A long list of things was tried and refuted (section C). The main one: never fix units automatically.

---

## 2. The ranked builds B1-B12 (from the latest build list)

The ranked order itself is reproduced exactly in section A.

### B1. te-validate - TE record checker ("spell-checker" for TE data)
- **What.** A tool that reads a TE record and checks that its numbers fit together. It recomputes zT from S, rho and kappa. It flags power-of-ten (unit) mistakes, empty curves, out-of-range values, and spreadsheet cells that are formulas posing as measurements. It outputs a validation report and a review queue. It never edits data.
- **Gap.** Records contain mistakes that nothing catches. No existing tool checks power-factor errors (teMatDb stores no PF curve).
- **Status.** specified. QC scripts exist (analyze_starrydata.py, plausibility_starrydata.py, identity_starrydata.py, analyze_tematdb.py). The ESTM formula-cell detector is unwritten (1-2 days). The TE spec report calls it "effectively prototyped but not packaged as a tool".
- **Evidence it is worth doing.** [OWN-EXPERIMENT]
  - 646 of 13,702 checked Starrydata samples have zT off by more than 50%. 266 of those are off by a clean power of ten. About 1 in 25.
  - 2,622 curves have no finite points (787 samples entirely empty). 240 Seebeck curves and 770 temperature axes are out of range.
  - ESTM: 3,853 power-factor cells and 3,310 zT cells are unflagged Excel formulas.
  - When two databases digitised the same figure, more than 10% disagreement showed up in 15 of 361 comparisons (4.2%). All tail cases were record errors, not reading scatter. 8 were Starrydata errors (Celsius stored as kelvin twice, sign flip, power of ten, conductivity filed as Seebeck, curve swap, compressed temperature axis).
  - teMatDb's own filter of the same kind kept 10,840 of 15,532 Starrydata samples [SOURCE, arXiv 2505.19150]. Reuse it.
  - A review queue already exists: 633 specimens across 230 papers (2 rows mislabelled).
- **Inputs / on disk?** Starrydata (55,422 samples), teMatDb, ESTM. Corpus says on disk, but in the 09-14 session scratchpad, which is a temporary folder.
- **Approval.** None to build. Sending errors upstream needs a yes (see O1).
- **Effort / first step / done.** Build list: 1-3 months. Main session's effort table: 1-2 weeks for the spell-checker form. First step: one command that reproduces the TE spec section 3a/3d counts with an identical hash. Done-criterion (after Round 4): measure the real-data wrong-fix rate with a by-paper bound. Offer a fix only when a PF curve exists and both identities are off by the same power of ten. Never fix different-power specimens. All fixes are review-queue suggestions.
- **Risks / known failures.**
  - [REFUTED] "Most unit errors are fixable": only 85 of 266 fixed, at least 6 of those fixes likely wrong.
  - [REFUTED] "Gated rule gives at most 1% false fixes": 11.2% under an assumed 25% two-curve share. Round 4 measured the share at 13.7% (18 of 131 specimens, 36 papers, by-paper CI about 3-27%) and the false-fix rate at 7.2% (CI 0-19%; 4.4% with a PF curve, 11.9% without). The rule fixed 0 of 12 proven two-curve errors.
  - A zT-only auto-fix wrongly fixes about 19% of two-error records.
  - Errors are paper-wide (59 of 60 paper groups get one call). Count papers, not rows.
  - The PF curve is the single suspect in 133 of 245 cases (54.3%), so it cannot act as referee.
  - Hand check 22 of 24, but the real-choice cases were 11 of 13, below the bar.
  - Round 5 experiment 2 (hide the PF curve on 273 specimens) decides the fix rule.

### B2. splitgen - fair-exam (split) generator
- **What.** A tool that makes train/test splits where a whole paper (or another group unit) stays on one side. It writes a leak report and a manifest. It includes a cross-database index of shared papers, after cleaning DOI strings.
- **Gap.** Exams are too easy. The same paper sits on both sides of a random split, so reported accuracy is inflated.
- **Status.** started. The DOI normaliser is saved (regression test: 193 / 75 / 7 shared DOIs).
- **Evidence.** [OWN-EXPERIMENT]
  - Random split: the test paper is already in training 93.5% of the time. Seebeck median error goes from 25.5% to 42.2% when papers are held out (12,222 samples, 3,015 papers). Grouping by chemical system gives 46.6%.
  - Raw-string DOI matching finds 183 / 26 / 4 shared DOIs. After normalising: 193 / 75 / 7 (teMatDb-Starrydata / ESTM-Starrydata / all three).
  - The right group unit differs by dataset. In the Precursor Genome synthesis ledger (PG, 1,035 samples), holding out a precursor drops macro-F1 from 0.53 to 0.42 (rerun 0.49 to 0.39). Grouping by chemical system does almost nothing.
  - Matbench steels: 66 of 312 groups have a near-duplicate composition (within 0.1 wt%) in another group.
- **Inputs / on disk?** Same TE files as B1, plus PG ledger and steels. Corpus says on disk.
- **Approval.** None.
- **Effort / first step / done.** 1-2 weeks (main session: about 1 week). Next step: reproduce the TE spec section 3e split table. Build on scikit-learn GroupKFold and MatFold (an existing materials split tool). Round-4 done-criteria: a matched-null false-positive bound, recall on real duplicate pairs, and a per-dataset group unit.
- **Risks.** Composition joins are fragile: the ESTM-to-Starrydata unique join share is 74.9% at tolerance 0.001, 59.5% at 0.005, 34.0% at 0.02. Join on figure labels instead (label match is the closest curve in its paper 91-94% of the time). Store the tolerance with every join.

### B3. recordlint - linter for qualifiers, uncertainty and blanks in tables
- **What.** A command-line checker for compiled data tables. It flags cells where ">", "<", "±", ranges or blanks were flattened into a plain number. It flags blanks. It never fills them.
- **Gap.** Compiled tables destroy qualifiers, uncertainty and the meaning of "blank". Neither Frictionless Table Schema nor Citrine GEMD (two existing table/record standards) can represent an inequality or a censored value [SOURCE].
- **Status.** specified.
- **Evidence.** [OWN-EXPERIMENT]
  - MPEA (a multi-principal-element alloy table): 382 damaged cells. ">300" became 300 and "150-200" became 175. "±" deleted from 264 cells; 49 ">", 50 "<", 19 ranges.
  - The parser resolves 5,707 of 5,708 cells. But the meaning of a blank is recoverable for only 25.6% of blanks (12.2% without a post-hoc rule).
  - A polymer table has std "0.0" on 7,088 of 7,367 rows. It means n=1, not zero spread.
- **Inputs / on disk?** MPEA, polymer and composites tables from the Record Wall work. Corpus implies local copies (atlas raw files sit in a temporary workspace).
- **Approval.** None.
- **Effort / first step / done.** 1-2 weeks. First step: a CLI plus a regression test on the MPEA numbers. Round-4 design rules: three states (ok / flagged / not evaluable), error flags separate from provenance flags, the tolerance written into the rule id, the strict rate as the headline.
- **Risks.** A linter flags ambiguity; it cannot recover meaning. The B3 MPEA milestone was untouched as of Round 4.

### B4. Matbench provenance companion - PARKED (steels part stays)
- **What.** A side table ("sidecar") that says, for each Matbench formation-energy row, which Materials Project id and version it came from. Plus a member table for Matbench steels showing the raw records behind each averaged target.
- **Gap.** Benchmark rows carry no source id or version, so labels cannot be traced.
- **Status.** parked (MP side) after the user's "experimental data first" correction. The steels member table stays.
- **Evidence.** [OWN-EXPERIMENT] mp_e_form keeps no MP id or version. Ids recoverable for 279-295 of 300 sampled rows. 80 of 278 labels are within 0.01 eV/atom of the current value ("computed-value drift, not error"). Sidecar: 132,752 rows = 110,532 single match / 19,835 multiple / 2,385 none; 1,818 single rows share 820 ids. Steels: 842 records averaged into 312 targets (21 duplicates); 350 Charpy and 165 KIC values dropped; random-forest error 91.1 MPa on averages vs 116.9 on records (gap CI 11.5-43.8; ridge shows none).
- **Inputs / on disk?** A roughly 0.9 GB MP cache is on disk (there is an open offer to delete it).
- **Approval.** Upstream Matbench issue #124 needs a yes. No more bulk MP pulls (user decision).
- **Effort.** Not restated after parking. Dropped follow-ups: structure-verified identity, the 2,385 unserved rows, Matbench duplicate leakage.
- **Risks.** MP must never be framed as experimental ground truth. "Conditions help within steel groups" is [REFUTED] once leakage is controlled.

### B5. Scoring harness (z'/zeta scores, hashed answer key)
- **What.** Scoring code that reports model error in units of between-lab noise (z'), optionally using the entrant's own stated uncertainty (zeta). The answer key is frozen with a hash.
- **Gap.** No fixed task or metric in TE. Scores today do not say which model differences are real.
- **Status.** specified, not built.
- **Evidence.** [SOURCE] Between-lab spread is known: S 6%, rho 8%, kappa 11%, zT 19% (Alleno 2015). With three labs, z' (not z) is required by the proficiency-testing standard. [OWN-EXPERIMENT] Digitising noise is about 0.5-1%; model error is 42.2%. Round-4 notes: the noise floor is a lower bound, score zT separately, use a median metric.
- **Inputs.** Reuse metRology (R package for ISO 13528) and Codabench (open challenge platform). No new data.
- **Approval.** None. **Effort.** 1-2 weeks, after B1. MIT licence planned.
- **Risks.** The 0.5-1.7% curation agreement is a lower bound on label noise, not a scoring tolerance.

### B6. Baselines
- **What.** Reference models every entrant must beat: reproduce the 25.5% / 42.2% numbers, then run on the cleaned dev set (2,839 specimens, 870 DOIs; S and rho at 300-500 K). Run MODNet (an existing materials model) and a Dummy predictor.
- **Gap.** The spec's only baseline is a composition-only 5-nearest-neighbour model.
- **Status.** specified. The baseline experiment itself was done once (baseline_300K.py).
- **Evidence.** [OWN-EXPERIMENT] A plain same-composition median lookup (22.9%) beats kNN (29.4%). Even an oracle median chosen with the answers known misses by 15.0%. So composition-only inputs have a hard ceiling.
- **Inputs / on disk?** Starrydata snapshot already used. **Approval.** None. **Effort.** 1-2 weeks.
- **Risks.** Use the 2,839 / 870 recount, not the earlier 3,361 / 951.

### B7. Specimen layer (te-layer) - BLOCKED
- **What.** A schema that describes one physical TE specimen (how it was made and measured), not just its formula. 9 field groups, 28 fields.
- **Gap.** "One composition string carries many labels." Same formula across papers differs by a median 32.7% in S; the same specimen across labs differs by about 6%.
- **Status.** blocked on descriptor quality. Draft schema exists (TE spec). fillrate.py and the 28-field matrix are done.
- **Evidence.** [OWN-EXPERIMENT] Descriptor coverage reaches 43% against a 50% bar (audit precision 0.875 vs 0.90). 7 of 28 fields exist in no source (parent batch id, measured composition, step conditions as fields, density used for kappa, measured-vs-calculated flag, per-property uncertainty, measuring lab). Measurement direction is recorded on 12 of 55,422 samples.
- **Inputs / on disk?** Existing TE files only.
- **Approval.** Field requests to data owners are outreach: needs a yes.
- **Effort / deliverable.** 1-3 months. Deliver a schema plus field requests. Use the figure-label join as primary and store the tolerance.
- **Risks.** [REFUTED] "Descriptor clean-up recovers context." The shared specimen core it depends on has 37 weak links, 2 unsupported requirements, 27 other issues, all unresolved.

### B8. Release-file lint + owner schema packets
- **What.** (a) A file-only check that detects a calculated or cleaned pattern labelled "RAW", without trusting the header. (b) Short "packets" for database owners proposing missing header fields. First one: a 13-field header proposal for RRUFF (a mineral spectra/XRD archive).
- **Gap.** Records do not say how the measurement was made, and "RAW" is often not raw.
- **Status.** started. The 13-field RRUFF header proposal is drafted. It must round-trip on 30 saved spectra (formats: JCAMP-DX, Croissant).
- **Evidence.** [OWN-EXPERIMENT] 1,702 of 3,019 (56.4%) RRUFF "RAW" powder files declare a calculated profile in their own header. A noise-signature check agrees with the header on 2,928 of 3,006 files (97.4%, AUC 0.998). Wavelength is stated in 71 of 3,019 files (2.4%); step size and scan time in 0. opXRD (a pooled open XRD set) already absorbed 499 RRUFF copies, 414 of them calculated but marked "not simulated". GNoME's Density column is documented in one unit but matches another.
- **Inputs / on disk?** RRUFF (3,019 RAW / 1,484 processed) and the opXRD slice (2,680 patterns). Corpus says on disk (in the user's dara-conform data folder).
- **Approval.** Building: none. Sending packets to owners: needs a yes.
- **Effort.** About 2 weeks for packets.
- **Risks.** Round 5 experiment 1 runs this lint blind on the Dara patterns as a test.

### B9. Handedness crosswalk - PARKED
- **What.** A table linking mirror-image entries of the same crystal across databases, so joins do not silently drop or double-count them.
- **Status.** parked. 70-row prototype, 60 rows dedupe-eligible.
- **Evidence.** [OWN-EXPERIMENT] 74% of "both-hand" formula instances are mirror copies, not different polymorphs. 49 mirror-copy pairs sit as separate Matbench rows. A join on space group drops quartz: MP lists #152, experiment lists #154.
- **Why parked.** For powder XRD, merging mirror copies is correct (H6 verdict). The rest is MP-side, which is parked.
- **Risks.** [REFUTED] The "10x RMSE" mirror-copy threshold misses 8 of 61 copies (ratio as low as 2.58).

### B10. emmet patch + HTEM errata - emmet half PARKED
- **What.** A fix to MP's data-building code (emmet) for a misspelled field, `energy_uncertainy_per_atom`, empty on all 342,144 thermo documents. Plus an errata CSV for HTEM (a thin-film database) where the absorption field equals transmittance at 44 of 44 positions.
- **Status.** emmet half parked. HTEM errata CSV stays.
- **Approval.** Any upstream patch or issue needs a yes.
- **Risks.** HTEM repos were archived in June 2026 and cannot take fixes [SOURCE].

### B11. XRD known-answer + multi-rater set
- **What.** A small test set of powder XRD patterns where the right answer is known (weighed mixtures) and where several experts label each hard pattern, with every label kept.
- **Gap.** For phase ID there is no answer key. Human and software fits of the same scan differ in 316 of 343 cases, and all 1,216 human verifications carry one editor id, so this is machine-vs-human, not expert-vs-expert.
- **Status.** specified. A desk go/no-go stage comes first. Decide on the Dara supplement plus A-Lab GPSS. Drop the HKUST-B folder.
- **Evidence.** [OWN-EXPERIMENT]
  - Usable open pool (measured, raw-like, labelled): 1,683 of 7,183 files (1,600 deduped). Only 353 state a wavelength; 352 come from one institution. "These archives cannot seed a known-answer XRD benchmark."
  - Hard patterns (4 or more phases at 1 wt% or more): 167 (PG 157 of 1,035; GPSS 10 of 352). The plan's bar was 270. So a pilot only.
  - 20 weighed mixtures cannot rank methods: Dara 38 of 40 vs Jade 35 of 40 (paired difference 7.5 points, interval 0.0-15.0). Errors sit in 2-minute scans. 8-minute scans are at ceiling. "Needs harder items, not more items."
- **Inputs / on disk?** Dara supplement, GPSS (352), PG ledger: corpus says on disk. PG raw scans (23 MB) and refinement files (291 MB): NOT on disk.
- **Approval.** Downloads need a yes. Recruiting raters or a lab needs a yes.
- **Effort.** About 10^3 expert-hours. Partner needed. 3-12 months. Main session: "longer; probably needs lab partners; Round 5 decides".
- **Risks.** PG / GPSS / Dara answers are public, so they cannot be a hidden test split. Existing labels cannot stand in for independent raters. See X4 and X6 for the split into pilot and redesigned mixture set.

### B12. TE label-production kit
- **What.** A protocol kit for labs that would measure new, unpublished TE specimens for a blind test. Round 4 added a double-curation step and four declared fields.
- **Gap.** A real test set needs new replicated measurements; literature labels are public and under-described.
- **Status.** idea/specified. Needs 3 or more pilot labs. No pilot lab, cost estimate or funding route exists.
- **Approval.** Contacting labs needs a yes. **Effort.** Not stated beyond "needs partners".

### Dropped from the ranked list
- **SciGlass export patch** - dropped. (No DOI on any of 45,293 SciGlass references [SOURCE]; the earlier SciGlass uncertainty-recovery parser idea was also dropped.)

---

## 3. Thermoelectric (TE) line - items beyond B1-B12

Short cards. Fields: What / Gap / Status / Evidence / Inputs (on disk?) / Approval / Effort, first step, done / Risks. "n.s." = not stated in the corpus.

### T1. TE Benchmark Spec (report, draft 0.2, published, artifact ...5RN8Fu5o9AFQgQw64x2mp6)
- What: a written plan for the first blind TE benchmark. Models predict S(T) and rho(T) for specimens whose labels are newly measured and hidden.
- Gap: no blind TE test with new measurements was found; Matbench has no TE task [SOURCE, negative search: "none was found, not proven absent"].
- Status: done as a draft. Self-labelled "not a released standard".
- Evidence: all section-3 tests are [OWN-EXPERIMENT] on real files. A precedent check confirmed 285 claims and corrected 35.
- Open items: 17 missing rules; 22 major + 15 minor review issues unworked; no pilot lab, cost estimate, funding route, timeline or organizer baselines; the specimen layer was not adversarially reviewed; shared specimen core has 37 weak links, 2 unsupported requirements, 27 other issues.
- Approval: none to edit; republishing is the user's call.

### T2. Blind TE benchmark round (rules R1-R12)
- What: a challenge round. Predict S and rho on a temperature grid (300 K, then 50 K steps) from a frozen specimen record. kappa and zT come in phase 2. One ranked submission per group, no leaderboard feedback, anonymous entries not scored.
- Gap: no fixed task, no hidden labels in TE.
- Status: specified (draft 0.2). First step not stated.
- Evidence: [SOURCE] S and rho are fast to measure (under 20 s at room temperature). zT noise is about 3x S noise (19% vs 6%), so start with S and rho. Round robins took 4 months (7 labs) to about 2 years.
- Inputs: NEW measurements. Not on disk. Training pool = Starrydata snapshot 2026-09-14.
- Approval: any lab contact needs a yes.
- Effort: n.s. Blockers: pilot lab, 3 or more measuring labs (or pooled round-robin SD), funding, the 17 missing rules.
- Risks: every Starrydata value is a published figure, so any early release of test labels lands in the training pool. Scoring on 7 or fewer labs without an external reference is "generally not recommended" [SOURCE, EA-4/21].

### T3. Reference-check protocol (rule R8)
- What: each measuring lab reads a certified sample (SRM 3451 or 3452 for Seebeck; BCR-724 in the kappa phase) in the same session.
- Status: specified. Needs labs. Risks: neither SRM certifies resistivity; no SRM 3452 reading above 900 K; BCR-724 values lapse after 10 or more heatings [SOURCE].

### T4. Frozen answer key with independent custodian (rule R9)
- What: SHA-256-frozen, versioned answer key; fixed review period; assessor-approved corrections. Status: specified. Feeds B5.

### T5. "Small, checked, fair TE benchmark" (B1 + B2 + B5 + B6 packaged)
- What: the main session's 1-2 month package: spell-checker plus fair-exam generator, released together as a benchmark on existing data.
- Status: idea (spec drafted). Evidence: models at about 42% error vs about 1% reading noise [OWN-EXPERIMENT].
- Approval: none to build. Risks: test labels are public literature values, so this is a fair DEV benchmark, not a blind test.

### T6. Second curation as a null and as an error detector
- What: use two independent digitisations of the same figure to (a) estimate label noise and (b) find record errors. Anything more than 10% apart is re-read, never averaged.
- Status: done once (Round 4, w1). As a reusable tool: idea. Round 5 experiment 3 extends it to all 55,422 samples.
- Evidence: [OWN-EXPERIMENT] 0 of 96 zT pairs coincide, so the digitisations are independent. Median disagreement: S 0.48%, rho 0.83%, kappa 0.57%, zT 0.91% (361 comparisons, 102 pairs; scope: teMatDb's high-zT papers only).
- Risks: no source paper was opened, so "which database is wrong" rests on stored numbers.

### T7. Oracle / lookup demonstration (research note idea)
- What: publish the finding that a lookup table beats the ML baseline and that even an answers-known median misses by 15.0%.
- Status: idea (the experiment is done; the write-up is not). Evidence: [OWN-EXPERIMENT] see B6.

### T8. Cross-paper replot detector
- What: detect when one paper re-plots another paper's curve (a hidden duplicate).
- Status: curve-only version [REFUTED]: 51 of 272 hits vs nulls of 38-57. A post-hoc composition-gated variant (16 of 272 vs 1 of 272) is exploratory only. A registered version with 590 "Reference" samples is Round 5 candidate 4, deferred.

### T9. "Sibling" auto-rule and systematic-offset rule
- Status: not shipped. The sibling rule fires on 23.6% of agreeing pairs; the offset rule carries no information [OWN-EXPERIMENT].

### T10. Done TE groundwork (keep, do not redo)
- Family choice: 5 property families graded on 8 criteria; TE chosen, alloy mechanical runner-up. done.
- fillrate.py and the 28-field fill matrix. done.
- between_paper_spread v2: same formula, different papers, median S difference 32.7% (21,856 paper pairs); 17.8% have opposite sign. done [OWN-EXPERIMENT].
- Experiment rounds 1-4 (x1-x5, y1-y4, z1-z3, w1-w4). done. Round 3 (z1-z3) was on MP and is parked.

### T11. Track B - the 8-step "new dataset" roadmap (from the ImageNet report and early sessions)
- What: specimen schema; benchmark rules (hidden labels, new split each round, embargo, neutral organizer); provenance on every derived row with unaveraged records also published; deposition policy; blind test set from unpublished measurements; round robins; randomized sampling that records failures; new calculations. TE is the candidate family. A proposed reference composition is named (Co0.97Ni0.03Sb3).
- Status: idea/specified at roadmap level. T1, T2, B7, B12 are its concrete parts.
- Evidence: [OPINION + SOURCE] "evaluation data before a training corpus": open paired synthesis-plus-raw-XRD records number about 10^3; one lab at 100 experiments per day would need about 27 years for a million labels.
- Risks: whether to start with Track A (XRD) or Track B (TE) was never decided in that report.

---

## 4. XRD line

Source reports: "Toward a Materials ImageNet" (Track A, A1-A7; artifact ...TP5hW9Hdh56scE6LQV2NwC) and "XRD Curation Experiments" (H1-H7 and revised builds; artifact ...4NnMSiSzcGE7qHTJj3dMgS). The XRD session's five late ideas (A-E) are mapped in.
Datasets: Precursor Genome (PG) 1,035 samples / 1,351 scans; A-Lab GPSS 352 samples; Dara benchmark 20 reactions / 40 weighed-mixture scans.

### X1. Scoping count and field audit (XRD-report "B1")
- Status: done. Scripts and tables behind the H1-H7 report. 17 of 18 numbers re-derived exactly by a separate agent. Remaining step: pin file hashes for re-runs.
- Inputs: PG, GPSS, Dara, already downloaded (in a session workspace).

### X2. Handling-history schema + failure logs (Track A3; XRD-report "B2"; late idea E)
- What: a small set of record fields for what happened to a sample between synthesis and measurement: timestamped steps (synthesis end, grinding, storage, XRD start), plus atmosphere and humidity per step.
- Gap: handling is recorded nowhere. 0 of PG's 115 field paths cover it; 13 handling words get 0 hits in PG free text; scan headers are empty in 1,417 of 1,417 PG files and 352 of 352 GPSS files [OWN-EXPERIMENT].
- Status: specified, marked "Now" in the XRD report.
- Evidence: [OWN-EXPERIMENT, exploratory] PG samples re-scanned more than 180 days apart changed their fitted phase set in 105 of 136 cases (77%) vs 12 of 25 (48%) at 30 days or less. Without handling history, sample aging and fit drift cannot be told apart. (A chat slice gives a different cut of the same data: 154 of 184 vs 9 of 14. Use the report's numbers.)
- Inputs: no new data. Acceptance test on disk: could a record separate aging from drift in the 184-sample re-scan case?
- Approval: proposing fields to standards bodies is public outreach: needs a yes. Targets named: NeXus (its committee meets 25-27 Sep 2026), pdCIF, NOMAD, OPTIMADE. Follow the Open Reaction Database pattern.
- Effort: n.s. First step: map onto what NeXus already has, then propose only the missing fields.
- Risks: the user's own guardrail: do not default to "another schema/ontology". Justify by the re-scan test case.

### X3. Crosswalk + fair-scoring library for phase ID (Track A6; XRD-report "B3"; late idea C)
- What: (a) a mapping table from paywalled phase ids (ICSD/ICDD) to open ids (COD/MP). (b) a small open library that decides whether a predicted phase list matches the answer.
- Gap: the "equality function" of every XRD benchmark is currently ad hoc, and labels are locked to paywalled ids.
- Status: specified, marked "Now". Called the "cheapest high-leverage build" in the ImageNet report [OPINION].
- Evidence: [OWN-EXPERIMENT]
  - 745 of 755 PG labels carry ICSD ids; 0 carry COD or MP ids. GPSS: 334 of 687 CIFs are ICSD; 311 are a custom id-less spinel.cif.
  - Formula spelling alone (BiVO4 vs VBiO4) flips 3 of 20 verdicts. Composition-only matching credits a wrong Y2O3 polymorph. A phase listed twice is still marked correct in 4 of 4 Dara and 2 of 3 Jade cases.
  - pymatgen StructureMatcher defaults merge alpha and beta quartz (RMS 0.169) though their main peak differs (26.67 vs 26.21 degrees). A site tolerance (stol) of 0.15 or less separates them. Oxidation-state labels make the same Te structure fail to match.
- Rules to implement: normalize formulas; require space group / polymorph; duplicate-entry rule; define how "unknown phase" is scored; flag implausible phases; count both hands as one phase and say so; stol <= 0.15; ignore oxidation-state labels.
- Inputs / on disk?: PG ledger, GPSS, Dara, COD CIFs: corpus says on disk. Scope: 745 PG ICSD ids + 81 GPSS CIF names.
- Approval: none to build. Blocker before RELEASING a crosswalk: ICSD/ICDD redistribution terms are unchecked. GPSS CIFs are ICSD-derived: "don't redistribute".
- Effort: n.s.
- Risks: never use StructureMatcher defaults as the scorer. The custom spinels need structure matching (no id exists).

### X4. Multi-rater pilot on hard patterns (Track A1; XRD-report "B4"; part of B11)
- What: 167 existing hard patterns, each labelled blind by 3 or more diffraction experts under a published rubric. Keep every label.
- Status: specified, marked "Next". Usable only as a dev/calibration split because the answers are public.
- Evidence: [OWN-EXPERIMENT] see B11. At 167 items an agreement rate near 50% has a 95% interval of about +/-7.6 points. [SOURCE] NIST/IMMI dataset mds2-2301 already keeps every rater's labels, so the open gap is per-phase labels on hard patterns.
- Approval: recruiting raters needs a yes. Blocker: 3 or more experts per pattern.
- Risks: write the agreement bootstrap yourself (the krippendorff package has none). H1 failed the 270 bar; optional opXRD download (1.40 GB) might raise the count, but its multiphase label count is unverified.

### X5. Open judge-calibration kit (Track A5; XRD-report "B5")
- What: calibrate an automated or LLM judge of phase-ID answers against the pilot labels plus Dara's 40 weighed-mixture scans. Keep judge labels separate from expert labels.
- Gap: Periodic Labs uses an LLM as both judge and reward; its calibration claim is unsupported in public [OPINION]. Their own numbers: expert-expert agreement 77.2%, judge-expert 74.6%, judge-consensus 84% [SOURCE].
- Status: idea/specified, "Next". Depends on X4.

### X6. Weighed-mixture set, redesigned for difficulty (Track A2; XRD-report "B6"; late idea D; part of B11)
- What: a new known-answer set built to be hard: 4 or more phases, minor phases under 10 wt%, polymorph pairs, 2-minute scans. The XRD session calls this "the actual ImageNet-style seed" [OPINION].
- Status: idea, "Later". Blocker: a lab with calibrated diffractometers.
- Evidence: [OWN-EXPERIMENT] H7 inconclusive (see B11). [SOURCE] existing designs to start from: IUCr CPD round-robin Sample 2 (4 phases), NIST SRM 2686a (5 or more phases), the IUCr seven-phase synthetic bauxite (Scarlett 2002).
- Approval: lab outreach needs a yes. Size it with a paired power calculation from the H7 error rates.
- Risks: [REFUTED] "weighed truth stops at 3 phases" is false in general (true only for Dara).

### X7. Blind XRD challenge (Track A4; XRD-report "B7")
- What: a hidden-answer challenge for phase ID. First check whether to extend XRDBench rather than build a new harness. Use a salted answer hash and Codabench.
- Status: idea, "Later".
- Evidence: sample-size arithmetic [OWN-EXPERIMENT/OPINION]: about 270 items give +/-5 points on an agreement rate; 100-200 items separate only harness-sized gaps; about 770 to 1,570 items are needed to resolve 2-5 point model gaps.
- Risks: hidden items must be NEW. Public PG/GPSS/Dara answers cannot be hidden splits. CC BY data cannot carry evaluation-only terms. The corpus disagrees on whether XRDBench answers are public (see section E).

### X8. "Usable files" index of open XRD scans (late idea B)
- What: publish a clean list saying which open XRD files are measured vs calculated, raw-like, labelled, deduplicated.
- Gap: people train on "experimental" sets that contain simulated patterns and duplicates.
- Status: started: the manifest exists, but in a temporary area "that can vanish". Not yet through the XRD session's adversarial check.
- Evidence: [OWN-EXPERIMENT] 1,683 of 7,183 usable (1,600 deduped). opXRD slice: 501 unlabelled; 124 exact duplicates in 61 groups, 15 with conflicting labels; all 499 HKUST-B patterns copy RRUFF files.
- Inputs / on disk?: RRUFF + opXRD slice on disk. Approval: publishing it is public: needs a yes.
- Risks: the opXRD zip on disk is a sparse 88 MB slice, not the full 1.4 GB release.

### X9. Plausibility lint for fitted phases
- What: flag fitted phases that cannot be real, for example carbides or graphite in a carbon-free oxide sample.
- Status: exploratory result done; tool is an idea (would live inside X3).
- Evidence: [OWN-EXPERIMENT, exploratory] Y4C7 at 31 wt% and graphite at 66 wt% appear in carbon-free systems, both from automated fits. An element-set check alone is not enough: 0 of 3,240 fitted phases use an element outside precursors or air (a shuffled-precursor control flags 1,642).

### X10-X12. Small curation items from the XRD sessions
- X10 PG re-scan aging audit: status started (numbers above). Needs one question to the PG authors (were samples re-ground or re-made?). Approval: yes needed.
- X11 Failed-scan status gap report: only the "valid" status appears in 1,351 of 1,351 scans though the schema has five. idea; goes into the PG errata (O1).
- X12 Timestamp reconstruction of handling history: GPSS record-creation time to XRD start, median 3.0 days (range 1.0-36.2, n=352) [OWN-EXPERIMENT, proxy]. PG has 0 of 1,035 synthesis times. done as a measurement; idea as a required field.

### X13. dara-conform (the user's OWN existing project) and the tie-in
- What: a calibrated-confidence and "abstain when unsure" layer on top of Dara (an automated phase-ID tool). Pre-registered 2026-07-09. Uses the Dara benchmark (60 patterns), GPSS (about 352), an opXRD labelled subset (about 2,179 candidates), a RRUFF sample (about 200), COD-only reference pools.
- Status: started by the user before these sessions. Known only through session notes; not opened.
- Tie-in proposed: X8 (clean index) and X3 (fair scorer) feed it directly. Its manifest builder already drops RRUFF header-calculated files and HKUST-B.
- Risk flagged: exact duplicates straddling train and test are unchecked.

### X14. "Strongest version" XRD pipeline (from the simulator discussion)
- What: exact, batched, differentiable GPU simulator; inverse model trained on simulated patterns with domain randomization; learn the simulation-to-real residual; test-time refinement plus Bayesian model selection; output probabilities over phase sets.
- Status: idea. Not started. Only a local timing benchmark was done.
- Evidence: [SOURCE] simulate-then-train has been standard since about 2017 (AlphaDiffract has 31M simulated patterns). Periodic's Neon outputs one phase list and no probabilities.
- Risks: see refuted item "distil the XRD simulator" (section C).

### X15. Other XRD ideas that were only mentioned
- PDB+CASP-style yardstick for phase ID (judged a better analogy than ImageNet). idea.
- Licence-clean reference layer (COD CC0 + MP CC BY + computed) plus a task-specific supervision layer. idea.
- Label-provenance audit of public XRD sets (opXRD, AIF Zenodo 21141588, Dara). idea; partly covered by Round 4 w4 and H1-H7.
- Extend atlas-style provenance to opXRD, the Jain-group A-Lab Zenodo archive and Dara ("the work closest to the user's own"). idea.
- Label-origin field: weighed mixture / expert / AI judge / second technique. idea.
- Controlled public-only vs added-context comparison; controlled one-variable comparisons. idea.
- Checklist for press-release benchmarks: k/n counts, base rates, SE z-test, judges that are also contestants, matched cost bases. idea (the four method rules behind it were saved to standing notes: done).
- Open, reproducible FrontierXRD-like evaluation with error bars, and a stronger open-tool harness baseline (the open-tool baseline scored 8.33%). implied by the Periodic analysis, never stated as a proposal.
- Track A7: superconductor negatives with floors plus raw curves. idea, Low priority. See P4-P6.
- Earlier experiment "Dara known-answer scorer with 2 or fewer parameters, target 90%+": launched in an early session, no result (session hit its limit). Superseded by H7 and Round 5 experiment 1.
- "Forensic is-this-really-raw tests": idea in the first session; became B8.

---

## 5. Record Wall / compiled-table line

Source: the Materials Record Wall atlas (9 dataset cases x 8 record layers = 72 cells; artifact ...6VxduLQ5tjW1KqRCgTMFGc) and its debrief (artifact ...GpSntEXMyK6hw9znGTvxAV).

### W1. Record Wall atlas + build.py
- What: an audit page showing, for 9 public datasets, which parts of a record exist (composition, structure, processing, method, signal, uncertainty, provenance, supported tasks).
- Status: done and published (link-shared). 118 files, 27.2 MB.
- Risk: the raw files sit in a temporary workspace. An offer to move them to a permanent folder is unanswered (the user must name a folder).

### W2. Atlas legend fix
- What: define "present" and "partial" and how field-level states roll up; one rule for empty fields and match-only links; show "unknown" and "not in public release" inside partial cells; name the standard behind each layer.
- Gap: the wall's dominant label has no written definition. Cells: present 12, partial 50, absent 8, n/a 2. So 62 of 72 cells use undefined labels [OWN-EXPERIMENT, audit of own atlas].
- Status: specified. "Awaiting your yes." Visible effect: "uncertainty absent in 6 of 9 cases" becomes 4 of 9.
- Approval: YES needed (the page is link-visible; the assistant will not republish without go-ahead). Inputs in hand.
- Note: audit finding F3 in that review was [REFUTED].

### W3. Atlas DFT-tag relabel
- What: relabel one case "DFT -> ML", add "DFT intermediate" / "DFT output" tags, fix the header count (3 of 9 cases are DFT data).
- Status: offered, awaiting the user's yes.

### W4. Record Wall debrief action tiers
- What: 72 gap rows sorted into (1) 43 quick documentation fixes for dataset owners, (2) fixes that need a licence or release decision, (3) feasible new measurements, (4) a "complete-by-design" next dataset.
- Status: specified. None executed. Mostly third-party requests without milestones [OWN-EXPERIMENT, actionability audit].
- Evidence: gap types (a row can have several): definition 41, join 23, observation 17, model 15, uncertainty 14, variability 12. Fix type: documentation-only 49, new-data-only 9, both 14. Share needing new data: join 4%, definition 12%, uncertainty 50%, model 73%, observation 76%, variability 83%.
- Approval: every owner request is outreach: needs a yes.

### W5. Handoff linter (idea from the gap taxonomy)
- What: a check run when data moves from one table or team to the next, since most cheap gaps are definition and join gaps. Status: idea. B3 is its concrete first piece.

### W6. Feasible new measurements named in the debrief
- polymer #4 DSC re-measurement; polymer #6 SEC-MALS; thin-film #7; a glass #4 benchmark across 5-10 labs. (DSC and SEC-MALS are standard polymer lab measurements.)
- Status: idea. Needs labs. Approval: outreach.

### W7. "Complete-by-design" next dataset
- What: design a new dataset so nothing is lost: capture instrument settings at acquisition (Bluesky/NeXus), persistent sample ids (IGSN), replicates, separate value / qualifier / uncertainty fields, ids and a licence from day one. Models named: NIMS data sheets, NIST AM Bench, RSDB, Caltech Materials Provenance Store.
- Status: idea. Needs a lab partner.
- Decision behind it: "completing" old experimental records is ruled out. The unrecoverable rows are listed in the corpus; only a new designed dataset works [OPINION built on OWN-EXPERIMENT].

### W8. Record Wall experiments E1-E7 (pre-registered, launched, NO results - the session hit its limit)
Data was to be fetched; not on disk.
- E1 Matbench-to-MP id mapping table (bar: 90% or more unique structure match on 200 rows). Later done differently as Round 3 / B4; now parked.
- E2 MPEA qualifier and "±" re-extraction from the 2018/2019 source files. Feeds B3.
- E3 SciGlass DOI back-filler via Crossref (95% precision or better; 45,293 blank DOIs). SciGlass line later dropped.
- E4 HTEM API validator. Depends on the API still answering; repos archived 2026-06-30 and the raw endpoint returned HTTP 502.
- E5 Generic dataset quality checker for ambiguous zeros, blanks, qualifiers. Became B3.
- E6 RRUFF-to-NeXus (NXraman) converter plus acquisition template (test: public files fill half or more of the fields). Related to B8.
- E7 Handedness-aware cross-database linker plus MP uncertainty fill. Became B9 / B10; parked.

### W9. gapcheck.py scale-up (early session "E3")
- What: a script that should re-find at least 8 of 10 atlas findings automatically on new datasets. Status: launched, no result.

### W10. Other ideas from the atlas and debrief reports (all status idea unless noted)
- Machine-readable schema per table (GNoME, MPtrj parquet, SciGlass, EBSD .ang files); CHGNet/MPtrj schema plus split id lists.
- Stable ids carried into benchmarks; source database and version as columns; separate value / qualifier / uncertainty fields; handedness-aware ids.
- Matbench sidecar keeping v0.1 frozen (= B4). MP uncertainty fill owned by emmet (= B10). HTEM bug report owned by its lab (= B10).
- MPEA community fork (about 265 articles). Polymer per-value source table (about 8,992 entries; "hard").
- Reuse SNUMAT HSE06 band gaps (10,481 materials) with matminer's 4,604 experimental gaps.
- Hull-distance uncertainty via bootstrapped phase diagrams.
- Composites laminate table plus a boolean "runout" column.
- Field-level levers: round robins, licences, credit for curation, standards, pay-to-re-measure programmes.
- **Within-group label spread as a benchmark noise floor** (steels median 82.7 MPa; glass-transition SD 42.58 K). Non-obvious and cheap [OWN-EXPERIMENT numbers].
- Offered, not done: a tally of the four "partial" forms across the 50 partial cells; charts of the gap patterns; a per-row reference page; a companion xlsx workbook.
- Done utilities: concern map, gap taxonomy, quartz-chain audit method, biff8.py (legacy Excel reader), email guard.

### W11. Actionability audit
- Status: done [OWN-EXPERIMENT]. 188 action items: all say what; 120 say how; 59 name an owner; 11 give a first step; 8 a done-criterion; 3 have all four. This is the measured form of the user's "still too much to read" complaint.

---

## 6. DFT / computed-data line (PARKED by the user's "experimental first" decision)

### D1. DFT-size learning-curve experiment
- What: measure how error on EXPERIMENTAL formation energy falls as you pretrain on more DFT data. A controlled curve nobody has published [SOURCE/OPINION].
- Gap: the user asked whether DFT pretraining gains can be measured and extrapolated.
- Status: specified. Offered twice. "Awaiting your yes." Not started.
- Protocol: (1) fix and de-duplicate the test set; remove its compositions from the DFT data; report with and without. (2) nested DFT subsets 1k / 3k / 10k / 30k / 100k / about 300k, plus one curated subset. (3) 2-3 experimental training sizes x 5-10 seeds. (4) fit error = C + D*N^-alpha and a log-linear line; hold out the largest size; report ranges. (5) treat anything past the largest tested size as a rough guess.
- Evidence: [SOURCE] Jha 2019 (corrected): 0.0715 vs 0.1325 eV/atom, pretrained vs experiment-only. Closest existing curve is Chen 2021 band gaps: each 10x DFT buys -0.13 eV at 100 experimental points, -0.04 at 2,430. [OWN-EXPERIMENT fits] Predicted gain from 41k to 410k DFT is 0.009-0.040 eV, below the roughly 0.08 eV that a test set of about 270 compounds can detect. Backtest success had about zero correlation with extrapolation error.
- Inputs / on disk?: NOT on disk. Needs public DFT sets (OQMD / MP / JARVIS), an experimental set, and Python ML packages (none installed).
- Approval: YES needed for downloads, installs and the run. It also sits on the parked DFT side.
- Risks: measure yes, extrapolate no. Hidden coupling: MP's energy corrections are fitted to experiment (-0.687 eV per O atom), so "DFT to experiment transfer" may leak labels [SOURCE/OPINION]. Only about 13-55% of big DFT databases is informative (Li 2023), so raw count is the wrong x-axis. Do the detection-limit check BEFORE running.

### D2. Done DFT-side deliverables
- "DFT vs Experiment Debrief" report (artifact ...5L2YyZsjLzVkhvjHr1cnm4). done.
- learning-curve-answer-corrected.md (12 proofreading fixes). done.
- Quartz worked example: PBE cell volume +6.29%, r2SCAN +0.37% vs experiment; the Matbench label -3.2741 matches none of MP's three current values [OWN-EXPERIMENT]. done.
- Checklist for any merged DFT + experiment table (ids and version both sides; method; T and P; space group and handedness; value + uncertainty; how records were matched). done as a checklist, not as a tool.

### D3. DFT + experiment join lint (idea)
- What: turn the checklist and the three silent join failures (mixed functionals in one column; #152 vs #154; volume-rescaling matcher) into an automatic check. Status: idea.

### D4. Label-lineage trace Matbench -> MP ("H3" in an early session; Round 3 z1-z3)
- Status: done in part, now parked. 773 MP API requests. Follow-ups dropped. GNoME finding kept: PBE-to-r2SCAN stability flips on 22.1% of 117,043 entries (4.8% with a 25 meV/atom buffer) [OWN-EXPERIMENT].

---

## 7. Company analyses - Discovered Materials (DM)

DM is a two-person startup using LLM agents to propose thin-film materials for chip cooling. Reports: "Discovered Materials Data Gaps (v1)" (artifact ...NA5N4ym6w5pQMF8NrJb8Wb) and its debrief (artifact ...RHyiTnskp6Ad4dTCUamecJ). Page status: "Investigation and design only - nothing built - no one contacted". No direction has been chosen yet.
Key facts [OWN-EXPERIMENT, recount of DM's public files]: 527 of 531 graded submissions pass the computed-property window; the LLM recipe grader passes 1, marks 52 unlikely, refuses 478. Provenance of 526 exported candidates: 504 MLIP, 22 "mlip-verified", 0 DFT. No file links any verdict to a real deposition result.

### DM1. Outcome-grounded recipe evaluation set - RECOMMENDED direction
- What: a dataset plus a scoring protocol ("not an app"). About 80 real low-temperature film-deposition records from 6 or more research groups, 30% or more failures, each with a graded outcome. Then test whether DM's grader (or any predictor) actually predicts outcomes.
- Gap (DM-bottleneck 1 and 2): no public recipe-to-outcome records at 400 C or below with failures included; phase identity squeezed to yes/no where candidates cluster (hexagonal vs faulted cubic diamond). Refused recipes are never run, so the grader's hard penalties can never be proven wrong (selective labels).
- Status: specified. Nothing built.
- Test design: comparators = base rate, nearest neighbour, DM grader with web search on and off, summary-field learner, full-record learner. Splits = leave-one-group-out, leave-one-reactor-type-out, unpublished hold-out. Margin = at least 0.10 AUROC over the grader with a bootstrap 95% CI excluding zero.
- Inputs / on disk?: NOT on disk. Must be curated from literature and labs. First system: sputtered AlN if DM runs PVD; diamond-type carbon if CVD.
- Approval: needs DM's cooperation (user sends the message, DM2), a partner lab, a phase expert plus a second curator (Cohen's kappa 0.6 or more on 20 records).
- Effort: later scale about 150-300 records. First step: literature scoping. Done-criterion: the labelled set, a scoring script with group-held-out splits, a 2-page calibration report.
- Stop conditions: DM already calibrates against outcomes; DM moves to cheap combinatorial runs or amorphous films; no reply in 3 weeks after one follow-up; no grader or rubric access; fewer than about 80 records or under 30% negatives; kappa under 0.6 after one revision; leakage check fails; nothing beats the base rate; grader already at about 0.85 AUROC.
- Risks: DM's first lab work may be PVD/sputtering, not CVD carbon [SOURCE, job post]. Run-to-run noise caps any predictor [SOURCE, founder comment].

### DM2. One-page message to DM
- What: ask Question 1 first: "have grader verdicts ever been compared with deposition outcomes?" Offer an independent calibration report. Do not ask for IP. 3 weeks plus one follow-up. If no reply, do not contact labs on DM's behalf.
- Status: idea, not drafted. Approval: the USER sends it personally.

### DM3. Film thermal-conductivity set linked to computed bulk values - FALLBACK (DM-bottleneck 3)
- What: measured film kappa for AlN and low-temperature diamond, with thickness, boundary resistance, microstructure, method, fit assumptions, uncertainty. Test whether a thickness-aware correction ranks films better than raw computed values.
- Status: idea/specified. Done-when: a source list covering 2 or more materials and 2 or more methods. "Needs little permission." Data not on disk.
- Evidence: [OWN-EXPERIMENT + SOURCE, low confidence] 8 ordinary cubic-diamond entries sit in DM's "novel" set with computed kappa 508-544 W/m-K; a film grown at 400 C measured about 300 (Malakoutian 2022). A free calibration point.

### DM4. Smaller DM items
- Read DM's remaining public files (materials.csv 80.6 KB, mdb-materials.zip 319 KB, several .js files). Status: not done. Approval: download needs a yes.
- Correct the published DM report: 8 fixes plus internal inconsistencies. Status: offered, not applied. Approval: republish needs a yes.
- Outcome labelling protocol: 7 outcome classes plus an ambiguity class and replicate group; 2-3 pages with 5 worked cases. Status: idea.
- Pre-registration document. Status: idea.
- Leakage check (search-off and paraphrase tests on the grader). Status: specified.
- Prospective logging plus exploration arm with DM: log the verdict before each run and the outcome after, starting with the one approved recipe (BC4N); randomly run a few refused recipes. Status: idea. Needs DM.
- Log each rubric criterion as a prediction and score it against outcomes. Status: idea for DM.
- Solo prototype: literature extraction plus a stand-in judge. Status: idea/specified.
- Validation ladder with stop conditions. Status: specified.
- Curation experiments H1-H7 of that session: launched, no results. Build-plan page: started, never delivered.
- Set aside by decision (do not propose again): connector/data pipeline, dashboard, lab notebook/LIMS, universal schema/ontology, building a lab, a binary made/not-made table scraped from papers.

### DM5. Ideas from the interrupted follow-up session (all status idea; no final deliverable)
- Tool-level automatic capture of instrument and process logs (not templates).
- Outcome-calibrated grader evaluation harness.
- Thin-film thermal + phase measurement service.
- Makeability-aware screening (add stability/metastability and thin-film realism); a prototype is possible on DM's public exports.
- A falsifiable validation design: never written.

---

## 8. Company analyses - Periodic Labs

Context [SOURCE]: Periodic's XRD agent Neon scored 55.3% vs 2.7% for the base model on their own 134-sample set with no ground truth. 55.3% is best-of-7 with a learned selector; a single attempt is about 36%. The standard error is about +/-4.3 points, so Neon vs the next system is a statistical tie. The tool harness alone is worth about 3.8x (one digest says 31.63%, two others 31.53%, vs 8.33%).

- P1. "Measurement-checked XRD set from one outside lab" (revised pilot). What: about 150 synthesis attempts, 40 or more retained specimens, each checked by a second technique (SEM-EDS, TEM, TGA: microscope- and heating-based checks of composition and phase). About 12 weeks, about 200 hours, compute about $1,850 (or about $290 at low effort). Claim list sealed first; continue/stop rules defined. Status: specified, not started. Blocker: an outside lab (approval + partner). The earlier Pilot 1 (levels L0/L1/L2) is superseded.
- P2. Pilot sub-ideas: planted errors, injection tests, known-mixture standards, context ablation, abstention tests. Status: idea.
- P3. Nine questions for Periodic plus a watch list of signals. Status: specified, NOT sent. Approval: user decides and sends.
- P4. Hosono negatives extraction. Status: DONE [OWN-EXPERIMENT]. Of 671 entries in a published table of tried superconductor candidates, 332 (49.5%, CI 45.7-53.3%) were "never made". The made / not-made mark exists only as cell colour: 0 of 671 marks survive text extraction. 0 of 671 record measurement conditions. 384 formulas can be matched exactly.
- P5. Label-propagation test (Hosono -> Stanev 2018 -> 3DSC, two ML superconductor datasets). Prediction: 10% or more of matched "Tc = 0" entries were never actually made. Status: specified, script ready, NOT run. Blocker: download permission for Supercon_data.csv (358 KB) and 3DSC_MP.csv (9.46 MB), both CC BY 4.0.
- P6. NIMS SuperCon label-noise test. Status: idea. Needs a 1.88 MB and/or 17.4 MB download (approval).
- P7. Literature cross-check of seeded entries (25 + 15, seed 20260916). Status: started, no result.
- P8. Raw PPMS/MPMS re-extraction pilot (re-read raw files from common low-temperature measurement instruments). Status: idea.
- P9. Recover lost context via operator interviews and Taiwanese theses. Status: idea.
- P10. "What would settle it" benchmark: synthesis-planning with robot-confirmed outcomes. Status: idea addressed to Periodic and the field; needs a robotic lab. Not for the user to build.
- P11. Watch list: Periodic, the DeepMind UK lab, NUS Materials Data Foundry, DOE Genesis, CuspAI exclusivity. Status: idea.
- Files for this work sit in a temporary scratchpad. The build-plan workflow for this session started and produced no output.

---

## 9. Recursion / looped-model survey (published, artifact ...GvUexcJ37BA6dh4JuyGCET)

A literature survey: 110 papers, 56 datasets, 10 searches that came back empty. No experiments by the sessions. Nothing on disk. All directions below are status **idea**. The assistant ranked them cheapest first; the user never responded. They are all on the computed-data side and were never connected to the experimental agenda.

1. Looped (weight-tied) small model for small-data property prediction. Bars on Matbench steels: TPOT-Mat 79.95 MPa, AutoML-Mat 82.30, MODNet 87.76, TRIADS 91.20 [SOURCE]. Also run TabPFN (a pretrained tabular model) on steels: untested, near-zero cost.
2. Variable loop depth / adaptive stopping in MLIPs. Baselines DEQuify and I-MLFF; test on ISO17 and SPICE.
3. Data-repetition (multi-epoch) scaling study for potentials on MP-r2SCAN (238,247 frames). Blocker: GPU budget.
4. Diffusion vs autoregressive crystal generation under limited data (CrystaLLM vs DiffCSP on MP-20 subsets).
5. Curves of S.U.N. rate (share of generated crystals that are stable, unique, novel) vs sampling budget. Called "cheap"; needs a stability checker.
6. Learned mixing for the DFT self-consistency loop. Needs DFT expertise.
7. TRM/HRM-style recursion for crystal structure prediction or retrosynthesis. Largest gap, riskiest.
- Also noted: an agent "edit, run, keep if held-out error improves" loop on Matbench works on one consumer GPU [SOURCE]; the reusable asset is the auditable harness with a holdout check.
- Also noted: a dated, source-verified dataset-card registry is itself a small contribution (the survey found many conflicting headline dataset sizes).
- Evidence caution [SOURCE]: no looped materials model clearly beats the best conventional model. The refinement loop plus deep supervision, not the architecture, drives the gains.
- Offered, not done: publish the wrap-up as a page; copy the build files out of the temporary folder; an optional verification workflow.

---

## 10. Outreach and errata actions (all need the user's explicit yes; none sent)

### O1. Send the error lists already in hand
- What: error reports to database owners. The main session calls this the "days" item; the XRD report calls it "an immediate, credible contribution needing only the user's approval".
- Contents [OWN-EXPERIMENT]:
  - Starrydata: 8 wrong curves.
  - RRUFF: about 1,700 "RAW" files that declare a calculated profile; 11 file pairs with identical data under two mineral names (8 adjudicated weakly, 3 unresolved).
  - opXRD: 499 HKUST-B patterns copied from RRUFF (414 calculated, marked not simulated); 124 exact duplicates, 15 groups with conflicting labels.
  - PG ledger: weight_percent holds fractions (sums to 1.0 in 994 of 994); negative mass_for_xrd_mg in 19 of 991; stray Pb in 7 samples; 2 of 750 ICSD ids under two formula spellings; only "valid" scan status; verification method "manual" on all 1,216 blocks though 810 sit on automated fits; 20 scan files with no ledger entry; SiO2 #180 in 20 samples with scan temperature empty; undocumented 100 mg threshold; hydrate stocks stored as anhydrous formulas (132 samples).
  - Dara: README says "equal weight" but file names encode 10-90 wt%. GPSS: scan timestamps run 28 Jul-29 Dec 2025 vs the paper's 3 Nov-26 Dec 2025. A Li4CO5 CIF is mislabelled. COD 9000004 declares one space group but its atoms have another symmetry (checked only on a regenerated local copy).
  - Parked: Matbench issue #124, the emmet field, the GNoME density unit, HTEM.
- Status: drafted, unsent. The PG draft (ERRATA_DRAFT.md) needs its own retractions applied first (the "28% carry an error" claim became 9.0% strict). Round-4 artifacts have known defects (w1 README tolerance, 2 queue rows, header counts 125 / 414).
- Risks: no source paper was opened in the Round-4 adjudication. Several adjudications are weak. HTEM and MPEA cannot take fixes any more.

### O2. Questions to dataset authors
- One question to the PG authors (re-scan handling; failed scans; SiO2 #180). Status: idea. Needs a yes.

### O3. Standards proposals
- Handling-history fields to NeXus / pdCIF / NOMAD; experimental fields to OPTIMADE; RRUFF 13-field header packet; field requests to TE database owners. Status: idea to drafted. Needs a yes.

### O4. Company outreach
- DM message (DM2): user sends. Nine questions to Periodic (P3): not sent.

### O5. Partner recruiting
- XRD raters and a diffractometer lab (B11, X4, X6); 3 or more TE pilot labs (B12, T2); an outside lab for P1; a partner lab and curators for DM1. Status: none started. Needs a yes.

---

## 11. Reports and housekeeping

Published and done: Record Wall atlas; Record Wall Debrief; "Toward a Materials ImageNet"; Materials ImageNet Debrief (artifact ...WLmZGmNU3k87iizhuMSbJs); TE Benchmark Spec 0.2; XRD Curation Experiments; DFT vs Experiment Debrief; Recursion in Materials AI; DM Data Gaps v1; DM Debrief.

Started and never delivered: a "Materials Build Plan" page; build-plan workflows in the DM, Periodic and Record Wall sessions.

Open offers (each awaits the user):
- Publish the build list as a page.
- Move sidecar / crosswalk files; delete the roughly 0.9 GB MP cache.
- Move atlas raw files and recursion build files out of temporary folders (user must name a folder).
- Publish the ImageNet answer, the Periodic analysis and the recursion wrap-up as pages.
- Pin the MatterLab chat; save a user-profile memory note.
- Apply W2, W3 and the 8 DM report corrections.

Known stale text in published reports: the Materials ImageNet Debrief still carries the old wording of the Round-1 composites claim (retracted: lay-up never varies; the confounded factor is test environment vs cure schedule). Two Periodic statements were retracted ("a closed lab can produce labels ... without public data"; "that weakens the idea of an ImageNet built by pooling public records"). Two reports repeat "three PhD experts per pattern on thousands of calibration patterns", which the Periodic analysis session marked unverified.

---

## A. The current ranked working order and the Round-5 candidates (as the latest notes state them)

**Working order (memory notes / build list, 2026-09-18), quoted:**

> "Order: B1 → B2 → B3 → B8 → B11 desk stage → B5–B7, B12. All extend existing tools; all data for the first four is on disk."

- B1 te-validate - "TE validation report + submission checker. Specified; scripts exist, ESTM formula-cell detector unwritten (1–2 days). First step: one command reproducing TE spec §3a/3d counts with identical hash. Reuse teMatDb zT filter (arXiv 2505.19150). 1–3 months."
- B2 splitgen - "paper-grouped splits, leak report, manifest. Started (DOI normaliser saved); next reproduce §3e split table. GroupKFold + MatFold. 1–2 weeks."
- B3 recordlint - "qualifier/uncertainty/null linter. Specified; first step CLI + regression test on MPEA numbers. 1–2 weeks."
- B8 release-file lint + schema packets - "started: 13-field RRUFF header proposal drafted; must round-trip on 30 saved spectra (JCAMP-DX; Croissant). ~2 weeks for packets."
- "Parked: B4 MP side (steels member table stays), B9 crosswalk (70-row prototype, 60 dedupe-eligible), B10 emmet patch (HTEM errata CSV stays)."
- "B5 scoring harness (z′/ζ, key hash; metRology, Codabench), B6 baselines (reproduce 25.5/42.2, then 2,839/870 set; median metric; run MODNet, Dummy): 1–2 weeks each. B7 specimen layer: blocked on descriptor quality."
- "B11 XRD known-answer + multi-rater set: desk go/no-go first; ~10³ expert-hours. B12 TE label-production kit: needs ≥3 pilot labs. Dropped: SciGlass export patch."

**Round 5 candidates (memory notes), quoted:**

> "Round 5 (all on disk): (1) Dara weighed-mixture known-answer test + 2-min vs 8-min repeat scans, file-only lint blind on 61 Dara patterns — decides B11; (2) hide PF curve on 273 localizable specimens, measure real wrong-fix rate — decides B1; (3) five frozen checks over all 55,422 Starrydata samples with a second-curation null; (4) registered replot detector with 590 "Reference" samples; (5) does hold shortfall predict reaction outcome."

**What the last chat slice adds (same day, later):** Round 5 was started in the background with four experiments and has no results yet. E1 = Dara weighed-mixture known-answer + 2-min/8-min repeat scans + GPSS. E2 = PF-ablation wrong-fix rate on 273 localizable specimens (72 DOIs), with a null on 5,917 clean specimens. E3 = five frozen checks over all 55,422 Starrydata samples with a second-curation null. E5 = PG furnace-hold shortfall vs reaction outcome (147 samples at 1000 C or above). E4 (registered replot detector, 590 "Reference" positives) was deferred.

**Late evening, two sibling sessions (not reconciled):**
- Main session's recommendation [OPINION on OWN-EXPERIMENT numbers]: commit to the TE line in the order errata -> spell-checker (B1) -> fair exam (B2) -> small benchmark. Reason given: TE is the only area with a large dataset, a physics equation that checks records without the paper, and three overlapping independent databases. "We have run enough experiments."
- XRD session (had not answered yet): five ideas under 9 adversarial checkers. Tentative plan: error reports (O1) + usable-files index (X8) now, as door-openers to the labs needed for the hard known-answer set (X6); the scoring tool (X3) as the bridge; tie X8 and X3 to the user's own dara-conform project.

---

## B. Ideas that appear in the sessions but never made the ranked list

Grouped by how close they are to being actionable with data on disk.

**Data on disk, no partner needed (closest to actionable)**
- X3 crosswalk + fair-scoring library for phase ID. (On the ranked list only as parked B9, which is a different, MP-side thing.)
- X8 usable-files index of open XRD scans.
- X9 plausibility lint for fitted phases.
- X2 handling-history schema (design work; acceptance test on disk; proposing it is outreach).
- O1 sending the error lists (on the list only as an approval item, not as a build).
- T5 packaged small fair TE benchmark; T6 second-curation null as a tool; T7 oracle/lookup research note.
- W5 handoff linter; within-group label spread as a benchmark noise floor (W10).
- D3 DFT + experiment join lint (parked side).
- X13 tie-in to the user's dara-conform project, including a duplicate-straddle check.

**Needs a download or a yes first**
- P5 Hosono -> Stanev -> 3DSC label-propagation test (script ready; 358 KB + 9.46 MB).
- P6 NIMS SuperCon label-noise test.
- D1 DFT-size learning-curve experiment (listed only as an approval item).
- DM4 read DM's remaining public files.
- W2 / W3 atlas fixes; DM report corrections.

**Needs a lab, raters or a company**
- X4 multi-rater pilot, X5 judge-calibration kit, X6 redesigned weighed-mixture set, X7 blind XRD challenge (B11 covers X4 + X6 only at the go/no-go level).
- T2 blind TE round, T3 reference checks (B12 covers the lab kit only).
- DM1 outcome-grounded recipe evaluation set, DM3 film-kappa set, DM exploration arm, all DM5 ideas.
- P1 measurement-checked XRD set from one outside lab; P2, P8, P9, P10.
- W6 feasible new measurements; W7 complete-by-design dataset.

**Pure research directions, never linked to the main agenda**
- All 7 recursion directions (section 9), TabPFN on steels, agent edit-run-keep loops, dataset-card registry.
- X14 "strongest version" XRD pipeline.
- Licence-clean reference layer; PDB+CASP-style yardstick; controlled public-only vs added-context comparison; press-release benchmark checklist; label-origin field; OPTIMADE proposal (X15).

**Launched earlier and abandoned without results (decide before re-running)**
- Early-session E1-E6 (includes the Dara scorer and a rerun of the zT validator); gapcheck.py scale-up; Record Wall E1-E7 (W8); DM-session H1-H7; Periodic literature cross-check P7; three build-plan workflows.

---

## C. Tried and refuted - do not revive by accident

All [REFUTED] unless marked otherwise.

**TE**
- Automatic unit fixing. "Most unit errors are fixable" (85 of 266; 6 or more wrong). "Gated rule gives 1% or fewer false fixes" (measured 7.2%, CI 0-19%; fixed 0 of 12 proven two-curve errors). zT-only auto-fix wrongly fixes about 19% of two-error records. Decision: never auto-fix units; review queue only.
- The assumed 25% two-curve error share (measured 13.7%, 18 of 131).
- "zT is never the wrong curve." The PF curve cannot referee (single suspect in 54.3%).
- Curve-only replot detector (51 of 272 vs nulls 38-57).
- The "sibling" auto-rule (fires on 23.6% of agreeing pairs); the systematic-offset rule (no information).
- "Descriptor clean-up recovers specimen context" (43% coverage vs 50% bar).
- "Figure digitisation is the bottleneck" - it is not (about 0.5-1% scatter) [OWN-EXPERIMENT].
- "No certified kappa reference exists" (BCR-724 exists). ">=20% SD across 11 labs" and "round robins take 4-12 months" as stated earlier (corrected figures are in T2 / the spec).
- 35 precedent wordings in the TE spec were corrected (for example the SAMPL "no anonymous submissions" date).

**Compiled tables / synthesis ledger**
- "Conditions help within steel groups" (fails once leakage is controlled).
- "28% of PG samples carry an error" (strict rate 9.0%, 93 of 1,035; the 28.2% counted provenance notes).
- "Not a furnace effect" for PG hold shortfalls (post-hoc: 13 of 13 vs 0 of 7 runs at 1000 C by furnace; a lead, not a result).
- "Chemical mass ceiling is a good lint" (recovered mass cannot test chemistry).
- "56 files with 8,500 rows" (it is 125). "Cell fit settles 8 of 10."
- Retrofitting ("completing") old experimental records as a strategy. SciGlass export patch and SciGlass uncertainty parser: dropped.
- Round-1 composites claim (lay-up never varies; the confound is test environment vs cure schedule).

**XRD**
- H1: "enough hard multiphase patterns exist for a full eval set" (167 vs 270 needed).
- H6 read as a software bug. Merging mirror hands is CORRECT for powder XRD. What is unsafe is the default tolerance (merges alpha/beta quartz) and oxidation-state labels.
- "More weighed mixtures" as the fix. It is "harder mixtures" (H7 inconclusive: 38/40 vs 35/40).
- Using PG/GPSS labels as independent raters (one editor id). Using public PG/GPSS/Dara answers as a hidden test split.
- opXRD multi-phase share 41.4% (miscoded; it is 18.1%, 485 of 2,680).
- "Both-handed formulas are polymorphs" (74% are mirror copies). The 10x RMSE mirror-copy threshold (ratio as low as 2.58).
- "Weighed truth stops at 3 phases" (true for Dara only). "Nobody has measured interpretation error."
- **Distilling the XRD simulator into a neural net.** The simulator is already cheap: 4-13 ms per pattern in pymatgen, about 0.3 ms vectorized, 1M patterns in about 2 core-hours [OWN-EXPERIMENT timing]. Distillation still makes sense only for nanoparticle/amorphous scattering, electron diffraction, or Monte-Carlo instrument ray tracing.
- "Neutron diffraction is a better XRD." The user's premise that Neon outputs probabilities (it outputs one phase list).
- Non-commercial licensing as the main blocker (bulk access is).
- Several pre-registered checks passed by construction; row-level confidence intervals on clustered data were wrong. Method rule now: matched nulls, count clusters (papers, runs).

**Computed / DFT**
- Jha "0.06 vs 0.13-0.15" (pre-correction; corrected 0.0715 vs 0.1325). "Jha never varied DFT size", said flatly, is too strong: Jha 2019 did not vary DFT size *for transfer* (it always used all of OQMD), but a DFT-only table (11k / 24k / 341k -> 0.19 / 0.16 / 0.14) and Jha 2022 (JARVIS 20k / MP 102k / OQMD 353k -> 0.087 / 0.078 / 0.064 eV/atom) exist, both confounded because the databases differ in more than size [SOURCE]. "Jha's 0.07 is already at the noise floor." The "don't extrapolate past about 10x" rule (even 10x is too wide). The unqualified "only about 6 DFT points per experimental point". Chen 2021 as a clean pretrain-then-fine-tune curve (it is joint training).
- "OPTIMADE 2023-04-27" as the Matbench label source. "1,411 requests / 3.5 CPU-h." "page_limit max 500."
- "Computed records are all-or-nothing" (softened: 42% partial for computed vs 83% for experimental). "The cause is usually physical." "No 1064 nm Raman SRM exists" (SRM 2244 exists). "PolyMetriX has 6 versions" (7). "Citrination shut down" (public datasets remain). NOMAD does hold a 2021 MP mirror. Atlas audit finding F3. The atlas's own DFT/ML tagging (3 of 9 cases are DFT).

**Companies / surveys**
- "Periodic shows a closed lab can produce labels without public data"; "that weakens a pooled-public-records ImageNet"; "expert majority 84%"; "3.8x success for 19% more cost" (12 further wording corrections).
- DM: "60 of 526 recipes mention off-line fabrication" (about 50, crude scan). Three citations were used beyond what they show (Guo et al. is a simulation; Raccuglia 2016 has no with-vs-without-failures comparison; Jia 2019 is about human selection bias). "460 of 531 verdicts unanimous" holds only as a sum over 17 model rows. "Experts calibrated the grader": unverifiable.
- "Negatives merged at source" for the Hosono table (the loss is downstream).
- Recursion survey: TRIADS trails MODNet; an AutoGluon "77" baseline was dropped; SeqBattNet's headline gain (a plain feed-forward net edges it on NASA data); A-Lab 41 of 58 is now 36 of 57; ICAL 8/10 is 7/10; HRM's ARC score 40.3% re-ran at 32%. The first quick answer in that session was wrong in 13 places.

---

## D. Blocked on the user's approval (nothing below has been done)

**Sending or posting anything public**
- O1 all upstream error reports: Starrydata (8), PG errata draft, RRUFF, opXRD, GPSS, Dara, COD 9000004, and the parked Matbench #124 / emmet / GNoME / HTEM items.
- O2 one question to the PG authors.
- O3 schema and field proposals (NeXus, pdCIF, NOMAD, OPTIMADE; RRUFF header packet; TE owner field requests).
- O4 the DM message (user sends personally) and the nine questions to Periodic.
- O5 recruiting raters, labs or curators (B11, B12, X4, X6, T2, P1, DM1).
- X8 publishing the usable-files index.

**Downloads and installs**
- PG raw scans (23 MB) and refinement files (291 MB).
- Full opXRD (about 1.4 GB).
- COD CIF 9000004 (one file) and a few source PDFs.
- Supercon_data.csv (358 KB) and 3DSC_MP.csv (9.46 MB) for P5; NIMS SuperCon files (1.88 MB and/or 17.4 MB) for P6.
- DM's remaining public files (materials.csv 80.6 KB, mdb-materials.zip 319 KB, .js files).
- DFT and experimental datasets plus Python ML packages for D1.

**Go-aheads**
- D1 the learning-curve experiment itself.
- W2 atlas legend fix (republish); W3 atlas DFT-tag relabel; the 8 DM report corrections.
- Housekeeping offers in section 11 (publish pages, move files to a folder the user names, delete the MP cache, pin a chat, save a profile note).

**Standing guardrails stated in the sessions**
- Do not unpickle PG .pkl files. Do not run downloaded .py files. Do not modify anything under the user's github folder.
- Experimental data first; no bulk DFT pulls; computed values are never ground truth for experimental labels.
- User's own: "Do not automatically recommend a data platform, lab notebook, ontology, dashboard, or another AI scientist." "Do not assume richer data improves decisions." "Be willing to conclude that the dominant bottleneck is inaccessible to us." "Avoid unsupported percentages or speedup estimates."
- Working assumption never confirmed by the user: "we" = a small team that writes software and works with public data, with no lab of its own.

---

## E. Inconsistencies inside the corpus (check before relying on them)

1. **B-number clash** (see section 0).
2. **TE-first vs XRD-first**: two sessions, two recommendations, not reconciled. The earlier ImageNet report also left Track A vs Track B undecided.
3. **"GPSS and Dara on disk but unread"** (memory notes) vs the XRD session, which analysed both (H1-H7) from its own workspace copy.
4. **Dara file counts differ by note**: 20 reactions / 40 weighed-mixture scans (XRD report); 41 mixture files (last chat slice); 60 patterns (dara-conform notes); 61 patterns (Round 5 wording); 70 files (memory-note repo listing). Count on disk before trusting any Round 5 E1 result.
5. **XRDBench answers**: the XRD report and memory notes say the evaluator keeps them; the late XRD-session notes say they are in a public JSON with no licence; the ImageNet report says "published answers".
6. **Round 5**: the memory notes list five candidates; the last chat slice says four were started and the replot detector (4) was deferred.
7. **PG re-scan numbers**: report = 105 of 136 (77%) vs 12 of 25 (48%); a chat slice = 154 of 184 vs 9 of 14. Different cuts of the same 184 samples.
8. **B1 effort**: 1-3 months (build list) vs 1-2 weeks (main session's effort table, for the narrower spell-checker).
9. **Harness figure**: 31.63% in one digest, 31.53% in two others.
10. **Data persistence**: TE data, the usable-files manifest, atlas raw files, Periodic/Hosono files and recursion build files are all said to sit in temporary session folders. An earlier "PG ledger not local" note was wrong (only two repos had been searched); the ledger was already on disk.
11. **Dev-set size**: use 2,839 specimens / 870 DOIs, not the earlier 3,361 / 951.
12. **Stale published text**: see the end of section 11.

