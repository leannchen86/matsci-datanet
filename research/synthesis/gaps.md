# The Gap Ledger: every problem the corpus found in ML for materials

Built from all 33 digest files (N00, C01 to C16, R01 to R10). One entry per distinct gap. Duplicates across sessions are merged. Where two sessions give different numbers, both are shown and the later or corrected one is named.

**The one-paragraph picture.** The field has plenty of *computed* data and very little *measured* data that an ML person can trust, join, or test on. The gaps below fall into seven groups: bad labels, broken identity, untrustworthy evaluation, unrecorded context, access and incentives, the simulation-to-reality gap, and over-claimed lab automation. The user's own experiments are strongest on the first three groups. The last three rest mostly on literature and opinion.

## How to read this

**Status tags.** Every claim carries one.
- [OWN-EXPERIMENT]: the user's own sessions measured it on real files.
- [SOURCE]: a paper, dataset page or company post says it. Not re-measured here.
- [OPINION]: a judgment by the assistant or the user. No measurement behind it.
- [REFUTED]: claimed in one session, then shown wrong or weakened later.

**Slices.** C01 to C16 are chat sessions. C15 and C16 are late updates from two sessions that were still running (C15 is the main thermoelectric line plus XRD ideas; C16 is a verification pass on five XRD candidates, called c1 to c5). R01 to R10 are the published reports. N00 is the project notes file. Findings marked "single-agent" in C16 were found by one search agent and not double-checked.

**Build names.** The corpus uses five clashing id schemes (the notes file B1 to B12, the XRD page B1 to B7, Track A1 to A7, bottleneck labels B1 to B3 in four different reports, and the TE spec B1 to B8). This ledger names each build in words, then gives the id and its source in brackets.

**Seven words you need first.**
- *DFT*: a quantum simulation. It produces computed labels, not measured ones. Think of it as a synthetic-data generator with known systematic bias.
- *Powder XRD*: shine X-rays at a powder, get a 1-D curve. The curve is a fingerprint of which crystals are in the sample.
- *Phase*: one crystal type inside a sample. "Phase identification" is multi-label classification of an XRD curve.
- *Specimen*: the physical piece that was measured, with its processing history. Not the same as its chemical formula ("composition").
- *Thermoelectric (TE)*: a material that turns heat into electricity. Its quality score is zT, computed from three measured curves: Seebeck coefficient S, resistivity ρ, thermal conductivity κ.
- *Round robin*: many labs measure the same specimen. It is the lab version of inter-annotator agreement.
- *Materials Project (MP), Matbench, Starrydata*: a big DFT database, a set of 13 fixed ML benchmark tasks, and a database of numbers read off published TE plots.

**The seven themes.**
1. Labels you cannot trust (G1 to G9)
2. Identity and joins: you cannot tell which thing a row is about (G10 to G15)
3. Evaluation you cannot trust (G16 to G24)
4. Context that was never recorded (G25 to G29)
5. Access, ownership and incentives (G30 to G36)
6. Computed labels versus the real world (G37 to G41)
7. Lab-automation claims, makeability, and the project's own process (G42 to G50)

---

## Theme 1. Labels you cannot trust

### G1. Thermoelectric databases contain value and unit errors that nothing catches
- **Gap.** A small but real share of TE records are wrong by a unit slip, a sign flip or a swapped curve, and range checks do not see them.
- **Why ML cares.** These are label errors in both train and test. A power-of-ten error dominates any squared loss.
- **Evidence.** [OWN-EXPERIMENT] zT can be recomputed from the other three curves, like a checksum. On 13,702 Starrydata samples with declared zT above 0.05: 11,587 agree within 10%, 801 are off by 10 to 20%, 668 by 20 to 50%, 646 by more than 50%. (An earlier count of 13,704 / 667 / 649 is superseded.) For real experiments only (n = 11,004): 9,307 / 642 / 529 / 526, about 84.6% within 10%. Of the 646 bad ones, 266 are clean powers of ten, and 587 have every input inside a plausible range. Control set: teMatDb272 has 270 of 271 within 10%. Second check: two independent digitisations of the same figure disagree by more than 10% in 15 of 361 comparisons (4.2%, CI 1.7 to 7.4%), "about 1 in 25". The 8 Starrydata errors found were Celsius stored as kelvin (2), a sign flip, a power of ten, conductivity filed as Seebeck, a curve swap and a squeezed temperature axis. No source paper was opened to confirm. Other counts: 2,622 curves have no finite points (787 samples entirely empty), 240 Seebeck curves out of range, 770 curves with temperature outside 1 to 2000 K, 3 test records, 364 samples with battery descriptors. Snapshot size: 55,422 samples, 156,721 curves, 9,512 papers; Experiment count 32,435 (an earlier 32,497 is [REFUTED], 62 rows double-counted).
- **Slices.** C03-1, C03-2, C03-3, N00, R07, C15.
- **Others addressing.** Partly. teMatDb's Sc-ZT filter does the zT recompute and kept 10,840 of 15,532 [SOURCE]. It stores no power-factor curve, so it cannot catch power-factor errors.
- **Build.** TE record validator "te-validate" (N00 B1; C15 calls it a "spell-checker"). Scripts exist. First step: one command that reproduces these counts. Also Round-5 experiment (3): five frozen checks over all 55,422 samples. No results yet.

### G2. Automatic repair of those errors is not safe
- **Gap.** You can detect a bad TE record, but you often cannot tell which of the curves is wrong, so auto-fixing creates new errors.
- **Why ML cares.** A cleaning step that silently writes wrong "fixes" is worse than noise, because the fixed rows look verified.
- **Evidence.** [REFUTED] "Most unit errors are fixable": only 85 of 266 were fixed and at least 6 of those fixes are likely wrong. [REFUTED] "A gated auto-fix has at most 1% false fixes": round 2 gave 11.2% under an assumed 25% share of records with two bad curves. Round 4 (later) measured that share at 13.7% (18 of 131 specimens from 36 papers). Two intervals exist: 8.9 to 20.7% if rows are treated as independent, and about 3.1 to 26.3% when resampling by paper. The by-paper one is the honest one, because errors are paper-wide. At paper level it is 6 of 36. On round 2's narrower definition it is 7.6% (10 of 131), and 6 of those 10 come from one paper. The floor from the zT identity alone is 12 of 131 (9.2%). Round 4 also measured a false-fix rate of 7.2% (CI 0 to 19%, low confidence; 4.4% when a power-factor curve exists, 11.9% without). The rule fixed 0 of 12 proven two-curve errors. [OWN-EXPERIMENT] Errors are paper-wide: 59 of 60 paper groups get one consistent call, so the real sample size is papers, not rows. Power factor is the single suspect in 133 of 245 cases (54.3%). Hand check 22 of 24, but only 11 of 13 where there was a real choice. Review queue: 633 specimens in 230 papers.
- **Slices.** C03-2, C03-3, N00.
- **Others addressing.** No. No existing tool checks power-factor errors.
- **Build.** Same validator, with the decision "suggest, never auto-fix". Round-5 experiment (2): hide the power-factor curve on 273 specimens and see if the error can still be localised. No results yet.

### G3. Benchmark labels are averages that hide a large spread
- **Gap.** Several benchmark rows are the mean or median of many different measurements, and the spread was thrown away.
- **Why ML cares.** The model is scored against a number nobody measured. Reported error can drop below the real noise.
- **Evidence.** [OWN-EXPERIMENT] matbench_steels averages 842 source records into 312 rows (311 of 312 are means; 21 duplicates). One group of 53 records spanning 1005.9 to 1605.4 MPa became 1338.0. Across 160 multi-record compositions the median spread is 82.7 MPa, max 1225.8. A random forest scores MAE 91.1 MPa on the averages and 116.9 on the raw records (gap CI 11.5 to 43.8); ridge regression shows no gap. The file also drops 350 Charpy and 165 KIC values (two toughness tests), and its "Temperature" field is undefined. Polymer glass-transition set (PolyMetriX, 7,367 rows): the label is a median; "std 0.0" on 7,088 rows just means one value; 46.6% of multi-value rows span more than 10 K; one PLA row pools 10 values from 192 to 333 K into 324.5. High-entropy alloy set (MPEA): one alloy, CoCrFeMnNi, has 47 rows from 22 papers with yield strength 208 to 1692 MPa; grain size is recorded in 237 of 1,545 rows. [REFUTED] "Test conditions explain the steel spread": temperature explains 4.25% (p about 0.43), and 66 of 312 groups have a near-twin composition in another group.
- **Slices.** C01-1, C01-2, C01-3, C03-2, N00, R01, R03.
- **Others addressing.** No one in the corpus.
- **Build.** Steels member table that restores the per-record values (the surviving part of N00 B4); record linter (N00 B3); split generator that groups near-duplicates (N00 B2).

