class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        map_digits = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if digits == "":
            return []
        def backtrack(index, subset):
            if index == len(digits):
                result.append("".join(subset))
                return 
            for letter in map_digits[digits[index]]:
                subset.append(letter)
                backtrack(index+1, subset)
                subset.pop()
        backtrack(0,[])
        return result
        