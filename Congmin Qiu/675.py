class Solution:
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """

        nrow = len(forest)
        ncol = len(forest[0])

        forest.append([0]*ncol) # why this?
        for row in forst :
            row.append(0)

        trees = {(i, j) for i in range(nrow) for j in range(ncol) if forest[i][j] > 1}

        canReach = {(0,0)}
        stack = [(0,0)]
        # is deque better than stack in python as well?

        while stack:
            i, j = stack.pop();
            for i2, j2 in ((i-1,j), (i+1, j), (i, j-1), (i, j+1)):
                if forest[i2][j2] != 0 and (i2, j2) not in canReach:
                    canReach.add((i2,j2));
                    Stack>
