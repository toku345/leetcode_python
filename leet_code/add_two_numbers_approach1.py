# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        p, q, curr = l1, l2, dummy_head
        carry = 0
        while (p is not None) or (q is not None):
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if p is not None: p = p.next
            if q is not None: q = q.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy_head.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)

    expect = ListNode(7)
    expect.next = ListNode(0)
    expect.next.next = ListNode(8)

    # print(expect.val, result.val)
    assert expect.val == result.val
    assert expect.next.val == result.next.val
    assert expect.next.next.val == result.next.next.val
