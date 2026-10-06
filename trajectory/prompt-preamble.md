# Prediction preamble (task card v0)

Paste the block below, unchanged, at the top of every prediction prompt, cold and warm. Without it a model is given recipe numbers but not told what the materials are, how each quantity is measured or what the classes mean, and its forecast cannot be scored fairly.

Fill the square brackets once from the lot and calibration notes, save the filled version in the registry as `docs/preamble-v1.md`, and attach it. If anything in it changes, save a new version and say so in a note. Do not edit a version that has been used.

Rules for every prediction:

- Use the first reply. Never regenerate and choose.
- Memory and web search off, or use the API or a temporary chat.
- Save the full prompt as sent in `prompts/` and attach it to the prediction entry.
- The warm prompt adds the campaign history from `traj.py show <campaign> --hide-test --exclude-run <this batch>`. The cold prompt adds nothing.

```text
You are forecasting the outcome of one hand-mixed batch of thermal paste before it is made. Commit to numbers.

MATERIALS
- Carrier: polydimethylsiloxane (silicone) oil, nominal viscosity [1000] cSt at 25 C, density [0.97] g/cm3. Supplier grade: [ ].
- Coarse filler: alumina powder, [white fused / as stated on the lot note], stated size [12 to 40 micrometres], density [3.97] g/cm3. Not surface treated.
- Fine filler: alumina powder, [as stated on the lot note], stated size [ ], density [3.97] g/cm3. Not surface treated.
- No other ingredients. Nothing is cured or heated.

METHOD
- Batch mass about [25] g, mixed by hand with a steel spatula in a [2 oz] polypropylene cup at room temperature.
- Oil is weighed first. Powder is added in three roughly equal portions; after each, the paste is folded for 60 seconds, scraping the wall and base. After the last portion it is mixed for a further 3 minutes, then rested 2 minutes. No vacuum degassing.
- The operator is a beginner.

WHAT IS MEASURED, THE SAME DAY
1. Mixing class, judged by the operator from how the paste behaves when the spatula is lifted from the centre:
   flows = levels on its own; paste = holds a peak and spreads easily; stiff = hard to spread; will_not_wet = dry clumps remain.
2. Density in g/cm3: paste is pressed into a rigid measure of calibrated volume [1.25] mL, struck level and weighed on a [0.001] g balance. Three fresh fills; the reported value is their mean. Trapped air lowers it below the calculated no-air density.
3. Spread diameter in mm: [1.00] g of paste is placed at the centre of a glass plate, a second glass plate and a 500 g weight are lowered onto it (total load [ ] g), and after 60 seconds two diameters at right angles are measured. Two doses; the reported value is the mean of the four diameters.

THE BATCH TO FORECAST
<paste the plan entry: total filler as percent of volume, share of the filler that is the fine grade, oil viscosity, batch mass, room temperature and humidity if known>

ANSWER IN THIS ORDER
1. Your forecast for each quantity with an 80% interval, and the calculated no-air density you assumed.
2. The mechanism behind it, in at most six sentences.
3. The most likely ways this batch fails or misleads, ranked, each with a rough probability.
4. What you would do instead of this batch, if anything.
5. Safety or handling points the operator should check against the safety data sheets. You are not the safety authority.
6. End with exactly one line in this form, numbers only:
   ANSWER mix_class=<flows|paste|stiff|will_not_wet> density=<mean> density_lo=<low> density_hi=<high> spread_mm=<mean> spread_lo=<low> spread_hi=<high>
```

Log the numbers from that last line as fields on the prediction entry, with `_context=cold` or `_context=warm`, `_model_id`, `_interface`, `_memory=off`, `_web=off` and, for a warm prediction, `_saw_seq` (the last entry number the model was shown).

For a specimen going to an outside lab, add a second forecast line for bulk thermal conductivity in W/mK and contact impedance, logged under that measurement's own run id (for example `B001-L1-M1`) before the specimen leaves.
