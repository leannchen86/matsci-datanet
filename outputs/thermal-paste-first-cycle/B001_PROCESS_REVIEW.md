# B001 process review — 9 October 2026

**Status: retrospective review and candidate method changes. No new batch, weighing rehearsal or correction to B001 has been performed.** Keep B001 as the existing practice archive. The next physical task is a dry equipment/weighing rehearsal, followed by a revised run card; another powder batch waits for that preparation. B1 remains open.

Evidence is the operator's reports and four photos in the [published B001 record](https://github.com/leannchen86/matsci-datanet/tree/codex/aln-pilot-preparation/trajectory/releases/B001). That original 35-entry release is unchanged. This review records subsequent reasoning, not observations made before the experiment.

## 1. The operator's residue criticism

Leann raised the residue/composition concern **during B001, after round 2 and before round 3** (entry 23). The assistant recorded the uncertainty but continued the practice method. The new post-run proposal is to retain the spatula in the jar for weighing, measure mass differences, and adjust subsequent powder additions. The concern originated with the operator; it was not a later assistant discovery.

**Accept the concern and investigate the weighing improvement; do not adopt automatic recipe compensation.** The assistant should have designed the weighing boundary, tool handling and residual-material accounting before the first addition. “Scrape back” was insufficient as a quantitative material-recovery instruction.

Three different quantities matter:

| Quantity | What it tells us | What it cannot tell us |
|---|---|---|
| Sum of actual ingredient additions | Reported input amounts and input recipe | Composition of the final usable portion after handling |
| Mass retained within a defined jar/tool assembly | Whether total measured mass is approximately accounted for | Whether a discrepancy is oil, coarse powder, fine powder or weighing error |
| Composition and uniformity of the portion taken for testing | What the lab specimen actually contains | Not established by gross weighing or a photograph |

Paste on the **inside wall** is already included in the jar's weight. Paste on a spatula is included if that spatula is part of the weighed assembly. Neither is necessarily permanently lost. However, material outside the actively mixed body may be poorly incorporated. Scraping the walls and blade therefore still serves a mixing purpose; retaining the tool does not make scraping unnecessary.

If a homogeneous mixture were removed without preferentially retaining any ingredient, its removal would reduce amount without changing the remainder's ingredient ratio. During staged mixing, neither homogeneity nor the residue's composition is established. A mass deficit alone is one equation for three unknown ingredient deficits. For example, the same 0.05 g deficit could be oil or powder; the appropriate correction would differ. Adding powder automatically could move the recipe farther from its target.

**Decision:** keep intended ingredient targets fixed, record actual additions, and investigate discrepancies separately. A known shortfall of a pure ingredient before mixing can be handled against that ingredient's target. An unexplained post-mixing mass change is not grounds for adding oil or either powder. No compensation is prescribed for B001.

## 2. What the B001 numbers establish

| Item | Recorded or calculated value |
|---|---:|
| Oil input | 6.718 g |
| Coarse input: 4.272 + 4.266 + 4.267 | 12.805 g |
| Fine input: 1.835 + 1.847 + 1.886 | 5.568 g |
| Sum of reported inputs | **25.091 g** |
| Current empty labeled jar, no lid | 204.588 g |
| Final jar + contents, no lid | 229.612 g |
| Material associated with jar, by subtraction | **25.024 g** |
| Input minus jar-associated material | **0.067 g, about 0.27% of input** |

The 0.067 g is an **apparent discrepancy**, not proven physical loss or measured oil/powder loss. There is no clean-tool baseline or final residue measurement. Final spatula exclusion was instructed but not separately reconfirmed. The earlier empty-jar indication was 204.402 g; labeling occurred between reports, but the reason for the 0.186 g difference is unconfirmed. Neither difference can be assigned to a material component.

## 3. Other process problems and changes to make

