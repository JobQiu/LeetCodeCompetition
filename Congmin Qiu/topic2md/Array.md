# Array
## median-of-two-sorted-arrays

<p>There are two sorted arrays <b>nums1</b> and <b>nums2</b> of size m and n respectively.</p>

<p>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).</p>

<p>You may assume <strong>nums1</strong> and <strong>nums2</strong>&nbsp;cannot be both empty.</p>

<p><b>Example 1:</b></p>

<pre>
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
</pre>

<p><b>Example 2:</b></p>

<pre>
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## container-with-most-water

<p>Given <i>n</i> non-negative integers <i>a<sub>1</sub></i>, <i>a<sub>2</sub></i>, ..., <i>a<sub>n&nbsp;</sub></i>, where each represents a point at coordinate (<i>i</i>, <i>a<sub>i</sub></i>). <i>n</i> vertical lines are drawn such that the two endpoints of line <i>i</i> is at (<i>i</i>, <i>a<sub>i</sub></i>) and (<i>i</i>, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.</p>

<p><strong>Note:&nbsp;</strong>You may not slant the container and <i>n</i> is at least 2.</p>

<p>&nbsp;</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;" /></p>

<p><small>The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain&nbsp;is 49. </small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-subarray

<p>Given an integer array <code>nums</code>, find the contiguous subarray&nbsp;(containing at least one number) which has the largest sum and return its sum.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [-2,1,-3,4,-1,2,1,-5,4],
<strong>Output:</strong> 6
<strong>Explanation:</strong>&nbsp;[4,-1,2,1] has the largest sum = 6.
</pre>

<p><strong>Follow up:</strong></p>

<p>If you have figured out the O(<em>n</em>) solution, try coding another solution using the divide and conquer approach, which is more subtle.</p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## trapping-rain-water

<p>Given <em>n</em> non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;" /><br />
<small>The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. <strong>Thanks Marcos</strong> for contributing this image!</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [0,1,0,2,1,0,1,3,2,1,2,1]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## best-time-to-buy-and-sell-stock-ii

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).</p>

<p><strong>Note:</strong> You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
&nbsp;            Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
&nbsp;            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
&nbsp;            engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## majority-element

<p>Given an array of size <i>n</i>, find the majority element. The majority element is the element that appears <b>more than</b> <code>&lfloor; n/2 &rfloor;</code> times.</p>

<p>You may assume that the array is non-empty and the majority element always exist in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,2,3]
<strong>Output:</strong> 3</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-product-subarray

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
<br/>
<br/>
<br/>
<br/>
<br/>

## pascals-triangle

<p>Given a non-negative integer&nbsp;<em>numRows</em>, generate the first <em>numRows</em> of Pascal&#39;s triangle.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 5
<strong>Output:</strong>
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## search-in-rotated-sorted-array

<p>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., <code>[0,1,2,4,5,6,7]</code> might become <code>[4,5,6,7,0,1,2]</code>).</p>

<p>You are given a target value to search. If found in the array return its index, otherwise return <code>-1</code>.</p>

<p>You may assume no duplicate exists in the array.</p>

<p>Your algorithm&#39;s runtime complexity must be in the order of&nbsp;<em>O</em>(log&nbsp;<em>n</em>).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 0
<strong>Output:</strong> 4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 3
<strong>Output:</strong> -1</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## contains-duplicate-ii

<p>Given an array of integers and an integer <i>k</i>, find out whether there are two distinct indices <i>i</i> and <i>j</i> in the array such that <b>nums[i] = nums[j]</b> and the <b>absolute</b> difference between <i>i</i> and <i>j</i> is at most <i>k</i>.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,2,3,1]</span>, k = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[1,0,1,1]</span>, k = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-3-1">[1,2,3,1,2,3]</span>, k = <span id="example-input-3-2">2</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>
</div>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## longest-consecutive-sequence

<p>Given an unsorted array of integers, find the length of the longest consecutive elements sequence.</p>

<p>Your algorithm should run in O(<em>n</em>) complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;[100, 4, 200, 1, 3, 2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest consecutive elements sequence is <code>[1, 2, 3, 4]</code>. Therefore its length is 4.
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-minimum-in-rotated-sorted-array

<p>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., &nbsp;<code>[0,1,2,4,5,6,7]</code>&nbsp;might become &nbsp;<code>[4,5,6,7,0,1,2]</code>).</p>

<p>Find the minimum element.</p>

<p>You may assume no duplicate exists in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,4,5,1,2] 
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## spiral-matrix

<p>Given a matrix of <em>m</em> x <em>n</em> elements (<em>m</em> rows, <em>n</em> columns), return all elements of the matrix in spiral order.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong>
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## next-permutation

<p>Implement <strong>next permutation</strong>, which rearranges numbers into the lexicographically next greater permutation of numbers.</p>

<p>If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).</p>

<p>The replacement must be <strong><a href="http://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> and use only constant&nbsp;extra memory.</p>

<p>Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.</p>

<p><code>1,2,3</code> &rarr; <code>1,3,2</code><br />
<code>3,2,1</code> &rarr; <code>1,2,3</code><br />
<code>1,1,5</code> &rarr; <code>1,5,1</code></p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## find-all-numbers-disappeared-in-an-array

<p>Given an array of integers where 1 &le; a[i] &le; <i>n</i> (<i>n</i> = size of array), some elements appear twice and others appear once.</p>

<p>Find all the elements of [1, <i>n</i>] inclusive that do not appear in this array.</p>

<p>Could you do it without extra space and in O(<i>n</i>) runtime? You may assume the returned list does not count as extra space.</p>

<p><b>Example:</b>
<pre>
<b>Input:</b>
[4,3,2,7,8,2,3,1]

<b>Output:</b>
[5,6]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-the-duplicate-number

<p>Given an array <i>nums</i> containing <i>n</i> + 1 integers where each integer is between 1 and <i>n</i> (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>[1,3,4,2,2]</code>
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [3,1,3,4,2]
<b>Output:</b> 3</pre>

<p><b>Note:</b></p>

<ol>
	<li>You <b>must not</b> modify the array (assume the array is read only).</li>
	<li>You must use only constant, <i>O</i>(1) extra space.</li>
	<li>Your runtime complexity should be less than <em>O</em>(<em>n</em><sup>2</sup>).</li>
	<li>There is only one duplicate number in the array, but it could be repeated more than once.</li>
</ol>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## majority-element-ii

<p>Given an integer array of size <i>n</i>, find all elements that appear more than <code>&lfloor; n/3 &rfloor;</code> times.</p>

<p><strong>Note: </strong>The algorithm should run in linear time and in O(1) space.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,2,3]
<strong>Output:</strong> [3]</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,1,1,3,3,2,2,2]
<strong>Output:</strong> [1,2]</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## combination-sum

<p>Given a <strong>set</strong> of candidate numbers (<code>candidates</code>) <strong>(without duplicates)</strong> and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sums to <code>target</code>.</p>

<p>The <strong>same</strong> repeated number may be chosen from <code>candidates</code>&nbsp;unlimited number of times.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers (including <code>target</code>) will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = <code>[2,3,6,7], </code>target = <code>7</code>,
<strong>A solution set is:</strong>
[
  [7],
  [2,2,3]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5]<code>, </code>target = 8,
<strong>A solution set is:</strong>
[
&nbsp; [2,2,2,2],
&nbsp; [2,3,3],
&nbsp; [3,5]
]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## summary-ranges

<p>Given a sorted integer array without duplicates, return the summary of its ranges.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b>  [0,1,2,4,5,7]
<b>Output:</b> [&quot;0-&gt;2&quot;,&quot;4-&gt;5&quot;,&quot;7&quot;]
<strong>Explanation: </strong>0,1,2 form a continuous range;&nbsp;4,5 form a continuous range.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>  [0,2,3,4,6,8,9]
<b>Output:</b> [&quot;0&quot;,&quot;2-&gt;4&quot;,&quot;6&quot;,&quot;8-&gt;9&quot;]
<strong>Explanation: </strong>2,3,4 form a continuous range;&nbsp;8,9 form a continuous range.
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## triangle

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
<br/>
<br/>
<br/>
<br/>
<br/>

## find-all-duplicates-in-an-array

<p>Given an array of integers, 1 &le; a[i] &le; <i>n</i> (<i>n</i> = size of array), some elements appear <b>twice</b> and others appear <b>once</b>.</p>

<p>Find all the elements that appear <b>twice</b> in this array.</p>

<p>Could you do it without extra space and in O(<i>n</i>) runtime?</p>
</p>
<p><b>Example:</b><br/>
<pre>
<b>Input:</b>
[4,3,2,7,8,2,3,1]

<b>Output:</b>
[2,3]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## degree-of-an-array

<p>Given a non-empty array of non-negative integers <code>nums</code>, the <b>degree</b> of this array is defined as the maximum frequency of any one of its elements.</p>
<p>Your task is to find the smallest possible length of a (contiguous) subarray of <code>nums</code>, that has the same degree as <code>nums</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1, 2, 2, 3, 1]
<b>Output:</b> 2
<b>Explanation:</b> 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2,2,3,1,4,2]
<b>Output:</b> 6
</pre>
</p>

<p><b>Note:</b>
<li><code>nums.length</code> will be between 1 and 50,000.</li>
<li><code>nums[i]</code> will be an integer between 0 and 49,999.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## rotate-array

<p>Given an array, rotate the array to the right by <em>k</em> steps, where&nbsp;<em>k</em>&nbsp;is non-negative.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[1,2,3,4,5,6,7]</code> and <em>k</em> = 3
<strong>Output:</strong> <code>[5,6,7,1,2,3,4]</code>
<strong>Explanation:</strong>
rotate 1 steps to the right: <code>[7,1,2,3,4,5,6]</code>
rotate 2 steps to the right: <code>[6,7,1,2,3,4,5]
</code>rotate 3 steps to the right: <code>[5,6,7,1,2,3,4]</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[-1,-100,3,99]</code> and <em>k</em> = 2
<strong>Output:</strong> [3,99,-1,-100]
<strong>Explanation:</strong> 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.</li>
	<li>Could you do it in-place with O(1) extra space?</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## set-matrix-zeroes

