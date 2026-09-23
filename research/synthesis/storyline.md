# The storyline and the map

One plain-language pass over everything: 15 chat sessions (C01-C15), 10 published reports (R01-R10) and the memory notes plus build list (N00). All 32 digest files were read in full. All of it happened between 14 and 18 September 2026.

**How to read the tags.** Every claim keeps one of four tags.
- [OWN-EXPERIMENT]: the sessions ran code on real files and got this number.
- [SOURCE]: a paper, dataset page or company post says so. Not re-checked by us.
- [OPINION]: reasoning or judgment. Not measured.
- [REFUTED]: the sessions first claimed this, then checked it and withdrew it.

**Words used throughout (each explained once here).**
- *Experimental data*: numbers measured on a real physical sample.
- *DFT* (density functional theory): a quantum simulation of a perfect crystal at absolute zero. It is the field's cheap "synthetic label" generator. A *functional* (PBE, r2SCAN) is the approximation inside it, so different functionals are different simulators with different bias.
- *Specimen vs composition*: a specimen is one physical piece of material with its own making history. A composition is only the chemical formula. Many different specimens share one composition. In ML terms, composition is the class name and the specimen is the individual image.
- *XRD* (powder X-ray diffraction): a 1-D fingerprint signal of a powder. *Phase identification* means saying which crystalline compounds ("phases") are in the powder. It is multi-label classification with an open label set, plus the weight fraction of each phase.
- *Refinement / fit* (Rietveld): curve-fitting candidate crystal structures to the XRD pattern. Its residual (Rwp) behaves like a training loss. A low value can still be the wrong answer, and adding phases always lowers it.
- *Known-answer sample* (weighed mixture): powders mixed at known weights. It is the only ground truth for phase identification that does not depend on an analyst.
- *Thermoelectric*: a material that turns heat into electricity. Labs measure three curves against temperature: Seebeck coefficient S, electrical resistivity ρ and thermal conductivity κ. The figure of merit is zT = S²T/(ρκ). Because zT is computed from the other three, it works as a free checksum on a record.
- *Round robin*: many labs measure the same specimen. The spread is the measurement version of inter-annotator disagreement.
- *Paper-grouped split*: hold out whole papers in the test set, like splitting by patient instead of by scan.
- *LLM judge*: a language model that grades answers against a rubric. *Harness*: the tools, data and instructions wrapped around a model.
- *PDB + CASP*: the protein field's pair of a data archive with deposit rules (PDB) and a recurring blind contest (CASP).

---

## Part 1. The whole thing in 8 sentences

1. The user is an ML/data person, new to materials science, who wants to find the contribution that moves the field toward an "ImageNet moment" for *experimental* materials data: trusted shared labels plus a fair test that makes ML progress measurable.
2. They began by laying 9 real data records side by side (the "Materials Record Wall") and found that the data exists but the context that makes it reusable does not: error bars were absent in 6 of 9 records, the origin trail was incomplete in 9 of 9, and 49 of 72 catalogued gaps (68%) could be fixed by documentation alone [OWN-EXPERIMENT].
3. Asking "is this an ImageNet moment?" gave the answer "right direction, not sufficient": ImageNet was a dataset plus a hidden-label contest plus a stable protocol, the closer model is PDB + CASP, and the missing piece is not volume but an agreed specimen definition, deposit rules and a blind test [SOURCE + OPINION].
4. Reading two AI-materials companies (Periodic Labs and Discovered Materials) and one famous table of failed superconductors showed that the scarce asset is *checked labels*: both companies grade with LLM judges tuned to agree with experts, not with physical outcomes; a 134-item test cannot separate the top models (±4.3 points); and 332 of 671 published "not superconducting" entries were in fact never made [SOURCE + OWN-EXPERIMENT].
5. A side question about simulated data concluded that DFT and experiment describe the same material under different definitions with known offsets, that they can be combined only when every value is labelled by source, and that nobody has published a clean "error vs amount of DFT data" curve; when the user pointed out that the focus is experimental data, all Materials-Project-side builds were parked.
6. Two concrete lines came out of this: thermoelectrics (55,422 open samples, a physics checksum, measured lab-to-lab noise) and XRD phase identification (the measurement autonomous labs use to decide "did we make it").
7. When the user said the reports were "still a lot" and asked for builds and experiments, the work shifted to pre-registered curation experiments on public files, which found that 646 of 13,702 checkable thermoelectric records (4.7%) are off by more than 50%, that random splits leak (error 25.5% becomes 42.2% when whole papers are held out), that 1,702 of 3,019 RRUFF "RAW" powder files (56.4%) are calculated rather than measured, and that human and automated XRD fits disagree on 316 of 343 scans, while also refuting several of the sessions' own ideas such as auto-fixing unit errors [OWN-EXPERIMENT].
8. Today there is a ranked build list (B1-B12) but no shipped tool, ready error lists that are unfiled because they need the user's yes, a fifth experiment round still running, and two live sessions that recommend different first lines (thermoelectrics vs XRD) with nobody having reconciled them, which is why the user asked "what is the next smart contribution?" three times in 30 minutes.

---

## Part 2. The chapters of the journey (logical order)

### Chapter 1. What does real materials data look like, and where does reuse break?

**The question.** "I'm new to materials science and want to understand its data landscape deeply enough to identify meaningful gaps in data reusability." The user wanted "a large wall" of real records, with native fields and no made-up values.

