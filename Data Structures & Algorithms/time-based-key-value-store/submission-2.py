from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store= defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        left, right= 0, len(values)-1
        ans = ""
        while left<= right:
            mid = (left+right)//2
            if values[mid][0] <= timestamp:
                ans = values[mid][1]
                left +=1
            else:
                right -=1
        return ans
