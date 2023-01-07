# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return an integer

    def count(self, A):
        head = A
        count = 0
        while head:
            head = head.next
            count += 1
        return count

    def solve(self, A, B):
        length = self.count(A)

        if length == 1: return -1

        size = (length // 2) + 1

        if B > size: return -1

        ss = size - B - 1

        count = 0
        while A and count < ss:
            A = A.next
            count += 1
        if A: return A.val
        return None

