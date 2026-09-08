class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for j in range(n)] for i in range(m)]
        def dfs(r, c):
            nonlocal table
            if not (0 <= r < m and 0 <= c < n):
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if table[r][c] != 0:
                return table[r][c]
            # Calculate and store
            table[r][c] = dfs(r + 1, c) + dfs(r, c + 1)

            return table[r][c]
        return dfs(0,0)

        