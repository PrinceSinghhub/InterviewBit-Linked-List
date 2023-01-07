# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	def sortList(self, A):

        vis =[]

        curr=A

        n =0

        while(curr):

            vis.append(curr.val)

            n+=1

            curr=curr.next

        curr=A

        i=0

        vis = sorted(vis)

        while(curr and i<n):

            curr.val=vis[i]

            curr=curr.next

            i+=1

        return A