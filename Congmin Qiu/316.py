from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s):
        # 1. firstly decide the first char

        c = Counter(s)
        pos = 0

        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break

        return "" if len(s) == 0 else s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ""))

        pass
