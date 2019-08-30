satisfy# Greedy

## 406. Queue Reconstruction by Height

https://leetcode.com/problems/queue-reconstruction-by-height/

Given an array, for example, `[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]`. The first number in each tuple means the height, and the second number should be the number of higher people before him. We need to sort these tuples to make it right. For this example, the answer is `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]`.

### Solution

One idea is by sorting according (-height, numPeopleHigherBefore).
For this example, after sorting, the array becomes: `[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]`.

Then insert them into an empty array `[]` by result.insert(_2, (_1,_2)). For this example, it's like this:
- [**<font color=red>[7,0]</font>**]
- [[7,0], **<font color=red>[7,1]</font>**]
- [[7,0], **<font color=red>[6,1]</font>**, [7,1]]
- [**<font color=red>[5,0]</font>**, [7,0], [6,1], [7,1]]
- [[5,0], [7,0], **<font color=red>[5,2]</font>**, [6,1], [7,1]]
- [[5,0], [7,0], [5,2], [6,1], **<font color=red>[4,4]</font>**, [7,1]]

Because insert low people later will not influence those higher people.

``` python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) \
    -> List[List[int]]:

        def getKey(p ):
            return (-p[0], p[1])

        people = sorted(people, key=getKey)
        res = []
        for v, idx in people:
            res.insert(idx, [v, idx])
        return res
```
- Analysis: to sort the array, we need O(logN) time, and to insert, no matter you're using linked list or array list, you will need O(N) time to insert one tuple, then it's O(N^2).
- Status: May need redo
- Comment: brainteaser?
- Time: Aug 28, 2019 9:39 AM

---


## 316. Remove Duplicate Letters

https://leetcode.com/problems/remove-duplicate-letters/

Given a string only contains little letters, for example, `bcabc`, we need to remove all duplicate letters. for this example, it can be `bca`, `cab`, `abc`. And we need to return the one which is the smallest in lexicographical order among all possible results. For this example, we need to return `abc`.

### Solution

One idea is using a counter. For the example above it will be
b-2, c-2, a-1. And then use one pointer. Move this pointer and decrease the count corresponding to the character. Keep track the smallest lexicographical character.

```
bcabc
|
b-1,c-2,a-1, smallest is b
bcabc
 |
b-1,c-1,a-1, smallest is b
bcabc
  |
b-1,c-1,a-0, smallest is a, break
```

so the result should be "a"+removeDuplicateLetters("bc"), which is "abc".

```python
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        c = Counter(s)
        pos = 0

        for idx, ch in enumerate(s):
            if ch < s[pos]:
                pos = idx
            c[ch] -= 1
            if c[ch] == 0:
                break

        return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos],""))
```

But this is pretty slow.
We need to count every time we invoke this method, and because of recursion, so in the worst situation, it need O(N^2) time.

Another idea is using a Stack, continue to pop if current char is smaller than before. Unless the previous char is at its final position.

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        final = {ch:idx for idx,ch in enumerate(s)}
        stack = []
        seen = set()

        for idx, ch in enumerate(s):
            if ch not in seen:
                while stack and stack[-1] > ch and final[stack[-1]] > idx:
                    temp = stack.pop()
                    seen.remove(temp)
                stack.append(ch)
                seen.add(ch);
        return "".join(stack)
```

- Status: need redo
- Time : Aug 28, 2019 6:15 PM

---

## 45. Jump Game II
https://leetcode.com/problems/jump-game/
https://leetcode.com/problems/jump-game-ii/

Given an array, for example, [2,3,1,1,4], the number means from that position, the length you can jump.
From 2, you can jump to 3 or 1.
From 3, you can jump to 1 or 1 or 4.
So you only need 2 jumps to the end. You can always reach the end, so we don't need to worry about what to return when we can't reach the end.

### Solution:

So what we can do is using something like bfs. `start = 0, end = 0.` Iterate this range to get next start and end. Keep doing this until we reach the end.

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return 0

        res = 0
        start = 0
        end = 0
        while end < len(nums):
            nextEnd = end
            for i in range(start, end+1):
                nextEnd = max(nextEnd, i + nums[i])
                if nextEnd >= len(nums)-1:
                    return res + 1

            start = end + 1
            end = nextEnd
            res += 1
        return res
```

Other people's solution

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        len0 = len(nums)
        res = end = goal = 0
        for i in range(len0-1):
            goal = max(goal, i+nums[i])
            if i == end:
                res += 1
                end = goal
        return res
```

- Status: pass
- Comment: a classical bfs problem
- Time: Aug 28, 2019 6:31 PM

---

## 134. Gas Station
https://leetcode.com/problems/gas-station/

Given two arrays, gas and cost: gas  = [1,2,3,4,5]
cost = [3,4,5,1,2],

the gas means at a certain station, how much gas you can get, and cost means from a certain station to the next station, how much gas you will spend. The final station's next station is the first one.

The task is to find a station, from this station you can go to the end, then from the first station, you can reach this station again as a cycle. Assume there is only one possible station, or if not possible, return -1.

### Solution

Use 2 pointers. `start = len(gas)-1, end = 0`. Move start backward when gas is not enough, and move end forward when gas is still > 0.

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = len(gas) - 1
        end = 0

        cur = gas[-1] - cost[-1]
        while start > end:
            if cur > 0:
                cur += (gas[end] - cost[end])
                end += 1
            else:
                start -= 1
                cur += (gas[start]- cost[start])
        if cur >= 0:
            return start
        return -1
```

