"""English Word Segmentation in Python

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

Copyright (c) 2016 by Grant Jenks

Based on code from the chapter "Natural Language Corpus Data"
from the book "Beautiful Data" (Segaran and Hammerbacher, 2009)
http://oreilly.com/catalog/9780596157111/

Original Copyright (c) 2008-2009 by Peter Norvig

"""

import io
import math
import os.path as op
import sys

ALPHABET = set('abcdefghijklmnopqrstuvwxyz0123456789')
BIGRAMS = None
DATADIR = op.join(op.dirname(op.realpath(__file__)), 'wordsegment_data')
TOTAL = 1024908267229.0
UNIGRAMS = None

def clean(text):
    "Return `text` lower-cased with non-alphanumeric characters removed."
    return ''.join(letter for letter in text.lower() if letter in ALPHABET)

def divide(text, limit=24):
    """Yield `(prefix, suffix)` pairs from `text` with `len(prefix)` not
    exceeding `limit`.

    """
    for pos in range(1, min(len(text), limit) + 1):
        yield (text[:pos], text[pos:])

def load():
    "Load unigram and bigram counts from disk."
    global UNIGRAMS, BIGRAMS  # pylint: disable=global-statement
    UNIGRAMS = parse_file(op.join(DATADIR, 'unigrams.txt'))
    BIGRAMS = parse_file(op.join(DATADIR, 'bigrams.txt'))

def parse_file(filename):
    "Read `filename` and parse tab-separated file of (word, count) pairs."
    with io.open(filename, encoding='utf-8') as reader:
        lines = (line.split('\t') for line in reader)
        return dict((word, float(number)) for word, number in lines)

def score(word, prev=None):
    "Score a `word` in the context of the previous word, `prev`."
    if UNIGRAMS is None and BIGRAMS is None:
        load()

    if prev is None:
        if word in UNIGRAMS:

            # Probability of the given word.

            return UNIGRAMS[word] / TOTAL
        else:
            # Penalize words not found in the unigrams according
            # to their length, a crucial heuristic.

            return 10.0 / (TOTAL * 10 ** len(word))
    else:
        bigram = '{0} {1}'.format(prev, word)

        if bigram in BIGRAMS and prev in UNIGRAMS:

            # Conditional probability of the word given the previous
            # word. The technical name is *stupid backoff* and it's
            # not a probability distribution but it works well in
            # practice.

            return BIGRAMS[bigram] / TOTAL / score(prev)
        else:
            # Fall back to using the unigram probability.

            return score(word)

def segment(text, limit = 400):
    "Return a list of words that is the best segmenation of `text`."

    memo = dict()

    def search(text, prev='<s>'):
        "Return max of candidates matching `text` given previous word, `prev`."
        if text == '':
            return 0.0, []

        def candidates():
            "Generator of (score, words) pairs for all divisions of text."
            for prefix, suffix in divide(text):
                prefix_score = math.log10(score(prefix, prev))

                pair = (suffix, prefix)
                if pair not in memo:
                    memo[pair] = search(suffix, prefix)
                suffix_score, suffix_words = memo[pair]

                yield (prefix_score + suffix_score, [prefix] + suffix_words)

        return max(candidates())

    word_list = list() 
    next_text = clean(text)
    while len(next_text) > limit:
        current_text = next_text[:limit]
        next_text = next_text[limit:]
        _, result_words = search(current_text)
        word_list.extend(result_words)
        # Append last 5 words for resegment 
        # To resolve segmention problem in some cases
        next_text = ''.join([word_list[i] for i in xrange(-5, 0)]) + next_text
        word_list = word_list[:-5]

    _, result_words = search(next_text)
    word_list.extend(result_words)
    return word_list

def main(args=()):
    """Command-line entry-point. Parses `args` into in-file and out-file then
    reads lines from in-file, segments the lines, and writes the result to
    out-file. Input and output default to stdin and stdout respectively.

    """
    import argparse
    import os

    parser = argparse.ArgumentParser(description='English Word Segmentation')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)

    streams = parser.parse_args(args)

    for line in streams.infile:
        streams.outfile.write(' '.join(segment(line)))
        streams.outfile.write(os.linesep)

if __name__ == '__main__':
    main(sys.argv[1:])

__title__ = 'wordsegment'
__version__ = '0.7.3'
__build__ = 0x000703
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 Grant Jenks'
