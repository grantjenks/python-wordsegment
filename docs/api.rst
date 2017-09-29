WordSegment API Reference
=========================

`WordSegment`_ API reference.

.. _`WordSegment`: http://www.grantjenks.com/docs/wordsegment/

.. py:function:: clean(text)
   :module: wordsegment

    Return `text` lower-cased with non-alphanumeric characters removed.

.. py:function:: divide(text)
   :module: wordsegment

    Yield (prefix, suffix) pairs from `text` with len(prefix) not
    exceeding `limit`.

.. py:function:: load()
   :module: wordsegment

    Load unigram and bigram counts from disk.

.. py:function:: score(word, prev=None)
   :module: wordsegment

    Score a `word` in the context of the previous word, `prev`.

.. py:function:: isegment(text)
   :module: wordsegment

    Return iterator of words that is the best segmenation of `text`.

.. py:function:: segment(text)
   :module: wordsegment

    Return a list of words that is the best segmenation of `text`.

.. py:data:: UNIGRAMS
   :module: wordsegment

    Mapping of (unigram, count) pairs.
    Loaded from the file 'wordsegment/unigrams.txt'.

.. py:data:: BIGRAMS
   :module: wordsegment

    Mapping of (bigram, count) pairs.
    Bigram keys are joined by a space.
    Loaded from the file 'wordsegment/bigrams.txt'.
