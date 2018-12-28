Readable Notebook for leetcode


Pool：
2. Tree 2.5/4.5 页
1. Math 4/5 页
3. Stack 1/2 + Heap 1/1.5
5. DP 5/6
9. Binary search 3/3 + Design 2/2
8. Array 4/7
6. LinkedList 2/2 + Hash table 3/4
8. DFS 4/4 + BFS 2/2
11. Greedy 2/2 + Backtracking 2/2
13. String 4/5

| id  | Content                | Total Page | 预计       | 开学后            |
| --- | ---------------------- | ---------- | ---------- | ----------------- |
| 1   | Tree                   | 4.5        | 28号总结完 | 日刷经典，日增3道 |
| 2   | String                 | 5          | 30号总结完 | 日刷经典，日增3道 |
| 3   | Math                   | 5          | 1号总结完  | 日刷经典，日增3道 |
| 4   | Array                  | 7          | 3号总结完  | 日刷经典，日增3道 |
| 5   | DP                     | 6          | 6号总结完  | 日刷经典，日增3道 |
| 6   | Binary Search + Design | 5          | 刷         |                   |
| 7   | Stack + Heap           | 3.5        | 刷+总结    |                   |
| 8   | LinkedList + Hash      | 6          | 刷         |                   |
| 9   | DFS BFS                | 6          | 刷         |                   |
| 10  | Greedy + Backtracking  | 4          | 刷         |                   |


每天一个专题，然后寻找网上别人的总结，对这个topic下有哪些类的题目有个基本的认识。
第一遍就bug_free的放入 filter文件，check一下discussion， 如果有elegant的代码就不放入filter文件
discussion里面每个vote超过100的都看一下，解释一遍。



---


230 Kth Smallest Element in a BST

Dec 20, 2018 9:50 PM
玩了一个小时，蓝过！
Dec 20, 2018 10:58 PM

---


199 Binary Tree Right Side View

Dec 20, 2018 9:44 PM

<img src="https://ws3.sinaimg.cn/large/006tNbRwly1fye7wciqv2j316q0gggnt.jpg" width="400px"/>

The first idea is to use a BFS and put each layer's last element to the result list.

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        q = queue.Queue()
        q.put(root);
        cur = None

        while q.qsize()>0:
            size = q.qsize()
            for i in range(size):
                cur = q.get()
                if cur.left != None:
                    q.put(cur.left)
                if cur.right != None:
                    q.put(cur.right);

            res.append(cur.val)
        return res
```

it works, let's see if there're some more elegant solutions?



---


111 Minimum Depth of Binary Tree

Dec 20, 2018 9:41 PM

```

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1


        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0:
            return right+1
        if right == 0:
            return left+1
        return min(left, right)+1


```


---

257 Binary Tree Paths
Dec 20, 2018 9:39 PM
秒解

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root == None:
            return res

        if root.left == None and root.right == None:
            res.append("{}".format(root.val))
            return res

        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        for side in (left, right):
            for path in side:
                res.append("{}->".format(root.val) + path)
        return  res
```

---

543 Diameter of Binary Tree

Dec 20, 2018 9:26 PM

Easy, 秒解

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.maxDepth = 0

    def maxD(self, root):
        if root == None:
            return 0
        left = self.maxD(root.left)
        right = self.maxD(root.right)
        if left+right > self.maxDepth:
            self.maxDepth = left+right
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxD(root)
        return self.maxDepth
```


---

222 Count Complete Tree Nodes

Dec 20, 2018 9:05 PM

<img src="https://ws1.sinaimg.cn/large/006tNbRwly1fye6v55qjvj318q0j4tay.jpg" width="400px"/>

<img src="https://ws2.sinaimg.cn/large/006tNbRwly1fye72b7huyj30ub0u079k.jpg" width="350px"/>

These guys are really brilliant!

```
class Solution:

    def countNodes(self, root ):
      leftDepth = self.leftDepth(root)
      rightDepth = self.rightDepth(root)
      if leftDepth == rightDepth:
        return (1 << leftDepth) - 1
      else:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def rightDepth(self, root):
      dep = 0
      while root != None:
        root = root.right
        dep += 1
      return dep

    def leftDepth(self, root ):
      dep = 0
      while root != None:
        root = root.left
        dep += 1
      return dep
```

---

095 Unique Binary Search Trees II

tags: []

Dec 20, 2018 8:55 PM

<img src="https://ws2.sinaimg.cn/large/006tNbRwly1fye6fa2dk1j30rs0hcac5.jpg" width="250px"/>

Brute Force

iterate from 1 to n, split the array into left and right, combine all their combinations and return.

```
class Solution:
    def generateSubTrees(self, start, end ):
        """
        start = [1 inclusive
        end = 4) not inclusive

        when i = 1
        left = generateSubTrees(1,0)
        right =
        """
        res = []

        if start == end:
            res.append(None)
            return res

        if start == end-1:
            res.append(TreeNode(start))
            return res

        for sp in range(start, end):
            left = self.generateSubTrees(start, sp)
            right = self.generateSubTrees(sp+1,end)

            for l in left:
                for r in right:
                    root = TreeNode(sp)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        if n==0:
            return []

        return self.generateSubTrees(1, n+1)

```

---

114 Flatten Binary Tree to Linked List

tags: [manipulation of pointers]

Dec 20, 2018 8:46 PM

The question is as follows:

<img src="https://ws4.sinaimg.cn/large/006tNbRwly1fye5vwonfdj30640l63yu.jpg" width="80px"/>

An elegant solution is to preorder traverse the tree and append each value to a dummy head.

<img src="https://ws2.sinaimg.cn/large/006tNbRwly1fye62p4qcpj30fc0jaac7.jpg" width="250px"/>

The idea is to first flatten the right sub tree, and put its root to the self.prev
then flatten the left sub tree, put the right-flatten linked tree to the tail of left-linked Tree
the put this left linked tree to the root.

因为每次pre 保存的都是比当前root大的值，这个traverse实际上是从最大到最小的，所以6会被append到5后面，5会被append到4后面。。。

<img src="https://ws4.sinaimg.cn/large/006tNbRwly1fye5uaja9aj30g80b6q3t.jpg" width="250px"/>

`Take-away`



----
