class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        3,3,3,1,2,1,1,2,3,3,4
              i
                        j
        """
        start = 0
        end = 0
        res = 0
        m = {}

        while end < len(tree):
            if tree[end] in m:
                m[tree[end]] += 1
            else:
                m[tree[end]] = 1

            while len(m) > 2:
                m[tree[start]] -= 1
                if m[tree[start]] == 0:
                    m.pop(tree[start]);
                start += 1

            res = max(res, end-start+1)

            end += 1
        return res
