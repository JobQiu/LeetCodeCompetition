# Tree
## recover-binary-search-tree

<p>Two elements of a binary search tree (BST) are swapped by mistake.</p>

<p>Recover the tree without changing its structure.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,3,null,null,2]

&nbsp;  1
&nbsp; /
&nbsp;3
&nbsp; \
&nbsp;  2

<strong>Output:</strong> [3,1,null,null,2]

&nbsp;  3
&nbsp; /
&nbsp;1
&nbsp; \
&nbsp;  2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [3,1,4,null,null,2]

  3
 / \
1   4
&nbsp;  /
&nbsp; 2

<strong>Output:</strong> [2,1,4,null,null,3]

  2
 / \
1   4
&nbsp;  /
 &nbsp;3
</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A solution using O(<em>n</em>) space is pretty straight forward.</li>
	<li>Could you devise a constant space solution?</li>
</ul>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## construct-binary-tree-from-preorder-and-inorder-traversal

<p>Given preorder and inorder traversal of a tree, construct the binary tree.</p>

<p><strong>Note:</strong><br />
You may assume that duplicates do not exist in the tree.</p>

<p>For example, given</p>

<pre>
preorder =&nbsp;[3,9,20,15,7]
inorder = [9,3,15,20,7]</pre>

<p>Return the following binary tree:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## construct-binary-tree-from-inorder-and-postorder-traversal

<p>Given inorder and postorder traversal of a tree, construct the binary tree.</p>

<p><strong>Note:</strong><br />
You may assume that duplicates do not exist in the tree.</p>

<p>For example, given</p>

<pre>
inorder =&nbsp;[9,3,15,20,7]
postorder = [9,15,7,20,3]</pre>

<p>Return the following binary tree:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7
</pre>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## minimum-depth-of-binary-tree

<p>Given a binary tree, find its minimum depth.</p>

<p>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<p>Given binary tree <code>[3,9,20,null,null,15,7]</code>,</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

<p>return its minimum&nbsp;depth = 2.</p>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## flatten-binary-tree-to-linked-list

<p>Given a binary tree, flatten it to a linked list in-place.</p>

<p>For example, given the following tree:</p>

<pre>
    1
   / \
  2   5
 / \   \
3   4   6
</pre>

<p>The flattened tree should look like:</p>

<pre>
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
</pre>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## populating-next-right-pointers-in-each-node-ii

<p>Given a binary tree</p>

<pre>
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
</pre>

<p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code>NULL</code>.</p>

<p>Initially, all next pointers are set to <code>NULL</code>.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>You may only use constant extra space.</li>
	<li>Recursive approach is fine, implicit stack space does not count as extra space for this problem.</li>
</ul>

<p><strong>Example:</strong></p>

<p>Given the following binary tree,</p>

<pre>
     1
   /  \
  2    3
 / \    \
4   5    7
</pre>

<p>After calling your function, the tree should look like:</p>

<pre>
     1 -&gt; NULL
   /  \
  2 -&gt; 3 -&gt; NULL
 / \    \
4-&gt; 5 -&gt; 7 -&gt; NULL
</pre>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## binary-tree-maximum-path-sum

<p>Given a <strong>non-empty</strong> binary tree, find the maximum path sum.</p>

<p>For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain <strong>at least one node</strong> and does not need to go through the root.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]

       <strong>1</strong>
      <strong>/ \</strong>
     <strong>2</strong>   <strong>3</strong>

<strong>Output:</strong> 6
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [-10,9,20,null,null,15,7]

&nbsp;  -10
&nbsp; &nbsp;/ \
&nbsp; 9 &nbsp;<strong>20</strong>
&nbsp; &nbsp; <strong>/ &nbsp;\</strong>
&nbsp; &nbsp;<strong>15 &nbsp; 7</strong>

<strong>Output:</strong> 42
</pre>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## count-complete-tree-nodes

<p>Given a <b>complete</b> binary tree, count the number of nodes.</p>

<p><b>Note: </b></p>

<p><b><u>Definition of a complete binary tree from <a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>:</u></b><br />
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2<sup>h</sup> nodes inclusive at the last level h.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 
    1
   / \
  2   3
 / \  /
4  5 6

<strong>Output:</strong> 6</pre>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## count-univalue-subtrees

 The content is locked, copy the problem here. 
https://leetcode.com/problems/count-univalue-subtrees/description/
<a href = "https://leetcode.com/problems/" count-univalue-subtrees> count-univalue-subtrees</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## verify-preorder-sequence-in-binary-search-tree

 The content is locked, copy the problem here. 
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
<a href = "https://leetcode.com/problems/" verify-preorder-sequence-in-binary-search-tree> verify-preorder-sequence-in-binary-search-tree</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## closest-binary-search-tree-value-ii

 The content is locked, copy the problem here. 
https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
<a href = "https://leetcode.com/problems/" closest-binary-search-tree-value-ii> closest-binary-search-tree-value-ii</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## binary-tree-longest-consecutive-sequence

 The content is locked, copy the problem here. 
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
<a href = "https://leetcode.com/problems/" binary-tree-longest-consecutive-sequence> binary-tree-longest-consecutive-sequence</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## largest-bst-subtree

 The content is locked, copy the problem here. 
https://leetcode.com/problems/largest-bst-subtree/description/
<a href = "https://leetcode.com/problems/" largest-bst-subtree> largest-bst-subtree</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## binary-tree-upside-down

 The content is locked, copy the problem here. 
