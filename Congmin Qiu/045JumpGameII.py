import collections


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return 0

        # 2 3 1 1 4
        level = 0
        start = 0
        end = 1
        l = len(nums)  # l =5

        while end < l:  # end = 1 < 5
            new_end = end  # = 1
            for ind in range(start, end):  # form [0 to 1)
                if ind + nums[ind] >= l - 1:
                    return level + 1

                new_end = max(ind + nums[ind], new_end)
            start = end
            end = new_end+1
            level += 1
        return l

        # %%


s = Solution()
nums = [1,2,3]
res = s.jump(nums)

# assert res == 2


d = collections.deque()

# %%
