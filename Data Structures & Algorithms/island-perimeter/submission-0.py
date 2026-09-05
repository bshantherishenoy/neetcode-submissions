class Solution:
    def islandPerimeter(self, graph: List[List[int]]) -> int:
        row = len(graph)
        col = len(graph[0])
        def isvalid(r,c,graph):
            if 0<=r<row and 0<=c<col:
                return True
            return False
        def dfs(r,c,graph):
            if not isvalid(r,c,graph):
                return 1
            if graph[r][c]  == 0:
                return 1
            if graph[r][c] == -1:
                return 0
            graph[r][c] = -1
            return (
                dfs(r+1,c,graph) + dfs(r-1,c,graph) +dfs(r,c+1,graph)+dfs(r,c-1,graph)
            )
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if graph[i][j] == 1:
                    return dfs(i,j,graph)