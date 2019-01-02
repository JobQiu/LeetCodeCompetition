class Solution:
    def median(self, A, B):
        # 1. assure the length of A is larger than B
        if len(A) < len(B):
            return self.median(B, A)

        half = (len(A) + len(B)) // 2

        lo = 0
        hi = len(B)

        while lo <= hi:
            j = (lo + hi) // 2  # the index in B, the shorter one
            i = half - j  # the index in A, the longer one

            # A 1 2 3 4 5 6 7 8 9
            #             i = 5
            # B 1 4 6 7
            #     j = 1
            # i = 6 - 1 = 5

            if j < len(B) and B[j] < A[i - 1]:
                lo = j + 1
            elif j > 0 and A[i] < B[j - 1]:
                hi = j
            else:
                if j == len(B):
                    right_smallest = A[i]
                elif i == len(A):
                    right_smallest = B[j]
                else:
                    right_smallest = min(A[i], B[j])
                if (len(A) + len(B)) % 2 == 1:
                    return right_smallest

                if i == 0:
                    left_largest = B[j - 1]
                elif j == 0:
                    left_largest = A[i - 1]
                else:
                    left_largest = max(B[j - 1], A[i - 1])
                return (right_smallest + left_largest) / 2.0


s = Solution()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [1, 4, 6, 7]

# 1 1 2 3 4 4 5 6 6 7 7 8 9
# 0 1 2 3 4 5 6
res = s.median(A, B)
assert res == 5

A = []
res = s.median(A, B)
assert res == 5
print("")
