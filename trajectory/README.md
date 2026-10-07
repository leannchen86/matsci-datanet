# Trajectory log

**What every record must contain, the ids, and the rules that cannot be fixed afterwards are in [RECORD.md](RECORD.md).** The printable [batch sheet](batch-sheet.md) is the original record at the bench, and [prompt-preamble.md](prompt-preamble.md) is pasted into every per-batch prediction prompt (not the desk-test prompts, which are sent alone).

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
6. **Repeat on purpose, on a different day.** At least one run in five repeats an earlier condition exactly, with freshly prepared material in a different session. A same-day repeat only measures the instrument and understates the real noise several-fold.
7. **Measure something known, and make something known.** Each session measures a reference with a published value (checks the instrument) and makes one fixed control recipe fresh (measures day-to-day drift in the process).
8. **AI is the expert for now, not the safety authority.** Safety comes from the safety data sheet and the people who run the facility or sell the material. No AI prediction is a reason to skip either.
9. **Record settings and context as fields, not prose.** Put every setting on the plan entry with `--data key=value`. Context keys start with an underscore: `_session` (one bath make-up, one mixing batch, one day), `_lot`, `_chosen_by` (`schedule`, `human` or `ai`), `_status` on outcomes (`observed`, `out_of_range`, `not_measured`, `failed`). Free text cannot be counted, compared or scored.
10. **A redo is a new run.** Never reuse a run id. Give the retry its own id and `--data _retry_of=R07`; the original stays in the log.
11. **Two kinds of run, never mixed.** Exploration runs are chosen as you go. Evaluation runs come from a randomised schedule written and anchored before the first of them is made. Only evaluation runs may be scored or released as a test.
12. **Split by session, never by row.** Anything held back is held back as whole sessions. Count independent sessions and conditions, not records.
13. **Held-back outcomes never go to a model.** Mark held-back runs with `--data _split=test` on the plan entry and build every prompt with `show --hide-test`. A leaked answer cannot be un-leaked.

## What makes a score believable

- Every score is reported next to cheap baselines: the mean so far, the nearest earlier run, and a guess from run order alone.
- The task, the metric and how the scored number is computed from the raw file are fixed and anchored before the first evaluation run.
- A value that could not be measured is not a failure, and a failure is not a zero.
- Each run carries two model predictions, one made without the campaign history and one made with it. The difference shows how much the trajectory helps a model.

## Signal-to-noise checklist for one run (v0)

- [ ] Plan and both predictions (cold and warm) were logged before the run.
- [ ] Every setting is on the plan entry as a `--data` field, including the ones left alone, with `_session` and `_chosen_by`.
- [ ] Raw files are attached, not just the number read off them.
- [ ] The reference measured in the same session is within its expected range.
- [ ] If the run failed, the cause class is stated.
- [ ] The decision that followed is logged, with the reason.

## Commands

```sh
python3 trajectory/traj.py init <campaign> --text "the goal"
python3 trajectory/traj.py add <campaign> plan --run R01 --text "..." \
    --data additive_ppm=20 --data current_A=2 --data _session=S03 --data _chosen_by=schedule
python3 trajectory/traj.py add <campaign> prediction --run R01 --author ai:<model> < prediction.md
python3 trajectory/traj.py add <campaign> action --run R01 --text "..."
python3 trajectory/traj.py add <campaign> observation --run R01 --file raw/R01.csv --text "..."
python3 trajectory/traj.py add <campaign> interpretation --run R01 --author ai:<model> < interpretation.md
python3 trajectory/traj.py add <campaign> decision --text "..."
python3 trajectory/traj.py verify <campaign>
python3 trajectory/traj.py show <campaign> --run R01
python3 trajectory/traj.py anchor <campaign>
```

`verify` checks the chain, the attached files, how many runs had a prediction logged before the outcome, and how many exact repeats exist and how many of those crossed a session. `--at` records when something actually happened if you are logging it late. `--answers raw/reply.md` reads the `ANSWER` lines of a saved model reply into fields, so forecast numbers are not retyped.

## What is public and what is not

This repository is public. `trajectory/campaigns/` is ignored by Git, so real records stay on this machine until we decide what to release and what to hold back. `anchor` writes only the latest hash to `trajectory/anchors.log`; committing and pushing that file gives a public timestamp proving the predictions existed before the outcomes, without revealing either. Git-ignoring is not a backup: copy `campaigns/` somewhere else as well.
