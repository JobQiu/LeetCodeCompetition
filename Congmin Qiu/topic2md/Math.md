# Math
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
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

