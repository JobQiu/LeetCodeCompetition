class Solution:
    def path(self, n, m):
        """
        n: number of row
        m: number of col
        0 0 0 0  0
        1 1 2 4  1
        0 1 2 5  2
        0 0 1 3  3
        0 0 0 1  4
        0 0 0    5

        """

        dp = [[0] * (m) for _ in range(n + 2)]
        dp[1][0] = 1

        for col in range(1, m):
            for row in range(1, n + 1):
                dp[row][col] = dp[row - 1][col - 1] + dp[row][col - 1] + dp[row + 1][col - 1]

        return dp[1][-1]

    def path1d(self, n, m):
        dp = [0] * (n + 2)
        dp[1] = 1

        for col in range(1, m):
            temp = [0] * (n + 2)
            for row in range(1, n + 1):
                temp[row] = dp[row - 1] + dp[row] + dp[row + 1]
            dp = temp
        return dp[1]

    def pathPassingPoints(self, points, n, m):
        """
        """
        points.sort(key=lambda x: x[0])
        


    def passPoints(self, points, n, m):

        """
        """
        points.append([0, 0]);
        points.append([0, m - 1]);

        points.sort(key=lambda x: x[0])

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            if abs(y1 - y2) > abs(x1 - x2):
                return False
        return True

        pass


s = Solution()
input = None
res = s.path1d(n=4, m=14)
assert res == 37701

print("")
