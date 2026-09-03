class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        mem = {}
        count = 0
        for i in range(n):
            for j in range(i, n):
                string = s[i:j+1]
                if string in mem:
                    if mem[string]:
                        count +=1
                else:
                    if string == string[::-1]:
                        mem[string] = True
                        count +=1
                    else:
                        mem[string] = False
        return count  
        