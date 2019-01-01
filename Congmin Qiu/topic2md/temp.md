# Math
## palindrome-number

<p>Determine whether an integer is a palindrome. An integer&nbsp;is&nbsp;a&nbsp;palindrome when it&nbsp;reads the same backward as forward.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 121
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p><strong>Follow up:</strong></p>

<p>Coud you solve&nbsp;it without converting the integer to a string?</p>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## reverse-integer

<p>Given a 32-bit signed integer, reverse digits of an integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 123
<strong>Output:</strong> 321
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> -123
<strong>Output:</strong> -321
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> 120
<strong>Output:</strong> 21
</pre>

<p><strong>Note:</strong><br />
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.</p>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## add-digits

<p>Given a non-negative integer <code>num</code>, repeatedly add all its digits until the result has only one digit.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>38</code>
<strong>Output:</strong> 2 
<strong>Explanation: </strong>The process is like: <code>3 + 8 = 11</code>, <code>1 + 1 = 2</code>. 
&nbsp;            Since <code>2</code> has only one digit, return it.
</pre>

<p><b>Follow up:</b><br />
Could you do it without any loop/recursion in O(1) runtime?</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## string-to-integer-atoi

<p>Implement <code><span>atoi</span></code> which&nbsp;converts a string to an integer.</p>

<p>The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.</p>

<p>The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.</p>

<p>If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.</p>

<p>If no valid conversion could be performed, a zero value is returned.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Only the space character <code>&#39; &#39;</code> is considered as whitespace character.</li>
	<li>Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]. If the numerical value is out of the range of representable values, INT_MAX (2<sup>31&nbsp;</sup>&minus; 1) or INT_MIN (&minus;2<sup>31</sup>) is returned.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;42&quot;
<strong>Output:</strong> 42
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;   -42&quot;
<strong>Output:</strong> -42
<strong>Explanation:</strong> The first non-whitespace character is &#39;-&#39;, which is the minus sign.
&nbsp;            Then take as many numerical digits as possible, which gets 42.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;4193 with words&quot;
<strong>Output:</strong> 4193
<strong>Explanation:</strong> Conversion stops at digit &#39;3&#39; as the next character is not a numerical digit.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> &quot;words and 987&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The first non-whitespace character is &#39;w&#39;, which is not a numerical 
&nbsp;            digit or a +/- sign. Therefore no valid conversion could be performed.</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> &quot;-91283472332&quot;
<strong>Output:</strong> -2147483648
<strong>Explanation:</strong> The number &quot;-91283472332&quot; is out of the range of a 32-bit signed integer.
&nbsp;            Thefore INT_MIN (&minus;2<sup>31</sup>) is returned.</pre>

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## number-of-digit-one

<p>Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 13
<strong>Output:</strong> 6 
<strong>Explanation: </strong>Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
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

## integer-to-english-words

<p>Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2<sup>31</sup> - 1.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 123
<b>Output:</b> &quot;One Hundred Twenty Three&quot;
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 12345
<b>Output:</b> &quot;Twelve Thousand Three Hundred Forty Five&quot;</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> 1234567
<b>Output:</b> &quot;One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven&quot;
</pre>

<p><b>Example 4:</b></p>

<pre>
<b>Input:</b> 1234567891
<b>Output:</b> &quot;One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One&quot;
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

## bulb-switcher

<p>There are <i>n</i> bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it&#39;s off or turning off if it&#39;s on). For the <i>i</i>-th round, you toggle every <i>i</i> bulb. For the <i>n</i>-th round, you only toggle the last bulb. Find how many bulbs are on after <i>n</i> rounds.</p>

<p><b>Example:</b></p>

<pre>
<strong>Input: </strong>3
<strong>Output:</strong> 1 
<strong>Explanation:</strong> 
At first, the three bulbs are <b>[off, off, off]</b>.
After first round, the three bulbs are <b>[on, on, on]</b>.
After second round, the three bulbs are <b>[on, off, on]</b>.
After third round, the three bulbs are <b>[on, off, off]</b>. 

So you should return 1, because there is only one bulb is on.
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

## missing-number

<p>Given an array containing <i>n</i> distinct numbers taken from <code>0, 1, 2, ..., n</code>, find the one that is missing from the array.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [3,0,1]
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [9,6,4,2,3,5,7,0,1]
<b>Output:</b> 8
</pre>

<p><b>Note</b>:<br />
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?</p>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## multiply-strings

<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as strings, return the product of <code>num1</code> and <code>num2</code>, also represented as a string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;2&quot;, num2 = &quot;3&quot;
<strong>Output:</strong> &quot;6&quot;</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = &quot;123&quot;, num2 = &quot;456&quot;
<strong>Output:</strong> &quot;56088&quot;
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The length of both <code>num1</code> and <code>num2</code> is &lt; 110.</li>
	<li>Both <code>num1</code> and <code>num2</code> contain&nbsp;only digits <code>0-9</code>.</li>
	<li>Both <code>num1</code> and <code>num2</code>&nbsp;do not contain any leading zero, except the number 0 itself.</li>
	<li>You <strong>must not use any built-in BigInteger library</strong> or <strong>convert the inputs to integer</strong> directly.</li>
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

