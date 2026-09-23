# v5b: fixes from the two-agent check of the v5 text
import sys
P = sys.argv[1]
s = open(P, encoding='utf-8').read()

def rep(old, new_, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:80])
    s = s.replace(old, new_)

LEN = 'ignore hydrogen the reference file never located (X-rays barely see hydrogen), then same elements with atom fractions within 0.04 for two-element compounds and 0.10 for others, phases matched one-to-one'

# 1 lenient rule, three places
rep('and the sameness rule (strict = formula text equal; lenient = atom fractions within 0.10). Copied from your frozen plan and the Dara paper, not invented.',
    'and the sameness rule (strict = reduced formulas equal; lenient = ' + LEN + '). Copy the exact wording from your frozen plan and the Dara paper on day 1; invent nothing.')
rep('Strict = the formula text must match exactly. Lenient = atom fractions within 0.10 (sum of absolute differences).',
    'Strict = the reduced formulas must be equal. Lenient = ' + LEN + ' (distance = sum of absolute differences).')
rep('Strict = formula text must match exactly. Lenient = atom fractions within 0.10.',
    'Strict = reduced formulas must be equal. Lenient = ignore unlocated hydrogen, then atom fractions within 0.04 (two-element compounds) or 0.10 (others).')

# 2 in-sample line becomes conditional
rep('The lenient rule was adjusted after seeing these scans (a hydrogen rule moved the pilot from 0.545 to 0.745), so its score here is in-sample.',
    'The lenient rule gained its hydrogen clause after pilot results were seen (the pilot score moved from 0.545 to 0.745). If that pilot includes these 40 scans, the lenient score here is in-sample; the first-hour overlap check confirms or removes this line.')
rep('and whether the hydrogen rule was added before or after', 'and whether the lenient rule’s hydrogen clause was added before or after')

# 3 the 6% figure
rep('The published between-lab figure (about 6%, eight labs, one specimen) goes on as a labelled outside reference line, not a rung.',
    'The published between-lab figure goes on as a labelled outside reference line, not a rung: about 6% standard uncertainty (eight labs, one specimen), roughly 5.7% as a median pairwise difference. The reviewers saw it as a search snippet only; open the paper before quoting it.')
rep('a formula alone does not fix the sample (about 6% between labs on one specimen, 32.7% across papers).',
    'a formula alone does not pin down the sample. Two samples with the same formula can measure very differently: about 6% spread between labs on one specimen, against a 32.7% median gap across papers (different statistics, shown only for scale).')
rep('The task may be ill-posed, not only too easy: a formula alone does not fix the sample.',
    'The task may be ill-posed, not only too easy: a formula alone does not pin down the sample.')

# 4 is it eval work: two thirds, and what it does not cover
rep('<b>Yes, this is evaluation work.</b> More exactly: checking the exams before trusting the scores. ML calls it benchmark auditing; measurement labs call it method validation. Every item below except the file rescue is a form of it. Test data is curated data, so this still sits inside your aim of better experimental data. Only the partner-lab item builds a new exam.',
    '<b>Yes, mostly.</b> About two thirds of the items check an exam: its metric, answer key, split or error bars. ML calls that benchmark auditing; measurement labs call it method validation. The rest is data-error reporting and file housekeeping, which one skeptic counts too (as label-noise and contamination checks). It fits the “fair exam” half of the picture in section 01. It does not cover the collecting half, and month one produces fixes for your own project, not something a stranger can load. Weigh that at the week-2 sitting. Only the partner-lab item builds a new exam.')

# 5-6, 8 verdict paragraph and trust row
rep('<b style="color:var(--ink)">All eight say: go ahead with the 40-row test, after about one hour of writing.</b>',
    '<b style="color:var(--ink)">All eight say: go ahead with the 40-row test.</b> The skeptics put the writing needed first at about one hour (one reviewer had asked for 2–3).')
rep('They read the plan and notes plus about 50 outside sources, some only as search snippets, and never opened your project folders.',
    'They read the plan and notes plus about 40 outside sources (51 source checks counting repeats): about 8 were never opened, several more were seen only as search snippets, and 4 turned out to be misdescribed. They never opened your project folders.')
rep('several outside figures the reviewers saw only as search snippets. The reviewers called this the last check before the test starts.',
    'the extra bismuth carbonate phase in the Dara paper (one reviewer’s reading through a summarising tool); several outside figures seen only as search snippets. None of these blocks the test. The skeptics said this eval check should be the last one before it starts: no further review round.')

# 7 second sheet
rep('Hand-sort the 18 rule-dependent rows among the 210 pilot rows with the same four bins, after checking they are not the same 40 scans. It covers',
    'Hand-sort the rule-dependent pilot rows that are not among the 40 scans, with the same four bins. The 210 pilot rows appear to include those 40, so expect roughly 13 of the 18 to be new; confirm the count on disk. It covers')

# 9 scorer hedge
rep('and the Dara paper states no sameness rule and ships no scorer.',
    'the Dara paper states no sameness rule, and no scorer was seen in its public code (a look by file name, not an exhaustive search).')

# 10 weighed key wording
rep('Truth comes from the scale, not an analyst: known to within', 'Truth starts from the scale rather than from an analyst’s reading: known to within')
rep('<td>The only annotator-free ground truth</td>', '<td>Labels from the recipe, not from annotators. Still noisy, and people still choose which reference entry counts as each ingredient</td>')
rep('The answer comes from a balance plus a purity check, not from an analyst.', 'The answer starts from a balance plus a purity check, rather than from an analyst’s reading.')

# 11 bismuth carbonate hedge
rep('The Dara paper itself reports a real extra phase (a bismuth carbonate) in one of the 20 mixtures and left it out of scoring.',
    'As one reviewer read the Dara paper (through a summarising tool, so re-check the wording on day 1), one of the 20 mixtures shows a real extra phase, a bismuth carbonate, which the authors left out of scoring.')
rep('(the rows holding both Bi2O3 and Li2CO3).', '(the rows holding both Bi2O3 and Li2CO3), once the paper’s wording is re-checked.')

# 12 K gating
rep('Only if the 40-row test clears your threshold K. Default size is a fix inside your project (days); the reusable 2–3 week version also waits for one specialist’s reply. Returns a tier',
    'A fix inside your own project (days) happens either way. The reusable 2–3 week version is built only if the 40-row test clears your threshold K and one specialist has replied. Returns a tier')
rep('It decides only whether the 2–3 week marker gets built.', 'It decides only whether the 2–3 week marker can be built; that build also waits for a specialist’s reply.')

# 13 glosses
rep('tiny amounts, a weak scatterer beside a strong one, overlapping or same-structure pairs, poorly crystalline material, short scans.',
    'tiny amounts; a compound that barely shows up in X-rays next to one that shows strongly; compounds whose peaks overlap or that share a crystal structure; powders whose crystals are poorly formed, so peaks are broad and faint; short scans.')
rep('for phase-naming software on synthesis-type chemistry.',
    'for phase-naming software on the kinds of inorganic compounds synthesis labs make (the one standing contest is on clay minerals).', count=2)
rep('All X-ray rows are fixed scans from one instrument,', 'All X-ray rows are stored scans from one instrument, not re-measured,')

# 14-15
rep('Both scorers call it by default.', 'The 40-row table script and the thermoelectric split script call it by default. Your project’s own marker is not touched.')
rep('Known statistics (Miller 2024, “Adding error bars to evals”)', 'Known statistics (a 2024 paper, “Adding error bars to evals”)')

open(P, 'w', encoding='utf-8').write(s)
print('v5b ok', len(s), 'em-dashes', s.count('—'))
