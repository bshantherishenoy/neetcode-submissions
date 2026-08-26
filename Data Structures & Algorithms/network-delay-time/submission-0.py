import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}
        for u,v,w in times:
            if u not in edges:
                edges[u] = [(v,w)]
            else:
                edges[u].append((v, w))
        minheap = [(0,k)]
        visited = set()
        t = 0 
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = w1
            for n2,w2 in edges.get(n1,[]):
                if n2 not in visited:
                    heapq.heappush(minheap, (w1+w2,n2))
        return t if len(visited) == n else -1
        