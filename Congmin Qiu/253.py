# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]

        starts.sort()
        ends.sort()

        res = 1
        endIndex = 0


        for start in starts:
            if start < ends[endIndex]:
                res += 1
            else:
                endIndex +=1
        return res
