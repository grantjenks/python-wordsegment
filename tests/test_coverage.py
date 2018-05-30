import os
import sys
from .context import wordsegment
from wordsegment import (
    clean, load, main, isegment, segment, UNIGRAMS, BIGRAMS, WORDS,
)

load()

def test_unigrams():
    assert 'test' in UNIGRAMS

def test_bigrams():
    assert 'in the' in BIGRAMS

def test_clean():
    assert clean("Can't buy me love!") == 'cantbuymelove'

def test_segment_0():
    result = ['choose', 'spain']
    assert segment(''.join(result)) == result

def test_segment_1():
    result = ['this', 'is', 'a', 'test']
    assert segment(''.join(result)) == result

def test_segment_2():
    result = [
        'when', 'in', 'the', 'course', 'of', 'human', 'events', 'it',
        'becomes', 'necessary'
    ]
    assert segment(''.join(result)) == result

def test_segment_3():
    result = ['who', 'represents']
    assert segment(''.join(result)) == result

def test_segment_4():
    result = ['experts', 'exchange']
    assert segment(''.join(result)) == result

def test_segment_5():
    result = ['speed', 'of', 'art']
    assert segment(''.join(result)) == result

def test_segment_6():
    result = ['now', 'is', 'the', 'time', 'for', 'all', 'good']
    assert segment(''.join(result)) == result

def test_segment_7():
    result = ['it', 'is', 'a', 'truth', 'universally', 'acknowledged']
    assert segment(''.join(result)) == result

def test_segment_8():
    result = [
        'it', 'was', 'a', 'bright', 'cold', 'day', 'in', 'april', 'and', 'the',
        'clocks', 'were', 'striking', 'thirteen'
    ]
    assert segment(''.join(result)) == result

def test_segment_9():
    result = [
        'it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst',
        'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was',
        'the', 'age', 'of', 'foolishness'
    ]
    assert segment(''.join(result)) == result

def test_segment_10():
    result = [
        'as', 'gregor', 'samsa', 'awoke', 'one', 'morning', 'from', 'uneasy',
        'dreams', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed',
        'into', 'a', 'gigantic', 'insect'
    ]
    assert segment(''.join(result)) == result

def test_segment_11():
    result = [
        'in', 'a', 'hole', 'in', 'the', 'ground', 'there', 'lived', 'a',
        'hobbit', 'not', 'a', 'nasty', 'dirty', 'wet', 'hole', 'filled', 'with',
        'the', 'ends', 'of', 'worms', 'and', 'an', 'oozy', 'smell', 'nor',
        'yet', 'a', 'dry', 'bare', 'sandy', 'hole', 'with', 'nothing', 'in',
        'it', 'to', 'sit', 'down', 'on', 'or', 'to', 'eat', 'it', 'was', 'a',
        'hobbit', 'hole', 'and', 'that', 'means', 'comfort'
    ]
    assert list(isegment(''.join(result))) == result

def test_segment_12():
    result = [
        'far', 'out', 'in', 'the', 'uncharted', 'backwaters', 'of', 'the',
        'unfashionable', 'end', 'of', 'the', 'western', 'spiral', 'arm', 'of',
        'the', 'galaxy', 'lies', 'a', 'small', 'un', 'regarded', 'yellow', 'sun'
    ]
    assert segment(''.join(result)) == result

def test_main():
    main(['tests/test.txt'])
    result = os.linesep.join(('choose spain', 'this is a test')) + os.linesep
    assert sys.stdout.getvalue() == result

def test_words():
    assert len(WORDS) > 0
    assert WORDS[0] == 'aa'
    assert WORDS[-1] == 'zzz'
