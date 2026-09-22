class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        mem = {}

        def dfs(i, j):

            if (i, j) in mem:
                return mem[(i, j)]

            if j == len(p):

                if i == len(s):
                    return True
                else:
                    return False

            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                match = True
            else:
                match = False

            if j + 1 < len(p) and p[j + 1] == '*':

                # Option 1: skip x*
                if dfs(i, j + 2):
                    mem[(i, j)] = True
                    return True

                # Option 2: use x*
                if match:
                    if dfs(i + 1, j):
                        mem[(i, j)] = True
                        return True

                mem[(i, j)] = False
                return False

            if match:
                ans = dfs(i + 1, j + 1)
                mem[(i, j)] = ans
                return ans

            mem[(i, j)] = False
            return False

        return dfs(0, 0)