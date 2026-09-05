class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i,j))
        directions = [
            (1,0),
            (-1,0),
            (0,-1),
            (0,1)
        ]
        while queue:
            r,c = queue.pop(0)
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))




      


