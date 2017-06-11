# -*- coding: utf-8 -*-

import sys
from .context import wordsegment
import wordsegment as ws

def test_segment_0():
    assert ws.segment('choosespain') == ['choose', 'spain']

def test_segment_1():
    assert ws.segment('thisisatest') == ['this', 'is', 'a', 'test']

def test_segment_2():
    assert ws.segment('wheninthecourseofhumaneventsitbecomesnecessary') == ['when', 'in', 'the', 'course', 'of', 'human', 'events', 'it', 'becomes', 'necessary']

def test_segment_3():
    assert ws.segment('whorepresents') == ['who', 'represents']

def test_segment_4():
    assert ws.segment('expertsexchange') == ['experts', 'exchange']

def test_segment_5():
    assert ws.segment('speedofart') == ['speed', 'of', 'art']

def test_segment_6():
    assert ws.segment('nowisthetimeforallgood') == ['now', 'is', 'the', 'time', 'for', 'all', 'good']

def test_segment_7():
    assert ws.segment('itisatruthuniversallyacknowledged') == ['it', 'is', 'a', 'truth', 'universally', 'acknowledged']

def test_segment_8():
    assert ws.segment('itwasabrightcolddayinaprilandtheclockswerestrikingthirteen') == ['it', 'was', 'a', 'bright', 'cold', 'day', 'in', 'april', 'and', 'the', 'clocks', 'were', 'striking', 'thirteen']

def test_segment_9():
    assert ws.segment('itwasthebestoftimesitwastheworstoftimesitwastheageofwisdomitwastheageoffoolishness') == ['it', 'was', 'the', 'best', 'of', 'times', 'it', 'was', 'the', 'worst', 'of', 'times', 'it', 'was', 'the', 'age', 'of', 'wisdom', 'it', 'was', 'the', 'age', 'of', 'foolishness']

def test_segment_10():
    assert ws.segment('asgregorsamsaawokeonemorningfromuneasydreamshefoundhimselftransformedinhisbedintoagiganticinsect') == ['as', 'gregor', 'samsa', 'awoke', 'one', 'morning', 'from', 'uneasy', 'dreams', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'gigantic', 'insect']

def test_segment_11():
    assert ws.segment('inaholeinthegroundtherelivedahobbitnotanastydirtywetholefilledwiththeendsofwormsandanoozysmellnoryetadrybaresandyholewithnothinginittositdownonortoeatitwasahobbitholeandthatmeanscomfort') == ['in', 'a', 'hole', 'in', 'the', 'ground', 'there', 'lived', 'a', 'hobbit', 'not', 'a', 'nasty', 'dirty', 'wet', 'hole', 'filled', 'with', 'the', 'ends', 'of', 'worms', 'and', 'an', 'oozy', 'smell', 'nor', 'yet', 'a', 'dry', 'bare', 'sandy', 'hole', 'with', 'nothing', 'in', 'it', 'to', 'sit', 'down', 'on', 'or', 'to', 'eat', 'it', 'was', 'a', 'hobbit', 'hole', 'and', 'that', 'means', 'comfort']

def test_segment_12():
    assert ws.segment('faroutintheunchartedbackwatersoftheunfashionableendofthewesternspiralarmofthegalaxyliesasmallunregardedyellowsun') == ['far', 'out', 'in', 'the', 'uncharted', 'backwaters', 'of', 'the', 'unfashionable', 'end', 'of', 'the', 'western', 'spiral', 'arm', 'of', 'the', 'galaxy', 'lies', 'a', 'small', 'un', 'regarded', 'yellow', 'sun']

def test_load_custom_files_no_recompute():
    total_before = ws.TOTAL
    ws.load('unigrams.txt', 'bigrams.txt')
    print("BEFORE {} AFTER {}".format(total_before, ws.TOTAL))
    assert total_before == ws.TOTAL

def test_load_custom_files_recompute():
    total_before = ws.TOTAL
    ws.load('unigrams.txt', 'bigrams.txt', compute_unigram_total=True)
    print("X BEFORE {} AFTER {}".format(total_before, ws.TOTAL))
    assert total_before != ws.TOTAL
    assert ws.TOTAL == 17311951284


def test_main():
    ws.main(['tests/test.txt'])
    import os
    result = os.linesep.join(('choose spain', 'this is a test')) + os.linesep
    assert sys.stdout.getvalue() == result
