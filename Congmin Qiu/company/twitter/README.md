# Fighting for TuiTui!


## 1. 给你一个sorted 全是整数的list，要你返回平方后的list并且依旧保持sorted [skip]
eg: [-4, 0, 1,2,3,4] => [1,4,9,16]
数字可以为负

solution:

1. find the insert position of 0, O(logN)
2. use two pointer from insert position of 0 to the two sides. scan and put the result into the result list. O(N)

The overall time is O(N). Space is also O(N) consider the space for the result.

```python
def insertPos( arr, target):
    """
    what should I do is the arr contains duplicate numbers?
    [1] if the arr are all integers, we can search 3.5 for target = 4
    [2] if the arr contains float, we have to find the first result,
        and check its left until not same
    assume this arr doesnot contains duplicate number and is sorted, and
    2 3 4 6 7 8
    search insertpos of 4, and 5
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right ) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid+1
    return left

arr = [2, 3, 4, 5,7,8,9]
for num in range(10):
    res = insertPos(arr, num)
    print("insert ", num, " into ", arr , " result is " , res)
```

for this problem, you can just start from 0 to the first positive,

```python

arr = [-3, -2, -1, 0, 4, 7,9]
for j in range(len(arr)):
    if arr[j] >= 0:
        break
print(j)

k = j-1
res = []
while k >= 0 and j < len(arr):
    if arr[k] + arr[j] >= 0:
        res.append(arr[k]**2)
        k -= 1
    else:
        res.append(arr[j]**2)
        j += 1

if k == -1:
    while j < len(arr):
        res.append(arr[j]**2)
        j += 1
else:
    while k>=0:
        res.append(arr[k]**2)
        k -= 1
res
```

## 2. Find Kth smallest element in array [need redo]

quick select, O(N) time,

```python
import random
def kthsmall(arr, k):
    """
    arr is not sorted
    """

    # shuffle the arr to keep the performance.
    random.shuffle(arr)
    print(arr)

    def partition(arr, left, right):
        print("partition ", arr[left: right+1])
        # arr[left] is the pivot
        i = left
        j = right + 1

        while i < j:
            while i < right:
                i += 1
                if arr[i] > arr[left]:
                    break
            while j > left:
                j -= 1
                if arr[j] < arr[left]:
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        arr[left], arr[j] = arr[j], arr[left]
        print(arr)
        return j
    k = k-1
    i = 0
    j = len(arr)-1

    while i< j:
        pivot = partition(arr, i, j)
        if pivot == k:
            break
        if pivot > k:
            j = pivot-1
        else:
            i = pivot+1
    return arr[k]


arr = [1,53,23,12,3,54,6,34,4,123,13]
res = kthsmall(arr, 5)
res
```

## 3. 把一个tweet中的所有链接加上HTML的<a> tag [skip]
比如:
Input: this is a twitter link http://twitter.com/twittertest
Output: this is a twitter link <a href="http://twitter.com/twittertest">http://twitter.com/twittertest</a>

several solutions,
1. use reg expression
2. iterate all the words and check if start with http, if so, replace, time is O(N)


## 4. trap rain water

## 5. find super prime with n digit

Super prime是一个prime, 而且所有prefix也是prime. 比如7331是super prime, 因为7, 73, 733, 7331都是prime.
方法就是brutal force search + pruning, 比如第一个digit必须是2, 3, 5, 7, 后面的digit必须是奇数.
然后实现boolean isPrime(int)函数, 参考CTCI.


while number is larger than 0,
  check if it's prime,
  if not, return  False
  number = number / 10
return True



---
