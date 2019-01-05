import itertools


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        from collections import defaultdict
        quot = defaultdict(dict)

        for (n1, n2), val in zip(equations, values):
            quot[n1][n1] = quot[n2][n2] = 1.0
            quot[n1][n2] = val
            quot[n2][n1] = 1 / val

        for k, i, j in itertools.permutations(quot, 3):
            if k in quot[i] and j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]

        return [quot[n1].get(n2, -1.0) for n1, n2 in queries]
    

s = Solution()
input = None
a = [["a", "b"], ["b", "c"]]
b = [2.0, 3.0]
c = [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]]
res = s.calcEquation(a, b, c)

print("")
