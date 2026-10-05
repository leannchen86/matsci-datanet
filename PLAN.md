# Plan

Updated 5 October 2026. This is the one live plan. [outputs/aln-first-cycle-preparation/](outputs/aln-first-cycle-preparation/README.md) is background: it was written for a single careful run at a different budget and is paused, not deleted.

## Decided

- **Goal.** Produce experimental materials data that people who train models would actually want: complete, checkable, with the failures left in.
- **Unit of data.** A trajectory, not a row: goal, plan, what was done, raw readings, interpretation, next decision, dead ends. Format and rules are in [trajectory/](trajectory/README.md).
- **Expert.** For now an AI model is the expert. It writes a prediction before every run; the measured outcome scores it. A human expert comes later, when there is money and time.
- **Method.** By hand, full time. Speed and learning come before automation or scale.
- **Budget.** About $15,000 for this first step.
- **Release.** The first dataset is given away to test demand. What is public and what is held back gets decided before anything is released, because public data cannot later serve as a hidden test.

## Open: the first target

A comparison of about a dozen candidate first targets is running. The result and the six-week plan will be written here. Criteria:

1. Decision cycles per week (make, measure, decide, repeat). More is better.
2. Cost per independent result, inside the budget.
3. Access without an institution behind us.
4. Relevance to heat removal in stacked chips and advanced packaging.
5. How much a failed run teaches.

The paused plan (one sputtered AlN film, thermal measurement by an outside lab) scores poorly on 1 to 3: one result per multi-week cycle, and about ten onboarding steps before the first film.

## Do now (does not depend on the target)

| # | Action | Done when |
|---|---|---|
| 1 | Answer the three source checks in [human-review.md](outputs/aln-public-record-audit/human-review.md) | A, B and C each marked supported, needs correction or unsure |
| 2 | Ask each scientist contact three questions: what prediction they wish their model could make; what each record would need to contain; how they would know the model got better | Answers written down, kept out of this public repository |
| 3 | Rehearse the loop once with `trajectory/traj.py` on any quick measurement, marked as a rehearsal | `verify` passes with a prediction logged before the outcome |
| 4 | Transcribe the tables of Perez et al. (ACS Nano 2023) and run the 16 frozen audit questions on them as a positive control | Counts recorded next to the Stanford/TSMC result |
| 5 | Decide whether this repository stays public, and review the two untracked folders under `outputs/` before committing them | Decision written here |

## Weekly review

Every Monday, five numbers: runs completed, runs with a prediction logged before the outcome, exact repeats, dollars spent, and reactions from anyone outside the project.
