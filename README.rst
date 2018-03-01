Python Word Segmentation
========================

`WordSegment`_ is an Apache2 licensed module for English word
segmentation, written in pure-Python, and based on a trillion-word corpus.

Based on code from the chapter "`Natural Language Corpus Data`_" by Peter
Norvig from the book "`Beautiful Data`_" (Segaran and Hammerbacher, 2009).

Data files are derived from the `Google Web Trillion Word Corpus`_, as
described by Thorsten Brants and Alex Franz, and `distributed`_ by the
Linguistic Data Consortium. This module contains only a subset of that
data. The unigram data includes only the most common 333,000 words. Similarly,
bigram data includes only the most common 250,000 phrases. Every word and
phrase is lowercased with punctuation removed.

.. _`WordSegment`: http://www.grantjenks.com/docs/wordsegment/
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
- Tested on CPython 2.6, 2.7, 3.2, 3.3, 3.4, 3.5, 3.6 and PyPy, PyPy3
- Tested on Windows, Mac OS X, and Linux
- Tested using Travis CI and AppVeyor CI

.. image:: https://api.travis-ci.org/grantjenks/python-wordsegment.svg
    :target: http://www.grantjenks.com/docs/wordsegment/

.. image:: https://ci.appveyor.com/api/projects/status/github/grantjenks/python-wordsegment?branch=master&svg=true
    :target: http://www.grantjenks.com/docs/wordsegment/

Quickstart
----------

Installing `WordSegment`_ is simple with
`pip <http://www.pip-installer.org/>`_::

    $ pip install wordsegment

You can access documentation in the interpreter with Python's built-in help
function::

    >>> import wordsegment
    >>> help(wordsegment)

Tutorial
--------

In your own Python programs, you'll mostly want to use `segment` to divide a
phrase into a list of its parts::

    >>> from wordsegment import load, segment
    >>> load()
    >>> segment('thisisatest')
    ['this', 'is', 'a', 'test']

The `load` function reads and parses the unigrams and bigrams data from
disk. Loading the data only needs to be done once.

`WordSegment`_ also provides a command-line interface for batch
processing. This interface accepts two arguments: in-file and out-file. Lines
from in-file are iteratively segmented, joined by a space, and written to
out-file. Input and output default to stdin and stdout respectively. ::

    $ echo thisisatest | python -m wordsegment
    this is a test

If you want to run `WordSegment`_ as a kind of server process then use Python's
``-u`` option for unbuffered output. You can also set ``PYTHONUNBUFFERED=1`` in
the environment. ::

    >>> import subprocess as sp
    >>> wordsegment = sp.Popen(
            ['python', '-um', 'wordsegment'],
            stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)
    >>> wordsegment.stdin.write('thisisatest\n')
    >>> wordsegment.stdout.readline()
    'this is a test\n'
    >>> wordsegment.stdin.write('workswithotherlanguages\n')
    >>> wordsegment.stdout.readline()
    'works with other languages\n'
    >>> wordsegment.stdin.close()
    >>> wordsegment.wait()  # Process exit code.
    0

The maximum segmented word length is 24 characters. Neither the unigram nor
bigram data contain words exceeding that length. The corpus also excludes
punctuation and all letters have been lowercased. Before segmenting text,
`clean` is called to transform the input to a canonical form::

    >>> from wordsegment import clean
    >>> clean('She said, "Python rocks!"')
    'shesaidpythonrocks'
    >>> segment('She said, "Python rocks!"')
    ['she', 'said', 'python', 'rocks']

Sometimes its interesting to explore the unigram and bigram counts
themselves. These are stored in Python dictionaries mapping word to count. ::

    >>> import wordsegment as ws
    >>> ws.load()
    >>> ws.UNIGRAMS['the']
    23135851162.0
    >>> ws.UNIGRAMS['gray']
    21424658.0
    >>> ws.UNIGRAMS['grey']
    18276942.0

Above we see that the spelling `gray` is more common than the spelling `grey`.

Bigrams are joined by a space::

    >>> import heapq
    >>> from pprint import pprint
    >>> from operator import itemgetter
    >>> pprint(heapq.nlargest(10, ws.BIGRAMS.items(), itemgetter(1)))
    [('of the', 2766332391.0),
     ('in the', 1628795324.0),
     ('to the', 1139248999.0),
     ('on the', 800328815.0),
     ('for the', 692874802.0),
     ('and the', 629726893.0),
     ('to be', 505148997.0),
     ('is a', 476718990.0),
     ('with the', 461331348.0),
     ('from the', 428303219.0)]

Some bigrams begin with `<s>`. This is to indicate the start of a bigram::

    >>> ws.BIGRAMS['<s> where']
    15419048.0
    >>> ws.BIGRAMS['<s> what']
    11779290.0

The unigrams and bigrams data is stored in the `wordsegment` directory in
the `unigrams.txt` and `bigrams.txt` files respectively.

User Guide
----------

* `Word Segment API Reference`_
* `Using a Different Corpus`_
* `Python: Load dict Fast From File`_

.. _`Word Segment API Reference`: http://www.grantjenks.com/docs/wordsegment/api.html
.. _`Using a Different Corpus`: http://www.grantjenks.com/docs/wordsegment/using-a-different-corpus.html
.. _`Python: Load dict Fast From File`: http://www.grantjenks.com/docs/wordsegment/python-load-dict-fast-from-file.html

References
----------

* `WordSegment Documentation`_
* `WordSegment at PyPI`_
* `WordSegment at Github`_
* `WordSegment Issue Tracker`_

.. _`WordSegment Documentation`: http://www.grantjenks.com/docs/wordsegment/
.. _`WordSegment at PyPI`: https://pypi.python.org/pypi/wordsegment
.. _`WordSegment at Github`: https://github.com/grantjenks/python-wordsegment
.. _`WordSegment Issue Tracker`: https://github.com/grantjenks/python-wordsegment/issues

WordSegment License
-------------------

Copyright 2018 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
