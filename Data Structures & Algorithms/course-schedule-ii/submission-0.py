class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i, j in prerequisites:
            if j not in graph:
                graph[j] = [i] 
            else:
                graph[j].append(i)
        visited = set ()
        path = set()
        result = []
        def dfs(node):
            if node in path:
                return True
            if node in visited:
                return False
            path.add(node)
            visited.add(node)
            for neg in graph.get(node,[]):
                if dfs(neg):
                    return True
            path.remove(node)
            result.append(node)
            return False
        for i in range(numCourses):
            if dfs(i):
                return []
        result.reverse()
        return result
        



        