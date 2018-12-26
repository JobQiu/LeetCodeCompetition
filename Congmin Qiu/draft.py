class Solution:
    def slove(self, n, s, k):
        pass


s = Solution()
input = "1 1 1 1 1 2 2 2 2 2 3 3 3 3 3"
kk = 6
res = s.slove(100, input, 30)

nums = [int(s) for s in input.split(" ")]
nums.sort()
print("")
res = []
count = 0
for i in range(len(nums) - 2):

    #if i > 0 and nums[i] == nums[i - 1]:
    #    continue
    j = i + 1
    k = len(nums) - 1


    while j < k:

        sum_ = sum([nums[i], nums[j], nums[k]])
        print("{} + {} + {} = {}".format(nums[i], nums[j], nums[k], sum_))
        if sum_ > kk:
            k -= 1
        elif sum_ < kk:
            j += 1
        else:
            res.append((nums[i], nums[j], nums[k]))
            count += 1

            if nums[j] == nums[k]:
                import math
                count += math.factorial(k-j-1)



            j += 1

print("")

