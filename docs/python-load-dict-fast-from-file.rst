Python: Load Dict Fast from File
================================

Python ``wordsegment`` uses two text files to store unigram and bigram
count data. The files currently store records separated by newline
characters with fields separated by tabs.

.. code:: python

    with open('../wordsegment_data/unigrams.txt', 'r') as reader:
        print repr(reader.readline())


.. parsed-literal::

    'the\\t23135851162\\n'


When the ``wordsegment`` module is imported these files are read from
disk and used to construct a Python ``dict`` mapping ``word`` to
``count`` pairs.

That function works like so:

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = (line.split('\t') for line in reader)
        dict((word, float(number)) for word, number in lines)


.. parsed-literal::

    1 loops, best of 3: 286 ms per loop


Since we're talking about performance, here's some details about my
platform.

.. code:: python

    import subprocess
    print subprocess.check_output([
        '/usr/sbin/sysctl', '-n', 'machdep.cpu.brand_string'
    ])

    import sys
    print sys.version


.. parsed-literal::

    Intel(R) Core(TM) i7-4960HQ CPU @ 2.60GHz

    2.7.10 (default, May 25 2015, 13:06:17)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)]


Loading the files in about a second is plenty fast for me but I wondered
if there was a faster way. Here's a few things I tried.

Simply reading all the lines from the file takes 27ms:

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = [line for line in reader]


.. parsed-literal::

    10 loops, best of 3: 26.6 ms per loop


Another way to accomplish the same:

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = reader.read().split('\n')


.. parsed-literal::

    10 loops, best of 3: 20.7 ms per loop


That's 30% faster but it's a small part of 286ms. What takes the
majority of the time?

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = (line.split('\t') for line in reader)
        for word, number in lines:
            pass


.. parsed-literal::

    10 loops, best of 3: 115 ms per loop


So splitting each line takes nearly 90ms. That's a bit surprising to me.
What else takes so long?

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = (line.split('\t') for line in reader)
        for word, number in lines:
            float(number)


.. parsed-literal::

    10 loops, best of 3: 167 ms per loop


Wow, 51ms to convert strings to floats. Maybe later we can optimize
that. Finally, the last chunk must be constructing the ``dict``.

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = (line.split('\t') for line in reader)
        result = dict()
        for word, number in lines:
            result[word] = float(number)


.. parsed-literal::

    1 loops, best of 3: 254 ms per loop


By calling ``__setitem__`` repeatedly we avoid the construction of the
tuple used to construct the dict using its constructor. Let's experiment
with that.

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = (line.split('\t') for line in reader)
        dict((word, float(number)) for word, number in lines)


.. parsed-literal::

    1 loops, best of 3: 303 ms per loop


This isn't Python 2.6 compatible but what about a ``dict``
comprehension?

.. code:: python

    # %%timeit
    with open('../wordsegment_data/unigrams.txt') as reader:
        lines = (line.split('\t') for line in reader)
        {word: float(number) for word, number in lines}


.. parsed-literal::

    1 loops, best of 3: 275 ms per loop


It's a bit disappointing that the constructor is slower than calling
``__setitem__`` repeatedly. But maybe that just reflects how much
optimization has gone into making ``__setitem__`` really fast.

Here's a breakdown of how long various steps are taking:

+--------------------------------+---------+
| Operation                      | Time    |
+================================+=========+
| Read file and parse lines      | 26ms    |
+--------------------------------+---------+
| Split lines by tab character   | 90ms    |
+--------------------------------+---------+
| Convert strings to floats      | 50ms    |
+--------------------------------+---------+
| Creating ``dict(...)``         | 135ms   |
+--------------------------------+---------+

Unfortunately, constructing the ``dict`` is hard to optimize. So let's
look at the other steps. If we stored the counts on disk in binary
format then we could avoid parsing them. If we did so, we might likewise
store the words in a separate file. Let's convert our unigrams file into
two.

.. code:: python

    with open('../wordsegment_data/unigrams.txt') as reader:
        pairs = [line.split('\t') for line in reader]
        words = [pair[0] for pair in pairs]
        counts = [float(pair[1]) for pair in pairs]

        with open('words.txt', 'wb') as writer:
            writer.write('\n'.join(words))

        from array import array
        values = array('d')
        values.fromlist(counts)
        with open('counts.bin', 'wb') as writer:
            values.tofile(writer)

Now we have two files: ``words.txt`` and ``counts.bin``. The first
stores words separated by newline characters in ascii. The latter stores
double-precision floating-point numbers in binary. Together we can use
these to construct our ``dict``.

.. code:: python

    from itertools import izip as zip

.. code:: python

    # %%timeit
    with open('words.txt', 'rb') as lines, open('counts.bin', 'rb') as counts:
        words = lines.read().split('\n')
        values = array('d')
        values.fromfile(counts, 333333)
        dict(zip(words, values))


.. parsed-literal::

    10 loops, best of 3: 106 ms per loop


Wow. We started at a time of 286ms and worked down to 106ms. That's 62%
faster. The key to the speedup is separating the ``dict`` keys and
values and using fast methods for parsing each. Reading words from a
file now uses ``str.split`` which is actually faster than Python's
built-in buffered-file readline mechanism. The ``array`` module parses
counts directly from a binary-formatted file. Finally, the ``dict``
constructor is used with arguments izipped together. I tried using the
``__setitem__`` trick here but results were within error of one another
and I prefer this style.

At the end of the day, I'm not that impressed. 62% is faster but I
expected to improve things by 10x not 2x. Even with this speedup, you'll
notice a delay on module import. And now the format of the files is
funky. They don't play nice with grep, etc. I'm going to leave things
as-is for now.

I'd be happy to hear what others have tried. Note in this case that I
don't care how long it takes to write the files. That would be another
interesting thing to benchmark.

I also tried formatting the ``dict`` in a Python module which would be
parsed on import. This was actually a little slower than the initial
code. My guess is the Python interpreter is doing roughly the same
thing.
