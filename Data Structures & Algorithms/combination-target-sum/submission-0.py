class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start, subset, total):
            if target == total:
                result.append(subset.copy())
                return
            if total > target:
                return 
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i, subset, total + nums[i])
                subset.pop()

        backtrack(0,[],0)
        return result