<p>Given a <em>m</em> x <em>n</em> matrix, if an element is 0, set its entire row and column to 0. Do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
[
&nbsp; [1,1,1],
&nbsp; [1,0,1],
&nbsp; [1,1,1]
]
<strong>Output:</strong> 
[
&nbsp; [1,0,1],
&nbsp; [0,0,0],
&nbsp; [1,0,1]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 
[
&nbsp; [0,1,2,0],
&nbsp; [3,4,5,2],
&nbsp; [1,3,1,5]
]
<strong>Output:</strong> 
[
&nbsp; [0,0,0,0],
&nbsp; [0,4,5,0],
&nbsp; [0,3,1,0]
]
</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A straight forward solution using O(<em>m</em><em>n</em>) space is probably a bad idea.</li>
	<li>A simple improvement uses O(<em>m</em> + <em>n</em>) space, but still not the best solution.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## minimum-path-sum

<p>Given a <em>m</em> x <em>n</em> grid filled with non-negative numbers, find a path from top left to bottom right which <em>minimizes</em> the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; [1,3,1],
  [1,5,1],
  [4,2,1]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1&rarr;3&rarr;1&rarr;1&rarr;1 minimizes the sum.
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## 1-bit-and-2-bit-characters

<p>We have two special characters. The first character can be represented by one bit <code>0</code>. The second character can be represented by two bits (<code>10</code> or <code>11</code>).  </p>

<p>Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
bits = [1, 0, 0]
<b>Output:</b> True
<b>Explanation:</b> 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
bits = [1, 1, 1, 0]
<b>Output:</b> False
<b>Explanation:</b> 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
</pre>
</p>

<p><b>Note:</b>
<li><code>1 <= len(bits) <= 1000</code>.</li>
<li><code>bits[i]</code> is always <code>0</code> or <code>1</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## 4sum

<p>Given an array <code>nums</code> of <em>n</em> integers and an integer <code>target</code>, are there elements <em>a</em>, <em>b</em>, <em>c</em>, and <em>d</em> in <code>nums</code> such that <em>a</em> + <em>b</em> + <em>c</em> + <em>d</em> = <code>target</code>? Find all unique quadruplets in the array which gives the sum of <code>target</code>.</p>

<p><strong>Note:</strong></p>

<p>The solution set must not contain duplicate quadruplets.</p>

<p><strong>Example:</strong></p>

<pre>
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## subsets

<p>Given a set of <strong>distinct</strong> integers, <em>nums</em>, return all possible subsets (the power set).</p>

<p><strong>Note:</strong> The solution set must not contain duplicate subsets.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong>
[
  [3],
&nbsp; [1],
&nbsp; [2],
&nbsp; [1,2,3],
&nbsp; [1,3],
&nbsp; [2,3],
&nbsp; [1,2],
&nbsp; []
]</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## flipping-an-image

<p>Given a binary matrix <code>A</code>, we want to flip the image horizontally, then invert it, and return the resulting image.</p>

<p>To flip an image horizontally means that each row of the image is reversed.&nbsp; For example, flipping&nbsp;<code>[1, 1, 0]</code>&nbsp;horizontally results in&nbsp;<code>[0, 1, 1]</code>.</p>

<p>To invert an image means&nbsp;that each <code>0</code> is replaced by <code>1</code>, and each <code>1</code> is replaced by <code>0</code>.&nbsp;For example, inverting&nbsp;<code>[0, 1, 1]</code>&nbsp;results in&nbsp;<code>[1, 0, 0]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0],[1,0,1],[0,0,0]]
<strong>Output: </strong>[[1,0,0],[0,1,0],[1,1,1]]
<strong>Explanation:</strong> First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
<strong>Output: </strong>[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
<strong>Explanation:</strong> First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
</pre>

<p><strong>Notes:</strong></p>

<ul>
	<li><code>1 &lt;= A.length = A[0].length &lt;= 20</code></li>
	<li><code>0 &lt;= A[i][j]<font face="sans-serif, Arial, Verdana, Trebuchet MS">&nbsp;&lt;=&nbsp;</font>1</code></li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## best-time-to-buy-and-sell-stock-iii

<p>Say you have an array for which the <em>i</em><sup>th</sup> element is the price of a given stock on day <em>i</em>.</p>

<p>Design an algorithm to find the maximum profit. You may complete at most <em>two</em> transactions.</p>

<p><strong>Note:&nbsp;</strong>You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,3,5,0,0,3,1,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
&nbsp;            Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
&nbsp;            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
&nbsp;            engaging multiple transactions at the same time. You must sell before buying again.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transaction is done, i.e. max profit = 0.</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## task-scheduler

<p>Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.</p>

<p>However, there is a non-negative cooling interval <b>n</b> that means between two <b>same tasks</b>, there must be at least n intervals that CPU are doing different tasks or just be idle.</p>

<p>You need to return the <b>least</b> number of intervals the CPU will take to finish all the given tasks.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2
<b>Output:</b> 8
<b>Explanation:</b> A -&gt; B -&gt; idle -&gt; A -&gt; B -&gt; idle -&gt; A -&gt; B.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The number of tasks is in the range [1, 10000].</li>
	<li>The integer n is in the range [0, 100].</li>
</ol>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## sort-array-by-parity

<p>Given an array <code>A</code> of non-negative integers, return an array consisting of all the even elements of <code>A</code>, followed by all the odd elements of <code>A</code>.</p>

<p>You may return any answer array that satisfies this condition.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">[2,4,3,1]</span>
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 5000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 5000</code></li>
</ol>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## spiral-matrix-ii

<p>Given a positive integer <em>n</em>, generate a square matrix filled with elements from 1 to <em>n</em><sup>2</sup> in spiral order.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong>
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## search-insert-position

<p>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You may assume no duplicates in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 5
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 2
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 7
<strong>Output:</strong> 4
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 0
<strong>Output:</strong> 0
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-peak-element

<p>A peak element is an element that is greater than its neighbors.</p>

<p>Given an input array <code>nums</code>, where <code>nums[i] &ne; nums[i+1]</code>, find a peak element and return its index.</p>

<p>The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.</p>

<p>You may imagine that <code>nums[-1] = nums[n] = -&infin;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <strong>nums</strong> = <code>[1,2,3,1]</code>
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 is a peak element and your function should return the index number 2.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <strong>nums</strong> = <code>[</code>1,2,1,3,5,6,4]
<strong>Output:</strong> 1 or 5 
<strong>Explanation:</strong> Your function can return either index number 1 where the peak element is 2, 
&nbsp;            or index number 5 where the peak element is 6.
</pre>

<p><strong>Note:</strong></p>

<p>Your solution should be in logarithmic complexity.</p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## jump-game-ii

<p>Given an array of non-negative integers, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Your goal is to reach the last index in the minimum number of jumps.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.</pre>

<p><strong>Note:</strong></p>

<p>You can assume that you can always reach the last index.</p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## jump-game

<p>Given an array of non-negative integers, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Determine if you are able to reach the last index.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum
&nbsp;            jump length is 0, which makes it impossible to reach the last index.
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## pascals-triangle-ii

<p>Given a non-negative&nbsp;index <em>k</em>&nbsp;where <em>k</em> &le;&nbsp;33, return the <em>k</em><sup>th</sup>&nbsp;index row of the Pascal&#39;s triangle.</p>

<p>Note that the row index starts from&nbsp;0.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> [1,3,3,1]
</pre>

<p><strong>Follow up:</strong></p>

<p>Could you optimize your algorithm to use only <em>O</em>(<em>k</em>) extra space?</p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## wiggle-sort

 The content is locked, copy the problem here. 
https://leetcode.com/problems/wiggle-sort/description/
<a href = "https://leetcode.com/problems/ wiggle-sort"> wiggle-sort</a>
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

## sort-colors

<p>Given an array with <em>n</em> objects colored red, white or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>&nbsp;</strong>so that objects of the same color are adjacent, with the colors in the order red, white and blue.</p>

<p>Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.</p>

<p><strong>Note:</strong>&nbsp;You are not suppose to use the library&#39;s sort function for this problem.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A rather straight forward solution is a two-pass algorithm using counting sort.<br />
	First, iterate the array counting number of 0&#39;s, 1&#39;s, and 2&#39;s, then overwrite array with total number of 0&#39;s, then 1&#39;s and followed by 2&#39;s.</li>
	<li>Could you come up with a&nbsp;one-pass algorithm using only constant space?</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## largest-rectangle-in-histogram

<p>Given <em>n</em> non-negative integers representing the histogram&#39;s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/histogram.png" style="width: 188px; height: 204px;" /><br />
<small>Above is a histogram where width of each bar is 1, given height = <code>[2,1,5,6,2,3]</code>.</small></p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png" style="width: 188px; height: 204px;" /><br />
<small>The largest rectangle is shown in the shaded area, which has area = <code>10</code> unit.</small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,1,5,6,2,3]
<strong>Output:</strong> 10
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## subarray-sum-equals-k

<p>Given an array of integers and an integer <b>k</b>, you need to find the total number of continuous subarrays whose sum equals to <b>k</b>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>nums = [1,1,1], k = 2
<b>Output:</b> 2
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the array is in range [1, 20,000].</li>
<li>The range of numbers in the array is [-1000, 1000] and the range of the integer <b>k</b> is [-1e7, 1e7].</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-product-of-three-numbers

<p>Given an integer array, find three numbers whose product is maximum and output the maximum product.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,2,3]
<b>Output:</b> 6
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2,3,4]
<b>Output:</b> 24
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the given array will be in range [3,10<sup>4</sup>] and all elements are in the range [-1000, 1000].</li>
<li>Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-first-and-last-position-of-element-in-sorted-array

<p>Given an array of integers <code>nums</code> sorted in ascending order, find the starting and ending position of a given <code>target</code> value.</p>

<p>Your algorithm&#39;s runtime complexity must be in the order of <em>O</em>(log <em>n</em>).</p>

<p>If the target is not found in the array, return <code>[-1, -1]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 8
<strong>Output:</strong> [3,4]</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 6
<strong>Output:</strong> [-1,-1]</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## min-cost-climbing-stairs

