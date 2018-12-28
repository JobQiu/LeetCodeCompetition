# 1. DP

## 1.1 一维DP

`5 和 647 很像，都是extend类型的, if you can solve the 5 in the fastest way, you can skip 5 and 647.`

### 5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring/description/

<p>Given a string <strong>s</strong>, find the longest palindromic substring in <strong>s</strong>. You may assume that the maximum length of <strong>s</strong> is 1000.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Note:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>


```
class Solution:
    def extend(self, s, i, j ):
        while i>=0 and j <len(s) and s[i] == s[j]:
            i-=1
            j+=1
        if j-i-1>self.maxLen:
            self.maxLen = j-i-1
            self.start = i+1

    def longestPalindrome(self, s):
        """ :type s: str :rtype: str """
        self.start = 0
        self.maxLen = 0

        for i in range(len(s)):
            self.extend(s, i, i)
            self.extend(s, i, i+1)
        return s[self.start: self.start+self.maxLen]
"""
one improvement according to the faster solution, is that your can skip those whose length is less than the current maxLen.
"""
```


---

### 647. palindromic-substrings

https://leetcode.com/problems/palindromic-substrings/description/

<p>
Given a string, your task is to count how many palindromic substrings in this string.
</p>

<p>
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "abc"
<b>Output:</b> 3
<b>Explanation:</b> Three palindromic strings: "a", "b", "c".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "aaa"
<b>Output:</b> 6
<b>Explanation:</b> Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The input string length won't exceed 1000.</li>
</ol>
</p>

```
class Solution:
    def extend(self, s, i, j ):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            self.count += 1

    def countSubstrings(self, s):
        """ :type s: str :rtype: int """
        self.count = 0
        for i in range(len(s)):
            self.extend(s, i, i)
            self.extend(s, i, i+1)
        return self.count
```

----

`try to explain 53, don't need to solve 53, relative easy.`

### 53. maximum-subarray

<p>Given an integer array <code>nums</code>, find the contiguous subarray&nbsp;(containing at least one number) which has the largest sum and return its sum.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [-2,1,-3,4,-1,2,1,-5,4],
<strong>Output:</strong> 6
<strong>Explanation:</strong>&nbsp;[4,-1,2,1] has the largest sum = 6.
</pre>

<p><strong>Follow up:</strong></p>

<p>If you have figured out the O(<em>n</em>) solution, try coding another solution using the divide and conquer approach, which is more subtle.</p>

```
class Solution:
    def maxSubArray(self, nums):
        """:type nums: List[int] :rtype: int"""
        res = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            res = max(res, curSum)
        return res

```

---

### 152. maximum-product-subarray
https://leetcode.com/problems/maximum-product-subarray

<p>Given an integer array&nbsp;<code>nums</code>, find the contiguous subarray within an array (containing at least one number) which has the largest product.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,3,-2,4]
<strong>Output:</strong> <code>6</code>
<strong>Explanation:</strong>&nbsp;[2,3] has the largest product 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;The result cannot be 2, because [-2,-1] is not a subarray.</pre>

```
class Solution:
    def maxProduct(self, nums):
        """:type nums: List[int] :rtype: int"""
        max_ = min_ = res = nums[0]
        for i in range(1, len(nums)):
            max_, min_  = max(nums[i], max_*nums[i], min_*nums[i]) , min(nums[i], max_*nums[i], min_*nums[i])
            res = max(max_, res, min_)
        return res
```

### 413 arithmetic slices

https://leetcode.com/problems/arithmetic-slices/description/


<p>A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.</p>

<p>For example, these are arithmetic sequence:</p>
<pre>1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>The following sequence is not arithmetic.</p> <pre>1, 1, 2, 5, 7</pre>
<br/>

<p>A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 less or equal to P less than  Q less than N.</p>

<p>A slice (P, Q) of array A is called arithmetic if the sequence:<br/>
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 less than Q.</p>

<p>The function should return the number of arithmetic slices in the array A. </p>
<br/>

<p><b>Example:</b>
<pre>
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
</pre>

`注意是连续的，跳着的不算，比如 1，2，3，4，5， [1，3，5]就不算。`

```

```

---

### 338. counting-bits


