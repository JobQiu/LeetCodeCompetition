# backtracking

## 22 Generate Parentheses Medium
Dec 21, 2018 1:21 PM
```
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(0,0,res,n, "")
        return res


    def helper(self, l, r ,res, max, cur):
        if len(cur) == max * 2:
            res.append(cur)
            return

        if l < max:
            self.helper(l+1,r, res, max, cur+'(')
        if r < l:
            self.helper(l, r+1, res, max, cur +')')
```
---
## 17 Letter Combinations of a Phone Number Medium

Dec 21, 2018 1:44 PM

```

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []

        if len(digits) == 0:
            return res

        self.m = {'2':"abc", '3':"def", '4':"ghi",'5':"jkl",'6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        self.helper(len(digits), "", res, digits )
        return res

        pass
    def helper(self, max_, cur, res, digits):
        if len(cur) == max_:
            res.append(cur)
            return

        for char in self.m[digits[len(cur)]]:
            self.helper(max_, cur + char, res, digits)
```
---
## 10 Regular Expression Matching Hard
skip because i will do this in dp
```

```
---
## 46 Permutations Medium
Dec 21, 2018 1:53 PM

Two solution, backtracking and swap

```
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums,0,res)
        return res

        pass

    def helper(self, nums, start, res ):
        if start == len(nums):
            res.append(list(nums))
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.helper(nums, start+1, res)
            nums[start], nums[i] = nums[i], nums[start]


```

The idea here is let each number appears once in the certain position.



---
## 79 Word Search Medium
skip
```

```
---
## 39 Combination Sum Medium
Dec 21, 2018 4:28 PM
```

class Solution:
    def helper(self, candidates, remain, res, cur, start):
        if remain < 0:
            return
        if remain == 0:
            res.append(list(cur))
            return

        for i in range(start, len(candidates)):
            num = candidates[i]
            if num <= remain:
                cur.append(num)
                self.helper(candidates, remain - num, res, cur, i)
                cur.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        res = []
        cur = []
        self.helper(candidates, target, res, cur, 0)
        return res


```
---
## 89 Gray Code Medium

```

```
---
## 78 Subsets Medium
Dec 21, 2018 9:13 PM

```

class Solution:
    def helper(self, nums, res, cur,start ):
        if  start == len(nums):
            res.append(list(cur))
            return

        self.helper(nums,res, list(cur), start+1)
        cur.append(nums[start])
        self.helper(nums,res, list(cur), start+1)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        self.helper(nums,res, cur, 0)
        return res




```
---
## 37 Sudoku Solver Hard
skip, will do this later
```

```
---
## 51 N-Queens Hard
don't have any idea
Dec 21, 2018 9:36 PM
```

class Solution:
    def helper(self, queens, xy_dif, xy_sum, n, res):
        p = len(queens)
        if p == n:
            res.append(queens)
            return

        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                self.helper(queens + [q], xy_dif + [p - q], xy_sum + [p + q], n, res)

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.helper([], [], [], n, res)
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in res]


```

take away, really smart of using diagonal

---
## 93 Restore IP Addresses Medium

```

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(ss):
            if len(ss) > 3 or len(ss) == 0:
                return False
            if ss[0]=='0' and  len(ss)>1:
                return False
            if (int)(ss) > 255:
                return False
            return True

        res = []
        i=0
        while i<4 and i<len(s) - 2:
            j = i+1
            if not isValid(s[0:i]):
                i+=1
                continue
            while j < i+4 and j < len(s) - 1:
                if not isValid(s[i:j]):
                    j+=1
                    continue
                k=j+1
                while k<j+4 and k<len(s):
                    if not isValid(s[j:k]) or not isValid(s[k:]):
                        k+=1
                        continue
                    res.append("{}.{}.{}.{}".format(s[0:i],s[i:j], s[j:k],s[k:] ))
                    k+=1

                j+=1

            i+=1
        return res


```
---
## 140 Word Break II Hard

```

```
---
## 306 Additive Number Medium

```

```
---
## 357 Count Numbers with Unique Digits Medium

```

```
---
## 77 Combinations Medium

Dec 21, 2018 10:56 PM

