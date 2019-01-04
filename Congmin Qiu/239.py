from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        dq = deque()

        for i in range(len(nums)):
            while len(dq) > 0 and dq[0]<i-k+1:
                dq.popleft()

            while len(dq) > 0 and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])
        return res
