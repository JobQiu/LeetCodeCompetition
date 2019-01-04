# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return  None
        m = {}
        m[None ] = None
        cur = head
        while cur:
            m[cur]=  RandomListNode(cur.label)
            cur = cur.next

        cur = head
        while cur :
            m[cur].next = m[cur.next]
            m[cur].random = m[cur.random]
            cur = cur.next
        return m[head]
