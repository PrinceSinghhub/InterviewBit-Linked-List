# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, head):
        even = None
        odd = head
        while odd and odd.next:
            temp = odd.next
            odd.next = temp.next
            temp.next = even
            even = temp
            odd = odd.next
        odd = head
        while even:
            temp = even.next
            even.next = odd.next
            odd.next = even
            odd = odd.next.next
            even = temp
        return head
