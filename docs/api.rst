WordSegment API Reference
=========================

.. py:function:: clean(text)
   :module: wordsegment

    Return `text` lower-cased with non-alphanumeric characters removed.

.. py:function:: divide(text, limit=24)
   :module: wordsegment

    Yield (prefix, suffix) pairs from `text` with len(prefix) not
    exceeding `limit`.

.. py:function:: score(word, prev=None)
   :module: wordsegment

    Score a `word` in the context of the previous word, `prev`.

.. py:function:: segment(text)
   :module: wordsegment

    Return a list of words that is the best segmenation of `text`.

.. py:data:: unigram_counts
   :module: wordsegment

    Mapping of (unigram, count) pairs.
    Loaded from the file 'wordsegment_data/unigrams.txt'.

.. py:data:: bigram_counts
   :module: wordsegment

    Mapping of (bigram, count) pairs.
    Loaded from the file 'wordsegment_data/bigrams.txt'.
