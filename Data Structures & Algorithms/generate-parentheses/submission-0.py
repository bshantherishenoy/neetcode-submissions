class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(subset):
            if len(subset) == 2*n:
                result.append("".join(subset))
                return
            if subset.count("(") < n:
                subset.append("(")
                backtrack(subset)
                subset.pop()
            if subset.count(")") < subset.count("("):
                subset.append(")")
                backtrack(subset)
                subset.pop()
        backtrack([])
        return result


        