### 7. 2018DEC

https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/

可以过test case，但是需要注意的是，如果k=0，需要返回0，我当时一直以为空字符串也属于答案，返回1。。被这个case卡了40分钟。。


https://yeqiuquan.blogspot.com/2017/03/lintcode-597-subtree-with-maximum.html



### test


1) 给定一个integer数组（无序）和2个node值，求构建bst(不可调整树）后，两个node的距离。2) 给定一个string 和K值，求包含 k个不同字符的子串集合。

https://www.1point3acres.com/bbs/thread-468865-1-1.html

https://yidongzhang.gitbooks.io/-oa-1/content/golf-event.html

https://www.1point3acres.com/bbs/thread-448373-1-1.html

1. 最长回文串。 LC 原题
2. 计算一个string中的高频word， 且word 不能在 wordToExclude中。 这部分我有两个tests没过。看了好久没看出来哪有错。。。



### 6. 2018 DEC

https://www.1point3acres.com/bbs/thread-465806-1-1.html

第一题是给一个list，每个element是<productId, productRating>，求每个product最高的5个评分的平均值，不是很难，不过要尽力快一点，第二题还是蛮花时间的。-baidu 1point3acres

第二题，给一个list，每个元素是<warehouseA, warehouseB, cost>，其实就是一条边， 求能把所有warehouse连起来的边集合，同时cost最小。这题实际上是一个MST的问题，写之前可以google一下求MST的算法，练一练。

第二题 mst 给你一堆connection 求能链接所有城市的最小的cost。 具体谷歌搜索 mst algorithm 就有类似的题。 感觉这是oa2的标配。 做得时候最后有一个testcase 想了很久， 就是如果不能成功的链接所有程序，例如用unionfind 有一个 城市跟别的城市不一样组，就返回空list


https://www.1point3acres.com/bbs/thread-464257-1-1.html


https://www.1point3acres.com/bbs/thread-468316-1-1.html

多叉树最大平均，和最小生成树。



### 5. 2019 Jan

2019(1-3月) 码农类General 本科 全职@Amazon - 内推 - 在线笔试  | Other | fresh grad应届毕业生
十月中旬投的，圣诞前收到OA。总的来说做之前看看地里的面经资料挺有用的，基本是原题或者类似的。OA1记不太清了：
1.debug的错是很明显的，主要是&&写成了||， +变成了-， 忘记++导致死循环这些错误。
2.logic部分大家都说时间比较充分，但是还是要看好时间，楼主就没有做完==

OA2:
1.work simulation：推荐大家看下面这个帖子，非常有用，我的simulation部分基本是这个帖里面的
https://www.1point3acres.com/bbs ... read&tid=468231
2.coding:


第一题：two sum变种，给一个数组和一个上限数字，从数组中找出和最大但不超过上限的pair(有tie只需要输出任意一个)
直接二层循环O(n^2)就能过了，也许排序+2 pointers的方法也可以，楼主没有尝试。

```python

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi )// 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                hi = mid
            else:
                lo = mid+1
        return lo

    def main(self, A, B, target):
        if len(A) > len(B):
            return self.main(B,A)

        A.sort()
        for num in B:
            insertPos = self.searchInsert(A, target-num)
            if A[insertPos] + num == target:
                return [A[insertPos], num]
            if insertPos > 0:
                sum_ = A[insertPos]-1 +  num
                if target - sum_ < prevDistance:
                  update ...



```

第二题：给一个text的string和一个excluded words的list， 要求统计text中单词的词频，输出不在excluded words中的词频最大的单词(有tie要输出所有)
这道题有两个细节：1）不区分大小写 2）所有不是字母的char都看成space，例如“ben‘s car“里有"ben", "s"和"car"三个单词。
方法就是一个hashset存excluded word， 一个hashmap存单词词频，然后扫一遍text就行了。

lc819

https://leetcode.com/problems/most-common-word/description/

```python

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        banWords = set(banned)

        import re
        from collections import Counter
        from collections import defaultdict
        p = paragraph.lower()
        words = re.findall(r'\w+', p)

        counter = defaultdict(int)
        maxCount = 0
        res = ""
        for word in words:
            if word in banWords:
                continue
            counter[word] += 1
            if counter[word] > maxCount:
                maxCount = counter[word]
                res = word
        return res





```

### 4. 2019 Jan两道

https://www.1point3acres.com/bbs/thread-469583-1-1.html