https://leetcode.com/problems/binary-tree-upside-down/description/
<a href = "https://leetcode.com/problems/" binary-tree-upside-down> binary-tree-upside-down</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## lowest-common-ancestor-of-a-binary-tree

<p>Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes p&nbsp;and q&nbsp;as the lowest node in T that has both p&nbsp;and q&nbsp;as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>Given the following binary tree:&nbsp; root =&nbsp;[3,5,1,6,2,0,8,null,null,7,4]</p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:</strong> 3
<strong>Explanation: </strong>The LCA of nodes <code>5</code> and <code>1</code> is <code>3.</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:</strong> 5
<strong>Explanation: </strong>The LCA of nodes <code>5</code> and <code>4</code> is <code>5</code>, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
<li>All of the nodes&#39; values will be unique.</li>
<li>p and q are different and both values will&nbsp;exist in the binary tree.</li>
</ul>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## sum-of-left-leaves

<p>Find the sum of all left leaves in a given binary tree.</p>

<p><b>Example:</b>
<pre>
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values <b>9</b> and <b>15</b> respectively. Return <b>24</b>.
</pre>
</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## path-sum-iii

<p>You are given a binary tree in which each node contains an integer value.</p>

<p>Find the number of paths that sum to a given value.</p>

<p>The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).</p>

<p>The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

<p><b>Example:</b>
<pre>
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    <b>5</b>   <b>-3</b>
   <b>/</b> <b>\</b>    <b>\</b>
  <b>3</b>   <b>2</b>   <b>11</b>
 / \   <b>\</b>
3  -2   <b>1</b>

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
</pre>
</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## delete-node-in-a-bst

<p>Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.</p>

<p>Basically, the deletion can be divided into two stages:
<ol>
<li>Search for a node to remove.</li>
<li>If the node is found, delete the node.</li>
</ol>
</p>

<p><b>Note:</b> Time complexity should be O(height of tree).</p>

<p><b>Example:</b>
<pre>
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
</pre>
</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-mode-in-binary-search-tree

<p>Given a binary search tree (BST) with duplicates, find all the <a href="https://en.wikipedia.org/wiki/Mode_(statistics)" target="_blank">mode(s)</a> (the most frequently occurred element) in the given BST.</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <b>less than or equal to</b> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <b>greater than or equal to</b> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>

<p>For example:<br />
Given BST <code>[1,null,2,2]</code>,</p>

<pre>
   1
    \
     2
    /
   2
</pre>

<p>&nbsp;</p>

<p>return <code>[2]</code>.</p>

<p><b>Note:</b> If a tree has more than one mode, you can return them in any order.</p>

<p><b>Follow up:</b> Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).</p>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## most-frequent-subtree-sum

<p>
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
</p>

<p><b>Examples 1</b><br>
Input:
<pre>
  5
 /  \
2   -3
</pre>
return [2, -3, 4], since all the values happen only once, return all of them in any order.
</p>

<p><b>Examples 2</b><br>
Input:
<pre>
  5
 /  \
2   -5
</pre>
return [2], since 2 happens twice, however -5 only occur once.
</p>

<p><b>Note:</b>
You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## construct-binary-tree-from-string

 The content is locked, copy the problem here. 
https://leetcode.com/problems/construct-binary-tree-from-string/description/
<a href = "https://leetcode.com/problems/" construct-binary-tree-from-string> construct-binary-tree-from-string</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## convert-bst-to-greater-tree

<p>Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.</p>

<p>
<b>Example:</b>
<pre>
<b>Input:</b> The root of a Binary Search Tree like this:
              5
            /   \
           2     13

<b>Output:</b> The root of a Greater Tree like this:
             18
            /   \
          20     13
</pre>
</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## kill-process

 The content is locked, copy the problem here. 
https://leetcode.com/problems/kill-process/description/
<a href = "https://leetcode.com/problems/" kill-process> kill-process</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## add-one-row-to-tree

<p>Given the root of a binary tree, then value <code>v</code> and depth <code>d</code>, you need to add a row of nodes with value <code>v</code> at the given depth <code>d</code>. The root node is at depth 1. </p>

<p>The adding rule is: given a positive integer depth <code>d</code>, for each NOT null tree nodes <code>N</code> in depth <code>d-1</code>, create two tree nodes with value <code>v</code> as <code>N's</code> left subtree root and right subtree root. And <code>N's</code> <b>original left subtree</b> should be the left subtree of the new left subtree root, its <b>original right subtree</b> should be the right subtree of the new right subtree root. If depth <code>d</code> is 1 that means there is no depth d-1 at all, then create a tree node with value <b>v</b> as the new root of the whole original tree, and the original tree is the new root's left subtree.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

<b>v = 1</b>

<b>d = 2</b>

<b>Output:</b> 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

<b>v = 1</b>

<b>d = 3</b>

<b>Output:</b> 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The given d is in range [1, maximum depth of the given tree + 1].</li>
<li>The given binary tree has at least one tree node.</li>
</ol>
</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-duplicate-subtrees

<p>Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any <b>one</b> of them.</p>

<p>Two trees are duplicate if they have the same structure with same node values.</p>

<p><b>Example 1: </b></p>

<pre>
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>

<p>The following are two duplicate subtrees:</p>

<pre>
      2
     /
    4
</pre>

<p>and</p>

<pre>
    4
</pre>
Therefore, you need to return above trees&#39; root in the form of a list.
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

