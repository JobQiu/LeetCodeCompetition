# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def flatten(self, nestedList ):
        for i in range(len(nestedList) -1, -1, -1):
            self.dq.append(nestedList[i])
        pass

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        from collections import deque
        self.dq = deque()
        self.flatten(nestedList)


    def next(self):
        """
        :rtype: int
        """

        return self.dq.pop().getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        dq = self.dq
        while len(dq) > 0:
            element = dq[-1]
            if element.isInteger():
                return True
            dq.pop()
            self.flatten(element.getList())
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
