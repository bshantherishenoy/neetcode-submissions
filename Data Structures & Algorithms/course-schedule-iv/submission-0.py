class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for i,j in prerequisites:
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
        
        def dfs(node):
            visited[node] = True
            for neg in graph.get(node,[]):
                if not visited[neg]:
                    dfs(neg)
        result = []
        for i, j in queries:
            visited = [False] * numCourses
            dfs(i)
            if visited[j] == False:
                result.append(False)
            else:
                result.append(True)
        return result 
            


        