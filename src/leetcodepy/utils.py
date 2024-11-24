class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ListNode):
            return False
        return self.val == value.val and self.next == value.next
