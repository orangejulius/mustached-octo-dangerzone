from nose.tools import *

from stock import *

def test_empty():
    prices = []
    assert_equal(maxProfit(prices), (0, 0))

def test_easy_two_item_list():
    prices = [1, 2]
    assert_equal(maxProfit(prices), (0, 1))
