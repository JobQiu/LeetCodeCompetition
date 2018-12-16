class Solution:
    def searchInsert(self, nums, target, i_start):
        left = i_start
        right = len(nums)

        while left < right:

            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    def triangleNumber( ):

    def triangleNumber2(self, nums):
        nums.sort()
        res = 0

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                target = nums[i] + nums[j] - 0.5
                k = self.searchInsert(nums, target, j + 1)
                print(k)
                res += (k - j - 1)
        return res


s = Solution()
nums = [2, 2, 3, 4]
target = 3.5
i_start = 2
res = s.searchInsert(nums, target, i_start)
print(res)

res = s.triangleNumber(nums)
print(res)
