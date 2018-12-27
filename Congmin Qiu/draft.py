class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        opt, i = [0,0], 1
        for j in range(2,len(A)):
            if A[j]-A[j-1] == A[j-1]-A[j-2]:
                opt.append(opt[j-1]+i)
                i += 1
            else:
                opt.append(opt[j-1])
                i = 1
        return opt[-1]
