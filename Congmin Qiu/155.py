class MinStack:
    """
    an example here,
    3  2  1 4 5  0 6
    0 -1 -1 3 4 -1 0
    3  2  1 1 1  0 0
    """


    def __init__(self):
        """
        initialize your data structure here.
        """
        self.curmin = 0
        from collections import deque
        self.dq = deque()



    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        dq = self.dq
        if len(dq) == 0:
            dq.append(0)
            self.curmin = x
        else:
            dq.append( x - self.curmin)
            self.curmin = min(self.curmin, x)



    def pop(self):
        """
        :rtype: void
        """
        dq = self.dq
        if len(dq) <= 0:
            return
        temp = dq.pop();
        if temp < 0:
            self.curmin =  self.curmin - temp



    def top(self):
        """
        :rtype: int
        """
        dq = self.dq
        temp = dq[-1]
        if temp > 0:
            return self.curmin + temp
        else:
            return self.min



    def getMin(self):
        """
        :rtype: int
        """
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
