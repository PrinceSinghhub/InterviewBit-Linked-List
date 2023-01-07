# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        node = A
        while node and node.next:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return A
