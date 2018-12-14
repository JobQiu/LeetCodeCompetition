class Solution:
    def backtrack(self, candidates, remain, curIndex, resList, soFarList):
        if remain < 0:
            return

        elif remain == 0:
            resList.append(list(soFarList))
            return

        for i in range(curIndex, len(candidates)):
            self.backtrack(candidates, remain - candidates[i], i, resList, soFarList + [candidates[i]])

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        resList = []
        soFarList = []
        self.backtrack(candidates, target, 0, resList, soFarList)

        return resList


s = Solution()

candidates = [2, 3, 6, 7]
target = 7
s.combinationSum(candidates, target)
