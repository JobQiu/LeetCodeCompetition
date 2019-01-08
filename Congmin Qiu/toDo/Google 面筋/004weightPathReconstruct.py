import copy


class Solution:
    path = ""

    def smallestSumPath(self, grid, storePath=False):
        """
        """
        m = {}

        def p2s(row, col):
            return "{}-{}".format(row, col)

        grid_ = copy.deepcopy(grid)
        num_row, num_col = len(grid), len(grid[0])
        # for the first row
        for i in range(1, num_col):
            m[p2s(0, i)] = p2s(0, i - 1)
            grid_[0][i] += grid_[0][i - 1]

        # 5 14 , 9 - > 5, 19, 28
        for j in range(1, num_row):
            m[p2s(j, 0)] = p2s(j - 1, 0)
            grid_[j][0] += grid_[j - 1][0]

        for row in range(1, num_row):
            for col in range(1, num_col):
                if grid_[row][col - 1] > grid_[row - 1][col]:
                    m[p2s(row, col)] = p2s(row - 1, col)
                    grid_[row][col] += grid_[row - 1][col]
                else:
                    m[p2s(row, col)] = p2s(row, col - 1)
                    grid_[row][col] += grid_[row][col - 1]
        m["0-0"] = None
        if storePath:
            end = p2s(num_row - 1, num_col - 1)
            while end != None:
                self.path = end + " " + self.path
                end = m[end]

        return grid_[-1][-1]


s = Solution()
input = None
res = s.smallestSumPath([[1, 4, 5, 3, 6], [4, 6, 1, 2, 1], [1, 4, 6, 0, 7]], storePath=True)
print(s.path)

print("")
