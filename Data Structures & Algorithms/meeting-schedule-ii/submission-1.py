"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        ini, end = list(), list()

        for interval in intervals:
            ini.append(interval.start)
            end.append(interval.end)

        ini.sort()
        end.sort()

        l, ans = 0, 0

        for r in range(len(intervals)):
            if ini[r] < end[l]: ans += 1
            else: l += 1

        return ans
