class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        S = S.upper().replace("-", "")
        firstL = len(S)%K

        if firstL == 0:
            res = ""
        else:
            res = S[0:firstL] + "-"

        while firstL <= len(S):
            res += S[firstL:firstL+K] + "-"
            firstL += K


        return res[:-1]
