# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        cur = head
        start = head

        while cur:
            if cur.val == 0:
                start.val, cur.val = cur.val, start.val
                start = start.next
            cur = cur.next

        return head
