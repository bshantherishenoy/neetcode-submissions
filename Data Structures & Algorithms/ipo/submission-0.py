class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = sorted(zip(capital,profits))
        i = 0

        for _ in range(k):
            while i<len(projects) and projects[i][0] <= w:
                c,p = projects[i]
                heapq.heappush(heap,-p)
                i+=1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w
