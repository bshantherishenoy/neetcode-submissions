import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        helper = {}
        x1 = 0
        y1 = 0
        heap = []
        for x2,y2 in points:
            distance  = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            if distance not in helper:
                helper[distance] = [[x2,y2]]
            else:
                helper[distance].append([x2,y2])
            heap.append(distance)
        print(helper)
        print(heap)
        ans = []
        heapq.heapify(heap)
        for i in range(k):
            nearest = heapq.heappop(heap)
            ans.append(helper[nearest].pop())
        return ans


        