API Documentation
-----------------

- segment(text)

    Return a list of words that is the best segmenation of `text`.

- score(word, prev=None)

    Score a `word` in the context of the previous word, `prev`.

- divide(text, limit=24)

    Yield (prefix, suffix) pairs from `text` with len(prefix) not
    exceeding `limit`.

- unigram_counts

    Mapping of (unigram, count) pairs.
    Loaded from the file 'unigrams.txt'.

- bigram_counts

    Mapping of (bigram, count) pairs.
    Loaded from the file 'bigrams.txt'.
