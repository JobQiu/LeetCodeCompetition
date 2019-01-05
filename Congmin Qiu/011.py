class Solution:

    def maxArea(self, A):
        i = 0
        j = len(A)-1
        res = 0
        while i < j:
            res = max(res, (j - i) * min(A[i], A[j]))
            if A[i] > A[j]:
                j -= 1
            else:
                i += 1
        return res


s = Solution()
input = None
res = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
assert res == 49

print("")

def minimize(self, test ):
    """ this is a method to ... """


    return test
