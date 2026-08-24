class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
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
        result = {}
        def dfs(node, visited):
            visited[node] = True
            height = 0
            for neg in graph.get(node,[]):
                if visited[neg] == False:
                    height =  max(height, 1+ dfs(neg, visited))
            return height
    
        for i in range(n):
            visited = [False]*n
            if visited[i] == False:
                height = dfs(i,visited)
                result.update({i:height})
        if len(result):
            minimum_height = min(result.values())
            mht = []
            for key, value in result.items():
                if value == minimum_height:
                    mht.append(key)
            return mht
        else:
            return [0]
