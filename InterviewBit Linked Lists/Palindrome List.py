class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        cur = A
        li = []
        while cur:
            li.append(cur.val)
            cur = cur.next
        n = len(li) // 2

        t = li[:n]
        li.reverse()
        t2 = li[:n]
        if (t == t2):
            return 1
        else:
            return 0