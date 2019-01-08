import copy


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.mat = matrix
        self.A = copy.deepcopy(matrix)
        A = self.A

        self.num_row = len(matrix)
        self.num_col = len(matrix[0])

        for i in range(1, self.num_row):
            A[i][0] += A[i - 1][0]

        for i in range(1, self.num_col):
            A[0][i] += A[0][i - 1]

        for i in range(1, self.num_row):
            for j in range(1, self.num_col):
                A[i][j] += A[i][j - 1] + A[i - 1][j] - A[i - 1][j - 1]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """

        A = self.A
        diff = val - self.mat[row][col]
        self.mat[row][col] = val
        for i in range(row, self.num_row):
            for j in range(col, self.num_col):
                A[i][j] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        a = self.A[row2][col2]
        b = self.sumR(row1 - 1, col1 - 1)
        c = self.sumR(row1 - 1, col2)
        d = self.sumR(row2, col1 - 1)

        return self.A[row2][col2] + self.sumR(row1 - 1, col1 - 1) - self.sumR(row1 - 1, col2) - self.sumR(row2,
                                                                                                          col1 - 1)

    def sumR(self, row, col):
        if row < 0 or col < 0:
            return 0
        return self.A[row][col]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

["NumMatrix", "update", "update", "update", "sumRegion"]
# [],,[1,1,-3],[0,1,1],[0,0,1,1]]
s = NumMatrix([[2, 4], [-3, 5]])
input = None
# res = s.sumRegion(2, 1, 4, 3)
res = s.update(0, 1, 3)
res = s.sumRegion(2, 1, 4, 3)

print("")
