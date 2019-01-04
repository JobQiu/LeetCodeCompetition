class Solution:
    def part(self, nums, lo, hi):

        i = lo
        j = hi + 1

        while True:
            while i < hi:
                i += 1
                if nums[i] >= nums[lo]:
                    break
            while j > lo:
                j -= 1
                if nums[j] <= nums[lo]:
                    break
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[lo], nums[j] = nums[j], nums[lo]
        return j
        pass

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import random
        random.shuffle(nums)

        k = len(nums) - k  # since we will sort it in asce

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            j = self.part(nums, lo, hi)
            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                break
        return nums[k]
        pass


# %%
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
#          l                    h
lo = 0
hi = len(nums) - 1

# %%

s = Solution()
input = None
res = s.findKthLargest(nums, 5)

print("")
