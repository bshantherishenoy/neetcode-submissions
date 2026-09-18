class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        R = len(matrix)
        C = len(matrix[0])
        memory = {}
        def dfs(i,j):
            longest = 1 
            if (i,j) in memory:
                return memory[(i,j)]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if  0<= nx < R and 0<= ny < C and matrix[i][j] < matrix[nx][ny]:
                    longest = max(longest, 1+dfs(nx,ny))
            memory[(i,j)] = longest 
            return memory[(i,j)]

        ans = 0 
        for i in range(R):
            for j in range(C):
                ans = max(ans, dfs(i,j))
        return ans

        