class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        result = []
        def backtrack(subset, used):
            if len(subset) == len(nums):
                if subset not in result:
                    result.append(subset.copy())
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                subset.append(nums[i])
                used[i] = True
                backtrack(subset, used)
                subset.pop()
                used[i] = False
        backtrack([],used)
        return result
        