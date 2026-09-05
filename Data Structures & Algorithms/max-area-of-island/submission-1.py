class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_grid = 0
        def isvalid(r,c, graph):
            if 0<=r<rows and 0<=c<cols and graph[r][c] == 1:
                return True
            else:
                return False
        def dfs(r,c,grid):
            if isvalid(r,c,grid):
                grid[r][c] = 0
                return 1 + dfs(r+1,c,grid)+dfs(r,c+1,grid)+dfs(r-1,c,grid)+dfs(r,c-1,grid)
            else:
                return 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count = dfs(i,j,grid)
                    max_grid = max(max_grid, count )
        return max_grid
    

        