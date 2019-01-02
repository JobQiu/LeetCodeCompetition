class Solution:
    def method(self, A ):

        s = set()
        for n in A:
            s.add(n)
        res = 0
        for n in A:
            if n-1 in s:
                continue
            count = 1
            while n in s:
                count += 1
                n = n+1
            res = max(res, count)
        return res


        pass

s = Solution()
input = None
res = s

print("")
