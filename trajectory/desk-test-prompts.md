# Desk-test prompts (before any powder is measured)

Two prompts for the first forecasts in [EXPERIMENTS.md](../outputs/thermal-paste-first-cycle/EXPERIMENTS.md#forecasts). They ask the open question only. They name no explanation and contain none of the plan's predicted numbers, so the replies show what a model would say unaided.

How to use them:

- Fill the square brackets from the labels and lot notes. Save the filled prompts in the `paste-commission` log's `prompts/` folder.
- One fresh chat per prompt per model. Memory and web search off. Send nothing else.
- Keep the first reply. Never regenerate.
- Log each reply as a `prediction` entry under the run id shown, with the numbers from its `ANSWER` lines as fields and `_context=cold`, `_model_id`, `_interface`, `_memory=off`, `_web=off`. Attach the prompt and the full reply.
- Run `anchor`, commit and push `trajectory/anchors.log`, and timestamp it outside, before the first titration or vial.

## Prompt A: the mixing limit (run id `E12-DESK`)

```text
You are forecasting the results of bench measurements before they are made. Commit to numbers.

MATERIALS
- Oil: polydimethylsiloxane (silicone) oil, nominal viscosity [1000] cSt at 25 C, density [0.97] g/cm3.
- Coarse powder: alumina, [white fused], stated size [325 mesh, 45 micrometres and finer], density taken as 3.97 g/cm3. Not surface treated.
- Fine powder: alumina, stated size [5.5 micrometres], density taken as 3.97 g/cm3. Not surface treated.
- Nothing else is added. Room temperature. The operator is a beginner working by hand.

DEFINITIONS
- Loading = powder volume / (powder volume + oil volume), from weighed masses and the densities above.
- A charge PASSES if, after 60 strokes at one per second with a steel spatula (slow press and smear) in a 60 mL polypropylene cup, all of it is one glossy body that closes over a spatula cut within 10 seconds and shows no matt patch when pressed. Otherwise it FAILS.

PROCEDURE 1, OIL INTO POWDER
12.00 g of powder is placed in the cup. Oil is added in 0.20 g steps, with 60 strokes after each, until the mass first forms one lump, then in 0.05 g steps. The result is the loading midway between the last step that fails and the first that passes.

PROCEDURE 2, POWDER INTO OIL
2.50 g of oil is placed in the cup. Powder is added in three rounds of 3.0 g (2.0 g for the fine powder), then 0.50 g steps until the paste first holds a peak, then 0.25 g steps, with 60 strokes after each. A fail counts only if the charge still fails after 120 further strokes with nothing added. The result is the loading midway between the last step that passes and the first that fails.

POWDERS TESTED
Coarse alone. Fine alone. Blends of the two in which the fine powder is 15%, 30%, 50% and 70% of the powder by mass, weighed separately into the cup and tumbled dry before any oil is added.

FORECAST
1. The result of procedure 1 for coarse alone, fine alone, and each of the four blends.
2. The result of procedure 2 for coarse alone, fine alone, and the 30% blend.
3. Take the loading midway between your two results for the 30% blend. That recipe is made directly, 12 g of powder, 360 strokes in all, in two ways: (a) all the powder first, the oil in three equal portions with 120 strokes after each; (b) all the oil first, the powder in three equal portions with 120 strokes after each. Does each pass or fail?

Give each number with an 80% interval. Then, in at most eight sentences, say why. Then list what could make these measurements misleading.

End with exactly these lines, numbers only:
ANSWER oil_into_powder coarse=<> fine=<> blend15=<> blend30=<> blend50=<> blend70=<>
ANSWER oil_into_powder_lo coarse=<> fine=<> blend15=<> blend30=<> blend50=<> blend70=<>
ANSWER oil_into_powder_hi coarse=<> fine=<> blend15=<> blend30=<> blend50=<> blend70=<>
ANSWER powder_into_oil coarse=<> fine=<> blend30=<>
ANSWER powder_into_oil_lo coarse=<> fine=<> blend30=<>
ANSWER powder_into_oil_hi coarse=<> fine=<> blend30=<>
ANSWER direct_make powder_first=<pass|fail> oil_first=<pass|fail>
```

## Prompt B: standing in a vial (run id `E3-DESK`)

```text
You are forecasting the results of bench measurements before they are made. Commit to numbers.

MATERIALS
- Oil: polydimethylsiloxane (silicone) oil, nominal viscosity [1000] cSt at 25 C, density [0.97] g/cm3.
- Coarse powder: alumina, [white fused], stated size [325 mesh, 45 micrometres and finer], density taken as 3.97 g/cm3. Not surface treated.
- Fine powder: alumina, stated size [5.5 micrometres], density taken as 3.97 g/cm3. Not surface treated.
- Nothing else is added. Room temperature, about [22] C.

PROCEDURE
Each mixture, about 4.5 mL, is mixed by hand with a spatula and within 10 minutes poured gently into a clear capped glass vial of about 12 mm inner diameter to the stated column height. The vial stands upright and undisturbed. It is photographed against a ruler at intervals. At 7 days the top third of the column is drawn into a syringe to a mark and weighed, giving the density of the top layer.

All shares below are by volume.

VIALS
A. Coarse powder alone in oil at 20%, 30% and 40% powder, column 28 mm.
B. Fine powder alone in oil at 5%, 10%, 15%, 20%, 25% and 30% powder, column 28 mm.
C. Blends in which coarse powder is 25% of the whole, and fine powder is 5%, 10%, 15%, 20%, 25% or 30% of the remaining fine-plus-oil part, column 28 mm.
D. A paste that is 40% powder, of which 30% is fine and 70% coarse, in columns of 10 mm and 40 mm.

FORECAST
1. For each vial in A: hours until the top third of the column is clear of coarse powder.
2. For each vial in B: height of clear oil above the powder after 7 days, in mm.
3. For each vial in C and D: the change in top-layer density after 7 days, as a percentage of its starting value (0 = unchanged).
4. Among the vials in C, is there a fine-powder share above which the top-layer density changes by less than 10% in 7 days? If so, which.

Give each number with an 80% interval. Then, in at most eight sentences, say why. Then list what could make these measurements misleading.

End with exactly these lines, numbers only:
ANSWER coarse_clear_hours c20=<> c30=<> c40=<>
ANSWER fine_clear_oil_mm f05=<> f10=<> f15=<> f20=<> f25=<> f30=<>
ANSWER blend_top_change_pct f05=<> f10=<> f15=<> f20=<> f25=<> f30=<>
ANSWER paste_top_change_pct col10=<> col40=<>
ANSWER holds_above=<share or none>
```

Intervals for prompt B are read from the body of the reply and logged as `_lo` and `_hi` fields by hand.
