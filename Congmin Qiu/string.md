# string
## 13 Roman to Integer [Easy]

```
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        kv = {"I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 1000}
        res = 0
        if "IV" in s:
            res -= 2
        if "IX" in s:
            res -= 2
        if "XL" in s:
            res -= 20
        if "XC" in s:
            res -= 20
        if "CD" in s:
            res -= 200
        if "CM" in s:
            res -= 200

        for ch in s:
            res += kv[ch]
        return res

```
---
## 344 Reverse String [Easy]

```



```
---
## 6 ZigZag Conversion [Medium]

```

```
---
## 14 Longest Common Prefix [Easy]

```

```
---
## 3 Longest Substring Without Repeating Characters [Medium]

```

```
---
## 12 Integer to Roman [Medium]

```

```
---
## 20 Valid Parentheses [Easy]

```

```
---
## 5 Longest Palindromic Substring [Medium]

```

```
---
## 38 Count and Say [Easy]

```

```
---
## 22 Generate Parentheses [Medium]

```

```
---
## 10 Regular Expression Matching [Hard]

```

```
---
## 151 Reverse Words in a String [Medium]

```

```
---
## 929 Unique Email Addresses [Easy]

```

```
---
## 67 Add Binary [Easy]

```

```
---
## 49 Group Anagrams [Medium]

```

```
---
## 72 Edit Distance [Hard]

```

```
---
## 8 String to Integer (atoi) [Medium]

```

```
---
## 657 Robot Return to Origin [Easy]

```

```
---
## 273 Integer to English Words [Hard]

```

```
---
## 804 Unique Morse Code Words [Easy]

```

```
---
## 28 Implement strStr() [Easy]

```

```
---
## 557 Reverse Words in a String III [Easy]

```

```
---
## 43 Multiply Strings [Medium]

```

```
---
## 709 To Lower Case [Easy]

```

```
---
## 383 Ransom Note [Easy]

```

```
---
## 387 First Unique Character in a String [Easy]

```

```
---
## 76 Minimum Window Substring [Hard]

```

```
---
## 336 Palindrome Pairs [Hard]

```

```
---
## 345 Reverse Vowels of a String [Easy]

```

```
---
## 65 Valid Number [Hard]

```

```
---
## 32 Longest Valid Parentheses [Hard]

```

```
---
## 93 Restore IP Addresses [Medium]

```

```
---
## 647 Palindromic Substrings [Medium]

```

```
---
## 115 Distinct Subsequences [Hard]

```

```
---
## 125 Valid Palindrome [Easy]

```

```
---
## 30 Substring with Concatenation of All Words [Hard]

```

```
---
## 165 Compare Version Numbers [Medium]

```

```
---
## 91 Decode Ways [Medium]

```

```
---
## 681 Next Closest Time [Medium]

```

```
---
## 609 Find Duplicate File in System [Medium]

```

```
---
## 214 Shortest Palindrome [Hard]

```

```
---
## 97 Interleaving String [Hard]

```

```
---
## 58 Length of Last Word [Easy]

```

```
---
## 87 Scramble String [Hard]

```

```
---
## 71 Simplify Path [Medium]

```

```
---
## 126 Word Ladder II [Hard]

```

```
---
## 44 Wildcard Matching [Hard]

```

```
---
## 68 Text Justification [Hard]

```

```
---
## 227 Basic Calculator II [Medium]

```

```
---
## 696 Count Binary Substrings [Easy]

```

```
---
## 521 Longest Uncommon Subsequence I [Easy]

```

```
---
## 606 Construct String from Binary Tree [Easy]

```

```
---
## 564 Find the Closest Palindrome [Hard]

```

```
---
## 770 Basic Calculator IV [Hard]

```

```
---
## 541 Reverse String II [Easy]

```

```
---
## 686 Repeated String Match [Easy]

```

```
---
## 159 Longest Substring with At Most Two Distinct Characters [Hard]

```

```
---
## 632 Smallest Range [Hard]

```

```
---
## 340 Longest Substring with At Most K Distinct Characters [Hard]

```

```
---
## 161 One Edit Distance [Medium]

```

```
---
## 788 Rotated Digits [Easy]

```

```
---
## 819 Most Common Word [Easy]

```

```
---
## 537 Complex Number Multiplication [Medium]

```

```
---
## 761 Special Binary String [Hard]

```

```
---
## 767 Reorganize String [Medium]

```

```
---
## 158 Read N Characters Given Read4 II - Call multiple times [Hard]

```

```
---
## 459 Repeated Substring Pattern [Easy]

```

```
---
## 890 Find and Replace Pattern [Medium]

```

```
---
## 553 Optimal Division [Medium]

```

```
---
## 443 String Compression [Easy]

```

```
---
## 539 Minimum Time Difference [Medium]

```

```
---
## 157 Read N Characters Given Read4 [Easy]

```

```
---
## 722 Remove Comments [Medium]

```

```
---
## 680 Valid Palindrome II [Easy]

```

```
---
## 385 Mini Parser [Medium]

```

```
---
## 520 Detect Capital [Easy]

```

```
---
## 730 Count Different Palindromic Subsequences [Hard]

```

```
---
## 249 Group Shifted Strings [Medium]

```

```
---
## 937 Reorder Log Files [Easy]

```

```
---
## 772 Basic Calculator III [Hard]

```

```
---
## 583 Delete Operation for Two Strings [Medium]

```

```
---
## 791 Custom Sort String [Medium]

```

```
---
## 186 Reverse Words in a String II [Medium]

```

```
---
## 556 Next Greater Element III [Medium]

```

```
---
## 856 Score of Parentheses [Medium]

```

```
---
## 736 Parse Lisp Expression [Hard]

```

```
---
## 678 Valid Parenthesis String [Medium]

```

```
---
## 434 Number of Segments in a String [Easy]

```

```
---
## 468 Validate IP Address [Medium]

```

```
---
## 635 Design Log Storage System [Medium]

```

```
---
## 551 Student Attendance Record I [Easy]

```

```
---
## 893 Groups of Special-Equivalent Strings [Easy]

```

```
---
## 271 Encode and Decode Strings [Medium]

```

```
---
## 293 Flip Game [Easy]

```

```
---
## 544 Output Contest Matches [Medium]

```

```
---
## 899 Orderly Queue [Hard]

```

```
---
## 917 Reverse Only Letters [Easy]

```

```
---
## 859 Buddy Strings [Easy]

```

```
---
## 824 Goat Latin [Easy]

```

```
---
## 522 Longest Uncommon Subsequence II [Medium]

```

```
---
## 833 Find And Replace in String [Medium]

```

```
---
## 616 Add Bold Tag in String [Medium]

```

```
---
## 809 Expressive Words [Medium]

```

```
---
## 842 Split Array into Fibonacci Sequence [Medium]

```

```
---
## 916 Word Subsets [Medium]

```

```
---
## 848 Shifting Letters [Medium]

```

```
---
## 831 Masking Personal Information [Medium]

```

```
---
## 800 Similar RGB Color [Easy]

```

```
---
## 536 Construct Binary Tree from String [Medium]

```

```
---
## 527 Word Abbreviation [Hard]

```

```
---
## 816 Ambiguous Coordinates [Medium]

```

```
---
## 591 Tag Validator [Hard]

```

```
---
## 408 Valid Word Abbreviation [Easy]

```

```
---
## 936 Stamping The Sequence [Hard]

```

```
---
## 925 Long Pressed Name [Easy]

```

```
---
## 758 Bold Words in String [Easy]

```

```
---
## 555 Split Concatenated Strings [Medium]

```

```
---
