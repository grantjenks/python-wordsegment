"""Merges frequencies of uppercase and lowercase n-grams.

For example, if the input looks like this:

    aa bb   5
    Aa bb   3
    Cc dd   2
    ee ff   1

This tool outputs:

    aa bb   8
    cc dd   2
    ee ff   1

"""
from __future__ import print_function

import sys
from collections import Counter

if __name__ == '__main__':
    ngram_frequency = Counter()
    for line in sys.stdin:
        ngram, count = line.split('\t')
        ngram, count = ngram.lower(), int(count)
        ngram_frequency[ngram] += count

    for ngram, count in sorted(ngram_frequency.items()):
        print(ngram, count, sep='\t')
