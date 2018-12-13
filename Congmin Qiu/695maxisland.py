class Solution:
    def mark(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0
        return self.mark(grid, i , j + 1) + self.mark(grid, i , j - 1) + self.mark(grid, i - 1,
                                                                                         j + 1) + self.mark(grid, i - 1,
                                                                                                            j - 1) + 1

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        """
        res = 0

        n_row = len(grid)
        n_col = len(grid[0])
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j] == 1:
                    res = max(res, self.mark(grid, i, j))
        return res


s = Solution()
grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
s.maxAreaOfIsland(grid)
