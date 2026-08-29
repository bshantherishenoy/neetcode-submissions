import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create the adjacency list
        graph = {}
        dist = [[float('inf')] * (k + 5) for _ in range(n)]
        for s,d,cost in flights:
            if s not in graph:
                graph[s] = [(d, cost)]
            else:
                graph[s].append((d, cost))
 
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        heap = [(0, src, 0)]
        while heap :
     
            mincost, cur_node, stops = heapq.heappop(heap)
          
            if cur_node == dst:
                return mincost
            if stops > k:
                continue          
            for dest, cost in graph.get(cur_node, []):
                newcost = mincost + cost
                newstops = stops+1
                if newcost < dist[dest][newstops]:
                    dist[dest][newstops] = newcost
                    heapq.heappush(heap,(newcost, dest, newstops))

        return -1

        