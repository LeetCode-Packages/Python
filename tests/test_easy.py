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


def test_palindrome_number():
    assert palindrome_number(121)
    assert not palindrome_number(-121)
    assert not palindrome_number(10)


def test_roman_to_integer():
    assert roman_to_integer("III") == 3
    assert roman_to_integer("LVIII") == 58
    assert roman_to_integer("MCMXCIV") == 1994


def test_longest_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""


def test_valid_parentheses():
    assert valid_parentheses("()")
    assert valid_parentheses("()[]{}")
    assert not valid_parentheses("(]")
    assert valid_parentheses("([])")


def test_merge_two_sorted_lists():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    assert merge_two_sorted_lists(list1, list2) == ListNode(
        1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
    )

    assert merge_two_sorted_lists(None, None) == None
    assert merge_two_sorted_lists(None, ListNode(0)) == ListNode(0)


def test_remove_duplicates_from_sorted_array():
    nums = [1, 1, 2]
    assert remove_duplicates_from_sorted_array(nums) == 2
    assert nums[:2] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates_from_sorted_array(nums) == 5
    assert nums[:5] == [0, 1, 2, 3, 4]


def test_remove_element():
    nums = [3, 2, 2, 3]
    assert remove_element(nums, 3) == 2
    assert set(nums[:2]) == set([2, 2])

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert remove_element(nums, 2) == 5
    assert set(nums[:5]) == set([0, 1, 4, 0, 3])


def test_find_the_index_of_the_first_occurrence_in_a_string():
    assert find_the_index_of_the_first_occurrence_in_a_string("sadbutsad", "sad") == 0
    assert find_the_index_of_the_first_occurrence_in_a_string("leetcode", "leeto") == -1


def test_search_insert_position():
    assert search_insert_position([1, 3, 5, 6], 5) == 2
    assert search_insert_position([1, 3, 5, 6], 2) == 1
    assert search_insert_position([1, 3, 5, 6], 7) == 4
