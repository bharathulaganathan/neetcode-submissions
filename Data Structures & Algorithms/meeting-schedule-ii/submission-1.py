"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = max([i.end for i in intervals]) if intervals else 0
        res = [0] * (n+1)
        for i in intervals:
            s = i.start
            e = i.end
            for j in range(s,e):
                res[j] += 1
        return max(res)
        