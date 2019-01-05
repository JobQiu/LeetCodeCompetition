class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        for example, 19:35 - > 19:39
        since 9 is larger then 5, so it will be replaced with 9

        """

        nums = [ch for ch in time if ch != ":"]
        nums.sort()
        min_ = nums[0]

        for num in nums:
            if num > time[4]:
                return time[:4] + num

        for num in nums:
            if num > time[3] and (num + min_) < "60":
                return time[:3] + num + min_

        for num in nums:
            if num > time[1] and (time[0] + num) < "24":
                return time[0] + num + ":" + min_*2

        for num in nums:
            if num > time[0] and (num + min_) < "24":
                return num + min_ + ":" + min_ * 2

        return  min_  * 2 + ":" +  min_  * 2
