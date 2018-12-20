class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        nums = [int(''.join(row), 2) for row in matrix]
        res = 0
        n = len(nums)
        for start in range(n):
            num = nums[start]
            end = start
            while end < n:
                num &= nums[end]
                if not num: break
                # find now the number of continous `1`
                cnt = 0
                new_num = num
                while new_num:
                    cnt += 1
                    new_num &= (num << cnt)
                res = max(res, (end - start + 1) * cnt)
                end += 1
        return res


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

s = Solution()
s.maximalRectangle(matrix)

