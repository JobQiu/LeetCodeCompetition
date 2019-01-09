from collections import defaultdict


class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        m = defaultdict(int)
        for giver, taker, val in transactions:
            m[giver] = m[giver] - val
            m[taker] = m[taker] + val

        def settle(start, debt):
            while start < len(debt) and debt[start] == 0:
                start += 1
            if start == len(debt):
                return 0

            r = float("inf")
            for i in range(start + 1, len(debt)):
                if debt[start] * debt[i] < 0:
                    debt[i] = debt[i] + debt[start]
                    r = min(r, 1 + settle(start + 1, debt))
                    debt[i] = debt[i] - debt[start]
            return r

            pass

        return settle(0, list(m.values()))


s = Solution()
input = None
res = s.minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]])

print("")
