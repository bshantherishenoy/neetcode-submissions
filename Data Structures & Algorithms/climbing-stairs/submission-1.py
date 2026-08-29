class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0 
        mem = {}
        def dfs(num):
            if num > n:
                return 0
            if num == n:
                return 1
            if num in mem:
                return mem[num]
            mem[num] = dfs(num+1) + dfs(num+2)
            return mem[num]
    
        return dfs(0)

        