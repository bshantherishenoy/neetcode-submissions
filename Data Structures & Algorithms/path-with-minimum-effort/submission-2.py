import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        effort = [[float('inf') for i in range(cols)] for j in range(rows)]
        heap = [(0,0,0)]
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        while heap:
            cur_effort ,r,c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return cur_effort
            if cur_effort > effort[r][c]:
                continue
            for i in range(4):
                dr,dc = directions[i]
                nr = r + dr
                nc = c + dc
                if 0<= nr <rows and 0<= nc <cols:
                    edge_cost = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(cur_effort, edge_cost)
                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort,nr,nc))
        return 0