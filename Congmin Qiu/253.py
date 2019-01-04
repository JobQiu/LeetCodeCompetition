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

        starts = []
        ends = []

        for interval in intervals:
            starts. append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()

        count = 0
        endInd = 0

        for num in starts:
            if num < ends[endInd]:
                count += 1
            else:
                endInd+=1
        return count
