class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = {}
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0 
            if (i,j) in mem:
                return mem[(i,j)]
            count = 0
            # take the word
            if s[i] == t[j]:
                count += dfs(i+1, j+1)
            # skip the word
            count += dfs(i+1,j)
            mem[(i,j)] =count 
            return mem[(i,j)]

        return dfs(0,0)