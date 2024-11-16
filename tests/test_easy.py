from src.leetcodepy.easy import *
import pytest


def test_two_sum():
    # Invalid inputs
    with pytest.raises(AssertionError):
        two_sum([1], 1)
    with pytest.raises(AssertionError):
        two_sum([1 for _ in range(10**5 + 1)], 1)
    with pytest.raises(AssertionError):
        two_sum([-(10**9) - 1, 2, 3, 4], 1)
    with pytest.raises(AssertionError):
        two_sum([2, 3, 4, 10**9 + 1], 2)
    with pytest.raises(AssertionError):
        two_sum([1, 2, 4, 5, 6], -(10**9) - 1)
    with pytest.raises(AssertionError):
        two_sum([1, 2, 4, 5, 6], 10**9 + 1)
    with pytest.raises(AssertionError):
        two_sum([1, 2, 13289, 10**9 + 9, 12312], 10**9 + 2)

    # Valid inputs
    assert set(two_sum([2, 7, 11, 15], 9)) == set([0, 1])
    assert set(two_sum([3, 2, 4], 6)) == set([1, 2])
    assert set(two_sum([3, 3], 6)) == set([0, 1])
