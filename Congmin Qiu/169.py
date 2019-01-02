class Solution:
    def method(self, A ):
        num = A[0]
        count =1

        for i in range(1, len(A)):
            if A[i]== num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num = A[i]
                    count = 1
        return  num
        pass

s = Solution()
input = None
res = s

print("")
