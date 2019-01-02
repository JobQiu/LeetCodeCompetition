class Solution:
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int

        [3,4,-1,1]
        """

        for i in range(len(A)):
            while A[i] != i + 1 and A[i] > 0 and A[i] <= len(A):
                if A[A[i] - 1] == A[i]:
                    break

                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]

        print("")



s = Solution()
input = None
res = s.firstMissingPositive([3, 4, -1, 1])

print("")
