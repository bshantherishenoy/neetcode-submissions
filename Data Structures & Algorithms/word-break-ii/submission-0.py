class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        def backtrack(index,path):
            if index == len(s):
                result.append(" ".join(path))
                return
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]

                if word in wordDict:
                    # choose
                    path.append(word)

                    # explore
                    backtrack(end, path)

                    # undo
                    path.pop()
                    
        backtrack(0,[])
        return  result 
        