# B001 process-review addendum — 9 October 2026

This release preserves the operator's post-run feedback, the assistant's review, and the decision to rehearse the equipment and revise the run card before another powder batch. It contains no new measurement or completed rehearsal. The operator had already raised the residue concern during B001 (original entry 23); the combined-weighing/compensation proposal is subsequent feedback.

- [Review as recorded](paste-practice/docs/B001-process-review.v1.md)
- [Original entries 36–38](paste-practice/log-addendum.jsonl)
- [Manifest and file hashes](manifest.json)
- [Unchanged original B001 release, entries 1–35](../B001/README.md)
- [Current checklist](../../../outputs/thermal-paste-first-cycle/CHECKLIST.md)

The addendum is a byte-identical suffix of the working campaign log. Entry 36 chains to the original release's entry-35 head. Existing photographs and files are referenced through the base release instead of duplicated. The new attached review is immutable here; later changes require a new entry/version.

To verify the complete campaign, copy the base release's `paste-practice` directory into a temporary root, copy this addendum's `docs` into that campaign's `docs`, append `log-addendum.jsonl` to the copied `log.jsonl`, then run `python3 trajectory/traj.py --root <temporary-root> verify paste-practice`. Do not append into the original release. The partial addendum alone is not a standalone campaign. Check both manifests for their listed byte sizes and SHA-256 values.

These are retrospective records. The earlier forecast and timestamp receipts remain unchanged; this review is not a preregistered prediction.
