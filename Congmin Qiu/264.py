class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * n
        dp[0] = 1
        ind2, ind3, ind5 = 0,0,0

        for i in range(1, n):
            temp = min(dp[ind2] * 2, dp[ind3] * 3, dp[ind5] * 5)
            if temp == dp[ind2] * 2:
                ind2 +=1

            if temp == dp[ind3] * 3:
                ind3 +=1

            if temp == dp[ind5] * 5:
                ind5 +=1
            dp[i] = temp
        return dp[-1]

        pass
        
