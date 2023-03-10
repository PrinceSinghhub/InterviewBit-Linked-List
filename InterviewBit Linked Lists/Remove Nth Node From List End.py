# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    def removeNthFromEnd(self, A, B):
        first = A

        second = A
        for i in range(B):
            if first.next == None:
                return A.next
            first = first.next

        while (first.next):
            first = first.next
            second = second.next
        second.next = second.next.next

        return (A)
