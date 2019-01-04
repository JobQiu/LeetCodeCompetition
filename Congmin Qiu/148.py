# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, l1, l2 ):
        dummy = ListNode(-1)
        head = dummy
        while l1 != None  and l2 != None  :
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head= head.next
        head.next = l1 if l1 else l2

        return dummy.next



        pass

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None :
            return head

        prev = None
        slow = head
        fast = head

        while fast != None and fast.next != None  :
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = None

        l1 = self.sort(head)
        l2 = self.sort(slow)
        return self.merge(l1,l2)

        pass
