def firstMissingPositive(nums):
    l = len(nums)
    for i in range(l):

        if nums[i] < 1 or nums[i] > l:
            continue
        else:
            while nums[i] != i + 1 and nums[i] >= 1 and nums[i] <= l:
                if nums[nums[i] - 1] == nums[i]:
                    break
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp

    for i in range(l):
        if nums[i] != i + 1:
            return i + 1
    return l + 1


nums = [1, 2, 0]
res = firstMissingPositive(nums)
assert res == 3

nums = [3, 4, -1, 1]
res = firstMissingPositive(nums)
assert res == 2

nums = [7, 8, 9, 11, 12]
res = firstMissingPositive(nums)
assert res == 1

nums = [1, 1]
res = firstMissingPositive(nums)
assert res == 2
