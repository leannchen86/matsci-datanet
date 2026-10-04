# Stanford AlN evidence table

AI checked; human review pending. All page numbers are physical PDF pages.

**6 main-supported; 7 newly resolved by the supplement; 3 unresolved.** These counts concern the fixed questions, not model performance or laboratory reproducibility.

Read [the original article and supplement](https://poplab.stanford.edu/pdfs/Vaziri-AlNthermalMaterial3DICs-afm25.pdf). The pinned local copy can be restored with fetch_source.py. `not_found` means the requested detail at the requested level was not located in this packet. Related information is preserved below.

## Q01 Which deposition technique was used for the AlN films?

**Object:** campaign. **Required:** Technique including sputtering excitation and reactive operation.

**Candidate answer:** Reactive DC magnetron sputtering

- Main: explicit — PDF p. 2; Section 2.1, opening sentence
- Supplement: explicit — PDF p. 10; S1, opening paragraph
- Human review: pending

## Q02 What manufacturer and model identify the AlN deposition instrument?

**Object:** campaign equipment. **Required:** Manufacturer and model; a generic technique alone is insufficient.

**Candidate answer:** AJA ATC 1800-F

- Main: not_found — PDF p. 2; Section 2.1; full main article inspected
- Supplement: explicit — PDF p. 10; S1, opening sentence
- Human review: pending

Interpretation limit: Associate the instrument with AlN deposition; do not substitute the transducer evaporator.

## Q03 What substrate stack was used for the standard cross-plane AlN specimens?

**Object:** cross-plane specimen family. **Required:** Underlying substrate, intervening material and its thickness; do not substitute the in-plane membrane stack.

**Candidate answer:** 14 nm amorphous SiO2 on Si

- Main: explicit — PDF p. 2, 3; Section 2.1; Figure 2a inset
- Supplement: explicit — PDF p. 10; S1, substrate paragraph
- Human review: pending

Interpretation limit: Standard cross-plane specimen family only. Keep the in-plane membrane family separate (main Section 2.4, PDF p4).

## Q04 Was the substrate actively heated or cooled during AlN deposition?

**Object:** deposition thermal control. **Required:** Explicit thermal-control mode; a temperature bound alone is insufficient.

**Candidate answer:** No active substrate heating or cooling

- Main: not_found — PDF p. 1, 2, 7; Temperature bounds; no control-mode statement located
- Supplement: explicit — PDF p. 10; S1, opening sentence
- Human review: pending

Interpretation limit: Do not translate absence of active heating into a room-temperature substrate.

## Q05 What typical stabilized substrate-temperature range is described during deposition?

**Object:** campaign thermal state. **Required:** A typical stabilized range with its qualifier, not merely an upper bound or a heater setpoint; do not imply a per-run temperature trace.

**Candidate answer:** Mostly 90–130 °C at saturation

- Main: not_found — PDF p. 1, 2, 7; Abstract; introductory results; conclusion
- Supplement: explicit — PDF p. 10; S1, opening paragraph
- Human review: pending

Related main context: Only <200 °C, not the requested stabilized range.

Interpretation limit: A qualified campaign description, not a universal bound, setpoint, or per-run temperature trace.

## Q06 What nitrogen fraction of the argon-plus-nitrogen gas mixture was explored?

**Object:** campaign parameter range. **Required:** Definition of fraction and numerical explored range, not only the favorable subset.

**Candidate answer:** N2/(Ar+N2): 30–98%

- Main: explicit — PDF p. 2; Section 2.1, parameter paragraph
- Supplement: explicit — PDF p. 11; S1, first paragraph
- Human review: pending

## Q07 What chamber-pressure range was explored for deposition?

**Object:** campaign parameter range. **Required:** Full explored numerical range and unit, not only favorable conditions.

**Candidate answer:** 2–8 mTorr

- Main: not_found — PDF p. 2, 6; Sections 2.1 and 2.7
- Supplement: explicit — PDF p. 11; S1, first paragraph
- Human review: pending

Related main context: Pressure is discussed; its numerical explored range was not located.

## Q08 What DC sputtering-power range was explored?

**Object:** campaign parameter range. **Required:** Full explored numerical range and unit, not only favorable conditions.

**Candidate answer:** 50–200 W

- Main: explicit — PDF p. 2; Section 2.1, parameter paragraph
- Supplement: explicit — PDF p. 11; S1, first paragraph
- Human review: pending

## Q09 What target-to-substrate distance range was explored?

**Object:** campaign parameter range. **Required:** Full explored numerical range and unit, not only favorable conditions.

**Candidate answer:** 10–30 cm

- Main: not_found — PDF p. 2; Section 2.1
- Supplement: explicit — PDF p. 11; S1, first paragraph
- Human review: pending

Related main context: Relative position is varied; the numerical distance range was not located.

## Q10 Which measurement methods were used to determine AlN film thickness?

**Object:** film metrology. **Required:** Explicit identification of the thickness measurement methods; a thickness value alone is insufficient.

**Candidate answer:** AFM and XRR

- Main: not_found — PDF p. 2, 6, 7; Methods and thickness discussion; full main article inspected
- Supplement: explicit — PDF p. 11; S1, second paragraph, opening sentence
- Human review: pending

Interpretation limit: Thickness metrology; do not substitute XRD structural characterization.

## Q11 What metal and thickness describe the TDTR transducer?

**Object:** cross-plane measurement stack. **Required:** Both transducer material and nominal thickness; do not substitute the in-plane heater.

**Candidate answer:** Al, 80 nm

- Main: explicit — PDF p. 3; Figure 2a stack inset; visual label
- Supplement: explicit — PDF p. 11; S1, second paragraph, TDTR preparation
- Human review: pending

Interpretation limit: Main-article figure label is omitted by pdftotext. Counting it as supplement-only would be an extraction error.

## Q12 What maximum cross-plane thermal conductivity and accompanying uncertainty are explicitly reported?

**Object:** reported best cross-plane result. **Required:** Value, stated uncertainty and units; preserve the uncertainty notation without inventing a confidence level.

**Candidate answer:** 92 ± 20 W m^-1 K^-1

- Main: explicit — PDF p. 3; Section 2.3, first paragraph
- Supplement: partial — PDF p. 12, 14; Figure S2; S5, error methodology
- Human review: pending

Related supplement context: Plot and uncertainty discussion; no exact numerical maximum label located in SI.

Interpretation limit: Do not relabel the stated uncertainty as SD, SE, 95% CI or deposition-to-deposition variability.

## Q13 How many spatial locations were measured by TDTR per sample, and how were their variations handled?

**Object:** within-sample measurement repetition. **Required:** Number of locations and stated treatment of variation; these are not independent depositions.

**Candidate answer:** Three locations; variation included in total error

- Main: not_found — PDF p. 3; Section 2.3; full main article inspected
- Supplement: explicit — PDF p. 11; S1, second paragraph, final sentences
- Human review: pending

Interpretation limit: Spatial locations are not independent deposition runs.

## Q14 How many independent deposition repeats at the recipe associated with the maximum cross-plane conductivity are identified?

**Object:** best-recipe deposition repetition. **Required:** Count explicitly linked to that recipe; campaign size, multiple spots or thickness variation across nominal repeats do not supply this count.

**Candidate answer:** Not found at the requested level in this source packet.

- Main: not_found — PDF p. 3; Section 2.3 and Figure 2; full main article inspected
- Supplement: not_found — PDF p. 11; S1; full supplement inspected
- Human review: pending

Related supplement context: Same-parameter inter-sample thickness variation is described, but no independent-repeat count linked to the best-result recipe.

Interpretation limit: Unknown count is not zero. Multiple specimens with common parameters need not represent independent depositions.

## Q15 What exact nitrogen fraction, pressure, power and target distance are linked to the specimen producing the maximum cross-plane conductivity?

**Object:** best-result recipe-to-specimen link. **Required:** All four exact settings and an explicit link to the identified result. A favorable multi-parameter window is insufficient.

**Candidate answer:** Not found at the requested level in this source packet.

- Main: not_found — PDF p. 2, 3; Section 2.1; Section 2.3 and Figure 2; full main article inspected
- Supplement: not_found — PDF p. 11; S1, first paragraph; full supplement inspected
- Human review: pending

Related supplement context: A favorable Type II parameter window is available; an exact four-setting recipe explicitly linked to the maximum result was not located.

Interpretation limit: Do not select endpoints or midpoints from four ranges and label the combination the authors' best recipe.

## Q16 Can a complete deposition-by-deposition recipe-to-specimen-to-thermal-result table be recovered for the reported campaign?

**Object:** campaign record linkage. **Required:** Inspect all tables, figures, captions and text for explicit run identifiers and linked records. A deposition count or aggregate trend is insufficient; state that any absence conclusion is bounded to this source packet.

**Candidate answer:** Not found at the requested level in this source packet.

- Main: not_found — PDF p. 2, 3, 5, 6, 7; Figures 1–6; Data Availability Statement; full main article inspected
- Supplement: not_found — PDF p. 11, 12, 13, 14, 15, 16, 17; S1 and Figures S1–S8; full supplement inspected
- Human review: pending

Related supplement context: About 90 depositions are mentioned, without a complete run-indexed recipe/specimen/thermal-results enumeration.

Interpretation limit: The paper has partial measurement links. This finding concerns a complete campaign ledger, not the absence of all linked data or poor laboratory recordkeeping.
