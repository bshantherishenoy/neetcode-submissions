class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = {}
        def dfs(total,i):
            if total == amount:
                return 1
            if total > amount:
                return 0 
            if (total,i) in mem:
                return mem[(total,i)]
            count = 0 
            for j in range(i,len(coins)):
                count += dfs(total+coins[j],j)
                mem[(total, i)] = count 
            return mem[(total, i)]
       
        return  dfs(0,0)