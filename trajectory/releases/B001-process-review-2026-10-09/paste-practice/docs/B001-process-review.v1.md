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