<p>
On a staircase, the <code>i</code>-th step has some non-negative cost <code>cost[i]</code> assigned (0 indexed).
</p><p>
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> cost = [10, 15, 20]
<b>Output:</b> 15
<b>Explanation:</b> Cheapest is start on cost[1], pay that cost and go to the top.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
<b>Output:</b> 6
<b>Explanation:</b> Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>cost</code> will have a length in the range <code>[2, 1000]</code>.</li>
<li>Every <code>cost[i]</code> will be an integer in the range <code>[0, 999]</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## reshape-the-matrix

<p>In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
</p>

<p>
You're given a matrix represented by a two-dimensional array, and two <b>positive</b> integers <b>r</b> and <b>c</b> representing the <b>row</b> number and <b>column</b> number of the wanted reshaped matrix, respectively.</p>

 <p>The reshaped matrix need to be filled with all the elements of the original matrix in the same <b>row-traversing</b> order as they were.
</p>

<p>
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
<b>Output:</b> 
[[1,2,3,4]]
<b>Explanation:</b><br>The <b>row-traversing</b> of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
<b>Output:</b> 
[[1,2],
 [3,4]]
<b>Explanation:</b><br>There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The height and width of the given matrix is in range [1, 100].</li>
<li>The given r and c are all positive.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-minimum-in-rotated-sorted-array-ii

<p>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., &nbsp;<code>[0,1,2,4,5,6,7]</code>&nbsp;might become &nbsp;<code>[4,5,6,7,0,1,2]</code>).</p>

<p>Find the minimum element.</p>

<p>The array may contain duplicates.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5]
<strong>Output:</strong> 1</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [2,2,2,0,1]
<strong>Output:</strong> 0</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>This is a follow up problem to&nbsp;<a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/">Find Minimum in Rotated Sorted Array</a>.</li>
	<li>Would allow duplicates affect the run-time complexity? How and why?</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## combination-sum-iii

<div>
<p>Find all possible combinations of <i><b>k</b></i> numbers that add up to a number <i><b>n</b></i>, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <i><b>k</b></i> = 3, <i><b>n</b></i> = 7
<strong>Output:</strong> [[1,2,4]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <i><b>k</b></i> = 3, <i><b>n</b></i> = 9
<strong>Output:</strong> [[1,2,6], [1,3,5], [2,3,4]]
</pre>
</div>
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
<br/>
<br/>
<br/>
<br/>
<br/>

## word-ladder-ii

<p>Given two words (<em>beginWord</em> and <em>endWord</em>), and a dictionary&#39;s word list, find all shortest transformation sequence(s) from <em>beginWord</em> to <em>endWord</em>, such that:</p>

<ol>
	<li>Only one letter can be changed at a time</li>
	<li>Each transformed word must exist in the word list. Note that <em>beginWord</em> is <em>not</em> a transformed word.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>Return an empty list if there is no such transformation sequence.</li>
	<li>All words have the same length.</li>
	<li>All words contain only lowercase alphabetic characters.</li>
	<li>You may assume no duplicates in the word list.</li>
	<li>You may assume <em>beginWord</em> and <em>endWord</em> are non-empty and are not the same.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>Output:</strong>
[
  [&quot;hit&quot;,&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;cog&quot;],
&nbsp; [&quot;hit&quot;,&quot;hot&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>Output: </strong>[]

<strong>Explanation:</strong>&nbsp;The endWord &quot;cog&quot; is not in wordList, therefore no possible<strong>&nbsp;</strong>transformation.
</pre>

<ul>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## insert-delete-getrandom-o1

<p>Design a data structure that supports all following operations in <i>average</i> <b>O(1)</b> time.</p>

<p>
<ol>
<li><code>insert(val)</code>: Inserts an item val to the set if not already present.</li>
<li><code>remove(val)</code>: Removes an item val from the set if present.</li>
<li><code>getRandom</code>: Returns a random element from current set of elements. Each element must have the <b>same probability</b> of being returned.</li>
</ol>
</p>

<p><b>Example:</b>
<pre>
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## toeplitz-matrix

<p>A matrix is <em>Toeplitz</em> if every diagonal from top-left to bottom-right has the same element.</p>

<p>Now given an <code>M x N</code> matrix, return&nbsp;<code>True</code>&nbsp;if and only if the matrix is <em>Toeplitz</em>.<br />
&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong>matrix = [
&nbsp; [1,2,3,4],
&nbsp; [5,1,2,3],
&nbsp; [9,5,1,2]
]
<strong>Output:</strong> True
<strong>Explanation:</strong>
In the above grid, the&nbsp;diagonals are:
&quot;[9]&quot;, &quot;[5, 5]&quot;, &quot;[1, 1, 1]&quot;, &quot;[2, 2, 2]&quot;, &quot;[3, 3]&quot;, &quot;[4]&quot;.
In each diagonal all elements are the same, so the answer is True.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong>matrix = [
&nbsp; [1,2],
&nbsp; [2,2]
]
<strong>Output:</strong> False
<strong>Explanation:</strong>
The diagonal &quot;[1, 2]&quot; has different elements.
</pre>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li><code>matrix</code> will be a 2D array of integers.</li>
	<li><code>matrix</code> will have a number of rows and columns in range <code>[1, 20]</code>.</li>
	<li><code>matrix[i][j]</code> will be integers in range <code>[0, 99]</code>.</li>
</ol>

<p><br />
<strong>Follow up:</strong></p>

<ol>
	<li>What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?</li>
	<li>What if the matrix is so large that you can only load up a partial row into the memory at once?</li>
</ol>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## remove-duplicates-from-sorted-array-ii

<p>Given a sorted array <em>nums</em>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that duplicates appeared at most&nbsp;<em>twice</em> and return the new length.</p>

<p>Do not allocate extra space for another array, you must do this by <strong>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></strong> with O(1) extra memory.</p>

<p><strong>Example 1:</strong></p>

<pre>
Given <em>nums</em> = <strong>[1,1,1,2,2,3]</strong>,

Your function should return length = <strong><code>5</code></strong>, with the first five elements of <em><code>nums</code></em> being <strong><code>1, 1, 2, 2</code></strong> and <strong>3</strong> respectively.

It doesn&#39;t matter what you leave beyond the returned length.</pre>

<p><strong>Example 2:</strong></p>

<pre>
Given <em>nums</em> = <strong>[0,0,1,1,1,1,2,3,3]</strong>,

Your function should return length = <strong><code>7</code></strong>, with the first seven elements of <em><code>nums</code></em> being modified to&nbsp;<strong><code>0</code></strong>, <strong>0</strong>, <strong>1</strong>, <strong>1</strong>, <strong>2</strong>, <strong>3</strong> and&nbsp;<strong>3</strong> respectively.

It doesn&#39;t matter what values are set beyond&nbsp;the returned length.
</pre>

<p><strong>Clarification:</strong></p>

<p>Confused why the returned value is an integer but your answer is an array?</p>

<p>Note that the input array is passed in by <strong>reference</strong>, which means modification to the input array will be known to the caller as well.</p>

<p>Internally you can think of this:</p>

<pre>
// <strong>nums</strong> is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to <strong>nums</strong> in your function would be known by the caller.
// using the length returned by your function, it prints the first <strong>len</strong> elements.
for (int i = 0; i &lt; len; i++) {
&nbsp; &nbsp; print(nums[i]);
}
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## insert-interval

<p>Given a set of <em>non-overlapping</em> intervals, insert a new interval into the intervals (merge if necessary).</p>

<p>You may assume that the intervals were initially sorted according to their start times.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:</strong> [[1,5],[6,9]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = <code>[[1,2],[3,5],[6,7],[8,10],[12,16]]</code>, newInterval = <code>[4,8]</code>
<strong>Output:</strong> [[1,2],[3,10],[12,16]]
<strong>Explanation:</strong> Because the new interval <code>[4,8]</code> overlaps with <code>[3,5],[6,7],[8,10]</code>.</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## beautiful-arrangement-ii

<p>
Given two integers <code>n</code> and <code>k</code>, you need to construct a list which contains <code>n</code> different positive integers ranging from <code>1</code> to <code>n</code> and obeys the following requirement: <br/>

Suppose this list is [a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ... , a<sub>n</sub>], then the list [|a<sub>1</sub> - a<sub>2</sub>|, |a<sub>2</sub> - a<sub>3</sub>|, |a<sub>3</sub> - a<sub>4</sub>|, ... , |a<sub>n-1</sub> - a<sub>n</sub>|] has exactly <code>k</code> distinct integers.
</p>

<p>
If there are multiple answers, print any of them.
</p>

<p><b>Example 1:</b><br/>
<pre>
<b>Input:</b> n = 3, k = 1
<b>Output:</b> [1, 2, 3]
<b>Explanation:</b> The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> n = 3, k = 2
<b>Output:</b> [1, 3, 2]
<b>Explanation:</b> The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The <code>n</code> and <code>k</code> are in the range 1 <= k < n <= 10<sup>4</sup>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## search-in-rotated-sorted-array-ii

<p>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., <code>[0,0,1,2,2,5,6]</code> might become <code>[2,5,6,0,0,1,2]</code>).</p>

<p>You are given a target value to search. If found in the array return <code>true</code>, otherwise return <code>false</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2<code>,5,6,0,0,1,2]</code>, target = 0
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2<code>,5,6,0,0,1,2]</code>, target = 3
<strong>Output:</strong> false</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>This is a follow up problem to&nbsp;<a href="/problems/search-in-rotated-sorted-array/description/">Search in Rotated Sorted Array</a>, where <code>nums</code> may contain duplicates.</li>
	<li>Would this affect the run-time complexity? How and why?</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## k-empty-slots

 The content is locked, copy the problem here. 
https://leetcode.com/problems/k-empty-slots/description/
<a href = "https://leetcode.com/problems/ k-empty-slots"> k-empty-slots</a>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## search-a-2d-matrix

<p>Write an efficient algorithm that searches for a value in an <em>m</em> x <em>n</em> matrix. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted from left to right.</li>
	<li>The first integer of each row is greater than the last integer of the previous row.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
<strong>Output:</strong> false</pre>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## transpose-matrix

<p>Given a&nbsp;matrix <code>A</code>, return the transpose of <code>A</code>.</p>

<p>The transpose of a matrix is the matrix flipped over it&#39;s main diagonal, switching the row and column indices of the matrix.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,2,3],[4,5,6],[7,8,9]]</span>
<strong>Output: </strong><span id="example-output-1">[[1,4,7],[2,5,8],[3,6,9]]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,2,3],[4,5,6]]</span>
<strong>Output: </strong><span id="example-output-2">[[1,4],[2,5],[3,6]]</span>
</pre>

