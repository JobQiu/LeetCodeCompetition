## 1. Email + coupon, Feb 2019

![](https://ws4.sinaimg.cn/large/006tKfTcly1g09xy5jq7fj30la0o8n2j.jpg)


unique email address(lc 929)和coupon
第一题和LeetCode不太一样，要求返回number of most common email
第二题很简单，就是返回数组里出现两个重复元素时的subarray最短长度，比如[1, 2, 3, 1, 4, 5, 4, 6, 8], 1,2,3,1 和4,5,4出现了重复元素，返回最短length为 3 < 4


## 2.

![](https://ws2.sinaimg.cn/large/006tKfTcly1g09y0da5o4j30ly0po42c.jpg)

![](https://ws4.sinaimg.cn/large/006tKfTcly1g09y0pyl7hj30m50pq79u.jpg)

## 3.

{hide=120}1. distance，第k个最小值，给的是X和Y两个array； 2. chair，和lc meeting room一样， 给的是S和E两个array。{/hide}

## 4.

![](https://ws2.sinaimg.cn/large/006tKfTcly1g09y2t54xgj30sg0viq8e.jpg)

![](https://ws2.sinaimg.cn/large/006tKfTcly1g09y2zeypkj30se0w8gro.jpg)


比如对于[10,13,12,14,15]
1. 求出来每一个位置在奇&偶数步跳的下一个位置
e.g 这里13在奇数步的下个位置是14，在偶数步的下个位置是12
这里可以暴力做 应该是O（n^2)，也可以用平衡二叉树从后往前加节点，每次加好节点以后就找当前节点要跳的下个位置，存起来，应该O(nlogn)就可以了
2. 从后往前递归来看当前位置能不能跳到最后。
我这里构造了两个list，一个list是奇偶奇偶...这样能跳到最后的结果（1表示能0表示不能），一个list是偶奇偶奇...这样跳到最后的结果。结果就是第一个list里1的个数。这里就是用第1步我们算出来的矩阵从后往前递归就好。


## 5.


第一题：利口二幺雾近似。原点有一个modem，然后附近有一堆设备，给了他们的坐标，ceiling取整算距离后返回第K小的那个的距离。第二题：meetingroomII近似。有N个客人被邀请参加一个party，input是两个数组，分别是开始和结束时间，求需要几把椅子。

![](https://ws3.sinaimg.cn/large/006tKfTcly1g09y3v3tfej30u011x13x.jpg)

## 6.

https://www.1point3acres.com/bbs/thread-472621-1-1.html

第二题变成了Coupons: 给了一个Array存着coupon类型，每买一个花费一个金币，只有买到至少两个相同的才可以赢得奖金。问想要获得奖金最少花费多少。（买的时候必须按顺序购买，但可以不从第一个开始买起）

感觉第二题就是利口零零三的变种，求最小的non-repeating，然后加一。像lz说的一个hashmap

更准确的说法是sliding window

爆一个狗家的OA，依旧是面经题没有换，第一题unique email address，区别是要return most common address，我注意到这道题要求只考虑正确率
第二题是coupon题，最少的金币来pick至少两个相同的coupon，要求是efficient！

---
