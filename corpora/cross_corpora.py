"""
Coalesce verb lists across corpora of early acquired/produced/comprehended verbs.
Alphabetized and marked by which list they appear on (and how many words were in that as a whole.
"""
import os
from collections import defaultdict

if __name__ == "__main__":
	corpora = [f for f in os.listdir('.') if f.endswith('.txt')]
	verbs = defaultdict(lambda: [0] * len(corpora))

	stems = defaultdict(list)
	for i, corpus in enumerate(corpora):
		with open(corpus) as f:
			lines = [l.strip() for l in f.readlines()]
		for w in lines:
			stem = w.split()[0]
			if len(w.split()) > 1:
				stems[stem].append(' '.join(w.split()[1:]))
			verbs[stem][i] = 1

	print("\t".join(['stem'] + corpora))
	for stem in sorted(list(verbs.keys()), key=lambda k: (-sum(verbs[k]), k)):
		w = stem
		if stem in stems.keys():
			w = "%s (%s)" % (stem, ','.join(set(stems[stem])))
		print('\t'.join([w] + [str(i) for i in verbs[stem]]))