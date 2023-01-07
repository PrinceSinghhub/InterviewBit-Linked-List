# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):

        if (A == None):
            return A

        vis = []

        n = 0

        curr = A

        while (curr):
            vis.append(curr.val)

            n += 1

            curr = curr.next

        B = B % n

        curr = A

        j = 0

        while (curr):
            curr.val = vis[(n + j - B) % n]

            j += 1

            curr = curr.next

        return A
