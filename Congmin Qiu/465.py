# -*- coding: utf-8 -*-

# in py2.7
from collections import defaultdict
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        
        debt = defaultdict(int)
        
        for give, take, val in transactions:
            debt[give] += val
            debt[take] -= val
            
        debt = debt.values()
        print(debt)
        
        def helper(start, debt):
            while start < len(debt) and debt[start] == 0:
                start += 1
            
            if start == len(debt):
                return  0
            
            res = float('inf')
            for i in range(start+1, len(debt)):
                if debt[i] * debt[start] < 0:
                    debt[i] += debt[start]
                    res = min(res, helper(start+1, debt)+1)
                    debt[i] -= debt[start]
            return res
                 
            pass
        
        res = helper(0, debt)
        print(res)
        return res
        
s = Solution()
res = s.minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])
#%%
            

                