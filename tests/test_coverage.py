# -*- coding: utf-8 -*-

import sys
from .context import wordsegment
from wordsegment import segment, main

def test_segment_0():
    assert segment('choosespain') == ['choose', 'spain']

def test_segment_1():
    assert segment('thisisatest') == ['this', 'is', 'a', 'test']

def test_segment_2():
    assert segment('wheninthecourseofhumaneventsitbecomesnecessary') == ['when', 'in', 'the', 'course', 'of', 'human', 'events', 'it', 'becomes', 'necessary']

def test_segment_3():
    assert segment('whorepresents') == ['who', 'represents']

def test_segment_4():
    assert segment('expertsexchange') == ['experts', 'exchange']

def test_segment_5():
    assert segment('speedofart') == ['speed', 'of', 'art']

def test_segment_6():
    assert segment('nowisthetimeforallgood') == ['now', 'is', 'the', 'time', 'for', 'all', 'good']

def test_segment_7():
    assert segment('itisatruthuniversallyacknowledged') == ['it', 'is', 'a', 'truth', 'universally', 'acknowledged']

def test_segment_8():
    assert segment('itwasabrightcolddayinaprilandtheclockswerestrikingthirteen') == ['it', 'was', 'a', 'bright', 'cold', 'day', 'in', 'april', 'and', 'the', 'clocks', 'were', 'striking', 'thirteen']

def test_segment_9():
    assert segment('itwasthebestoftimesitwastheworstoftimesitwastheageofwisdomitwastheageoffoolishness') == ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']

def test_segment_10():
    assert segment('asgregorsamsaawokeonemorningfromuneasydreamshefoundhimselftransformedinhisbedintoagiganticinsect') == ['as', 'gregor', 'samsa', 'awoke', 'one', 'morning', 'from', 'uneasy', 'dreams', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'gigantic', 'insect']

def test_segment_11():
    assert segment('inaholeinthegroundtherelivedahobbitnotanastydirtywetholefilledwiththeendsofwormsandanoozysmellnoryetadrybaresandyholewithnothinginittositdownonortoeatitwasahobbitholeandthatmeanscomfort') == ['in', 'a', 'hole', 'in', 'the', 'ground', 'there', 'lived', 'a', 'hobbit', 'not', 'a', 'nasty', 'dirty', 'wet', 'hole', 'filled', 'with', 'the', 'ends', 'of', 'worms', 'and', 'an', 'oozy', 'smell', 'nor', 'yet', 'a', 'dry', 'bare', 'sandy', 'hole', 'with', 'nothing', 'in', 'it', 'to', 'sit', 'down', 'on', 'or', 'to', 'eat', 'it', 'was', 'a', 'hobbit', 'hole', 'and', 'that', 'means', 'comfort']

def test_segment_12():
    assert segment('faroutintheunchartedbackwatersoftheunfashionableendofthewesternspiralarmofthegalaxyliesasmallunregardedyellowsun') == ['far', 'out', 'in', 'the', 'uncharted', 'backwaters', 'of', 'the', 'unfashionable', 'end', 'of', 'the', 'western', 'spiral', 'arm', 'of', 'the', 'galaxy', 'lies', 'a', 'small', 'un', 'regarded', 'yellow', 'sun']

def test_main():
    main(['tests/test.txt'])
    assert sys.stdout.getvalue() == 'choose spain \nthis is a test \n'
