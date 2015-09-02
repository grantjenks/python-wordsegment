WordSegment API Reference
=========================

- wordsegment.clean(text)

    Return `text` lower-cased with non-alphanumeric characters removed.

- wordsegment.divide(text, limit=24)

    Yield (prefix, suffix) pairs from `text` with len(prefix) not
    exceeding `limit`.

- wordsegment.score(word, prev=None)

    Score a `word` in the context of the previous word, `prev`.

- wordsegment.segment(text)

    Return a list of words that is the best segmenation of `text`.

- wordsegment.unigram_counts

    Mapping of (unigram, count) pairs.
    Loaded from the file 'unigrams.txt'.

- wordsegment.bigram_counts

    Mapping of (bigram, count) pairs.
    Loaded from the file 'bigrams.txt'.
