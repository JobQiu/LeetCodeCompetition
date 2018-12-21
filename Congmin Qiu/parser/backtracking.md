# backtracking
## 22 Generate Parentheses Medium

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

```

```
---
## 10 Regular Expression Matching Hard

```

```
---
## 46 Permutations Medium

```

```
---
## 79 Word Search Medium

```

```
---
## 39 Combination Sum Medium

```

```
---
## 89 Gray Code Medium

```

```
---
## 78 Subsets Medium

```

```
---
## 37 Sudoku Solver Hard

```

```
---
## 51 N-Queens Hard

```

```
---
## 93 Restore IP Addresses Medium

```

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

```

```
---
## 131 Palindrome Partitioning Medium

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

```

```
---
## 60 Permutation Sequence Medium

```

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

```

```
---
## 784 Letter Case Permutation Easy

```

```
---
## 90 Subsets II Medium

```

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

```

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
