class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        count = 0 
        mem = {}
        n = len(cost)
        def dfs(num):
            if num >= n:
                return 0
            if num in mem:
                return mem[num]
            mem[num] = cost[num] + min(dfs(num+1),dfs(num+2))
            return mem[num]
    
        return min(dfs(0), dfs(1))
        