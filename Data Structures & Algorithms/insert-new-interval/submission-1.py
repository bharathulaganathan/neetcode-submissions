class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        newL, newR = newInterval
        start = -1
        insert = -1
        for i in range(n):
            l, r = intervals[i]
            if l <= newL <= r:
                newL = l
                start = i
                insert = i
                break
            if newL < l:
                insert = i
                break
        end = start
        for i in range(max(0,start),n):
            l, r = intervals[i]
            if l <= newR <= r:
                newR = r
                end = i
                break
            if newR < l:
                break
        if end == -1:
            end = n-1
        if start > -1:
            for _ in range(end+1-start):
                del intervals[start]
        intervals.insert(insert, [newL,newR])
        return intervals