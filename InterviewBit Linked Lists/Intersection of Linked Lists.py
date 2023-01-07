# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        countA = 0
        countB = 0

        headA = A
        headB = B

        while A is not None:
            A = A.next
            countA += 1

        while B is not None:
            B = B.next
            countB += 1

        A = headA
        B = headB

        if countA > countB:
            for i in range(countA - countB):
                A = A.next

        else:
            for i in range(countB - countA):
                B = B.next

        for i in range(min(countA, countB)):
            if A is B:
                return A
            A = A.next
            B = B.next

        return None


