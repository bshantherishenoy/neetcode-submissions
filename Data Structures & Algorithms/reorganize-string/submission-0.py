from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        prevCount = 0
        prevChar = ""
        count = Counter(s)
        heap = []
        for k, v in count.items():
            heapq.heappush(heap,(-v,k))
        while heap:
            freq, ele = heapq.heappop(heap)
            if prevCount < 0:
                heapq.heappush(heap,(prevCount, prevChar))
            freq += 1
            ans += ele
            prevChar = ele
            prevCount = freq
        if prevCount < 0:
            return ""
        return ans
        