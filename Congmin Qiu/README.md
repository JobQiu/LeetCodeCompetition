# Greedy

## 406 Queue Reconstruction by Height

https://leetcode.com/problems/queue-reconstruction-by-height/

Given an array, for example, `[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]`. The first number in each tuple means the height, and the second number should be the number of higher people before him. We need to sort these tuples to make it right. For this example, the answer is `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]`.

### Solution

One idea is by sorting according (-height, numPeopleHigherBefore).
For this example, after sorting, the array becomes: `[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]`.

Then insert them into an empty array `[]` by result.insert(_2, (_1,_2)). For this example, it's like this:
- [<font color=red>[7,0]</font>]
- [[7,0], <font color=red>[7,1]</font>]
- [[7,0], <font color=red>[6,1]</font>, [7,1]]
- [<font color=red>[5,0]</font>, [7,0], [6,1], [7,1]]
- [[5,0], [7,0], <font color=red>[5,2]</font>, [6,1], [7,1]]
- [[5,0], [7,0], [5,2], [6,1], <font color=red>[4,4]</font>, [7,1]]

Because insert low people later will not influence those higher people.

``` python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:


```
