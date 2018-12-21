Readable Notebook for leetcode

095 Unique Binary Search Trees II

tags: []

<img src="https://ws2.sinaimg.cn/large/006tNbRwly1fye6fa2dk1j30rs0hcac5.jpg" width="250px"/>

---

114 Flatten Binary Tree to Linked List

tags: [manipulation of pointers]

Dec 20, 2018 8:46 PM

The question is as follows:
<img src="https://ws4.sinaimg.cn/large/006tNbRwly1fye5vwonfdj30640l63yu.jpg" width="250px"/>

An elegant solution is to preorder traverse the tree and append each value to a dummy head.

<img src="https://ws2.sinaimg.cn/large/006tNbRwly1fye62p4qcpj30fc0jaac7.jpg" width="250px"/>

The idea is to first flatten the right sub tree, and put its root to the self.prev
then flatten the left sub tree, put the right-flatten linked tree to the tail of left-linked Tree
the put this left linked tree to the root.

因为每次pre 保存的都是比当前root大的值，这个traverse实际上是从最大到最小的，所以6会被append到5后面，5会被append到4后面。。。

<img src="https://ws4.sinaimg.cn/large/006tNbRwly1fye5uaja9aj30g80b6q3t.jpg" width="250px"/>

`Take-away`



----
