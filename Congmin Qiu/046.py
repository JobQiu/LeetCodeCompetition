class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(res, start ):
            if start == len(num):
                res.append(list(num))
                return

            for i in range(start, len(nums)):
                num[start], num[i] = num[i], num[start]
                helper(res, start+1)
                num[start], num[i] = num[i], num[start]


            pass
        res = []
        helper(res, 0)
        return res
        
