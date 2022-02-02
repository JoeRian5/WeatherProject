import Functions
from pytest import approx


def test_calc_mean():
    assert Functions.calc_mean([4,6,2]) == 4, "should be 4"


def test_median():
    assert (Functions.calc_median([1,3,3,6,7,8,9]) == 10) == False
    assert Functions.calc_median([1,2,3,4,5,6,7,8,9]) == 4.5
