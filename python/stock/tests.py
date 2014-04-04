from nose.tools import *

from stock import *

def test_empty():
    prices = []
    assert_equal(maxProfit(prices), (0, 0))

def test_easy_two_item_list():
    prices = [1, 2]
    assert_equal(maxProfit(prices), (0, 1))

#test a case where the all time high price is not the best sell price
def test_three_item_list():
    prices = [3, 1, 2]
    assert_equal(maxProfit(prices), (1, 2))

#test a case where the all time low is not the best buy price
def test_four_item_list():
    prices = [4, 6, 1, 2]
    assert_equal(maxProfit(prices), (0, 1))

#test a case where the best buy and sell prices are not the all time high or low prices
def test_six_item_list():
    prices = [4, 6, 2, 5, 1, 3]
    assert_equal(maxProfit(prices), (2, 3))