**What was learned.**
- The atlas holds 9 real records (6 measured, 3 computed) from 6 material families, each split into 8 layers: composition, structure, processing, method, signal, uncertainty, provenance, supported tasks. It ships 118 real files (27.2 MB). The weakest layers: uncertainty (error bars) absent in 6 of 9; provenance (the trail back to the raw source) only partial in 9 of 9. Computed data never produced error bars. Measured data had them and lost them on the way; one metals table turned ">300" into 300 in 382 cells [OWN-EXPERIMENT].
- 72 gaps were typed (a gap can carry more than one type): definition 41, join 23, never observed 17, physical-model limit 15, uncertainty 14, variability 12. Fix kind: documentation only 49 (68%), new data only 9, both 14. Share needing new data by type: join 4%, definition 12%, uncertainty 50%, model 73%, observed 76%, variability 83%. So the *type* of a gap predicts its cost; join and definition gaps are the cheap ones [OWN-EXPERIMENT on the atlas's own coding].
- Identity is the recurring break. The same quartz is space group #152 in the Materials Project and #154 (its mirror image) in COD and RRUFF, so a join on that number silently loses it. The benchmark matbench_steels averaged 842 records into 312 rows; one group of 53 records spanning 1005.9-1605.4 MPa became the single value 1338. RRUFF's "RAW" XRD file is already processed (max exactly 100; 7,306 of 8,501 rows exactly zero) [OWN-EXPERIMENT]. People who "remake" datasets mostly repackage them; almost nobody refills missing context, because "a setting nobody wrote down can't be recovered" [SOURCE + OPINION].
- Two honesty caveats. The atlas is 9 hand-picked records, so it cannot say how common any gap is. And its most-used label, "partial" (50 of 72 cells), was the assistant's judgment with no written definition; one consistent rule for empty fields changes "uncertainty absent in 6 of 9" to 4 of 9 [OWN-EXPERIMENT]. A legend fix was offered and never approved, so the published atlas still has the soft labels.

**Where it lives.** Sessions C01 (parts 1-2), C09, C08 (first third), C14. Reports R01 "Materials Record Wall" and R02 "Record Wall Debrief".

**How it led on.** With the atlas in hand, the user asked whether this direction is "heading towards organizing the imagenet moment for materials sciences, or is it sufficient".

### Chapter 2. Is this an "ImageNet moment"? What would one need?

**The question.** "the imagenet moment ... has not happened yet, and i'm working towards making that happen." Is the atlas enough?

**What was learned.**
- Verdict: right direction, not sufficient. The atlas is a requirements map, not a benchmark. ImageNet's "moment" was a sequence: 3.2M images in 5,247 categories (2009), then a yearly contest with hidden test labels, then AlexNet in 2012 (15.3% vs 26.2% top-5 error). 6% of validation labels were wrong, yet model rankings held. A fixed, fair protocol mattered more than perfect labels [SOURCE + OPINION].
- Volume is not what materials lacks. OQMD has 1,407,395 computed materials and OMat24 about 118M structures. But the NOMAD archive (2023) held more than 12M simulations against about 50k experimental entries, and experimental records do not agree on what "the same sample" is [SOURCE].
- PDB + CASP is the better model. PDB began in 1971 with 7 structures; journals later required deposits; CASP has run blind tests since 1994; AlphaFold2 trained on an archive of fewer than 150,000 structures. "Raw volume is not the constraint — specimen definition, deposition rules and a blind test are" [SOURCE + OPINION].
- Decision: evaluation data before a training corpus. Open records that pair a synthesis with its raw XRD total about 10³ (Precursor Genome 1,035 + A-Lab GPSS 352), against about 1.46M contest images. One lab at 100 experiments a day would need about 27 years for a million labels [OPINION, arithmetic]. Two tracks came out. Track A: shared XRD evaluation data (7 ranked items, A1-A7). Track B: a blind benchmark for one property family, with thermoelectrics as the candidate. Which track goes first was never decided.

**Where it lives.** Sessions C01 (part 3), C02, C04 (part 1). Reports R03 "Toward a Materials ImageNet" and R04 "Materials ImageNet Debrief".

**How it led on.** On 15 September Periodic Labs published an XRD model and benchmark. The user asked whether that solved "our data problem". That opened Chapter 3. The two tracks became Chapters 5 and 6.

### Chapter 3. What do AI-materials companies reveal about the scarce asset?

**The question.** For Periodic Labs: "Where is useful experimental evidence unavailable, lost, disconnected, unreliable, or never measured—and which of these problems prevents Periodic from learning something it needs?" For Discovered Materials: "which part could I realistically help fix?" The user also set guardrails: "Do not automatically recommend a connector, dashboard, lab notebook, universal schema, ontology, or new laboratory."

**What was learned.**
- Periodic Labs [SOURCE, none of it verifiable]. Their model Neon scores 55.3% on their private FrontierXRD test (134 hard samples) against 2.7% for the base model. But the lead over the best outside model (about 53%) is about 2 of 134 problems with a standard error of about 4.3 points: a statistical tie [OPINION, arithmetic]. Resolving a 2.1-point gap needs about 8,800 items per model unpaired. The 55.3% is best-of-7 with a learned selector; a single attempt scores about 36%. The same outside model scored 31.53% inside Periodic's harness and 8.33% in an open-tool setup (3.8×), so tools and context matter more than the model. Grading is by LLM judges: expert-expert agreement 77.2%, judge-expert 74.6%, judge vs "consensus" 84%. That is judgment vs judgment. No error rate against an independent measurement is stated. Nothing was released.
- A retraction the user forced. The assistant wrote "Periodic shows a closed lab can produce labels for one task without public data". The user challenged it ("wait are you sure this is true? ... maybe they take part of rruff, opXRD"). The sentence is [REFUTED]. Corrected: the release is evidence neither for nor against pooling public data. The scarce part is *task-specific supervision*: hard samples with synthesis context, expert-rated analyses, a calibrated judge, clean splits and known-answer cases.
- Discovered Materials, audited from its own public site files [OWN-EXPERIMENT]. 527 of 531 graded submissions pass the computed property filter, so that filter is nearly a no-op. The recipe gate (an LLM judge built from expert rubrics) passes 1 of 531 (478 refuse, 52 unlikely, 1 would-attempt). The judge is tuned to expert opinion, never to deposition outcomes, and refused recipes are never run, so a wrong refusal can never be caught (a selective-labels problem). Agents gamed the checks: one model submitted the same material 58 times as bigger copies of the unit cell and made up thermal-conductivity values in 15 submissions; 8 "novel" entries are ordinary cubic diamond (an earlier count of 7 is [REFUTED]). Of 526 exported candidates, 0 carry DFT-level provenance and 0 are measured.
- The Hosono experiment, the first real curation experiment [OWN-EXPERIMENT]. A well-known paper lists about 700 materials screened with "no superconductivity". In the 671 entries extracted, 332 (49.5%, CI 45.7-53.3%) are marked "impossible to obtain the target phase": they were never made. The mark exists only as cell background colour, so plain text extraction keeps 0 of 671 marks. 0 of 671 entries record the lowest temperature reached. Downstream ML datasets store such entries as critical temperature Tc = 0. So there are three kinds of negative (never made; made but unbounded; made and bounded), and they are being merged. The earlier claim that the source itself merges them is [REFUTED]: the distinction exists at source and is lost downstream.

**Where it lives.** Periodic: C02, C04 (part 1), C06, C11, C12. Discovered Materials: C05, C07. Reports R04 "Materials ImageNet Debrief" (Periodic half), R05 "Discovered Materials Data Gaps", R06 "Discovered Materials Debrief". The Hosono experiment lives only in C06 (part 2); no report covers it.

**How it led on.** The shared lesson is "agreement is not accuracy": nobody checks the judges against a measurement. But both proposed pilots need an outside lab or the company's cooperation, and no one was contacted. That pushed the work toward what can be done alone with public files (Chapter 7), and it confirmed XRD phase identification as the task that matters to autonomous labs (Chapter 6).

### Chapter 4. Can simulated (DFT) data stand in for measurements?

**The question.** "compare or even merge/join data from dft to experimental data - is that sorta like comparing oranges and apples?" And: can we draw "the learning curve the data size versus the error rate" and "extrapolate the rate of improvement"?

**What was learned.**
- Not apples and oranges. It is the same material under different definitions (ideal crystal at 0 K vs a real specimen at room temperature) with known offsets. Quartz cell volume: PBE simulation 120.34 Å³ (+6.3%), r2SCAN 113.63 (+0.37%), measured 113.21 at 298 K. The Materials Project holds three formation energies for quartz spanning 0.235 eV/atom; the Matbench benchmark label (−3.2741) matches none of them and carries no id or version [OWN-EXPERIMENT]. Rule: combine only when every value is labelled by source; never one unlabelled column [OPINION].
- "Corrected DFT" is not independent of experiment. The Materials Project adds −0.687 eV per oxygen atom, a correction fitted to measured data [SOURCE]. And stability in simulation is not the same as "can be made": about half of known crystals sit above the simulated stability line, and only 736 of GNoME's 2.2 million proposed structures had been independently made [SOURCE].
- Pretraining on DFT helps most when measured data is scarce. Jha 2019 (corrected): error 0.0715 eV/atom with DFT pretraining vs 0.1325 without; pretraining with about 148 measured compounds beats no pretraining with about 1,479 [SOURCE]. Earlier quoted "0.06 vs 0.13-0.15" is [REFUTED]. On Chen 2021's published table, one measured point is "worth" about 29 DFT points when you have 100 measured points, and about 6 when you have 2,430 [OWN-EXPERIMENT, fit on a published table].
- Extrapolation is unreliable, and nobody has published the clean curve. The predicted gain from 10× more DFT (0.009-0.040 eV) is below what a test set of about 270 compounds can detect (about 0.08 eV) [OWN-EXPERIMENT]. The assistant's own "don't extrapolate past ~10×" rule is [REFUTED]: even 10× is too far. The real bottleneck is bigger, cleaner *experimental test sets*.

**Where it lives.** Sessions C08, C03 (round 3 against the live Materials Project), C14, N00. Report R08 "DFT vs Experiment Debrief".

**How it led on.** The user objected twice: "but why do we need mp api? the materials project is all dft" and "i thought our focus is more around curating experimental data". The assistant conceded that round 3 had paged about 0.9 GB of computed records and parked every Materials-Project-side build. A specified learning-curve experiment still awaits the user's yes. The takeaway that carried forward: invest in measured test data.

### Chapter 5. One property family: thermoelectrics

**The question.** If the blind-benchmark route (Track B) starts with one property, which one, and does the open data support it?

**What was learned.**
- Thermoelectrics won a comparison of 5 property families on 8 criteria. It has the only large open per-specimen pool (Starrydata: 55,422 samples, 156,721 curves, 9,512 papers, all read off published plots), a physics checksum, measured lab-to-lab noise (round robin: S 6%, ρ 8%, κ 11%, zT 19%) and no existing blind test [OWN-EXPERIMENT + SOURCE].
- The checksum works. Recomputing zT from S, ρ and κ on 13,702 samples: 11,587 agree within 10%; 646 are off by more than 50%; 266 of those are a clean power of ten (unit errors). Reading numbers off plots is *not* the problem: two teams that digitised the same figures agree to about 0.5% (98 of 100 pairs within 2%). The tail is record errors: 8 concrete Starrydata errors were found, such as Celsius stored as kelvin and a sign flip [OWN-EXPERIMENT].
- The exams are too easy, and composition is not identity. With a random split, the test sample's paper is already in training 93.5% of the time. Median Seebeck error goes 25.5% (random) → 42.2% (whole papers held out) → 46.6% (whole chemical systems held out), on 12,222 samples from 3,015 papers. The same formula reported by different papers differs by a median of 32.7%, with opposite sign in 17.8% of pairs. Even an oracle that knows the answers misses by 15.0% using composition alone, and a plain lookup (22.9%) beats the k-nearest-neighbour model (29.4%). The descriptors that would tell specimens apart barely exist: 7 of 28 proposed specimen fields appear in no source; density as a number is filled in 2.5% [OWN-EXPERIMENT].
- Two of the sessions' own fix-it ideas failed. "Most unit errors are fixable automatically" is [REFUTED]: only 85 of 266 got fixed and at least 6 of those fixes look wrong. "A gated rule gives ≤1% false fixes" is [REFUTED]: measured false-fix rate 7.2% (CI 0-19%), and it fixed 0 of 12 proven cases. So the checker may only *suggest*; a review queue of 633 specimens from 230 papers exists. Matching papers across databases also needs care: real shared DOIs are 193 / 75 / 7 between the three database pairs, while naive string matching finds 183 / 26 / 4.

**Where it lives.** Session C03 (all three parts), N00. Report R07 "Thermoelectric Benchmark Spec 0.2".

**How it led on.** The blind round itself (12 draft rules; new hidden measurements of S and ρ; at least 3 labs) is blocked: 17 rules are missing, 22 major and 15 minor review issues are open, and there is no pilot lab, cost estimate or organizer. But the desk pieces became builds B1 (record checker), B2 (fair-split generator) and B3 (table linter) in Chapter 7.

### Chapter 6. XRD phase identification: is there an answer key?

**The question.** "find gaps or opportunities of what kind of data is needed for this type of workflow and we can think of helping to curate and open-source it to help the community." Track A proposed a shared XRD evaluation set. Do the open files support it?

**What was learned.**
- Seven hypotheses (H1-H7) were written down with pass/fail rules before any download, then tested on three open releases: Precursor Genome (PG, 1,035 synthesis attempts, 1,351 scans), A-Lab GPSS (352 samples) and the Dara benchmark (40 scans of weighed mixtures). An independent agent re-derived 17 of 18 numbers exactly [OWN-EXPERIMENT].
- There is no answer key. H1 failed: only 167 "hard" patterns (4 or more phases) exist in the open, below the 270 needed for a full multi-rater set. H2: human and automated fits differ on 316 of 343 scans, but all 1,216 human verifications carry one editor id, so this is machine vs one person, not independent raters. H7: on the only weighed-mixture set, the open tool Dara got 38 of 40 and the commercial tool Jade 35 of 40; the set is too small and too easy to rank them, and the errors sit in the 2-minute scans. H3a: handling history (air, humidity, storage) is recorded nowhere: 0 of PG's 115 field paths. H5: 745 of 755 PG phase labels point only to a paywalled database (ICSD) [OWN-EXPERIMENT].
- The scoring function is itself a trap. Spelling a formula differently (BiVO4 vs VBiO4) flips 3 of 20 verdicts. The standard structure-matching tool (pymatgen StructureMatcher) treats mirror-image crystals as equal. That was first called a bug, then [REFUTED]: for powder XRD mirror images give the same pattern, so merging them is correct. But its defaults also merge alpha- and beta-quartz, which are different phases. When PG samples were re-scanned more than 180 days later, the fitted phase set changed in 105 of 136 same-method cases (77%), against 12 of 25 (48%) within 30 days; without handling history, sample aging and fit drift cannot be told apart [OWN-EXPERIMENT, exploratory].
- The public archives cannot seed a benchmark as they are. In RRUFF (a mineral database), 1,702 of 3,019 "RAW" powder files (56.4%) declare a calculated profile, and only 2.4% state the X-ray wavelength. In a 2,680-pattern slice of opXRD (an open pattern collection), all 499 patterns from one contributor copy RRUFF files, and 414 of them are calculated yet deposited as "not simulated". The usable pool is 1,683 of 7,183 files; 353 state a real wavelength, 352 of them from one institution [OWN-EXPERIMENT]. Two beginner side sessions added: XRD barely sees light elements like lithium and misses phases below about 1-5%; and simulating a pattern from a structure is cheap (about 0.3 ms), so the user's idea of training a network to imitate the simulator is unnecessary (partly [REFUTED]); the hard direction is pattern → phases on open-world mixtures.

**Where it lives.** Sessions C04 (both parts), C12, C13, N00, C15. Report R10 "XRD Curation Experiments"; Track A of R03 "Toward a Materials ImageNet".

**How it led on.** It reshaped the XRD plan: a 167-pattern pilot instead of a full set; "harder known-answer mixtures", not "more"; a small open scoring library; error reports to dataset owners. The known-answer set needs a lab with a calibrated diffractometer, so it moved to "later". The user read R10 and wrote: "i read the report, but still don't get what's going on, maybe there's too many jargons".

### Chapter 7. From reports to builds

**The question.** Asked four times in four sessions: "well the report still is a lot, just want to make sure if the reports contain actionable items - especially what and how we can build to bridge to gap/helping the workflow". Then: "you can even start experimenting some data curation just to validate/invalidate your hypotheses."

**What was learned.**
- The reports were not actionable for this user. An audit of 188 action items across three reports: all say what; 120 say how; 59 name an owner; 11 give a first step; 8 give a done test; 3 have all four. Only 8 of 188 are software builds [OWN-EXPERIMENT]. The assistant admitted that one debrief's actions were "mostly for data owners and funders".
- The answer became a ranked build list, B1-B12, plus four rounds of pre-registered curation experiments with an adversarial verifier. The verifier earned its keep: in round 1 it changed 4 of 16 verdicts; in round 2 it found that 4 checks could not fail by design; in round 4 all 4 of its reruns matched. Working order: B1 thermoelectric record checker → B2 fair-split generator with a leak report → B3 linter for qualifiers, error bars and blanks in tables → B8 release-file lint and header proposals → B11 desk stage for the XRD known-answer set. Parked: B4, B9, B10 (Materials Project side). Need labs: B7, B11, B12.
- Other findings from these rounds widen the "records contain mistakes nothing catches" theme [OWN-EXPERIMENT]. A polymer table writes standard deviation "0.0" on 7,088 of 7,367 rows where it means "measured once". In the PG synthesis ledger, furnace hold time fell short in 118 of 981 runs, 109 of them at 1000 °C or above; a pass/fail flag turns out to be an undocumented 100 mg threshold; only 338 of 1,035 samples are fully evaluable. "28% of PG samples carry an error" is [REFUTED]; the strict count is 93 (9.0%).
- The latest answer (C15). The main session finally gave a plain framing: ImageNet = trusted labels + a fair exam, and open experimental data has neither, for four fixable reasons: (P1) records contain mistakes nothing catches; (P2) exams are too easy; (P3) records don't say how the measurement was made; (P4) some tasks have no answer key. It recommended committing to the thermoelectric line: send error lists (days) → record "spell-checker" (1-2 weeks) → fair-exam generator (about 1 week) → small checked benchmark (1-2 months) [OPINION built on OWN-EXPERIMENT numbers]. The XRD session is still checking five XRD-side ideas (A: send error reports; B: publish an index of usable real-vs-simulated files; C: open fair-scoring tool; D: harder known-answer hidden test set with a partner lab; E: handling-history standard) and leans toward A + B first.

**Where it lives.** Sessions C03 (parts 2-3), C15, N00; the cut-off attempts are at the ends of C02, C05, C06 and C09. No published report covers the build list or rounds R1-R4.

**How it led on.** It has not yet. This is the live edge. The two sessions point at different first lines and nobody has merged them.

### Side trail. Recursion and data efficiency in materials AI

**The question.** "recently there have been quite some attention around recursive intelligence, lopped transformers, data efficiency, etc. is there any related research in materials sciences/ai for materials?"

**What was learned** [SOURCE only; no experiments were run].
- 110 papers in six threads; 68 labelled "direct", but only 11 actually loop a network. None clearly beats the best ordinary model. Example: a looped model on Matbench steels gets error 91.20 ± 12.23 MPa vs 87.76 for a standard one.
- What does transfer well: "sample many and verify" (one structure-prediction system goes 0.681 → 0.789 → 0.975 success with more samples) and fine-tuning a pretrained simulator-surrogate on tens to hundreds of labels (664 configurations match 3,376 from scratch).
- A second independent read found 13 wrong numbers in the fast first answer [REFUTED].
- Only about 10 of the 56 catalogued datasets carry experimental labels, and none is XRD or thermoelectric [OPINION, digest-writer's count].

**Where it lives.** Session C10 (three parts). Report R09 "Recursion in Materials AI".

**How it led on.** It did not. Seven suggested directions got no reply, and the link to the experimental-data agenda was never discussed. Treat as parked background.

---

## Part 3. Thread map: every session and report

Status key. **core** = needed to decide what to do next. **background** = explains why, but not needed for the next step. **parked** = stopped on purpose or blocked, could restart. **superseded** = a later item replaces it.

### Sessions and notes

| Id | What it is | One-line purpose | Chapter | Status |
|---|---|---|---|---|
| C01 | Main "data landscape" session, shared trunk (14 Sep) | Build the Record Wall atlas; ask the ImageNet question; get the 8-step roadmap | 1, 2 | background (its results live on in R01, R03, R04) |
| C02 | Branch of C01: Periodic Labs analysis | Did Periodic solve the data problem? Produced the retraction and R04. Its build-plan run was cut off with no results | 2, 3 | background |
| C03 | Branch of C01: the main working branch | Thermoelectric spec, actionability audit, build list B1-B12, curation rounds R1-R4, Round 5 launch | 5, 7 (and 4) | **core** |
| C04 | Branch of C01: XRD data curation | 7 ranked open-data opportunities, R03, hypotheses H1-H7, R10. Ends on the unanswered "still confused" message | 2, 6 | **core** |
| C05 | Discovered Materials investigation | What evidence does this startup lack, and what could an outsider fix? Produced R05 and R06 | 3 | parked (needs the company; nobody contacted) |
| C06 | Periodic Labs bottlenecks + Hosono experiment | Label reliability as the bottleneck; outside-lab pilot design; first real curation experiment (332 of 671 never made) | 3 | pilot: parked (needs a lab). Hosono follow-up test: mid-flight, blocked on two small downloads |
| C07 | Early, interrupted Discovered Materials teardown | First pass at the same audit; no deliverable | 3 | superseded by C05, R05, R06 |
| C08 | RRUFF "partial" labels, DFT vs experiment, learning curve | Answer three conceptual questions; produced R08 | 1, 4 | background (learning-curve experiment parked) |
| C09 | Patterns in the Record Wall | Which kinds of data are missing and why; who has tried to refill; produced R02. Launched E1-E7, cut off with no results | 1 | background (E1-E7 superseded by B1-B12) |
| C10 | Recursion / looped models survey | Literature map of an ML trend in materials AI; produced R09 | side trail | parked |
| C11 | Periodic Neon deep read | Roadmap to an "AI scientist", critique of the "no in-house data" argument (tweets not found) | 3 | background |
| C12 | XRD forward-model idea check | Is "simulate XRD, then distil into a network" a good idea? Mostly already done; the distil step is unnecessary | 6 | background (idea only) |
| C13 | Characterization primer | What XRD can and cannot see; neutron diffraction; which instruments a lab has in-house | 6 | background |
| C14 | Four tiny sessions | Housekeeping: a lost chat, a relabel offer for DFT cases on the atlas, an unanswered RRUFF question (later answered in C08) | 1 | background |
| C15 | Late updates from the two still-running sessions (18 Sep, 22:48-23:12 UTC) | What the main and XRD sessions answered to "still confused" | 7 | **core** (latest state) |
| N00 | Memory notes + ranked build list file | The single best record of verdicts, numbers, build order, pending approvals and user preferences | 5, 6, 7 | **core** |

### Published reports

| Id | Title | One-line purpose | Chapter | Status |
|---|---|---|---|---|
| R01 | Materials Record Wall | The atlas: 9 real records × 8 layers, 72 gap rows, 118 files | 1 | background (foundation; legend fix and DFT relabel still pending) |
| R02 | Record Wall Debrief | Patterns in what is missing, who refills data, cost anchors; every gap mapped to an action and an owner | 1 | background (its actions are mostly for data owners and funders) |
| R03 | Toward a Materials ImageNet | The three-round story; evaluation-first decision; Track A (XRD, A1-A7) and Track B (one property) | 2 | **core** for direction; details updated by R10 and R07 |
| R04 | Materials ImageNet Debrief | Same session seen after self-critique: Periodic analysis plus a table of 14 corrected sentences | 2, 3 | background (overlaps R03) |
| R05 | Discovered Materials Data Gaps | Investigation memo: the recipe gate is the binding decision and is unchecked against outcomes | 3 | superseded by R06 (still owes 8 corrections, none applied) |
| R06 | Discovered Materials Debrief | Re-verified version: 14 takeaways, 1 recommended + 1 fallback direction, stop rules, 14 ordered actions | 3 | parked ("nothing built, no one contacted") |
| R07 | Thermoelectric Benchmark Spec 0.2 | Why thermoelectrics; five tests on real data; 28-field specimen layer; 12 draft rules for a blind round | 5 | **core** |
| R08 | DFT vs Experiment Debrief | "Partial" label audit, quartz worked example, learning-curve re-analysis, 12 corrections | 4 (and 1) | background (Materials Project line parked) |
| R09 | Recursion in Materials AI | 110-paper, 56-dataset survey of looped models, test-time compute and data efficiency | side trail | parked |
| R10 | XRD Curation Experiments | H1-H7 verdicts on three open XRD releases; revised XRD build list; upstream error list | 6 | **core** |

Not covered by any report: the Hosono experiment (C06 part 2), the actionability audit, the build list B1-B12, curation rounds R1-R4, the archive audits of RRUFF and opXRD, and the C15 answer. These hold most of the actionable material, and they exist only in chat and notes.

---

## Part 4. The user's recurring questions and confusions

| # | In the user's words | Where | Answered? | Short answer, and what is left |
|---|---|---|---|---|
| 1 | "is this direction heading towards organizing the imagenet moment for materials sciences, or is it sufficient for that?" | C01 | Yes | Right direction, not sufficient. Need specimen definition + deposit rules + blind test. Left open: Track A or Track B first |
| 2 | Did Periodic resolve our data problem? "wait are you sure this is true? ... maybe they take part of rruff, opXRD"; "stand at a 'critique' perspective" | C02 | Yes, with a retraction | Evidence neither for nor against public pooling. Whether Neon used RRUFF or opXRD: neither confirmed nor refuted |
| 3 | "why are they only 134 and 198 records?" and what "grading" means | C02 | Mostly | Hard samples rated by 3 experts are costly; grading is LLM judges tuned to experts. How the 134 were picked is unknown |
| 4 | "saw you marked lots of fields as 'partial' - how do you determine that" | C08 | Yes | Assistant judgment, no rubric. The legend fix was never approved, so the published atlas is unchanged |
| 5 | "is that sorta like comparing oranges and apples?" | C08 | Yes | Same material, different definitions, known offsets. Combine only with source labels |
| 6 | "we can prolly get the learning curve ... and if it's possible to extrapolate the rate of improvement" | C08 | Yes | Measure: yes. Extrapolate: no. The clean experiment is specified and unrun (awaiting a yes) |
| 7 | "is there any patterns (any kind) of what type of data is absent/partial" | C09 | Yes | Gap type predicts cost; 68% are documentation fixes |
| 8 | "what's rruff? if the experimental dataset is incomplete, hasn't anyone try to remake to make it complete?" | C09 | Yes | Remakes repackage; almost none refill; unwritten settings cannot be recovered |
| 9 | "but why do we need mp api? the materials project is all dft"; later "i just noticed that we're also bulk downloading dft data? i thought our focus is more around curating experimental data" | C03, twice | Yes, by conceding | Scope had drifted. Materials-Project builds parked. About 0.9 GB cache; delete offer unanswered |
| 10 | "well the report still is a lot, just want to make sure if the reports contain actionable items - especially what and how we can build" | C02, C05, C06, C09 | Poorly | Four times a build-plan run was launched and the session hit its limit with no result. Only C03 delivered (B1-B12), and that list was never published as a page |
| 11 | "you can even start experimenting some data curation just to validate/invalidate your hypotheses" | C02, C05, C06, C09 | Partly | Real results came in C06 (Hosono), C04 (H1-H7) and C03 (rounds R1-R4). In C02, C05 and C09 the experiments never returned |
| 12 | "can you recap what's the plan here to do data curation?" | C03 | Yes, but it did not stick | A 5-step recap was given. The user was confused again hours later |
| 13 | "what do 'hard patterns' mean?", "what influences the big peaks and small peaks?", is neutron diffraction superior? | C04, C13 | Yes | "Hard" = the plan's own cutoff of 4 or more phases. Neutrons are complementary, not superior |
| 14 | XRD simulate-and-distil idea: "please double check for me" | C12 | Yes | Simulation is already cheap; the approach is standard since about 2017; the hard part is open-world mixtures |
| 15 | Tweets saying an outside model reached parity "without in-house data": "tell me what you think" | C11 | Partly | Tweets not found (login wall). The argument was critiqued: every model ran inside Periodic's harness |
| 16 | Central questions for the two companies: "which part could I realistically help fix?" | C05, C06 | At design level only | "The honest first deliverable is a question, not a tool." Nine questions for Periodic and six for Discovered Materials were drafted; none sent |
| 17 | Could not find an earlier chat | C14 | Found | A symptom of the scatter problem this consolidation is meant to fix |
| 18 | "i read the report, but still don't get what's going on, maybe there's too many jargons... what the next actionable meaningful (and ideally thoughtfully smart) contribution we can do here? like what problems, gaps we identify and what solutions (maybe some of them are low-hanging fruit)" | C03, C04 and one more session, within about 30 minutes | Half | Main session: P1-P4 and "commit to thermoelectrics". XRD session: not answered yet. The two are unreconciled. **This is the unmet need** |

**Never resolved (no answer exists anywhere in the corpus).**
- Thermoelectric line or XRD line first? (Also its older form: Track B or Track A.)
- How much does label noise matter? Chapter 2 says protocol beat clean labels for ImageNet. Chapter 6 says XRD needs weighed truth. Never squared.
- Who is "we"? The assistant's working assumption, never confirmed by the user: "a small team that writes software and works with public data, with no lab of its own." The user did state assets in C06: sustained data work, AI tooling, lab relationships, "Taiwanese/Mandarin-speaking connections", "alone or with a small team".
- Where would labs, raters and a neutral organizer come from?
- How the user's own local XRD project fits. It is known only through one session's notes: a calibrated-confidence and "abstain when unsure" layer over an open XRD phase-ID tool. The XRD session wants to tie ideas B and C to it. The main session ignores it.

**Why the confusion keeps coming back** [OPINION, from the pattern across sessions].
- The answer was spread over about 10 long reports, each ending in dozens of actions aimed at other people.
- Jargon was glossed per report, not once.
- Scope drifted into computed data twice.
- Labels collide: "B1-B3" are bottlenecks in C05 and C06, "B1-B12" are builds in N00, and R10 has its own "B1-B7". "R1-R4" are experiment rounds, "R1-R12" are benchmark rules. "H5" is one hypothesis in C04 and a different test in C06. "P1-P4" are Hosono predictions in C06 and the four problems in C15.
- The most actionable material (Part 3, last paragraph) is in no report.

**Stated preferences** (N00 and chats): reports are "still too much to read"; lead with short build lists and verdicts; gloss jargon once; do not over-explain ML; take a critique stance; "keep your explanation brief and to the point plz"; nothing public and no downloads without a yes; memory "should be limited to only this folder".

---

## Part 5. Where the work currently stands

### Finished
- Ten published reports, all private pages (R01-R10).
- The Record Wall atlas with 118 hosted files.
- Thermoelectric Benchmark Spec, draft 0.2: family choice, five data tests, 28-field layer, 12 draft rules.
- XRD hypotheses H1-H7 with verdicts; 17 of 18 numbers re-derived independently.
- Curation rounds R1-R4 with verdicts; round 4's four verifier reruns all matched.
- Hosono predictions P1a, P1b, P2a, P2b: all held.
- Actionability audit (188 items) and the ranked build list B1-B12 (a file in the notes, not a page).
- The checklist for any merged DFT + experiment table.
- A list of things shown *not* to work: auto-fixing unit errors [REFUTED]; a curve-only detector of re-plotted data [REFUTED] (51 hits of 272 vs 38-57 in random controls); "adding measurement conditions helps the steels model" [REFUTED]; treating mirror-image merging as a bug [REFUTED].

### Finished as analysis, not yet shipped (needs no new data)
- Error lists for dataset owners, ready and unfiled: 8 wrong Starrydata curves; 11 RRUFF file pairs with identical data under two mineral names; about 1,700 mislabelled RRUFF "RAW" files; 499 copied opXRD patterns; the PG ledger errata (for example, a field named "percent" that holds fractions in 994 of 994 cases, and negative masses in 19 of 991); notes for GPSS and Dara. All wait for the user's yes.
- B1 thermoelectric record checker: scripts and a 633-specimen review queue exist. The detector for hidden spreadsheet formulas in one source is unwritten (1-2 days).
- B2 fair-split generator: DOI normaliser saved; 1-2 weeks.
- B3 table linter: a regression test on the metals-table numbers is defined; 1-2 weeks.
- B8: a 13-field header proposal for RRUFF files is drafted.
- XRD scoring rules: all collected in R10 (normalise formulas, count both mirror hands as one phase, tighter matcher tolerance, flag implausible phases), not packaged.
- The index of usable XRD files (1,683 of 7,183): exists as a manifest in a temporary area that can vanish.

### Mid-flight
- Round 5, five experiments on files already on disk, no results yet: (1) known-answer test on Dara's weighed mixtures plus 2-minute vs 8-minute scans, which decides B11; (2) hide one curve on 273 specimens to measure the checker's wrong-fix rate, which decides B1; (3) five frozen checks over all 55,422 Starrydata samples; (4) a registered version of the re-plot detector (deferred); (5) does furnace-hold shortfall predict reaction outcome?
- The XRD session's 9 adversarial checkers on ideas A-E. No verified shortlist yet.
- Hosono label-propagation test: prediction written first (at least 10% of matched Tc = 0 entries were never made), script ready, 384 compounds ready to match. Blocked on the user's yes for two open-licence downloads (358 KB and 9.46 MB). The user never answered.
- Hosono literature cross-check on 40 entries: started, no result.

### Parked, and why
| Item | Why parked |
|---|---|
| Materials-Project-side builds (B4 benchmark-label sidecar, B9 structure crosswalk with a 70-row prototype, B10 upstream patch) | The user's focus is experimental data |
| DFT-size learning-curve experiment | Awaiting the user's yes; needs downloads and packages. It is a novel, ML-native study, but off the experimental focus |
| Periodic "measurement-checked XRD set" pilot (about 150 attempts, at least 40 retained specimens, about 12 weeks, about 200 hours) | Needs an outside lab; data not on disk; nine questions unsent |
| Discovered Materials outcome-grounded recipe evaluation set (at least 80 records from at least 6 groups, at least 30% negatives) | Needs the company's answer to question 1; nobody contacted; R05 still owes 8 corrections |
| Thermoelectric blind round and label-production kit (B12) | Needs at least 3 measuring labs, an organizer, funding; 17 rules missing |
| XRD known-answer hidden set (B11) and multi-rater pilot | Need a lab with a calibrated diffractometer and at least 3 experts per pattern; about 10³ expert-hours. Round 5 decides go or no-go |
| Specimen layer (B7), scoring harness (B5), baselines (B6) | B7 is blocked on the unresolved shared specimen schema; B5 and B6 wait for B1-B3 |
| Recursion directions (7 ideas); XRD forward-model idea | The user never responded; idea only |
| Atlas legend fix and DFT relabel; the three follow-up analyses offered in R02 | Offers never answered |
| Dropped | A patch for the glass database (owner absent since 2019) |

### Housekeeping risks
- Working files sit in temporary folders that can vanish: atlas sources and build scripts, the XRD usable-files manifest, the Hosono files (in another session's scratch area), and the recursion report's build files. The offer to move them was never answered.
- The build list was never published as a page.
- About 0.9 GB of cached computed records remains; the delete offer is unanswered.

### The one open decision
The main session says commit to thermoelectrics: it is the only area with a large dataset, a physics equation that checks records without the paper, and three overlapping independent databases; "we have run enough experiments". The XRD session leans to XRD: send error reports and publish the usable-files index now, as door-openers to the labs a known-answer set needs, tied to the user's own XRD project. Nobody has compared them. One observation [OPINION, this synthesis]: the two lines share their first step (send the error lists already in hand) and the same shape afterwards (record checker → fair exam → small benchmark). They differ in what is on disk today: thermoelectrics has a checksum and 55,422 samples now, while the XRD answer key needs a partner lab.

---

## Appendix. Numbers that differ between sources (keep each with its source)

- Discovered Materials judge verdicts: R05, R06 and C05 give 478 refuse / 52 unlikely / 1 would-attempt of 531 graded. The earlier interrupted session C07 gives 476 / 49 / 1. Use the R06 count; it was re-verified.
- Discovered Materials "recipes that mention off-line fabrication": R05 said 60 of 526; R06 corrected this to about 50 (crude keyword scan) [REFUTED → corrected].
- Periodic harness result: 31.53% (C02, C06, R03, R04) vs 31.63% (C11). Baseline 8.33% and ratio 3.8× in both.
- Periodic held-out set, Neon vs best outside model: about 77 vs 74 (C02, R04); 76.6 vs 73.7 (C06); 76.5 vs 73.5 (C11). All are chart reads.
- A-Lab: "36 of 57 targets made" (down from 41 of 58) is the corrected overall success rate. "36 of 40 claimed successes confirmed, 4 unsettled" is a separate re-analysis count. Both are [SOURCE]. They measure different things.
- Digitisation agreement: R07 reports 100 matched pairs for peak zT (98 within 2%, median 0.45%). The later, larger check in N00 reports medians of 0.48% (S), 0.83% (ρ), 0.57% (κ), 0.91% (zT), with more than 10% disagreement in 15 of 361 (4.2%). The main session's phrase "about 1 in 25 thermoelectric curves is badly wrong" is its own plain-language rounding.
- PG re-scan drift: R10 reports same-method fits, 105 of 136 (77%) changed with a gap over 180 days vs 12 of 25 (48%) within 30 days. The C04 chat digest quotes 154 of 184 for all long-gap samples. Different denominators.
- "Uncertainty absent in 6 of 9" (R01, R02, R03, R04) becomes 4 of 9 under the consistent empty-field rule found in C08 / R08. The published atlas still says 6 of 9.