- Status: may need redo
- Comment: a little brainteaser.
- Time: Aug 28, 2019 6:59 PM

----

## 763. Partition Labels

https://leetcode.com/problems/partition-labels/

Given a string, for example, `ababcbacadefegdehijhklij`. Split it, and one kind of character will only exist in one of those strings after splitting.
For this example, it can be split into "ababcbaca", "defegde", "hijhklij", we need to return the length of them, i.e., `[9,7,8]`.


### Solution

We use a variable `last` to tracking the last position of all characters in this substring.

For the example above, the last index of every character is:
{'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}

So we iterate the string, and i from 0 to 8, the variable last, will be the max([8,5,7]), so when i = 8, we reach the current last, we stop and record it and start again from i=9.

```python
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        if not S:
            return res

        m = {ch:idx for idx, ch in enumerate(S)}

        last = 0
        start = 0
        for idx, ch in enumerate(S):
            if m[ch] > last:
                last = m[ch]
            if last == idx:
                res.append(last-start+1)
                start = last+1
        return res
```

- Status: need redo
- Comment: kind like merge intervals if you consider the start and end of a character as an interval.
- Time: Aug 28, 2019 7:38 PM

---

## 135. Candy
https://leetcode.com/problems/candy/
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

For example, [1, 0, 2],
we should assign [2,1,2], so we need to return 5.

### Solution

We can solve it use a two pass.

the forward pass, if current weight is larger than before, dp[i] = dp[i-1] + 1
else = 1.

For the backward pass, do the same thing, but pick the larger peak.

For our example, [1, 0, 2]
after the forward pass, it will be
[1, 1, 2]
after the backward pass, it will be [2, 1, 2]

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:

        if not ratings:
            return 0

        if len(ratings) <= 1:
            return len(ratings)

        dp = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                dp[i] = dp[i-1] + 1

        for i in reversed(range(len(ratings)-1)):
            if ratings[i] > ratings[i+1]:
                dp[i] = max(dp[i+1] + 1, dp[i])

        return sum(dp)
```

- Status: may need redo
- Analysis: two pass, so O(N) time, and need a dp to store something, so space is also O(N).
- Time: Aug 29, 2019 10:53 AM

Another Solution(164ms)

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = 0
        up, down = 0, 1
        pre = 0

        for cur in ratings:
            if cur >= pre:
                if down > 1:
                    if down > up:
                        ans += down - up
                    up = down = 1
                up = 1 if cur == pre else up + 1
                ans += up
            else:
                ans += down
                down += 1

            pre = cur

        if down > up:
            ans += down - up

        return ans
```

## 767. Reorganize String

https://leetcode.com/problems/reorganize-string/

Given a string, for example, "aab", we need to reorganize this string so that every pair of adjacent characters are not same, for our example, we should return "aba". If this kind of operation is not possible, for example, "aaab", we just need to return an empty string.
### Solution

An example for a much more complicated example:
"aafheihgiwehgsfhsaufwegb"

After sort by count:
['b', 'u', 'i', 'i', 's', 's', 'w', 'w', 'a', 'a', 'a', 'e', 'e', 'e', 'f', 'f', 'f', 'g', 'g', 'g', 'h', 'h', 'h', 'h']

The 1st half will be 'b', 'u', 'i', 'i', 's', 's', 'w', 'w', 'a', 'a', 'a', 'e',

The 2nd half will be 'e', 'e', 'f', 'f', 'f', 'g', 'g', 'g', 'h', 'h', 'h', 'h'.

We merge them and the output will be `beueififsfsgwgwgagahahaheh`


```python
  def reorganizeString3(self, S: str) -> str:
      a = sorted(sorted(S), key=S.count)
      print(a)
      h = len(a) // 2
      a[1::2], a[::2] = a[:h], a[h:]
      return ''.join(a) * (a[-1:] != a[-2:-1])
```

Some remaining questions:
1. how to write a lambda in python?
2. what does sorted(str) return? An array?


- Status: may need redo
- Analysis: sort will cost O(logN) in the worst situation, merge will cost O(N), so overall it's O(logN). Space, need O(N) to store the res.
- Comment: more like a string or array problem.
- Time: Aug 29, 2019 12:29 PM

---

## 714. Best Time to Buy and Sell Stock with Transaction Fee

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

prices = [1, 3, 2, 8, 4, 9], fee = 2

Given a price array, and transaction fee, we can do buy or sell in a certain, and each time we finish a buy-sell, we need to pay the transaction fee. And you must sell the stock before you buy it again.


### Solution

The idea here, is using 2 array to store temporary values.

buy[] and sell[], buy[i] means the max profit when the previous operation is buy. sell[i] means the max profit when the previous operation is sell.


```
For our example, [1,3,2,8,4,9]
buy[0] = -3
sell[0] = 0

to calculate buy[1]
you can buy unless your previous operation is sell, so one possible value is sell[0] - prices[1] - fee = 0 - 3 - 2 = -5. Or you can don't buy that day, then it's buy[0] = -3. We keep the larger one.

You can sell unless your previous operation is buy, so one possible value is buy[0] + prices[1] = 0, or you can don't sell. it's sell[0] = 0. We still keep the larger one.

Keep doing this to the end.
```

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = - prices[0] - fee
        sell = 0
        for i in range(1, len(prices)):
            buy, sell = max(buy, sell - prices[i] - fee), max(sell, buy+prices[i])
        return sell
```

This solution is faster

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        if len(prices) < 2:
            return 0

        profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price > min_price + fee:
                profit += price - min_price - fee
                min_price = price - fee  # save the fee for higher future price
        return profit   

"""
[1, 3, 2, 8, 4, 9]
min_price is 1,
when price = 3 > min_price, will do nothing
when price = 2, do nothing
when price is 8 > min_price + fee, so we will sell it, profit += 8-1-2 = 5
min_price = 8-2 = 6
so it means if we see some higher price, we will sell the stock at that price. if price < min_price, we can start another cycle, buy and sell again.
"""
```

- Status: need redo
- Time: Aug 29, 2019 5:11 PM

----

## 330. Patching Array

https://leetcode.com/problems/patching-array/

Given an array and an integer, nums = [1,3], n = 6 for example, we need to use these nums to get possible from 1 to n. From the current array, we can only get 1,3,4. So the task is to find minimum number of patches we need to add to satisfy that requirement. For this example, we just need to add a 2. We can only use each number once, otherwise you can just use 1 to get any possible sum. `(╯' - ')╯︵ ┻━┻`.

### Solution

for example nums = [2,5,10], n = 20.

for i from 1 to 20.

```python
class Solution:
    def minPatches2(self, nums: List[int], n: int) -> int:
        i, far, re = 0, 0, 0
        nums = sorted(nums)
        while far < n :
            if i < len(nums) and nums[i] <= far + 1:
                far += nums[i]
                i += 1
            else:
                re += 1
                far += far+1
        return re

    def minPatches(self, nums: List[int], n: int) -> int:
        covered = 0
        ans = 0
        for num in nums:
            while num > covered + 1:
                ans += 1
                covered = 2 * covered + 1
                if covered >= n:
                    return ans
            covered += num
            if covered >= n:
                return ans
        while covered < n:
            ans += 1
            covered = 2 * covered + 1
        return ans
```

- Status: need redo!
- Time: Aug 29, 2019 8:23 PM

---

## 376. Wiggle Subsequence

https://leetcode.com/problems/wiggle-subsequence/

Given an array, for example, [1,17,5,10,13,15,10,5,16,8], we need to find the length of the longest subsequence which is a wiggle subsequence. For the example above it can be [1,17,10,13,10,16,8], so we need to return 7.

### Solution

We can use a dp to store the last state is up or down. If current value is larger than previous value, we can update up[i] to be down[i-1] + 1.


for our example,

|      | 1   | 17  | 5   | 10  | 13  | 15  | 10  | 5   | 16  | 8   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| up   | `1`  | 1+1=2 |  2    | 3+1=4    |  4   | 4    |  4   |    4 |  5+1=6   | 6    |
| down | 1   | `1`   | 2+1=3    |  3   |   3  | 3     | 4+1=5    |5     | 5    | 6+1=7    |

So we should return 7 for this example.

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if not nums:
            return 0

        up = [1] * len(nums)
        down = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(down[-1], up[-1])
```

Based on this, we can continue to optimize it by using two variable instead of two arrays.

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down= up + 1
        return max(down, up)
```
---

## 452. Minimum Number of Arrows to Burst Balloons

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Given some intervals, [[10,16], [2,8], [1,6], [7,12]], the two numbers of each tuple means the start and end of a certain ballon, for some balloons, we can burst them using one arrow.

<img src="https://ws3.sinaimg.cn/large/006y8mN6ly1g6i5i2gy9fj31400u0x6p.jpg" width="250px"/>

As you can see, we just need 2 arrows for this example, so just return 2.

```python
class Solution:
    def findMinArrowShots(self, p ):
        res = 0
        if not p:
            return res
        p.sort(key=lambda x:x[1])
        res += 1
        start, end = p[0]

        for s, e in p[1:]:
            if s > end:
                res += 1
                end = e
        return res
```
- Status: don't need redo
- Time: Aug 30, 2019 11:06 AM

---

## 392. Is Subsequence

https://leetcode.com/problems/is-subsequence/

Example 1:
s = "abc", t = "ahbgdc". Return true.

Example 2:
s = "axc", t = "ahbgdc". Return false.

### Solution

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for ch in s:
            idx = t.find(ch)
            if idx == -1:
                return False
            t = t[idx+1:]
        return True
```

- Status: may need redo
- Time: Aug 30, 2019 11:16 AM

---


## 765. Couples Holding Hands

https://leetcode.com/problems/couples-holding-hands/








----
