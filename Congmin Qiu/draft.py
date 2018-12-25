class Solution2:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = list([t for t in time if t != ":"])
        nums.sort()
        min_ = nums[0]

        for n in nums:
            if n > time[4] and n <= '9':
                return time[:4] + n

        for n in nums:
            if n > time[3] and n <= '5':
                return time[:3] + n + min_

        for n in nums:
            if n > time[1] and int(time[0] + n) < 24:
                return time[:1] + n + ":" + min_ * 2
        for n in nums:
            if n > time[0] and int(n + time[1]) < 24:
                return n + min_ + ":" + min_ * 2
        return min_ * 2 + ":" + min_ * 2


class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        garden = [[i - 1, i + 1] for i in range(len(flowers))]
        garden[0][0], garden[-1][1] = None, None
        ans = -1
        for i in range(len(flowers) - 1, -1, -1):
            cur = flowers[i] - 1
            left, right = garden[cur]
            if right != None and right - cur == k + 1:
                ans = i + 1
            if left != None and cur - left == k + 1:
                ans = i + 1
            if right != None:
                garden[right][0] = left
            if left != None:
                garden[left][1] = right
        return ans


"""

s = Solution()
res = s.kEmptySlots([6, 5, 8, 9, 7, 1, 10, 2, 3, 4], 2)
print(res)
"""
"""
fruit
    def totalFruit(self, tree):
        count = {}
        i = res = 0
        for j, v in enumerate(tree):
            count[v] = count.get(v, 0) + 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0: del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
"""


class Solution3:
    def jump(self, nums):
        map_ = {len(nums) - 1: (True, True)}
        res = 1
        for ind in range(len(nums) - 2, -1, -1):
            odd = False
            even = False
            for j in range(ind+1, len(nums)):
                if nums[j] > nums[ind] :
                    if map_[j][1]:
                        odd = True
                        res += 1
                    break
            for j in range(ind+1, len(nums)):
                if nums[j] < nums[ind]:
                    if map_[j][0]:
                        even = True
                    break
            map_[ind] = (odd, even)
        return res


s = Solution3()
s.jump([10, 13, 12, 14, 15])
