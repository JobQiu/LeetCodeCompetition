class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class Solution:
    def __init__(self, capacity):
        self.capacity = capacity

        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        head = self.head
        tail = self.tail
        head.next= tail
        tail.prev = head

        self.key2node= {}
        self.count = 0

    def get(self, key):
        if key not in self.key2node:
            return  -1

        node = self.key2node[key]
        self.delete(node)
        self.put(node.key, node.val)
        return  node.val


    def delete(self, node):

        node.prev.next = node.next
        node.next.prev= node.prev
        self.count -= 1
        if node.key in self.key2node:
            self.key2node.pop(node.key);

    def put(self, key, val):
        if key in self.key2node:
            self.delete(self.key2node[key])

        if self.count == self.capacity:
            self.delete(self.tail.prev)


        node = Node(key, val)
        self.key2node[key] = node
        self.head.next.prev=  node
        node.next= self.head.next
        node.prev = self.head
        self.head.next = node

        self. count += 1



        pass