<p>Given a non negative integer number <b>num</b>. For every numbers <b>i</b> in the range <b>0 &le; i &le; num</b> calculate the number of 1&#39;s in their binary representation and return them as an array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">2</span>
<strong>Output: </strong><span id="example-output-1">[0,1,1]</span></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">5</span>
<strong>Output: </strong><code>[0,1,1,2,1,2]</code>
</pre>

<p><b>Follow up:</b></p>

<ul>
	<li>It is very easy to come up with a solution with run time <b>O(n*sizeof(integer))</b>. But can you do it in linear time <b>O(n)</b> /possibly in a single pass?</li>
	<li>Space complexity should be <b>O(n)</b>.</li>
	<li>Can you do it like a boss? Do it without using any builtin function like <b>__builtin_popcount</b> in c++ or in any other language.</li>
</ul>

---



### 279. perfect-squares


<p>Given a positive integer <i>n</i>, find the least number of perfect square numbers (for example, <code>1, 4, 9, 16, ...</code>) which sum to <i>n</i>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>12</code>
<b>Output:</b> 3
<strong>Explanation: </strong><code>12 = 4 + 4 + 4.</code></pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <i>n</i> = <code>13</code>
<b>Output:</b> 2
<strong>Explanation: </strong><code>13 = 4 + 9.</code></pre>

`DP方法 和 数学方法，hint只有1，2，3，4四种可能，公式是 4k*(8m+7) -> 4`

----



## 1.2 二维DP

### 10. regular-expression-matching


<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement regular expression matching with support for <code>&#39;.&#39;</code> and <code>&#39;*&#39;</code>.</p>

<pre>
&#39;.&#39; Matches any single character.
&#39;*&#39; Matches zero or more of the preceding element.
</pre>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>s</code>&nbsp;could be empty and contains only lowercase letters <code>a-z</code>.</li>
	<li><code>p</code> could be empty and contains only lowercase letters <code>a-z</code>, and characters like&nbsp;<code>.</code>&nbsp;or&nbsp;<code>*</code>.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;a*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; means zero or more of the precedeng&nbsp;element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;ab&quot;
p = &quot;.*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aab&quot;
p = &quot;c*a*b&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;c can be repeated 0 times, a can be repeated 1 time. Therefore it matches &quot;aab&quot;.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;mississippi&quot;
p = &quot;mis*is*p*.&quot;
<strong>Output:</strong> false
</pre>

---

### 85. maximal-rectangle


<p>Given a 2D binary matrix filled with 0&#39;s and 1&#39;s, find the largest rectangle containing only 1&#39;s and return its area.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
  [&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;0&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;,&quot;<strong>1</strong>&quot;],
  [&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 6
</pre>

---

### 312. burst-balloons


<p>Given <code>n</code> balloons, indexed from <code>0</code> to <code>n-1</code>. Each balloon is painted with a number on it represented by array <code>nums</code>. You are asked to burst all the balloons. If the you burst balloon <code>i</code> you will get <code>nums[left] * nums[i] * nums[right]</code> coins. Here <code>left</code> and <code>right</code> are adjacent indices of <code>i</code>. After the burst, the <code>left</code> and <code>right</code> then becomes adjacent.</p>

<p>Find the maximum coins you can collect by bursting the balloons wisely.</p>

<p><b>Note:</b></p>

<ul>
	<li>You may imagine <code>nums[-1] = nums[n] = 1</code>. They are not real therefore you can not burst them.</li>
	<li>0 &le; <code>n</code> &le; 500, 0 &le; <code>nums[i]</code> &le; 100</li>
</ul>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[3,1,5,8]</code>
<b>Output:</b> <code>167
<strong>Explanation: </strong></code>nums = [3,1,5,8] --&gt; [3,5,8] --&gt;   [3,8]   --&gt;  [8]  --&gt; []
&nbsp;            coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
</pre>


---

### 120. triangle


<p>Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.</p>

<p>For example, given the following triangle</p>

<pre>
[
     [<strong>2</strong>],
    [<strong>3</strong>,4],
   [6,<strong>5</strong>,7],
  [4,<strong>1</strong>,8,3]
]
</pre>

<p>The minimum path sum from top to bottom is <code>11</code> (i.e., <strong>2</strong> + <strong>3</strong> + <strong>5</strong> + <strong>1</strong> = 11).</p>

<p><strong>Note:</strong></p>

<p>Bonus point if you are able to do this using only <em>O</em>(<em>n</em>) extra space, where <em>n</em> is the total number of rows in the triangle.</p>

---

### 188 & 123 best-time-to-buy-and-sell-stock-iv


<p>Say you have an array for which the <i>i</i><sup>th</sup> element is the price of a given stock on day <i>i</i>.</p>

<p>Design an algorithm to find the maximum profit. You may complete at most <b>k</b> transactions.</p>

<p><b>Note:</b><br />
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,4,1], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [3,2,6,5,0,3], k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
&nbsp;            Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
</pre>