<p>&nbsp;</p>

<p><span><strong>Note:</strong></span></p>

<ol>
	<li><code><span>1 &lt;= A.length&nbsp;&lt;= 1000</span></code></li>
	<li><code><span>1 &lt;= A[0].length&nbsp;&lt;= 1000</span></code></li>
</ol>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-length-of-repeated-subarray

<p>Given two integer arrays <code>A</code> and <code>B</code>, return the maximum length of an subarray that appears in both arrays.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
A: [1,2,3,2,1]
B: [3,2,1,4,7]
<b>Output:</b> 3
<b>Explanation:</b> 
The repeated subarray with maximum length is [3, 2, 1].
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>1 <= len(A), len(B) <= 1000</li>
<li>0 <= A[i], B[i] < 100</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## minimum-size-subarray-sum

<p>Given an array of <strong>n</strong> positive integers and a positive integer <strong>s</strong>, find the minimal length of a <b>contiguous</b> subarray of which the sum &ge; <strong>s</strong>. If there isn&#39;t one, return 0 instead.</p>

<p><strong>Example:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> <code>s = 7, nums = [2,3,1,2,4,3]</code>
<strong>Output:</strong> 2
<strong>Explanation: </strong>the subarray <code>[4,3]</code> has the minimal length under the problem constraint.</pre>

<div class="spoilers"><b>Follow up:</b></div>

<div class="spoilers">If you have figured out the <i>O</i>(<i>n</i>) solution, try coding another solution of which the time complexity is <i>O</i>(<i>n</i> log <i>n</i>).&nbsp;</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## find-the-celebrity

 The content is locked, copy the problem here. 
https://leetcode.com/problems/find-the-celebrity/description/
<a href = "https://leetcode.com/problems/ find-the-celebrity"> find-the-celebrity</a>
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

## non-decreasing-array

<p>
Given an array with <code>n</code> integers, your task is to check if it could become non-decreasing by modifying <b>at most</b> <code>1</code> element.
</p>

<p>
We define an array is non-decreasing if <code>array[i] <= array[i + 1]</code> holds for every <code>i</code> (1 <= i < n).
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [4,2,3]
<b>Output:</b> True
<b>Explanation:</b> You could modify the first <code>4</code> to <code>1</code> to get a non-decreasing array.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [4,2,1]
<b>Output:</b> False
<b>Explanation:</b> You can't get a non-decreasing array by modify at most one element.
</pre>
</p>

<p><b>Note:</b>
The <code>n</code> belongs to [1, 10,000].
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## best-time-to-buy-and-sell-stock-with-transaction-fee

<p>Your are given an array of integers <code>prices</code>, for which the <code>i</code>-th element is the price of a given stock on day <code>i</code>; and a non-negative integer <code>fee</code> representing a transaction fee.</p>
<p>You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)</p>
<p>Return the maximum profit you can make.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> prices = [1, 3, 2, 8, 4, 9], fee = 2
<b>Output:</b> 8
<b>Explanation:</b> The maximum profit can be achieved by:
<li>Buying at prices[0] = 1</li><li>Selling at prices[3] = 8</li><li>Buying at prices[4] = 4</li><li>Selling at prices[5] = 9</li>The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < prices.length <= 50000</code>.</li>
<li><code>0 < prices[i] < 50000</code>.</li>
<li><code>0 <= fee < 50000</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## max-consecutive-ones

<p>Given a binary array, find the maximum number of consecutive 1s in this array.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,1,0,1,1,1]
<b>Output:</b> 3
<b>Explanation:</b> The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
</pre>
</p>

<p><b>Note:</b>
<ul>
<li>The input array will only contain <code>0</code> and <code>1</code>.</li>
<li>The length of input array is a positive integer and will not exceed 10,000</li>
</ul>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## image-smoother

<p>Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.  If a cell has less than 8 surrounding cells, then use as many as you can.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
[[1,1,1],
 [1,0,1],
 [1,1,1]]
<b>Output:</b>
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
<b>Explanation:</b>
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The value in the given matrix is in the range of [0, 255].</li>
<li>The length and width of the given matrix are in the range of [1, 150].</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## shortest-word-distance

 The content is locked, copy the problem here. 
https://leetcode.com/problems/shortest-word-distance/description/
<a href = "https://leetcode.com/problems/ shortest-word-distance"> shortest-word-distance</a>
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

## subsets-ii

<p>Given a collection of integers that might contain duplicates, <strong><em>nums</em></strong>, return all possible subsets (the power set).</p>

<p><strong>Note:</strong> The solution set must not contain duplicate subsets.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,2,2]
<strong>Output:</strong>
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-average-subarray-i

<p>
Given an array consisting of <code>n</code> integers, find the contiguous subarray of given length <code>k</code> that has the maximum average value. And you need to output the maximum average value.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,12,-5,-6,50,3], k = 4
<b>Output:</b> 12.75
<b>Explanation:</b> Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>1 <= <code>k</code> <= <code>n</code> <= 30,000.</li>
<li>Elements of the given array will be in the range [-10,000, 10,000].</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## unique-paths-ii

<p>A robot is located at the top-left corner of a <em>m</em> x <em>n</em> grid (marked &#39;Start&#39; in the diagram below).</p>

<p>The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked &#39;Finish&#39; in the diagram below).</p>

<p>Now consider if some obstacles are added to the grids. How many unique paths would there be?</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" style="width: 400px; height: 183px;" /></p>

<p>An obstacle and empty space is marked as <code>1</code> and <code>0</code> respectively in the grid.</p>

<p><strong>Note:</strong> <em>m</em> and <em>n</em> will be at most 100.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong>[
&nbsp; [0,0,0],
&nbsp; [0,1,0],
&nbsp; [0,0,0]
]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -&gt; Right -&gt; Down -&gt; Down
2. Down -&gt; Down -&gt; Right -&gt; Right
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## valid-triangle-number

Given an array consists of non-negative integers,  your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [2,2,3,4]
<b>Output:</b> 3
<b>Explanation:</b>
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the given array won't exceed 1000.</li>
<li>The integers in the given array are in the range of [0, 1000].</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## shortest-unsorted-continuous-subarray

<p>Given an integer array, you need to find one <b>continuous subarray</b> that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too. </p> 

<p>You need to find the <b>shortest</b> such subarray and output its length.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [2, 6, 4, 8, 10, 9, 15]
<b>Output:</b> 5
<b>Explanation:</b> You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>Then length of the input array is in range [1, 10,000].</li>
<li>The input array may contain duplicates, so ascending order here means <b><=</b>. </li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## missing-ranges

 The content is locked, copy the problem here. 
https://leetcode.com/problems/missing-ranges/description/
<a href = "https://leetcode.com/problems/ missing-ranges"> missing-ranges</a>
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

## longest-continuous-increasing-subsequence

<p>
Given an unsorted array of integers, find the length of longest <code>continuous</code> increasing subsequence (subarray).
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,3,5,4,7]
<b>Output:</b> 3
<b>Explanation:</b> The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [2,2,2,2,2]
<b>Output:</b> 1
<b>Explanation:</b> The longest continuous increasing subsequence is [2], its length is 1. 
</pre>
</p>

<p><b>Note:</b>
Length of the array will not exceed 10,000.
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## subarray-product-less-than-k

<p>Your are given an array of positive integers <code>nums</code>.</p>
<p>Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than <code>k</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> nums = [10, 5, 2, 6], k = 100
<b>Output:</b> 8
<b>Explanation:</b> The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < nums.length <= 50000</code>.</li>
<li><code>0 < nums[i] < 1000</code>.</li>
<li><code>0 <= k < 10^6</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## third-maximum-number

<p>Given a <b>non-empty</b> array of integers, return the <b>third</b> maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [3, 2, 1]

<b>Output:</b> 1

<b>Explanation:</b> The third maximum is 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1, 2]

<b>Output:</b> 2

<b>Explanation:</b> The third maximum does not exist, so the maximum (2) is returned instead.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> [2, 2, 3, 1]

<b>Output:</b> 1

<b>Explanation:</b> Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## array-nesting

<p>A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.</p>

<p>Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]&hellip; By that analogy, we stop adding right before a duplicate element occurs in S.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> A = [5,4,0,3,1,6,2]
<b>Output:</b> 4
<b>Explanation:</b> 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>N is an integer within the range [1, 20,000].</li>
	<li>The elements of A are all distinct.</li>
	<li>Each element of A is an integer within the range [0, N-1].</li>
</ol>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-sum-of-3-non-overlapping-subarrays

<p>
In a given array <code>nums</code> of positive integers, find three non-overlapping subarrays with maximum sum.
</p>
<p>
Each subarray will be of size <code>k</code>, and we want to maximize the sum of all <code>3*k</code> entries.
</p>
<p>
Return the result as a list of indices representing the starting position of each interval (0-indexed).  If there are multiple answers, return the lexicographically smallest one.
</p>
<p><b>Example:</b><br />
<pre>
<b>Input:</b> [1,2,1,2,6,7,5,1], 2
<b>Output:</b> [0, 3, 5]
<b>Explanation:</b> Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
</pre>
</p>

<p><b>Note:</b><br />
<li><code>nums.length</code> will be between 1 and 20000.</li>
<li><code>nums[i]</code> will be between 1 and 65535.</li>
<li><code>k</code> will be between 1 and floor(nums.length / 3).</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## combination-sum-ii

