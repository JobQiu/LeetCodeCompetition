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


nums = [1, 3, 2, 6, 8, 7, 9, 4]
nums.sort()

for i in range(11):
    print(binarySearch(nums, i))
