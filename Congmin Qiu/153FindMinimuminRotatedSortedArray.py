def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] < nums[r]:
            return nums[l]
        mid = (l + r) // 2
        if nums[mid] > nums[l]:
            l = mid + 1
        elif nums[mid] <= nums[l]:
            r = mid
    return nums[l]
    pass


nums = [3, 4, 5, 1, 2]
# assert findMin(nums) == 1

nums = [4, 5, 6, 7, 0, 1, 2]

assert findMin(nums) == 0
