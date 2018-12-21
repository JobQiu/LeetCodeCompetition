class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.helper(0,0,[],n, "")


    def helper(self, l, r ,res, max, cur):
        if len(cur) == max * 2:
            res.append(cur)
            return

        if l < max:
            self.helper(l+1,r, res, max, cur+'(')
        if r < l:
            self.helper(l, r+1, res, max, cur +')')
