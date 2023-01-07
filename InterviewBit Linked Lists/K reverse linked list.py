# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if B == 1:
            return A
        if A is None:
            return None
        cur = A
        main = A
        Prev = None
        x = 0
        while x < B:
            temp = cur.next
            cur.next = Prev
            Prev = cur
            cur = temp
            x += 1
        main.next = self.reverseList(cur, B)
        return Prev