| Issue and evidence | Consequence | Concrete improvement |
|---|---|---|
| **Chat drove the sequence.** The first actual coarse reading, 4.272 g, was confused with a possible next target. About one extra minute of mixing followed round 1. Round-2 mixing duration was not explicitly reported. | The real mixing history differs from the planned history; interruptions also obscure elapsed time. | One complete run card before starting, with target and actual columns kept separate. Show all seven additions and every timer. Record locally, then transcribe; no routine chat approval between additions. |
| **Tool/vessel suitability was not rehearsed.** Photos show wall/rim coatings in a relatively large reused jar and a narrow blade. Actual dimensions are unrecorded. | Poor access is a plausible contributor to uneven incorporation and awkward handling, not a demonstrated cause of stiffness. | With clean, dry equipment, check that the blade reaches the bottom and walls and that the vessel is stable. Record vessel and blade geometry. Change to a smaller smooth-sided vessel only if needed, then rehearse that exact combination. Do not enlarge the batch just to fill the jar. |
| **Weighing qualification remained incomplete.** Calibration with a supplied 200 g weight was reported; the cover affected readings. Five repeat readings and zero returns were never supplied. | Displayed 0.001 g increments are not verified small-addition accuracy. | Save actual repeat readings in the final configuration; check small additions with the working preload before counted batches. Record any cover/static/contact effects without guessing the cause. The learning-only exception did not establish a numerical pass. |
| **The final fine addition overshot.** 1.886 g versus 1.830 g was +0.056 g, outside the working ±0.020 g addition target. | Actual inputs differ from the planned recipe. We cannot attribute stiffness to this difference. | Approach the target in smaller increments; record the stable reading once. Keep the overshoot as a deviation. Do not extract mixed material or dilute it to conceal the deviation. The working tolerance is not a measured uncertainty or a scientifically validated performance threshold. |
| **Mixing and endpoint descriptions were underspecified.** “Mix normally” and “stiff” depend on motion, timing and operator. Temperature was unmeasured. | A label alone can hide differences in preparation and observation. | Specify the same folding/scraping motion and durations; record actual times and interruptions. After a fixed rest, use the same lift/spreading observation, a brief timed video if practical, and separate notes for visible dry pockets, peak relaxation and perceived resistance. Preserve the operator label too. |
| **Readiness was treated too loosely.** Initial records described a living-room table and ordinary bags; subsequent readiness was self-reported without the actual revised arrangement. | The archive does not demonstrate an SDS-based powder-control arrangement or completion of the stated readiness checks. | Before another powder session, document the actual applicable handling setup and balance check results. The assistant should not have treated a general completion statement as those missing records. An ordinary bag catching spills is not demonstrated airborne-dust containment. |

The logging interval from the empty-jar entry to final weighing was approximately 116 minutes. This is **not measured active bench time**, but it reinforces the need to separate hands-on work from transcription. The original 30–45 minute estimate was not validated by this session.