----

### 115. distinct-subsequences


<p>Given a string <strong>S</strong> and a string <strong>T</strong>, count the number of distinct subsequences of <strong>S</strong> which equals <strong>T</strong>.</p>

<p>A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, <code>&quot;ACE&quot;</code> is a subsequence of <code>&quot;ABCDE&quot;</code> while <code>&quot;AEC&quot;</code> is not).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <code>&quot;rabbbit&quot;</code>, T = <code>&quot;rabbit&quot;
<strong>Output:</strong>&nbsp;3
</code><strong>Explanation:
</strong>
As shown below, there are 3 ways you can generate &quot;rabbit&quot; from S.
(The caret symbol ^ means the chosen letters)

<code>rabbbit</code>
^^^^ ^^
<code>rabbbit</code>
^^ ^^^^
<code>rabbbit</code>
^^^ ^^^
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <code>&quot;babgbag&quot;</code>, T = <code>&quot;bag&quot;
<strong>Output:</strong>&nbsp;5
</code><strong>Explanation:
</strong>
As shown below, there are 5 ways you can generate &quot;bag&quot; from S.
(The caret symbol ^ means the chosen letters)

<code>babgbag</code>
^^ ^
<code>babgbag</code>
^^    ^
<code>babgbag</code>
^    ^^
<code>babgbag</code>
  ^  ^^
<code>babgbag</code>
    ^^^
</pre>


---

# 2. Stack

### 32. longest-valid-parentheses


<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, find the length of the longest valid (well-formed) parentheses substring.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()&quot;</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;<code>)()())</code>&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()()&quot;</code>
</pre>

---

### 20. valid-parentheses


<p>Given a string containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p>Note that an empty string is&nbsp;also considered valid.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> &quot;([)]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> &quot;{[]}&quot;
<strong>Output:</strong> true
</pre>

---

### 155. min-stack


<p>
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
<ul>
<li>
push(x) -- Push element x onto stack.
</li>
<li>
pop() -- Removes the element on top of the stack.
</li>
<li>
top() -- Get the top element.
</li>
<li>
getMin() -- Retrieve the minimum element in the stack.
</li>
</ul>
</p>

<p><b>Example:</b><br />
<pre>
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
</pre>
</p>

---

### 316. remove-duplicate-letters


<p>Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>&quot;bcabc&quot;</code>
<b>Output:</b> <code>&quot;abc&quot;</code>
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <code>&quot;cbacdcbc&quot;</code>
<b>Output:</b> <code>&quot;acdb&quot;</code>
</pre>

<br/>

---

### 341. flatten-nested-list-iterator
### 341. flatten-nested-list-iterator




<p>Given a nested list of integers, implement an iterator to flatten it.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],2,[1,1]]</span>
<strong>Output: </strong><span id="example-output-1">[1,1,2,1,1]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false,
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,1,2,1,1]</code>.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,[4,[6]]]</span>
<strong>Output: </strong><span id="example-output-2">[1,4,6]
</span><strong>Explanation: </strong>By calling <i>next</i> repeatedly until <i>hasNext</i> returns false,
&nbsp;            the order of elements returned by <i>next</i> should be: <code>[1,4,6]</code>.
</pre>
</div>
</div>

---

### 224. basic-calculator


<p>Implement a basic calculator to evaluate a simple expression string.</p>

<p>The expression string may contain open <code>(</code> and closing parentheses <code>)</code>, the plus <code>+</code> or minus sign <code>-</code>, <b>non-negative</b> integers and empty spaces <code> </code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;1 + 1&quot;
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot; 2-1 + 2 &quot;
<strong>Output:</strong> 3</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;(1+(4+5+2)-3)+(6+8)&quot;
<strong>Output:</strong> 23</pre>
<b>Note:</b>

<ul>
	<li>You may assume that the given expression is always valid.</li>
	<li><b>Do not</b> use the <code>eval</code> built-in library function.</li>
</ul>
