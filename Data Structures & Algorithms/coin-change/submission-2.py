class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}

        def dfs(cur_amount):

            if cur_amount == 0:
                return 0

            if cur_amount < 0:
                return float('inf')

            if cur_amount in mem:
                return mem[cur_amount]

            min_coins = float('inf')

            for coin in coins:
                result = dfs(cur_amount - coin)

                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            mem[cur_amount] = min_coins

            return min_coins

        result = dfs(amount)

        if result == float('inf'):
            return -1

        return result