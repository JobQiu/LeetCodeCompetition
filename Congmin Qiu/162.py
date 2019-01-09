class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo < hi :
            mid = (lo + hi) // 2
            mid2 = mid + 1
            if nums[mid] < nums[mid2]:
                lo = mid2
            else:
                hi = mid
                
        return lo
