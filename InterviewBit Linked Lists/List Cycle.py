# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):

        hash = {}

        while A:

            if A.val in hash:

                return A


            hash[A.val] = A

            A = A.next

        return None