# Definition for an interval.

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        res = []
        if len(intervals) == 0:
            return [].append(newInterval)

        for i in range(len(intervals)):
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
            else:
                break

        start = newInterval.start
        end = newInterval.end

        for j in range(i, len(intervals)):
            if intervals[j].start > newInterval.end:
                res.append(Interval(start, end))
            else:
                start = min(start, intervals[j].start)
                end = max(end, intervals[j].end)

        for k in range(j, len(intervals)):
            res.append(intervals[k])

        return res


intervalsL = [[1, 3], [6, 9]]
newInterval = Interval(2, 5)
# intervalsL = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = Interval(4, 8)
# intervalsL = [[1, 5]]
# newInterval = Interval(2, 3)

intervals = []
for l in intervalsL:
    intervals.append(Interval(l[0], l[1]))

s = Solution()
s.insert(intervals, newInterval)


# %%


def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left = [i for i in intervals if i.end < s]
    right = [i for i in intervals if i.start > e]

    if left + right != intervals:
        s = min(s, intervals[len(left)].start)
        e = max(e, intervals[~len(right)].end)
    return left + [Interval(s, e)] + right
