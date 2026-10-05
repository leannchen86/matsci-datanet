# Plan

Updated 5 October 2026. This is the one live plan. [outputs/aln-first-cycle-preparation/](outputs/aln-first-cycle-preparation/README.md) is background: it was written for a single careful run at a different budget and is paused, not deleted.

## Decided

- **Goal.** Produce experimental materials data that people who train models would actually want: complete, checkable, with the failures left in.
- **Unit of data.** A trajectory, not a row: goal, plan, what was done, raw readings, interpretation, next decision, dead ends. Format and rules are in [trajectory/](trajectory/README.md). That a trajectory is worth more than the row is a hypothesis, not a result: the earlier `materials-event-modeling` project tested it three times on public data and it did not survive a held-out batch. Every run here tests it again with a cold and a warm prediction.
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
| 1 | Rehearse the loop with `trajectory/traj.py` on any quick physical measurement (kitchen scale, multimeter), three runs across two sessions, marked as a rehearsal | `verify` passes: predictions logged first, one repeat in a different session |
| 2 | Decide whether this repository stays public, and review the two untracked folders under `outputs/` before committing them | Decision written here |
| 3 | Show scientist contacts one concrete task card (input, output, metric) for the chosen target and ask what number would change what they do | Answers written down, kept out of this public repository |
| 4 | Answer the three source checks in [human-review.md](outputs/aln-public-record-audit/human-review.md) | A, B and C each marked supported, needs correction or unsure |

The rehearsal is first on purpose. The earlier project spent four months on tooling and documents without one physical measurement; the first real record matters more than any further desk work. Transcribing more published tables is dropped for the same reason.

## Weekly review

Every Monday, seven numbers: runs completed, independent sessions, runs with a prediction logged before the outcome, exact repeats in a different session, spread between those repeats, dollars spent, and reactions from anyone outside the project. Runs completed is the one that must go up.
