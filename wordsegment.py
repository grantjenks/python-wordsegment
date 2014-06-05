"""
# English Word Segmentation in Python

The number 1024908267229 is the total number of words in the corpus. A
subset of this corpus is found in unigrams.txt and bigrams.txt which
should accompany this file. A copy of these files may be found at
http://norvig.com/ngrams/ under the names count_1w.txt and count_2w.txt
respectively.

# Copyright (c) 2014 by Grant Jenks

Based on code from the chapter "Natural Language Corpus Data"
from the book "Beautiful Data" (Segaran and Hammerbacher, 2009)
http://oreilly.com/catalog/9780596157111/

Original Copyright (c) 2008-2009 by Peter Norvig
"""

from math import log10
from functools import wraps

from sys import hexversion

if hexversion < 0x03000000:
    range = xrange

def parse_file(filename):
    """Read `filename` and parse tab-separated file of (word, count) pairs."""
    with open(filename) as fptr:
        lines = (line.split('\t') for line in fptr)
        return dict((word, float(number)) for word, number in lines)

unigram_counts = parse_file('unigrams.txt')
bigram_counts = parse_file('bigrams.txt')

def memoize(func):
    """Memoize arguments to function `func`."""
    cache = dict()
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def divide(text, limit=24):
    """
    Yield (prefix, suffix) pairs from text with len(prefix) not
    exceeding `limit`.
    """
    for pos in range(1, min(len(text), limit) + 1):
        yield (text[:pos], text[pos:])

def score(word, prev=None):
    """Score a `word` in the context of the previous word, `prev`."""

    if prev is None:
        if word in unigram_counts:

            # Probability of the given word.

            return unigram_counts[word] / 1024908267229.0
        else:
            # Penalize words not found in the unigrams according
            # to their length, a crucial heuristic.

            return 10.0 / (1024908267229.0 * 10 ** len(word))
    else:
        bigram = '{0} {1}'.format(prev, word)

        if bigram in bigram_counts and prev in unigram_counts:

            # Conditional probability of the word given the previous
            # word. The technical name is *stupid backoff* and it's
            # not a probability distribution but it works well in
            # practice.

            return bigram_counts[bigram] / 1024908267229.0 / score(prev)
        else:
            # Fall back to using the unigram probability.

            return score(word)

@memoize
def segment(text, prev='<S>'): 
    """
    Return (score, words) where words is the best
    segmentation of `text`.
    """
    if text is '':
        return 0.0, []

    def candidates():
        for prefix, suffix in divide(text):
            prefix_score = log10(score(prefix, prev))
            suffix_score, suffix_words = segment(suffix, prefix)
            yield (prefix_score + suffix_score, [prefix] + suffix_words)

    return max(candidates())

if __name__ == '__main__':
    import IPython
    IPython.embed()