<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sums to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers (including <code>target</code>) will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates =&nbsp;<code>[10,1,2,7,6,1,5]</code>, target =&nbsp;<code>8</code>,
<strong>A solution set is:</strong>
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates =&nbsp;[2,5,2,1,2], target =&nbsp;5,
<strong>A solution set is:</strong>
[
&nbsp; [1,2,2],
&nbsp; [5]
]
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-pivot-index

<p>Given an array of integers <code>nums</code>, write a method that returns the "pivot" index of this array.
</p><p>
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
</p><p>
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
nums = [1, 7, 3, 6, 5, 6]
<b>Output:</b> 3
<b>Explanation:</b> 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
nums = [1, 2, 3]
<b>Output:</b> -1
<b>Explanation:</b> 
There is no index that satisfies the conditions in the problem statement.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>nums</code> will be in the range <code>[0, 10000]</code>.</li>
<li>Each element <code>nums[i]</code> will be an integer in the range <code>[-1000, 1000]</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## reveal-cards-in-increasing-order

<p>In a deck of cards, every card has a unique integer.&nbsp; You can order the deck in&nbsp;any order you want.</p>

<p>Initially, all the cards start face down (unrevealed) in one deck.</p>

<p>Now, you do the following steps repeatedly, until all cards are revealed:</p>

<ol>
	<li>Take the top card of the deck, reveal it, and take it out of the deck.</li>
	<li>If there are still cards in the deck, put the next top card of the deck at&nbsp;the bottom of the deck.</li>
	<li>If there are still unrevealed cards, go back to step 1.&nbsp; Otherwise, stop.</li>
</ol>

<p>Return an ordering of the deck that would reveal the cards&nbsp;in <strong>increasing order.</strong></p>

<p>The first entry in the answer is considered to be the top of the deck.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[17,13,11,2,3,5,7]</span>
<strong>Output: </strong><span id="example-output-1">[2,13,3,11,5,17,7]</span>
<strong>Explanation: </strong>
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
</pre>

<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 10^6</code></li>
	<li><code>A[i] != A[j]</code>&nbsp;for all&nbsp;<code>i != j</code></li>
</ol>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## sum-of-subarray-minimums

<p>Given an array of integers <code>A</code>, find the sum of <code>min(B)</code>, where <code>B</code> ranges over&nbsp;every (contiguous) subarray of <code>A</code>.</p>

<p>Since the answer may be large, <strong>return the answer modulo <code>10^9 + 7</code>.</strong></p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">17</span>
<strong>Explanation:</strong> Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.&nbsp; Sum is 17.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 30000</code></li>
</ol>

<div>
<p>&nbsp;</p>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## can-place-flowers

<p>Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.</p>

<p>Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number <b>n</b>, return if <b>n</b> new flowers can be planted in it without violating the no-adjacent-flowers rule.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> flowerbed = [1,0,0,0,1], n = 1
<b>Output:</b> True
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> flowerbed = [1,0,0,0,1], n = 2
<b>Output:</b> False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The input array won't violate no-adjacent-flowers rule.</li>
<li>The input array size is in the range of [1, 20000].</li>
<li><b>n</b> is a non-negative integer which won't exceed the input array size.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## max-chunks-to-make-sorted

<p>Given an array <code>arr</code> that is a permutation of <code>[0, 1, ..., arr.length - 1]</code>, we split the array into some number of &quot;chunks&quot; (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.</p>

<p>What is the most number of chunks we could have made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,3,2,1,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn&#39;t sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,0,2,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>arr</code> will have length in range <code>[1, 10]</code>.</li>
	<li><code>arr[i]</code> will be a permutation of <code>[0, 1, ..., arr.length - 1]</code>.</li>
</ul>

<p>&nbsp;</p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-swap

<p>
Given a non-negative integer, you could swap two digits <b>at most</b> once to get the maximum valued number. Return the maximum valued number you could get.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 2736
<b>Output:</b> 7236
<b>Explanation:</b> Swap the number 2 and the number 7.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 9973
<b>Output:</b> 9973
<b>Explanation:</b> No swap.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The given number is in the range [0, 10<sup>8</sup>]</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## k-diff-pairs-in-an-array

<p>
Given an array of integers and an integer <b>k</b>, you need to find the number of <b>unique</b> k-diff pairs in the array. Here a <b>k-diff</b> pair is defined as an integer pair (i, j), where <b>i</b> and <b>j</b> are both numbers in the array and their <a href = "https://en.wikipedia.org/wiki/Absolute_difference">absolute difference</a> is <b>k</b>.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [3, 1, 4, 1, 5], k = 2
<b>Output:</b> 2
<b>Explanation: </b>There are two 2-diff pairs in the array, (1, 3) and (3, 5).</br>Although we have two 1s in the input, we should only return the number of <b>unique</b> pairs.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>[1, 2, 3, 4, 5], k = 1
<b>Output: </b>4
<b>Explanation:</b> There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input: </b>[1, 3, 1, 5, 4], k = 0
<b>Output: </b>1
<b>Explanation:</b> There is one 0-diff pair in the array, (1, 1).
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The pairs (i, j) and (j, i) count as the same pair.</li>
<li>The length of the array won't exceed 10,000.</li>
<li>All the integers in the given input belong to the range: [-1e7, 1e7].</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## image-overlap

<p>Two images <code>A</code> and <code>B</code> are given, represented as&nbsp;binary, square matrices of the same size.&nbsp; (A binary matrix has only 0s and 1s as values.)</p>

<p>We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.&nbsp; After, the <em>overlap</em> of this translation is the number of positions that have a 1 in both images.</p>

<p>(Note also that a translation does <strong>not</strong> include any kind of rotation.)</p>

<p>What is the largest possible overlap?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = [[1,1,0],
            [0,1,0],
&nbsp;           [0,1,0]]
&nbsp;      B = [[0,0,0],
&nbsp;           [0,1,1],
&nbsp;           [0,0,1]]
<strong>Output: </strong>3
<strong>Explanation:</strong> We slide A to right by 1 unit and down by 1 unit.</pre>

<p><strong>Notes:</strong>&nbsp;</p>

<ol>
	<li><code>1 &lt;= A.length = A[0].length = B.length = B[0].length &lt;= 30</code></li>
	<li><code>0 &lt;=&nbsp;A[i][j], B[i][j] &lt;= 1</code></li>
</ol>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## sort-array-by-parity-ii

<p>Given an array <code>A</code>&nbsp;of non-negative integers, half of the integers in A are odd, and half of the integers are even.</p>

<p>Sort the array so that whenever <code>A[i]</code> is odd, <code>i</code> is odd; and whenever <code>A[i]</code> is even, <code>i</code> is even.</p>

<p>You may return any answer array that satisfies this condition.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[4,2,5,7]</span>
<strong>Output: </strong><span id="example-output-1">[4,5,2,7]</span>
<strong>Explanation: </strong>[4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 20000</code></li>
	<li><code>A.length % 2 == 0</code></li>
	<li><code>0 &lt;= A[i] &lt;= 1000</code></li>
</ol>

<div>
<p>&nbsp;</p>
</div>
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
<br/>
<br/>
<br/>
<br/>
<br/>

## teemo-attacking

<p>
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking <b>ascending</b> time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.
</p>

<p>You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,4], 2
<b>Output:</b> 4
<b>Explanation:</b> At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. <br />This poisoned status will last 2 seconds until the end of time point 2. <br />And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. <br />So you finally need to output 4.
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2], 2
<b>Output:</b> 3
<b>Explanation:</b> At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. <br />This poisoned status will last 2 seconds until the end of time point 2. <br/>However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. <br/>Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. <br/>So you finally need to output 3.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>You may assume the length of given time series array won't exceed 10000.</li>
<li>You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## find-k-th-smallest-pair-distance

<p>Given an integer array, return the k-th smallest <b>distance</b> among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B. </p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
nums = [1,3,1]
k = 1
<b>Output: 0</b> 
<b>Explanation:</b>
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>2 <= len(nums) <= 10000</code>.</li>
<li><code>0 <= nums[i] < 1000000</code>.</li>
<li><code>1 <= k <= len(nums) * (len(nums) - 1) / 2</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## 3sum-smaller

 The content is locked, copy the problem here. 
https://leetcode.com/problems/3sum-smaller/description/
<a href = "https://leetcode.com/problems/ 3sum-smaller"> 3sum-smaller</a>
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

## fair-candy-swap

<p>Alice and Bob have candy bars of different sizes: <code>A[i]</code> is the size of the <code>i</code>-th bar of candy that Alice has, and <code>B[j]</code> is the size of the <code>j</code>-th bar of candy that Bob has.</p>

<p>Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total&nbsp;amount of candy.&nbsp; (<em>The total amount of candy&nbsp;a person has is the sum of the sizes of candy&nbsp;bars they have.</em>)</p>

<p>Return an integer array <code>ans</code>&nbsp;where <code>ans[0]</code> is the size of the candy bar that Alice must exchange, and <code>ans[1]</code> is the size of the candy bar that Bob must exchange.</p>

<p>If there are multiple answers, you may return any one of them.&nbsp; It is guaranteed an answer exists.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,1]</span>, B = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,2]</span>, B = <span id="example-input-2-2">[2,3]</span>
<strong>Output: </strong><span id="example-output-2">[1,2]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2]</span>, B = <span id="example-input-3-2">[1,3]</span>
<strong>Output: </strong><span id="example-output-3">[2,3]</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">[1,2,5]</span>, B = <span id="example-input-4-2">[2,4]</span>
<strong>Output: </strong><span id="example-output-4">[5,4]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ul>
	<li><span><code>1 &lt;= A.length &lt;= 10000</code></span></li>
	<li><span><code>1 &lt;= B.length &lt;= 10000</code></span></li>
	<li><code><span>1 &lt;= A[i] &lt;= 100000</span></code></li>
	<li><code><span>1 &lt;= B[i] &lt;= 100000</span></code></li>
	<li>It is guaranteed that Alice and Bob have different total amounts of&nbsp;candy.</li>
	<li>It is guaranteed there exists an&nbsp;answer.</li>
</ul>
</div>
</div>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## pour-water

 The content is locked, copy the problem here. 
