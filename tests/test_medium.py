from src.leetcodepy.medium import *
from src.leetcodepy.utils import ListNode


def test_add_two_numbers():
    def list_node_to_list(l: ListNode) -> list[int]:
        result: list[int] = []
        current_node = l
        while current_node.next is not None:
            result.append(current_node.val)
            current_node = current_node.next
        result.append(current_node.val)
        return result

    assert list_node_to_list(
        add_two_numbers(
            ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))
        )
    ) == [7, 0, 8]
    assert list_node_to_list(add_two_numbers(ListNode(0), ListNode(0))) == [0]
    assert list_node_to_list(
        add_two_numbers(
            ListNode(
                9,
                ListNode(
                    9,
                    ListNode(
                        9,
                        ListNode(
                            9,
                            ListNode(9, ListNode(9, ListNode(9))),
                        ),
                    ),
                ),
            ),
            ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
        )
    ) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_longest_substring_without_repeating_characters():
    # Valid inputs
    assert longest_substring_without_repeating_characters("abcabcbb") == 3
    assert longest_substring_without_repeating_characters("bbbbb") == 1
    assert longest_substring_without_repeating_characters("pwwkew") == 3
