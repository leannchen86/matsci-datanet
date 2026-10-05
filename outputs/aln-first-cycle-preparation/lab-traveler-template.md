# AlN cycle 001 — printable run and handoff sheet

**Template only. No material has been received and no experiment has occurred.** Proposed identifiers below are reserved names, not evidence of fabricated samples. Use a lab-approved electronic device or approved cleanroom paper inside the facility. Keep completed forms and private supplier records in approved private storage.

## Before anything is ordered

| Decision | Agreed value / evidence | Owner / date |
|---|---|---|
| Fabrication tool and permitted process | | |
| Executable recipe version, including temperature-evidence plan | | |
| Oxide target and allowable deviation; any departure from paper | | |
| Si orientation, wafer thickness/grade and polished face | | |
| Whole-wafer size or coupon dimensions and tolerances | | |
| Coupon carrier size/material, mounting method and source | | |
| Cutting before/after deposition; operator and surface protection | | |
| Thickness/texture measurement plan and specimen identity | | |
| Thermal provider accepts stack, dimensions and model inputs | | |
| Al transducer and reference owner | | |
| Fabrication slot, measurement receipt cutoff, final report date | | |
| Total commitments, overhead/tax, cancellation terms, stop-work limit | | |

Do not fill unknowns with paper values and call them approved. Save the staff/provider's actual response beside the decision.

## Planned identifiers and roles

| Proposed ID | Role | Actual status / date |
|---|---|---|
| ALN-001-W01 | Parent oxide-coated wafer / substrate lot | Not received |
| ALN-001-W02 | Proposed matching spare research wafer; preserve until needed | Not received |
| ALN-001-R01 | Planned deposition run | Not executed |
| ALN-001-A | Primary coupon: thickness/texture, then Al and thermal testing | Not created |
| ALN-001-B | Same-run AlN-coated companion / reserve, without Al transducer | Not created |
| ALN-001-C | Optional same-run reserve, only if included in scope | Not created |

Record position on the parent wafer and deposition carrier. If a specimen is cut after coating, create child IDs such as ALN-001-A1 and retain the parent link. Never reuse an ID after breakage or replacement. All samples from R01 share one deposition history; they do not constitute independent deposition repeats.

## Substrate receipt and preparation

- Supplier / order / lot / certificate files:
- Receipt date and recipient:
- Actual quantity and dimensions; polished/oxide-bearing side:
- Measured or certified oxide thickness, method, uncertainty/tolerance:
- Silicon thickness, orientation and available doping/resistivity information:
- Package condition / chip or scratch observations / photo paths:
- Storage location and case ID:
- Cutting and cleaning actually performed, operator, date and approved procedure reference:
- Mounting method and carrier ID; any backside contact material:
- Changes from approved specification and disposition:

Photograph packaging and labels at receipt. Open and handle samples only in the appropriate area using the facility's approved method. Keep film surfaces free of unapproved markings/adhesives; identify the external container and position map instead. Any cleaning that changes the intended oxide needs explicit process review.

## Deposition: intended versus observed

| Variable | Agreed setpoint / plan | Observed/logged value | Evidence file or basis |
|---|---|---|---|
| Tool ID / run start and end, with timezone | | | |
| Target material, position and available condition/history | | | |
| Base pressure, with units | | | |
| Ar flow, sccm | | | |
| N2 flow, sccm | | | |
| N2 fraction; definition used | | | |
| Working pressure, mTorr | | | |
| Power and mode; W | | | |
| Target/substrate geometry; cm | | | |
| Rotation/bias | | | |
| Conditioning/pre-sputter and shutter timing | | | |
| Deposition duration; s | | | |
| Heater setting / cooling configuration | | | |
| Sample temperature and measurement/estimate basis | | | |
| Intended / measured film thickness; nm | | | |

Mark unavailable readings as **not recorded**. Absence of heating is not a measured substrate temperature. Record any tool-approved recipe changes with their time and reason; do not silently overwrite the initial plan.

Operator, qualification/first-run support arrangement:

Carrier-position sketch or image path:

Interruptions, alarms, drift, unusual observations, rejected attempts:

Native recipe/log export filenames and any export restrictions:

## Measurement and handoff log

| Date/time | Sample ID | Sender → receiver | Treatment / measurement | Files and fitted-input sources | Condition / remaining sample |
|---|---|---|---|---|---|
| | | | | | |

Planned order: **substrate record → AlN deposition → thickness/texture → approved Al transducer → thermal measurement → interpretation**. Record any changed order. Distinguish primary-sample measurements from companion measurements. Record Al preparation and actual thickness evidence; identify additional layers or treatments if any.

Before dispatch, get the actual receiving address, contact, case/packing instructions, sample intake reference and delivery date. Photograph closed labeled containers, list contents and receive confirmation. Do not assume an office address is the test laboratory.

## End-of-run closeout

- Outcome: valid measured / fabrication-execution failure / measurement failure / inconclusive / not executed.
- Reported quantity, units, conditions and uncertainty interpretation:
- What is directly observed versus inferred or assumed:
- Raw/processed data, model/version, fixed/fitted parameters and residual files:
- Unsuccessful acquisitions retained and exclusion reasons:
- Missing information and its effect on interpretation:
- Next experimental decision this record supports:
- Remaining specimens and storage/return plan:
- Incurred cost, remaining commitments and unused allowance:
- Rights/restrictions for sharing each provider's records:

## Desk rehearsal before the lab visit

Use paper cards or dummy labels, not real wafers: simulate W01 → R01 → A/B → measurements → transfer. Check that every mock file has a specimen ID, units, timestamp and source. Mark all rehearsal files `SYNTHETIC_REHEARSAL`; keep them separate from real records and never report them as data. For the actual cycle, use [the machine-readable record template](run-record-template.json) alongside this human-readable sheet.
