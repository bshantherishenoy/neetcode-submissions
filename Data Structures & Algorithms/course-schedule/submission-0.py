class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i, j in prerequisites:
            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)
        visited = set ()
        path = set()
        def dfs(node):
            if node in path:
                return True
            if node in visited:
                return False
            visited.add(node)
            path.add(node)
            for neg in graph.get(node, []):
                if dfs(neg):
                    return True
            path.remove(node)
            return False
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
        