# Greedy

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
- Time: Aug 28, 2019 6:31 PM

---

## 134. Gas Station
https://leetcode.com/problems/gas-station/

Given two arrays, gas and cost: gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
