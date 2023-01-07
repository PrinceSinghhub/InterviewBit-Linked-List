# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        if not A or not A.next:
            return A
        reverse = True
        counter = 1

        prev = None
        cur = A
        ans = None

        prev_tail = None
        cur_tail = A
        while cur:
            if reverse:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            else:
                prev = cur
                cur = cur.next

            if counter == B:
                if reverse:
                    if prev_tail:
                        prev_tail.next = prev
                    cur_tail.next = cur
                else:
                    prev_tail = prev
                    cur_tail = cur
                if not ans:
                    ans = prev

                counter = 1
                reverse = reverse ^ True
            else:
                counter += 1

        return ans





