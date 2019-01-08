import itertools
from collections import defaultdict

class Solution2:
    def calcEquation(self, equations, values, queries):

        edges = defaultdict(list)
        def initialize():
            for idx, (a,b) in enumerate(equations):
                v = values[idx]
                edges[a].append([b, v])
                edges[b].append([a,1.0/v])
            pass

        def dfs(start, end, visited, total):
            if start == end:
                if start in edges:
                    return total
                else:
                    return -1.0
            visited.add(start);

            for next_, cost in edges[start]:
                res = dfs(next_, end, visited, total * cost)
                if res != -1:
                    return res
            return -1.0

        initialize()


        return map(lambda (start, end) : dfs(start, end, set(), 1.0), queries)




        pass




class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        d = defaultdict(int)
        for (n1, n2), val in zip(equations, values):
            d[n1][n1] = d[n2][n2] = 1.0
            d[n1][n2] = val
            d[n2][n1] = 1.0/val

        for i, j, k in itertools.permutations(d,3):
            if j in d[i] and k in d[j]:
                d[i][k] = d[i][j] * d[j][k]
        res = []
        for (n1, n2) in queries:
            if n1 not in d or n2 not in d[n1]:
                res.append(-1.0)
            else:
                res.append(d[n1][n2])
        return res




s = Solution()
input = None
a = [["a", "b"], ["b", "c"]]
b = [2.0, 3.0]
c = [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]]
res = s.calcEquation(a, b, c)

print("")
