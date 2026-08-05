import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # solution to check in k log n time 
        #  we store things that we need in heap
        # if the distance is to the origin there is no need to calulate the sqart
        heap = []
        for x,y in points:
            distance = x**2 + y**2 
            heapq.heappush(heap,(-distance, [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [points for d,points in heap]