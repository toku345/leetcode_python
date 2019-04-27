#!/usr/bin/env python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def listToNumber(l, position):
            if l is None:
                return 0
            value = l.val * position
            return value + listToNumber(l.next, position * 10)
        def numberToListNode(value):
            node = None
            for val in str(value):
                if node is None:
                    node = ListNode(int(val))
                else:
                    n = ListNode(int(val))
                    n.next = node
                    node = n
            return node

        l1_value = listToNumber(l1, 1)
        l2_value = listToNumber(l2, 1)

        return numberToListNode(l1_value + l2_value)


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    expect = ListNode(7)
    expect.next = ListNode(0)
    expect.next.next = ListNode(8)

    result = Solution().addTwoNumbers(l1, l2)
    assert expect.val == result.val
    assert expect.next.val == result.next.val
    assert expect.next.next.val == result.next.next.val
