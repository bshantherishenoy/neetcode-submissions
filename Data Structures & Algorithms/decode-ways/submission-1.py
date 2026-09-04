class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        mem = {}
        def dfs(i):
            nonlocal mem
            if i == n:
                return 1
            if i in mem:
                return mem[i]
            if s[i] == '0':
                return 0 
            ways = dfs(i+1)
            if i + 1 < n and int(s[i:i+2]) <= 26:
                ways+= dfs(i+2)
            mem[i] = ways
            return ways
        return dfs(0)