https://leetcode.com/problems/pour-water/description/
<a href = "https://leetcode.com/problems/ pour-water"> pour-water</a>
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

## candy-crush

 The content is locked, copy the problem here. 
https://leetcode.com/problems/candy-crush/description/
<a href = "https://leetcode.com/problems/ candy-crush"> candy-crush</a>
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

## my-calendar-ii

<p>
Implement a <code>MyCalendarTwo</code> class to store your events. A new event can be added if adding the event will not cause a <b>triple</b> booking.
</p><p>
Your class will have one method, <code>book(int start, int end)</code>.  Formally, this represents a booking on the half open interval <code>[start, end)</code>, the range of real numbers <code>x</code> such that <code>start <= x < end</code>.
</p><p>
A <i>triple booking</i> happens when <b>three</b> events have some non-empty intersection (ie., there is some time that is common to all 3 events.)
</p><p>
For each call to the method <code>MyCalendar.book</code>, return <code>true</code> if the event can be added to the calendar successfully without causing a <b>triple</b> booking.  Otherwise, return <code>false</code> and do not add the event to the calendar.
</p>

Your class will be called like this:
<code>MyCalendar cal = new MyCalendar();</code>
<code>MyCalendar.book(start, end)</code>

<p><b>Example 1:</b><br />
<pre>
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
<b>Explanation:</b> 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
</pre>
</p>

<p><b>Note:</b>
<li>The number of calls to <code>MyCalendar.book</code> per test case will be at most <code>1000</code>.</li>
<li>In calls to <code>MyCalendar.book(start, end)</code>, <code>start</code> and <code>end</code> are integers in the range <code>[0, 10^9]</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## insert-delete-getrandom-o1-duplicates-allowed

<p>Design a data structure that supports all following operations in <i>average</i> <b>O(1)</b> time.</p>
<b>Note: Duplicate elements are allowed.</b>
<p>
<ol>
<li><code>insert(val)</code>: Inserts an item val to the collection.</li>
<li><code>remove(val)</code>: Removes an item val from the collection if present.</li>
<li><code>getRandom</code>: Returns a random element from current collection of elements. The probability of each element being returned is <b>linearly related</b> to the number of same value the collection contains.</li>
</ol>
</p>

<p><b>Example:</b>
<pre>
// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## number-of-subarrays-with-bounded-maximum

<p>We are given an array <code>A</code> of positive integers, and two positive integers <code>L</code> and <code>R</code> (<code>L &lt;= R</code>).</p>

<p>Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least <code>L</code> and at most <code>R</code>.</p>

<pre>
<strong>Example :</strong>
<strong>Input:</strong> 
A = [2, 1, 4, 3]
L = 2
R = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three subarrays that meet the requirements: [2], [2, 1], [3].
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>L, R&nbsp; and <code>A[i]</code> will be an integer in the range <code>[0, 10^9]</code>.</li>
	<li>The length of <code>A</code> will be in the range of <code>[1, 50000]</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## sum-of-subsequence-widths

<p>Given an array of integers <code>A</code>, consider all non-empty subsequences of <code>A</code>.</p>

<p>For any sequence S, let the&nbsp;<em>width</em>&nbsp;of S be the difference between the maximum and minimum element of S.</p>

<p>Return the sum of the widths of all subsequences of A.&nbsp;</p>

<p>As the answer may be very large, <strong>return the answer modulo 10^9 + 7</strong>.</p>

<div>
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,3]</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation:
</strong>Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 20000</code></li>
</ul>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## largest-number-at-least-twice-of-others

<p>In a given integer array <code>nums</code>, there is always exactly one largest element.</p>

<p>Find whether the largest element in the array is at least twice as much as every other number in the array.</p>

<p>If it is, return the <strong>index</strong> of the largest element, otherwise return -1.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3, 6, 1, 0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
</pre>

<p>&nbsp;</p>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1, 2, 3, 4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 4 isn&#39;t at least as big as twice the value of 3, so we return -1.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>nums</code> will have a length in the range <code>[1, 50]</code>.</li>
	<li>Every <code>nums[i]</code> will be an integer in the range <code>[0, 99]</code>.</li>
</ol>

<p>&nbsp;</p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## range-module

<p>A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.</p>

<p><li><code>addRange(int left, int right)</code> Adds the half-open interval <code>[left, right)</code>, tracking every real number in that interval.  Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval <code>[left, right)</code> that are not already tracked.</li></p>

<p><li><code>queryRange(int left, int right)</code> Returns true if and only if every real number in the interval <code>[left, right)</code>
 is currently being tracked.</li></p>

<p><li><code>removeRange(int left, int right)</code> Stops tracking every real number currently being tracked in the interval <code>[left, right)</code>.</li></p>

<p><b>Example 1:</b><br />
<pre>
<b>addRange(10, 20)</b>: null
<b>removeRange(14, 16)</b>: null
<b>queryRange(10, 14)</b>: true (Every number in [10, 14) is being tracked)
<b>queryRange(13, 15)</b>: false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
<b>queryRange(16, 17)</b>: true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
</pre>
</p>

<p><b>Note:</b>
<li>A half open interval <code>[left, right)</code> denotes all real numbers <code>left <= x < right</code>.</li>

<li><code>0 < left < right < 10^9</code> in all calls to <code>addRange, queryRange, removeRange</code>.</li>
<li>The total number of calls to <code>addRange</code> in a single test case is at most <code>1000</code>.</li>
<li>The total number of calls to <code>queryRange</code> in a single test case is at most <code>5000</code>.</li>
<li>The total number of calls to <code>removeRange</code> in a single test case is at most <code>1000</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## global-and-local-inversions

<p>We have some permutation <code>A</code> of <code>[0, 1, ..., N - 1]</code>, where <code>N</code> is the length of <code>A</code>.</p>

<p>The number of (global) inversions is the number of <code>i &lt; j</code> with <code>0 &lt;= i &lt; j &lt; N</code> and <code>A[i] &gt; A[j]</code>.</p>

<p>The number of local inversions is the number of <code>i</code> with <code>0 &lt;= i &lt; N</code> and <code>A[i] &gt; A[i+1]</code>.</p>

<p>Return <code>true</code>&nbsp;if and only if the number of global inversions is equal to the number of local inversions.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> A = [1,0,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> There is 1 global inversion, and 1 local inversion.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> A = [1,2,0]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are 2 global inversions, and 1 local inversion.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A</code> will be a permutation of <code>[0, 1, ..., A.length - 1]</code>.</li>
	<li><code>A</code> will have length in range <code>[1, 5000]</code>.</li>
	<li>The time limit for this problem has been reduced.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## number-of-matching-subsequences

<p>Given string <code>S</code> and a&nbsp;dictionary of words <code>words</code>, find the number of <code>words[i]</code> that is a subsequence of <code>S</code>.</p>

<pre>
<strong>Example :</strong>
<strong>Input:</strong> 
S = &quot;abcde&quot;
words = [&quot;a&quot;, &quot;bb&quot;, &quot;acd&quot;, &quot;ace&quot;]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three words in <code>words</code> that are a subsequence of <code>S</code>: &quot;a&quot;, &quot;acd&quot;, &quot;ace&quot;.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All words in <code>words</code> and <code>S</code> will only consists of lowercase letters.</li>
	<li>The length of <code>S</code> will be in the range of <code>[1, 50000]</code>.</li>
	<li>The length of <code>words</code> will be in the range of&nbsp;<code>[1, 5000]</code>.</li>
	<li>The length of <code>words[i]</code> will be in the range of <code>[1, 50]</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## positions-of-large-groups

<p>In a string&nbsp;<code>S</code>&nbsp;of lowercase letters, these letters form consecutive groups of the same character.</p>

<p>For example, a string like <code>S = &quot;abbxxxxzyy&quot;</code> has the groups <code>&quot;a&quot;</code>, <code>&quot;bb&quot;</code>, <code>&quot;xxxx&quot;</code>, <code>&quot;z&quot;</code> and&nbsp;<code>&quot;yy&quot;</code>.</p>

<p>Call a group <em>large</em> if it has 3 or more characters.&nbsp; We would like the starting and ending positions of every large group.</p>

<p>The final answer should be in lexicographic order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;abbxxxxzzy&quot;
<strong>Output: </strong>[[3,6]]
<strong>Explanation</strong>: <code>&quot;xxxx&quot; is the single </code>large group with starting  3 and ending positions 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;abc&quot;
<strong>Output: </strong>[]
<strong>Explanation</strong>: We have &quot;a&quot;,&quot;b&quot; and &quot;c&quot; but no large group.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;abcdddeeeeaabbbcd&quot;
<strong>Output: </strong>[[3,5],[6,9],[12,14]]</pre>

<p>&nbsp;</p>

<p><strong>Note:&nbsp;</strong>&nbsp;<code>1 &lt;= S.length &lt;= 1000</code></p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## maximize-distance-to-closest-person

<p>In a row of <code>seats</code>, <code>1</code> represents a person sitting in that seat, and <code>0</code> represents that the seat is empty.&nbsp;</p>

<p>There is at least one empty seat, and at least one person sitting.</p>

<p>Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.&nbsp;</p>

<p>Return that maximum distance to closest person.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,0,0,0,1,0,1]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,0,0,0]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= seats.length &lt;= 20000</code></li>
	<li><code>seats</code>&nbsp;contains only 0s or 1s, at least one <code>0</code>, and at least one <code>1</code>.</li>
</ol>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-average-subarray-ii

 The content is locked, copy the problem here. 
https://leetcode.com/problems/maximum-average-subarray-ii/description/
<a href = "https://leetcode.com/problems/ maximum-average-subarray-ii"> maximum-average-subarray-ii</a>
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

## magic-squares-in-grid

<p>A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers <strong>from 1 to 9</strong> such that each row, column, and both diagonals all have the same sum.</p>

<p>Given an <code>grid</code>&nbsp;of integers, how many 3 x 3 &quot;magic square&quot; subgrids are there?&nbsp; (Each subgrid is contiguous).</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
<strong>Output: </strong>1
<strong>Explanation: </strong>
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length&nbsp;&lt;= 10</code></li>
	<li><code>1 &lt;= grid[0].length&nbsp;&lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 15</code></li>
