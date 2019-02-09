


https://www.1point3acres.com/bbs/thread-295357-1-1.html

Akuna Capital海投拿到的OA， 它家只要海投都有OA，楼主申请的quantitative developer的OA一共120分钟，3题
1. LAMP， 给你矩阵的长宽，起始点，和相对位置，从起始点开始关灯，所有相连位置都要关灯，最后返回亮灯的数目
2. 难到炸的polygon题，完全没有思路，如果有想法的小伙伴可以一起分享一下~有m个多边形，每个多边形有n条边，每条边可以有k中染色方式，求从多边形中取出两个多边形，染色相同的概率，另如果rotate之后染色相同也算相同，但不能翻折
3. 求标准差，输出保留4位小数. check 1point3acres for more.

攒人品！GOOD LUCK!

https://www.1point3acres.com/bbs/thread-309729-1-1.html

1. Market Equilibriu
2. 俄罗斯方块填满给定矩形
3. 统计合法单词+字母


https://www.dropbox.com/s/yji7sfjul0jmcps/Akuna_Capital_Questions.pdf?dl=0


## 2018-8-22

https://www.1point3acres.com/bbs/thread-439229-1-1.html

第一题：
规定四条交易策略（低买高卖等，题目非常长），given a list of stock price as input, write a function to compute the profit/loss given the above strategy & assumptions.

第二题：
给定一串数和target integer，return sum 最接近target integer的一串连续数列的index。. check 1point3acres for more.
基本上是这道题：https://rafal.io/posts/subsequence-closest-to-t.html

第三题：
给定一个二维空间里的三角形，要求输出三角形内部或边界上的整数点，which has the minimum sum of distance from 三个顶点。. check 1point3acres for more.

求


## 2016-10-5

https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=200665

1.两个流水线,一个是Box,一个是Melon.每个都有大小,如果Box比对应的Melon大就能装下它,一个box只能装一个melon.可以自己melon选起始点,然后开始装.box可以skip,但是melon不行,问最多装多少melon.
2.给一个空格分开的句子,单词是小写字母的序列,统计单词个数和每个字母个数.蛋疼之处在于有非法输入,但是如何handle非法输入题目写的不清楚,反正试了很多种不同方法都有个数据点过不了.
3.给n个股票交易信息和对应label,每个交易信息包含3维特征float[0,100],对应利润,风险,延迟.然后给你了m个测试数据,也是三维的特征,让你预测它们的label.注意训练数据中label的分布不是平衡的,然后n大概是m的10倍.
4.机器人运输系统,每个grid有50个home,home标号为1-50,于是每个home可以由gridId-homeId唯一地表示.你有几个机器人,每个机器人只能去一个grid然后在1号home开始投递,投递\往+1方向移动一格\等待都需要1分钟.然后给你一个投递包裹列表,gridId-homeId这样的list,要求用户收到货的顺序必须严格按照表来.问最少多少分钟可以投递完成.


1. box and melon
2. count words
3. classify
4. drone
之前地里出现过，就不赘述了
第一题直接 brute force。。。第二题不知道有什么非法字符总有test case过不去，第三实现classifier? kNN? k-means?


## 2018-12-20

1. 3-card poker
2. chess game with knight
3. flipping


## \#6
第一题：也就是网上称为 valid parentheses 的题目，匹配大中小括号，给的例子是：Return true if passed a string: (), [], [(){}()[{}]], Return false if passed a string: (, ], (], ([)], [({}[]], {[}], }{. 整个string左右括号的数量和种类必须匹配，而且右括号出现时左边必须紧邻与之匹配的括号。这道题所有的 test cases 都过了，比较简短，网上现成思路很多


第二题：装西瓜，网上称为 watermelons in boxes，给的例子是：四个 boxes，每个的 size 是：[2, 1, 2, 2]，三个西瓜，每个 size 是：[2, 3, 2]。一个箱子只能放一个西瓜。可以选择任何一个西瓜开始（但不能循环，只能往右走），箱子必须从第一个开始，期间如果西瓜放不进某个箱子，可以等到下一个箱子再试。尽可能把更多的西瓜放进箱子。这个例子应该 return 的结果是2，因为第二个西瓜绝对放不进任何箱子。这道题所有的 test cases 都过了，也比较简短，网上的思路也很多


第三题：最难的一题，绳子圈石头，给一条固定长度的 ribbon，和几个 rocks 的平面坐标，用绳子来圈石头，看最多能圈多少石头进来（不是经过多少石头）。给的例子是：ribbon 长度是10，石头坐标：[[0,0], [0,3], [3,3]]。结果应该是2，绳子长度不够把3个全圈进来。这道题分两个步骤：一，把现有石头全圈起来，算周长有多少；二，如果周长超过 ribbon，怎么最优选定剔除一个石头。这两个步骤我做成了一个loop，直到最后周长不大于 ribbon 长度为止，return 最多圈进石头的数目。第一步的算法，网上称为 convex hull，这个思路和参照很多了，难的是如果周长 > ribbon，下一步如何通过 greedy 原则去掉一个石头，这个石头的去除可以最大限度的缩小余下石头 convex hull 的周长。这一步我纯粹自己写的，反正就是从上一个 loop 得出的最外一圈的点里最优选一个踢掉。最开始担心不能用 numpy，所以纯粹用 list 做的，写的又长又蠢，至少给的例子能过，然后就放上去算了，一共6个 test cases，没想到只有最后一个没过。其实我猜最后一个例子肯定是有关 k-means 的点分布，我的算法对于一堆没有明显 group 的点比较有效，但如果 test case 中的点分布成好几个明显分离较远的 groups，那么我的算法一定是会出错的，相信各位大能肯定一眼能看出问题在哪儿，肯定有更周全的解题方法。
