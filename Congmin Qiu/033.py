class Solution:
    def method(self, nums, target ):

        # 1. find the minimum
        lo = 0
        hi = len(nums)

        while lo < hi :
            inLeft = target >= nums[lo]
            mid = (lo + hi ) // 2
            if nums[mid] >= nums[lo] and target >= nums[lo]:
                num_mid = nums[mid]
            elif nums[mid] < nums[lo] and target < nums[lo]:
                num_mid = nums[mid]
            elif nums[mid] >= nums[lo] and target < nums[lo]:
                num_mid = -9999
            else:
                num_mid = 9999

            if nums[mid] == target:
                return  mid

            if nums[mid] > target:
                hi = mid
            else:
                lo = mid+1
        return lo







        pass

s = Solution()
input = None
res = s

print("")
