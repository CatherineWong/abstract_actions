"""
Coalesce verb lists across corpora of early acquired/produced/comprehended verbs.
Alphabetized and marked by which list they appear on (and how many words were in that as a whole.
"""
import os
from collections import defaultdict

if __name__ == "__main__":
	corpora = [f for f in os.listdir('.') if f.endswith('.txt')]
	verbs = defaultdict(lambda: [0] * len(corpora))
	for i, corpus in enumerate(corpora):
		with open(corpus) as f:
			lines = [l.strip() for l in f.readlines()]
		for w in lines:
			verbs[w][i] = 1

	print("\t".join(['stem'] + corpora))
	for w in sorted(list(verbs.keys()), key=lambda k: sum(verbs[k]), reverse=True):
		print('\t'.join([w] + [str(i) for i in verbs[w]]))