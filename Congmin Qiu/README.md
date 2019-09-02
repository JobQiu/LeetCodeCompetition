# Array

## 4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays, we need to find the median of all the numbers in these two arrays.


For example, if nums1 = [1, 2], nums2 = [3, 4], we should return 2.5

### Solution

One easy solution is make a copy and use two pointers to get merged sorted array, contains all numbers, and then find the median.
Which cost O(N) time and O(N) space.

We can improve the space by just updating two pointers, until i+j == (len(A) + len(B)) // 2, then it will be O(N) time and O(1) space.

One faster solution: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481

split the first array using index i,
[0: i-1] belong to the left part, and [i:] belong to the right part.
split the second array using index j,
[0: j-1] belong to the left part, and [j:] belong to the right part.

i + j == (len(A) + len(B)) // 2


```python

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1, l2 = len(nums1), len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)
        if l1 == 0:
            if len(nums2) % 2 == 1:
                return nums2[len(nums2)//2]
            else:
                return (nums2[len(nums2)//2-1] + nums2[len(nums2)//2]) / 2.0

        halflen = (len(nums1) + len(nums2)+1) // 2
        lo, hi = 0, len(nums1)
        i = (lo + hi) // 2
        j = halflen - i


        lo = 0
        hi = len(nums1)
        while lo <= hi:
            i = (lo + hi) // 2
            j = halflen - i

            if i<len(nums1) and j > 0 and nums2[j-1] > nums1[i]:
                lo = i + 1
            elif i >0 and j < len(nums2) and nums1[i-1] > nums2[j]:
                hi = i
            else:
                break

        left = []
        if i > 0:
            left.append(nums1[i-1])
        if j > 0:
            left.append(nums2[j-1])
        leftmax=  max(left)
        if (len(nums1) + len(nums2)) % 2 == 1:
            return leftmax

        right = []
        if i < len(nums1):
            right.append(nums1[i])
        if j < len(nums2):
            right.append(nums2[j])
        rightmin = min(right)
        return (leftmax+rightmin) / 2.0
```
- Status: need redo, too many corner case
- Time: Sep 1, 2019 3:28 PM

## 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/

<img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" width="500px"/>
Idea, use two pointers.

- Status : skip
- Time: Sep 1, 2019 3:28 PM

## 53. Maximum Subarray

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

Idea: use two variable, 1. `result` to store the global optimal result, 2. `curMax` to store the sum of subarray end at current index.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = nums[0]
        curMax = nums[0]

        for num in nums[1:]:
            curMax = max(curMax + num, num)
            res = max(res, curMax)
        return res
```

- Status: skip
- Time: Sep 1, 2019 3:33 PM

---

## 42. Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/


<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" width="500px"/>

idea, use two pointers,

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxleft, maxright = 0, 0
        ans = 0
        while l<r:
            if height[l]<height[r]:
                if height[l]>=maxleft:
                    maxleft = height[l]
                else:
                    ans += maxleft - height[l]
                l+=1
            else:
                if height[r]>=maxright:
                    maxright = height[r]
                else:
                    ans += maxright - height[r]
                r-=1
        return ans
```

- Status: skip
- Time: Sep 1, 2019 3:40 PM

---

## 122. Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Given an array, [7,1,5,3,6,4], the number means the price of stock at a certain day, you can complete as many transactions as you want. can't buy and sell in the same day.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res
```

- Status: may skip
- Time: Sep 1, 2019 3:56 PM

----

## 85. Maximal Rectangle

https://leetcode.com/problems/maximal-rectangle/

Given a matrix, return the 
```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```








---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
---
