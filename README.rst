English Word Segmentation in Python
===================================

.. image:: https://api.travis-ci.org/grantjenks/wordsegment.svg
    :target: http://www.grantjenks.com/blog/portfolio-post/english-word-segmentation-python/

WordSegment is an Apache2 licensed module for English word segmentation, written
in pure-Python, and based on a trillion-word corpus.

Based on code from the chapter "`Natural Language Corpus Data`_" by Peter Norvig
from the book "`Beautiful Data`_" (Segaran and Hammerbacher, 2009).

Data files are derived from the `Google Web Trillion Word Corpus`_, as described
by Thorsten Brants and Alex Franz, and `distributed`_ by the Linguistic Data
Consortium. This module contains only a subset of that data. The unigram data
includes only the most common 333,000 words. Similarly, bigram data includes
only the most common 250,000 phrases. Every word and phrase is lowercased with
punctuation removed.

.. _`Natural Language Corpus Data`: http://norvig.com/ngrams/
.. _`Beautiful Data`: http://oreilly.com/catalog/9780596157111/
.. _`Google Web Trillion Word Corpus`: http://googleresearch.blogspot.com/2006/08/all-our-n-gram-are-belong-to-you.html
.. _`distributed`: https://catalog.ldc.upenn.edu/LDC2006T13

Features
--------

- Pure-Python
- Fully documented
- 100% test coverage
- Includes unigram and bigram data
- Command line interface for batch processing
- Easy to hack (e.g. different scoring, new data, different language)
- Developed on Python 2.7
- Tested on CPython 2.6, 2.7, 3.2, 3.3, 3.4 and PyPy 2.2

User Guide
----------

Installing WordSegment is simple with
`pip <http://www.pip-installer.org/>`_::

    > pip install wordsegment

You can access documentation in the interpreter with Python's built-in help
function:

    >>> import wordsegment
    >>> help(wordsegment)

In your own Python programs, you'll mostly want to use *segment* to divide a
phrase into a list of its parts:

    >>> from wordsegment import segment
    >>> segment('thisisatest')
    ['this', 'is', 'a', 'test']

WordSegment also provides a command-line interface for batch processing. This
interface accepts two arguments: in-file and out-file. Lines from in-file are
segmented iteratively, joined by a space, and written to out-file. Input and
output default to stdin and stdout respectively.::

    > echo thisisatest | python -m wordsegment
    this is a test

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

Useful Links
------------

- `WordSegment Project @ GrantJenks.com`_
- `WordSegment @ PyPI`_
- `WordSegment @ Github`_
- `Issue Tracker`_

.. _`WordSegment Project @ GrantJenks.com`: http://www.grantjenks.com/blog/portfolio-post/english-word-segmentation-python/
.. _`WordSegment @ PyPI`: https://pypi.python.org/pypi/wordsegment
.. _`WordSegment @ Github`: https://github.com/grantjenks/wordsegment
.. _`Issue Tracker`: https://github.com/grantjenks/wordsegment/issues


WordSegment License
-------------------

Copyright (c) 2014 Grant Jenks

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
