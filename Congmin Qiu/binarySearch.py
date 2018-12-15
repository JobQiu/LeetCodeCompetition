def binarySearch(nums, target):
    # l = 0
    # r = len(nums)-1
    #
    # while l <= r:
    #     mid = (l + r) // 2
    #     if nums[mid] < target:
    #         l = mid + 1
    #     elif nums[mid] > target:
    #         r = mid - 1
    #     else:
    #         return mid

    return -1


def insertPos(nums, target):
    l = 0
    r = len(nums)

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return l
    pass


nums = [1, 3, 2, 6, 8, 7, 9, 4]
nums.sort()
print(nums)

for i in range(11):
    print(insertPos(nums, i))
