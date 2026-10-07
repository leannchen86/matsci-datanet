# What one record contains

Written 6 October 2026, before any batch exists. Sizes and minutes are estimates, to be replaced by measured ones after the first three batches.

The aim is a record that is small but complete: every part a company's batch record or a good public provenance format would have, present in miniature, plus the parts neither of those keeps.

## Format

A handful of folders, not a table.

- `campaigns/registry/`: one log holding a note for every container of material, every piece of bench equipment, every calibration and every version of the method.
- `campaigns/<name>/` for each campaign (practice, pilot, main, each goal-seeking campaign): one append-only `log.jsonl`, one JSON object per line, each carrying the hash of the line before it; and `raw/`, `docs/` and `prompts/` folders of untouched files, each pinned in the log by its hash.
- `anchors.log`: one line per anchor, pushed publicly and timestamped.

Tables for people who only want rows are rebuilt from the logs by script, never typed by hand. The file formats are deliberately ordinary.

## Expected size

| Stage | Batches | Sessions | Log entries | Files | Lab-measured specimens | Disk |
|---|---|---|---|---|---|---|
| First lab submission | about 3 | 2 | about 105 | about 35 | 3 | about 0.1 GB |
| First gate | about 35 | 8 | about 440 | about 135 | 6 to 7 | 0.3 to 0.5 GB |
| End of the six-week cycle | about 144 | about 28 | about 1,600 | several hundred | 12 to 20 | a few GB |

## What is new, and what is not

**Not new.** The lineage structure is borrowed, on purpose: the plan-versus-action split is the "spec versus run" of GEMD (Citrine's open materials data model); sample and container ids with parent links follow ESAMP (Caltech's sample-event database, released with about 30 million sample-process events); lots, equipment, actual weights and yield are what a regulated batch record requires. The idea of the experimental trajectory as a kind of record was named in a 2026 preprint. The file formats, the hash chain and the science are all ordinary.

**New, as far as the search found.** One record per physical batch that holds all of these together, in an order an outsider can check:

- a numeric prediction by a named model, fixed before the outcome, made once without and once with the history;
- what was planned against what was actually done, with lots and instrument state actually filled in (public formats have these fields; released data mostly leaves them empty);
- failures and excluded readings as countable fields with a cause;
- the decision that followed, its alternatives and the runs it rested on;
- the minutes and dollars it cost;
- every change to the method, with the reason and the batches made before and after;
- a beginner's learning curve, since every batch from the first practice one is kept.

"As far as the search found" means not found in the schemas and datasets that were opened, not proven absent. The nearest neighbour to check before telling anyone this is unique: a 2026 self-driving-lab paper in which a language model reasons over 352 physically made samples, with a public archive (<https://zenodo.org/records/19396297>).

## The twelve parts

| # | Part | Where it goes | Today |
|---|---|---|---|
| 1 | Goal, requirements, gate thresholds | A `goal` entry with the thresholds as fields; each gate is a `decision` with `_kind=gate` | Small change |
| 2 | Material lots | Registry `note` with `_kind=lot` per container: seller, manufacturer, product, lot or "none given", received, opened, storage, density used; data sheet and label photo attached | New |
| 3 | Equipment, calibration, session checks | Registry notes `_kind=equipment` and `_kind=calibration`; each session opens with a `_kind=session_start` note (balance check readings, room temperature, humidity) and a reference-paste run | New |
| 4 | Method version and changes | The method file copied into the registry as `BP-v1`, `BP-v2`...; `protocol=BP-v1` as a plain setting on every plan; each change is a note with the reason and the batches before and after | New |
| 5 | Recipe as intended, batch as made | `plan` holds targets; `action` holds actual masses, lots used, times, deviations. A hand-filled [batch sheet](batch-sheet.md) is the original, photographed and attached | Small change |
| 6 | Sample identity, mass ledger, custody | Ids for batch and every container; where every gram went; who received what and when | New |
| 7 | Raw readings and how numbers are derived | Every individual reading as a list field, the photos, the rule that reduces them; the lab's files unchanged | Small change |
| 8 | Prediction before the outcome | Two `prediction` entries with the numbers as fields and the exact prompt attached; see [prompt-preamble.md](prompt-preamble.md) | Small change |
| 9 | Outcome status, failure cause, disposition | Fields on the observation: `_status`, `_cause`, `_effect`, `_disposition`, `_excluded` | Small change |
| 10 | Decisions and dead ends | `decision` with `_options`, `_chosen`, `_based_on`, `_leads_to`, `_followed_ai`; only where there was a real choice or a surprise | Small change |
| 11 | Cost and time | Clock times on the batch sheet; a weekly `_kind=cost` note; lab fee and turnaround on the lab result | New |
| 12 | Order, attribution, rights, backup | The hash chain; `--author human:<initials>`; anchor, push and outside timestamp; a second copy | Small change |

## Ids

Fixed before the first entry, because an append-only log cannot rename them.

- Sessions: `S01`, `S02`...
- Batches: `B001`, `B002`... on one counter across practice, pilot and main. Never reused. The batch id is the run id for its same-day home measurements.
- Containers filled from a batch: `B001-L1` (for a lab), `B001-A1` (archive).
- Any later measurement of a container gets its own run id: `B001-L1-M1`, `B001-L1-M2`.
- After the pilot: every titration cup and every small batch for vials takes the next batch id on the same counter. Vials filled from a batch are `B041-V1`, `B041-V2`. Each titration step is an `observation` entry under its cup's id.
- Forecasts taken once for a condition are `prediction` entries under a run id for that condition, for example `E2-X30`. Each cup then starts with one `prediction` entry under its own id carrying `_forecast_run=E2-X30`.
- Reference paste containers: `REF-L1`, `REF-L2`, with `_parent=LOT-REF-1`.
- Lots: `LOT-OIL-1`, `LOT-COARSE-1`, `LOT-FINE-1`, `LOT-REF-1`. Equipment: `BAL-1`, `MEAS-1`, `PLATES-1`...

## Rules that cannot be fixed afterwards

1. Supplier lot, serial and model numbers are written JSON-quoted (`--data supplier_lot='"20260"'`) so they are stored as text.
2. Times typed by hand always carry the offset: `2026-10-08T14:03-07:00`.
3. A label that was not measured is written as `null`, never left out.
4. Reference-paste runs carry underscore keys only, so the tool does not count them as recipe repeats.
5. Phone camera: location tagging off, one photo format chosen once, files never edited after logging.
6. Models: first reply only, never regenerate; memory and web search off; both prompt files saved.
7. After every push of `anchors.log`, timestamp that file with an outside service (for example opentimestamps.org) and keep the receipt beside it. A git commit date can be set by the committer; an outside timestamp cannot.

## Left out on purpose

A second person's check of each step. Separate records for each density fill. A photo of the balance at every weighing and a video of every mix (one photo of the mixed paste is kept as the evidence for its class). A third model on every run. Exporters to other formats, until someone outside asks for one. Full names, addresses, receipts and private messages.

One limit to state in any release: one person made and measured everything, so operator-to-operator scatter cannot be estimated.

## Cost of keeping this up

About 3 hours of one-off set-up, and by a reviewer's estimate 15 to 20 minutes per batch in the first weeks. If it slows bench work, cut in this order: timer laps (keep clock times), repeated session constants (put them once on the session-start note), and decisions or interpretations on scheduled runs where nothing surprising happened.
