class Solution:
    def method(self, n):
        res = []
        res.append([1])

        for i in range(1, n):
            A = [0] + res[-1]
            B = res[-1] + [0]
            temp = [A[j] + B[j] for j in range(len(A))]
            res.append(temp)
        return res




        pass

s = Solution()
input = None
res = s

print("")
