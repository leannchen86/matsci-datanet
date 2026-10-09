# B001: first thermal-paste practice record

Published with the operator's explicit permission on 9 October 2026. This is a frozen copy of the first learning-only preparation, including the original photographs. It is not a qualified lab-submission sample, thermal-performance result, or held-out model evaluation.

Start with the [execution record](paste-practice/docs/B001-execution-record.v1.json), then the [append-only event log](paste-practice/log.jsonl). The [manifest](manifest.json) lists every copied evidence file and its SHA-256 hash. The snapshot contains 35 log entries and four original photographs, approximately 5.24 MB in total.

| Recorded quantity | Value |
|---|---:|
| Oil additions | 6.718 g |
| Coarse additions | 4.272 + 4.266 + 4.267 = 12.805 g |
| Fine additions | 1.835 + 1.847 + 1.886 = 5.568 g |
| Total weighed inputs | 25.091 g |
| Empty labeled jar, without lid | 204.588 g |
| Final jar plus material, without lid | 229.612 g |
| Derived material remaining with jar | 25.024 g |
| Apparent unaccounted mass | 0.067 g, about 0.27% of inputs |
| Operator's final mixing class | Stiff / hard to spread |

These are reported balance indications and derived arithmetic. Small-mass accuracy was not verified. The apparent discrepancy could include handling residue, vessel/label changes and weighing error; it does not identify lost component masses or verify the paste's retained composition.

Documented deviations include approximately one extra minute of first-round mixing and the final fine-powder addition exceeding its target by 0.056 g. Round-two mixing duration was not explicitly reported. Do not attribute stiffness to a particular deviation from this one run. No density, spread-diameter or thermal-conductivity measurement was made.

The [practice prompt](paste-practice/prompts/B001.v1.txt) and [first model response](paste-practice/raw/B001.inherited.first.md) were recorded before preparation. The inherited model's resolved identifier was not exposed; this response must not be attributed to either named desk-forecast model. The preparation differs from the planned prompt in documented ways. This single observation is not a model-quality score or evidence of training-data value.

Photographs, unchanged from the supplied files:

- [Intermediate, after round-two addition instructions](paste-practice/raw/B001.round2.intermediate.01.jpg)
- [After the reported final four-minute mix](paste-practice/raw/B001.after-final-mix.01.jpg)
- [After the rest/lift instructions, labeled jar](paste-practice/raw/B001.post-rest.01.jpg)
- [After the rest/lift instructions, top view](paste-practice/raw/B001.post-rest.02.jpg)

No EXIF GPS IFD or XMP location payload was found in these four images. Image bytes were preserved. Historical entries that say records were private describe their status before publication; entry 34 records the operator's subsequent release permission. Original entries and attachments were not rewritten.

Verify from the repository root:

```sh
python3 trajectory/traj.py --root trajectory/releases/B001 verify paste-practice
```

The included timestamp receipt for the earlier preparation anchor initially contained pending calendar attestations, not verified Bitcoin anchoring. Publication of this release does not change that verification status. Later observations should receive new log entries and a new release; do not overwrite this snapshot.

Storage and next-run recommendations are in log entry 35 and the [working checklist](../../../outputs/thermal-paste-first-cycle/CHECKLIST.md). They are recommendations, not confirmation that storage, cleanup or another experiment happened.
