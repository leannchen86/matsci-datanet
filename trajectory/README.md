# Trajectory log

The unit of data in this project is a **trajectory**, not a row of numbers: a goal pursued through many runs, with the plan, what was actually done, the raw readings, the interpretation, the next decision and the dead ends, each written down at the time.

`traj.py` keeps that record honest. It is an append-only log in which every entry carries the hash of the one before it, so nobody, including us, can later reorder or rewrite what was predicted and what was found. It uses only the Python standard library.

Status: v0, built 5 October 2026 before the first target is chosen. Expect the entry types and the checklist to change after the first real campaign.

## The loop for every run

| Step | Entry type | Written by | What goes in |
|---|---|---|---|
| 1 | `plan` | you | What you will do in this run and why, in a few sentences |
| 2 | `prediction` | AI expert | The expected outcome with numbers, before the run exists. See [ai-expert-prompts.md](ai-expert-prompts.md) |
| 3 | `action` | you | What was actually done, including every deviation from the plan |
| 4 | `observation` | you | The raw readings, with the raw files attached |
| 5 | `interpretation` | AI expert and you | What the result means and how it compares with the prediction |
| 6 | `decision` or `deadend` | you | What happens next and why, or why this line stops |

Use `note` for anything else, including corrections to earlier entries.

## Rules

1. **Write it when it happens.** An entry written the next day is hindsight. If that is unavoidable, say so in the entry.
2. **Prediction before outcome.** The tool refuses an `observation` for a run with no `prediction`, and refuses a `prediction` after the outcome exists. `--force` records the entry and flags it permanently.
3. **Never edit.** A mistake is corrected with a new `note` entry. Raw files go in the campaign's `raw/` folder and are not touched after logging; `verify` detects any change.
4. **Save AI output verbatim**, with the model name and version as the author (`--author ai:<model>`). Do not tidy it.
5. **Every failure gets a cause.** Start the entry with one of: `process` (the conditions produced a bad result: informative), `measurement`, `handling`, `equipment`, `unknown`. Only `process` failures teach anything about the material; the rest measure how noisy we are.
6. **Repeat on purpose.** At least one run in five repeats an earlier condition exactly. Without repeats the noise is unknown and no single result means anything.
7. **Measure something known.** Each measurement session includes a reference with a published value, so a wrong instrument or method shows up as a wrong reference.
8. **AI is the expert for now, not the safety authority.** Safety comes from the safety data sheet and the people who run the facility or sell the material. No AI prediction is a reason to skip either.

## Signal-to-noise checklist for one run (v0)

- [ ] Plan and prediction were logged before the run.
- [ ] Every setting that could be changed is recorded, including the ones left alone.
- [ ] Raw files are attached, not just the number read off them.
- [ ] The reference measured in the same session is within its expected range.
- [ ] If the run failed, the cause class is stated.
- [ ] The decision that followed is logged, with the reason.

## Commands

```sh
python3 trajectory/traj.py init <campaign> --text "the goal"
python3 trajectory/traj.py add <campaign> plan --run R01 --text "..."
python3 trajectory/traj.py add <campaign> prediction --run R01 --author ai:<model> < prediction.md
python3 trajectory/traj.py add <campaign> action --run R01 --text "..."
python3 trajectory/traj.py add <campaign> observation --run R01 --file raw/R01.csv --text "..."
python3 trajectory/traj.py add <campaign> interpretation --run R01 --author ai:<model> < interpretation.md
python3 trajectory/traj.py add <campaign> decision --text "..."
python3 trajectory/traj.py verify <campaign>
python3 trajectory/traj.py show <campaign> --run R01
python3 trajectory/traj.py anchor <campaign>
```

`verify` checks the chain, the attached files, and how many runs had a prediction logged before the outcome.

## What is public and what is not

This repository is public. `trajectory/campaigns/` is ignored by Git, so real records stay on this machine until we decide what to release and what to hold back. `anchor` writes only the latest hash to `trajectory/anchors.log`; committing and pushing that file gives a public timestamp proving the predictions existed before the outcomes, without revealing either. Git-ignoring is not a backup: copy `campaigns/` somewhere else as well.
