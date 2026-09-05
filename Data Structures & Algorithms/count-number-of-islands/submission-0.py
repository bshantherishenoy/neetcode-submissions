class Solution:
    def numIslands(self, graph: List[List[str]]) -> int:
        count = 0
        m = len(graph)
        n = len(graph[0])
        def isvalid(r,c,graph) -> bool:
            if 0<=r<m and 0<=c<n and graph[r][c] == "1":
                return True
            return False
        def dfs(r, c , graph) -> None:
            if isvalid(r,c,graph):
                # mark as visited
                graph[r][c] = "0"
                dfs(r-1,c,graph)
                dfs(r+1,c,graph)
                dfs(r,c-1,graph)
                dfs(r,c+1,graph)

        for i in range(m):
            for j in range(n):
                if graph[i][j] == "1":
                    dfs(i,j,graph)
                    count +=1
        return count 