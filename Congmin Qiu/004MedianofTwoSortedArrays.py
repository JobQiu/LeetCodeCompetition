class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # 1. be sure nums1 is shorter than nums2
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        l1 = len(nums1)
        l2 = len(nums2)

        if l1 == 0:
            return nums2[l2 // 2] if l2 % 2 == 1 else (nums2[l2 // 2 - 1] + nums2[l2 // 2]) / 2.0

        half_length = (l1 + l2) // 2

        '''
        take [2] and [1,3] as an example, half_length = 1
        start to search in nums1
        '''

        l = 0
        r = l1

        while l <= r:
            # iter = 1, l = 0, r = 0
            ind_1 = (l + r) // 2  # 0
            ind_2 = half_length - ind_1  # 1

            if ind_1 > 0 and nums1[ind_1 - 1] > nums2[ind_2]:
                r = ind_1 - 1
            elif ind_1 < l1 and nums1[ind_1] < nums2[ind_2 - 1]:
                l = ind_1 + 1
            else:
                if ind_1 == l1:  # all number in nums1 is belong to left
                    right_smallest = nums2[ind_2]
                elif ind_2 == l2:  # all number in nums2 is belong to left
                    right_smallest = nums1[ind_1]
                else:
                    right_smallest = min(nums1[ind_1], nums2[ind_2])
                if (l1 + l2) % 2 == 1:
                    return right_smallest

                if ind_1 == 0:  # all number in nums1 is belong to right
                    left_biggest = nums2[ind_2 - 1]
                elif ind_2 == 0:  # all number in nums2 is belong to right
                    left_biggest = nums1[ind_1 - 1]
                else:
                    left_biggest = max(nums1[ind_1 - 1], nums2[ind_2 - 1])
                return (right_smallest + left_biggest) / 2.0


s = Solution()

nums1 = [3, 4]
nums2 = [1, 2]

res = s.findMedianSortedArrays(nums1, nums2)
assert res == 2.5

nums1 = [1]
nums2 = [1]

res = s.findMedianSortedArrays(nums1, nums2)
assert res == 1.0

nums1 = []
nums2 = [1, 2]

res = s.findMedianSortedArrays(nums1, nums2)
assert res == 1.5
