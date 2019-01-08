class Solution:
    def helper(self, nums, target):
        if len(nums) <= 1:
            return False
        if len(nums) == 2 and sum(nums) % target == 0:
            return True

        i = 0
        j = 2
        curSum = nums[0] + nums[1]
        while j <= len(nums) :

            if curSum % target == 0:
                return True

            if j == len(nums) and curSum < target:
                break

            if curSum > target and i < j:
                curSum -= nums[i]
                i += 1
            else:

                curSum += nums[j]
                j += 1

        return False

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return True

        import copy
        temp = copy.deepcopy(nums)
        for i in range(len(temp)):
            temp[i] = temp[i] % k


        s = sum(temp)

        for i in range(s // k):

            target = (i + 1) * k
            if self.helper(temp, target):
                return True
        return False


s = Solution()
input = None
res = s.checkSubarraySum([2]*7, 7)
res = s.checkSubarraySum([1, 2, 3], 4)

print("")
