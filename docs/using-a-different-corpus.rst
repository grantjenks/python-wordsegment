Using a Different Corpus
========================

WordSegment makes it easy to use a different corpus for word
segmentation.

If you simply want to "teach" the algorithm a single phrase it doesn't
know then read `this StackOverflow
answer <http://stackoverflow.com/questions/20695825/english-word-segmentation-in-nlp>`__.

Now, let's get a new corpus. For this example, we'll use the text from
Jane Austen's *Pride and Prejudice*.

.. code:: python

    import requests

    response = requests.get('https://www.gutenberg.org/ebooks/1342.txt.utf-8')

    text = response.text

    print len(text)

.. parsed-literal::

    717573

Great. We've got a new corpus for ``wordsegment``. Now let's look at
what parts of the API we need to change. There's one function and two
dictionaries: ``wordsegment.clean``, ``wordsegment.BIGRAMS`` and
``wordsegment.UNIGRAMS``. We'll work on these in reverse.

.. code:: python

    import wordsegment
    wordsegment.load()

.. code:: python

    print type(wordsegment.UNIGRAMS), type(wordsegment.BIGRAMS)

.. parsed-literal::

    <type 'dict'> <type 'dict'>

.. code:: python

    print wordsegment.UNIGRAMS.items()[:3]
    print wordsegment.BIGRAMS.items()[:2]

.. parsed-literal::

    [('biennials', 37548.0), ('verplank', 48349.0), ('tsukino', 19771.0)]
    [('personal effects', 151369.0), ('basic training', 294085.0)]

Ok, so ``wordsegment.UNIGRAMS`` is just a dictionary mapping
unigrams to their counts. Let's write a method to tokenize our text.

.. code:: python

    import re

    def tokenize(text):
        pattern = re.compile('[a-zA-Z]+')
        return (match.group(0) for match in pattern.finditer(text))

    print list(tokenize("Wait, what did you say?"))

.. parsed-literal::

    ['Wait', 'what', 'did', 'you', 'say']

Now we'll build our dictionaries.

.. code:: python

    from collections import Counter

    wordsegment.UNIGRAMS.clear()
    wordsegment.UNIGRAMS.update(Counter(tokenize(text)))

    def pairs(iterable):
        iterator = iter(iterable)
        values = [next(iterator)]
        for value in iterator:
            values.append(value)
            yield ' '.join(values)
            del values[0]

    wordsegment.BIGRAMS.clear()
    wordsegment.BIGRAMS.update(Counter(pairs(tokenize(text))))

That's it.

Now, by default, ``wordsegment.segment`` lowercases all input and
removes punctuation. In our corpus we have capitals so we'll also have
to change the ``clean`` function. Our heaviest hammer is to simply
replace it with the identity function. This will do no sanitation of the
input to ``segment``.

.. code:: python

    from wordsegment import _segmenter

    def identity(value):
        return value

    _segmenter.clean = identity

.. code:: python

    wordsegment.segment('wantofawife')

.. parsed-literal::

    ['want', 'of', 'a', 'wife']

If you find this behaves poorly then you may need to change the
``_segmenter.total`` variable to reflect the total of all unigrams. In
our case that's simply:

.. code:: python

    _segmenter.total = float(sum(wordsegment.UNIGRAMS.values()))

WordSegment doesn't require any fancy machine learning training
algorithms. Simply update the unigram and bigram count dictionaries and
you're ready to go.
