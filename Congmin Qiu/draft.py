class Solution(object):
    def isMatch(self, s, p):
        a = 0
        b = 0
        m = 0
        i = -1
        while a < len(s):
            if b < len(p) and (p[b] == "?" or p[b] == s[a]):
                a = a + 1
                b = b + 1
            elif b < len(p) and p[b] == "*":
                i = b
                m = a
                b = b + 1
            elif i != -1:
                b = i + 1
                m = m + 1
                a = m
            else:
                return False
        while b < len(p):
            if p[b] == "*":
                b = b + 1
            else:
                break
        if b == len(p):
            return True
        else:
            return False


s = Solution()
res = s.isMatch("adceb", "*a*b")
