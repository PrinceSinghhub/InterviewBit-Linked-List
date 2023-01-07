# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        lis = []
        temp = A
        while temp:
            lis.append(temp.val)
            temp = temp.next
        lis.sort()
        temp = A
        i = 0
        while temp:
            temp.val = lis[i]
            i += 1
            temp = temp.next
        return A
