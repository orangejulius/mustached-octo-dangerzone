from nose.tools import *

from rotate import *

def test_no_duplicates():
    shiftedArray = [6, 3, 4, 5]
    assert_equal(amountShifted(shiftedArray), 1)

def test_no_duplicates2():
    shiftedArray = [6, 7, 9, 1, 4, 5]
    assert_equal(amountShifted(shiftedArray), 3)

def test_duplicates():
    shiftedArray = [6, 3, 4, 5, 5]
    assert_equal(amountShifted(shiftedArray), 1)

def test_mostly_shifted():
    shiftedArray = [6, 7, 9, 11, 5]
    assert_equal(amountShifted(shiftedArray), 4)

def test_not_shifted():
    array = [1, 2, 3, 4]
    assert_equal(amountShifted(array), 0)
