# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        n = m = 0  # Length of A, B

        current = A
        while current:
            n += 1
            current = current.next

        current = B
        while current:
            m += 1
            current = current.next

        if m > n:  # A always contain the longest list
            current = A
            A = B
            B = current

        temp1 = A
        temp2 = B
        carry = 0
        while temp1 and temp2:  # Run loop untill smaller list
            value = (temp1.val + temp2.val + carry) % 10
            carry = (temp1.val + temp2.val + carry) // 10
            temp1.val = value
            current = temp1
            temp1 = temp1.next
            temp2 = temp2.next

        while temp1:  # Run loop untill longer one
            if carry:
                value = temp1.val
                temp1.val = (value + carry) % 10
                carry = (value + carry) // 10
            current = temp1
            temp1 = temp1.next

        if carry:  # If after addition complete, carry left?
            node = ListNode(carry)
            current.next = node

        return A

