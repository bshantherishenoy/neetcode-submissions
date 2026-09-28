class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = result[-1][1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start,end])
        return result 

        