```

class Solution:
    def helper(self, res ,cur , start, n, k):
        if len(cur) == k:
            res.append(cur)
        for i in range(start, n+1):
            cur.append(i)
            self.helper(res,list( cur),i+1, n, k )
            cur.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], 1,n,k)
        return res

```
---
## 131 Palindrome Partitioning Medium
Dec 21, 2018 10:58 PM
don't have any idea
```

```
---
## 52 N-Queens II Hard

```

```
---
## 126 Word Ladder II Hard

```

```
---
## 216 Combination Sum III Medium
Dec 21, 2018 9:08 PM

take away is when the answer is not duplicate, we can just search the smallest one firstly.


```

class Solution:
    def helper(self, remain, k ,  cur, res, start):
        if len(cur) == k and remain == 0:
            res.append(list(cur))
            return

        for i in range(start, 10):
            cur.append(i)
            self.helper(remain - i, k, cur, res, i + 1)
            cur.pop()



    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res= []
        cur = []
        self.helper(n, k, cur,res,1)
        return res

```
---
## 60 Permutation Sequence Medium

```
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k-1

        candidate = []
        for i in range(n):
            candidate.append(i+1)
        factrials = [1]
        for i in range(2,n):
            factrials.append(factrials[-1]*i)
        res = ""
        while len(factrials) > 0:
            fac = factrials.pop()
            index_ = k//fac
            value = candidate[index_]
            res += (str)(value)
            k = k - fac*index_
            candidate.remove(value)

        if len(candidate) > 0:
            res = res + (str)(candidate[0])
        return res


```
---
## 44 Wildcard Matching Hard

```

```
---
## 401 Binary Watch Easy

```

```
---
## 212 Word Search II Hard

```

```
---
## 47 Permutations II Medium

swap version:

```
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.helper(nums, 0, len(nums), res)
        return res

    def helper(self, nums, start, end, res):
        if start == end - 1:
            res.append(nums)
            return

        for i in range(start, end):
            if i != start and nums[i] == nums[start]:
                continue

            nums[i], nums[start] = nums[start], nums[i]
            self.helper( list(nums), start+1, end, res)

```

---

The trick here to avoid duplicate is
`if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:continue`

```

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        used = [False] * len(nums)
        cur = []

        nums.sort()
        self.helper(nums, res, cur, used)
        return res

    def helper(self, nums, res, cur, used):
        pass

        if len(cur) == len(nums):
            res.append(list(cur))
            return

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            if used[i]:
                continue

            used[i] = True
            cur.append(nums[i])
            self.helper(nums, res, cur, used)
            cur.pop()
            used[i] = False

```
---
## 784 Letter Case Permutation Easy

```

```
---
## 90 Subsets II Medium

```

from collections import Counter

class Solution:


    def helper(self, nums, counter, res, cur, start):

        if  start == len(nums):
            res.append(list(cur))
            return

        self.helper(nums,counter, res, list(cur), start+1)
        for i in range(counter[nums[start]]):
            cur.append(nums[start])
            self.helper(nums,counter, res, list(cur), start+1)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = Counter(nums)
        nums = list(counter.keys())
        nums.sort()
        res = []
        self.helper(nums, counter, res, [], 0)
        return res


```
---
## 526 Beautiful Arrangement Medium

```

```
---
## 320 Generalized Abbreviation Medium

```

```
---
## 291 Word Pattern II Hard

```

```
---
## 40 Combination Sum II Medium
Dec 21, 2018 4:31 PM 秒解
```

class Solution:
    def helper(self, candidates, remain, res, cur, start ):
        if remain < 0:
            return
        if remain == 0:
            res.append(list(cur))
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            num = candidates[i]
            if num <= remain:
                cur.append(num)
                self.helper(candidates, remain - num, res, cur, i + 1)
                cur.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        cur = []
        candidates.sort()
        self.helper(candidates, target, res, cur , 0)
        return res



```
---
## 211 Add and Search Word - Data structure design Medium

```

```
---
## 351 Android Unlock Patterns Medium

```

```
---
## 254 Factor Combinations Medium

```

```
---
## 267 Palindrome Permutation II Medium

```

```
---
## 294 Flip Game II Medium

```

```
---
## 425 Word Squares Hard

```

```
---
## 842 Split Array into Fibonacci Sequence Medium

```

```
---
## 411 Minimum Unique Word Abbreviation Hard

```

```
---
## 691 Stickers to Spell Word Hard

```

```
---