### G4. Qualifiers, error bars and the meaning of "blank" are destroyed during compilation
- **Gap.** When data is copied into a table, ">300" becomes 300, "±" values are deleted, and an empty cell can mean several different things.
- **Why ML cares.** Censored values (known only as a bound) become fake exact labels, and you lose the per-label noise you need for weighting.
- **Evidence.** [OWN-EXPERIMENT] MPEA has 382 damaged cells: 264 "±" deleted, 49 ">" and 50 "<" stripped, 19 ranges collapsed ("150-200" became 175). 0 of 263 ± cells say which statistic was meant. The meaning of a blank is recoverable for only 25.6% of cells (12.2% without a rule invented after the fact). The value `0` has 8 meanings across 5 datasets; blanks in the composites set have 4. SciGlass drops ± values, ranges and methods that exist in its own source scripts, and has 0 DOIs on 45,293 references. RRUFF (a minerals database) drops error estimates when it copies headers, and its microprobe SD divides by n instead of n−1. Across 9 atlas cases, uncertainty is absent in 6 of 9. A later, consistent legend rule (C08, R08) makes it 4 of 9, because empty uncertainty fields should count as "unknown" not "absent". Show both; the 4 of 9 is later. Provenance is only partial in 9 of 9. [SOURCE] Two common table schemas (Frictionless, GEMD) cannot express an inequality or a censored value.
- **Slices.** C01-1, C01-2, C01-3, C03-2, C08, C09, N00, R01, R08.
- **Others addressing.** No.
- **Build.** Record linter "recordlint" (N00 B3; specified, 1 to 2 weeks; first step is a command-line tool with a regression test on the MPEA numbers). A generic `gapcheck.py` that must re-find at least 8 of 10 atlas findings was launched with no result.

