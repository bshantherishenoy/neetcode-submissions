class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def dfs(i, j):
            
            if i == len(word1):
                return len(word2) - j 
            if j == len(word2):
                return len(word1) - i 
            if (i,j) in mem:
                return mem[(i,j)]
            if word1[i] == word2[j]:
                mem[(i,j)] = dfs(i+1, j+1)
            else:
                delete = dfs(i,j+1)
                insert =  dfs(i+1,j)
                update = dfs(i+1,j+1)
                mem[(i,j)] =  1+ min(delete,insert,update)
            return mem[(i,j)]
        return dfs(0,0)