# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        aa=[]
        if A==None:
                return A
        while(A):
            aa.append(A.val)
            A=A.next
        i=0
        bb=[]
        while(i<len(aa)):
            try:
                bb.append(aa[i+1])
                bb.append(aa[i])
                i+=2
            except:
                bb.append(aa[i])
                i+=1
        head = ListNode(bb[0])
        cur=head
        for i in range(1,len(bb)):
            cur.next = ListNode(bb[i])
            cur = cur.next
        return head
