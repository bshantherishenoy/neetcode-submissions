class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort()
        result = [intervals[0]]
        count = 0
        for start, end in intervals[1:]:
            last_end = result[-1][1]

            if start < last_end:
                result[-1][1] = min(last_end, end)
                count +=1
            else:
                result.append([start,end])
        
        return count  