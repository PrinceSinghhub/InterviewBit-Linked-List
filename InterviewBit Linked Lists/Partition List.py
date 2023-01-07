# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        head = ListNode(None)
        head.next = A

        end = []
        cur_node = head
        while cur_node.next != None:

            last_node = cur_node
            cur_node = cur_node.next

            if cur_node.val >= B:
                last_node.next = cur_node.next
                end.append(cur_node.val)
                tail = last_node
                cur_node = last_node

            else:
                tail = cur_node

        for i in end:
            x = ListNode(i)
            tail.next = x
            tail = x

        tail.next = None

        return head.next



