class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (a,b), value in zip(equations, values):
            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        
        def dfs(node, target, visited):
            if node == target:
                return 1
            visited.add(node)
            for  neighbour , weight in graph[node]:
                if neighbour in visited:
                    continue
                result = dfs(neighbour,target,visited)
                if result != -1:
                    return weight * result 
            return -1
        answer = []
        for start, end in queries:

            if start not in graph or end not in graph:
                answer.append(-1.0)
                continue

            visited = set()

            result = dfs(start, end, visited)

            answer.append(result)

        return answer
