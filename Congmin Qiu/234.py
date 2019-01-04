# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverse(self, head ):
        prev = None
        while head != None :
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.nex
        if fast != None:
            slow = slow.next
        slow = self.reverse(slow)
        fast = head
        while slow != None:
            if fast.val != slow.val:
                return False

            fast= fast.next
            slow = slow.next
        return True
