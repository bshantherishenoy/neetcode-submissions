class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for v,e in edges:
            if v not in graph:
                graph[v] = [e]
            else:
                graph[v].append(e)
            if e not in graph:
                graph[e] = [v]
            else:
                graph[e].append(v)
        visited = [False] * n 
        def dfs(node):
            visited[node] = True 
            for neg in graph.get(node,[]):
                if not visited[neg]:
                    dfs(neg)
        count = 0 
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count +=1
        return count  
