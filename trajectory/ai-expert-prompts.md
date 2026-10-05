# Prompts for the AI expert

For now an AI model plays the expert. Use the same two prompts every time so the predictions are comparable, and save each reply verbatim with the model name and version. Asking two different models is better than one: where they disagree is where a run teaches the most.

A model's reasoning is not the valuable part of the record. The valuable parts are what was physically done, the raw result, and the measured gap between what the model expected and what happened.

## 1. Before the run: two predictions, cold and warm

Ask twice, in two fresh conversations, with the same prompt:

- **Cold:** leave the campaign log out and write "none" in its place. The model sees only the planned run.
- **Warm:** paste the output of `traj.py show <campaign> --hide-test`. Do not include anything from the run being predicted.

**Held-back outcomes never go to a model.** Anything pasted into a model may end up in training data, and a leaked answer cannot be un-leaked. Mark every held-back run with `--data _split=test` on its plan entry and always use `--hide-test` when building a prompt. For the same reason, do not ask a model to interpret a held-back run; write that interpretation yourself.

Warm error minus cold error, on runs from sessions the log does not yet contain, is the measured value of the trajectory. If warm is no better than cold, the history is not helping and that is a finding. Score exact repeats separately: on a repeat the warm model has already seen the answer.

Log each with `--data _context=cold` or `--data _context=warm`.

```text
You are acting as an experienced experimentalist advising on the next run of a hands-on materials experiment.

Campaign log so far:
<paste the log>

Planned next run:
<paste the plan entry>

Answer in this exact structure. Be specific and commit to numbers.
1. Predicted outcome: the value you expect for each quantity that will be measured, with units and an 80% interval.
2. Reasoning: the mechanism behind the prediction, in at most six sentences.
3. Most likely ways this run fails or misleads, ranked, with a rough probability for each.
4. What you would do instead of this run, if anything, and why.
5. What result would most change your mind about how this system behaves.
6. Safety or handling points the operator should check with the safety data sheet or facility staff. You are not the safety authority.
Do not hedge beyond the intervals you give.
```

Log it with `traj.py add <campaign> prediction --run <id> --author ai:<model>`.

## 2. After the run: interpretation

```text
You are reviewing the result of a run you did not see beforehand.

Campaign log so far, including the prediction made before this run:
<paste the log>

Result of the run:
<paste the action and observation entries>

Answer in this exact structure.
1. Was the prediction right? State for each quantity whether the result fell inside the 80% interval.
2. If the run failed, classify the cause as process, measurement, handling, equipment or unknown, and say what evidence would confirm it.
3. What this result does and does not show. Name the single most likely alternative explanation.
4. The next run you would do and what it would distinguish between.
5. Anything in the record that is missing and would be needed to trust this result.
```

Log it with `traj.py add <campaign> interpretation --run <id> --author ai:<model>`, then write your own `decision` entry. The decision is yours: say where you followed the model and where you did not.
