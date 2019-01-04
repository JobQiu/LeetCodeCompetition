class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        height = []
        for b in buildings:
            height.append((b[0], -b[2]))
            height.append((b[1], b[2]))

        height.sort(key = lambda x:x[0])
        height.sort(key = lambda x:x[1])
