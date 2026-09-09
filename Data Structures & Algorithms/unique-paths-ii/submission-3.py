class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # change the 1 to -1 
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def dfs(r,c):
            if not (0<=r<m and 0<=c<n ):
                return 0 
            
            if obstacleGrid[r][c] == -1:
                return 0

            if r == m-1 and c == n-1:
                return 1
        
            if obstacleGrid[r][c] >0 :
                return obstacleGrid[r][c] 
            obstacleGrid[r][c] = dfs(r,c+1) + dfs(r+1,c)
            return obstacleGrid[r][c]
        return dfs(0,0)
        