</ol>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## longest-line-of-consecutive-one-in-matrix

 The content is locked, copy the problem here. 
https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/
<a href = "https://leetcode.com/problems/ longest-line-of-consecutive-one-in-matrix"> longest-line-of-consecutive-one-in-matrix</a>
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

## my-calendar-i

<p>
Implement a <code>MyCalendar</code> class to store your events. A new event can be added if adding the event will not cause a double booking.
</p><p>
Your class will have the method, <code>book(int start, int end)</code>.  Formally, this represents a booking on the half open interval <code>[start, end)</code>, the range of real numbers <code>x</code> such that <code>start <= x < end</code>.
</p><p>
A <i>double booking</i> happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
</p><p>
For each call to the method <code>MyCalendar.book</code>, return <code>true</code> if the event can be added to the calendar successfully without causing a double booking.  Otherwise, return <code>false</code> and do not add the event to the calendar.
</p>

Your class will be called like this:
<code>MyCalendar cal = new MyCalendar();</code>
<code>MyCalendar.book(start, end)</code>

<p><b>Example 1:</b><br />
<pre>
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
<b>Explanation:</b> 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
</pre>
</p>

<p><b>Note:</b>
<li>The number of calls to <code>MyCalendar.book</code> per test case will be at most <code>1000</code>.</li>
<li>In calls to <code>MyCalendar.book(start, end)</code>, <code>start</code> and <code>end</code> are integers in the range <code>[0, 10^9]</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## x-of-a-kind-in-a-deck-of-cards

<p>In a deck of cards, each card has an integer written on it.</p>

<p>Return <code>true</code> if and only if you can choose&nbsp;<code>X &gt;= 2</code> such that&nbsp;it is possible to split the entire deck&nbsp;into 1 or more groups of cards, where:</p>

<ul>
	<li>Each group has exactly <code>X</code> cards.</li>
	<li>All the cards in each group have the same integer.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4,4,3,2,1]</span>
<strong>Output: </strong><span id="example-output-1">true
<strong>Explanation</strong>: Possible partition [1,1],[2,2],[3,3],[4,4]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1,2,2,2,3,3]</span>
<strong>Output: </strong><span id="example-output-2">false
</span><span id="example-output-1"><strong>Explanation</strong>: No possible partition.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1]</span>
<strong>Output: </strong><span id="example-output-3">false
</span><span id="example-output-1"><strong>Explanation</strong>: No possible partition.</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,1]</span>
<strong>Output: </strong><span id="example-output-4">true
</span><span id="example-output-1"><strong>Explanation</strong>: Possible partition [1,1]</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[1,1,2,2,2,2]</span>
<strong>Output: </strong><span id="example-output-5">true
</span><span id="example-output-1"><strong>Explanation</strong>: Possible partition [1,1],[2,2],[2,2]</span>
</pre>
</div>
</div>
</div>
</div>

<p><br />
<strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= deck.length &lt;= 10000</code></li>
	<li><code>0 &lt;= deck[i] &lt;&nbsp;10000</code></li>
</ol>

<div>
<div>
<div>
<div>
<div>&nbsp;</div>
</div>
</div>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## monotonic-array

<p>An array is <em>monotonic</em> if it is either monotone increasing or monotone decreasing.</p>

<p>An array <code>A</code> is monotone increasing if for all <code>i &lt;= j</code>, <code>A[i] &lt;= A[j]</code>.&nbsp; An array <code>A</code> is monotone decreasing if for all <code>i &lt;= j</code>, <code>A[i] &gt;= A[j]</code>.</p>

<p>Return <code>true</code> if and only if the given array <code>A</code> is monotonic.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,2,3]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[6,5,4,4]</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,3,2]</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,2,4,5]</span>
<strong>Output: </strong><span id="example-output-4">true</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[1,1,1]</span>
<strong>Output: </strong><span id="example-output-5">true</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>-100000 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-distance-in-arrays

 The content is locked, copy the problem here. 
https://leetcode.com/problems/maximum-distance-in-arrays/description/
<a href = "https://leetcode.com/problems/ maximum-distance-in-arrays"> maximum-distance-in-arrays</a>
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

## range-addition

 The content is locked, copy the problem here. 
https://leetcode.com/problems/range-addition/description/
<a href = "https://leetcode.com/problems/ range-addition"> range-addition</a>
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

## length-of-longest-fibonacci-subsequence

<p>A sequence <code>X_1, X_2, ..., X_n</code>&nbsp;is <em>fibonacci-like</em> if:</p>

<ul>
	<li><code>n &gt;= 3</code></li>
	<li><code>X_i + X_{i+1} = X_{i+2}</code>&nbsp;for all&nbsp;<code>i + 2 &lt;= n</code></li>
</ul>

<p>Given a <b>strictly increasing</b>&nbsp;array&nbsp;<code>A</code> of positive integers forming a sequence, find the <strong>length</strong> of the longest fibonacci-like subsequence of <code>A</code>.&nbsp; If one does not exist, return 0.</p>

<p>(<em>Recall that a subsequence is derived from another sequence <code>A</code> by&nbsp;deleting any number of&nbsp;elements (including none)&nbsp;from <code>A</code>, without changing the order of the remaining elements.&nbsp; For example, <code>[3, 5, 8]</code> is a subsequence of <code>[3, 4, 5, 6, 7, 8]</code>.</em>)</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[1,2,3,4,5,6,7,8]
<strong>Output: </strong>5
<strong>Explanation:
</strong>The longest subsequence that is fibonacci-like: [1,2,3,5,8].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[1,3,7,11,12,14,18]
<strong>Output: </strong>3
<strong>Explanation</strong>:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>3 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[0] &lt; A[1] &lt; ... &lt; A[A.length - 1] &lt;= 10^9</code></li>
	<li><em>(The time limit has been reduced by 50% for submissions in Java, C, and C++.)</em></li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## maximum-sum-circular-subarray

<p>Given a <strong>circular&nbsp;array</strong>&nbsp;<strong>C</strong> of integers represented by&nbsp;<code>A</code>, find the maximum possible sum of a non-empty subarray of <strong>C</strong>.</p>

<p>Here, a&nbsp;<em>circular&nbsp;array</em> means the end of the array connects to the beginning of the array.&nbsp; (Formally, <code>C[i] = A[i]</code> when <code>0 &lt;= i &lt; A.length</code>, and <code>C[i+A.length] = C[i]</code>&nbsp;when&nbsp;<code>i &gt;= 0</code>.)</p>

<p>Also, a subarray may only include each element of the fixed buffer <code>A</code> at most once.&nbsp; (Formally, for a subarray <code>C[i], C[i+1], ..., C[j]</code>, there does not exist <code>i &lt;= k1, k2 &lt;= j</code> with <code>k1 % A.length&nbsp;= k2 % A.length</code>.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,-2,3,-2]</span>
<strong>Output: </strong><span id="example-output-1">3
<strong>Explanation: </strong>Subarray [3] has maximum sum 3</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,-3,5]</span>
<strong>Output: </strong><span id="example-output-2">10
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [5,5] has maximum sum </span><span>5 + 5 = 10</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[3,-1,2,-1]</span>
<strong>Output: </strong><span id="example-output-3">4
<strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [2,-1,3] has maximum sum </span><span>2 + (-1) + 3 = 4</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,-2,2,-3]</span>
<strong>Output: </strong><span id="example-output-4">3
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [3] and [3,-2,2] both have maximum sum </span><span>3</span>
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[-2,-3,-1]</span>
<strong>Output: </strong><span id="example-output-5">-1
</span><span id="example-output-3"><strong>Explanation:</strong>&nbsp;</span><span id="example-output-1">Subarray [-1] has maximum sum -1</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ol>
	<li><code>-30000 &lt;= A[i] &lt;= 30000</code></li>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
</ol>
</div>
</div>
</div>
</div>
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
<br/>
<br/>
<br/>
<br/>
<br/>

## shortest-word-distance-iii

 The content is locked, copy the problem here. 
https://leetcode.com/problems/shortest-word-distance-iii/description/
<a href = "https://leetcode.com/problems/ shortest-word-distance-iii"> shortest-word-distance-iii</a>
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

## friends-of-appropriate-ages

<p>Some people will make friend requests. The&nbsp;list of their ages is given and&nbsp;<code>ages[i]</code>&nbsp;is the age of the&nbsp;ith person.&nbsp;</p>

<p>Person A will NOT friend request person B (B != A) if any of the following conditions are true:</p>

<ul>
	<li><code>age[B]&nbsp;&lt;= 0.5 * age[A]&nbsp;+ 7</code></li>
	<li><code>age[B]&nbsp;&gt; age[A]</code></li>
	<li><code>age[B]&nbsp;&gt; 100 &amp;&amp;&nbsp;age[A]&nbsp;&lt; 100</code></li>
</ul>

<p>Otherwise, A will friend request B.</p>

<p>Note that if&nbsp;A requests B, B does not necessarily request A.&nbsp; Also, people will not friend request themselves.</p>

<p>How many total friend requests are made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[16,16]
<strong>Output: </strong>2
<strong>Explanation: </strong>2 people friend request each other.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[16,17,18]
<strong>Output: </strong>2
<strong>Explanation: </strong>Friend requests are made 17 -&gt; 16, 18 -&gt; 17.</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>[20,30,100,110,120]
<strong>Output: </strong>
<strong>Explanation: </strong>Friend requests are made 110 -&gt; 100, 120 -&gt; 110, 120 -&gt; 100.
</pre>

<p>&nbsp;</p>

<p>Notes:</p>

<ul>
	<li><code>1 &lt;= ages.length&nbsp;&lt;= 20000</code>.</li>
	<li><code>1 &lt;= ages[i] &lt;= 120</code>.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## rle-iterator

<p>Write an iterator that iterates through a run-length encoded sequence.</p>

