# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # boundary case
        if len(intervals) == 0:
            return []

        ret = []

        # sort the intervals
        # 1) by start
        # 2) by end
        intervals = sorted(intervals, key=lambda i: (i.start, i.end))

        current_start, current_end = None, None
        for interval in intervals:
            if current_start == None:
                current_start, current_end = interval.start, interval.end
            else:
                if interval.start <= current_end:
                    current_end = max(current_end, interval.end)
                else:
                    ret.append(Interval(current_start, current_end))
                    current_start, current_end = interval.start, interval.end
        ret.append(Interval(current_start, current_end))
        return ret
