
class Solution:
  def canCross(self, stones):
    """
    :type stones: List[int]
    :rtype: bool

    [0,1,3,5,6,8,12,17]
    """

    if stones is None or len(stones) <= 1:
        return  True



    num2k = {} # 1 ->{1}
    for num in stones:
        num2k[num] = {}
    num2k[1].add(1);


    for i in range(1, len(stones)):
        for k in num2k[stones[i]]:
            if stones[-1] in [stones[i] + k-1, stones[i] + k,stones[i] + k+1]:
                return  True
            if k-1>0 and stones[i] + k-1 in num2k:
                num2k[stones[i] + k-1].add(k-1)
            if stones[i] + k in num2k:
                num2k[stones[i] + k].add(k)
            if stones[i] + k + 1 in num2k:
                num2k[stones[i] + k + 1].add(k+1)
    return  False
