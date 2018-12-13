class Solution:
    def isAlive(self, board, i, j):
        if i < 0:
            return 0
        if j < 0:
            return 0
        if i >= len(board):
            return 0
        if j >= len(board[0]):
            return 0

        if board[i][j] % 2 == 1:
            return 1
        else:
            return 0

    def count(self, board, i, j):

        return self.isAlive(board, i - 1, j - 1) + self.isAlive(board, i - 1, j) + self.isAlive(board, i - 1,
                                                                                                j + 1) + self.isAlive(
            board, i, j - 1) + self.isAlive(board, i, j + 1) + self.isAlive(board, i + 1, j - 1) + self.isAlive(
            board, i + 1, j) + self.isAlive(board, i + 1, j + 1)

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n_row = len(board)
        n_col = len(board[0])

        for i in range(n_row):
            for j in range(n_col):
                n_live = self.count(board, i, j)
                if board[i][j] == 1:
                    if n_live == 2 or n_live == 3:
                        board[i][j] = 3
                    else:
                        board[i][j] = 1
                else:
                    if n_live == 3:
                        board[i][j] = 2

        for i in range(n_row):
            for j in range(n_col):
                board[i][j] = board[i][j] // 2


s = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
s.gameOfLife(board)
