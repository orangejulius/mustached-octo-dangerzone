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

def test_first_middle_last_element_identical():
    array = [4, 4, 4, 4, 4, 4, 5, 4]
    assert_equal(amountShifted(array), 7)

def test_first_middle_last_element_identical2():
    array = [4, 5, 4, 4, 4, 4, 4, 4]
    assert_equal(amountShifted(array), 2)

def test_first_last_not_middle_identical():
    array = [4, 5, 6, 7, 8, 9, 4, 4]
    assert_equal(amountShifted(array), 6)

def test_all_elements_identical():
    array = [4, 4, 4, 4, 4, 4, 4, 4]
    assert_equal(amountShifted(array), 0)

def test_size_two_shifted():
    array = [5, 4]
    assert_equal(amountShifted(array), 1)

def test_size_two_not_shifted():
    array = [4, 5]
    assert_equal(amountShifted(array), 0)
