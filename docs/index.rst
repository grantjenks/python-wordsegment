English Word Segmentation in Python
===================================

WordSegment is an :ref:`Apache2 Licensed <apache2>` module for English word
segmentation, written in pure-Python, and based on a trillion-word corpus.

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

In your own Python programs, you'll mostly want to use :ref:`segment <segment>`
to divide a phrase into a list of its parts:

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

.. _`segment`:

.. function:: segment(text)

    Return a list of words that is the best segmenation of `text`.

.. function:: score(word, prev=None)

    Score a `word` in the context of the previous word, `prev`.

.. function:: divide(text, limit=24)

    Yield (prefix, suffix) pairs from `text` with len(prefix) not
    exceeding `limit`.

.. data:: unigram_counts

    Mapping of (unigram, count) pairs.
    Loaded from the file 'unigrams.txt'.

.. data:: bigram_counts

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

Indices and Utilities
---------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _`apache2`:

Apache2 License
---------------

A large number of open source projects you find today are `GPL Licensed`_.
A project that is released as GPL cannot be used in any commercial product
without the product itself also being offered as open source.

The MIT, BSD, ISC, and Apache2 licenses are great alternatives to the GPL
that allow your open-source software to be used freely in proprietary,
closed-source software.

SortedContainers is released under terms of `Apache2 License`_.

.. _`GPL Licensed`: http://www.opensource.org/licenses/gpl-license.php
.. _`Apache2 License`: http://opensource.org/licenses/Apache-2.0


WordSegment License
-------------------

    .. include:: ../LICENSE
