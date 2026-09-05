class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
        dis = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        count = 0
        def check_all_rotten():
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 1:
                        return False
            return True
        while queue:
            for _ in range(len(queue)):
                r,c = queue.pop(0)
                for dx,dy in dis:
                    nx = r + dx
                    ny = c + dy
                    if 0<=nx<row and 0<=ny<col and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
            count +=1
            
        if check_all_rotten():
            return max(0, count - 1)
        else:
            return -1
        
                    
        