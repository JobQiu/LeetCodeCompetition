class Solution:
    def method(self, A ):
        left_max = A[0]
        right_max = A[-1]

        i = 0
        j = len(A) - 1
        res = 0
        while i < j :

            if left_max <= right_max:
                i += 1
                if A[i] < left_max:
                    res += left_max - A[i]
                else:
                    left_max = A[i]
            else:
                j -= 1
                if A[j] < right_max:
                    res += right_max - A[j]
                else:
                    right_max = A[j]
        return  res
        pass

s = Solution()
input = None
res = s

print("")
