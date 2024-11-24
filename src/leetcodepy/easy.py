from typing import Optional
from .utils import ListNode


def two_sum(nums: list[int], target: int) -> list[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.



    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]



    Constraints:

        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.

    """
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    return []


def palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    x_str = str(x)
    return x_str == x_str[::-1]


def roman_to_integer(s: str) -> int:
    translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number


def longest_common_prefix(strs: list[str]) -> str:
    ans = ""
    v = sorted(strs)
    first = v[0]
    last = v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans


def valid_parentheses(s: str) -> bool:
    d = {"(": ")", "{": "}", "[": "]"}
    stack: list[str] = []
    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:
            return False
    return len(stack) == 0


def merge_two_sorted_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1 or not list2:
        return list1 or list2
    if list1.val <= list2.val:
        list1.next = merge_two_sorted_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_sorted_lists(list1, list2.next)
        return list2


def remove_duplicates_from_sorted_array(nums: list[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return j


def remove_element(nums: list[int], val: int) -> int:
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j


def find_the_index_of_the_first_occurrence_in_a_string(
    haystack: str, needle: str
) -> int:
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack)):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1


def search_insert_position(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
