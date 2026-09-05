class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            i = 1

            while i * i <= target:
                dp[target] = min(
                    dp[target],
                    1 + dp[target - i * i]
                )
                i += 1

        return dp[n]
        
        
        