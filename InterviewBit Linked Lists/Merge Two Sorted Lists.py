# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A.val <= B.val:
            new = ListNode(A.val)
            head = new
            curr2 = B
            curr1 = A.next
        else:
            new = ListNode(B.val)
            head = new
            curr2 = B.next
            curr1 = A

    while curr1 != None and curr2 != None:
        if curr1.val <= curr2.val:
            new.next = ListNode(curr1.val)
            new = new.next
            curr1 = curr1.next
        else:
            new.next = ListNode(curr2.val)
            new = new.next
            curr2 = curr2.next
    while curr1 != None:
        new.next = ListNode(curr1.val)
        new = new.next
        curr1 = curr1.next
    while curr2 != None:
        new.next = ListNode(curr2.val)
        new = new.next
        curr2 = curr2.next
    return head
