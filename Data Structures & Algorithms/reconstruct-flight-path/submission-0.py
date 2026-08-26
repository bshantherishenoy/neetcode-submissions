import heapq
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for S,D in tickets:
            if S not in graph:
                graph[S] = []
            heapq.heappush(graph[S],D)
        result = []
        print(graph)
        def dfs(code):
            while graph.get(code,[]):
                next_airport = heapq.heappop(graph[code])
                dfs(next_airport)
            result.append(code)
        
        dfs("JFK")
        return result[::-1]
       