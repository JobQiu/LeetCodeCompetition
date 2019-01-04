# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        extra = ListNode(0)
        dummy = ListNode(-1)
        head = dummy

        while l1 != None or l2 != None  or extra.val != 0:
            tempSum = 0
            if l1 != None:
                tempSum += l1.val
                l1 = l1.next


            if l2 != None:
                tempSum += l2.val
                l2 = l2.next

            tempSum += extra.val

            extra.val = tempSum // 10
            head.next = ListNode(tempSum % 10)
            head = head.next
        return dummy.next
            
