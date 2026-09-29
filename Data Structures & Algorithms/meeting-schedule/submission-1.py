"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals_new = []
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            intervals_new.append([start,end])
        intervals_new.sort()
        result = [intervals_new[0]]

        for start, end in intervals_new[1:]:
            last_end = result[-1][1]

            if start < last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start,end])
        return len(result) == len(intervals)
    