<img src="https://www.1point3acres.com/bbs/data/attachment/forum/201901/07/093147l4l4ikkob6qbb4l9.jpg" width="550px"/>

```python
from collections import deque

def maze(A):
  if A[0][0] == 0:
    return -1 # or False,
  dq = deque()


  num_row = len(A)
  num_col = len(A[0])

  dq.append((0,0))
  visited = set()
  visited.add((0,0));

  while len(dq) >0 :
    size_ = len(dq)

    for i in range(size_):
      x, y = dq.pop();
      for nextX, nextY in ((x+1,y), (x-1,y), (x,y+1),(x, y-1)):
        if (nextX, nextY) not in visited and nextX > 0 and nextX <:
          if A[nextX][nextY] == 9:
            pass, reach the res, return
          elif == 1:
            pass, put into dq
          else:
            don't put this into the dq

    return not reachable.


```

<img src="https://www.1point3acres.com/bbs/data/attachment/forum/201901/07/093146lfi2f568afqdqd5w.jpg" width="950px"/>

本质是最近的K个点，下面有quick的code

return List<List<Integer>>


```python

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        banWords = set(banned)

        import re
        from collections import Counter
        from collections import defaultdict
        p = paragraph.lower()
        words = re.findall(r'\w+', p)

        counter = defaultdict(int)
        maxCount = 0
        res = ""
        for word in words:
            if word in banWords:
                continue
            counter[word] += 1
            if counter[word] > maxCount:
                maxCount = counter[word]
                res = word
        return res





```

2.第二题是0代表空地，1代表building， 9代表obstacle，最短距离。

停车场里找obstable最短路径的题目。这题难度高一点，但只要会BFS，基本无难度。。。只是最后记得没找到obstacle要返回-1，不然只会过12个test case。加了这行就16


### 3. 2018 DEC两题

https://www.1point3acres.com/bbs/thread-468910-1-1.html


![](https://ws3.sinaimg.cn/large/006tNc79ly1fz1g2m3140j31sg03kwgj.jpg)

第一题 可以参考 https://leetcode.com/problems/kth-largest-element-in-an-array/description/

```python

# quick select


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(arr, lo, hi ):
            """
            """
            i = lo
            j = hi+1

            while i < j:
                while i < hi:
                    i+=1
                    if arr[i] >= arr[lo]:
                        break
                while j > lo:
                    j -=1
                    if arr[j] <= arr[lo]:
                        break
                if i>=j:
                    break
                arr[i], arr[j]= arr[j], arr[i]
            arr[lo], arr[j] = arr[j], arr[lo]
            return j
        k = len(nums) - k
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            j = partition(nums, lo, hi)
            if j == k:
                return nums[j]
            elif j > k:
                hi = j - 1
            else:
                lo = j + 1
        return nums[lo]




```

第二题

sort其中短的那个数组,然后one pass长的数组 在sort完的短素族里面binary search。

MlogN + NlogN

都sort后双指针
MlogM + NlogN + M+N

```java

```



### 2. mst

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz1fr4hb33j30tq0eo1kx.jpg)
![](https://ws4.sinaimg.cn/large/006tNc79ly1fz1futozyvj30ss0drqps.jpg)

Similar with leetcode 465

https://leetcode.com/problems/optimal-account-balancing/

```python


from collections import defaultdict
class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """

        debt = defaultdict(int)

        for give, take, val in transactions:
            debt[give] += val
            debt[take] -= val

        debt = debt.values()
        print(debt)

        def helper(start, debt):
            while start < len(debt) and debt[start] == 0:
                start += 1

            if start == len(debt):
                return  0

            res = float('inf')
            for i in range(start+1, len(debt)):
                if debt[i] * debt[start] < 0:
                    debt[i] += debt[start]
                    res = min(res, helper(start+1, debt)+1)
                    debt[i] -= debt[start]
            return res

            pass

        res = helper(0, debt)
        print(res)
        return res

```

### 1. merge two linked list

https://leetcode.com/problems/merge-two-sorted-lists/description/

```java

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(-1);

        ListNode head = dummy;

        while( l1 != null && l2 != null){
            if(l1.val < l2.val){
                head.next = l1;
                l1 = l1.next;
            } // END of if
            else{
                head.next = l2;
                l2 = l2.next;
            }

            head = head.next;


        } // END of while

        if(l1 == null){
            head.next = l2;
        } // END of if
        else{
            head.next = l1;
        }
        return dummy.next;
    }
}

```
