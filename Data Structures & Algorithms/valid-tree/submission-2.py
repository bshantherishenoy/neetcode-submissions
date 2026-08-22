class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        for i, j in edges:
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)
        visited = [False] * n 
        def dfs(node, parent):
            visited[node] = True
            for neg in graph.get(node, []):
                if visited[neg] == False:
                    if dfs(neg, node):
                        return True
                elif neg != parent:
                    return True
            return False
        if dfs(0,-1):
            return False
        return all(visited)
            


        