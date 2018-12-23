class Solution:
    def calculateMinimumHP(self, d):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        num_row = len(d)
        num_col = len(d[0])

        d.reverse()
        for row in d:
            row.reverse()
        d[0][0] = 1 - min(d[0][0], 0)

        for i in range(1, num_row):
            if d[0]
            d[0][i] = 1 - min(d[0][i], 0) + d[0][i - 1]

        for i in range(1, num_col):
            d[i][0] = 1 - min(d[i][0], 0) + d[i - 1][0]

        for i in range(1, num_row):
            for j in range(1, num_col):
                d[i][j] = 1 - min(d[i][j], 0) + min(d[i - 1][j], d[i][j - 1])
        return d[-1][-1]


d = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
s = Solution()
res = s.calculateMinimumHP(d)
print(res)