<p>The iterator is initialized by <code>RLEIterator(int[] A)</code>, where <code>A</code> is a run-length encoding of some&nbsp;sequence.&nbsp; More specifically,&nbsp;for all even <code>i</code>,&nbsp;<code>A[i]</code> tells us the number of times that the non-negative integer value <code>A[i+1]</code> is repeated in the sequence.</p>

<p>The iterator supports one function:&nbsp;<code>next(int n)</code>, which exhausts the next <code>n</code> elements&nbsp;(<code>n &gt;= 1</code>) and returns the last element exhausted in this way.&nbsp; If there is no element left to exhaust, <code>next</code>&nbsp;returns <code>-1</code> instead.</p>

<p>For example, we start with <code>A = [3,8,0,9,2,5]</code>, which is a run-length encoding of the sequence <code>[8,8,8,5,5]</code>.&nbsp; This is because the sequence can be read as&nbsp;&quot;three eights, zero nines, two fives&quot;.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;RLEIterator&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;,&quot;next&quot;]</span>, <span id="example-input-1-2">[[[3,8,0,9,2,5]],[2],[1],[1],[2]]</span>
<strong>Output: </strong><span id="example-output-1">[null,8,8,5,-1]</span>
<strong>Explanation: </strong>
RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
This maps to the sequence [8,8,8,5,5].
RLEIterator.next is then called 4 times:

.next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].

.next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].

.next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].

.next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
but the second term did not exist.  Since the last term exhausted does not exist, we return -1.

</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 1000</code></li>
	<li><code>A.length</code>&nbsp;is an even integer.</li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li>There are at most <code>1000</code> calls to <code>RLEIterator.next(int n)</code> per test case.</li>
	<li>Each call to&nbsp;<code>RLEIterator.next(int n)</code>&nbsp;will have <code>1 &lt;= n &lt;= 10^9</code>.</li>
</ol>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## transform-to-chessboard

<p>An N x N <code>board</code> contains only <code>0</code>s and <code>1</code>s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.</p>

<p>What is the minimum number of moves to transform the board into a &quot;chessboard&quot; - a board where no <code>0</code>s and no <code>1</code>s are 4-directionally adjacent? If the task is impossible, return -1.</p>

<pre>
<strong>Examples:</strong>
<strong>Input:</strong> board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --&gt; 1010 --&gt; 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.


<strong>Input:</strong> board = [[0, 1], [1, 0]]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.

<strong>Input:</strong> board = [[1, 0], [1, 0]]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
No matter what sequence of moves you make, you cannot end with a valid chessboard.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>board</code> will have the same number of rows and columns, a number in the range <code>[2, 30]</code>.</li>
	<li><code>board[i][j]</code> will be only <code>0</code>s or <code>1</code>s.</li>
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## max-chunks-to-make-sorted-ii

<p><em>This question is the same as &quot;Max Chunks to Make Sorted&quot; except the integers of the given array are not necessarily distinct, the input array could be up to length <code>2000</code>, and the elements could be up to <code>10**8</code>.</em></p>

<hr />

<p>Given an array <code>arr</code> of integers (<strong>not necessarily distinct</strong>), we split the array into some number of &quot;chunks&quot; (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.</p>

<p>What is the most number of chunks we could have made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [5,4,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn&#39;t sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,1,3,4,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>arr</code> will have length in range <code>[1, 2000]</code>.</li>
	<li><code>arr[i]</code> will be an integer in range <code>[0, 10**8]</code>.</li>
</ul>

<p>&nbsp;</p>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## flip-string-to-monotone-increasing

<p>A string of <code>&#39;0&#39;</code>s and <code>&#39;1&#39;</code>s is <em>monotone increasing</em> if it consists of some number of <code>&#39;0&#39;</code>s (possibly 0), followed by some number of <code>&#39;1&#39;</code>s (also possibly 0.)</p>

<p>We are given a string <code>S</code> of <code>&#39;0&#39;</code>s and <code>&#39;1&#39;</code>s, and we may flip any <code>&#39;0&#39;</code> to a <code>&#39;1&#39;</code> or a <code>&#39;1&#39;</code> to a <code>&#39;0&#39;</code>.</p>

<p>Return the minimum number of flips to make <code>S</code>&nbsp;monotone increasing.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;00110&quot;</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>We flip the last digit to get 00111.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;010110&quot;</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>We flip to get 011111, or alternatively 000111.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;00011000&quot;</span>
<strong>Output: </strong><span id="example-output-3">2</span>
<strong>Explanation: </strong>We flip to get 00000000.
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 20000</code></li>
	<li><code>S</code> only consists of <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code> characters.</li>
</ol>
</div>
</div>
</div>
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
<br/>
<br/>
<br/>
<br/>
<br/>

## partition-array-into-disjoint-intervals

<p>Given an array <code>A</code>, partition it&nbsp;into two (contiguous) subarrays&nbsp;<code>left</code>&nbsp;and <code>right</code>&nbsp;so that:</p>

<ul>
	<li>Every element in <code>left</code>&nbsp;is less than or equal to every element in <code>right</code>.</li>
	<li><code>left</code> and <code>right</code> are non-empty.</li>
	<li><code>left</code>&nbsp;has the smallest possible size.</li>
</ul>

<p>Return the <strong>length</strong> of <code>left</code> after such a partitioning.&nbsp; It is guaranteed that such a partitioning exists.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[5,0,3,8,6]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>left = [5,0,3], right = [8,6]
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1,0,6,12]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>left = [1,1,1,0], right = [6,12]
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length&nbsp;&lt;= 30000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^6</code></li>
	<li>It is guaranteed there is at least one way to partition <code>A</code> as described.</li>
</ol>

<div>
<div>&nbsp;</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## advantage-shuffle

<p>Given two arrays <code>A</code> and <code>B</code> of equal size, the <em>advantage of <code>A</code> with respect to <code>B</code></em> is the number of indices <code>i</code>&nbsp;for which <code>A[i] &gt; B[i]</code>.</p>

<p>Return <strong>any</strong> permutation of <code>A</code> that maximizes its advantage with respect to <code>B</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[2,7,11,15]</span>, B = <span id="example-input-1-2">[1,10,4,11]</span>
<strong>Output: </strong><span id="example-output-1">[2,11,7,15]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[12,24,8,32]</span>, B = <span id="example-input-2-2">[13,25,32,11]</span>
<strong>Output: </strong><span id="example-output-2">[24,32,8,12]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length = B.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= B[i] &lt;= 10^9</code></li>
</ol>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## split-array-with-equal-sum

 The content is locked, copy the problem here. 
https://leetcode.com/problems/split-array-with-equal-sum/description/
<a href = "https://leetcode.com/problems/ split-array-with-equal-sum"> split-array-with-equal-sum</a>
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

## minimum-increment-to-make-array-unique

<p>Given an array of integers A, a <em>move</em> consists of choosing any <code>A[i]</code>, and incrementing it by <code>1</code>.</p>

<p>Return the least number of moves to make every value in <code>A</code> unique.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,2]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong> After 1 move, the array could be [1, 2, 3].
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[3,2,1,2,1,7]</span>
<strong>Output: </strong><span id="example-output-2">6</span>
<strong>Explanation: </strong> After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 40000</code></li>
	<li><code>0 &lt;= A[i] &lt; 40000</code></li>
</ol>

<div>
<div>&nbsp;</div>
</div>
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
<br/>
<br/>
<br/>
<br/>
<br/>

## lonely-pixel-ii

 The content is locked, copy the problem here. 
https://leetcode.com/problems/lonely-pixel-ii/description/
<a href = "https://leetcode.com/problems/ lonely-pixel-ii"> lonely-pixel-ii</a>
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

## lonely-pixel-i

 The content is locked, copy the problem here. 
https://leetcode.com/problems/lonely-pixel-i/description/
<a href = "https://leetcode.com/problems/ lonely-pixel-i"> lonely-pixel-i</a>
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

## maximum-width-ramp

<p>Given an array <code>A</code> of integers, a <em>ramp</em>&nbsp;is a tuple <code>(i, j)</code> for which <code>i &lt; j</code>&nbsp;and&nbsp;<code>A[i] &lt;= A[j]</code>.&nbsp; The width of such a&nbsp;ramp is <code>j - i</code>.</p>

<p>Find the maximum width of a ramp in <code>A</code>.&nbsp; If one doesn&#39;t exist, return 0.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[6,0,8,2,1,5]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[9,8,1,0,1,9,4,0,4,1]</span>
<strong>Output: </strong><span id="example-output-2">7</span>
<strong>Explanation: </strong>
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
</pre>
</div>

<div>
<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 50000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 50000</code></li>
</ol>
</div>
</div>

<div>
<div>&nbsp;</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

## valid-mountain-array

<p>Given an array <code>A</code> of integers, return <code>true</code> if and only if it is a <em>valid mountain array</em>.</p>

<p>Recall that A is a mountain array if and only if:</p>

<ul>
	<li><code>A.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with&nbsp;<code>0 &lt; i&nbsp;&lt; A.length - 1</code>&nbsp;such that:
	<ul>
		<li><code>A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] </code></li>
		<li><code>A[i] &gt; A[i+1] &gt; ... &gt; A[B.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[3,5,5]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[0,3,2,1]</span>
<strong>Output: </strong><span id="example-output-3">true</span></pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000&nbsp;</code></li>
</ol>

<div>
<p>&nbsp;</p>

<div>
<div>&nbsp;</div>
</div>
</div>
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
<br/>
<br/>
<br/>
<br/>
<br/>

## array-of-doubled-pairs

<p>Given an array of integers <code>A</code>&nbsp;with even length, return <code>true</code> if and only if it is possible to reorder it such that <code>A[2 * i + 1] = 2 * A[2 * i]</code> for every <code>0 &lt;=&nbsp;i &lt; len(A) / 2</code>.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,3,6]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,1,2,6]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[4,-2,2,-4]</span>
<strong>Output: </strong><span id="example-output-3">true</span>
<strong>Explanation: </strong><span id="example-output-3">We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,2,4,16,8,4]</span>
<strong>Output: </strong><span id="example-output-4">false</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A.length</code> is even</li>
	<li><code>-100000 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>
</div>

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
<br/>
<br/>
<br/>
<br/>
<br/>

