class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start, subset, total):
            if target  == total:
                result.append(subset.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1, subset, total + candidates[i])
                subset.pop()
        backtrack(0,[],0)
        return result
