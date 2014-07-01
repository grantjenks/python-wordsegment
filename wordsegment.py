# -*- coding: utf-8 -*-

"""
English Word Segmentation in Python

Word segmentation is the process of dividing a phrase without spaces back
into its constituent parts. For example, consider a phrase like "thisisatest".
For humans, it's relatively easy to parse. This module makes it easy for
machines too. Use `segment` to parse a phrase into its parts:

>>> from wordsegment import segment
>>> segment('thisisatest')
['this', 'is', 'a', 'test']

In the code, 1024908267229 is the total number of words in the corpus. A
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

import sys
from os.path import join, dirname, realpath
from math import log10
from functools import wraps

if sys.hexversion < 0x03000000:
    range = xrange

def parse_file(filename):
    """Read `filename` and parse tab-separated file of (word, count) pairs."""
    with open(filename) as fptr:
        lines = (line.split('\t') for line in fptr)
        return dict((word, float(number)) for word, number in lines)

unigram_counts = parse_file(join(dirname(realpath(__file__)), 'wordsegment_data', 'unigrams.txt'))
bigram_counts = parse_file(join(dirname(realpath(__file__)), 'wordsegment_data', 'bigrams.txt'))

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

def segment(text):
    """Return a list of words that is the best segmenation of `text`."""

    @memoize
    def search(text, prev='<S>'):
        if text == '':
            return 0.0, []

        def candidates():
            for prefix, suffix in divide(text):
                prefix_score = log10(score(prefix, prev))
                suffix_score, suffix_words = search(suffix, prefix)
                yield (prefix_score + suffix_score, [prefix] + suffix_words)

        return max(candidates())

    result_score, result_words = search(text)

    return result_words

def main(args=''):
    """
    Command-line entry-point. Parses args into in-file and out-file then
    reads lines from infile, segments the lines, and writes the result
    to outfile. Input and output default to stdin and stdout respectively.
    """
    import argparse

    parser = argparse.ArgumentParser(description='English Word Segmentation')
    
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)

    args = parser.parse_args(args)

    for line in args.infile:
        args.outfile.write(' '.join(segment(line)))

if __name__ == '__main__':
    main(sys.argv[1:])

__title__ = 'English Word Segmentation'
__version__ = '0.3'
__build__ = 0x0003
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright (c) 2014 Grant Jenks'
