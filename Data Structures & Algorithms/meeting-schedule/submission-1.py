"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        n = max([x.end for x in intervals])
        res = [False] * (n+1)
        for interval in intervals:
            start = interval.start
            end = interval.end
            for i in range(start, end):
                if res[i] == True:
                    return False
                res[i] = True
        return True