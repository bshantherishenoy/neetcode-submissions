from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])
        @lru_cache(None)
        def dfs(r, c):

            # destination
            if r == R - 1 and c == C - 1:
                return grid[r][c]

            # only one direction possible: down
            if c == C - 1:
                return grid[r][c] + dfs(r + 1, c)

            # only one direction possible: right
            if r == R - 1:
                return grid[r][c] + dfs(r, c + 1)

            # both directions possible
            min_down = dfs(r + 1, c)
            min_right = dfs(r, c + 1)

            return grid[r][c] + min(min_down, min_right)

        return dfs(0, 0)

        


