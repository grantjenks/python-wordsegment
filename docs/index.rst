English Word Segmentation in Python
===================================

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
- 100% Test Coverage
- Includes unigram and bigram data
- Command line interface for batch processing
- Easy to hack (e.g. different scoring, new data, different language)
- Developed on Python 2.7
- Tested on CPython 2.6, 2.7, 3.2, 3.3, 3.4 and PyPy 2.5+, PyPy3 2.4+

Quickstart
----------

Installing WordSegment is simple with
`pip <http://www.pip-installer.org/>`_::

    $ pip install wordsegment

You can access documentation in the interpreter with Python's built-in help
function::

    >>> import wordsegment
    >>> help(wordsegment)

Tutorial
--------

In your own Python programs, you'll mostly want to use `segment` to divide a
phrase into a list of its parts:

    >>> from wordsegment import segment
    >>> segment('thisisatest')
    ['this', 'is', 'a', 'test']

WordSegment also provides a command-line interface for batch processing. This
interface accepts two arguments: in-file and out-file. Lines from in-file are
segmented iteratively, joined by a space, and written to out-file. Input and
output default to stdin and stdout respectively.::

    $ echo thisisatest | python -m wordsegment
    this is a test

// todo: show score
// todo: show divide
// todo: show clean
// todo: show unigram_counts
// todo: show bigram_counts

Reference and Indices
---------------------

.. toctree::

   api
   python-load-dict-fast-from-file

* `WordSegment Documentation`_
* `WordSegment at PyPI`_
* `WordSegment at Github`_
* `WordSegment Issue Tracker`_
* :ref:`search`
* :ref:`genindex`

.. _`WordSegment Documentation`: http://www.grantjenks.com/docs/wordsegment/
.. _`WordSegment at PyPI`: https://pypi.python.org/pypi/wordsegment
.. _`WordSegment at Github`: https://github.com/grantjenks/wordsegment
.. _`WordSegment Issue Tracker`: https://github.com/grantjenks/wordsegment/issues

WordSegment License
-------------------

.. include:: ../LICENSE
