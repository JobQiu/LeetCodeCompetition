class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.new = []
        self.old = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.new.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        self.old.pop()



    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return  self.old[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (len(self.new) + len(self.old)) == 0

    def move(self):
        while len(new) > 0:
            old.append(new.pop())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
