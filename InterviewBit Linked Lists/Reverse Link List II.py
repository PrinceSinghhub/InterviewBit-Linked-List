# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, head, m, n):
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            p = p.next
        cur, prev = p.next, None
        for _ in range(n - m + 1):
            cur.next, prev, cur = prev, cur, cur.next
        p.next.next = cur
        p.next = prev

        return dummy.next

