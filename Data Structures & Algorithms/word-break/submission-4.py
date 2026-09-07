class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        mem = {}
        def check(start, end) -> bool:
            if start == n:
                return True
            if start in mem:
                return mem[start]
            for i in range(start, end):
                substring = s[start:i+1]
                if substring in wordDict:
                    result = check(i+1, end)
                    if result:
                        mem[substring] = result
                        return mem[substring]
            mem[start] = False
            return False 
        return check(0,n )

        