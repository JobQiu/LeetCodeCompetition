from collections import defaultdict, deque


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.map = {}
        self.maxFreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        f = self.freq[x] + 1
        self.freq[x] = f
        self.maxFreq = max(self.maxFreq, f)
        if f not in self.map:
            self.map[f] = deque()
        self.map[f].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.map[self.maxFreq].pop()
        self.freq[x] = self.maxFreq - 1
        if len(self.map[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
param_2 = obj.pop()
