import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0,0)]
        visited = set()
        total = 0
        while heap:
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            visited.add(point)
            total += cost
            x1, y1 = points[point]
            for next_point in range(len(points)):
                if next_point not in visited:
                    x2,y2 = points[next_point]
                    distance = abs(x2-x1) + abs(y2-y1)
                    heapq.heappush(heap,(distance, next_point))
        return total