### G5. Released files have wrong, undefined or swapped fields and units
- **Gap.** Public data files ship with mislabelled units, swapped columns, undefined flags and headers that change halfway down.
- **Why ML cares.** A loader that trusts the header trains on the wrong quantity, and nothing fails loudly.
- **Evidence.** [OWN-EXPERIMENT] GNoME (DeepMind's set of predicted crystals): density is documented as Å³/atom but the values are g/cm³; the `Is Train` flag is True 412,757 / False 72,513 / blank 68,784 and is never defined; the decomposition-energy column is blank in all 554,054 rows; band gap is 'inf' in 14,565 rows; a formula spelled "NaN" is parsed as missing. MPtrj (frames used to train force-field models): 1,580,484 rows in the file vs 1,580,395 in the release text; stress is in kbar and needs a factor of −0.1; no per-atom energy column. HTEM (NREL thin-film database): absorption coefficient equals transmittance in 44 of 44 positions; resistivity unit label is wrong; the xrd and optical kinds are swapped in one file; gas names are spelled four ways (ARGON 562, Argon 469, Ar 31, "VACCUM" 28); substrate is null in 796 of 1,891 libraries; `peak_count` is the constant 207944; no units anywhere in the JSON. Composites set (2,558 rows): a second header at row 911 redefines 10 columns for 1,685 rows; 56 legends live only in cell comments; 20 duplicate "unique" ids; "*" in 480 rows is undefined. MP has a misspelled field `energy_uncertainy_per_atom` that is empty on 342,144 documents, although the underlying library computes the value. In one microscopy (EBSD) file the "confidence" column actually holds a dot product.
- **Slices.** C01-1, C01-2, C01-3, C08, C09, N00, R01, R08.
- **Others addressing.** No. HTEM (archived June 2026) and MPEA (archived Nov 2024) can no longer accept fixes.
- **Build.** Release-file lint plus "schema packets" that document each file (N00 B8). HTEM errata list as a CSV (the surviving part of N00 B10; the MP code patch is parked). Filing issues upstream needs the user's approval.

### G6. Files called "raw" are often processed, or not measurements at all
- **Gap.** Many XRD files labelled RAW are calculated patterns or already cleaned, and open XRD collections copy them without saying so.
- **Why ML cares.** You think you are training or testing on real instrument noise, but you are testing on synthetic data. It also creates hidden train/test duplicates.
- **Evidence.** [OWN-EXPERIMENT] RRUFF: 1,702 of 3,019 "RAW" powder files (56.4%) declare a calculated profile in their own header. A noise signature computed from the file alone agrees with the header 97.4% of the time (AUC 0.998). The quartz "RAW" pattern has a maximum of exactly 100.0 and 7,306 of 8,501 points equal to zero. Raman "RAW" is background-subtracted by an undocumented method (11 of 11 pairs). 11 file pairs hold identical data under two mineral names. opXRD slice (2,680 patterns): 501 unlabelled; multi-phase is 485 (18.1%) after removing 625 placeholder slots (the registered guess of 41.4% is [REFUTED]); only 41 patterns give all phase fractions; 124 exact duplicates in 61 groups; all 499 patterns from one contributor (HKUST-B) have intensity values identical to RRUFF RAW files, and 414 of those are calculated but flagged as not simulated. Usable pool (measured, raw-like, labelled): 1,683 of 7,183 files (1,600 after de-duplication). Only 353 state a real X-ray wavelength, 352 from one institution. Corpus conclusion: these archives cannot seed a known-answer XRD benchmark.
  - *Later check (C16, candidate c1) that narrows this.* The 499 of 499 match was re-hashed independently and holds. It is the new part: the match is not disclosed anywhere, and the same group re-published 261 of those files elsewhere as "experimental". Eight papers use between 148 and 3,002 RRUFF "experimental" files and give no id lists [SOURCE, single-agent]. But three earlier framings are weakened. (1) "15 duplicate groups with conflicting labels" is [REFUTED as worded]: in 9 of 20 hand-checked groups the "conflict" was two phases of one multi-phase sample. Say "same pattern, different label text". (2) The 501 unlabelled patterns include the 499 copied files, so that is one problem, not two. (3) RRUFF's calculated status is declared in its own headers, and a March 2026 Argonne paper (AlphaDiffract) also notes it, so it is "not news" on its own. A smoothness-only flag is unsafe: of 29 label conflicts only 3 look calculated. The user's own project filter searches for "calculat" and misses "computed"; the impact there is small (0 HKUST-B rows, 8 of 200 RRUFF rows suspect, 8 duplicate pairs, all inside one opXRD subset).
- **Slices.** C01-2, C03-3, C08, N00, R01, C15, C16.
- **Others addressing.** Partly. RRUFF's own headers declare calculated profiles. AlphaDiffract notes it [SOURCE, single-agent]. Since 2025-10-02 RRUFF writes the Raman wavelength into headers (default "unknown") [SOURCE].
- **Build.** A 499-row match table plus a tiny checker (C16 c1; C15 XRD idea B calls the wider version a "usable files index"). Input: a list of file ids. Output: how many are calculated or duplicated. Key each row on RRUFF id plus content hash plus snapshot date, add a basis-of-evidence column, and use neutral wording. Also: file-only lint and a 13-field header proposal for RRUFF (N00 B8). Sending errata upstream waits for the user's approval. Risk: the manifest sits in a temporary folder that can vanish.

### G7. "Negative" labels include materials that were never made
- **Gap.** In superconductor datasets, "does not superconduct" (coded Tc = 0) mixes three cases: never made, made but not measured cold enough, and properly tested.
- **Why ML cares.** It is absence of evidence stored as evidence of absence. A classifier learns that "hard to make" means "not a superconductor".
- **Evidence.** [OWN-EXPERIMENT, pre-registered] In the Hosono screening table, 332 of 671 extracted entries (49.5%, CI 45.7 to 53.3%) were never made. (The paper says about 700; extraction got 671; not reconciled.) The made / not-made mark exists only as cell background colour, so a text extraction keeps 0 of 671 marks. 0 of 671 negatives record the lowest temperature reached, the method or the pressure. [REFUTED] "The negatives were merged at the source": the loss happens downstream. [SOURCE] Stanev 2018 added about 300 Hosono materials as Tc = 0; 3DSC has 3,854 entries coded Tc = 0. 384 compounds can be matched by formula, but that match was NOT run (blocked on a download). The prediction that at least 10% of matched entries were never made is untested. Anecdote [SOURCE]: La3Ni2O7 was marked never-made, then later reported superconducting near 80 K under pressure.
- **Slices.** C06-2, C04, R03.
- **Others addressing.** Partly. SuperCon has a field for the measurement floor [SOURCE]. No public store of raw resistance-vs-temperature files exists.
- **Build.** Three-way negative labelling of the matched set (Track A7, low priority). Idea: re-extract bounded negatives from raw instrument files.

### G8. Computed numbers presented as if measured
- **Gap.** Some files and pipelines do not say whether a value was measured, calculated from other columns, or predicted by a model.
- **Why ML cares.** You cannot weight, filter or split by label origin if the origin is not recorded.
- **Evidence.** [OWN-EXPERIMENT] ESTM (a TE table, 5,205 rows): power factor in 3,853 cells and zT in 3,310 cells are Excel formulas, not reported values, with no flag; the file has no licence. Matbench metadata never says its formation energy comes from DFT. In the Discovered Materials export, the harness calls computed values "measured"; provenance is 504 by ML force field, 22 "verified" by ML force field, 0 by DFT. [SOURCE] Thermal conductivity was fabricated in 15 submissions.
- **Slices.** C03-2, C01, C05, C07, R05, R06, N00.
- **Others addressing.** No.
- **Build.** Formula-cell detector inside the TE validator (unwritten, 1 to 2 days). A `value_origin` field in the TE specimen schema (draft).

### G9. The best open synthesis-plus-XRD releases carry record errors of their own
- **Gap.** Even the most complete open lab dataset has a few wrong units and impossible values, and one person's id on every verification.
- **Why ML cares.** These are the only open records that pair a recipe with an XRD outcome, so their errors flow straight into any synthesis model. The error rate is small, though. It shrank each time it was re-checked.
- **Evidence.** [OWN-EXPERIMENT] The PG release (Precursor Genome, an autonomous-lab dataset, 1,035 samples, 1,351 scans). The headline number moved three times. First "28% carry an error" (292 of 1,035) [REFUTED]. Then a strict wrong-value rate of 93 of 1,035 (9.0%). LATEST (C16, candidate c2): about 30 of 1,035 (about 3%) hold a truly wrong stored value. Only five items are certain: a stale copy of the target in 9 samples (the 7 lead-containing samples with a mismatched element list fold into this); 19 negative XRD specimen masses; 2 negative recovered masses; `weight_percent` holds fractions where the schema's own comment shows 45.2; hydrate formulas differ between `formula` and `formula_clean`. Four earlier errata items are RETRACTED: "verification method reads manual" (that is the schema default, not a claim); "20 scan files have no ledger entry" (18 are leftovers of dropped precursors); an SiO2 space-group count that did not reproduce; and "not a furnace effect" (see G27). One fact stays, as a fact and not an error: one editor id is on all 1,216 verification blocks, so the labels are single-rater. Two paper-versus-file contradictions were found: the paper says a 1-hour hold where the file has 231 samples at 4 hours, and the paper says doses are within 0.2% where about a third miss that. Only 338 samples are fully checkable. A companion README (Dara) says "equal weight" while mixtures are actually 10 to 90 wt%. A second dataset's scan dates do not match its paper's campaign dates.
- **Slices.** C04-1, C04-2, C03-3, R10, N00, C16.
- **Others addressing.** No.
- **Build.** A polite 2-to-5-item note to the dataset owners with a reproducer script, plus the user's own sidecar corrections file (the CC BY 4.0 licence permits it). Needs the user's yes. Caution from C16: the PG paper is still under review, so a public issue would be seen by its reviewers. Also a plausibility lint for fit results.

---

## Theme 2. Identity and joins: you cannot tell which thing a row is about

### G10. Databases share no ids, so the same material cannot be linked across them
- **Gap.** There is no common key between the big computed database, the benchmark sets and the experimental databases.
- **Why ML cares.** You cannot join computed features to measured labels, find duplicates, or check one source against another.
- **Evidence.** [OWN-EXPERIMENT] One RRUFF quartz record has 0 mentions of an MP or ICSD id in its 37 files. Quartz is filed under space group #152 in MP and #154 in COD and RRUFF (these are mirror images, see G14). The key "formula + space group" is non-unique for 10,181 of 180,107 keys (5.65%). A composition maps to exactly one MP entry for 58.4% / 56.3% of Matbench rows but only 8.55% of Starrydata experiments; 73.1% of Starrydata samples have no MP candidate. GNoME has 0 MP ids in its main tables, though companion files hold about 41k that all resolve; 45,064 of 54,485 external rows have no source id. One polymer lot appears with three molar masses (15000 / 12273 / 10131) and no shared sample id. SciGlass has 1,604 "identical" silica rows with density 2.02 to 2.60.
- **Slices.** C01-1, C01-2, C01-3, C02, C03-2, C08, R01, R03, R04, R08.
- **Others addressing.** Partly. OPTIMADE gives a common query format, and IGSN gives sample ids [SOURCE]. Neither is used by these datasets.
- **Build.** Cross-database id table "xwalk" (N00 B9, parked; a 70-row prototype exists). Merged-table checklist (done, as a checklist only).

### G11. Benchmark rows drop their source id and version
- **Gap.** Matbench rows do not record which MP entry or MP release they came from.
- **Why ML cares.** You cannot tell label drift from label error, or trace a test row to its source.
- **Evidence.** [OWN-EXPERIMENT] The 132,752-row formation-energy task has no MP id anywhere in 823,693,845 bytes of files. Ids are recoverable for 279 of 300 sampled rows (295 with a tie-break). Labels within 0.01 eV/atom of current MP values: 83 of 279 in the first pass, then 80 of 278 in the later round 3 (use the later). This was reframed as "computed values drift between MP releases", not error. Full recovery attempt: 110,532 rows map to a single id, 19,835 to several, 2,385 to none; 1,818 single rows share 820 ids, and 184 groups spread by more than 0.1 eV/atom. [REFUTED] "The Matbench quartz label matches no MP value": it equals the 2011 calculation; the difference to the current mixed value is 0.0013 eV/atom. Reports R01, R03, R04, R08 and session C08 still carry the old claim.
- **Slices.** C01-2, C01-3, C08, N00, R01, R03, R04, R08.
- **Others addressing.** No.
- **Build.** Matbench provenance sidecar (N00 B4; MP side parked by the user's "experimental first" decision).

### G12. The chemical formula is not the specimen
- **Gap.** Two samples with the same formula can have very different properties, because processing and microstructure matter, yet most ML tasks use the formula as the only input.
- **Why ML cares.** It sets a hard floor on error. The target is not a function of the input you have.
- **Evidence.** [OWN-EXPERIMENT] In Starrydata, 647 compositions appear in two or more papers (21,856 pairs). The median between-paper difference in Seebeck coefficient is 32.7%; only 35.6% of pairs agree within 20%; the sign is opposite in 3,881 pairs (17.8%). Within one paper (5,161 pairs) the median is 12.9%. For Bi2Te3 (111 papers), paper medians run from −241 to +280 µV/K. Resistivity: median 0.35 decades between papers, 0.14 within. An "answers-known" lookup has a 15.0% error floor. Looking up the same composition gives 22.9% error and beats a nearest-neighbour model at 29.4% (3,593 samples). [SOURCE] For comparison, a round robin on one specimen gives spreads of S 6%, ρ 8%, κ 11%, zT 19% (Alleno 2015). So most of the 32.7% is real specimen difference, not instrument noise.
- **Slices.** C03-1, C03-2, C01, N00, R07.
- **Others addressing.** No dataset in the corpus fixes it. The atlas lists what identity needs per material class: crystal adds structure and handedness; glass adds thermal history; metal adds processing and microstructure; polymer adds chain distribution; composite adds architecture and cure; thin film adds substrate, thickness and deposition [OPINION].
- **Build.** TE specimen layer "te-layer" (N00 B7, blocked on descriptor quality, see G13). Specimen schema core v1 (25 entities, 31 requirements, 12 null codes; still 37 weak mappings and 27 structural issues).

### G13. The specimen details that would explain the spread are mostly not recorded
- **Gap.** Fields such as processing route, density, grain size and measurement method are empty for most records, and some needed fields exist in no source at all.
- **Why ML cares.** You cannot add the missing features after the fact. Text clean-up does not recover them.
- **Evidence.** [OWN-EXPERIMENT] Fill rates over all 55,422 Starrydata samples: form 41.0%, fabrication process 29.1%, electrical measurement method 24.8%, thermal method 17.0%, purity 8.5%, relative density 4.4%, grain size 1.7%, measurement direction 12 samples. 7 of 28 proposed specimen fields exist in no TE source: parent batch id, measured composition, processing parameters, density used for κ, value origin, uncertainty, measuring lab. [REFUTED] "Cleaning the free-text descriptors recovers the context": coverage reached 43.0% against a 50% bar (ceiling 47.1%; audit precision 0.875 against 0.90). 0 of 3,361 specimens meet a closed-field completeness proxy. (The development set was later recounted as 2,839 specimens / 870 DOIs; use the later figure.)
- **Slices.** C03-1, C03-2, N00, R07.
- **Others addressing.** No.
- **Build.** TE label-production kit for labs to record these at the source (N00 B12; needs at least 3 pilot labs). TE family layer draft (9 groups, 28 fields).

### G14. XRD phase labels point to paywalled ids, and the rule for marking an answer right is unwritten
- **Gap.** Open XRD datasets name their phases with ids from licensed databases, and the community has no written, runnable rule for when two phase answers count as "the same phase".
- **Why ML cares.** You cannot score a phase-identification model reproducibly. The choice of marking rule moves the score more than the gap between tools does. It is like an image benchmark where nobody agreed whether "husky" counts for "dog".
- **Headline evidence (latest, C16 recount).** [OWN-EXPERIMENT, from the user's own separate abstention project, read-only] The same program (a local install of Dara, an open phase-identification tool) on the same 40 weighed-mixture scans scores 12 of 40 under a strict rule (formulas must be equal), 17 of 40 under a lenient rule using stored labels, and 32 of 40 under the lenient rule after the matching was corrected. The Dara paper reports 38 of 40, but that run used the paid ICSD reference library, so the 32-versus-38 difference also reflects the library. Across all 210 error-free pilot rows, 63 are marked correct by the lenient rule and only 45 of those by the strict rule, so 18 of 63 (28.6%) credited answers depend on the rule. In that project's pilot, accuracy moved from 0.545 to 0.745 after one rule about hydrogen was added; at n = 55, lenient is 0.745 and strict is 0.309. The misses are naming artifacts: "LaO3" for La(OH)3 (hydrogen atoms were never located in the reference file), "Ni1.875O2" for NiO, "V4O9.93316" for V2O5. Neither rule is right: on 18 tricky pairs the strict rule gets 8 wrong and the lenient rule gets 13 wrong. The lenient rule merges genuinely different compounds: Nb2O5 with Nb12O29 (distance 0.0139), WO3 with W18O49 (0.0373), TiO2 with Ti9O17 (0.0256), Ca3SiO5 with Ca2SiO4, YFeO3 with Y3Fe5O12, and a hydroxide with a peroxide. A "same space group" rule would itself be wrong in at least 3 cases (for example Y2O3 #199 vs #206). 15 of 56 rows in one results file carry stale lenient labels (64 stored vs 79 recomputed, out of 260). About 250 of 590 checkable scans offer two or more crystal forms of the same formula, but 0 wrong marks from crystal form are proven so far. The project's grader compares formulas only and throws away which reference file the tool chose.
- **Earlier evidence (C04, R10, still valid).** [OWN-EXPERIMENT] 745 of 755 PG labels carry only ICSD ids (ICSD is a licensed structure database). A second set has 334 of 687 ICSD ids and 353 custom ones. Open ids (COD, MP) appear nowhere. Formula spelling alone flips 3 of 20 verdicts (BiVO4 vs VBiO4). Scoring by composition only credits a wrong Y2O3 polymorph (same formula, different structure). Duplicate phase entries were still marked correct in 4 of 4 and 2 of 3 cases. Exact-string scoring gives tool A 17 and tool B 4 correct; composition scoring gives 18 and 7. The standard structure-comparison function (pymatgen StructureMatcher) with default settings merges alpha and beta quartz (they separate only at a tighter tolerance; their main peaks sit at 26.67 vs 26.21 degrees), splits identical files over oxidation-state labels, and rescales volume so a cell 6.3% too large still "matches". [REFUTED] "It wrongly matches mirror-image crystals (36 of 36)": that is correct behaviour for powder XRD, which cannot see handedness. Exposure: 17 mirror-pair labels in 91 of 1,035 PG samples; one sample uses both hands in one fit; 49 mirror-copy pairs sit as separate Matbench rows. [REFUTED] "Formulas filed under both hands are polymorphs": 74% are mirror copies. [REFUTED] a "10× error" flag for mirror copies (ratio as low as 2.58; misses 8 of 61).
- **Slices.** C02-1, C02-2, C04-1, C04-2, C01-3, R03, R10, N00, C15, C16.
- **Others addressing.** The ideas are old; a runnable tool is missing. [SOURCE, single-agent] A 1990 IUCr paper defines levels of structure similarity. A 2002 search-match round robin used lenient human grading. RADAR-PD uses a GPT-4 judge. Experts publicly dispute whether an ordered and a disordered version of a crystal count as the same (Leeman vs A-Lab, see G42). No installable grader or rule card was found.
- **Build.** The "fair marking kit" (C16 candidate c3; C15 XRD idea C; XRD page B3; Track A6). This is the XRD session's tentative top recommendation. First step: publish a CSV of about 25 tricky pairs with the verdict of each of five markers: strict formula, lenient formula, StructureMatcher at default settings, StructureMatcher at a looser tolerance (stol 0.15), and the proposed tier. It should return a tier, not a yes/no. It needs sign-off from one practising diffraction specialist. Present it as the "first executable, tested card", not as a new taxonomy. It needs no lab, no permission and no download to start, and it fits that project's pre-registered fallback ("shrink to the evaluation harness"). For the wider id crosswalk, the blocker is that redistribution terms for ICSD and ICDD codes are unchecked.

### G15. Joining two datasets about the same papers silently loses or mismatches rows
- **Gap.** Even when two TE tables cover the same papers, DOI strings differ and composition matching is ambiguous.
- **Why ML cares.** Wrong joins create wrong labels and hidden duplicates across train and test.
- **Evidence.** [OWN-EXPERIMENT] Shared papers across three TE sources: 193 / 75 / 7 after DOI normalisation, versus 183 / 26 / 4 with raw strings. So naive matching found 26 of 75 shared papers in one pair. Joining ESTM to Starrydata by composition gives a unique match for 1,029 of 1,728 rows (59.5%, CI 48.4 to 69.8%) at tolerance 0.005, 34.0% at 0.02 and 74.9% at 0.001; the verdict was downgraded from validated to mixed. The figure label is the reliable key: the matched sample is the closest in its paper 91 to 94% of the time. ESTM has no sample key, and 49 (formula, temperature) pairs repeat. A first double-digitisation pass is [REFUTED] because it mixed in composition-only matches (max gap 32%); the clean pass has 100 label-matched pairs, median peak-zT gap 0.45%, 98 of 100 within 2%, largest 15.0%. Round 4 (later, per property): S 0.48%, ρ 0.83%, κ 0.57%, zT 0.91% over 361 comparisons.
- **Slices.** C03-1, C03-2, C03-3, N00, R07, C15.
- **Others addressing.** No.
- **Build.** DOI normaliser inside the split generator (N00 B2).

---

## Theme 3. Evaluation you cannot trust

### G16. Random train/test splits leak, and they make models look about twice as good
- **Gap.** A random split puts samples from the same paper, furnace run or near-identical composition on both sides.
- **Why ML cares.** Reported accuracy measures memorising a paper, not predicting a new material.
- **Evidence.** [OWN-EXPERIMENT] TE: under a random split, 93.5% of test papers are also in training. Median Seebeck error for a 5-nearest-neighbour baseline goes 25.5% (random) to 42.2% (split by paper) to 46.6% (split by chemical system), n = 12,222 samples from 3,015 papers. Share within 20%: 43.4% to 31.1% to 28.6%. (A chat line saying "21% vs 42%" mixed two baselines; ignore it.) Synthesis: holding out a whole precursor drops outcome macro-F1 from 0.526 to 0.415 (rerun 0.488 to 0.394); grouping by chemical system barely matters. The right grouping unit differs by dataset: paper for TE, precursor plus furnace run for synthesis, duplicate group for XRD. [SOURCE] One transfer-learning paper's random splits share structures between its DFT training set and its experimental test set.
- **Slices.** C03-1, C03-2, C03-3, N00, R07, R08, C15.
- **Others addressing.** Partly. GroupKFold and MatFold exist as tools [SOURCE]. No TE task uses them.
- **Build.** Split generator "splitgen" (N00 B2; C15 calls it a "fair-exam generator"; started, about 1 to 2 weeks).

### G17. There is no blind test, and one is hard to build from public data
- **Gap.** Materials ML has no hidden-answer test like CASP in protein folding. Any test built from published figures or open datasets already has its answers in the wild.
- **Why ML cares.** Without a sequestered test, leaderboards can be overfit and web-connected agents can look answers up.
- **Evidence.** [OWN-EXPERIMENT, negative search, "not proven absent"] No blind TE test was found; Matbench has no TE task; the JARVIS leaderboard has no experimental TE task. Every Starrydata value is a published figure. Hidden splits cannot be built from the public XRD sets: the answers are public and a CC BY licence cannot carry "evaluation only" terms. [SOURCE] The one blind test in the field (CCDC's) covers molecular crystals only and had a leak incident. The sessions flip-flopped on XRDBench (an LLM-oriented XRD benchmark): R03 said its answers are published; a reviewer correction in C04 / R10 said they are "retained by the evaluator"; C15 and C16 then found the answers sitting in public JSON in the repository, with no licence and no scoring server (30% of its score comes from an LLM judge). The LATEST word (Version 4 of the XRD page, 23:51Z) is that the answers are PUBLIC, so its 134 cases cannot serve as a hidden test. The R10 sentence is superseded. [SOURCE, single-agent, C16] Codabench is a free host that keeps answers hidden; it has a 20-minute default compute cap, so entrants should upload answers, not code. [OPINION] PDB plus CASP is a better model than ImageNet: a stable protocol mattered more than clean labels (ImageNet has about 6% label error; a re-test dropped accuracy 11 to 14% while rankings held [SOURCE]).
- **Slices.** C02, C03-1, C04, C15, C16, R02, R03, R04, R07, R10.
- **Others addressing.** Partly. XRDBench (100 question tasks, 34 end-to-end tasks) [SOURCE], but its answers are public. The Reynolds Cup is a blind weighed-mineral contest for human analysts (see G20). See G34 for the institutional side.
- **Build.** TE blind round (TE spec, R07; specified; lacks 17 rules, has 22 major and 15 minor open review issues, no pilot lab, no cost estimate). XRD blind challenge (Track A4 / XRD page B7; about 770 items for ±5 points, about 1,570 for 80% power; "extend XRDBench"). Scoring harness (N00 B5) and baselines (N00 B6).

### G18. Nobody knows the noise floor of the labels
- **Gap.** For most measured properties there is no agreed between-lab error, and literature labels come from one paper each.
- **Why ML cares.** Without a noise floor you cannot tell whether a model is at the limit or whether a gain is real.
- **Evidence.** [OWN-EXPERIMENT] The digitisation floor for Seebeck near 300 K is 0.55% (95th percentile 11.1%), against a 42.2% model baseline. It is a lower bound only. [SOURCE] TE round robins on one specimen: S 6%, ρ 8%, κ 11%, zT 19%; a second study gives 2σ of 5.7 to 7.9% for S and 11.5 to 16.4% for zT; two probe geometries differ by 11.3 to 13.6% in Seebeck. Certified reference samples exist for Seebeck (SRM 3451 / 3452) and for thermal diffusivity and conductivity (BCR-724, to 1025 K), but none for resistivity. Other fields: 6 of 13 CO2 adsorption datasets fall outside the NIST consensus; glass-transition temperature differs about 3 to 4 °C between labs; no certified PLA molar-mass reference. [REFUTED] "No certified κ reference exists." [REFUTED] "SD of at least 20% across 11 labs" was the authors' expectation, not a result. [REFUTED] "Round robins took 4 to 12 months": 4 months to about 2 years. The computed counterpart is weak: R² 0.79 for S and 0.33 for power factor (Ricci 2017).
- **Slices.** C03-1, C03-2, C03-3, N00, R07, R02.
- **Others addressing.** Partly, per property, by the round-robin authors and NIST [SOURCE].
- **Build.** Scoring harness using z′ scores, which scale error by the expected between-lab spread (N00 B5). TE label-production kit (N00 B12).

### G19. Multiphase XRD has no ground truth, no multi-rater labels and too few hard cases
- **Gap.** For real samples with four or more phases, the "label" is one person's or one program's fit, and open data has too few such patterns to test on.
- **Why ML cares.** This is the perception step of every autonomous lab. With one unverified annotator you cannot measure accuracy at all.
- **Evidence.** [OWN-EXPERIMENT] Hard patterns (at least 4 phases at 1 wt% or more; the plan's own cutoff): 157 of 1,035 in PG plus 10 of 352 in a second set, total 167, against a pre-set bar of 270. The hypothesis FAILED. Human and automated fits of the same scan disagree in 316 of 343 cases (92.1%); the human adds phases in 227, adds and removes in 84, removes in 5. One editor id is on all verifications, so this is one person against one machine, with selection bias. On 20 reaction products: expert 16 of 20, tool A 15, tool B 7; tool A found four different three-phase answers with near-identical fit. [SOURCE] Periodic Labs reports expert-expert agreement of 77.2% with 3 experts per pattern (self-reported, nothing released). 2002 search-match round robin: 1 of 25 participants found all 10 phases. [REFUTED] "Nobody keeps every rater's labels": a NIST dataset (mds2-2301) does; the real gap is per-phase multi-rater labels on hard multiphase patterns. [REFUTED] "Open paired records are about 10^3": that is a lower bound, not a census. [REFUTED] "About 270 patterns gives ±5 points": only at accuracy near 0.77; it is ±6.0 at 0.5.
  - *Later check (C16, candidate c5) that WEAKENS the "use human-vs-machine disagreements as a test set" idea.* The 316 of 343 PG disagreement set has no headroom as a test: a random guesser scores 20.1% and a perfect method only 21.8%. A fuller PG table has 1,151 scans (354 positives), and there the trivial rule "the program named one phase" already scores about 50%. In the second set (A-Lab GPSS, 352 samples, where the "automated" answer is Dara itself), the 124 of 352 figure counts only scans where the number of phases differs; comparing the phase lists gives about 150; and 137 of 352 "human" files are the program's fit left unchanged. [SOURCE, single-agent] A published trust-score tool on top of Dara (AIF, LBNL, Advanced Science 2026, data at Zenodo 21141588) reports that the PG annotator reversed 83.3% of re-reviewed cases, that chemists agree pairwise only 35 to 70% of the time, and that its trust decisions matched experts in 77.6% of cases. So "nobody has measured interpretation error" is [REFUTED] in the narrow sense: it has been measured judgment-against-judgment. It has never been measured judgment-against-measurement (see G21). [OPINION, C11] Periodic's 77.2% expert agreement works out to a chance-corrected agreement (Cohen's kappa) of about 0.54. Sizing [C16]: 270 items give ±5 points only if accuracy is about 78% or higher; near 50% accuracy about 385 separate powders are needed; separating two tools 5 points apart needs about 470 to 780 paired powders.
- **Slices.** C02-1, C02-2, C04-1, C04-2, C06, C11, R03, R04, R10, N00, C15, C16.
- **Others addressing.** Partly: NIST/IMMI, RADAR-PD (291 RRUFF samples), OPENXRD (non-commercial licence), and AIF above (Dartsi et al., Jain group; the same Zenodo record; earlier sessions cite it for "preferred over the best-fit answer in 93% of clear-preference cases", CI 78 to 98, n = 30, and accept/reject matching experts about 75 to 80%) [SOURCE].
- **Build.** Multi-rater pilot on the 167 hard patterns (N00 B11 / Track A1 / XRD page B4; at least 3 raters, about 10^3 expert-hours, development split only; desk go/no-go first). The C16 pass puts both "expert relabelling" and "the human-overrule test set" on its skip list: the human-check set is already milestone M3 of the user's own abstention project and overlaps AIF. Do not re-host the GPSS reference files, which derive from ICSD.

### G20. The known-answer XRD sets that do exist are small and too easy
- **Gap.** Mixtures weighed out from known powders give true labels, but open sets have few samples and few phases each.
- **Why ML cares.** An easy test cannot separate tools. Everyone scores near the ceiling.
- **Evidence.** [OWN-EXPERIMENT] On 20 weighed mixtures with 3 phases or fewer: tool A 38 of 40 (CI 87.5 to 100), tool B 35 of 40 (77.5 to 95.0); paired difference 7.5 points, CI 0 to 15. INCONCLUSIVE. Errors cluster in 2-minute scans. Weight-fraction error 4.81 vs 5.49. No open set has a weighed mixture with 4 or more phases in the three datasets checked. [REFUTED] "Weighed truth stops at 3 phases": an IUCr round-robin sample has 4 phases, a NIST reference has at least 5, and a 2002 round robin used a seven-phase bauxite [SOURCE].
  - *Set size, three ways.* The Dara benchmark is 20 mixtures, each scanned for 2 and for 8 minutes, so 40 mixture scans, plus 10 single-ingredient scans (C16, latest). C15 says "60 patterns"; the notes file mentions 61 and 70 files. Use 40 + 10. 8 of the 10 singles sit on a shifted measurement grid with longer counting.
  - *Harder public sets exist (C16, [SOURCE, single-agent]).* The IUCr quantitative-analysis round robin (Madsen 2001, Scarlett 2002): 4- and 7-ingredient weighed mixtures, minor phases at 1 to 5 wt%, raw scans and answers public. Szymanski 2023: 240 weighed two-phase mixtures, minor phase 2 to 20 wt%, CC BY 4.0. Leon-Reina 2016: spiked series at 0.12 to 4.0 wt%, CC BY 4.0. The Reynolds Cup: a blind weighed-mineral contest every two years, with physical powders ($250 per unit for past ones) and human analysts. Doebelin 2020: numerical mixing of real scans, built into the Profex program, unstable at 1 wt% or less. So the novelty is narrow: a *standing, machine-scored, hidden-recipe* test on hundreds of measured mixtures with 4 or more ingredients.
  - *Can you fake mixtures by adding single scans? (C16, [OWN-EXPERIMENT])* A plain weight-proportional sum misjudges the recipe by about 15 percentage points (worst 49). Weighting by X-ray absorption brings that to about 5. Absorption varies from 8.4 (Li2CO3) to 261.0 (La(OH)3) cm²/g. Summed scans still differ from real ones by about 4 times the counting noise. Hygiene problem: the public file names spell out the recipes.
- **Slices.** C04-1, C04-2, R10, C15, C16, C02-2.
- **Others addressing.** Partly (the sets above). None is a hidden, machine-scored test.
- **Build.** Harder weighed mixtures: at least 4 phases, minor phases under 10 wt%, 2-minute scans (Track A2 / XRD page B6 / C16 candidate c4; needs a partner lab; C16 sizes it at about 385 or more powders). C15 calls the hidden version of this "the actual ImageNet-style seed" (XRD idea D). Desk first step: the "replay test". Rebuild the 40 mixtures as absorption-weighted sums, freeze the scorer first, and compare with stored outcomes (about 25 minutes of compute plus about a day of coding). Before that, run Dara on the public harder scans (needs download approval). Caveat: the local Dara install (version 1.1.12, open reference pools capped at 80 candidates) is not the published set-up.

### G21. LLM judges are checked against other judgments, never against a measurement
- **Gap.** When a model grades XRD answers, its quality is reported as agreement with experts, not as accuracy against an independent physical check.
- **Why ML cares.** Agreement between two fallible raters is not accuracy. If the same judge family gives the training reward, picks the best sample and scores the test, errors compound.
- **Evidence.** [SOURCE, self-reported by Periodic Labs] Judge-expert agreement 74.6% (±1.5 points) vs expert-expert 77.2%; judge vs an undefined "consensus" 84%. No judgment-versus-measurement number is given. Nothing was released. The judges are also contestants. "Thousands of calibration patterns" and "PhD annotators" are UNVERIFIED (C11). [OPINION] Reward, best-of-n selection and evaluation all run through one judge family. [SOURCE] What lab XRD cannot see at all: amorphous content, minor phases below about 1 to 5 wt%, light atoms, phases missing from the databases, sample swaps. Other instruments (electron microscopy, neutron diffraction, thermal analysis, Raman) can contradict an XRD reading.
- **Slices.** C04, C06-1, C06-2, C11, R03, R04.
- **Others addressing.** No.
- **Build.** Judge-calibration kit (Track A5 / XRD page B5). Measurement-checked XRD set from one outside lab (C06 pilot: about 150 attempts, at least 40 retained specimens, about 12 weeks, about 200 hours, compute about $1,850; continue if at least 3 of 30 claims are contradicted; specified, not started). Decision recorded: a small outside set can estimate error rates; it cannot rank models.

### G22. Headline results rest on small test sets with no error bars
- **Gap.** Published comparisons use tens to a few hundred test items, report no intervals, and change several things at once.
- **Why ML cares.** Many claimed wins are statistical ties.
- **Evidence.** [SOURCE plus own arithmetic] Periodic's FrontierXRD test has n = 134: 55.3% vs a base model at 2.7% (the base appears as 2.7, about 3, 4.5 to 4.6 and 2.9 in different places). The standard error is about 4.3 points. The 55.3% is best-of-7 with a learned selector; a single attempt scores about 36%. Scores are not whole counts (55.3% of 134 is 74.1). On the held-out set (n = 198) two models score 76.6 vs 73.7 (C06), 76.5 vs 73.5 (C11, read by eye) or about 77 vs 74 (C04, R04); z is 0.4 to 0.77, a tie. The general model's top score reads 53.2 (C06), about 53.5 (C11), about 53% (R04). Putting a general model inside Periodic's tool harness moved it from 8.33% to 31.53% (C04, C06, R03, R04) or 31.63% (C11), at $5.41 vs $4.56 per attempt; four things changed at once, so it is not an ablation. The split excludes larger chemical systems but allows sub-systems, with no cross-lab or cross-instrument split. [OWN-EXPERIMENT] The user's own re-scan finding is also confounded (see G25).
- **Slices.** C04, C06, C11, R03, R04.
- **Others addressing.** No.
- **Build.** Implied by C11: an open evaluation like FrontierXRD with error bars, and a stronger open-tool baseline. Not specified further.

### G23. The fit residual is a hackable reward, and tools give one answer with no confidence
- **Gap.** XRD software scores a fit by how well the curve matches, but adding a spurious phase always improves the match.
- **Why ML cares.** It is a textbook reward-hacking setup. There is also no cheap verifier and no calibrated output to abstain on.
- **Evidence.** [OWN-EXPERIMENT] In samples that contain no carbon, fits report Ag2CO3 at 23 to 25 wt%, Li2CO3 at 13 wt%, and impossible phases (Y4C7 at 31 wt%, graphite at 66 wt%). Across 921 fits of carbon-free samples, carbonates appear 81 times (68 in human fits); the other 13 carbon phases all come from automated fits. A check for "elements outside precursors plus air" flags 0 of 3,240 phases while a control flags 1,642, so the fits never even consider contamination. [SOURCE] Train-on-simulated classifiers score about 93% on a fixed candidate list but fail on open multiphase patterns. An autonomous lab's automated XRD was called its weak link (Leeman 2024). [OPINION] Most systems output a single answer with no calibration. [REFUTED] "Distil the simulator to speed it up": simulation is already closed-form, about 0.3 ms per pattern.
- **Slices.** C02, C04-2, R03, R10, C11.
- **Others addressing.** Partly. The user's own separate project adds a calibrated abstention layer (known only from notes; not opened here).
- **Build.** Plausibility lint; "ladder of rewards" idea (cheap checks first, physical checks last); Round-5 experiment (1). No results yet.

### G24. ML-method papers in the field are often too weak to compare
- **Gap.** New-architecture papers tend to be single-seed, single-author and tested on sets too small to detect the gains they claim.
- **Why ML cares.** You cannot read the literature as a leaderboard.
- **Evidence.** [SOURCE, literature survey of 110 papers and 56 datasets] Recursive or looped models in materials: none clearly beats the conventional best (steels MAE 91.20 ± 12.23 vs 87.76; another 0.0986 vs 0.0945). One headline was [REFUTED]. A second verification pass softened about half the headline claims, and 13 numbers in the first answer were wrong. Ten searches came back empty (for example no early-exit in graph force fields, no data-repetition study for force fields, few quality-vs-budget curves for crystal generators). Dataset sizes conflict at the source: Alexandria 30.5M (C09) vs 5,777,914 PBE entries (C10, R09); OMat24 about 101M vs about 118M; MPtrj "1.3M" vs 1,580,395. Label hygiene: QM9 has 3,054 of 133,885 failing a geometry check; QM7-X about 4.6% duplicates. [OWN-EXPERIMENT arithmetic] With about 270 test compounds the minimum detectable gain is about 0.08 eV, while the predicted gain from 10× more DFT data is 0.009 to 0.040 eV.
- **Slices.** C10-1, C10-2, C10-3, R09, C08, R08.
- **Others addressing.** No.
- **Build.** None chosen. Seven survey directions were listed; the user never replied, and they were never linked to the main agenda.

---

## Theme 4. Context that was never recorded

### G25. Nobody records what happened to a sample between making and measuring
- **Gap.** Humidity, air exposure, storage and elapsed time are not recorded, although samples change.
- **Why ML cares.** The label (which phases are present) depends on a hidden variable, time and exposure, that is in no feature.
- **Evidence.** [OWN-EXPERIMENT] PG has 115 metadata key paths and none for humidity, atmosphere, storage or exposure; 13 handling words get 0 hits. Operator and comment fields are empty in 1,417 of 1,417 scan files; a second set's headers are empty in 352 of 352. Absolute synthesis time is recorded for 0 of 1,035 samples. Exploratory re-scan result: the phase set changed in 154 of 184 samples re-scanned after more than 180 days vs 9 of 14 at 1 to 30 days (all fits). For same-method fits only it is 105 of 136 (77%) vs 12 of 25 (48%); R10 publishes this one. Both are confounded. In 115 of 184 cases the official outcome comes from the earlier scan. [SOURCE] The powder-diffraction file standard (pdCIF) has no humidity or atmosphere field. [REFUTED] "No schema has an atmosphere field": NeXus and NOMAD record atmosphere as a category; humidity, exposure, storage and time-to-measurement are still missing.
- **Slices.** C04-1, C04-2, R10, N00.
- **Others addressing.** Partly (NeXus, NOMAD).
- **Build.** Handling-history schema proposal (Track A3 / XRD page B2; target a NeXus committee meeting 25 to 27 Sep 2026; acceptance test is the 184-sample re-scan case).

### G26. Basic instrument settings are missing from measurement files
- **Gap.** Most archived XRD files do not state the X-ray wavelength, step size or instrument.
- **Why ML cares.** Peak positions depend on wavelength. Without it you cannot simulate matching training data or pool across labs.
- **Evidence.** [OWN-EXPERIMENT] Wavelength or anode is stated in 71 of 3,019 RRUFF powder files (2.4%); step size, scan time and instrument in 0 to 2 files. 29 arrays in one RRUFF record have no axis names or units. HTEM raw files return a server error (7 of 8). Raw EBSD microscopy patterns are not public (about 26 GB per scan). RRUFF has 9,858 samples, 4,349 public, no licence and no persistent ids.
- **Slices.** C01-2, C03-3, C08, N00, R01.
- **Others addressing.** Partly (RRUFF's 2025 Raman header change).
- **Build.** 13-field header proposal and file-only lint (N00 B8).

### G27. The synthesis log records what was programmed, not what happened
- **Gap.** Lab ledgers store setpoints and use undocumented pass/fail rules.
- **Why ML cares.** The model's input (the recipe) differs from the treatment the sample actually got, in a temperature-dependent way.
- **Evidence.** [OWN-EXPERIMENT] Furnace logs fall short of the programmed hold in 118 of 981 runs (12.0%): 0 of 743 at 500 °C or below vs 109 of 147 at 1000 °C or above. The count ranges 43 to 420 depending on tolerance. [REFUTED] "It is not a furnace effect": 13 of 13 vs 0 of 7 runs at 1000 °C by furnace; found after the fact, so a lead only. Powder dosing is tight (median 0.12% off). `met_target_mass` is an undocumented 100 mg threshold while the documented target is 150 mg. Hydrated chemicals are stored under their dry formulas (132 samples). Failures are logged for outcomes (369 unreacted, 113 partial, 26 physical failures), but every scan has status "valid" (1,351 of 1,351). [SOURCE] A startup founder: "same experiment done twice often gives different results due to small undocumented changes".
- **Slices.** C03-3, C04-2, C05, N00, R05.
- **Others addressing.** No.
- **Build.** Round-5 experiment (5). No results yet.

### G28. Negative results carry no detection limit
- **Gap.** "Not found" is recorded without saying how hard anyone looked.
- **Why ML cares.** A negative label without a bound cannot be compared with a positive one. This is the general form of G7.
- **Evidence.** [OWN-EXPERIMENT] 0 of 671 Hosono negatives record lowest temperature, method or pressure. [SOURCE] XRD misses minor phases below about 1 to 5 wt% and all amorphous content, so "phase not present" is also unbounded. [OPINION] Failures should be typed four ways: chemistry failed, tool failed, characterisation inconclusive, run not finished. A cracked tube or a sample mix-up cannot be recovered by software.
- **Slices.** C06-2, C05, R05, R06, C02.
- **Others addressing.** Partly (SuperCon's floor field).
- **Build.** Outcome labelling protocol (from the Discovered Materials report; specified only).

### G29. Standards are missing for common measurements and for basic data features
- **Gap.** Shared schemas lack definitions for some routine measurements and cannot express bounds or missing-value reasons.
- **Why ML cares.** Every group invents its own encoding, so pooled data needs hand cleaning each time.
- **Evidence.** [SOURCE] NeXus has no definitions for XRF quantification or the four-point resistivity probe. Frictionless and GEMD cannot represent inequalities. [OWN-EXPERIMENT] The user's atlas logged 72 gap rows; by type: undefined field 41, no join key 23, not observed 17, model limit 15, no uncertainty 14, too little variation 12; by fix: 49 need only documentation, 14 both, 9 need new data. [SOURCE] No agreed uncertainty model exists; MP's correction uncertainties cover fit error only.
- **Slices.** C01-3, C08, C09, R01, R02, R08, N00.
- **Others addressing.** Partly (the standards bodies).
- **Build.** Schema packets (N00 B8); specimen schema core v1.

---

## Theme 5. Access, ownership and incentives

### G30. Measured data is tiny next to computed data, and what exists cannot be pooled
- **Gap.** The field has millions of simulated records and only thousands of open, usable, measured ones for any one task.
- **Why ML cares.** Models are trained and scored almost entirely on simulator output. There is no large measured set to pre-train on or to test against.
- **Evidence.** [SOURCE] One large archive (NOMAD, 2023) holds more than 12 million simulations against about 50 thousand experiment or synthesis entries. Computed sets: OQMD 1,407,395 materials; OMat24 about 118 million structures; MPtrj 1,580,395 frames. Measured sets are large but not usable as one corpus: CSD more than 1.4 million crystal structures (licensed); MEAD 1.5 million samples; HTEM 141,574 thin-film entries, of which only about 10% appear in papers; Starrydata2 more than 194,000 curves read off plots. Open records that pair a synthesis recipe with a raw XRD scan number about 10^3: PG 1,035 samples / 1,351 scans; GPSS 352 samples; opXRD 92,552 patterns of which only 2,179 (or 2,680 in the slice on disk) are labelled; Dara 20 mixtures. That "about 10^3" is a lower bound, not a census (see G19). [OWN-EXPERIMENT] The usable open XRD pool is 1,683 of 7,183 files (G6). For scale, ImageNet 2009 had 3.2 million images in 5,247 categories. [OPINION, arithmetic] Reaching 1 million labels would take about 130 years at one autonomous lab's roughly 21 samples a day, about 27 years at 100 a day, and about 9 to 14 years at hundreds a day. [OPINION, reader's count] About 10 of the 56 datasets in the ML-methods survey carry experimental labels, and none is XRD or thermoelectric. Corpus verdict [OPINION]: raw volume is not the real constraint; specimen definition, deposition rules and a blind test are.
- **Slices.** C01-3, C02, C04-1, R03, R04, R09, N00.
- **Others addressing.** Partly. A 2026 effort re-measures the top 600 minerals (RSDB). A text-mining set (MatSKRAFT) extracts 535,643 values from papers at F1 71%, under a no-derivatives licence [SOURCE].
- **Build.** TE label-production kit so labs record usable data at the source (N00 B12; needs at least 3 pilot labs). "Complete by design" dataset principles (R02).

### G31. Licences and bulk-access walls block the reference data that XRD needs
- **Gap.** The best crystal-structure libraries are paid, bar ML use, or ban bulk download, and several open sets have no licence at all.
- **Why ML cares.** You cannot legally train on, redistribute, or build a public benchmark around the reference data the task depends on. Scores also change with which library you are allowed to use (32 vs 38 of 40 in G14).
- **Evidence.** [SOURCE] ICSD (335,032 entries): its API licence is tied to one named project; 2020 terms ban commercial use; 2021 terms ban building powder-pattern collections for identification. ICDD bars ML/AI derivatives. CSD typically bars AI use. One company (CuspAI) announced "exclusive AI training rights" to CSD and ICSD in July 2026. MPDS costs from EUR 9,500 a year for academics. PoLyInfo bans bulk download. The input files for the main DFT code (VASP) cannot be shared. MatSKRAFT v2 is no-derivatives; GNoME is non-commercial. RRUFF, ESTM and the composites database have no licence text. SciGlass ships a LICENSE file titled ODbL whose text is MIT (a 2022 question about it is unanswered). Open side: COD, 534,931 entries, CC0; MP, CC BY 4.0 but seeded from ICSD (the quartz entry cites 37 ICSD ids). The GPSS reference files derive from ICSD, so they should not be re-hosted. The user's own project uses COD-only reference pools because it has no ICSD licence. [OPINION] "Bulk access, not licence type, is the blocker"; ImageNet itself was non-commercial.
- **Slices.** C01-3, C02, C04, R02, R03, R04, R10, N00, C15, C16.
- **Others addressing.** Partly: COD, MP, and the OPTIMADE common query interface [SOURCE].
- **Build.** Open-id crosswalk from paid ids to COD / MP ids (Track A6 / XRD page B3). Blocker: whether ICSD and ICDD code numbers may be redistributed is unchecked.

### G32. Private labs with robots release nothing
- **Gap.** The companies and labs that now generate the most experimental data publish posts and charts, not data.
- **Why ML cares.** The scarce ingredient, task-specific supervision (hard samples, expert-rated answers, a calibrated judge, clean splits), sits behind closed doors. Outside claims about it cannot be checked.
- **Evidence.** [SOURCE, negative search] None of Periodic Labs, Lila ($550M+), Radical AI ($55M seed), CuspAI or DeepMind's UK lab has released its own lab data. Periodic runs about 100 experiments a day (1,000 a day planned) and has reported no discoveries (IEEE Spectrum, 2026-09-02). Its FrontierXRD test set is private. No repository of raw A-Lab XRD scans was found in one search (other sessions do use the A-Lab GPSS release of 352 samples and the AIF archive, so treat this as partial). Discovered Materials (DM, a chip-cooling materials startup) has released no run records; stages 6 to 9 of its traced workflow had to be filled in from literature. [REFUTED, caught by the user] "Periodic shows a closed lab can produce labels for one task without public data." Corrected: the release is evidence neither for nor against pooling public data; "without releasing" is not "without using"; and what they produced are ratings, not ground-truth labels. [OPINION] Periodic staffs metadata work internally, so pitching them a schema is pointless.
- **Slices.** C02, C04-1, C06, C11, R03, R04, R05, R06.
- **Others addressing.** No.
- **Build.** An outside, measurement-checked XRD set (C06 pilot, see G21 and G48). An outcome-grounded recipe evaluation set for DM (see G45). Both are specified only.

### G33. Failures and unbiased sampling are missing from the record
- **Gap.** Literature-derived data over-samples what chemists like to try and what worked.
- **Why ML cares.** A model trained on it learns the habits of chemists, not chemistry. It has few true negatives to learn from.
- **Evidence.** [SOURCE] In one hydrothermal-synthesis study, 17% of the possible amines appear in 79% of reported compounds, and a smaller randomized dataset beat a larger human-chosen one (Jia 2019). One autonomous lab made its target in only 30% of 353 recipes. One recipe set has 80,806 recipes and no failures (Lee 2025). MEAD v1 left out failed measurements. Only about 10% of HTEM entries reached a paper. Text-mined recipes have known biases (Sun & David 2025). [REFUTED] "Open releases are success-only": PG logs 369 unreacted, 113 partial and 26 physical failures. But every one of its 1,351 scans carries status "valid", so scan-level failures are invisible (G27). [REFUTED, two citation uses in the DM report] Raccuglia 2016 has no with-versus-without-failures comparison (it reports 89% success for one compound family). Jia 2019 is about human selection bias, not about journals publishing only successes.
- **Slices.** C01-3, C02, C05, R03, R04, R05, R06.
- **Others addressing.** Partly: PG; combinatorial thin-film libraries that record every composition [SOURCE].
- **Build.** Designed or randomized sampling that records failures (roadmap item, needs labs). An "exploration arm" that deliberately runs some refused recipes (DM proposal, G45).

### G34. No deposition policy and no neutral organizer
- **Gap.** Materials journals do not require authors to deposit raw measurements, and no neutral body runs a recurring blind test.
- **Why ML cares.** In protein folding, the dataset (PDB) and the blind test (CASP) came from rules and institutions, not from one big data release. Without them there is nothing stable to train or rank on.
- **Evidence.** [SOURCE] PDB began in 1971 with 7 structures. A 1989 crystallography-union policy asked for deposition; journals required accession codes in the early 1990s; raw structure factors were required from 2008. CASP has run since 1994. AlphaFold2 trained on an archive of fewer than 150 thousand structures. In materials, the one blind test (run by CCDC) covers molecular crystals only and had one leak incident. A metal 3-D-printing benchmark (AM Bench) drew 3 submissions against 6,044 downloads. ImageNet's own lesson: hidden test labels from 2010 to 2017; AlexNet 15.3% vs 26.2% error; 24 teams in 2013 vs 21 in the three years before; about 6% of validation labels are wrong; a fresh re-test cut accuracy 11 to 14% but kept rankings; pre-training on 127 instead of 1,000 classes cost only 2.8 points, so a narrow start is fine. Working examples: NIMS data sheets; ICDD grants ($1,000 for up to 5 patterns, and ICDD takes the copyright); RSDB; a Caltech provenance store (30 million entries, 1.1 TB); NIST AM Bench. [OPINION] Right order: deposition policy with an embargo first, neutral blind test second, model breakthrough last.
- **Slices.** C01-3, C02, R02, R03, R04, R07.
- **Others addressing.** Partly, outside the target tasks (the examples above).
- **Build.** TE blind round (R07 spec; still no organizer, pilot lab or cost estimate). XRD blind challenge (Track A4 / XRD page B7). Free hidden-answer hosting on Codabench (C16). See G17.

### G35. Datasets have absent owners, and remakes repackage rather than refill
- **Gap.** Many widely used datasets are no longer maintained, so found errors cannot be fixed upstream. New versions mostly re-clean the same rows.
- **Why ML cares.** Errors in benchmark sources are permanent, links rot, and "v2" rarely adds the missing fields you need.
- **Evidence.** [OWN-EXPERIMENT, repository and link checks] The SciGlass repository has been untouched since 2019-05-27. The MPEA repository was archived 2024-11-13. The HTEM repositories were archived 2026-06-30; 7 raw-data endpoints return HTTP 502; a lab rename (NREL to NLR) broke links; public libraries stop at 2019. Open Citrination (a materials-data hosting platform) was decommissioned, though its public datasets stay at their existing URLs (an earlier "shut down" wording is [REFUTED]). One dataset copy (GREA, 7,170 rows) returned 404 on 2026-09-14, and the Sandia composites file (V29) sits behind a form plus a CAPTCHA. The only outside issue on the opXRD repository has been unanswered since March 2026; RRUFF is mid-migration with only a contact form. Starrydata does have a working fixes channel. C16 ranks errata targets: PG first, Starrydata second, opXRD third, RRUFF dropped. Remakes [SOURCE]: MP's recompute with a better simulator setting (r2SCAN) is about 26% done; SciGlass Next v0.9.0 fixed 2,360 ranges; GlassNet went from 281,093 to 218,533 rows; a 2026 paper re-measured 396 alloy conditions (about 9%); nothing was found for steels; PolyMetriX is a merge of 9 sources. Some rows are unrecoverable: 2006 to 2008 Raman settings, a 1980 intensity file, glass thermal history, raw microscopy at about 26 GB per scan, one force-field paper's train/test split (an unseeded shuffle), polymer chain-length distributions. [OWN-EXPERIMENT, tally of the user's own coding] 21 of 106 status marks are "not in the public release". Of 72 gap rows, 49 need only documentation, 14 need both, 9 need only new data. The share needing new data rises by gap type: join 4%, definition 12%, uncertainty 50%, model limit 73%, observation 76%, variation 83%.
- **Slices.** C01-3, C09, R02, N00, C16.
- **Others addressing.** Partly (the remakes above).
- **Build.** Errata lists to owners who still answer (approval-gated). Sidecar correction files instead of upstream edits. HTEM errata as a CSV (the surviving part of N00 B10). Principle from R02: "design the next one complete".

### G36. No credit for sharing, no cost data, and frozen leaderboards
- **Gap.** Researchers get little credit for sharing or fixing data, nobody knows what curating a record costs, and fixing a benchmark breaks its leaderboard.
- **Why ML cares.** These incentives explain why G1 to G29 persist. A fix that needs unpaid effort from many labs will not happen by itself.
- **Evidence.** [SOURCE] 69.2% of surveyed researchers say they get too little credit for sharing data (State of Open Data 2025). Only about a quarter of authors answered requests for missing glass details. 30.9% of the values a GPT-4 extractor missed appeared only in figures. Cost anchors: PDB about $420 per structure; one biology database $219 per paper; one synchrotron beamline €543.84 per hour; one US materials-data grant type $1.5 to 2.0 million over 4 years; a composite moisture soak takes 1,150 to 5,100 hours; a 10-million-cycle fatigue test 29 to 116 days; the longest NIMS creep test ran 350,771.8 hours; OMat24 used more than 400 million core hours; expert XRD relabelling is estimated at about 1,000 expert-hours. No cost per curated materials record was found. [OPINION] Correcting Matbench labels would break comparability, so the benchmark stays frozen and fixes must live in side files.
- **Slices.** R02, C09, N00, C16.
- **Others addressing.** No.
- **Build.** None. The corpus lists field-level levers only: fund round robins, credit curation.

---

## Theme 6. Computed labels versus the real world

The user set this theme aside with an "experimental data first" decision. It stays in the ledger because most public ML benchmarks live here.

### G37. DFT labels carry a systematic physical-model error
- **Gap.** The standard simulator setting (called PBE) is biased in known directions, and every label is for a perfect crystal at absolute zero.
- **Why ML cares.** A model can match the simulator perfectly and still be wrong about the real material. More training data does not remove a bias in the labels.
- **Evidence.** [OWN-EXPERIMENT, one traced material: quartz] Cell volume: PBE 120.3357 Å³ (+6.29%), the newer r2SCAN setting 113.62545 (+0.37%), measured 113.211(7) at room temperature. Against a 0 K measurement the errors are +7.2% and +1.2%, so r2SCAN's room-temperature match is partly luck. Measured cells themselves spread by 0.19%. The PBE cell shifts the strongest XRD line by about 0.56 degrees (26.082 vs 26.642). Band gap: 5.719 eV computed vs 8.9 to 9.65 measured (36 to 41% low). Formation energy against a measured −3.147 eV/atom: −3.257, −3.038 and −3.273 under three settings, a span of 0.235 eV/atom. PBE also ranks quartz 10.6 meV/atom above a sister form (cristobalite), the wrong order; experiment puts cristobalite about 8.7 above quartz. All 17 quartz frames in MPtrj are PBE. [SOURCE] Across 472 solids PBE band gaps average 41.1% low. Raman line positions: 11 cm⁻¹ error with a hybrid setting vs 34 with PBE.
- **Slices.** C01-2, C01-3, C08, R01, R08, N00.
- **Others addressing.** Partly: MP's r2SCAN recompute; newer force-field training sets (MatPES) [SOURCE].
- **Build.** Merged-table checklist (done, as a checklist only).

### G38. Records silently mix simulator settings, and corrections are fitted to experiment
- **Gap.** One database entry can combine values from different simulator settings, and its energies include a correction term that was fitted to measured data.
- **Why ML cares.** Mixed settings are hidden label shift inside one column. A correction fitted to experiments is a possible leak when you later test against experiments.
- **Evidence.** [OWN-EXPERIMENT] In MP's quartz entry: a warning says "Volume change > 20.0%" while the actual change is −4.32%; the elastic constants sit on the PBE cell (volume 120.21) while the headline structure is r2SCAN (113.63); the stability field reads 0.0106 in one place and 0.0 in another; three band gaps coexist (5.719, 6.6311, and a deprecated 7.527); the headline formation energy is the mixed-settings value, as it is on 117,421 documents where setting types differ. GNoME: moving from PBE to r2SCAN flips the stable/unstable call for 22.1% of 117,043 shared entries (4.8% with a 25 meV buffer); 21.7% of ids are no longer served; 30.8% of shared formation energies changed; the training configurations have been listed as "Upcoming" since 2023. [SOURCE] MP's oxygen correction is −0.687 eV per O atom, fitted on 222 compounds, with a residual error of 51 meV/atom; without corrections the error is about 0.35 eV/atom. [OPINION] The correction is a plausible leakage channel, but unmeasured. A counterpoint (Gong 2022) finds about 0.075 vs about 0.104 when test compounds are removed from the fit. [REFUTED] "Matbench's quartz label matches no MP value" (G11).
- **Slices.** C01, C03-2, C03-3, C08, R01, R08, N00.
- **Others addressing.** Partly (the r2SCAN recompute will reduce mixing).
- **Build.** Matbench provenance sidecar (N00 B4, parked). A small patch to MP's open code (N00 B10, parked).

### G39. "Stable on the computer" does not mean makeable
- **Gap.** The usual screen, computed energy relative to competing phases ("energy above hull"), predicts neither whether a material can be made nor how.
- **Why ML cares.** Headline "discovery" counts are counts of simulator-stable candidates. The label that matters, "someone made it", is scarce and disputed.
- **Evidence.** [SOURCE] 50.5% of known phases are metastable, with a median of 15 meV/atom above the hull (Sun 2016). GNoME reports 2.2 million candidates below the hull and 736 matches to known experimental structures ("a lower bound"). Energy differences between crystal forms of one compound (about 10 meV/atom) are smaller than typical formation-energy errors (51 to 136). One autonomous lab found no correlation between computed stability and success. Two senior chemists found "scant" novelty or usefulness in the GNoME list (Cheetham & Seshadri).
- **Slices.** C01-3, C07, C08, R01, R08.
- **Others addressing.** No.
- **Build.** None proposed.

### G40. Nobody has a clean learning curve of real-world error against amount of computed data
- **Gap.** The question "does 10 times more DFT data make predictions of measured values better?" has no direct published answer.
- **Why ML cares.** It decides whether to spend on more simulation or more measurement. The test sets are also too small to see the predicted gain.
- **Evidence.** [SOURCE, corrected after re-reading the paper] The key transfer-learning paper (Jha 2019): error against experiment 0.0715 eV/atom with DFT pre-training, 0.1325 from scratch, 0.1385 using DFT data only, 0.1516 for a random forest; its experimental set shrinks from 1,963 to 1,643 after removing duplicates. [REFUTED] the earlier quote "0.06 vs 0.13 to 0.15". With transfer, about 148 experimental compounds give 0.106 (0.436 from scratch), which beats 1,479 compounds from scratch (0.133). On whether Jha varied the amount of DFT data, the digests word it differently: the notes file says he never did; the later report says he did not vary it *for transfer*, but a side table confounded with source database shows 11k / 24k / 341k giving 0.19 / 0.16 / 0.14, and a 2022 follow-up shows 20k / 102k / 353k giving 0.087 / 0.078 / 0.064 on computed targets. The later wording is the careful one. [OWN-EXPERIMENT, fits to a published table (Chen 2021)] Each 10× of DFT data moves band-gap error by −0.13 to −0.04 eV; about 29 PBE points are worth 1 experimental point at N = 100 (range 10 to 52), about 6 at N = 2,430 (range 0.3 to 37). [SOURCE] Another study: about 221 simulations are worth 1 experiment, and each 10× removes 1.4 to 7.8% of error (Minami 2025). Noise floors: calorimetry about 0.023 eV/atom; compilations about 0.030; two experimental databases differ by 0.082 on 75 intermetallics; DFT vs experiment about 0.08 to 0.10. The predicted gain from 41k to 410k DFT entries (0.009 to 0.040 eV) is below what about 270 test compounds can detect (about 0.08 eV). [REFUTED, retracted] a "rule" that error extrapolates by about 10×. [SOURCE] About 250k of about 300k OQMD entries are hypothetical; a model at 0.022 in-distribution fell to 0.297 on newer alloys (Li 2023).
- **Slices.** C08, R08, N00.
- **Others addressing.** Partly (the papers above, none a clean test).
- **Build.** A nested-subset experiment (1k to 300k DFT entries, 5 to 10 seeds, leakage on and off). Fully specified, "awaiting your yes", not run.

### G41. Computed-side leaderboards score agreement with the simulator
- **Gap.** The mature leaderboards measure how well a model reproduces DFT, not how well it predicts measurements.
- **Why ML cares.** Near-ceiling leaderboard scores do not transfer to the makeability and performance questions.
- **Evidence.** [SOURCE] Matbench Discovery: top F1 0.931; best model trained only on MPtrj 0.863. One force field fine-tunes with about 100 configurations. The 2021 catalyst-challenge winner reached 0.5474 eV against about 0.2 eV needed in practice; one model's error went 0.374 to 0.239 eV across dataset versions. Computed TE properties against experiment: R² 0.79 for Seebeck, 0.33 for power factor (Ricci 2017). [OPINION] Screening bulk stability "looks close to a moment"; predicting what can be made and how it performs does not.
- **Slices.** C01-3, C10, R01, R03, R04.
- **Others addressing.** Not applicable (this is the state of the leaderboards).
- **Build.** None. It motivates the experimental-first decision.

<!--NEXT7-->
