class Solution:
    def method(self, A ):

        max_ = A[0]
        min_ = A[0]
        res = A[0]

        for i in range(1, len(A)):
            if A[i] < 0:
                max_, min_ = min_, max_
            max_ = max(max_ * A[i], A[i])
            min_ = min(min_ * A[i], A[i])
            res = max(max_, res)
        return res

        pass

s = Solution()
input = None
res = s

print("")
