# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        dummy = ListNode(-1)
        dummy.next = node
        cur = dummy

        while cur != None:
            cur = cur.next
            if cur.val == node.
