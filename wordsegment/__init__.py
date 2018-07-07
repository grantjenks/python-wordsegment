"""English Word Segmentation in Python

Word segmentation is the process of dividing a phrase without spaces back
into its constituent parts. For example, consider a phrase like "thisisatest".
For humans, it's relatively easy to parse. This module makes it easy for
machines too. Use `segment` to parse a phrase into its parts:

>>> from wordsegment import load, segment
>>> load()
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


class Segmenter(object):
    """Segmenter

    Support for object-oriented programming and customization.

    """
    ALPHABET = set('abcdefghijklmnopqrstuvwxyz0123456789')
    UNIGRAMS_FILENAME = op.join(
        op.dirname(op.realpath(__file__)),
        'unigrams.txt',
    )
    BIGRAMS_FILENAME = op.join(
        op.dirname(op.realpath(__file__)),
        'bigrams.txt',
    )
    TOTAL = 1024908267229.0
    LIMIT = 24
    WORDS_FILENAME = op.join(
        op.dirname(op.realpath(__file__)),
        'words.txt',
    )


    def __init__(self):
        self.unigrams = {}
        self.bigrams = {}
        self.total = 0.0
        self.limit = 0
        self.words = []


    def load(self):
        "Load unigram and bigram counts from disk."
        self.unigrams.update(self.parse(self.UNIGRAMS_FILENAME))
        self.bigrams.update(self.parse(self.BIGRAMS_FILENAME))
        self.total = self.TOTAL
        self.limit = self.LIMIT
        with io.open(self.WORDS_FILENAME, encoding='utf-8') as reader:
            text = reader.read()
            self.words.extend(text.splitlines())


    @staticmethod
    def parse(filename):
        "Read `filename` and parse tab-separated file of word and count pairs."
        with io.open(filename, encoding='utf-8') as reader:
            lines = (line.split('\t') for line in reader)
            return dict((word, float(number)) for word, number in lines)


    def score(self, word, previous=None):
        "Score `word` in the context of `previous` word."
        unigrams = self.unigrams
        bigrams = self.bigrams
        total = self.total

        if previous is None:
            if word in unigrams:

                # Probability of the given word.

                return unigrams[word] / total

            # Penalize words not found in the unigrams according
            # to their length, a crucial heuristic.

            return 10.0 / (total * 10 ** len(word))

        bigram = '{0} {1}'.format(previous, word)

        if bigram in bigrams and previous in unigrams:

            # Conditional probability of the word given the previous
            # word. The technical name is *stupid backoff* and it's
            # not a probability distribution but it works well in
            # practice.

            return bigrams[bigram] / total / self.score(previous)

        # Fall back to using the unigram probability.

        return self.score(word)


    def isegment(self, text):
        "Return iterator of words that is the best segmenation of `text`."
        memo = dict()

        def search(text, previous='<s>'):
            "Return max of candidates matching `text` given `previous` word."
            if text == '':
                return 0.0, []

            def candidates():
                "Generator of (score, words) pairs for all divisions of text."
                for prefix, suffix in self.divide(text):
                    prefix_score = math.log10(self.score(prefix, previous))

                    pair = (suffix, prefix)
                    if pair not in memo:
                        memo[pair] = search(suffix, prefix)
                    suffix_score, suffix_words = memo[pair]

                    yield (prefix_score + suffix_score, [prefix] + suffix_words)

            return max(candidates())

        # Avoid recursion limit issues by dividing text into chunks, segmenting
        # those chunks and combining the results together. Chunks may divide
        # words in the middle so prefix chunks with the last five words of the
        # previous result.

        clean_text = self.clean(text)
        size = 250
        prefix = ''

        for offset in range(0, len(clean_text), size):
            chunk = clean_text[offset:(offset + size)]
            _, chunk_words = search(prefix + chunk)
            prefix = ''.join(chunk_words[-5:])
            del chunk_words[-5:]
            for word in chunk_words:
                yield word

        _, prefix_words = search(prefix)

        for word in prefix_words:
            yield word


    def segment(self, text):
        "Return list of words that is the best segmenation of `text`."
        return list(self.isegment(text))


    def divide(self, text):
        "Yield `(prefix, suffix)` pairs from `text`."
        for pos in range(1, min(len(text), self.limit) + 1):
            yield (text[:pos], text[pos:])


    @classmethod
    def clean(cls, text):
        "Return `text` lower-cased with non-alphanumeric characters removed."
        alphabet = cls.ALPHABET
        text_lower = text.lower()
        letters = (letter for letter in text_lower if letter in alphabet)
        return ''.join(letters)


_segmenter = Segmenter()        # pylint: disable=invalid-name
clean = _segmenter.clean        # pylint: disable=invalid-name
load = _segmenter.load          # pylint: disable=invalid-name
isegment = _segmenter.isegment  # pylint: disable=invalid-name
segment = _segmenter.segment    # pylint: disable=invalid-name
UNIGRAMS = _segmenter.unigrams
BIGRAMS = _segmenter.bigrams
WORDS = _segmenter.words


def main(arguments=()):
    """Command-line interface (CLI) entry-point. Parse `arguments` into in-file
    and out-file then read lines from in-file, segment the lines, and write the
    result to out-file. Input and output default to stdin and stdout
    respectively.

    """
    import argparse
    import os

    parser = argparse.ArgumentParser(description='English Word Segmentation')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)

    streams = parser.parse_args(arguments)
    load()

    for line in iter(streams.infile.readline, ''):
        streams.outfile.write(' '.join(segment(line.strip())))
        streams.outfile.write(os.linesep)


if __name__ == '__main__':
    main(sys.argv[1:])


__all__ = [
    'Segmenter',
    'load', 'isegment', 'segment',
    'UNIGRAMS', 'BIGRAMS', 'WORDS',
    'main'
]
__title__ = 'wordsegment'
__version__ = '1.3.1'
__build__ = 0x010301
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2018 Grant Jenks'