Balance readability, repeatability and accuracy are different concepts; the check must match the load and environment. See the [METTLER TOLEDO analytical-balance guidance](https://www.mt.com/us/en/home/products/Laboratory_Weighing_Solutions/analytical-balances.html). Flow measurements can depend on temperature, time and deformation history; this motivates recording conditions, not diagnosing B001 as thixotropic. See [AMETEK Brookfield's rheology guidance](https://www.brookfieldengineering.com/resourcelibrary/why-perform-rheology-testing). The existing [calcined-alumina SDS](https://gnpgraystar.com/wp-content/uploads/2020/10/Calcined-Alumina-2020.pdf) requires avoiding dust and appropriate ventilation; applicability to the delivered lot still needs confirmation.

## 4. Candidate weighing revision — rehearse before adopting

1. Define the weighed assembly as the **labeled jar + one dedicated mixing spatula**, with no lid. Record the clean, dry jar-only baseline and then the combined baseline. Keep all labels and components unchanged. The combined load must remain within capacity and be supported entirely by the pan; the tool must not touch the housing, cover, table or hand.
2. Rehearse stable placement, removal, zero return and known-weight additions with this assembly. Keeping a tool in the jar is not automatically more accurate. If it causes contact, instability or an unsafe layout, retain a cup-only method with a defined tool rest and documented residue accounting instead.
3. If the revised assembly passes that rehearsal, write it into a new method version. Use a fresh tare with the same assembly for each net ingredient addition. Mix **off the balance**. Continue scraping/folding to incorporate wall and blade material; do not promise 100% recovery.
4. Use planned gross-mass checkpoints after mixing stages, without creating chat pauses. To obtain gross mass, remove the assembly, clear the prior tare with the pan empty, then replace it and record the stable reading. Calculate:

   `apparent unaccounted mass = sum of actual additions − recorded intentional removals − (current gross assembly − empty assembly baseline)`

   This formula applies only to the unchanged assembly. Powder or paste on the pan or jar exterior may also be counted without entering the usable mixture; keep those surfaces clean and document contamination and cleanup losses. Record any unexplained change. Do not apply the per-addition ±0.020 g target as a mass-closure acceptance limit: uncertainty from multiple readings and the actual repeatability screen must be considered.
5. Take the final combined-assembly checkpoint **before** removing the tool. Any subsequent jar-only recovery calculation uses the empty-jar baseline instead. A clean-tool baseline and final tool-plus-residue reading can estimate residue mass if feasible, but not its composition; do not count that residue twice. Keep the configuration change explicit. Close the jar properly for rest/storage; do not leave the lid ajar around a spatula to preserve the weighing arrangement.

This proposal changes the method. It does not retrospectively improve B001's measurements or authorize counted A/B batches. The immediate dry rehearsal needs no new paste. A later practice batch tests whether the revised workflow is executable; changing several handling details at once does not isolate which detail affects material properties.

## 5. What counts as progress

The next practice pass means the operator can follow the prepared sequence, obtain and preserve the required weighing checks, reach the vessel surfaces, record actual additions/times/deviations, and make the stated observation. It does **not** require a runny paste, zero residue, every addition hitting the last decimal, or demonstrated microscopic uniformity.

B001's “stiff” result is a valid handling observation, not a thermal-conductivity measurement or an overall failure label. Its actual preparation differs from the forecast prompt. Preserve both; one practice batch cannot establish forecast calibration or the value of expanded experimental histories. A useful immediate output is a method with identifiable uncertainties and a record another person could follow. Later, compare recipe/results, a competent concise summary, and the expanded history on the same decision and subsequent outcomes; do not equate more logging or more noise with more scientific value.

**Current decision:** review and dry rehearsal first; freeze a revised run card only afterward. B001 stays unchanged and archived. Counted A/B still need the full applicable balance/handling checks, a rehearsed written method, and confirmed lab packaging and timing requirements.

## 6. Second, independent review (9 October)

Added by a second assistant after sections 1 to 5 were written. Five reviewers each took one part of the process; three skeptics then checked every finding against the log, the arithmetic and whether one beginner can do it at a home bench. Only findings that survived are here. No new measurement was made. "Loading" is the share of the paste's volume that is powder; 0.01 is 1 vol%.

### 6.1 How big the residue effect was

| Quantity | Value |
|---|---|
| B001 as weighed | Loading 0.4006 against a target of 0.3999; 30.3% of the powder fine |
| Everything that left the jar | 0.067 g. At most +0.0024 loading if it was all oil; 0 if it was finished paste |
| Paste stranded inside the jar and never folded back | +0.013 loading per gram if it is round-1 material; +0.004 per gram if round-2; 0 if finished paste |
| The fine overshoot of 0.056 g | +0.0007 loading |
| Powder correction the 0.067 g would have called for | 0.022 g coarse and 0.010 g fine per round, smaller than the dosing error it would sit on |
| Smallest difference the experiments count | 0.03 |

The photos show only thin streaks high on the wall at round 2; the thick lump on the rim appears after the final scrape. So most of it is finished paste, which costs yield and not concentration. Early stranded material is probably under 0.2 g, under +0.003 loading; a photo cannot measure it. The 0.067 g itself rests on one unrepeated empty-jar reading.

**So:** for B001 the residue did not matter. In a titration, where one step is 0.005 loading, it can.

### 6.2 Where this review differs from sections 1 to 5

1. **Spatula on a weighed rest, not standing in the vessel.** Weigh "rest + clean dry spatula" before the oil and again at the end. From then on the spatula is only ever in the vessel or on that rest, and is never wiped. This works in a light 60 mL cup, lets the lid go on for the rest, and turns what the blade holds into a number. With the spatula inside the weighed assembly the mass closes by construction and measures nothing. Standing-in is allowed only in a vessel where a dry test passes.
2. **The scrape caused the stranding.** Paste wiped on the rim is outside the folding path. New rule: never wipe the blade on the rim or the upper wall; strokes 51 to 60 of every 60 sweep the wall and the blade down into the paste.
3. **Vessel.** Make the next practice batch in the vessel A and B will use: the 60 mL cup if it is in hand. A weighing routine rehearsed in the 205 g jar is not a rehearsal for a 5 g cup.
4. **Outcome.** Replace the feel word with timed yes/no answers taken from one video after the 2:00 rest: one cut to the base with the thin edge of the blade, one lift. Cut closed at 10 s? At 60 s? Peak still standing at 60 s? Any dry or matt patch? The feel word stays as its own field. Write the paste depth. Put this readout into the forecast prompt before the forecast is taken.
5. **The titration endpoint is untested and may not hold.** It requires the paste to close over a cut within 10 seconds. B001 at loading 0.40 held ridges on vertical glass through the rest; a liquid of this thickness would level in seconds, so the paste may have a yield stress (it does not flow below some push). No cut was made, so this is not known. If a 0.40 blend does not close a cut, the endpoint as written puts this blend's limit below 0.40, where the plan assumed 0.49 to 0.62 and the two desk forecasts said 0.56 and 0.62. The dry side would then need at least 4.40 g of oil on 12 g of powder, and the wet side's opening rounds (0.23, 0.37, 0.47) would jump straight over it. **Check on the next practice batch:** if the cut is open at 10 s, the wetting clauses (one glossy body, no matt patch) become the pass or fail and closing time becomes a recorded number, before C1. The desk forecasts answered the endpoint as written; if it changes, say so in the log and take a second, labelled forecast.
6. **Time.** The batch took 115 min 40 s by the log, against 8 minutes of timed work in the method. Seven weighed additions took 48 minutes. The gap that should have held a 2 minute rest was 35 min 37 s, so the rest was somewhere between 2 and about 35 minutes. The class cannot be scored cleanly against a forecast made for a 2 minute rest.
7. **The balance at the size of a titration step.** A balance that under-reads each 0.05 g step by 0.010 g would by itself create a 0.03 gap in Experiment 1. Test in the dry sitting: ten additions of about 0.05 g of oil, each tared; their sum must match the change in gross mass within 0.010 g. The five repeat readings and zero returns need only a fixed object such as a coin, not check weights.
8. **The forecast.** It gave flows 0.50, paste 0.38, stiff 0.09. Scored as "stiff" it does worse than a uniform guess (log score 2.41 against 1.39; lower is better); had the same paste been called "paste" it would do better (0.97). The score turns on a word nobody can check; the photos support only "did not level". B001 is recorded as not scored. Write the scoring rule before the next forecast; that forecast is no longer blind, because B001 is public.
9. **A cap on the paperwork.** All the proposals together come to about 110 written items. Cap the run card at about 45, no more than 25 of them while paste is in the vessel, and do the balance and equipment checks in a separate sitting.

Three choices were contested between reviewers and settled this way: never add strokes when lumps remain (write the lump count instead); weigh powder straight into the vessel, tapping the last few hundredths in, and aim low; nothing is ever placed above the paste line during a batch.

### 6.3 Free now, no powder

From the B001 jar and the kit, after the planned side photo of the closed jar:

- Reweigh the jar without its lid, twice, beside 229.612 g. This is the only repeat reading B001 can still give.
- Measure the jar's inside diameter, the paste depth, and the spatula's length, blade width and mass.
- Write down the balance model, its stated repeatability from the manual, and the pan diameter.
- Read the capture time of each of the four photos from the phone's camera roll, and the send times of the bench messages. That may recover the rest time.
- Say what the knife in the after-final-mix photo was used for, and what covered the jar during the rest.
- Cut the same paper and tape as the label and weigh them, to check the 0.186 g jump in the empty-jar reading.

### 6.4 For the project owner to decide

1. Spatula on a weighed rest (this section) or standing in the jar (section 4).
2. The 60 mL cup or the glass jar for the next batch, A and B.
3. Whether aged B001 may be used as rehearsal paste for the cut, the lift and 60 counted strokes. It costs nothing and needs no powder, but B001 then stops being an undisturbed archive.
