class Solution:
    def containsNearbyDuplicate(self, A, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        m = {}

        for i in range(len(A)):
            if A[i] in m and i - m[A[i]] <= k:
                return True
            m[A[i]] = i
        return False
        

s = Solution()
input = None
res = s

print("")
