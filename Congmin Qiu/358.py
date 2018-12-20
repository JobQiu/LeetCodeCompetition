from collections import Counter, defaultdict


class Solution(object):
    def candidateChar(self, counter, valid, index):
        max_ = -1
        candidateChar = -1
        for k in counter:
            if counter[k] > max_ and index >= valid[k]:
                max_ = counter[k]
                candidateChar = k
        return candidateChar

    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        c = Counter(s)
        valid = defaultdict(int)

        res = ""

        for i in range(len(s)):
            candidateChar = self.candidateChar(c, valid, i)
            if candidateChar == -1:
                return ""

            c[candidateChar] -= 1
            valid[candidateChar] = i + k
            res += candidateChar

        return res
ss = Solution()
s = "aabbcc"
res = ss.rearrangeString(s,2)

