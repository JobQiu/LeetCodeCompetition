class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        fin = []

        def pat(st, curr):
            if len(st) == 0:
                fin.append(list(curr))
                return
            for i in range(len(st)):
                now = st[:i + 1]
                if now == now[::-1]:
                    curr.append(now)
                    pat(st[i + 1:], curr)
                    curr.pop()

        pat(s, [])
        return fin


s = Solution()
s.partition("aabbbbcc")
