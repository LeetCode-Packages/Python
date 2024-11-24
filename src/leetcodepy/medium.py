import re

from .utils import ListNode


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.



    Example 1:

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Example 2:

    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]



    Constraints:

        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.
    """
    dummy_head = ListNode(0)
    curr = dummy_head
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        column_sum = l1_val + l2_val + carry
        carry = column_sum // 10
        new_node = ListNode(column_sum % 10)
        curr.next = new_node
        curr = new_node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy_head.next


def longest_substring_without_repeating_characters(s: str) -> int:
    """
    Given a string s, find the length of the longest substring
    without repeating characters.


    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



    Constraints:

        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.
    """
    pattern = r'^[A-Za-z0-9\s!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]+$'
    assert re.match(pattern, s)
    assert 0 <= len(s) <= 5 * 10**4

    max_length = left = 0
    count: dict[str, int] = {}

    for right, c in enumerate(s):
        count[c] = 1 + count.get(c, 0)
        while count[c] > 1:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
