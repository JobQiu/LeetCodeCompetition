class Solution:
    def maxisum(self, A):
        if len(A) == 0:
            return 0

        res = A[0]
        max_ = A[0]
        for i in range(1, len(A)):
            max_ = max(max_ + A[i], A[i])
            res = max(max_, res)
        return res
