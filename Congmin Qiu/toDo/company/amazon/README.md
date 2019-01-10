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

```java

```

第二题：给一个text的string和一个excluded words的list， 要求统计text中单词的词频，输出不在excluded words中的词频最大的单词(有tie要输出所有)
这道题有两个细节：1）不区分大小写 2）所有不是字母的char都看成space，例如“ben‘s car“里有"ben", "s"和"car"三个单词。
方法就是一个hashset存excluded word， 一个hashmap存单词词频，然后扫一遍text就行了。

lc819

https://leetcode.com/problems/most-common-word/description/

```java

```

### 4. 2019 Jan两道

https://www.1point3acres.com/bbs/thread-469583-1-1.html


<img src="https://www.1point3acres.com/bbs/data/attachment/forum/201901/07/093147l4l4ikkob6qbb4l9.jpg" width="550px"/>

```java

```

<img src="https://www.1point3acres.com/bbs/data/attachment/forum/201901/07/093146lfi2f568afqdqd5w.jpg" width="550px"/>

本质是最近的K个点，下面有quick的code

return List<List<Integer>>


```java

```

2.第二题是0代表空地，1代表building， 9代表obstacle，最短距离。

停车场里找obstable最短路径的题目。这题难度高一点，但只要会BFS，基本无难度。。。只是最后记得没找到obstacle要返回-1，不然只会过12个test case。加了这行就16


### 3. 2018 DEC两题

https://www.1point3acres.com/bbs/thread-468910-1-1.html


![](https://ws3.sinaimg.cn/large/006tNc79ly1fz1g2m3140j31sg03kwgj.jpg)

第一题 可以参考 https://leetcode.com/problems/kth-largest-element-in-an-array/description/

```java

# quick select



```

第二题

sort其中短的那个数组,然后one pass长的数组 在sort完的短素族里面binary search。

MlogN + NlogN

都sort后双指针
MlogM + NlogN + M+N

```java

```



### 2. 类似LC465

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz1fr4hb33j30tq0eo1kx.jpg)
![](https://ws4.sinaimg.cn/large/006tNc79ly1fz1futozyvj30ss0drqps.jpg)

Similar with leetcode 465

https://leetcode.com/problems/optimal-account-balancing/

```java

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
