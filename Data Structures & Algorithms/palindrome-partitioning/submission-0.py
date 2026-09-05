class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def ispallindrome(word:str)->bool:
            if word == word[::-1]:
                return True 
            else:
                return False
        def backtrack(start, subset):
            if start == len(s):
                result.append(subset.copy())
                return 
            for end in range(start,len(s)):
                substring = s[start:end+1]
                if ispallindrome(substring):
                    subset.append(substring)
                    backtrack(end+1, subset)
                    subset.pop()
        backtrack(0,[])
        return result
