# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def insertPos(self, nums, target):
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        return start

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """

        nums = []
        dq = deque()
        while root != None:
            dq.append(root)
            root = root.left

        while len(dq) > 0:
            cur = dq.pop()
            nums.append(cur.val)
            cur = cur.right
            while cur != None:
                dq.append(cur)
                cur = cur.left
        insertPos = self.insertPos(nums, target)


s = Solution()
for i in range(0, 6):
    res = s.insertPos([1, 2, 3, 4, 5], i)
    print(res)
"""
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

res = s.closestKValues(root, 3.73, 4)
"""