## perfect-squares

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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## count-primes

<p>Count the number of prime numbers less than a non-negative number, <b><i>n</i></b>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
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

## sqrtx

<p>Implement <code>int sqrt(int x)</code>.</p>

<p>Compute and return the square root of <em>x</em>, where&nbsp;<em>x</em>&nbsp;is guaranteed to be a non-negative integer.</p>

<p>Since the return type&nbsp;is an integer, the decimal digits are truncated and only the integer part of the result&nbsp;is returned.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 4
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since 
&nbsp;            the decimal part is truncated, 2 is returned.
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

## basic-calculator

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

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## arithmetic-slices

<p>A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.</p>

<p>For example, these are arithmetic sequence:</p>
<pre>1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>The following sequence is not arithmetic.</p> <pre>1, 1, 2, 5, 7</pre> 
<br/>

<p>A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.</p>

<p>A slice (P, Q) of array A is called arithmetic if the sequence:<br/>
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.</p>

<p>The function should return the number of arithmetic slices in the array A. </p>
<br/>

<p><b>Example:</b>
<pre>
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
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

## fraction-to-recurring-decimal

<p>Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.</p>

<p>If the fractional part is repeating, enclose the repeating part in parentheses.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> numerator = 1, denominator = 2
<strong>Output:</strong> &quot;0.5&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> numerator = 2, denominator = 1
<strong>Output:</strong> &quot;2&quot;</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> numerator = 2, denominator = 3
<strong>Output: </strong>&quot;0.(6)&quot;
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

## ugly-number-ii

<p>Write a program to find the <code>n</code>-th ugly number.</p>

<p>Ugly numbers are<strong> positive numbers</strong> whose prime factors only include <code>2, 3, 5</code>.&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 12
<strong>Explanation: </strong><code>1, 2, 3, 4, 5, 6, 8, 9, 10, 12</code> is the sequence of the first <code>10</code> ugly numbers.</pre>

<p><strong>Note: </strong>&nbsp;</p>

<ol>
	<li><code>1</code> is typically treated as an ugly number.</li>
	<li><code>n</code> <b>does not exceed 1690</b>.</li>
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

## integer-break

<p>Given a positive integer <i>n</i>, break it into the sum of <b>at least</b> two positive integers and maximize the product of those integers. Return the maximum product you can get.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">2</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>2 = 1 + 1, 1 &times; 1 = 1.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">10</span>
<strong>Output: </strong><span id="example-output-2">36</span>
<strong>Explanation: </strong>10 = 3 + 3 + 4, 3 &times;&nbsp;3 &times;&nbsp;4 = 36.</pre>

<p><b>Note</b>: You may assume that <i>n</i> is not less than 2 and not larger than 58.</p>
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

## best-meeting-point

null
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

## nth-digit

<p>Find the <i>n</i><sup>th</sup> digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... </p>

<p><b>Note:</b><br />
<i>n</i> is positive and will fit within the range of a 32-bit signed integer (<i>n</i> < 2<sup>31</sup>).
</p>

<p><b>Example 1:</b>
<pre>
<b>Input:</b>
3

<b>Output:</b>
3
</pre>
</p>

<p><b>Example 2:</b>
<pre>
<b>Input:</b>
11

<b>Output:</b>
0

<b>Explanation:</b>
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
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

## largest-divisible-subset

<p>Given a set of <b>distinct</b> positive integers, find the largest subset such that every pair (S<sub>i</sub>, S<sub>j</sub>) of elements in this subset satisfies:</p>

<p>S<sub>i</sub> % S<sub>j</sub> = 0 or S<sub>j</sub> % S<sub>i</sub> = 0.</p>

<p>If there are multiple solutions, return any subset is fine.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3]</span>
<strong>Output: </strong><span id="example-output-1">[1,2] </span>(of course, [1,3] will also be ok)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,4,8]</span>
<strong>Output: </strong><span id="example-output-2">[1,2,4,8]</span>
</pre>
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

## super-ugly-number

<p>Write a program to find the <code>n<sup>th</sup></code> super ugly number.</p>

<p>Super ugly numbers are positive numbers whose all prime factors are in the given prime list <code>primes</code> of size <code>k</code>.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> n = 12, <code>primes</code> = <code>[2,7,13,19]</code>
<b>Output:</b> 32 
<strong>Explanation: </strong><code>[1,2,4,7,8,13,14,16,19,26,28,32] </code>is the sequence of the first 12 
             super ugly numbers given <code>primes</code> = <code>[2,7,13,19]</code> of size 4.</pre>

<p><b>Note:</b></p>

<ul>
	<li><code>1</code> is a super ugly number for any given <code>primes</code>.</li>
	<li>The given numbers in <code>primes</code> are in ascending order.</li>
	<li>0 &lt; <code>k</code> &le; 100, 0 &lt; <code>n</code> &le; 10<sup>6</sup>, 0 &lt; <code>primes[i]</code> &lt; 1000.</li>
	<li>The n<sup>th</sup> super ugly number is guaranteed to fit in a 32-bit signed integer.</li>
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

