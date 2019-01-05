class Solution:
    def mask(self, grid, i, j, num_row, num_col ):
        if i

        pass
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        num_row = len(grid)
        num_col = len(grid[0])

        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == "1":
                    self.mask(grid, i, j, num_row, num_col)
                    count += 1

        return  count
