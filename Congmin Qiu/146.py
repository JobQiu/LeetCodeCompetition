class Node:
    def __init__(self, val, key ):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.next= self.head
        self.count = 0
        self.m = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.m :
            return  -1
        node = self.m[key]
        self.delete(node)
        self.put(key, node.val)
        return  node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.m:
            self.delete(self.m[key])

        if self.count == self.c:
            self.delete(self.tail.prev)


        node = Node(value, key)
        head = self.head
        self.m[key] = node
        node.next = head.next
        node.prev = head
        head.next = node
        node.next.prev= node
        self.count += 1

        pass

    def delete(self, node ):
        if node == None :
            return

        node.prev.next = node.next
        node.next.prev = node. prev
        self.count -= 1
        if node.key in self.m:

            self.m.pop(node.key)

        pass
